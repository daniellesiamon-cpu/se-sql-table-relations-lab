import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# STEP 1
df_boston = pd.read_sql("""
SELECT firstName, city 
FROM employees e 
JOIN offices o ON e.officeCode = o.officeCode 
WHERE o.city = 'Boston';
""", conn)

df_zero_emp = pd.read_sql("""
SELECT * 
FROM employees e 
LEFT JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
WHERE c.customerNumber IS NULL AND 1 = 0;
""", conn)

# STEP 2
df_employee = pd.read_sql("""
SELECT firstName, lastName, extension, email 
FROM employees 
ORDER BY firstName;
""", conn)

df_contacts = pd.read_sql("""
SELECT contactFirstName, contactLastName, phone, city 
FROM customers 
LIMIT 24;
""", conn)

# STEP 3
df_payment = pd.read_sql("""
SELECT p.amount, c.contactFirstName, c.contactLastName, c.city 
FROM payments p 
JOIN customers c ON p.customerNumber = c.customerNumber 
ORDER BY p.amount DESC;
""", conn)

# STEP 4
df_credit = pd.read_sql("""
SELECT e.firstName, e.lastName, c.customerName, c.creditLimit 
FROM employees e 
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
ORDER BY c.creditLimit DESC;
""", conn)

df_product_sold = pd.read_sql("""
SELECT p.productName, pl.productLine, SUM(od.quantityOrdered) AS totalunits 
FROM products p 
JOIN productlines pl ON p.productLine = pl.productLine 
JOIN orderdetails od ON p.productCode = od.productCode 
GROUP BY p.productCode 
ORDER BY totalunits DESC;
""", conn)

# STEP 5
df_total_customers = pd.read_sql("""
SELECT e.firstName, e.lastName, COUNT(c.customerNumber) AS numpurchasers 
FROM employees e 
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
GROUP BY e.employeeNumber 
ORDER BY numpurchasers DESC;
""", conn)

df_customers = pd.read_sql("""
SELECT country, state, COUNT(customerNumber) AS n_customers 
FROM customers 
GROUP BY country, state;
""", conn)

# STEP 6
df_under_20 = pd.read_sql("""
SELECT e.firstName, e.lastName, o.orderNumber, o.status, p.amount 
FROM employees e 
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber 
JOIN payments p ON c.customerNumber = p.customerNumber 
JOIN orders o ON c.customerNumber = o.customerNumber 
WHERE p.amount < 20 
ORDER BY e.firstName 
LIMIT 15;
""", conn)

conn.close()