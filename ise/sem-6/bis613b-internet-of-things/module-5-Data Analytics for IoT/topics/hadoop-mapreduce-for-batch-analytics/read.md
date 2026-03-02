# Hadoop MapReduce for Batch Data Analytics


## Table of Contents

- [Hadoop MapReduce for Batch Data Analytics](#hadoop-mapreduce-for-batch-data-analytics)
- [Overview](#overview)
- [What is MapReduce?](#what-is-mapreduce)
  - [MapReduce Philosophy](#mapreduce-philosophy)
- [MapReduce Programming Model](#mapreduce-programming-model)
  - [Basic Concepts](#basic-concepts)
  - [MapReduce Phases](#mapreduce-phases)
- [Map Phase](#map-phase)
  - [Map Function](#map-function)
  - [Map Process Flow](#map-process-flow)
  - [Map Example: Word Count](#map-example-word-count)
  - [IoT Map Examples](#iot-map-examples)
- [Shuffle and Sort Phase](#shuffle-and-sort-phase)
  - [Shuffle Process](#shuffle-process)
  - [Sort Process](#sort-process)
  - [Combiner (Optional)](#combiner-optional)
- [Reduce Phase](#reduce-phase)
  - [Reduce Function](#reduce-function)
  - [Reduce Process Flow](#reduce-process-flow)
  - [Reduce Example: Word Count](#reduce-example-word-count)
  - [IoT Reduce Examples](#iot-reduce-examples)
- [Complete MapReduce Workflow](#complete-mapreduce-workflow)
  - [Detailed Execution Flow](#detailed-execution-flow)
  - [Task Scheduling](#task-scheduling)
  - [Fault Tolerance](#fault-tolerance)
- [Classic Example: Word Count](#classic-example-word-count)
  - [Problem Statement](#problem-statement)
  - [MapReduce Solution](#mapreduce-solution)
- [IoT Batch Analytics Use Cases](#iot-batch-analytics-use-cases)
  - [1. Sensor Data Aggregation](#1-sensor-data-aggregation)
  - [2. Device Log Analysis](#2-device-log-analysis)
  - [3. Energy Consumption Analysis](#3-energy-consumption-analysis)
  - [4. Network Traffic Pattern Analysis](#4-network-traffic-pattern-analysis)
  - [5. Predictive Maintenance Data Preparation](#5-predictive-maintenance-data-preparation)
- [MapReduce Performance Optimization](#mapreduce-performance-optimization)
  - [1. Data Locality](#1-data-locality)
  - [2. Combiner Usage](#2-combiner-usage)
  - [3. Compression](#3-compression)
  - [4. Appropriate Number of Reducers](#4-appropriate-number-of-reducers)
  - [5. Custom Partitioner](#5-custom-partitioner)
- [Advantages of MapReduce](#advantages-of-mapreduce)
- [Limitations of MapReduce](#limitations-of-mapreduce)
- [Summary](#summary)
- [Key Takeaways for Exams](#key-takeaways-for-exams)

## Overview

MapReduce is a programming model and software framework developed by Google for processing and generating large datasets in a distributed computing environment. Hadoop MapReduce is Apache's implementation of this paradigm, enabling parallel processing of massive datasets across clusters of commodity hardware. For IoT applications, MapReduce provides the computational engine needed to analyze historical sensor data, perform batch analytics, and extract valuable insights from petabytes of device-generated information.

## What is MapReduce?

MapReduce is a programming paradigm that allows for massive scalability across hundreds or thousands of servers in a Hadoop cluster. It breaks down data processing into two main phases:

1. **Map Phase:** Processes input data and produces intermediate key-value pairs
2. **Reduce Phase:** Aggregates intermediate results to produce final output

The framework automatically handles parallelization, fault tolerance, data distribution, and load balancing, allowing developers to focus on the processing logic rather than distributed systems complexities.

### MapReduce Philosophy

**Key Principles:**

- **Divide and Conquer:** Break large problems into smaller tasks
- **Data Locality:** Move computation to data, not data to computation
- **Parallel Processing:** Execute tasks simultaneously across cluster
- **Fault Tolerance:** Automatically handle failures and retry tasks
- **Scalability:** Linear performance improvement with cluster size

## MapReduce Programming Model

### Basic Concepts

**Input Data:**

- Stored in HDFS as files
- Split into fixed-size blocks (128MB default)
- Each split processed independently

**Key-Value Pairs:**

- Basic data structure in MapReduce
- Map produces: (key, value)
- Reduce consumes: (key, list of values)

**Functional Programming:**

- Map and Reduce are pure functions
- No side effects
- Predictable and testable

### MapReduce Phases

```
Input Data → Split → Map → Shuffle/Sort → Reduce → Output

Phase 1: INPUT SPLIT
┌─────────────┐
│ File Block1 │ → Split 1
│ File Block2 │ → Split 2
│ File Block3 │ → Split 3
└─────────────┘

Phase 2: MAP
Split 1 → Mapper 1 → (k1, v1), (k2, v2)
Split 2 → Mapper 2 → (k1, v3), (k3, v4)
Split 3 → Mapper 3 → (k2, v5), (k3, v6)

Phase 3: SHUFFLE & SORT
(k1, v1), (k1, v3) → (k1, [v1, v3])
(k2, v2), (k2, v5) → (k2, [v2, v5])
(k3, v4), (k3, v6) → (k3, [v4, v6])

Phase 4: REDUCE
(k1, [v1, v3]) → Reducer 1 → (k1, result1)
(k2, [v2, v5]) → Reducer 2 → (k2, result2)
(k3, [v4, v6]) → Reducer 3 → (k3, result3)

Phase 5: OUTPUT
Results written to HDFS
```

## Map Phase

The Map phase is the first processing stage where input data is transformed into intermediate key-value pairs.

### Map Function

```java
map(key, value) → list(intermediate_key, intermediate_value)
```

**Characteristics:**

- Processes one input record at a time
- Produces zero or more key-value pairs
- Stateless operation (no communication between mappers)
- Runs in parallel across cluster nodes

### Map Process Flow

**1. Input Split Reading:**

```
Input: (offset, line)
offset = byte position in file
line = text content
```

**2. Map Execution:**

```
For each input record:
  - Parse and process data
  - Extract relevant information
  - Emit key-value pairs
```

**3. In-Memory Buffering:**

- Mapper output buffered in memory (100MB default)
- Sorted by key in memory
- Spilled to disk when buffer full

### Map Example: Word Count

```java
// Input: (0, "hello world")
// Input: (12, "hello hadoop")

map(lineOffset, lineText):
  words = lineText.split(" ")
  for word in words:
    emit(word, 1)

// Output from Mapper 1:
// ("hello", 1)
// ("world", 1)

// Output from Mapper 2:
// ("hello", 1)
// ("hadoop", 1)
```

### IoT Map Examples

**Temperature Sensor Analysis:**

```java
// Input: "2024-01-15,sensor1,25.5"

map(offset, record):
  fields = record.split(",")
  date = fields[0]
  sensor = fields[1]
  temperature = fields[2]
  emit(sensor, temperature)

// Output: ("sensor1", "25.5")
```

**Device Status Monitoring:**

```java
// Input: "device123,online,timestamp"

map(offset, record):
  fields = record.split(",")
  device = fields[0]
  status = fields[1]
  emit(status, 1)  // Count devices by status

// Output: ("online", 1)
```

## Shuffle and Sort Phase

The Shuffle and Sort phase is the intermediary step between Map and Reduce, organizing data for efficient aggregation.

### Shuffle Process

**Purpose:**

- Transfer mapper outputs to reducers
- Group all values for same key together
- Ensure each reducer gets complete data for its keys

**Steps:**

**1. Partition:**

```
Partitioner determines which reducer gets which keys

Default: hash(key) mod num_reducers

Example:
hash("sensor1") mod 3 = Reducer 0
hash("sensor2") mod 3 = Reducer 1
hash("sensor3") mod 3 = Reducer 2
```

**2. Transfer:**

```
Network transfer from mappers to reducers
- Most expensive MapReduce operation
- Optimization critical for performance
```

**3. Merge:**

```
Reducer receives data from multiple mappers
- Merge-sort algorithm
- Maintains sorted order
- Handles large volumes efficiently
```

### Sort Process

**Characteristics:**

- Automatic sorting by key
- Happens during shuffle phase
- Uses external merge-sort for large data
- Ensures ordered input to reducers

**Sorting Example:**

```
Mapper Outputs (unsorted):
("sensor2", 23.5)
("sensor1", 25.0)
("sensor2", 24.0)
("sensor1", 26.5)

After Shuffle & Sort:
("sensor1", [25.0, 26.5])
("sensor2", [23.5, 24.0])
```

### Combiner (Optional)

A combiner is a local reducer that runs on the mapper node to reduce data transfer.

```java
// Before Combiner:
Mapper output: ("hello", 1), ("hello", 1), ("hello", 1)
Network transfer: 3 records

// After Combiner:
Combiner output: ("hello", 3)
Network transfer: 1 record

// Reducer sees: ("hello", [3, 5, 2])
// Instead of: ("hello", [1,1,1,1,1,1,1,1,1,1])
```

**Benefits:**

- Reduces network traffic
- Improves performance
- Lower reducer load

**Limitations:**

- Only works for associative and commutative operations
- Not all problems can use combiners

## Reduce Phase

The Reduce phase aggregates intermediate values grouped by key to produce final results.

### Reduce Function

```java
reduce(key, list_of_values) → list(final_key, final_value)
```

**Characteristics:**

- Receives all values for a single key
- Processes values iteratively
- Produces final output
- Multiple reducers run in parallel

### Reduce Process Flow

**1. Input Reception:**

```
Receive: (key, [value1, value2, ..., valueN])
All values for same key grouped together
```

**2. Reduce Execution:**

```
For each key and its value list:
  - Aggregate/process values
  - Compute final result
  - Emit output key-value pair
```

**3. Output Writing:**

```
Results written to HDFS
One output file per reducer
Part-r-00000, Part-r-00001, etc.
```

### Reduce Example: Word Count

```java
// Input to Reducer:
// ("hello", [1, 1])
// ("world", [1])
// ("hadoop", [1])

reduce(word, counts):
  total = 0
  for count in counts:
    total = total + count
  emit(word, total)

// Output:
// ("hello", 2)
// ("world", 1)
// ("hadoop", 1)
```

### IoT Reduce Examples

**Average Temperature Calculation:**

```java
// Input: ("sensor1", [25.5, 26.0, 24.5, 25.0])

reduce(sensor, temperatures):
  sum = 0
  count = 0
  for temp in temperatures:
    sum = sum + temp
    count = count + 1
  average = sum / count
  emit(sensor, average)

// Output: ("sensor1", 25.25)
```

**Device Status Aggregation:**

```java
// Input: ("online", [1, 1, 1, 1, 1])
//        ("offline", [1, 1])

reduce(status, counts):
  total = sum(counts)
  emit(status, total)

// Output: ("online", 5)
//         ("offline", 2)
```

## Complete MapReduce Workflow

### Detailed Execution Flow

```
┌─────────────────────────────────────────────────────┐
│  Step 1: JOB SUBMISSION                             │
│  Client submits job to ResourceManager              │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 2: JOB INITIALIZATION                         │
│  - ApplicationMaster started                        │
│  - Input splits computed                            │
│  - Map tasks created (one per split)                │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 3: MAP TASK EXECUTION                         │
│  - Map tasks scheduled on DataNodes                 │
│  - Tasks run in parallel                            │
│  - Output buffered and sorted locally               │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 4: SHUFFLE & SORT                             │
│  - Partition mapper outputs                         │
│  - Transfer data over network                       │
│  - Merge and sort at reducers                       │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 5: REDUCE TASK EXECUTION                      │
│  - Reduce tasks process grouped data                │
│  - Final results computed                           │
│  - Output written to HDFS                           │
└──────────────────┬──────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────┐
│  Step 6: JOB COMPLETION                             │
│  - ApplicationMaster notifies client                │
│  - Cleanup temporary files                          │
│  - Job statistics reported                          │
└─────────────────────────────────────────────────────┘
```

### Task Scheduling

**Data Locality Optimization:**

```
Level 1 - Node Local (best):
  Task runs on same node as data
  No network transfer
  Highest performance

Level 2 - Rack Local (good):
  Task runs on same rack as data
  Minimal network transfer
  Good performance

Level 3 - Off-Rack (acceptable):
  Task runs on different rack
  Network transfer required
  Lower performance but necessary for load balancing
```

### Fault Tolerance

**Map Task Failures:**

```
If mapper fails:
  1. YARN detects failure (no heartbeat)
  2. Task rescheduled on different node
  3. Re-executes from beginning
  4. Uses same input split
```

**Reduce Task Failures:**

```
If reducer fails:
  1. Partial output discarded
  2. Task rescheduled
  3. Re-processes all input data
  4. Fetches mapper outputs again
```

**Node Failures:**

```
If DataNode fails:
  1. All tasks on node marked as failed
  2. Tasks rescheduled on healthy nodes
  3. HDFS provides data from replicas
  4. No data loss due to replication
```

## Classic Example: Word Count

### Problem Statement

Count the frequency of each word in a large text corpus.

### MapReduce Solution

**Input Data:**

```
File 1: "hello world hello"
File 2: "hadoop mapreduce"
File 3: "hello hadoop world"
```

**Mapper Code (Pseudocode):**

```java
class WordCountMapper:
  method map(lineOffset, lineText):
    for each word in lineText.split():
      emit(word, 1)
```

**Reducer Code (Pseudocode):**

```java
class WordCountReducer:
  method reduce(word, counts):
    sum = 0
    for count in counts:
      sum = sum + count
    emit(word, sum)
```

**Execution Trace:**

```
MAP PHASE:
---------
Mapper 1 (File 1):
  Input: "hello world hello"
  Output: (hello,1), (world,1), (hello,1)

Mapper 2 (File 2):
  Input: "hadoop mapreduce"
  Output: (hadoop,1), (mapreduce,1)

Mapper 3 (File 3):
  Input: "hello hadoop world"
  Output: (hello,1), (hadoop,1), (world,1)

SHUFFLE & SORT:
--------------
Group by key:
  hadoop: [1, 1]
  hello: [1, 1, 1]
  mapreduce: [1]
  world: [1, 1]

REDUCE PHASE:
------------
Reducer 1:
  Input: (hadoop, [1,1])
  Output: (hadoop, 2)

Reducer 2:
  Input: (hello, [1,1,1])
  Output: (hello, 3)

Reducer 3:
  Input: (mapreduce, [1])
  Output: (mapreduce, 1)

Reducer 4:
  Input: (world, [1,1])
  Output: (world, 2)

FINAL OUTPUT:
------------
hadoop      2
hello       3
mapreduce   1
world       2
```

## IoT Batch Analytics Use Cases

### 1. Sensor Data Aggregation

**Scenario:** Calculate daily average temperature for each sensor

**Input Data:**

```
2024-01-15,09:00,sensor1,25.5
2024-01-15,10:00,sensor1,26.0
2024-01-15,09:00,sensor2,23.0
2024-01-15,10:00,sensor2,24.5
```

**MapReduce Implementation:**

```java
// Mapper
map(offset, record):
  fields = record.split(",")
  date = fields[0]
  sensor = fields[2]
  temperature = float(fields[3])
  key = date + "," + sensor
  emit(key, temperature)

// Output: ("2024-01-15,sensor1", 25.5)
//         ("2024-01-15,sensor1", 26.0)

// Reducer
reduce(key, temperatures):
  sum = 0
  count = 0
  for temp in temperatures:
    sum += temp
    count += 1
  average = sum / count
  emit(key, average)

// Output: ("2024-01-15,sensor1", 25.75)
//         ("2024-01-15,sensor2", 23.75)
```

### 2. Device Log Analysis

**Scenario:** Count error occurrences by error type

**Input Data:**

```
2024-01-15 ERROR Connection timeout device123
2024-01-15 INFO Device connected device456
2024-01-15 ERROR Memory overflow device789
2024-01-15 ERROR Connection timeout device234
```

**MapReduce Implementation:**

```java
// Mapper
map(offset, logLine):
  if "ERROR" in logLine:
    parts = logLine.split()
    errorType = " ".join(parts[2:4])
    emit(errorType, 1)

// Output: ("Connection timeout", 1)
//         ("Memory overflow", 1)
//         ("Connection timeout", 1)

// Reducer
reduce(errorType, counts):
  total = sum(counts)
  emit(errorType, total)

// Output: ("Connection timeout", 2)
//         ("Memory overflow", 1)
```

### 3. Energy Consumption Analysis

**Scenario:** Calculate total energy consumption per building

**Input Data:**

```
building_A,meter1,100.5
building_A,meter2,150.3
building_B,meter1,200.7
building_B,meter2,180.2
```

**MapReduce Implementation:**

```java
// Mapper
map(offset, record):
  fields = record.split(",")
  building = fields[0]
  consumption = float(fields[2])
  emit(building, consumption)

// Output: ("building_A", 100.5)
//         ("building_A", 150.3)

// Reducer
reduce(building, consumptions):
  total = sum(consumptions)
  emit(building, total)

// Output: ("building_A", 250.8)
//         ("building_B", 380.9)
```

### 4. Network Traffic Pattern Analysis

**Scenario:** Identify peak traffic hours

**Input Data:**

```
2024-01-15,09:00,device1,1024
2024-01-15,09:00,device2,2048
2024-01-15,10:00,device1,4096
2024-01-15,10:00,device2,3072
```

**MapReduce Implementation:**

```java
// Mapper
map(offset, record):
  fields = record.split(",")
  hour = fields[1]
  bytes = int(fields[3])
  emit(hour, bytes)

// Reducer
reduce(hour, bytesList):
  totalBytes = sum(bytesList)
  deviceCount = len(bytesList)
  avgBytes = totalBytes / deviceCount
  emit(hour, (totalBytes, avgBytes))

// Output: ("09:00", (3072, 1536))
//         ("10:00", (7168, 3584))
```

### 5. Predictive Maintenance Data Preparation

**Scenario:** Extract vibration patterns for ML training

**Input Data:**

```
machine1,sensor_vibration,timestamp1,0.05
machine1,sensor_vibration,timestamp2,0.06
machine1,sensor_temp,timestamp1,75
```

**MapReduce Implementation:**

```java
// Mapper
map(offset, record):
  fields = record.split(",")
  machine = fields[0]
  sensorType = fields[1]
  value = float(fields[3])

  if sensorType == "sensor_vibration":
    emit(machine, ("vibration", value))

// Reducer
reduce(machine, sensorData):
  vibrations = []
  for (type, value) in sensorData:
    vibrations.append(value)

  maxVibration = max(vibrations)
  avgVibration = sum(vibrations) / len(vibrations)

  emit(machine, (maxVibration, avgVibration))
```

## MapReduce Performance Optimization

### 1. Data Locality

**Technique:** Schedule tasks on nodes containing data

**Impact:**

- 10-20x faster than remote data access
- Reduces network congestion
- Improves cluster utilization

### 2. Combiner Usage

**Technique:** Local aggregation on mapper nodes

**Example:**

```
Without Combiner:
  Network transfer: 1M records

With Combiner:
  Network transfer: 1K records (1000x reduction)
```

### 3. Compression

**Technique:** Compress mapper outputs

**Benefits:**

- Reduces disk I/O
- Decreases network transfer
- Faster shuffle phase

**Codecs:**

- Snappy: Fast, moderate compression
- LZO: Good balance
- Gzip: High compression, slower

### 4. Appropriate Number of Reducers

**Guidelines:**

```
Too few reducers:
  - Slower reduce phase
  - Large output files
  - Memory issues

Too many reducers:
  - Overhead of task startup
  - Many small files
  - Inefficient processing

Optimal: 0.95 × (nodes × max containers per node)
```

### 5. Custom Partitioner

**Purpose:** Even distribution of work across reducers

**Default:**

```java
hash(key) mod num_reducers
```

**Custom:**

```java
class CustomPartitioner:
  method getPartition(key, value, numReducers):
    // Custom logic for better distribution
    return partition_number
```

## Advantages of MapReduce

1. **Simplicity:** Abstract away distributed systems complexity
2. **Scalability:** Linear performance with cluster size
3. **Fault Tolerance:** Automatic failure handling
4. **Data Locality:** Efficient data processing
5. **Cost-Effective:** Runs on commodity hardware
6. **Flexibility:** Handles various data types and formats

## Limitations of MapReduce

1. **High Latency:** Not suitable for real-time analytics
2. **Disk I/O Overhead:** Multiple read/write cycles
3. **Iterative Processing:** Inefficient for ML algorithms
4. **Programming Complexity:** Requires MapReduce thinking
5. **Limited Expressiveness:** Not all problems fit model
6. **Startup Overhead:** Small jobs have high overhead

## Summary

Hadoop MapReduce provides a powerful programming model for batch processing of large-scale IoT data. The framework divides processing into Map phase (data transformation), Shuffle/Sort phase (data organization), and Reduce phase (aggregation), with automatic parallelization and fault tolerance.

The Map phase processes input splits in parallel, producing intermediate key-value pairs. The Shuffle and Sort phase groups all values for the same key together and transfers data to reducers. The Reduce phase aggregates values to produce final results.

MapReduce excels at batch analytics for IoT applications including sensor data aggregation, log analysis, energy consumption monitoring, and historical trend analysis. While it has limitations (high latency, disk overhead), it remains fundamental for processing petabyte-scale IoT datasets.

## Key Takeaways for Exams

1. **MapReduce Phases:** Map (transformation) → Shuffle/Sort (organization) → Reduce (aggregation)

2. **Map Function:** map(key, value) → list(k2, v2); processes records independently in parallel

3. **Reduce Function:** reduce(key, list_of_values) → list(final_key, final_value); aggregates grouped data

4. **Shuffle & Sort:** Groups values by key, transfers to reducers, maintains sorted order

5. **Combiner:** Local reducer on mapper node, reduces network transfer, only for associative operations

6. **Data Locality:** Tasks scheduled on nodes with data (node-local > rack-local > off-rack)

7. **Fault Tolerance:** Failed tasks automatically rescheduled, HDFS replication ensures data availability

8. **Word Count Example:** Classic MapReduce example - map emits (word, 1), reduce sums counts

9. **IoT Use Cases:** Sensor aggregation, log analysis, energy monitoring, traffic patterns, maintenance data prep

10. **Optimization:** Use combiners, compression, appropriate reducer count, custom partitioning for performance
