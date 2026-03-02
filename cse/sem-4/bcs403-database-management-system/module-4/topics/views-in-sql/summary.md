# Views in SQL - Summary

## Key Definitions and Concepts

- **View**: A virtual table defined by a stored SELECT query; does not store data physically but derives results from underlying base tables when queried.

- **Simple View**: A view created from a single table without aggregate functions, GROUP BY, or joins; typically updatable.

- **Complex View**: A view created from multiple tables or containing aggregates, GROUP BY, or expressions; often read-only.

- **Materialized View**: A view that stores actual query results physically and can be refreshed periodically.

- **WITH CHECK OPTION**: A constraint that ensures DML operations through a view satisfy the view's defining condition.

## Important Formulas and Syntax

```sql
CREATE VIEW view_name [(column_list)] AS
select_statement
[WITH CHECK OPTION];

CREATE OR REPLACE VIEW view_name AS select_statement;

DROP VIEW view_name;
```

## Key Points

- Views provide data security by restricting access to specific columns and rows of base tables.

- Simple views (single table, no aggregates) are updatable; complex views are usually read-only.

- The WITH CHECK OPTION prevents insertions or updates that would make rows invisible through the view.

- Views offer logical data independence, allowing schema changes without affecting user applications.

- Materialized views improve query performance for complex aggregations but require refresh mechanisms.

- Views do not store data; they store query definitions that are executed at runtime.

- A view can reference multiple tables through joins but updatability is restricted in such cases.

## Common Mistakes to Avoid

- Assuming all views are updatable—complex views with aggregates cannot be modified.

- Forgetting that views don't store data physically, only the query definition.

- Not understanding that WITH CHECK OPTION applies to the WHERE condition in the view definition.

- Attempting to update multiple base tables through a single view, which is not allowed.

## Revision Tips

- Practice writing CREATE VIEW statements with different complexity levels.

- Memorize the conditions required for a view to be updatable.

- Understand the difference between views and materialized views clearly.

- Review past university exam questions on views to understand the question patterns.

- Focus on the practical applications of views in database security and query simplification.
