import argparse
import csv
import sqlite3
from pathlib import Path


DATASETS = {
    "customers": {
        "file": "customers.csv",
        "expected_headers": [
            "customer_id",
            "first_name",
            "last_name",
            "email",
            "signup_date",
            "city",
        ],
        "ddl": """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id   TEXT PRIMARY KEY,
            first_name    TEXT NOT NULL,
            last_name     TEXT NOT NULL,
            email         TEXT NOT NULL,
            signup_date   TEXT NOT NULL,
            city          TEXT NOT NULL
        );
        """,
        "insert": """
        INSERT OR REPLACE INTO customers (
            customer_id, first_name, last_name, email, signup_date, city
        ) VALUES (:customer_id, :first_name, :last_name, :email, :signup_date, :city);
        """,
    },
    "products": {
        "file": "products.csv",
        "expected_headers": [
            "product_id",
            "name",
            "category",
            "price",
            "cost",
            "currency",
        ],
        "ddl": """
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            name       TEXT NOT NULL,
            category   TEXT NOT NULL,
            price      REAL NOT NULL,
            cost       REAL NOT NULL,
            currency   TEXT NOT NULL
        );
        """,
        "insert": """
        INSERT OR REPLACE INTO products (
            product_id, name, category, price, cost, currency
        ) VALUES (:product_id, :name, :category, :price, :cost, :currency);
        """,
    },
    "orders": {
        "file": "orders.csv",
        "expected_headers": [
            "order_id",
            "customer_id",
            "order_date",
            "product_id",
            "quantity",
            "status",
            "total_amount",
        ],
        "ddl": """
        CREATE TABLE IF NOT EXISTS orders (
            order_id     TEXT PRIMARY KEY,
            customer_id  TEXT NOT NULL,
            order_date   TEXT NOT NULL,
            product_id   TEXT NOT NULL,
            quantity     INTEGER NOT NULL,
            status       TEXT NOT NULL,
            total_amount REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY(product_id)  REFERENCES products(product_id)
        );
        """,
        "insert": """
        INSERT OR REPLACE INTO orders (
            order_id, customer_id, order_date, product_id, quantity, status, total_amount
        ) VALUES (:order_id, :customer_id, :order_date, :product_id, :quantity, :status, :total_amount);
        """,
    },
    "inventory": {
        "file": "inventory.csv",
        "expected_headers": [
            "product_id",
            "warehouse",
            "stock_on_hand",
            "reorder_level",
            "last_restock_date",
            "in_transit",
        ],
        "ddl": """
        CREATE TABLE IF NOT EXISTS inventory (
            product_id        TEXT NOT NULL,
            warehouse         TEXT NOT NULL,
            stock_on_hand     INTEGER NOT NULL,
            reorder_level     INTEGER NOT NULL,
            last_restock_date TEXT NOT NULL,
            in_transit        INTEGER NOT NULL,
            PRIMARY KEY (product_id, warehouse),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        );
        """,
        "insert": """
        INSERT OR REPLACE INTO inventory (
            product_id, warehouse, stock_on_hand, reorder_level, last_restock_date, in_transit
        ) VALUES (:product_id, :warehouse, :stock_on_hand, :reorder_level, :last_restock_date, :in_transit);
        """,
    },
    "payments": {
        "file": "payments.csv",
        "expected_headers": [
            "payment_id",
            "order_id",
            "payment_date",
            "method",
            "amount",
            "status",
        ],
        "ddl": """
        CREATE TABLE IF NOT EXISTS payments (
            payment_id   TEXT PRIMARY KEY,
            order_id     TEXT NOT NULL,
            payment_date TEXT NOT NULL,
            method       TEXT NOT NULL,
            amount       REAL NOT NULL,
            status       TEXT NOT NULL,
            FOREIGN KEY(order_id) REFERENCES orders(order_id)
        );
        """,
        "insert": """
        INSERT OR REPLACE INTO payments (
            payment_id, order_id, payment_date, method, amount, status
        ) VALUES (:payment_id, :order_id, :payment_date, :method, :amount, :status);
        """,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load sample ecom CSVs into SQLite.")
    parser.add_argument(
        "--db",
        default="ecom.db",
        help="Path to SQLite database file (will be created if missing).",
    )
    parser.add_argument(
        "--data-dir",
        default="input_data",
        help="Directory containing the CSV files (default: input_data).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print extra logging while loading.",
    )
    return parser.parse_args()


def ensure_headers(path: Path, expected_headers: list[str]) -> None:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            raise ValueError(f"{path.name} is empty.")
    if headers != expected_headers:
        raise ValueError(
            f"Header mismatch in {path.name}.\n"
            f"Expected: {expected_headers}\n"
            f"Found:    {headers}"
        )


def load_csv(conn: sqlite3.Connection, dataset_key: str, data_dir: Path, verbose: bool) -> int:
    meta = DATASETS[dataset_key]
    csv_path = data_dir / meta["file"]
    ensure_headers(csv_path, meta["expected_headers"])

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with conn:
        conn.executemany(meta["insert"], rows)

    if verbose:
        print(f"Loaded {len(rows)} rows into {dataset_key}.")
    return len(rows)


def create_schema(conn: sqlite3.Connection) -> None:
    with conn:
        # Foreign keys are enforced only when enabled per-connection.
        conn.execute("PRAGMA foreign_keys = ON;")
        # Drop in reverse dependency order to keep reruns clean.
        conn.executescript(
            """
            DROP TABLE IF EXISTS payments;
            DROP TABLE IF EXISTS inventory;
            DROP TABLE IF EXISTS orders;
            DROP TABLE IF EXISTS products;
            DROP TABLE IF EXISTS customers;
            """
        )
        for meta in DATASETS.values():
            conn.executescript(meta["ddl"])
        # Helpful indexes for common lookups.
        conn.executescript(
            """
            CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
            CREATE INDEX IF NOT EXISTS idx_orders_product ON orders(product_id);
            CREATE INDEX IF NOT EXISTS idx_payments_order ON payments(order_id);
            """
        )


def main() -> None:
    args = parse_args()
    data_dir = Path(args.data_dir).resolve()
    db_path = Path(args.db).resolve()

    missing = [meta["file"] for meta in DATASETS.values() if not (data_dir / meta["file"]).exists()]
    if missing:
        missing_list = ", ".join(missing)
        raise FileNotFoundError(f"Missing CSV files in {data_dir}: {missing_list}")

    conn = sqlite3.connect(db_path)
    try:
        create_schema(conn)
        total = 0
        # Load in dependency order: customers -> products -> orders -> inventory -> payments
        for key in ["customers", "products", "orders", "inventory", "payments"]:
            total += load_csv(conn, key, data_dir, args.verbose)
    finally:
        conn.close()

    if args.verbose:
        print(f"Finished loading {total} rows into {db_path}")


if __name__ == "__main__":
    main()

