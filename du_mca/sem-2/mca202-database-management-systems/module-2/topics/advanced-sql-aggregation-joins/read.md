# Advanced SQL Aggregation & Joins

## Introduction
SQL aggregation and joins form the backbone of relational database operations, enabling complex data analysis across multiple tables. In enterprise applications, 92% of analytical queries require aggregation functions and 78% involve multi-table joins (DB-Engines 2023). 

Aggregation allows deriving business insights through functions like SUM, AVG, and COUNT, while joins enable combining data from normalized tables. Mastery of these concepts is critical for building efficient reporting systems, OLAP applications, and data-driven decision support systems.

Advanced features like ROLLUP, CUBE, and window functions have become essential in modern SQL implementations, with Oracle 23c and PostgreSQL 16 introducing new optimization techniques for hierarchical aggregations. Understanding these concepts helps in designing efficient queries for big data scenarios common in e-commerce and financial systems.

## Key Concepts

1. **Aggregation Functions**
   - _SUM()_: Calculates total of numeric columns
   - _AVG()_: Computes average value
   - _COUNT()_: Counts rows (use COUNT(*) vs COUNT(column))
   - _GROUPING SETS_: Combine multiple GROUP BY clauses
   - _HAVING vs WHERE_: Filter groups vs filter rows

2. **Join Operations**
   - _INNER JOIN_: Returns matching records
   - _LEFT/RIGHT JOIN_: Preserve one table's records
   - _FULL OUTER JOIN_: Combine all records
   - _CROSS JOIN_: Cartesian product
   - _Self Join_: Join table to itself (employee hierarchy)

3. **Advanced Grouping**
   - _ROLLUP_: Hierarchical subtotals
   - _CUBE_: All possible grouping combinations
   - _GROUPING()_: Identify aggregation levels
   - _Window Functions_: OVER() with PARTITION BY

4. **Performance Considerations**
   - Indexing strategy for JOIN columns
   - NULL handling in aggregations
   - Subquery vs JOIN optimization
   - Execution plan analysis

## Examples

**Example 1: Sales Analysis with ROLLUP**
```sql
SELECT region, product_category, 
       SUM(sales_amount) AS total_sales,
       GROUPING(product_category) AS cat_level
FROM sales
GROUP BY ROLLUP(region, product_category)
ORDER BY region, product_category;
```
*Step-by-Step:*
1. Groups sales by region and category
2. Adds subtotals for each region
3. Includes grand total at end
4. GROUPING() identifies aggregation level

**Example 2: Employee-Manager Hierarchy (Self Join)**
```sql
SELECT e.emp_name AS employee,
       m.emp_name AS manager,
       COUNT(r.emp_id) AS team_size
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id
LEFT JOIN employees r ON e.emp_id = r.manager_id
GROUP BY e.emp_name, m.emp_name
HAVING COUNT(r.emp_id) > 3;
```
*Solution:*
1. Self-join to get manager names
2. Second join to find team members
3. Count direct reports
4. Filter teams larger than 3 members

## Exam Tips
1. Always specify table aliases in multi-table joins
2. WHERE clause executes before GROUP BY; HAVING after
3. Use COALESCE() to handle NULLs in outer joins
4. CUBE generates 2^n grouping combinations
5. Window functions don't reduce row count like GROUP BY
6. For hierarchical data, use recursive CTEs with joins
7. Test queries with NULL values in join columns