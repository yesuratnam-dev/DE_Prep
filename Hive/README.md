
-- Create database
CREATE DATABASE IF NOT EXISTS retail_db;

-- Use the database 
USE retail_db;

-- Create table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT,
    order_date TIMESTAMP,
    customer_id INT, 
    order_status STRING,
    order_total DECIMAL(10,2)
)
COMMENT 'Table containing order information'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Create partitioned table example
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT,
    order_id INT,
    product_id INT,
    quantity INT,
    item_price DECIMAL(10,2)
)
PARTITIONED BY (order_date STRING)
COMMENT 'Table containing order items information'
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;