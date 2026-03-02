# Hadoop Ecosystem: HDFS & MapReduce

## Introduction
The Hadoop ecosystem revolutionized big data processing by enabling distributed storage and computation across commodity hardware. At its core, Hadoop Distributed File System (HDFS) provides reliable storage while MapReduce offers a parallel processing framework. This combination addresses two fundamental challenges of big data: storing massive datasets (petabyte-scale) and processing them efficiently.

For MCA students, understanding HDFS and MapReduce is crucial as they form the foundation for modern data engineering. Companies like Facebook (storing 300+ PB in HDFS) and LinkedIn (processing 1.4M+ daily jobs) rely on these technologies. The Hadoop ecosystem's scalability makes it ideal for Indian use cases like Aadhaar data management and UPI transaction analysis.

## Key Concepts
1. **HDFS Architecture**
   - NameNode: Metadata manager (file->block mapping)
   - DataNode: Stores actual data blocks (default 128MB)
   - Replication: 3x replication across racks (rack-aware)
   - Write Pipeline: Client -> DataNode chain for block storage

2. **MapReduce Model**
   - Map Phase: (key, value) -> list(intermediate key, value)
   - Shuffle & Sort: Group values by key across nodes
   - Reduce Phase: Aggregate values per key
   - Combiner: Local reducer to minimize network traffic

3. **YARN (Resource Management)**
   - ResourceManager: Cluster resource allocation
   - NodeManager: Per-machine resource monitoring
   - ApplicationMaster: Per-job lifecycle manager

4. **Fault Tolerance**
   - DataNode heartbeat mechanism
   - Speculative execution for slow tasks
   - Checkpointing for NameNode recovery

## Examples
**Example 1: Word Count (MapReduce)**
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

**Example 2: HDFS File Write**
1. Client contacts NameNode for block locations
2. NameNode returns DataNode list (e.g., DN1, DN2, DN3)
3. Client writes block to DN1, which replicates to DN2, then DN3
4. Pipeline acknowledgment sent back through chain

**Example 3: Log Analysis (Error Count by Hour)**
Map Phase: Extract (hour, error_code) from logs
Shuffle: Group errors by hour
Reduce: Count occurrences per error type per hour

## Exam Tips
1. Always mention HDFS block size (128MB default) and replication factor (3)
2. For MapReduce questions, clearly separate mapper/shuffle/reduce phases
3. Remember YARN components: ResourceManager vs ApplicationMaster
4. Practice writing pseudocode for common problems (sorting, joins)
5. Understand rack awareness in HDFS replication strategy
6. Compare Hadoop 1 (JobTracker) vs Hadoop 2 (YARN) architectures
7. Explain speculative execution with real-world scenarios

Length: 2200 words, MCA PG level