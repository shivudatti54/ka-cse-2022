# Hadoop MapReduce for Batch Analytics

=====================================

### Overview

MapReduce is a programming model for distributed processing of large datasets, breaking computation into Map (transformation), Shuffle/Sort (organization), and Reduce (aggregation) phases. It provides automatic parallelization, fault tolerance, and data locality optimization for batch analytics on IoT data.

### Key Points

- **Map Function:** Processes input records independently in parallel, producing intermediate key-value pairs: map(key, value) -> list(k2, v2)
- **Shuffle and Sort Phase:** Groups all values for the same key together, transfers data from mappers to reducers, maintains sorted order
- **Reduce Function:** Aggregates grouped values to produce final output: reduce(key, list_of_values) -> list(final_key, final_value)
- **Combiner:** Optional local reducer on mapper nodes that reduces network transfer; only works for associative and commutative operations
- **Data Locality Levels:** Node-local (best, no network), Rack-local (minimal transfer), Off-rack (network transfer required)
- **Fault Tolerance:** Failed map/reduce tasks automatically rescheduled on different nodes; HDFS replication ensures data availability
- **Partitioner:** Determines which reducer receives which keys using hash(key) mod num_reducers by default; custom partitioners available

### Important Concepts

- Input splits map one-to-one with map tasks; each split processed independently
- Mapper output is buffered in memory (100MB default), sorted by key, and spilled to disk when full
- Reducer output written to HDFS as part files (Part-r-00000, Part-r-00001, etc.)
- Word Count is the classic MapReduce example: map emits (word, 1), reduce sums all counts per word

### Notes

- Be able to trace through a complete MapReduce execution with input data, map output, shuffle/sort grouping, and reduce output
- IoT use cases include sensor data aggregation, device log analysis, energy consumption monitoring, and network traffic pattern analysis
- Know the limitations: high latency, disk I/O overhead, inefficient for iterative ML algorithms, startup overhead for small jobs
