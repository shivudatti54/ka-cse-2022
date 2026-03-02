# Aggregation, GROUP BY, and HAVING - Summary

## Key Definitions and Concepts

- **Aggregate Functions**: SQL functions (COUNT, SUM, AVG, MIN, MAX) that perform calculations across multiple rows and return a single result
- **GROUP BY**: Clause that groups rows with identical values in specified columns for aggregate calculations
- **HAVING**: Clause that filters groups after aggregation (unlike WHERE which filters before)
- **Logical Query Execution Order**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

## Important Formulas and Techniques

- Basic aggregation: `SELECT COUNT(*) FROM table;`
- Grouped aggregation: `SELECT col, AGG(col) FROM table GROUP BY col;`
- Filtered groups: `SELECT col, AGG(col) FROM table GROUP BY col HAVING AGG(col) condition;`
- Multiple grouping: `GROUP BY col1, col2` creates subgroups

## Key Points

- Aggregate functions ignore NULL values except COUNT(*)
- Every non-aggregated column in SELECT must appear in GROUP BY
- WHERE filters rows before grouping; HAVING filters groups after grouping
- ORDER BY always follows GROUP BY and HAVING
- Multiple columns in GROUP BY create composite groups
- Use ROUND() with AVG() to control decimal precision
- JOINs can precede GROUP BY for multi-table aggregations
- HAVING can reference aggregate functions; WHERE cannot

## Common Mistakes to Avoid

1. Using HAVING without GROUP BY (produces incorrect results)
2. Including non-aggregated columns in SELECT that aren't in GROUP BY
3. Confusing WHERE and HAVING—using WHERE to filter aggregated results
4. Forgetting that GROUP BY creates groups, not filtered results
5. Omitting ORDER BY when asking for "top N" results (undefined ordering)

## Revision Tips

1. Practice writing 5-10 queries daily covering different scenarios
2. Trace through execution order manually for complex queries
3. Solve previous year DU exam questions on this topic
4. Create your own scenarios: e.g., "sales by region," "student statistics by course"
5. Use EXPLAIN or trace tables to verify query results step-by-step