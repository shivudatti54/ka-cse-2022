# Apache Spark Core Concepts - Summary

## Key Definitions and Concepts
- **RDD**: Immutable distributed collection with lineage
- **DAG**: Directed Acyclic Graph of RDD transformations
- **Shuffle**: Data redistribution between stages
- **Lazy Evaluation**: Deferred execution until action

## Important Formulas and Theorems
- **RDD Lineage**: RDDₙ = f(RDDₙ₋₁) 
- **Partitioning**: Hash: `partition = hash(key) % numPartitions`
- **Data Locality**: PreferredLocations in RDD interface
- **Narrow vs Wide Dependencies**: Determines stage boundaries

## Key Points
- Spark achieves speed through in-memory computing and DAG optimization
- RDD persistence levels directly impact iterative algorithm performance
- Shuffle operations are expensive - minimize through partitioning
- Catalyst optimizer uses rule-based query optimization
- Tungsten engine uses binary memory format for efficiency
- Accumulators and broadcast variables enable shared state
- Structured APIs (DataFrames) build on RDDs with schema

## Common Mistakes to Avoid
- Using `collect()` on large datasets causing driver OOM
- Forgetting to persist intermediate RDDs in iterative processes
- Misusing `repartition` causing unnecessary shuffles
- Ignoring data skew in key-based transformations

## Revision Tips
1. Practice visualizing DAGs using Spark UI
2. Experiment with different persistence levels
3. Use `explain()` method to study query plans
4. Implement a PageRank algorithm from scratch
5. Compare performance of reduceByKey vs groupByKey