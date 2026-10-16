# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
df_boston = pd.read_sql("""
SELECT * 
FROM customers 
WHERE city = 'Boston';
""", conn)

# STEP 2
df_zero_emp = pd.read_sql("""
SELECT * 
FROM employees e
LEFT JOIN orders o ON e.employee_id = o.employee_id
WHERE o.order_id IS NULL;
""", conn)

# STEP 3
df_employee = pd.read_sql("""
SELECT * 
FROM employees;
""", conn)

# STEP 4
df_contacts = pd.read_sql("""
SELECT contact_name, phone 
FROM customers;
""", conn)

# STEP 5
df_payment = pd.read_sql("""
SELECT * 
FROM orders
ORDER BY CAST(amount AS REAL) DESC;
""", conn)

# STEP 6
df_credit = pd.read_sql("""
SELECT * 
FROM customers 
WHERE credit_limit > 50000;
""", conn)

# STEP 7
df_product_sold = pd.read_sql("""
SELECT DISTINCT p.product_name, c.category_name
FROM products p
JOIN order_details od ON p.product_id = od.product_id
JOIN orders o ON od.order_id = o.ID;
""", conn)

# STEP 8
df_total_customers = pd.read_sql("""
SELECT COUNT(*) AS total_customers 
FROM customers;
""", conn)

# STEP 9
df_customers = pd.read_sql("""
SELECT * 
FROM customers;
""", conn)

# STEP 10
df_under_20 = pd.read_sql("""
SELECT * 
FROM products 
WHERE unit_price < 20;
""", conn)

conn.close()