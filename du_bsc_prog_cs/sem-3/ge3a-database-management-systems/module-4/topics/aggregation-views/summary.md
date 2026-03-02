# Aggregation Views — DBMS Summary

## Introduction
Aggregation views are virtual or materialized database objects that store pre-computed summary data derived from base tables. They are essential for improving query performance in large databases by providing quick access to aggregated information without recalculating results at runtime.

## Key Concepts

### What Are Aggregation Views?
- Virtual tables defined by a query that performs aggregate operations (SUM, AVG, COUNT, MIN, MAX)
- Do not store data physically (unless materialized)
- Automatically update when underlying data changes

### Types of Views in DBMS
- **Simple Views**: Derived from single tables with no aggregate functions
- **Complex Views**: Include GROUP BY, JOINs, and aggregate functions
- **Materialized Views**: Store pre-computed results physically; refreshed periodically or on-demand

### Aggregation in Views
- Used to summarize large datasets
- Common aggregates: SUM, AVG, COUNT, MIN, MAX
- Often combined with GROUP BY clause
- Can include HAVING for filtering grouped results

### Benefits
- **Performance**: Reduces query execution time significantly
- **Simplifies Queries**: Users query the view instead of writing complex joins/aggregations
- **Data Independence**: Applications remain unaffected when table structure changes
- **Security**: Restricts access to sensitive aggregated data only

### Implementation Considerations
- **Refresh Methods**: On commit, on demand, or scheduled
- **Storage Overhead**: Materialized views require disk space
- **Maintenance**: Base table changes must reflect in views
- **Query Rewrite**: Optimizer may automatically use materialized views for query optimization

### Limitations
- Additional storage for materialized views
- Potential data staleness between refreshes
- Maintenance overhead for updating aggregates
- Not all DBMS support all view types

## Conclusion
Aggregation views are crucial for efficient database management, especially in analytical workloads. They balance query performance against storage costs and are vital for exam success in DBMS. Understand the difference between virtual and materialized views, their refresh mechanisms, and practical applications.

---
*Reference: Delhi University BSc (H) Computer Science NEP 2024 — Unit: Views and Materialization*