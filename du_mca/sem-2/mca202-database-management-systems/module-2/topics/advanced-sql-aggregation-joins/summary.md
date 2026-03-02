# Advanced SQL Aggregation & Joins - Summary

## Key Definitions and Concepts
- **GROUP BY**: Groups rows sharing common values
- **HAVING**: Filters groups after aggregation
- **Equi-Join**: Join using equality operator
- **Theta Join**: Join with any comparison operator
- **Semi-Join**: EXISTS/NOT EXISTS subqueries
- **Anti-Join**: Exclude matching records

## Important Formulas and Theorems
- `COUNT(DISTINCT column) = ...` (Count unique values)
- `SUM() OVER(PARTITION BY ...)` (Window aggregation)
- Join Cardinality: |A ⨝ B| ≤ |A| × |B|
- NULL Propagation: SUM(NULL) = NULL

## Key Points
- LEFT JOIN preserves left table's unmatched rows
- ROLLUP creates subtotals from rightmost column
- CUBE generates all possible grouping combinations
- Window functions maintain individual row visibility
- Composite indexes improve join performance
- EXISTS is faster than COUNT(*) > 0 in subqueries
- Materialized views can precompute aggregations

## Common Mistakes to Avoid
- Using HAVING without GROUP BY
- Forgetting table aliases in self-joins
- Mixing aggregated/non-aggregated columns in SELECT
- Assuming INNER JOIN default in outer join scenarios
- Ignoring NULLs in COUNT(column) vs COUNT(*)

## Revision Tips
1. Practice writing 5-table joins with different join types
2. Create matrix of all JOIN types with Venn diagrams
3. Use EXPLAIN ANALYZE to compare query plans
4. Solve past DU papers on inventory management systems
5. Memorize SQL order of execution:
   FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY