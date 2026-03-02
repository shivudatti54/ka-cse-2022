# Stream Processing

## Introduction
Stream processing is a paradigm for real-time data analysis where continuous data streams are processed with millisecond latency. Unlike traditional batch processing that handles data in large chunks, stream processing enables immediate insights from high-velocity data sources like IoT sensors, financial transactions, and social media feeds.

In cloud computing and big data architectures, stream processing solves critical challenges in fraud detection, algorithmic trading, and predictive maintenance. For instance, PayPal processes 1.4 million transactions/hour using Apache Flink for real-time fraud analysis. The technology's importance has grown with 5G networks and edge computing, requiring sub-second response times across distributed systems.

Key differentiators from batch processing include:
- Event-time processing for out-of-order data
- Stateful computations across unbounded datasets
- Exactly-once processing semantics
- Horizontal scalability in cloud environments

## Key Concepts
1. **Data Streams**: Unbounded sequences of events with timestamps (e.g., stock ticks, server logs). Implemented via Apache Kafka/Pulsar.

2. **Event Time vs Processing Time**:
   - Event Time: When event occurred (source clock)
   - Processing Time: When system receives event (server clock)
   *Critical for handling network delays in distributed systems*

3. **Windowing Techniques**:
   - Tumbling Window: Fixed-size, non-overlapping (e.g., 1-minute aggregates)
   - Sliding Window: Fixed-size with overlap (e.g., 1-min window sliding every 30s)
   - Session Window: Activity-based grouping (e.g., user web sessions)

4. **State Management**:
   - Operator State: Local to parallel task (e.g., count per server)
   - Keyed State: Partitioned by key (e.g., user session counters)
   *Managed via RocksDB in Apache Flink*

5. **Fault Tolerance**:
   - Checkpointing: Periodic snapshots of operator state
   - Watermarks: Event-time progress indicators handling late data
   *Apache Flink uses Chandy-Lamport algorithm for distributed snapshots*

6. **Stream Processing Frameworks**:
   - Apache Flink: Hybrid batch/stream engine with stateful computations
   - Kafka Streams: Library for building Kafka-native apps
   - Spark Structured Streaming: Micro-batch approach

## Examples

**Example 1: Real-Time Fraud Detection with Apache Flink**
```java
DataStream<Transaction> transactions = env.addSource(kafkaSource);

Pattern<Transaction, ?> fraudPattern = Pattern.<Transaction>begin("start")
    .where(new SimpleCondition<>() {
        public boolean filter(Transaction t) {
            return t.getAmount() > 10000;
        }
    })
    .next("follow")
    .within(Time.seconds(10));

PatternStream<Transaction> patternStream = CEP.pattern(
    transactions.keyBy(Transaction::getUserId), 
    fraudPattern
);

patternStream.process(new FraudAlertFunction()).addSector(alertSink);
```
*Steps:*
1. Consume transactions from Kafka
2. Define pattern: >$10k transaction followed by another within 10s
3. Key by user ID for state partitioning
4. Generate alerts using Complex Event Processing (CEP)

**Example 2: IoT Sensor Aggregation**
Problem: Calculate average temperature from 10,000 sensors every 15s with 99.9% uptime.

Solution:
```python
# Using PyFlink
t_env = StreamTableEnvironment.create(env)

t_env.execute_sql("""
    CREATE TABLE sensor_data (
        sensor_id STRING,
        temperature DOUBLE,
        ts TIMESTAMP(3),
        WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
    ) WITH (...)
""")

result = t_env.sql_query("""
    SELECT 
        TUMBLE_START(ts, INTERVAL '15' SECOND) as window_start,
        AVG(temperature) as avg_temp
    FROM sensor_data
    GROUP BY TUMBLE(ts, INTERVAL '15' SECOND)
""")
```
*Uses event-time processing with 5s watermark delay*

**Example 3: Social Media Trend Analysis**
Tools: Kafka Streams + Redis
1. Ingest tweets via Kafka Producer
2. Apply KStreams topology:
   - Filter for hashtags
   - Count occurrences in 5-min tumbling windows
   - Store results in Redis for dashboard queries
3. Scale using Kafka partitions

## Exam Tips
1. **Always mention event-time processing** when discussing stream vs batch
2. **Compare window types** with real examples (tumbling vs sliding vs session)
3. **Explain watermarks** using diagram: handles late data via time thresholds
4. **Flink vs Spark Streaming**: True streaming vs micro-batch architectures
5. **State management** questions: Discuss checkpointing and state backends
6. **Fault tolerance mechanisms**: Checkpointing vs record acknowledgments
7. **Use case analysis**: Prepare 2-3 industry examples (e.g., Uber surge pricing)