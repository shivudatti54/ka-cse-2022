# Real-Time Data Analysis with Apache Storm

## 1. Introduction to Apache Storm

Apache Storm is a distributed real-time stream processing system designed for processing unbounded data streams with low latency and high throughput. Originally developed by Twitter and now Apache top-level project, Storm provides exactly-once processing semantics with fault tolerance guarantees essential for mission-critical IoT applications.

### 1.1 Formal Definition of Storm Architecture

**Definition 1.1 (Storm Topology):** A Storm topology is a directed acyclic graph (DAG) of computation nodes consisting of **spouts** (data sources) and **bolts** (processing nodes), connected by stream groupings.

**Definition 1.2 (Tuple):** The fundamental data unit in Storm is a tuple—a named list of values of arbitrary types. Each tuple carries a unique 64-bit message ID used for tracking processing guarantees.

**Definition 1.3 (Stream):** A stream is an unbounded sequence of tuples with a defined schema, processed in parallel across the topology.

### 1.2 Storm Cluster Architecture

Storm employs a master-worker architecture with the following components:

| Component  | Function                                 | Role                 |
| ---------- | ---------------------------------------- | -------------------- |
| Nimbus     | Resource allocation, topology submission | Master Node          |
| ZooKeeper  | Coordination, state management           | Coordination Service |
| Supervisor | Worker process management                | Worker Node          |
| Worker     | Task execution within JVM                | Execution Container  |

The **acker mechanism** provides end-to-end reliability by tracking the tuple tree rooted at each spout tuple. When all tuples in the tree are successfully processed, the root tuple is acknowledged, ensuring exactly-once semantics.

## 2. Theoretical Foundations of Stream Processing

### 2.1 Processing Semantics

**Theorem 2.1 (At-Least-Once Delivery):** If a spout emits tuple `t` with message ID `m`, and all downstream bolts anchor and acknowledge tuples derived from `t`, then `t` will be processed at least once.

_Proof:_ The acker maintains a mapping from `m` to a 64-bit value representing the XOR of all tuple IDs in the tree. Each bolt anchors to incoming tuples by including their IDs in outgoing tuple anchors. Upon acknowledgment, the acker XORs the anchor ID with its stored value. When the value becomes zero, all tuples in the tree have been acknowledged. If any tuple fails (timeout or explicit fail), the root tuple is replayed. ∎

**Corollary 2.2 (Exactly-Once Semantics):** Storm provides exactly-once semantics when combined with a transactional Trident topology or external idempotent state management.

### 2.2 Parallelism Model

**Definition 2.4 (Parallelism Hierarchy):**

- **Worker Processes:** JVM processes running on supervisor nodes (configured via `num_workers`)
- **Executors:** Threads within workers executing spout/bolt instances (configured via `setParallelism`)
- **Tasks:** Actual tuple processing objects (configured via `setNumTasks`)

The relationship: `num_tasks ≥ parallelism`, where each executor runs at least one task.

**Theorem 2.5 (Throughput Bound):** For a topology with spout parallelism `P_s` and bolt parallelism `P_b` connected by a field grouping on key `k`, maximum throughput is bounded by:

`T_max ≤ min(P_s, P_b) × (C / H_k)`

where `C` is the channel capacity and `H_k` is the hash distribution entropy of key `k`.

_Proof:_ Field grouping ensures all tuples with the same key value are processed by the same bolt task, establishing a total ordering constraint. The bottleneck occurs at the partition with maximum load. With uniform key distribution, throughput scales linearly with parallelism; skewed distributions reduce effective parallelism by `H_k ∈ (0, 1]`. ∎

## 3. IoT Streaming Architecture

### 3.1 Architectural Pattern for IoT Data Ingestion

```
┌─────────────────────────────────────────────────────────────────┐
│ IoT Data Pipeline Architecture │
├─────────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐ │
│ │ Sensors/ │ │ Message │ │ Storm Cluster │ │
│ │ Devices │───►│ Broker │───►│ (Processing) │ │
│ │ (Raw Data) │ │ (Kafka/ │ │ │ │
│ └──────────────┘ │ MQTT) │ │ ┌────────────┐ │ │
│ └──────────────┘ │ │ Spout │ │ │
│ │ └────────────┘ │ │
│ │ ┌────────────┐ │ │
│ │ │ Bolts │ │ │
│ │ └────────────┘ │ │
│ └──────────────────┘ │
│ │ │
│ ┌─────────────────────────────┼─────────────┐ │
│ │ │ │ │
│ ▼ ▼ ▼ │
│ ┌─────────────┐ ┌────────────┐ ┌─────────┐ │
│ │ Real-time │ │ Long-term│ │ Alerts │ │
│ │ Dashboard │ │ Storage │ │ System │ │
│ └─────────────┘ │ (HDFS/Cass)│ └─────────┘ │
│ └────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Design Principles for IoT Topologies

**Principle 1 (Partitioning Strategy):** Field grouping should be applied on device_id or sensor_id for stateful operations requiring historical context, ensuring related tuples maintain processing order.

**Principle 2 (Parallelism Tuning):** Initial parallelism should be set conservatively: `P = ceil(peak_throughput / single_task_throughput)`. Monitor `complete-latency` metric and adjust dynamically.

**Principle 3 (Fault Tolerance):** Configure acker executors using formula: `acker_executors = max(1, num_workers × 2)`. Set tuple timeout to `max_processing_time × 1.5`.

**Principle 4 (State Management):** For windowed aggregations, use sliding windows with external state stores (Redis/HBase) when window size exceeds memory constraints.

**Principle 5 (Backpressure):** Configure `topology.max.spout.pending` to prevent executor overload: `max_pending = buffer_capacity × num_bolts × parallelism_factor`.

## 4. Complete Java Topology Implementation

### 4.1 Maven Dependencies (pom.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
 http://maven.apache.org/xsd/maven-4.0.0.xsd">
 <modelVersion>4.0.0</modelVersion>

 <groupId>com.iot.analytics</groupId>
 <artifactId>storm-industrial-monitoring</artifactId>
 <version>1.0.0</version>

 <properties>
 <storm.version>2.5.1</storm.version>
 <maven.compiler.source>11</maven.compiler.source>
 <maven.compiler.target>11</maven.compiler.target>
 </properties>

 <dependencies>
 <!-- Storm Core -->
 <dependency>
 <groupId>org.apache.storm</groupId>
 <artifactId>storm-core</artifactId>
 <version>${storm.version}</version>
 <scope>provided</scope>
 </dependency>

 <!-- Kafka Spout -->
 <dependency>
 <groupId>org.apache.storm</groupId>
 <artifactId>storm-kafka-client</artifactId>
 <version>${storm.version}</version>
 </dependency>

 <!-- Jackson for JSON -->
 <dependency>
 <groupId>com.fasterxml.jackson.core</groupId>
 <artifactId>jackson-databind</artifactId>
 <version>2.13.0</version>
 </dependency>
 </dependencies>
</project>
```

### 4.2 Sensor Data Model

```java
import java.io.Serializable;

public class SensorReading implements Serializable {
 private static final long serialVersionUID = 1L;

 private String machineId;
 private String sensorType;
 private double value;
 private long timestamp;
 private String unit;

 // Constructors, getters, setters

 public static class Builder {
 private String machineId;
 private String sensorType;
 private double value;
 private long timestamp;
 private String unit;

 public Builder machineId(String machineId) {
 this.machineId = machineId;
 return this;
 }

 public Builder sensorType(String sensorType) {
 this.sensorType = sensorType;
 return this;
 }

 public Builder value(double value) {
 this.value = value;
 return this;
 }

 public Builder timestamp(long timestamp) {
 this.timestamp = timestamp;
 return this;
 }

 public Builder unit(String unit) {
 this.unit = unit;
 return this;
 }

 public SensorReading build() {
 return new SensorReading(machineId, sensorType, value, timestamp, unit);
 }
 }

 // Getters and setters
 public String getMachineId() { return machineId; }
 public String getSensorType() { return sensorType; }
 public double getValue() { return value; }
 public long getTimestamp() { return timestamp; }
 public String getUnit() { return unit; }

 private SensorReading(String machineId, String sensorType, double value,
 long timestamp, String unit) {
 this.machineId = machineId;
 this.sensorType = sensorType;
 this.value = value;
 this.timestamp = timestamp;
 this.unit = unit;
 }
}
```

### 4.3 Kafka Spout Configuration

```java
import org.apache.storm.kafka.spout.KafkaSpout;
import org.apache.storm.kafka.spout.KafkaSpoutConfig;
import org.apache.storm.kafka.spout.RecordTranslator;
import org.apache.storm.Config;
import org.apache.storm.StormSubmitter;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.tuple.Fields;

public class IndustrialMonitorTopology {

 public static TopologyBuilder buildTopology(String kafkaBootstrapServers) {
 TopologyBuilder builder = new TopologyBuilder();

 // Configure Kafka Spout
 KafkaSpoutConfig<String, String> kafkaSpoutConfig = KafkaSpoutConfig
 .builder(kafkaBootstrapServers, "industrial-sensors")
 .setGroupId("storm-consumer-group")
 .setOffsetResetPolicy(EarliestOffsetResetPolicy.EARLIEST)
 .setRecordTranslator(RecordTranslator.of(
 (record) -> new Values(
 record.value(),
 record.timestamp()
 ),
 new Fields("json_data", "timestamp")
 ))
 .setMaxUncommittedOffsets(1000)
 .build();

 // Set spout parallelism: 4 workers for high throughput
 builder.setSpout("sensor-spout", new KafkaSpout<>(kafkaSpoutConfig), 4);

 // Add validation bolt with parallelism 8
 builder.setBolt("validation-bolt", new ValidationBolt(), 8)
 .fieldsGrouping("sensor-spout", new Fields("machine_id"));

 // Add anomaly detection bolt with parallelism 12
 builder.setBolt("anomaly-detection", new AnomalyDetectionBolt(), 12)
 .fieldsGrouping("validation-bolt", new Fields("machine_id"));

 // Add aggregation bolt with parallelism 4
 builder.setBolt("aggregation", new AggregationBolt(), 4)
 .globalGrouping("anomaly-detection");

 // Add HDFS persistence bolt
 builder.setBolt("hdfs-persist", new HDFSBolt(), 2)
 .globalGrouping("aggregation");

 // Add alert bolt for notifications
 builder.setBolt("alert-notification", new AlertBolt(), 4)
 .fieldsGrouping("anomaly-detection", new Fields("machine_id"));

 return builder;
 }

 public static void main(String[] args) throws Exception {
 String kafkaBootstrapServers = args.length > 0 ? args[0] : "localhost:9092";

 TopologyBuilder builder = buildTopology(kafkaBootstrapServers);

 Config config = new Config();
 config.setNumWorkers(4); // 4 worker processes
 config.setMaxSpoutPending(5000); // Backpressure limit
 config.setMessageTimeoutSecs(30); // 30 second timeout
 config.put(Config.TOPOLOGY_WORKERS, 4);

 StormSubmitter.submitTopology("industrial-monitor", config, builder.createTopology());
 }
}
```

### 4.4 Validation Bolt Implementation

```java
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;
import java.util.HashMap;

public class ValidationBolt extends BaseRichBolt {

 private static final Logger LOG = LoggerFactory.getLogger(ValidationBolt.class);
 private OutputCollector collector;

 // Valid sensor ranges: [min, max]
 private static final Map<String, double[]> VALID_RANGES = new HashMap<>();
 static {
 VALID_RANGES.put("vibration", new double[]{0.0, 100.0});
 VALID_RANGES.put("temperature", new double[]{-20.0, 200.0});
 VALID_RANGES.put("pressure", new double[]{0.0, 1000.0});
 }

 @Override
 public void prepare(Map stormConf, TopologyContext context,
 OutputCollector collector) {
 this.collector = collector;
 LOG.info("ValidationBolt initialized with parallelism: {}",
 context.getComponentTasks("validation-bolt").size());
 }

 @Override
 public void execute(Tuple tuple) {
 try {
 String jsonData = tuple.getStringByField("json_data");
 long timestamp = tuple.getLongByField("timestamp");

 // Parse JSON
 Map<String, Object> reading = parseJson(jsonData);

 String machineId = (String) reading.get("machine_id");
 String sensorType = (String) reading.get("sensor_type");
 double value = ((Number) reading.get("value")).doubleValue();

 // Validate sensor reading
 if (isValidReading(sensorType, value)) {
 // Emit valid reading to default stream
 collector.emit("valid-stream", tuple,
 new Values(machineId, sensorType, value, timestamp, "VALID"));
 } else {
 // Emit to error stream for logging/alerting
 collector.emit("error-stream", tuple,
 new Values(machineId, sensorType, value, timestamp, "INVALID_RANGE"));
 LOG.warn("Invalid reading: machine={}, sensor={}, value={}",
 machineId, sensorType, value);
 }

 // Acknowledge successful processing
 collector.ack(tuple);

 } catch (Exception e) {
 LOG.error("Validation error: {}", e.getMessage());
 collector.fail(tuple); // Trigger replay
 }
 }

 private boolean isValidReading(String sensorType, double value) {
 double[] range = VALID_RANGES.get(sensorType);
 if (range == null) return false;
 return value >= range[0] && value <= range[1];
 }

 private Map<String, Object> parseJson(String json) {
 // Using Jackson ObjectMapper (simplified)
 // In production, use proper JSON parsing
 return new com.fasterxml.jackson.databind.ObjectMapper()
 .readValue(json, Map.class);
 }

 @Override
 public void declareOutputFields(OutputFieldsDeclarer declarer) {
 declarer.declareStream("valid-stream",
 new Fields("machine_id", "sensor_type", "value", "timestamp", "status"));
 declarer.declareStream("error-stream",
 new Fields("machine_id", "sensor_type", "value", "timestamp", "error_type"));
 }
}
```

### 4.5 Anomaly Detection Bolt

```java
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class AnomalyDetectionBolt extends BaseRichBolt {

 private OutputCollector collector;

 // Threshold configuration
 private static final Map<String, double[]> THRESHOLDS = new HashMap<>();
 static {
 THRESHOLDS.put("vibration", new double[]{70.0, 85.0}); // warning, critical
 THRESHOLDS.put("temperature", new double[]{150.0, 180.0});
 THRESHOLDS.put("pressure", new double[]{800.0, 900.0});
 }

 // In-memory history for statistical analysis (per machine-sensor)
 private final Map<String, Deque<Double>> history = new ConcurrentHashMap<>();
 private static final int MAX_HISTORY = 100;
 private static final int MIN_HISTORY_FOR_STATS = 10;

 @Override
 public void prepare(Map stormConf, TopologyContext context,
 OutputCollector collector) {
 this.collector = collector;
 }

 @Override
 public void execute(Tuple tuple) {
 String machineId = tuple.getStringByField("machine_id");
 String sensorType = tuple.getStringByField("sensor_type");
 double value = tuple.getDoubleByField("value");
 long timestamp = tuple.getLongByField("timestamp");

 String key = machineId + ":" + sensorType;

 // Update history
 Deque<Double> sensorHistory = history.computeIfAbsent(key, k -> new ArrayDeque<>());
 synchronized (sensorHistory) {
 sensorHistory.addLast(value);
 if (sensorHistory.size() > MAX_HISTORY) {
 sensorHistory.removeFirst();
 }
 }

 // Detect anomalies
 AnomalyResult result = detectAnomaly(sensorType, value, sensorHistory);

 // Emit alert if anomaly detected
 if (result.severity != Severity.NORMAL) {
 collector.emit("alerts", tuple, new Values(
 machineId, sensorType, value, timestamp,
 result.severity.name(), result.zScore
 ));
 }

 // Emit to processing stream
 collector.emit(tuple, new Values(
 machineId, sensorType, value, timestamp,
 result.severity.name(), result.zScore
 ));

 collector.ack(tuple);
 }

 private AnomalyResult detectAnomaly(String sensorType, double value,
 Deque<Double> history) {
 double[] thresholds = THRESHOLDS.getOrDefault(sensorType,
 new double[]{Double.MAX_VALUE, Double.MAX_VALUE});

 Severity severity;
 if (value >= thresholds[1]) {
 severity = Severity.CRITICAL;
 } else if (value >= thresholds[0]) {
 severity = Severity.WARNING;
 } else {
 severity = Severity.NORMAL;
 }

 // Calculate Z-score for statistical anomaly detection
 double zScore = 0.0;
 synchronized (history) {
 if (history.size() >= MIN_HISTORY_FOR_STATS) {
 double mean = calculateMean(history);
 double std = calculateStd(history, mean);
 if (std > 0) {
 zScore = Math.abs((value - mean) / std);
 }
 }
 }

 // Elevate severity if statistical anomaly
 if (zScore > 3.0 && severity == Severity.NORMAL) {
 severity = Severity.STATISTICAL_ANOMALY;
 }

 return new AnomalyResult(severity, zScore);
 }

 private double calculateMean(Collection<Double> values) {
 return values.stream().mapToDouble(Double::doubleValue).average()
 .orElse(0.0);
 }

 private double calculateStd(Collection<Double> values, double mean) {
 double variance = values.stream()
 .mapToDouble(v -> Math.pow(v - mean, 2))
 .average()
 .orElse(0.0);
 return Math.sqrt(variance);
 }

 @Override
 public void declareOutputFields(OutputFieldsDeclarer declarer) {
 declarer.declareStream("alerts",
 new Fields("machine_id", "sensor_type", "value", "timestamp",
 "severity", "z_score"));
 declarer.declare(new Fields("machine_id", "sensor_type", "value",
 "timestamp", "severity", "z_score"));
 }

 // Inner classes
 private enum Severity { NORMAL, WARNING, CRITICAL, STATISTICAL_ANOMALY }

 private static class AnomalyResult {
 final Severity severity;
 final double zScore;

 AnomalyResult(Severity severity, double zScore) {
 this.severity = severity;
 this.zScore = zScore;
 }
 }
}
```

## 5. Comparative Analysis: Storm vs. Spark Streaming vs. Apache Flink

| Feature              | Apache Storm            | Spark Streaming          | Apache Flink             |
| -------------------- | ----------------------- | ------------------------ | ------------------------ |
| **Processing Model** | Native streaming        | Micro-batching           | Native streaming         |
| **Latency**          | Sub-second (∼100ms)     | 1-2 seconds              | Sub-second (∼10ms)       |
| **Exactly-Once**     | Trident/Transactional   | Checkpointing            | Checkpointing            |
| **State Management** | External ( Trident)     | RDD checkpoints          | Managed state backend    |
| **Windowing**        | Basic (Trident)         | DStream windows          | Rich (session, sliding)  |
| **API**              | Java/Python/Trident     | Scala/Java/Python        | Java/Scala/Python        |
| **Use Case**         | Low-latency ETL, alerts | Batch-oriented streaming | Complex event processing |

**Theorem 5.1 (Latency-Throughput Tradeoff):** For IoT applications requiring sub-second response to critical events (e.g., safety shutdown), Storm and Flink outperform Spark Streaming. The micro-batch model introduces inherent latency equal to batch interval plus processing time.

_Proof:_ Spark Streaming accumulates tuples for duration `Δ` before processing, guaranteeing latency ≥ `Δ`. Storm processes each tuple immediately upon arrival, achieving latency bounded by bolt processing time `τ` plus network latency `ν`. For safety-critical applications where `τ + ν << Δ`, native streaming provides necessary responsiveness. ∎

## 6. Assessment Questions

### 6.1 Multiple Choice Questions

**Question 1:** In Apache Storm, what is the relationship between executors and tasks?

A) Each executor runs exactly one task
B) Each task runs exactly one executor
C) Executors are processes, tasks are threads
D) Tasks are processes, executors are threads

**Answer: A**
_Explanation:_ In Storm's parallelism model, an executor is a thread that runs one or more tasks (instances of spouts or bolts). By default, `num_tasks = parallelism`, meaning one task per executor. However, `num_tasks` can exceed `parallelism` to run multiple tasks per executor, providing additional parallelism without additional threads.

---

**Question 2:** Which grouping strategy ensures that all tuples with the same field value are processed by the same task?

A) Shuffle grouping
B) Global grouping
C) Fields grouping
D) All grouping

**Answer: C**
_Explanation:_ Fields grouping uses a hash function on specified field values to partition tuples across bolt tasks. This guarantees that all tuples sharing the same field value (e.g., machine_id) are processed by the same task, essential for stateful operations requiring contextual awareness.

---

**Question 3:** What mechanism does Storm use to guarantee at-least-once processing semantics?

A) Checkpointing
B) Acker mechanism
C) Write-ahead logging
D) Transactional state

**Answer: B**
_Explanation:_ The acker (acker bolt) tracks the tuple tree for each spout tuple using XOR operations. Each downstream bolt anchors to incoming tuples by including their IDs in outgoing tuples. When all tuples in the tree are acknowledged, the root tuple's ID reaches zero (XOR of all IDs), confirming complete processing.

---

**Question 4:** For a field grouping on a heavily skewed key distribution, what is the expected impact on throughput?

A) Throughput increases proportionally with parallelism
B) Throughput remains constant regardless of distribution
C) Throughput decreases due to load imbalance
D) Throughput becomes unlimited

**Answer: C**
_Explanation:_ With skewed key distribution (high entropy deficiency), hash partitioning creates uneven load across tasks. The partition with the most frequent key becomes the bottleneck, limiting overall throughput despite high parallelism on other partitions. This is formalized in Theorem 2.5 where `H_k < 1` reduces effective throughput.

---

**Question 5:** In an industrial IoT scenario monitoring 10,000 machines, which bolt design pattern minimizes state management complexity?

A) Store all historical data in bolt memory
B) Use external Redis for windowed aggregation
C) Emit aggregates to downstream bolt for consolidation
D) Disable state tracking entirely

**Answer: C**
_Explanation:_ The partial-aggregate pattern reduces per-bolt state by having each bolt maintain partial aggregates for its partition, then consolidating in a downstream bolt. This balances state size with accuracy. Alternative approaches either exceed memory limits (A), add external dependency complexity (B), or lose processing guarantees (D).

---

### 6.2 Flashcard Deck

**Card 1:**
_Front:_ Define Apache Storm Topology
_Back:_ A directed acyclic graph (DAG) of computation nodes consisting of spouts (data sources) and bolts (processing nodes), connected by stream groupings. Topologies process infinite streams of tuples in parallel across a distributed cluster.

---

**Card 2:**
_Front:_ What is the purpose of the acker mechanism in Storm?
_Back:_ The acker tracks the tuple tree rooted at each spout tuple using XOR operations. It ensures at-least-once processing semantics by confirming when all derived tuples have been successfully processed. If acknowledgment is not received within the timeout, the root tuple is replayed.

---

**Card 3:**
_Front:_ Explain fields grouping
_Back:_ A stream grouping that partitions tuples across bolt tasks based on hash values of specified field(s). All tuples with identical field values are guaranteed to be processed by the same task, enabling stateful operations requiring ordered or contextual processing.

---

**Card 4:**
_Front:_ What is the difference between Storm workers, executors, and tasks?
_Back:_ Workers are JVM processes running on supervisor nodes. Executors are threads within workers that run spout/bolt instances. Tasks are the actual processing objects (instances of spouts/bolts). Relationship: `num_tasks ≥ parallelism`, with each executor running at least one task.

---

**Card 5:**
_Front:_ Why is native streaming preferred over micro-batching for safety-critical IoT applications?
_Back:_ Native streaming (Storm/Flink) processes tuples immediately upon arrival, achieving sub-second latency. Micro-batching (Spark Streaming) accumulates tuples before processing, introducing latency equal to batch interval. For safety-critical events requiring immediate response, native streaming provides necessary responsiveness.

---

### 6.3 Numerical Problem

**Problem:** A Storm topology processes IoT sensor data with the following configuration:

- 3 worker processes
- 8 spout executors with 8 tasks each
- 16 bolt executors with 16 tasks each
- Peak throughput: 50,000 tuples/second
- Single task processing capacity: 2,000 tuples/second

Calculate: (a) Total parallelism, (b) Required bolt parallelism to handle peak load, (c) Whether current configuration can handle 2× peak load.

**Solution:**

(a) Total parallelism = workers × executors_per_worker
Total spout parallelism = 3 × 8 = 24 (for spouts)
Total bolt parallelism = 3 × 16 = 48 (for bolts)

(b) Required bolt parallelism = ceil(peak_throughput / single_task_capacity)
= ceil(50,000 / 2,000) = 25 executors
Current: 48 executors → Sufficient headroom

(c) For 2× peak load = 100,000 tuples/second
Required bolt parallelism = ceil(100,000 / 2,000) = 50 executors
Current: 48 executors → INSUFFICIENT
Recommended: Set bolt parallelism to 56 (1.2× safety factor)

---

## 7. Summary

This chapter established the theoretical and practical foundations of real-time IoT data analysis using Apache Storm. Key learnings include:

1. **Storm Architecture**: Master-worker model with Nimbus, ZooKeeper, Supervisor, and Worker components, where the acker mechanism provides reliability guarantees.

2. **Theoretical Foundations**: At-least-once semantics via tuple tree tracking, parallelism hierarchy (workers→executors→tasks), and throughput bounds based on grouping strategy and key distribution.

3. **IoT Design Patterns**: Partitioning by device_id, parallelism tuning based on throughput calculations, fault tolerance configuration, and state management strategies.

4. **Implementation**: Complete Java topology with Kafka spout, validation bolt, anomaly detection bolt, demonstrating field grouping, multi-stream output, and fault-tolerant tuple processing.

5. **Comparative Analysis**: Native streaming (Storm/Flink) preferred over micro-batching for latency-critical IoT applications requiring sub-second response to critical events.
