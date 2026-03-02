# Retrieval Queries in SQL - Summary

## Key Definitions and Concepts

- **SELECT Statement:** The fundamental SQL command used to retrieve data from database tables, specifying which columns to fetch.

- **WHERE Clause:** Filters rows based on specified conditions before any grouping or aggregation occurs.

- **GROUP BY Clause:** Groups rows with identical values for aggregate function calculations.

- **HAVING Clause:** Filters groups after GROUP BY, the only way to filter based on aggregate function results.

- **Aggregate Functions:** COUNT, SUM, AVG, MIN, MAX perform calculations across rows.

- **DISTINCT Keyword:** Eliminates duplicate values from query results.

## Important Formulas and Theorems

- **Basic SELECT:** `SELECT column1, column2 FROM table_name;`

- **Filtering:** `SELECT * FROM table WHERE condition;`

- **Pattern Matching:** `WHERE column LIKE 'pattern%'`

- **Range Check:** `WHERE column BETWEEN value1 AND value2;`

- **List Check:** `WHERE column IN (val1, val2, val3);`

- **Grouping:** `SELECT dept, COUNT(*) FROM table GROUP BY dept;`

- **Group Filter:** `SELECT dept, AVG(sal) FROM table GROUP BY dept HAVING AVG(sal) > value;`

- **Sorting:** `SELECT * FROM table ORDER BY column [ASC|DESC];`

## Key Points

- The SELECT statement is the most frequently used SQL command in database applications.

- WHERE filters individual rows; HAVING filters groups created by GROUP BY.

- Aggregate functions ignore NULL values except COUNT(\*).

- LIKE operator uses % (multiple characters) and \_ (single character) wildcards.

- ORDER BY defaults to ASC if not specified explicitly.

- NULL values cannot be compared using =; use IS NULL or IS NOT NULL.

- GROUP BY columns must be in SELECT list (non-aggregated columns).

- DISTINCT applies to the entire row combination, not a single column.

## Common Mistakes to Avoid

1. Using WHERE with aggregate functions (use HAVING instead).

2. Comparing NULL values with = NULL (always use IS NULL).

3. Forgetting to include non-aggregated columns in GROUP BY clause.

4. Confusing BETWEEN (inclusive) with exclusive range checks.

5. Using OR without parentheses when combining with AND conditions.

## Revision Tips

1. Practice writing queries step-by-step: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY.

2. Memorize the logical sequence: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.

3. Create sample tables and practice all query types covered in this module.

4. Focus on understanding WHEN to use each clause rather than just syntax.

5. Review previous year university question papers to understand the exam pattern and important topics.
