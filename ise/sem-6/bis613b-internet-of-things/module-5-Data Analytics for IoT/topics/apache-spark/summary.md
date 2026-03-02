# Apache Spark

=====================================

### Overview

Apache Spark is a unified analytics engine for large-scale data processing that performs in-memory computations, achieving 10-100x faster performance than MapReduce. It provides a single platform for batch processing, stream processing, machine learning, and graph analytics, making it ideal for IoT applications.

### Key Points

- **In-Memory Computing:** Data cached in memory across operations, avoiding repeated disk I/O, resulting in 10-100x speedup over MapReduce
- **RDD (Resilient Distributed Dataset):** Core abstraction -- immutable, distributed, fault-tolerant collection of objects processed in parallel
- **Architecture Components:** Driver Program (SparkContext), Cluster Manager (YARN/Mesos/Standalone), Worker Nodes, and Executors
- **Two Operation Types:** Transformations (lazy: map, filter, flatMap -- build DAG) and Actions (eager: count, collect, reduce -- trigger execution)
- **Lazy Evaluation:** Transformations build a DAG of operations; actual execution deferred until an action is called, enabling optimization
- **Spark Ecosystem:** Spark Core, Spark SQL (structured data), Spark Streaming (micro-batch DStreams), MLlib (machine learning), GraphX (graph processing)
- **Spark Streaming:** Divides input stream into micro-batches (DStreams), each processed as an RDD for near real-time analytics
- **MLlib:** Provides scalable ML algorithms including classification, regression, clustering, and collaborative filtering

### Important Concepts

- RDD fault tolerance achieved through lineage-based recovery: lost partitions recomputed from parent RDDs
- DAG Scheduler breaks jobs into stages at shuffle boundaries; each stage contains parallel tasks
- DataFrames provide higher-level abstraction with schema, enabling SQL queries on structured IoT data
- Spark supports multiple deployment modes: Local, Standalone, YARN, and Kubernetes

### Notes

- Spark vs MapReduce comparison is a key exam topic: in-memory vs disk-based, unified vs batch-only, high-level APIs vs verbose code
- Know the RDD operations: Transformations are lazy (map, filter, union, distinct) while Actions trigger execution (count, collect, reduce)
- IoT use cases with Spark include real-time traffic analysis, predictive maintenance with MLlib, and energy consumption optimization
