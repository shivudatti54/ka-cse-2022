# **Language (HQL)**

## **Introduction**

Hive Query Language (HQL) is a SQL-like language used to interact with Hive, a data warehousing and SQL-like language for Hadoop. HQL is used to create, modify, and query data stored in Hive.

## **Key Features of HQL**

- **SQL-like syntax**: HQL is similar to SQL, making it easy for users familiar with SQL to learn HQL.
-     **Data manipulation**: HQL allows users to create, modify, and drop tables, as well as perform CRUD (Create, Read, Update, Delete) operations.
- **Data analysis**: HQL provides various functions and operators for data analysis, such as aggregations, filtering, sorting, and grouping.

## **Basic Syntax**

- **CREATE TABLE**: used to create a new table in Hive.
- **DROP TABLE**: used to drop an existing table in Hive.
- **SELECT**: used to retrieve data from a table.
- **FROM**: specifies the table(s) to retrieve data from.
- **WHERE**: used to filter data based on a condition.
- **GROUP BY**: used to group data based on one or more columns.

## **Data Types in HQL**

- **String**: used to represent a string value.
- **Int**: used to represent an integer value.
- **Float**: used to represent a floating-point value.
- **Date**: used to represent a date value.
- **Timestamp**: used to represent a timestamp value.
- **Boolean**: used to represent a boolean value.

## **Hive File Formats**

- **Text files**: used to store text data.
- **RC files**: used to store compacted data.
- **RC compressed files**: used to store data compressed using the RC algorithm.
- **Parquet files**: used to store columnar data.

## **Hive Query**

- **SELECT statement**: used to retrieve data from a table.
- **FROM clause**: specifies the table(s) to retrieve data from.
- **WHERE clause**: used to filter data based on a condition.
- **GROUP BY clause**: used to group data based on one or more columns.
- **HAVING clause**: used to filter grouped data based on a condition.

## **Example HQL Query**

```sql
-- Create a new table called "sales"
CREATE TABLE sales (
    date DATE,
    product String,
    quantity Int,
    amount Float
);

-- Insert data into the "sales" table
INSERT INTO TABLE sales VALUES
    ('2022-01-01', 'Product A', 10, 100.0),
    ('2022-01-02', 'Product B', 20, 200.0),
    ('2022-01-03', 'Product A', 30, 300.0);

-- Select data from the "sales" table
SELECT date, product, quantity, amount
FROM sales
WHERE product = 'Product A';

-- Group data by date and calculate the total quantity
SELECT date, SUM(quantity) AS total_quantity
FROM sales
GROUP BY date
HAVING SUM(quantity) > 50;
```

## **Common HQL Functions**

- **SUM**: used to calculate the sum of a column.
- **AVG**: used to calculate the average of a column.
- **MAX**: used to find the maximum value in a column.
- **MIN**: used to find the minimum value in a column.
- **COUNT**: used to count the number of rows in a table.
- **GROUP BY**: used to group data based on one or more columns.

## **Common HQL Operators**

- **=**: used for equality comparison.
- **<**: used for less-than comparison.
- **>**: used for greater-than comparison.
- **<=>**: used for equality comparison with negation.
- **LIKE**: used for pattern matching.
- **IN**: used for membership testing.

## **Conclusion**

Hive Query Language (HQL) is a powerful tool for interacting with Hive. HQL provides a SQL-like syntax and supports various data manipulation and analysis operations. By mastering HQL, users can efficiently manage and analyze data in Hive, making it an essential skill for data analysts and data engineers working with Hive.
