# Apache Spark Core Concepts

## Introduction
Apache Spark has revolutionized big data processing through its in-memory computing capabilities and advanced DAG execution engine. Developed at UC Berkeley's AMPLab, Spark addresses limitations of Hadoop MapReduce by offering 100x faster performance for iterative algorithms through resilient distributed datasets (RDDs). Its unified stack (Spark SQL, MLlib, GraphX, Spark Streaming) makes it indispensable for modern data pipelines.

The core architecture combines fault tolerance through lineage graphs with efficient resource management via cluster managers. For DU MSc CS students, understanding Spark's execution model is crucial for developing efficient ETL processes, machine learning pipelines, and real-time analytics systems. Current research focuses on optimizing Catalyst query planner and Tungsten execution engine for AI workloads.

## Key Concepts
1. **Resilient Distributed Datasets (RDDs)**: 
   - Immutable distributed collections with partitioning metadata
   - Lineage tracking through transformation graphs
   - Lazy evaluation and persistence levels (MEMORY_ONLY, DISK_ONLY)

2. **DAG Scheduler**:
   - Converts logical execution plan into physical stages
   - Optimizes narrow/wide transformations through pipelining
   - Handles shuffle operations using HashPartitioner/RangePartitioner

3. **SparkContext**:
   - Entry point for cluster connectivity
   - Manages job submission and task scheduling
   - Coordinates with Cluster Manager (YARN/Mesos/Standalone)

4. **Transformations vs Actions**:
   - Transformations (map, filter, join) build RDD lineage
   - Actions (count, collect, saveAsTextFile) trigger job execution

5. **Shuffle Operations**:
   - Data redistribution between partitions during groupByKey/reduceByKey
   - Managed through shuffle managers (Sort vs TungstenSort)

## Examples

**Example 1: Word Count with Lineage**
```python
text_file = sc.textFile("hdfs:///data.txt")
counts = text_file.flatMap(lambda line: line.split()) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a,b: a+b)
print(counts.collect())
```
*Lineage Graph*: 
textFile → flatMap → map → reduceByKey → collect

**Example 2: Fault Tolerance Demonstration**
```python
rdd = sc.parallelize([1,2,3,4], 2).map(lambda x: x*2)
rdd.persist(StorageLevel.MEMORY_AND_DISK)
print(rdd.sum())  # Action triggers persistence
# Simulate node failure
recovered = rdd.map(lambda x: x/2)  # Recomputes from lineage
```

**Example 3: Join Optimization**
```python
users = sc.parallelize([(1, "Alice"), (2, "Bob")])
transactions = sc.parallelize([(1, 100), (1, 200), (2, 50)])
joined = users.join(transactions).partitionBy(4)
# Optimized using co-partitioned RDDs
```

## Exam Tips
1. Always differentiate between transformations (lazy) vs actions (eager)
2. Understand partitioning impact on shuffle operations
3. Memorize RDD properties: Immutable, Partitioned, Typed
4. Compare Spark's DAG vs MapReduce's two-stage execution
5. Explain checkpointing vs lineage for fault tolerance
6. Know storage levels and their memory/CPU tradeoffs
7. Describe Catalyst optimizer's role in Spark SQL