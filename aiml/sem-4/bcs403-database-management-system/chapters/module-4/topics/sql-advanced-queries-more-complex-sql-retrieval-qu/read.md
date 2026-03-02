# **SQL: Advanced Queries: More Complex SQL Retrieval Queries**

## **Module Overview**

This module covers the advanced queries for SQL, focusing on more complex retrieval queries. You will learn how to use aggregate functions, subqueries, and window functions to retrieve data from a database.

## **Subqueries**

A subquery is a query nested inside another query. It is used to retrieve data from another table based on the results of the outer query.

### Types of Subqueries

- **Simple Subquery**: A single table is used in the subquery.
- **Compound Subquery**: Multiple tables are used in the subquery.
- **Correlated Subquery**: The subquery is executed for each row of the outer query.

### Example

Suppose we have two tables: `orders` and `customers`.

`orders` table:

| order_id | customer_id | order_date |
| -------- | ----------- | ---------- |
| 1        | 1           | 2022-01-01 |
| 2        | 2           | 2022-01-15 |
| 3        | 1           | 2022-02-01 |

`customers` table:

| customer_id | name     | email               |
| ----------- | -------- | ------------------- |
| 1           | John Doe | johndoe@example.com |
| 2           | Jane Doe | janedoe@example.com |

We want to find the orders that were placed by customers who live in New York.

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT customer_id
  FROM customers
  WHERE state = 'NY'
);
```

## **Aggregates**

Aggregate functions are used to group data and perform calculations on it.

### Types of Aggregate Functions

- **SUM**: Used to calculate the total of a column.
- **AVG**: Used to calculate the average of a column.
- **MAX**: Used to find the maximum value in a column.
- **MIN**: Used to find the minimum value in a column.
- **COUNT**: Used to count the number of rows in a table or a specified condition.
- **GROUPING SETS**: Used to group data into multiple levels.

### Example

Suppose we have a table `sales`, which contains the sales data of a company.

`sales` table:

| product_id | product_name | quantity | price |
| ---------- | ------------ | -------- | ----- |
| 1          | Product A    | 10       | 100   |
| 2          | Product B    | 20       | 200   |
| 3          | Product C    | 30       | 300   |
| 4          | Product D    | 40       | 400   |
| 5          | Product E    | 50       | 500   |

We want to find the total sales for each product and the total sales for all products.

```sql
SELECT product_name, SUM(price * quantity) AS total_sales
FROM sales
GROUP BY product_name;

SELECT product_name, SUM(price * quantity) AS total_sales
FROM sales
GROUP BY product_name, price;
```

## **Window Functions**

Window functions are used to perform calculations on data that is partitioned into one or more groups.

### Types of Window Functions

- **ROW_NUMBER**: Used to assign a unique number to each row in a partition.
- **RANK**: Used to rank rows in a partition based on a specified column.
- **DENSE_RANK**: Used to rank rows in a partition based on a specified column, without gaps.
- **NTILE**: Used to divide rows in a partition into equal-sized groups.
- **LAG**: Used to access data from a previous row in a partition.
- **LEAD**: Used to access data from a next row in a partition.

### Example

Suppose we have a table `employees`, which contains the employee data of a company.

`employees` table:

| employee_id | name          | salary |
| ----------- | ------------- | ------ |
| 1           | John Doe      | 50000  |
| 2           | Jane Doe      | 60000  |
| 3           | Bob Smith     | 70000  |
| 4           | Alice Johnson | 80000  |
| 5           | Mike Brown    | 90000  |

We want to find the salary of each employee, ranked by salary in descending order.

```sql
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;
```

## **Key Concepts**

- Subqueries are used to retrieve data from another table based on the results of the outer query.
- Aggregate functions are used to group data and perform calculations on it.
- Window functions are used to perform calculations on data that is partitioned into one or more groups.
- ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, and LEAD are used to assign a unique number to each row in a partition, rank rows in a partition, divide rows in a partition, access data from a previous or next row in a partition.
