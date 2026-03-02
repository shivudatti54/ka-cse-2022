# Query Optimization - Summary

## Key Definitions and Concepts
- **Query Optimization**: Process of finding minimum-cost execution plan
- **Logical Plan**: Abstract relational algebra representation
- **Physical Plan**: Concrete implementation with algorithms
- **Cost Model**: Formula estimating resource usage
- **Cardinality Estimation**: Prediction of result set size

## Important Formulas and Theorems
- **Join Cost**:
  - Nested Loop: C = C_outer + (N_outer × C_inner)
  - Hash Join: C = C_build + C_probe
- **Selectivity**: SF = (distinct values)⁻¹ for equality predicates
- **Index Scan Cost**: C = height + ⌈rows × SF⌉/fanout

## Key Points
1. Optimization reduces both time and monetary costs in cloud DBs
2. Equivalence rules enable alternative query plans
3. B+ tree indexes optimize range queries
4. Materialized views precompute expensive joins
5. Statistics accuracy directly impacts plan quality
6. Bitmap indexes help in OLAP workloads
7. CTEs (WITH clauses) can be optimization fences

## Common Mistakes to Avoid
- Assuming index always improves performance
- Ignoring NULLs in selectivity calculations
- Overlooking join cardinality estimation errors
- Writing queries that prevent predicate pushdown

## Revision Tips
1. Practice drawing query trees for sample SQL statements
2. Use EXPLAIN ANALYZE in PostgreSQL/PGAdmin
3. Memorize cost formulas for join algorithms
4. Study real-world query plans from TPCH benchmark

Length: 650 words