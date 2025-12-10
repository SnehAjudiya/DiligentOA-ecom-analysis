# Create e-commerce data for assessment
_Exported on 12/10/2025 at 15:42:37 GMT+5:30 from Cursor (2.1.50)_

---

**User**

I am working on the Online Assessment of Diligent Co. 

The 1st task is to generate synthetic ecom data of 5 files and no of rows should be 15-20 in each file.

The files can be customers, products, orders, inventory, payments.

No. of cols can be 5-6 in each table, you can give important col names and data.

The data should be related because in further steps i have to injest it into database and perform queries in sql

So perform this 1st step and make this files in my current folder properly according to my instructions





---

**Cursor**

```plaintext
customer_id,first_name,last_name,email,signup_date,city
C001,Alice,Johnson,alice.johnson@example.com,2024-01-12,New York
C002,Brian,Smith,brian.smith@example.com,2024-02-03,Chicago
C003,Carla,Ramirez,carla.ramirez@example.com,2024-02-17,Los Angeles
C004,David,Lee,david.lee@example.com,2024-03-05,San Francisco
C005,Emma,Williams,emma.williams@example.com,2024-03-22,Austin
C006,Felix,Brown,felix.brown@example.com,2024-04-01,Seattle
C007,Gina,Martinez,gina.martinez@example.com,2024-04-18,Miami
C008,Henry,Clark,henry.clark@example.com,2024-05-02,Denver
C009,Ivy,Nguyen,ivy.nguyen@example.com,2024-05-14,Boston
C010,Jacob,Davis,jacob.davis@example.com,2024-05-30,Portland
C011,Karen,Miller,karen.miller@example.com,2024-06-12,Atlanta
C012,Liam,Roberts,liam.roberts@example.com,2024-06-25,Minneapolis
C013,Mia,Thompson,mia.thompson@example.com,2024-07-07,Salt Lake City
C014,Noah,Anderson,noah.anderson@example.com,2024-07-21,Philadelphia
C015,Olivia,Garcia,olivia.garcia@example.com,2024-08-04,Dallas

```

```plaintext
product_id,name,category,price,cost,currency
P001,Wireless Mouse,Electronics,24.99,12.00,USD
P002,Mechanical Keyboard,Electronics,79.99,45.00,USD
P003,USB-C Charger,Electronics,19.99,8.50,USD
P004,Noise-Canceling Headphones,Electronics,129.99,70.00,USD
P005,4K Monitor,Electronics,329.00,220.00,USD
P006,Office Chair,Furniture,189.00,120.00,USD
P007,Standing Desk,Furniture,399.00,250.00,USD
P008,Notebook Pack,Stationery,9.99,4.00,USD
P009,Gel Pen Set,Stationery,6.49,2.50,USD
P010,Backpack,Accessories,59.99,28.00,USD
P011,Laptop Sleeve,Accessories,24.50,10.00,USD
P012,Webcam,Electronics,49.99,22.00,USD
P013,Portable SSD 1TB,Electronics,139.00,90.00,USD
P014,Smartwatch,Electronics,199.00,120.00,USD
P015,Ceramic Mug,Home,12.99,5.00,USD
P016,Desk Lamp,Home,34.99,15.00,USD

```

```plaintext
order_id,customer_id,order_date,product_id,quantity,status,total_amount
O1001,C001,2024-05-10,P001,2,Shipped,49.98
O1002,C003,2024-05-12,P002,1,Delivered,79.99
O1003,C002,2024-05-14,P004,1,Delivered,129.99
O1004,C005,2024-05-18,P005,1,Processing,329.00
O1005,C004,2024-05-20,P008,4,Delivered,39.96
O1006,C006,2024-05-22,P007,1,Shipped,399.00
O1007,C008,2024-05-24,P010,1,Delivered,59.99
O1008,C007,2024-05-26,P009,3,Delivered,19.47
O1009,C009,2024-05-28,P012,1,Delivered,49.99
O1010,C010,2024-06-01,P003,2,Delivered,39.98
O1011,C011,2024-06-03,P006,1,Processing,189.00
O1012,C012,2024-06-05,P014,1,Shipped,199.00
O1013,C013,2024-06-07,P016,2,Delivered,69.98
O1014,C014,2024-06-09,P011,2,Delivered,49.00
O1015,C015,2024-06-11,P015,4,Delivered,51.96
O1016,C002,2024-06-13,P013,1,Shipped,139.00
O1017,C005,2024-06-15,P002,2,Processing,159.98
O1018,C001,2024-06-17,P010,1,Processing,59.99

```

```plaintext
product_id,warehouse,stock_on_hand,reorder_level,last_restock_date,in_transit
P001,WH1,120,40,2024-06-01,30
P002,WH1,85,30,2024-06-02,20
P003,WH1,150,50,2024-05-29,40
P004,WH2,60,20,2024-05-30,15
P005,WH2,35,10,2024-05-25,10
P006,WH3,48,15,2024-06-03,12
P007,WH3,22,10,2024-06-04,8
P008,WH1,200,60,2024-05-28,50
P009,WH1,175,50,2024-05-28,40
P010,WH2,90,25,2024-06-01,25
P011,WH2,110,30,2024-06-02,30
P012,WH2,70,20,2024-05-31,18
P013,WH3,40,15,2024-06-03,10
P014,WH3,55,15,2024-06-04,12
P015,WH1,130,35,2024-05-27,30
P016,WH2,95,25,2024-05-30,22

```

```plaintext
payment_id,order_id,payment_date,method,amount,status
PMT2001,O1001,2024-05-10,Credit Card,49.98,Completed
PMT2002,O1002,2024-05-12,PayPal,79.99,Completed
PMT2003,O1003,2024-05-14,Credit Card,129.99,Completed
PMT2004,O1004,2024-05-18,Credit Card,329.00,Authorized
PMT2005,O1005,2024-05-20,PayPal,39.96,Completed
PMT2006,O1006,2024-05-22,Credit Card,399.00,Completed
PMT2007,O1007,2024-05-24,Debit Card,59.99,Completed
PMT2008,O1008,2024-05-26,PayPal,19.47,Completed
PMT2009,O1009,2024-05-28,Credit Card,49.99,Completed
PMT2010,O1010,2024-06-01,Credit Card,39.98,Completed
PMT2011,O1011,2024-06-03,Bank Transfer,189.00,Pending
PMT2012,O1012,2024-06-05,Credit Card,199.00,Completed
PMT2013,O1013,2024-06-07,Debit Card,69.98,Completed
PMT2014,O1014,2024-06-09,Credit Card,49.00,Completed
PMT2015,O1015,2024-06-11,PayPal,51.96,Completed
PMT2016,O1016,2024-06-13,Credit Card,139.00,Completed
PMT2017,O1017,2024-06-15,Bank Transfer,159.98,Authorized
PMT2018,O1018,2024-06-17,Debit Card,59.99,Pending

```

Created 5 related CSV datasets (15–18 rows each) in the current folder for your ecom scenario:

- `customers.csv` – 15 customers with ids, names, contact, signup date, city.
- `products.csv` – 16 products with category, price, cost, currency.
- `orders.csv` – 18 orders linking customers to products with quantity, status, totals.
- `inventory.csv` – stock per product/warehouse with reorder levels and in-transit counts.
- `payments.csv` – 18 payments tied to orders with method, amount, and status.

Relationships are consistent: `orders.customer_id` ↔ `customers.customer_id`, `orders.product_id` ↔ `products.product_id`, `payments.order_id` ↔ `orders.order_id`. Amounts align with product price × quantity.

Next steps: load these CSVs into your database (e.g., staging tables) and run referential checks or queries as needed.

---

**User**

i have to injest these in a database, i have to use sqlite. So write the whole code for it.



See to it that the cols are consistently maintained.

---

**Cursor**

```python
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
        default=".",
        help="Directory containing the CSV files (default: current directory).",
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

```

Added a ready-to-run SQLite loader at `ingest_sqlite.py` that preserves all column names and relationships.

What it does:
- Defines schemas for `customers`, `products`, `orders`, `inventory`, `payments` with the exact CSV headers.
- Enforces foreign keys and drops/recreates tables on each run for a clean load.
- Validates CSV headers before inserting.
- Loads data in dependency order and creates helpful indexes.

Run it from the folder with the CSVs:
- Default DB path `ecom.db`: `python ingest_sqlite.py --verbose`
- Custom paths: `python ingest_sqlite.py --db mydb.sqlite --data-dir . --verbose`

Tables and keys:
- `orders.customer_id` → `customers.customer_id`
- `orders.product_id` → `products.product_id`
- `payments.order_id` → `orders.order_id`
- `inventory.product_id` → `products.product_id`

---

**User**

change the file name to "ecommerce_data.py"

in terminal run a complex Join query for the ecom.db

---

**Cursor**

Here’s a complex join query already run against `ecom.db`:

```sql
SELECT
  c.customer_id,
  c.first_name || ' ' || c.last_name AS customer_name,
  COUNT(DISTINCT o.order_id)       AS orders_count,
  SUM(p.amount)                    AS total_paid,
  GROUP_CONCAT(DISTINCT pr.category) AS categories
FROM customers c
JOIN orders o     ON o.customer_id = c.customer_id
JOIN products pr  ON pr.product_id = o.product_id
LEFT JOIN payments p ON p.order_id = o.order_id
GROUP BY c.customer_id, customer_name
ORDER BY total_paid DESC;
```

Result (per-customer spend and categories):
- C005 Emma Williams — orders: 2 — paid: 488.98 — cats: Electronics
- C006 Felix Brown — orders: 1 — paid: 399.00 — cats: Furniture
- C002 Brian Smith — orders: 2 — paid: 268.99 — cats: Electronics
- C012 Liam Roberts — orders: 1 — paid: 199.00 — cats: Electronics
- C011 Karen Miller — orders: 1 — paid: 189.00 — cats: Furniture
- C001 Alice Johnson — orders: 2 — paid: 109.97 — cats: Electronics,Accessories
- C003 Carla Ramirez — orders: 1 — paid: 79.99 — cats: Electronics
- C013 Mia Thompson — orders: 1 — paid: 69.98 — cats: Home
- C008 Henry Clark — orders: 1 — paid: 59.99 — cats: Accessories
- C015 Olivia Garcia — orders: 1 — paid: 51.96 — cats: Home
- C009 Ivy Nguyen — orders: 1 — paid: 49.99 — cats: Electronics
- C014 Noah Anderson — orders: 1 — paid: 49.00 — cats: Accessories
- C010 Jacob Davis — orders: 1 — paid: 39.98 — cats: Electronics
- C004 David Lee — orders: 1 — paid: 39.96 — cats: Stationery
- C007 Gina Martinez — orders: 1 — paid: 19.47 — cats: Stationery

Need another query (e.g., product margin, inventory gaps, unpaid orders)? I can run it and share results.

```sql
SELECT
  c.customer_id,
  c.first_name || ' ' || c.last_name AS customer_name,
  COUNT(DISTINCT o.order_id)       AS orders_count,
  SUM(p.amount)                    AS total_paid,
  GROUP_CONCAT(DISTINCT pr.category) AS categories
FROM customers c
JOIN orders o     ON o.customer_id = c.customer_id
JOIN products pr  ON pr.product_id = o.product_id
LEFT JOIN payments p ON p.order_id = o.order_id
GROUP BY c.customer_id, customer_name
ORDER BY total_paid DESC;
```

---

**User**

make a different file for the sql query input

---

**Cursor**

```sql
-- Customers with order counts, total paid, and categories purchased
SELECT
  c.customer_id,
  c.first_name || ' ' || c.last_name AS customer_name,
  COUNT(DISTINCT o.order_id) AS orders_count,
  SUM(p.amount) AS total_paid,
  GROUP_CONCAT(DISTINCT pr.category) AS categories
FROM customers c
JOIN orders o     ON o.customer_id = c.customer_id
JOIN products pr  ON pr.product_id = o.product_id
LEFT JOIN payments p ON p.order_id = o.order_id
GROUP BY c.customer_id, customer_name
ORDER BY total_paid DESC;

-- Product sales summary with revenue and quantity sold
SELECT
  pr.product_id,
  pr.name,
  pr.category,
  SUM(o.quantity) AS units_sold,
  SUM(o.total_amount) AS revenue
FROM products pr
LEFT JOIN orders o ON o.product_id = pr.product_id
GROUP BY pr.product_id, pr.name, pr.category
ORDER BY revenue DESC;

-- Inventory status highlighting low stock vs reorder level
SELECT
  i.product_id,
  pr.name,
  i.warehouse,
  i.stock_on_hand,
  i.reorder_level,
  i.in_transit,
  (i.stock_on_hand + i.in_transit) AS projected_stock
FROM inventory i
JOIN products pr ON pr.product_id = i.product_id
WHERE i.stock_on_hand < i.reorder_level
ORDER BY i.stock_on_hand ASC;

-- Orders and payments with any pending/authorized payments
SELECT
  o.order_id,
  o.customer_id,
  o.status AS order_status,
  p.status AS payment_status,
  p.method,
  p.amount
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE p.status IN ('Pending', 'Authorized')
ORDER BY o.order_date;

```

Added a dedicated SQL script `queries.sql` with ready-to-run joins and summaries:
- Per-customer spend/categories.
- Product sales with revenue/units sold.
- Inventory low-stock view vs reorder levels.
- Orders with pending/authorized payments.

Run any query via SQLite CLI:
- `sqlite3 ecom.db ".read queries.sql"` (runs all)
- Or copy/paste individual queries as needed.

---

**User**

run these queries in terminal, or give me the command to run this queries

---

**Cursor**

Ran the script against `ecom.db`:

Command used:
- `sqlite3 ecom.db ".read queries.sql"`

Key outputs (in order of queries):
- Per-customer spend/categories (top rows shown): Emma Williams 488.98; Felix Brown 399.00; Brian Smith 268.99; Liam Roberts 199.00; Karen Miller 189.00 … down to Gina Martinez 19.47.
- Product sales (revenue/units): Standing Desk 399.00; 4K Monitor 329.00; Mechanical Keyboard 239.97; Smartwatch 199.00; Office Chair 189.00; … Gel Pen Set 19.47.
- Pending/authorized payments: O1004 (Authorized 329.00), O1011 (Pending 189.00), O1017 (Authorized 159.98), O1018 (Pending 59.99).

You can re-run anytime with the same command, or edit `queries.sql` and rerun.

---

**User**

Thank you so much for the help.

---

**Cursor**

You’re welcome! Glad it helped. If you need more queries or tweaks to the loader, just let me know.

---

**User**

see i have also created the output file,

just make me a readme markdown file,

---

**Cursor**

```markdown
# Diligent OA – Sample E-commerce Dataset and SQLite Loader

This repo contains synthetic e-commerce CSV data, a SQLite ingestion script, and example analytical queries.

## Contents
- `customers.csv`, `products.csv`, `orders.csv`, `inventory.csv`, `payments.csv` – related sample data (15–18 rows each).
- `ecommerce_data.py` – loads the CSVs into SQLite with foreign keys enforced.
- `queries.sql` – reusable SQL joins/summaries.
- `ecom.db` – SQLite database produced after running the loader.
- `output.csv` – example output generated by your run.

## Prerequisites
- Python 3.x
- `sqlite3` CLI (usually bundled with SQLite/Python installs)

## Load the data into SQLite
From the repo folder:
```bash
python ecommerce_data.py --db ecom.db --data-dir . --verbose
```
- Recreates tables each run (drops/rebuilds) and validates CSV headers.
- Foreign keys are enabled; the loader inserts in dependency order.

## Run the sample queries
Execute all queries in `queries.sql`:
```bash
sqlite3 ecom.db ".read queries.sql"
```
Or open an interactive shell:
```bash
sqlite3 ecom.db
-- then paste queries from queries.sql
```

## Files and schemas
- `customers` (`customer_id` PK) -> referenced by `orders`
- `products` (`product_id` PK) -> referenced by `orders`, `inventory`
- `orders` (`order_id` PK) -> references `customers`, `products`
- `payments` (`payment_id` PK) -> references `orders`
- `inventory` (composite PK: `product_id`, `warehouse`) -> references `products`

## Customizing
- Update CSVs to change data; rerun `ecommerce_data.py` to rebuild `ecom.db`.
- Add new SQL to `queries.sql` for additional reports; rerun the `.read` command.

## Example commands
- Reload DB: `python ecommerce_data.py --db ecom.db --verbose`
- Run queries: `sqlite3 ecom.db ".read queries.sql"`

```

Added `README.md` covering dataset contents, loader usage, schema notes, and how to run the sample queries. Let me know if you want any specific outputs or examples included.

---

**User**



add my credits

created by  Ajudiya Sneh, student of IIT Hyderabad

---

**Cursor**

```markdown
# Diligent OA – Sample E-commerce Dataset and SQLite Loader

This repo contains synthetic e-commerce CSV data, a SQLite ingestion script, and example analytical queries.

## Contents
- `customers.csv`, `products.csv`, `orders.csv`, `inventory.csv`, `payments.csv` – related sample data (15–18 rows each).
- `ecommerce_data.py` – loads the CSVs into SQLite with foreign keys enforced.
- `queries.sql` – reusable SQL joins/summaries.
- `ecom.db` – SQLite database produced after running the loader.
- `output.csv` – example output generated by your run.

## Prerequisites
- Python 3.x
- `sqlite3` CLI (usually bundled with SQLite/Python installs)

## Load the data into SQLite
From the repo folder:
```bash
python ecommerce_data.py --db ecom.db --data-dir . --verbose
```
- Recreates tables each run (drops/rebuilds) and validates CSV headers.
- Foreign keys are enabled; the loader inserts in dependency order.

## Run the sample queries
Execute all queries in `queries.sql`:
```bash
sqlite3 ecom.db ".read queries.sql"
```
Or open an interactive shell:
```bash
sqlite3 ecom.db
-- then paste queries from queries.sql
```

## Files and schemas
- `customers` (`customer_id` PK) -> referenced by `orders`
- `products` (`product_id` PK) -> referenced by `orders`, `inventory`
- `orders` (`order_id` PK) -> references `customers`, `products`
- `payments` (`payment_id` PK) -> references `orders`
- `inventory` (composite PK: `product_id`, `warehouse`) -> references `products`

## Customizing
- Update CSVs to change data; rerun `ecommerce_data.py` to rebuild `ecom.db`.
- Add new SQL to `queries.sql` for additional reports; rerun the `.read` command.

## Example commands
- Reload DB: `python ecommerce_data.py --db ecom.db --verbose`
- Run queries: `sqlite3 ecom.db ".read queries.sql"`

## Credits
Created by Ajudiya Sneh, student of IIT Hyderabad.


```

Added a Credits section to `README.md`: “Created by Ajudiya Sneh, student of IIT Hyderabad.”

