# Query Processing and Optimization - Summary

## Key Definitions and Concepts
- **Query Processing**: Sequence of steps converting SQL to executable code
- **Logical Plan**: Abstract algebra representation (σ, π, ⋈)
- **Physical Plan**: Specific implementation choices (index scan vs full scan)
- **Cost Model**: Formula estimating resource usage (I/O + CPU)
- **Pipeline Breaker**: Operators requiring full input before producing output

## Important Formulas and Theorems
- **Cost Estimation**:
  - Index Scan Cost: `C = h + ⌈B(R)/V(R,a)⌉`
  - Join Cost (Nested Loop): `C = B(R) + B(R)×B(S)`
- **AC0 Complexity Theorem**: Relational algebra queries have PTIME data complexity
- **Selinger's Algorithm**: O(n!) → O(3^n) join ordering via dynamic programming

## Key Points
- Optimization accounts for 70-90% of total query execution time
- Cardinality estimation errors compound exponentially in deep query trees
- Distributed systems require considering data partitioning and network latency
- Modern optimizers use hybrid cost models combining statistics and ML
- Materialized views trade storage space for computation time
- Adaptive methods re-optimize during execution using runtime statistics
- Cloud-native optimizers must account for elastic resources and spot instances

## Common Mistakes to Avoid
- Assuming optimal join order is always left-deep
- Ignoring correlation between predicates in selectivity estimation
- Overlooking memory constraints in hash join operations
- Treating distributed nodes as homogeneous in cost models

## Revision Tips
1. Practice cost calculations for nested loop vs merge vs hash joins
2. Memorize System R's 3-phase optimization process
3. Study real optimizer architectures (PostgreSQL vs Spark SQL)
4. Review cutting-edge papers on learned query optimizers
5. Create comparison charts for different join algorithms' time/space complexity

Length: 650 words