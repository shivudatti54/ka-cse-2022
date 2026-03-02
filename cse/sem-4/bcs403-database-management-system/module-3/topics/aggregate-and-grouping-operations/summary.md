# Aggregate and Grouping - Summary

## Key Functions

- **COUNT**: Number of rows (COUNT(\*) includes NULLs)
- **SUM**: Total of numeric values
- **AVG**: Average of numeric values
- **MAX**: Largest value
- **MIN**: Smallest value

## GROUP BY

- Groups rows with same values
- Used with aggregate functions
- Syntax: SELECT col, AGG(col) FROM table GROUP BY col

## HAVING

- Filters groups after aggregation
- Used only with GROUP BY
- Can use aggregate functions in condition

## Important Formulas

```sql
SELECT column, AGGREGATE_FUNCTION(column)
FROM table
[WHERE condition]
GROUP BY column
[HAVING group_condition]
[ORDER BY column];
```

## Exam Tips

1. Remember: WHERE → GROUP BY → HAVING → ORDER BY (order of execution)
2. COUNT(\*) counts all rows; COUNT(column) ignores NULLs
3. All columns in SELECT must either be aggregated or in GROUP BY
4. HAVING cannot exist without GROUP BY
5. Use HAVING for conditions on aggregate results
6. For maximum/minimum queries, remember to use appropriate aliases if needed
