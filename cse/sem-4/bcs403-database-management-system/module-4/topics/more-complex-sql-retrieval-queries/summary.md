# More Complex SQL Retrieval Queries - Summary

## Key Definitions and Concepts

- **Subquery:** A query nested inside another SQL statement, used to retrieve intermediate results
- **Correlated Subquery:** A subquery that references columns from the outer query; executes once per row
- **Set Operations:** Combine results from multiple queries - UNION (all distinct), INTERSECT (common), EXCEPT (difference)
- **Aggregate Functions:** COUNT, SUM, AVG, MAX, MIN - perform calculations on row groups
- **JOIN Types:** INNER (matching rows), LEFT (all left + matching right), RIGHT (all right + matching left), FULL (all rows)
- **EXISTS/ NOT EXISTS:** Test whether subquery returns any rows (boolean operators)
- **ALL/ANY:** Compare against all values or any value from subquery results

## Important Formulas and Theorems

- WHERE executes before GROUP BY; HAVING executes after GROUP BY
- Execution order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- salary > ALL(subquery) ≡ salary > MAX(subquery values)
- salary > ANY(subquery) ≡ salary > MIN(subquery values)

## Key Points

- Subqueries can appear in SELECT, WHERE, FROM, and HAVING clauses
- Set operations require matching column count and compatible data types
- UNION removes duplicates; UNION ALL preserves duplicates
- LEFT JOIN includes all rows from left table even if no match exists
- HAVING filters grouped data; WHERE filters individual rows
- EXISTS stops execution when first match is found (efficient)
- Correlated subqueries reference outer table columns

## Common Mistakes to Avoid

- Using WHERE instead of HAVING for aggregate condition filtering
- Forgetting that subqueries must return compatible data types
- Not handling NULL values properly in comparisons
- Confusing UNION (distinct) with UNION ALL (all rows including duplicates)
- Omitting GROUP BY when using aggregate functions with non-aggregated columns

## Revision Tips

1. Practice writing both JOIN and equivalent subquery solutions for the same problem
2. Memorize the SQL query execution order to understand filter placement
3. Use EXISTS for existence checks rather than COUNT(\*) for better performance
4. Always verify column compatibility when using set operations
5. Test queries with sample data to verify correctness before examinations
