# Apache Spark


## Table of Contents

- [Apache Spark](#apache-spark)
- [Overview](#overview)
- [What is Apache Spark?](#what-is-apache-spark)
  - [Key Characteristics](#key-characteristics)
- [Spark Architecture](#spark-architecture)
  - [Components Overview](#components-overview)
  - [Spark Components](#spark-components)
- [Resilient Distributed Datasets (RDDs)](#resilient-distributed-datasets-rdds)
  - [RDD Characteristics](#rdd-characteristics)
  - [RDD Operations](#rdd-operations)
- [Transformation examples](#transformation-examples)
- [Action examples](#action-examples)
  - [RDD Creation](#rdd-creation)
- [From collection](#from-collection)
- [From file](#from-file)
- [From existing RDD](#from-existing-rdd)
  - [RDD Persistence](#rdd-persistence)
- [Cache in memory](#cache-in-memory)
- [Cache with serialization](#cache-with-serialization)
- [Disk storage](#disk-storage)
- [Memory and disk](#memory-and-disk)
- [Spark Execution Model](#spark-execution-model)
  - [Lazy Evaluation](#lazy-evaluation)
- [These transformations are NOT executed immediately](#these-transformations-are-not-executed-immediately)
- [Only when action is called, entire DAG is executed](#only-when-action-is-called-entire-dag-is-executed)
  - [DAG (Directed Acyclic Graph)](#dag-directed-acyclic-graph)
  - [Stages and Tasks](#stages-and-tasks)
- [Spark SQL](#spark-sql)
  - [DataFrames](#dataframes)
- [Create DataFrame from JSON](#create-dataframe-from-json)
- [Show schema](#show-schema)
- [root](#root)
- [|-- sensor_id: string](#---sensorid-string)
- [|-- temperature: double](#---temperature-double)
- [|-- timestamp: timestamp](#---timestamp-timestamp)
- [Query operations](#query-operations)
  - [SQL Queries](#sql-queries)
- [Register as temporary view](#register-as-temporary-view)
- [Run SQL queries](#run-sql-queries)
  - [IoT Data Processing Example](#iot-data-processing-example)
- [Read sensor data](#read-sensor-data)
- [Data cleaning](#data-cleaning)
- [Aggregation](#aggregation)
- [Save results](#save-results)
- [Spark Streaming](#spark-streaming)
  - [DStream (Discretized Stream)](#dstream-discretized-stream)
  - [Streaming Example](#streaming-example)
- [Create streaming context with 1-second batch interval](#create-streaming-context-with-1-second-batch-interval)
- [Create DStream from socket](#create-dstream-from-socket)
- [Word count on stream](#word-count-on-stream)
- [Print results](#print-results)
- [Start streaming](#start-streaming)
  - [IoT Streaming Example](#iot-streaming-example)
- [Read from Kafka topic](#read-from-kafka-topic)
- [Parse sensor data](#parse-sensor-data)
- [Filter anomalies](#filter-anomalies)
- [Generate alerts](#generate-alerts)
- [Save to HDFS](#save-to-hdfs)
  - [Windowed Operations](#windowed-operations)
- [Sliding window: 30-second window, 10-second slide](#sliding-window-30-second-window-10-second-slide)
- [MLlib - Machine Learning Library](#mllib---machine-learning-library)
  - [ML Algorithms](#ml-algorithms)
  - [Predictive Maintenance Example](#predictive-maintenance-example)
- [Load training data](#load-training-data)
- [Feature engineering](#feature-engineering)
- [Train model](#train-model)
- [Make predictions](#make-predictions)
- [Evaluate](#evaluate)
- [Save model](#save-model)
- [Advantages of Spark over MapReduce](#advantages-of-spark-over-mapreduce)
  - [Performance Comparison](#performance-comparison)
  - [Why Spark for IoT?](#why-spark-for-iot)
- [Spark Deployment Modes](#spark-deployment-modes)
  - [1. Local Mode](#1-local-mode)
  - [2. Standalone Cluster](#2-standalone-cluster)
  - [3. YARN Cluster](#3-yarn-cluster)
  - [4. Kubernetes](#4-kubernetes)
- [IoT Use Cases with Spark](#iot-use-cases-with-spark)
  - [1. Smart City Traffic Analysis](#1-smart-city-traffic-analysis)
- [Real-time traffic analysis](#real-time-traffic-analysis)
- [Parse and analyze](#parse-and-analyze)
- [Aggregate by location](#aggregate-by-location)
- [Write to dashboard](#write-to-dashboard)
  - [2. Predictive Maintenance](#2-predictive-maintenance)
- [Historical sensor data](#historical-sensor-data)
- [Feature extraction](#feature-extraction)
- [Train classifier](#train-classifier)
- [Real-time prediction](#real-time-prediction)
  - [3. Energy Consumption Optimization](#3-energy-consumption-optimization)
- [Smart meter data](#smart-meter-data)
- [Hourly consumption patterns](#hourly-consumption-patterns)
- [Identify high consumers](#identify-high-consumers)
- [Recommendations](#recommendations)
- [Spark Optimization Techniques](#spark-optimization-techniques)
  - [1. Caching/Persistence](#1-cachingpersistence)
- [Cache frequently accessed data](#cache-frequently-accessed-data)
- [Different storage levels](#different-storage-levels)
  - [2. Partitioning](#2-partitioning)
- [Repartition for better parallelism](#repartition-for-better-parallelism)
- [Partition by key for joins](#partition-by-key-for-joins)
  - [3. Broadcasting](#3-broadcasting)
- [Broadcast small lookup tables](#broadcast-small-lookup-tables)
- [Use in transformations](#use-in-transformations)
  - [4. Avoiding Shuffles](#4-avoiding-shuffles)
- [Bad: Multiple shuffles](#bad-multiple-shuffles)
- [Better: Single aggregation](#better-single-aggregation)
- [Summary](#summary)
- [Key Takeaways for Exams](#key-takeaways-for-exams)

## Overview

Apache Spark is a unified analytics engine for large-scale data processing that provides high-performance batch and stream processing capabilities. Developed at UC Berkeley in 2009 and donated to Apache in 2013, Spark has become one of the most popular big data processing frameworks. Unlike Hadoop MapReduce which relies on disk I/O, Spark performs in-memory computations, achieving 10-100x faster performance for iterative algorithms and interactive data analysis—critical capabilities for IoT analytics where real-time insights and machine learning are essential.

## What is Apache Spark?

Apache Spark is a fast, general-purpose cluster computing system that provides high-level APIs in Java, Scala, Python, and R. It offers a unified programming model that spans batch processing, interactive queries, streaming analytics, and machine learning.

### Key Characteristics

**1. In-Memory Computing:**

- Data cached in memory across operations
- Avoids repeated disk I/O
- 10-100x faster than MapReduce for iterative jobs

**2. Unified Platform:**

- Batch processing (Spark Core, Spark SQL)
- Stream processing (Spark Streaming)
- Machine learning (MLlib)
- Graph processing (GraphX)

**3. Ease of Use:**

- High-level APIs (Python, Scala, Java, R)
- Interactive shell for exploration
- Rich set of built-in functions

**4. Fault Tolerance:**

- Resilient Distributed Datasets (RDDs)
- Lineage-based recovery
- Automatic recomputation on failure

**5. Scalability:**

- Runs on clusters from 1 to 10,000+ nodes
- Processes petabytes of data
- Dynamic resource allocation

## Spark Architecture

### Components Overview

```
┌──────────────────────────────────────────────────────┐
│                  Spark Application                   │
├──────────────────────────────────────────────────────┤
│                    Driver Program                    │
│              ┌────────────────────┐                  │
│              │   SparkContext     │                  │
│              └─────────┬──────────┘                  │
└────────────────────────┼───────────────────────────  ┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ Cluster       │ │               │ │               │
│ Manager       │ │  Worker Node  │ │  Worker Node  │
│ (YARN/Mesos/  │ │ ┌───────────┐ │ │ ┌───────────┐ │
│  Standalone)  │ │ │ Executor  │ │ │ │ Executor  │ │
└───────────────┘ │ │  - Task 1 │ │ │ │  - Task 3 │ │
                  │ │  - Task 2 │ │ │ │  - Task 4 │ │
                  │ │  - Cache  │ │ │ │  - Cache  │ │
                  │ └───────────┘ │ │ └───────────┘ │
                  └───────────────┘ └───────────────┘
```

### Spark Components

**1. Driver Program:**

- Main control of Spark application
- Creates SparkContext
- Transforms user code into tasks
- Schedules tasks on executors
- Collects results

**2. SparkContext:**

- Entry point to Spark functionality
- Connects to cluster manager
- Coordinates job execution
- Manages RDD operations

**3. Cluster Manager:**

- Allocates resources across applications
- Options: YARN, Mesos, Kubernetes, Standalone
- Manages cluster nodes
- Monitors resource usage

**4. Worker Nodes:**

- Execute application code
- Store data for processing
- Report status to driver
- Contain one or more executors

**5. Executors:**

- Process assigned to worker node
- Runs tasks in threads
- Stores data in memory/disk cache
- Communicates results to driver

## Resilient Distributed Datasets (RDDs)

RDDs are the fundamental data structure of Spark—an immutable, distributed collection of objects that can be processed in parallel.

### RDD Characteristics

**1. Resilient:**

- Fault-tolerant through lineage
- Automatic recovery from failures
- Recomputes lost partitions

**2. Distributed:**

- Data partitioned across cluster
- Parallel processing
- Data locality optimization

**3. Immutable:**

- Once created, cannot be changed
- Transformations create new RDDs
- Enables lineage tracking

### RDD Operations

**Transformations (Lazy):**

- Create new RDD from existing one
- Not executed immediately
- Build computation DAG

```python
# Transformation examples
rdd2 = rdd1.map(lambda x: x * 2)      # Apply function
rdd3 = rdd1.filter(lambda x: x > 10)  # Filter elements
rdd4 = rdd1.flatMap(lambda x: x.split()) # Flatten
rdd5 = rdd1.union(rdd2)               # Combine RDDs
rdd6 = rdd1.distinct()                # Remove duplicates
```

**Actions (Eager):**

- Trigger computation and return results
- Execute transformations in DAG
- Produce non-RDD values

```python
# Action examples
count = rdd.count()                   # Count elements
result = rdd.collect()                # Collect to driver
first = rdd.first()                   # Get first element
taken = rdd.take(10)                  # Take n elements
reduced = rdd.reduce(lambda a,b: a+b) # Aggregate
```

### RDD Creation

```python
# From collection
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# From file
rdd = sc.textFile("hdfs://path/to/file.txt")

# From existing RDD
rdd2 = rdd.map(lambda x: x * 2)
```

### RDD Persistence

```python
# Cache in memory
rdd.cache()  # or rdd.persist(StorageLevel.MEMORY_ONLY)

# Cache with serialization
rdd.persist(StorageLevel.MEMORY_ONLY_SER)

# Disk storage
rdd.persist(StorageLevel.DISK_ONLY)

# Memory and disk
rdd.persist(StorageLevel.MEMORY_AND_DISK)
```

## Spark Execution Model

### Lazy Evaluation

Spark uses lazy evaluation for transformations:

```python
# These transformations are NOT executed immediately
rdd1 = sc.textFile("sensors.log")
rdd2 = rdd1.filter(lambda line: "ERROR" in line)
rdd3 = rdd2.map(lambda line: line.split())

# Only when action is called, entire DAG is executed
result = rdd3.count()  # NOW all transformations execute
```

**Benefits:**

- Optimization of execution plan
- Avoids unnecessary computations
- Efficient pipelining of operations
- Reduced memory usage

### DAG (Directed Acyclic Graph)

Spark builds a DAG of operations:

```
Input RDD
    │
    ├─► filter() ──► map() ──► reduceByKey() ──► collect()
    │                                              (Action)
    └─► Transformations (Lazy) ──────────────────► Execution
```

### Stages and Tasks

**Stage:** Set of tasks that can be executed together

**Task:** Unit of work sent to executor

```
Job (triggered by action)
├─── Stage 1 (wide transformation boundary)
│    ├─── Task 1.1 (partition 1)
│    ├─── Task 1.2 (partition 2)
│    └─── Task 1.3 (partition 3)
└─── Stage 2
     ├─── Task 2.1
     └─── Task 2.2
```

## Spark SQL

Spark SQL provides a programming interface for working with structured and semi-structured data.

### DataFrames

Higher-level abstraction than RDDs with schema:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IoTAnalytics").getOrCreate()

# Create DataFrame from JSON
df = spark.read.json("sensors.json")

# Show schema
df.printSchema()
# root
#  |-- sensor_id: string
#  |-- temperature: double
#  |-- timestamp: timestamp

# Query operations
df.select("sensor_id", "temperature").show()
df.filter(df.temperature > 25).show()
df.groupBy("sensor_id").avg("temperature").show()
```

### SQL Queries

```python
# Register as temporary view
df.createOrReplaceTempView("sensors")

# Run SQL queries
result = spark.sql("""
    SELECT sensor_id, AVG(temperature) as avg_temp
    FROM sensors
    WHERE temperature > 20
    GROUP BY sensor_id
    ORDER BY avg_temp DESC
""")

result.show()
```

### IoT Data Processing Example

```python
# Read sensor data
sensor_df = spark.read \
    .option("header", "true") \
    .csv("hdfs://sensors/data/*.csv")

# Data cleaning
clean_df = sensor_df \
    .filter(sensor_df.temperature.isNotNull()) \
    .filter(sensor_df.temperature > -50) \
    .filter(sensor_df.temperature < 100)

# Aggregation
daily_avg = clean_df \
    .groupBy("sensor_id", "date") \
    .agg(
        avg("temperature").alias("avg_temp"),
        max("temperature").alias("max_temp"),
        min("temperature").alias("min_temp")
    )

# Save results
daily_avg.write \
    .mode("overwrite") \
    .parquet("hdfs://output/daily_analysis")
```

## Spark Streaming

Spark Streaming enables scalable, high-throughput, fault-tolerant stream processing.

### DStream (Discretized Stream)

Continuous stream divided into micro-batches:

```
Input Stream
    │
    ├─── Batch 1 (RDD) ────┐
    ├─── Batch 2 (RDD) ────┤
    ├─── Batch 3 (RDD) ────┼─► Processing
    ├─── Batch 4 (RDD) ────┤
    └─── Batch 5 (RDD) ────┘
```

### Streaming Example

```python
from pyspark.streaming import StreamingContext

# Create streaming context with 1-second batch interval
ssc = StreamingContext(sc, 1)

# Create DStream from socket
lines = ssc.socketTextStream("localhost", 9999)

# Word count on stream
words = lines.flatMap(lambda line: line.split())
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda a, b: a + b)

# Print results
wordCounts.pprint()

# Start streaming
ssc.start()
ssc.awaitTermination()
```

### IoT Streaming Example

```python
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

ssc = StreamingContext(sc, 10)  # 10-second batches

# Read from Kafka topic
kafka_stream = KafkaUtils.createStream(
    ssc,
    "localhost:2181",
    "spark-streaming-consumer",
    {"iot-sensors": 1}
)

# Parse sensor data
sensor_data = kafka_stream.map(lambda x: json.loads(x[1]))

# Filter anomalies
anomalies = sensor_data.filter(
    lambda data: data['temperature'] > 50 or data['temperature'] < 0
)

# Generate alerts
alerts = anomalies.map(lambda data: {
    'sensor_id': data['sensor_id'],
    'alert': 'Temperature anomaly',
    'value': data['temperature'],
    'timestamp': data['timestamp']
})

# Save to HDFS
alerts.foreachRDD(lambda rdd:
    rdd.saveAsTextFile(f"hdfs://alerts/{time.time()}")
)

ssc.start()
ssc.awaitTermination()
```

### Windowed Operations

```python
# Sliding window: 30-second window, 10-second slide
windowed_counts = pairs \
    .reduceByKeyAndWindow(
        lambda a, b: a + b,
        lambda a, b: a - b,
        30,  # window duration
        10   # slide duration
    )
```

## MLlib - Machine Learning Library

MLlib provides scalable machine learning algorithms for IoT predictive analytics.

### ML Algorithms

**1. Classification:**

- Logistic Regression
- Decision Trees
- Random Forests
- Naive Bayes

**2. Regression:**

- Linear Regression
- Decision Tree Regression
- Random Forest Regression

**3. Clustering:**

- K-means
- Gaussian Mixture
- Bisecting K-means

**4. Collaborative Filtering:**

- Alternating Least Squares (ALS)

### Predictive Maintenance Example

```python
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# Load training data
sensor_data = spark.read.parquet("hdfs://machine_sensors/")

# Feature engineering
assembler = VectorAssembler(
    inputCols=['vibration', 'temperature', 'pressure', 'rpm'],
    outputCol='features'
)

training_data = assembler.transform(sensor_data)

# Train model
rf = RandomForestRegressor(
    featuresCol='features',
    labelCol='remaining_useful_life',
    numTrees=100
)

model = rf.fit(training_data)

# Make predictions
predictions = model.transform(test_data)

# Evaluate
evaluator = RegressionEvaluator(
    labelCol='remaining_useful_life',
    predictionCol='prediction',
    metricName='rmse'
)

rmse = evaluator.evaluate(predictions)
print(f"RMSE: {rmse}")

# Save model
model.save("hdfs://models/predictive_maintenance")
```

## Advantages of Spark over MapReduce

### Performance Comparison

| Aspect                  | Spark                 | MapReduce    |
| ----------------------- | --------------------- | ------------ |
| **Speed**               | 10-100x faster        | Baseline     |
| **Memory Usage**        | In-memory caching     | Disk-based   |
| **Iterative Jobs**      | Efficient (ML, graph) | Very slow    |
| **Interactive Queries** | Sub-second latency    | Minutes      |
| **Ease of Use**         | High-level APIs       | Verbose code |
| **Unified Platform**    | Batch + Stream + ML   | Batch only   |

### Why Spark for IoT?

**1. Real-Time Analytics:**

- Spark Streaming for near real-time processing
- Sub-second latency for critical decisions
- Continuous query processing

**2. Machine Learning:**

- MLlib for predictive models
- Iterative algorithms efficient
- Model training on large datasets

**3. Unified Processing:**

- Same framework for batch and stream
- Simplified architecture
- Code reuse across workloads

**4. Performance:**

- In-memory computation
- Optimized execution plans
- Efficient for complex workflows

**5. Ease of Development:**

- Python, Scala, Java, R APIs
- Interactive shell for experimentation
- Rich ecosystem of libraries

## Spark Deployment Modes

### 1. Local Mode

```python
spark = SparkSession.builder \
    .master("local[*]")  # Use all cores \
    .appName("IoTApp") \
    .getOrCreate()
```

### 2. Standalone Cluster

```python
spark = SparkSession.builder \
    .master("spark://master:7077") \
    .appName("IoTApp") \
    .getOrCreate()
```

### 3. YARN Cluster

```bash
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --num-executors 10 \
    --executor-memory 4G \
    --executor-cores 2 \
    app.py
```

### 4. Kubernetes

```bash
spark-submit \
    --master k8s://https://kubernetes:443 \
    --deploy-mode cluster \
    --name iot-analytics \
    app.py
```

## IoT Use Cases with Spark

### 1. Smart City Traffic Analysis

```python
# Real-time traffic analysis
traffic_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "traffic-sensors") \
    .load()

# Parse and analyze
traffic_data = traffic_stream.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*")

# Aggregate by location
congestion = traffic_data \
    .groupBy(window("timestamp", "5 minutes"), "location") \
    .agg(avg("vehicle_count").alias("avg_vehicles"))

# Write to dashboard
query = congestion.writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()
```

### 2. Predictive Maintenance

```python
# Historical sensor data
sensor_df = spark.read.parquet("hdfs://machines/sensors/")

# Feature extraction
features = sensor_df.select(
    'machine_id',
    'vibration',
    'temperature',
    'pressure',
    'rpm',
    'failure_occurred'
)

# Train classifier
from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(labelCol='failure_occurred')
model = lr.fit(training_data)

# Real-time prediction
stream = spark.readStream.format("kafka")...
predictions = model.transform(stream)
```

### 3. Energy Consumption Optimization

```python
# Smart meter data
meter_df = spark.read.json("hdfs://smart_meters/")

# Hourly consumption patterns
hourly_consumption = meter_df \
    .groupBy("meter_id", hour("timestamp").alias("hour")) \
    .agg(sum("kwh").alias("total_kwh"))

# Identify high consumers
high_consumers = hourly_consumption \
    .filter(col("total_kwh") > 100) \
    .orderBy(desc("total_kwh"))

# Recommendations
recommendations = high_consumers.join(
    consumption_profiles, "meter_id"
).select("meter_id", "optimization_tips")
```

## Spark Optimization Techniques

### 1. Caching/Persistence

```python
# Cache frequently accessed data
sensor_df.cache()

# Different storage levels
sensor_df.persist(StorageLevel.MEMORY_AND_DISK)
```

### 2. Partitioning

```python
# Repartition for better parallelism
df.repartition(100)

# Partition by key for joins
df.repartition("sensor_id")
```

### 3. Broadcasting

```python
# Broadcast small lookup tables
broadcast_var = sc.broadcast(lookup_dict)

# Use in transformations
rdd.map(lambda x: broadcast_var.value.get(x))
```

### 4. Avoiding Shuffles

```python
# Bad: Multiple shuffles
df.groupBy("key1").sum() \
  .groupBy("key2").sum()

# Better: Single aggregation
df.groupBy("key1", "key2").sum()
```

## Summary

Apache Spark is a unified analytics engine providing high-performance batch and stream processing through in-memory computation. Its core abstraction, RDDs, enables fault-tolerant distributed data processing with lazy evaluation and lineage-based recovery.

Spark's architecture consists of Driver, Executors, and Cluster Manager, executing tasks in parallel across worker nodes. Key components include Spark SQL for structured data, Spark Streaming for real-time processing, and MLlib for machine learning.

For IoT applications, Spark offers 10-100x faster performance than MapReduce, unified batch and stream processing, and integrated machine learning capabilities. It excels at real-time analytics, predictive maintenance, and large-scale data processing, making it ideal for modern IoT platforms.

## Key Takeaways for Exams

1. **Spark Definition:** Unified analytics engine with in-memory computing, 10-100x faster than MapReduce

2. **RDD:** Resilient Distributed Dataset - immutable, distributed, fault-tolerant collection

3. **Architecture:** Driver (SparkContext) → Cluster Manager → Executors (on Worker Nodes)

4. **Operations:** Transformations (lazy: map, filter) + Actions (eager: count, collect)

5. **Lazy Evaluation:** Transformations build DAG, execution deferred until action

6. **Components:** Spark Core, Spark SQL, Spark Streaming, MLlib, GraphX

7. **Spark Streaming:** Micro-batch processing with DStreams, near real-time analytics

8. **MLlib:** Machine learning library with classification, regression, clustering algorithms

9. **Advantages:** In-memory, unified platform, ease of use, iterative efficiency, interactive queries

10. **IoT Use Cases:** Traffic analysis, predictive maintenance, energy optimization, anomaly detection
