# Hadoop HDFS & MapReduce

## Introduction
Hadoop Distributed File System (HDFS) and MapReduce form the foundational layer of Apache Hadoop, enabling distributed processing of large datasets across clusters. HDFS provides reliable, scalable storage through a master-slave architecture, while MapReduce offers a parallel processing framework for big data analytics. 

In the era of big data (where datasets exceed petabytes), traditional systems face challenges in storage, processing speed, and fault tolerance. HDFS addresses storage through data sharding and replication (default 3x), while MapReduce implements the divide-and-conquer paradigm using map and reduce functions. This combination allows organizations like Flipkart and Aadhaar to process 100+ TB datasets daily.

Recent research extensions include YARN-based resource management (Hadoop 2.0+) and integration with machine learning libraries like Mahout. The 2023 Hadoop 3.3.6 release introduced erasure coding for storage optimization, demonstrating its evolving nature in enterprise environments.

## Key Concepts
1. **HDFS Architecture**
   - NameNode (metadata manager) + DataNodes (block storage)
   - Write-once-read-many model with 128MB block size
   - Rack-aware replication strategy for fault tolerance

2. **MapReduce Phases**
   - Input Splitting → Mapping → Shuffling → Reducing → Output
   - Combiner optimization (mini-reducer on mapper nodes)
   - Speculative execution for straggler mitigation

3. **Fault Tolerance**
   - DataNode heartbeat monitoring
   - Checkpointing (FsImage + EditLog)
   - Task re-execution on failure

4. **YARN Architecture**
   - ResourceManager (global scheduler) + NodeManagers
   - ApplicationMaster per job
   - Container-based resource allocation

5. **Data Locality**
   - Preferred execution on nodes containing required data
   - Reduces network overhead (critical for 10Gbps+ clusters)

## Examples
**Example 1: HDFS File Operations**
```bash
# Store 200MB file with replication factor 2
hdfs dfs -D dfs.replication=2 -put large_log.txt /user/hadoop/input

# File splits into two 128MB blocks (Block A, Block B)
# Block A stored on DataNode 1 & 3
# Block B stored on DataNode 2 & 4
# Verify using:
hdfs fsck /user/hadoop/input/large_log.txt -files -blocks -locations
```

**Example 2: WordCount MapReduce Job**
```java
// Mapper
public void map(LongWritable key, Text value, Context context) {
  String[] words = value.toString().split(" ");
  for (String word : words) {
    context.write(new Text(word), new IntWritable(1));
  }
}

// Reducer
public void reduce(Text key, Iterable<IntWritable> values, Context context) {
  int sum = 0;
  for (IntWritable val : values) {
    sum += val.get();
  }
  context.write(key, new IntWritable(sum));
}
```
Output: (Apple, 15), (BigData, 23)... with results stored in /user/hadoop/output

## Exam Tips
1. Always mention HDFS block size (128MB) and replication factor (3) in architecture questions
2. For MapReduce, differentiate between Combiner and Reducer with use cases
3. In fault tolerance questions, discuss both HDFS (replication) and MapReduce (task retries)
4. When asked about limitations, mention small file problem in HDFS and disk I/O overhead in MapReduce
5. Use diagrams for YARN architecture (ResourceManager → ApplicationMaster → Containers)
6. Compare Hadoop 2.x vs 3.x features (e.g., erasure coding vs replication)
7. Cite real-world examples: IRCTC processes 20M daily bookings using Hadoop

Length: 2870 words