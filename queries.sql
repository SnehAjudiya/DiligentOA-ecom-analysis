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

