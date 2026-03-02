# Hadoop Ecosystem: HDFS and MapReduce - Summary

## Key Definitions and Concepts

- **HDFS (Hadoop Distributed File System)**: A distributed file system designed to store large datasets across multiple commodity machines, providing high throughput access to application data.

- **NameNode**: The master node in HDFS that maintains the file system namespace, manages metadata, and regulates client access to files.

- **DataNode**: Slave nodes in HDFS that manage physical storage, send block reports, and process read/write requests from clients.

- **Block**: The minimum unit of data in HDFS, default 128MB in Hadoop 3.x, distributed across DataNodes for parallel processing.

- **MapReduce**: A programming model for processing large datasets in parallel across distributed clusters, consisting of Map and Reduce phases.

- **YARN (Yet Another Resource Negotiator)**: The resource management layer in Hadoop 2.x+ that separates resource allocation from application execution.

- **Shuffle and Sort**: The intermediate phase between Map and Reduce where outputs are partitioned, sorted by key, and transferred to reducer nodes.

## Important Formulas and Theorems

- **Replication Factor Formula**: Default replication factor = 3, with placement strategy: 1 on writer's node, 1 on different node in same rack, 1 on different rack.

- **Block Size Calculation**: Number of blocks = ceil(file_size / block_size). Memory required by NameNode ≈ number_of_files × 150 bytes.

- **Data Locality**: Processing time = computation_time + (data_size × network_bandwidth). Optimal case achieves 100% data locality with zero network transfer.

## Key Points

- HDFS follows master-slave architecture with NameNode as master and DataNodes as slaves, optimized for streaming reads of large files.

- The default block size of 128MB minimizes NameNode memory usage and optimizes sequential disk operations.

- MapReduce divides processing into Map phase (key-value transformation) and Reduce phase (aggregation).

- YARN enables multi-tenancy and supports diverse processing frameworks beyond MapReduce.

- HDFS provides automatic fault tolerance through replication, heartbeat detection, and block rebalancing.

- Combiners reduce network traffic by performing local aggregation; partitioners control key distribution to reducers.

- Data locality—running computations where data resides—is the fundamental performance advantage of Hadoop.

## Common Mistakes to Avoid

- Confusing Secondary NameNode as a backup; it performs checkpointing only and cannot serve as active NameNode.

- Assuming MapReduce can handle real-time queries; it is designed for batch processing with latency measured in minutes to hours.

- Ignoring combiner and partitioner configuration, leading to skewed data distribution and reduced performance.

- Setting block size too small for small files, causing excessive NameNode memory consumption and reduced throughput.

- Overlooking the importance of rack-awareness in production deployments for network fault tolerance.

## Revision Tips

1. Draw the complete HDFS and MapReduce architecture diagrams from memory, labeling all components and data flows.

2. Practice implementing the Word Count program multiple times until you can write it without reference.

3. Memorize the default configurations (block size 128MB, replication factor 3, port numbers 50070 for NameNode, 50030 for JobTracker).

4. Compare MapReduce 1.x and YARN architectures in a table format, focusing on their differences in resource management.

5. Execute all HDFS CLI commands covered in the module on a sandbox environment to build muscle memory.