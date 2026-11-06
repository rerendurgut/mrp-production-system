INSERT INTO customer (customer_id, customer_name)
VALUES ("CUST001", "Eren");
SET SQL_SAFE_UPDATES = 0;

INSERT INTO orders (order_id, customer_id, period_number, item_id, amount)
VALUES ("ORD001", "CUST001", 10, "001", 15);

INSERT INTO orders (order_id, customer_id, period_number, item_id, amount)
VALUES ("ORD002", "CUST001", 3, "001", 5);
SET SQL_SAFE_UPDATES = 1;
