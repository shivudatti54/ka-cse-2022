# DML Operations: SELECT, INSERT, UPDATE - Summary

## Key Definitions and Concepts

- **DML (Data Manipulation Language)**: SQL commands used to manipulate data within database tables—SELECT, INSERT, UPDATE, DELETE
- **SELECT**: Query statement to retrieve data from one or more tables
- **INSERT**: Statement to add new rows of data into a table
- **UPDATE**: Statement to modify existing data in a table
- **WHERE Clause**: Filter condition that specifies which rows to affect
- **Transaction**: A sequence of DML operations treated as a single unit of work

## Important Formulas and Theorems

- **Basic SELECT Syntax**: `SELECT column_list FROM table WHERE conditions ORDER BY columns;`
- **INSERT Syntax**: `INSERT INTO table (cols) VALUES (values);` or `INSERT INTO table SELECT ...`
- **UPDATE Syntax**: `UPDATE table SET col1=val1, col2=val2 WHERE condition;`
- **LIKE Pattern**: `%` matches any sequence; `_` matches single character
- **Logical Precedence**: NOT > AND > OR (use parentheses to override)

## Key Points

- SELECT is the most frequently used SQL command for data retrieval
- DISTINCT eliminates duplicate rows from query results
- WHERE clause filters rows before aggregation; HAVING filters after GROUP BY
- String literals must use single quotes ('); numeric values should not be quoted
- NULL comparisons require IS NULL or IS NOT NULL (not = NULL)
- UPDATE without WHERE clause updates ALL rows—always verify with SELECT first
- Aggregate functions (COUNT, SUM, AVG, MAX, MIN) cannot be used in WHERE clause
- Subqueries can be used in WHERE, FROM, and SELECT clauses for complex queries
- Transaction control (COMMIT/ROLLBACK) ensures data integrity during DML operations

## Common Mistakes to Avoid

1. **Forgetting WHERE in UPDATE/DELETE**: This affects all rows; always test with SELECT first
2. **Using = NULL instead of IS NULL**: NULL comparisons always evaluate to UNKNOWN
3. **Missing quotes around string values**: Causes syntax errors or incorrect comparisons
4. **Incorrect operator precedence**: Complex AND/OR conditions may evaluate incorrectly
5. **Using aggregate functions in WHERE**: Use HAVING or subqueries instead

## Revision Tips

1. Practice writing at least 30-40 SELECT queries covering all clauses before exams
2. Memorize the logical order of query execution: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
3. Always test UPDATE/DELETE conditions with equivalent SELECT before execution
4. Review previous 5 years' DU question papers for pattern and frequently asked query types
5. Create a quick reference sheet of all SQL operators and their usage for last-minute revision