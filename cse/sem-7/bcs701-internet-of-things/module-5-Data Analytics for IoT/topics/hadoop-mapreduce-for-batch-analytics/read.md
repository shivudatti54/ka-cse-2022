# Hadoop MapReduce for Batch Data Analytics

## Overview

MapReduce is a programming model and software framework originally developed by Google for processing and generating large datasets in a distributed computing environment. Hadoop MapReduce, Apache's implementation of this paradigm, enables parallel processing of massive datasets across clusters of commodity hardware. Within the Internet of Things (IoT) ecosystem, MapReduce serves as a critical computational engine for analyzing historical sensor data, performing batch analytics on petabytes of device-generated information, and extracting actionable insights from time-series telemetry. This document provides a comprehensive examination of Hadoop MapReduce architecture, programming model, and its applications in IoT batch data analytics.

## 1. MapReduce Architecture and Execution Model

### 1.1 YARN Resource Manager Architecture

Hadoop MapReduce employs YARN (Yet Another Resource Negotiator) as its resource management layer, which decouples resource allocation from application execution. The YARN architecture comprises three primary components:

**ResourceManager (RM):** The master daemon that negotiates resource containers from NodeManagers and monitors application submission. It maintains a global view of cluster resources and schedules applications based on capacity guarantees and fairness policies.

**NodeManager (NM):** The per-node agent responsible for container management, resource monitoring, and communicating heartbeat messages to the ResourceManager. Each NodeManager reports available memory, CPU cores, and disk capacity to the ResourceManager.

**ApplicationMaster (AM):** Instantiated for each MapReduce job, the ApplicationMaster negotiates resource containers from the ResourceManager and coordinates task execution across worker nodes. It monitors task progress, handles failures, and coordinates the entire job lifecycle.

### 1.2 Job Execution Flow

The complete MapReduce job execution pipeline follows this sequence:

```
Client Submission → ResourceManager → ApplicationMaster → NodeManagers
 ↓
 Task Execution (Map → Shuffle → Reduce)
 ↓
 Job Completion Notification
```

**Step 1:** The client application submits the MapReduce job to the ResourceManager, providing the job configuration, input paths, output paths, and mapper/reducer classes.

**Step 2:** The ResourceManager allocates a container for the ApplicationMaster and negotiates with the appropriate NodeManager to launch it.

**Step 3:** The ApplicationMaster computes input splits, determines resource requirements, and requests containers from the ResourceManager for map and reduce tasks.

**Step 4:** NodeManagers launch containerized map and reduce tasks, which execute the user-defined map() and reduce() functions on data stored in HDFS.

**Step 5:** Upon job completion, the ApplicationMaster releases resources and notifies the client of job status, including statistics such as map completion percentage, reduce progress, and job counter values.

## 2. Programming Model and Data Flow

### 2.1 Formal Definition

MapReduce adheres to the functional programming paradigm, where the computation is expressed as two pure functions: **map** and **reduce**. Formally:

**Map Function:** Given an input key-value pair (k₁, v₁), the map function produces a list of intermediate key-value pairs [(k₂, v₂)].

**Reduce Function:** Given an intermediate key k₂ with associated list of values [v₂], the reduce function produces a list of output values [(k₃, v₃)].

This mathematical formulation ensures that map and reduce operations are inherently parallelizable, as each invocation operates independently without shared state or side effects.

### 2.2 Input and Output Specifications

**InputFormat:** Defines how input files are split into logical records. The default TextInputFormat treats each line as a record, with the line offset as the key and the line content as the value.

**OutputFormat:** Specifies the mechanism for writing output data. TextOutputFormat writes key-value pairs as tab-separated lines, suitable for subsequent processing or human inspection.

### 2.3 Key-Value Pair Processing

The fundamental data structure in MapReduce is the key-value pair. During the map phase, the input split is processed record-by-record, transforming each input record into zero or more intermediate key-value pairs. The shuffle phase groups all values associated with each unique key, presenting each reducer with a sorted list of values for its assigned keys.

## 3. Map Phase: Detailed Analysis

### 3.1 Map Task Execution

The map phase processes input splits in parallel across cluster nodes. For each input record, the mapper performs the following operations:

1. **Record Parsing:** The InputFormat reads the input split and produces key-value pairs representing the raw input data.

2. **User Logic Execution:** The developer's map() function processes each key-value pair, implementing domain-specific transformation logic.

3. **Intermediate Output Collection:** Mapper outputs are collected in an in-memory buffer (default 100MB), sorted by partition and key, and periodically spilled to local disk when the buffer threshold is exceeded.

4. **Partitioning:** Each intermediate key-value pair is assigned to a reducer partition using the Partitioner interface. The default HashPartitioner computes `hash(key) mod num_reducers` to determine the target partition.

### 3.2 Map Task Optimization for IoT Workloads

For IoT batch analytics involving sensor telemetry, several optimizations enhance map task performance:

**Compression:** Enabling mapper output compression (mapreduce.map.output.compress=true) significantly reduces disk I/O and network transfer costs, particularly beneficial for text-based sensor readings.

**Combiner Execution:** The combiner function aggregates mapper outputs locally before the shuffle phase, reducing network traffic. For aggregation operations like sum or count, the combiner can safely merge partial results without altering correctness.

## 4. Shuffle and Sort Phase

### 4.1 Shuffle Process

The shuffle phase transfers mapper outputs to reducers while ensuring data locality and load balancing. This phase constitutes the most expensive operation in MapReduce, often dominating job execution time.

**Partitioning:** The Partitioner determines which reducer receives each key. A well-designed partitioner ensures even data distribution across reducers, preventing reducer skew that degrades performance.

**Data Transfer:** Mapper outputs are transferred over the network using HTTP, with reducers pulling data from map task completion URLs. The shuffle phase begins while map tasks are still executing, enabling pipeline parallelism.

**Merging:** Reducers receive map outputs from multiple mappers and merge these streams using a merge-sort algorithm, maintaining sorted order by key.

### 4.2 Complexity Analysis

The shuffle phase exhibits the following complexity characteristics:

- **Network Traffic:** O(N × S) where N represents the number of mappers and S represents the average shuffle size per mapper.
- **Sort Complexity:** O(K × V log V) where K is the number of distinct keys and V is the total number of values.
- **Memory Requirements:** Reducers require memory proportional to the size of value lists for keys assigned to that reducer.

## 5. Reduce Phase

### 5.1 Reduce Task Execution

The reduce phase aggregates intermediate results to produce final outputs:

1. **Copy Phase:** Reducers copy sorted map outputs from mappers over the network.

2. **Merge Phase:** Downloaded data is merged into a single sorted stream, maintaining the shuffle-sort invariant.

3. **Group Phase:** The Iterator provides access to all values associated with each key, iterating through the sorted value list.

4. **Reduce Execution:** The user's reduce() function is invoked once per unique key, processing the entire list of values and emitting output key-value pairs.

### 5.2 Reduce Function Examples

**Word Count (Aggregation):**

```java
public void reduce(Text key, Iterable<IntWritable> values, Context context)
 throws IOException, InterruptedException {
 int sum = 0;
 for (IntWritable val : values) {
 sum += val.get();
 }
 context.write(key, new IntWritable(sum));
}
```

**IoT Temperature Aggregation:**

```java
public void reduce(Text key, Iterable<DoubleWritable> temperatures,
 Context context) throws IOException, InterruptedException {
 double sum = 0.0;
 int count = 0;
 for (DoubleWritable temp : temperatures) {
 sum += temp.get();
 count++;
 }
 double average = sum / count;
 context.write(key, new DoubleWritable(average));
}
```

## 6. Fault Tolerance Mechanisms

### 6.1 Task Failure Handling

MapReduce implements robust fault tolerance through automatic task retry and speculative execution:

**Task Failure:** If a map or reduce task fails (due to process crash, JVM exit, or task timeout), the ApplicationMaster reschedules the failed task on an available node. The task attempt is marked as failed after four task attempts (configurable via mapreduce.map.maxattempts).

**ApplicationMaster Failure:** The ResourceManager monitors ApplicationMaster heartbeats. If the AM fails, a new ApplicationMaster is launched, which retrieves job state from the previous attempts and resumes execution.

**NodeManager Failure:** When a NodeManager fails or loses connectivity, the ResourceManager marks all containers on that node as failed. The ApplicationMaster reschedules affected tasks on healthy nodes.

### 6.2 Speculative Execution

To address straggler tasks (nodes experiencing hardware degradation or resource contention), MapReduce launches duplicate tasks on alternative nodes. When the first duplicate completes, the slower attempt is killed. This optimization is enabled by default (mapreduce.map.speculative=true) and particularly effective for IoT workloads with uniform data distributions.

## 7. IoT Batch Analytics Use Cases

### 7.1 Time-Series Sensor Aggregation

MapReduce excels at batch processing of historical sensor data for trend analysis:

**Problem:** Calculate hourly average temperature readings from IoT sensors over one month of data.

**Solution:** The map function extracts hour and temperature from sensor records, emitting (hour, temperature) pairs. The reduce function computes the arithmetic mean for each hour, producing aggregated statistics.

**Performance Characteristics:** For N sensor readings across T time periods, the time complexity is O((N/T) × log T) assuming optimal partitioner design and balanced data distribution.

### 7.2 Anomaly Detection in Device Telemetry

MapReduce enables large-scale anomaly detection through statistical analysis:

**Problem:** Identify devices with temperature readings exceeding three standard deviations from the mean.

**Solution:** A two-pass MapReduce job: First pass computes mean and standard deviation; second pass flags anomalous readings. This pattern extends to detecting security breaches, equipment failures, or data quality issues across millions of IoT devices.

## 8. MapReduce vs. Apache Spark for IoT Analytics

While MapReduce remains foundational for batch processing, Apache Spark provides advantages for certain IoT workloads:

| Aspect           | MapReduce             | Apache Spark              |
| ---------------- | --------------------- | ------------------------- |
| Processing Model | Disk-based, two-phase | In-memory, DAG-based      |
| Latency          | Minutes (batch)       | Seconds (batch/iterative) |
| IoT Use Case     | Historical analysis   | Near-real-time analytics  |
| Fault Tolerance  | Replication-based     | Lineage-based             |

For IoT batch analytics involving historical data spanning months or years, MapReduce's disk-based model provides cost-effective processing with excellent fault tolerance characteristics.

## 9. Assessment Components

### 9.1 Multiple Choice Questions

**Question 1:** In a MapReduce job processing IoT sensor data, the mapper outputs 1,000 key-value pairs with the key representing device_id and value representing temperature reading. If a HashPartitioner with 10 reducers is used, and the hash function produces values uniformly distributed in [0, 99], what is the expected number of keys processed by each reducer?

A) 10
B) 100
C) 1000
D) Cannot be determined from given information

**Answer:** B) 100

**Explanation:** With a uniform hash distribution, each of the 10 reducers receives approximately 1000/10 = 100 key-value pairs. This assumes the hash function distributes keys uniformly across partitions, which is the expected behavior of HashPartitioner.

---

**Question 2:** Consider a MapReduce job with 5 mappers and 3 reducers processing 15 GB of data with 128 MB input splits. Each mapper generates 2 GB of intermediate data. What is the total network traffic during the shuffle phase (assuming no compression)?

A) 2 GB
B) 5 GB
C) 10 GB
D) 15 GB

**Answer:** C) 10 GB

**Explanation:** Each mapper generates 2 GB of intermediate output. All mapper outputs must be transferred to reducers: 5 mappers × 2 GB = 10 GB total shuffle traffic. The number of reducers does not affect total network traffic, only the distribution of data.

---

**Question 3:** In a MapReduce job for calculating maximum temperature per sensor, why is it unsafe to use a Combiner that outputs (sensor_id, max_temperature)?

A) Combiners cannot be used with max/min functions
B) The Combiner might run zero or more times, potentially missing intermediate values
C) Reducers cannot process combined results correctly
D) HDFS does not support combined outputs

**Answer:** B) The Combiner might run zero or more times, potentially missing intermediate values

**Explanation:** The Combiner is an optimization that may run locally after the map phase, but it is not guaranteed to execute. If max values from different mappers are combined, and the Combiner does not run, the Reducer receives individual values and correctly computes the maximum. However, using Combiner with max requires idempotency guarantees that may not hold in all scenarios.

---

**Question 4:** For an IoT batch analytics job processing 10 million sensor records, the map phase completes in 10 minutes with 100 map slots, and the reduce phase completes in 5 minutes with 20 reduce slots. What is the primary bottleneck in this job?

A) Map phase is bottleneck due to insufficient map slots
B) Reduce phase is bottleneck due to insufficient reduce slots
C) Shuffle phase is bottleneck as it overlaps with map completion
D) Cannot determine from given information

**Answer:** C) Shuffle phase is bottleneck as it overlaps with map completion

**Explanation:** The reduce phase can only begin after mappers produce output. Since map takes 10 minutes and reduce takes 5 minutes, the actual bottleneck is typically the shuffle phase (network transfer of mapper outputs to reducers), which overlaps with the tail end of map execution.

---

**Question 5:** Given a MapReduce cluster with 10 nodes, each having 8 cores and 16 GB memory, with mapreduce.map.memory.mb=2048 and mapreduce.reduce.memory.mb=4096, what is the maximum number of concurrent map tasks per node?

A) 2
B) 4
C) 8
D) 16

**Answer:** C) 8

**Explanation:** Each node has 16 GB memory. With map tasks requiring 2 GB each (mapreduce.map.memory.mb=2048), the theoretical maximum concurrent maps is 16/2 = 8. This assumes no other memory constraints and that CPU cores (8) are not the limiting factor.

### 9.2 Numerical Problem

**Problem:** A manufacturing facility has 1,000 IoT sensors, each recording temperature every 10 seconds, operating continuously for 30 days. Each sensor reading is approximately 100 bytes.

**Part A:** Calculate the total data volume generated in 30 days.

**Part B:** If this data is stored in HDFS with 3x replication and processed using MapReduce with 128 MB blocks, how many map tasks are created assuming TextInputFormat?

**Part C:** If each map task processes 100,000 records per second, estimate the total map phase execution time with 50 concurrent map slots.

**Solution:**

**Part A:**

- Records per sensor per day: (24 × 60 × 60) / 10 = 8,640 records
- Total records in 30 days: 1,000 × 8,640 × 30 = 259,200,000 records
- Data volume: 259,200,000 × 100 bytes = 25,920,000,000 bytes ≈ 24.15 GB

**Part B:**

- Unreplicated data size: 24.15 GB
- With 3x replication: 24.15 × 3 = 72.45 GB physical storage
- Number of input splits: 24.15 GB / 128 MB = 24.15 × 1024 / 128 ≈ 194 splits
- Therefore, approximately 194 map tasks are created

**Part C:**

- Total records: 259,200,000
- Map throughput: 100,000 records/second/map
- Concurrent map slots: 50
- Time = 259,200,000 / (100,000 × 50) = 259,200,000 / 5,000,000 = 51.84 seconds ≈ 52 seconds

---

### 9.3 Flashcard

**Term:** Data Locality
**Definition:** The MapReduce optimization principle that prefers executing map tasks on nodes containing the relevant data blocks in HDFS, minimizing network data transfer and improving job performance.
**Key Insight:** Hadoop achieves data locality by scheduling map tasks on DataNodes where input data is stored. With "process data where it lives," MapReduce reduces network congestion and improves throughput by up to 10x compared to moving data to computation.
