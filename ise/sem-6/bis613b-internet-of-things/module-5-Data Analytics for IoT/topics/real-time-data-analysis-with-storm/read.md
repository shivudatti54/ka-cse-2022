# Real-time Data Analysis with Storm


## Table of Contents

- [Real-time Data Analysis with Storm](#real-time-data-analysis-with-storm)
- [Overview](#overview)
- [Building Storm Topologies for IoT](#building-storm-topologies-for-iot)
  - [IoT Streaming Architecture](#iot-streaming-architecture)
  - [Design Principles](#design-principles)
- [Real-Time Sensor Data Processing](#real-time-sensor-data-processing)
  - [Use Case: Industrial Equipment Monitoring](#use-case-industrial-equipment-monitoring)
  - [Topology Design](#topology-design)
- [Spout: Read from Kafka](#spout-read-from-kafka)
- [Re-emit failed tuple](#re-emit-failed-tuple)
- [Bolt 1: Parse and Validate](#bolt-1-parse-and-validate)
- [Validate range](#validate-range)
- [Log invalid reading](#log-invalid-reading)
- [Bolt 2: Anomaly Detection](#bolt-2-anomaly-detection)
- [Load pre-trained anomaly detection model](#load-pre-trained-anomaly-detection-model)
- [Maintain history for statistical analysis](#maintain-history-for-statistical-analysis)
- [Threshold-based detection](#threshold-based-detection)
- [Calculate deviation from mean](#calculate-deviation-from-mean)
- [Emit with severity](#emit-with-severity)
- [Bolt 3: Windowed Aggregation](#bolt-3-windowed-aggregation)
- [Add to window](#add-to-window)
- [Remove old data outside window](#remove-old-data-outside-window)
- [Emit aggregation every slide_interval](#emit-aggregation-every-slideinterval)
- [Bolt 4: Alert Generation](#bolt-4-alert-generation)
- [Check if alert needed](#check-if-alert-needed)
- [Cooldown to prevent alert spam](#cooldown-to-prevent-alert-spam)
- [Emit to alert stream](#emit-to-alert-stream)
- [Log alert](#log-alert)
- [Bolt 5: Database Storage](#bolt-5-database-storage)
- [Initialize InfluxDB or Cassandra connection](#initialize-influxdb-or-cassandra-connection)
- [Prepare data point](#prepare-data-point)
- [Batch write for performance](#batch-write-for-performance)
  - [Topology Configuration](#topology-configuration)
- [Spout with 2 parallel instances](#spout-with-2-parallel-instances)
- [Validation bolt with shuffle grouping](#validation-bolt-with-shuffle-grouping)
- [Anomaly detection with shuffle grouping](#anomaly-detection-with-shuffle-grouping)
- [Aggregation with fields grouping (per machine-sensor combination)](#aggregation-with-fields-grouping-per-machine-sensor-combination)
- [Alert generation](#alert-generation)
- [Storage with shuffle grouping](#storage-with-shuffle-grouping)
- [Topology configuration](#topology-configuration)
- [Submit topology](#submit-topology)
- [Windowed Computations](#windowed-computations)
  - [Types of Windows](#types-of-windows)
  - [Window Implementation](#window-implementation)
- [Add to window](#add-to-window)
- [Remove expired data](#remove-expired-data)
- [Compute and emit aggregation](#compute-and-emit-aggregation)
- [Integration with Kafka](#integration-with-kafka)
  - [Kafka Spout Configuration](#kafka-spout-configuration)
  - [Producer-Consumer Pattern](#producer-consumer-pattern)
- [IoT Use Cases](#iot-use-cases)
  - [1. Smart City Traffic Management](#1-smart-city-traffic-management)
- [Topology: Traffic Monitoring](#topology-traffic-monitoring)
  - [2. Predictive Maintenance](#2-predictive-maintenance)
- [Topology: Predictive Maintenance](#topology-predictive-maintenance)
  - [3. Energy Grid Optimization](#3-energy-grid-optimization)
- [Topology: Smart Grid Management](#topology-smart-grid-management)
  - [4. Healthcare Patient Monitoring](#4-healthcare-patient-monitoring)
- [Topology: Patient Monitoring](#topology-patient-monitoring)
  - [5. Fraud Detection](#5-fraud-detection)
- [Topology: Fraud Detection](#topology-fraud-detection)
- [Performance Optimization](#performance-optimization)
  - [1. Parallelism Tuning](#1-parallelism-tuning)
- [Analyze bottlenecks](#analyze-bottlenecks)
- [Increase parallelism for bottleneck bolts](#increase-parallelism-for-bottleneck-bolts)
- [Balance across stages](#balance-across-stages)
  - [2. Batching](#2-batching)
- [Process batch](#process-batch)
- [Emit batch results](#emit-batch-results)
  - [3. Caching](#3-caching)
  - [4. Monitoring](#4-monitoring)
- [Monitor topology metrics](#monitor-topology-metrics)
- [Key metrics to watch:](#key-metrics-to-watch)
- [Summary](#summary)
- [Key Takeaways for Exams](#key-takeaways-for-exams)

## Overview

Real-time data analysis with Apache Storm enables organizations to process and analyze streaming IoT data as it arrives, providing instant insights and immediate responses to critical events. This capability is essential for modern IoT applications where delayed analysis can result in missed opportunities, safety hazards, or operational inefficiencies. Storm's ability to process millions of events per second with sub-second latency makes it ideal for use cases like anomaly detection in industrial equipment, real-time traffic management in smart cities, instant fraud detection in financial systems, and live monitoring of critical infrastructure.

## Building Storm Topologies for IoT

### IoT Streaming Architecture

```
IoT Devices/Sensors
        │
        ▼
   Data Ingestion Layer (Kafka/MQTT)
        │
        ▼
   Storm Topology
   ┌─────────────────────────────────┐
   │  Spout → Parse → Filter →       │
   │  Aggregate → Alert → Store      │
   └─────────────────────────────────┘
        │
        ├──► Alerts/Notifications
        ├──► Real-time Dashboards
        └──► Long-term Storage
```

### Design Principles

**1. Partitioning Strategy:**

- Distribute load evenly
- Use fields grouping for stateful operations
- Consider data skew

**2. Parallelism Tuning:**

- Balance spout and bolt parallelism
- Monitor throughput and latency
- Scale based on load

**3. Fault Tolerance:**

- Design for tuple replay
- Use reliable spouts
- Set appropriate timeouts

**4. State Management:**

- Minimize state in bolts
- Use external stores for large state
- Consider windowed state

**5. Performance Optimization:**

- Batch emissions where possible
- Use efficient serialization
- Monitor and tune buffer sizes

## Real-Time Sensor Data Processing

### Use Case: Industrial Equipment Monitoring

**Scenario:** Monitor 10,000 industrial machines with multiple sensors (vibration, temperature, pressure) sending data every second. Detect anomalies, predict failures, and generate instant alerts.

### Topology Design

```python
from storm import Topology, Spout, Bolt
import json
from collections import defaultdict
import time

# Spout: Read from Kafka
class IndustrialSensorSpout(Spout):
    """
    Reads sensor data from Kafka topics
    Format: {machine_id, sensor_type, value, timestamp}
    """
    def initialize(self, conf, context):
        from kafka import KafkaConsumer
        self.consumer = KafkaConsumer(
            'industrial-sensors',
            bootstrap_servers=['kafka:9092'],
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.pending = {}

    def nextTuple(self):
        for message in self.consumer:
            msg_id = f"{message.partition}:{message.offset}"
            self.pending[msg_id] = message.value
            self.emit([message.value], message_id=msg_id)
            break  # Process one message at a time

    def ack(self, msg_id):
        if msg_id in self.pending:
            del self.pending[msg_id]

    def fail(self, msg_id):
        if msg_id in self.pending:
            # Re-emit failed tuple
            data = self.pending[msg_id]
            self.emit([data], message_id=msg_id)

# Bolt 1: Parse and Validate
class ValidationBolt(Bolt):
    """
    Validates sensor readings and filters invalid data
    """
    def initialize(self, conf, context):
        self.valid_ranges = {
            'vibration': (0, 100),
            'temperature': (-20, 200),
            'pressure': (0, 1000)
        }

    def process(self, tup):
        try:
            data = tup.values[0]
            machine_id = data['machine_id']
            sensor_type = data['sensor_type']
            value = float(data['value'])
            timestamp = data['timestamp']

            # Validate range
            if sensor_type in self.valid_ranges:
                min_val, max_val = self.valid_ranges[sensor_type]
                if min_val <= value <= max_val:
                    self.emit([machine_id, sensor_type, value, timestamp],
                             anchors=[tup])
                else:
                    # Log invalid reading
                    self.emit([machine_id, sensor_type, value, timestamp, 'INVALID'],
                             anchors=[tup], stream='errors')

            self.ack(tup)

        except Exception as e:
            self.log(f"Validation error: {e}")
            self.fail(tup)

# Bolt 2: Anomaly Detection
class AnomalyDetectionBolt(Bolt):
    """
    Detects anomalies using statistical thresholds and ML models
    """
    def initialize(self, conf, context):
        # Load pre-trained anomaly detection model
        self.thresholds = {
            'vibration': {'warning': 70, 'critical': 85},
            'temperature': {'warning': 150, 'critical': 180},
            'pressure': {'warning': 800, 'critical': 900}
        }
        self.history = defaultdict(list)
        self.max_history = 100

    def process(self, tup):
        machine_id, sensor_type, value, timestamp = tup.values

        # Maintain history for statistical analysis
        key = f"{machine_id}:{sensor_type}"
        self.history[key].append(value)
        if len(self.history[key]) > self.max_history:
            self.history[key].pop(0)

        # Threshold-based detection
        if sensor_type in self.thresholds:
            thresholds = self.thresholds[sensor_type]

            severity = 'normal'
            if value >= thresholds['critical']:
                severity = 'critical'
            elif value >= thresholds['warning']:
                severity = 'warning'

            # Calculate deviation from mean
            if len(self.history[key]) >= 10:
                mean = sum(self.history[key]) / len(self.history[key])
                std = (sum((x - mean) ** 2 for x in self.history[key]) / len(self.history[key])) ** 0.5
                z_score = abs((value - mean) / std) if std > 0 else 0

                if z_score > 3:  # 3 sigma rule
                    severity = 'critical' if severity != 'critical' else severity

            # Emit with severity
            self.emit([machine_id, sensor_type, value, timestamp, severity],
                     anchors=[tup])

        self.ack(tup)

# Bolt 3: Windowed Aggregation
class WindowedAggregationBolt(Bolt):
    """
    Aggregates sensor data over sliding windows
    """
    def initialize(self, conf, context):
        self.window_size = 60  # 60 seconds
        self.slide_interval = 10  # 10 seconds
        self.windows = defaultdict(list)
        self.last_emit = defaultdict(float)

    def process(self, tup):
        machine_id, sensor_type, value, timestamp, severity = tup.values

        current_time = time.time()
        key = f"{machine_id}:{sensor_type}"

        # Add to window
        self.windows[key].append({
            'value': value,
            'timestamp': current_time,
            'severity': severity
        })

        # Remove old data outside window
        cutoff = current_time - self.window_size
        self.windows[key] = [
            item for item in self.windows[key]
            if item['timestamp'] > cutoff
        ]

        # Emit aggregation every slide_interval
        if current_time - self.last_emit[key] >= self.slide_interval:
            window_data = self.windows[key]

            if window_data:
                values = [item['value'] for item in window_data]
                severities = [item['severity'] for item in window_data]

                aggregation = {
                    'machine_id': machine_id,
                    'sensor_type': sensor_type,
                    'count': len(values),
                    'avg': sum(values) / len(values),
                    'min': min(values),
                    'max': max(values),
                    'critical_count': severities.count('critical'),
                    'warning_count': severities.count('warning'),
                    'timestamp': current_time
                }

                self.emit([aggregation], anchors=[tup])
                self.last_emit[key] = current_time

        self.ack(tup)

# Bolt 4: Alert Generation
class AlertBolt(Bolt):
    """
    Generates and sends alerts based on severity
    """
    def initialize(self, conf, context):
        self.alert_cooldown = {}
        self.cooldown_period = 300  # 5 minutes

    def process(self, tup):
        aggregation = tup.values[0]
        machine_id = aggregation['machine_id']
        sensor_type = aggregation['sensor_type']

        # Check if alert needed
        if aggregation['critical_count'] > 0:
            key = f"{machine_id}:{sensor_type}"
            current_time = time.time()

            # Cooldown to prevent alert spam
            if key not in self.alert_cooldown or \
               current_time - self.alert_cooldown[key] > self.cooldown_period:

                alert = {
                    'type': 'CRITICAL_ANOMALY',
                    'machine_id': machine_id,
                    'sensor_type': sensor_type,
                    'message': f"Critical anomaly detected: {aggregation['critical_count']} critical readings in last window",
                    'details': aggregation,
                    'timestamp': current_time,
                    'priority': 'HIGH'
                }

                # Emit to alert stream
                self.emit([alert], anchors=[tup], stream='alerts')
                self.alert_cooldown[key] = current_time

                # Log alert
                self.log(f"ALERT: {alert['message']}")

        self.ack(tup)

# Bolt 5: Database Storage
class StorageBolt(Bolt):
    """
    Stores aggregated data to time-series database
    """
    def initialize(self, conf, context):
        # Initialize InfluxDB or Cassandra connection
        from influxdb import InfluxDBClient
        self.client = InfluxDBClient(host='influxdb', port=8086)
        self.client.switch_database('iot_sensors')
        self.batch = []
        self.batch_size = 100

    def process(self, tup):
        aggregation = tup.values[0]

        # Prepare data point
        point = {
            'measurement': 'sensor_aggregations',
            'tags': {
                'machine_id': aggregation['machine_id'],
                'sensor_type': aggregation['sensor_type']
            },
            'time': int(aggregation['timestamp'] * 1000000000),
            'fields': {
                'count': aggregation['count'],
                'avg': aggregation['avg'],
                'min': aggregation['min'],
                'max': aggregation['max'],
                'critical_count': aggregation['critical_count'],
                'warning_count': aggregation['warning_count']
            }
        }

        self.batch.append(point)

        # Batch write for performance
        if len(self.batch) >= self.batch_size:
            try:
                self.client.write_points(self.batch)
                self.batch = []
            except Exception as e:
                self.log(f"Storage error: {e}")
                self.fail(tup)
                return

        self.ack(tup)
```

### Topology Configuration

```python
from storm import TopologyBuilder

builder = TopologyBuilder()

# Spout with 2 parallel instances
builder.setSpout("sensor-spout", IndustrialSensorSpout(), 2)

# Validation bolt with shuffle grouping
builder.setBolt("validation", ValidationBolt(), 4) \
       .shuffleGrouping("sensor-spout")

# Anomaly detection with shuffle grouping
builder.setBolt("anomaly-detection", AnomalyDetectionBolt(), 8) \
       .shuffleGrouping("validation")

# Aggregation with fields grouping (per machine-sensor combination)
builder.setBolt("aggregation", WindowedAggregationBolt(), 8) \
       .fieldsGrouping("anomaly-detection", ["machine_id", "sensor_type"])

# Alert generation
builder.setBolt("alerts", AlertBolt(), 2) \
       .shuffleGrouping("aggregation")

# Storage with shuffle grouping
builder.setBolt("storage", StorageBolt(), 4) \
       .shuffleGrouping("aggregation")

# Topology configuration
config = {
    'topology.workers': 4,
    'topology.max.spout.pending': 1000,
    'topology.message.timeout.secs': 30,
    'topology.debug': False
}

# Submit topology
from storm import StormSubmitter
StormSubmitter.submitTopology("industrial-monitoring", config, builder.createTopology())
```

## Windowed Computations

### Types of Windows

**1. Tumbling Window:**

- Fixed-size, non-overlapping
- Each event belongs to exactly one window

```
Window 1: [0-10s]
Window 2: [10-20s]
Window 3: [20-30s]
```

**2. Sliding Window:**

- Fixed size, overlapping
- Windows slide at regular intervals

```
Window 1: [0-60s]
Window 2: [10-70s]  (slides 10s)
Window 3: [20-80s]
```

**3. Session Window:**

- Dynamic size based on activity
- Closes after inactivity timeout

### Window Implementation

```python
class SlidingWindowBolt(Bolt):
    def initialize(self, conf, context):
        self.window_duration = 60  # 60 seconds
        self.slide_interval = 10   # 10 seconds
        self.windows = defaultdict(list)

    def process(self, tup):
        sensor_id, value, timestamp = tup.values
        current_time = time.time()

        # Add to window
        self.windows[sensor_id].append((value, current_time))

        # Remove expired data
        cutoff = current_time - self.window_duration
        self.windows[sensor_id] = [
            (v, t) for v, t in self.windows[sensor_id]
            if t > cutoff
        ]

        # Compute and emit aggregation
        if len(self.windows[sensor_id]) > 0:
            values = [v for v, t in self.windows[sensor_id]]
            avg = sum(values) / len(values)
            self.emit([sensor_id, avg, len(values), current_time])

        self.ack(tup)
```

## Integration with Kafka

Kafka provides reliable, scalable message buffering for Storm topologies.

### Kafka Spout Configuration

```python
from storm_kafka import KafkaSpout, SpoutConfig, ZkHosts

zkHosts = ZkHosts("localhost:2181")

spoutConfig = SpoutConfig(
    brokerHosts=zkHosts,
    topic="iot-sensors",
    zkRoot="/storm",
    id="storm-kafka-spout"
)

spoutConfig.scheme = SchemeAsMultiScheme(RawMultiScheme())
spoutConfig.forceFromStart = False  # Resume from last offset

kafkaSpout = KafkaSpout(spoutConfig)
```

### Producer-Consumer Pattern

```
IoT Devices → Kafka Producer → Kafka Broker → Storm Spout → Processing
                                     ↓
                              Reliable Buffer
                              (Retention: 7 days)
```

**Benefits:**

- Decoupling producers and consumers
- Message persistence and replay
- Handling data spikes
- Failure recovery

## IoT Use Cases

### 1. Smart City Traffic Management

**Real-time traffic monitoring and optimization**

```python
# Topology: Traffic Monitoring
Spout: Read traffic sensor data (vehicle counts, speeds)
  ↓
Bolt 1: Parse and validate sensor readings
  ↓
Bolt 2: Detect congestion (compare against thresholds)
  ↓
Bolt 3: Aggregate by road segment (fields grouping)
  ↓
Bolt 4: Generate traffic alerts and recommendations
  ↓
Bolt 5: Update traffic light control system
  ↓
Bolt 6: Store to dashboard database
```

**Metrics:**

- Process 100,000+ vehicles/minute
- <100ms detection latency
- Real-time dashboard updates

### 2. Predictive Maintenance

**Continuous equipment monitoring for failure prediction**

```python
# Topology: Predictive Maintenance
Spout: Stream machine sensor data
  ↓
Bolt 1: Feature extraction (vibration FFT, temp trends)
  ↓
Bolt 2: ML model scoring (predict remaining useful life)
  ↓
Bolt 3: Anomaly detection (statistical + ML)
  ↓
Bolt 4: Risk assessment (combine predictions)
  ↓
Bolt 5: Generate maintenance recommendations
  ↓
Bolt 6: Alert maintenance team
  ↓
Bolt 7: Update asset management system
```

**Business Impact:**

- Reduce downtime by 40%
- Prevent catastrophic failures
- Optimize maintenance scheduling

### 3. Energy Grid Optimization

**Real-time monitoring and balancing of smart grids**

```python
# Topology: Smart Grid Management
Spout: Smart meter readings (energy consumption)
  ↓
Bolt 1: Validate and normalize readings
  ↓
Bolt 2: Detect anomalies (theft, faults)
  ↓
Bolt 3: Aggregate by region (hierarchical)
  ↓
Bolt 4: Predict short-term demand (next 15 min)
  ↓
Bolt 5: Optimize generation and distribution
  ↓
Bolt 6: Send control signals to substations
  ↓
Bolt 7: Update monitoring dashboard
```

**Capabilities:**

- Process millions of meters
- Sub-second anomaly detection
- Dynamic load balancing

### 4. Healthcare Patient Monitoring

**Continuous vital sign monitoring in hospitals**

```python
# Topology: Patient Monitoring
Spout: Stream vital signs (heart rate, BP, SpO2)
  ↓
Bolt 1: Validate sensor data quality
  ↓
Bolt 2: Detect critical conditions (per patient)
  ↓
Bolt 3: Risk scoring (ML-based)
  ↓
Bolt 4: Priority classification
  ↓
Bolt 5: Alert medical staff (critical cases)
  ↓
Bolt 6: Update patient dashboard
  ↓
Bolt 7: Store to medical records
```

**Requirements:**

- Ultra-low latency (<1 second)
- 100% reliability
- HIPAA compliance

### 5. Fraud Detection

**Real-time fraud detection in IoT payments**

```python
# Topology: Fraud Detection
Spout: Transaction events
  ↓
Bolt 1: Feature engineering (location, amount, time)
  ↓
Bolt 2: User behavior profiling (fields grouping by user)
  ↓
Bolt 3: ML model scoring (fraud probability)
  ↓
Bolt 4: Rule-based checks (velocity, geography)
  ↓
Bolt 5: Risk assessment (combine scores)
  ↓
Bolt 6: Block suspicious transactions
  ↓
Bolt 7: Alert fraud team
  ↓
Bolt 8: Update fraud database
```

**Performance:**

- <50ms decision time
- 99.9% fraud detection rate
- Minimal false positives

## Performance Optimization

### 1. Parallelism Tuning

```python
# Analyze bottlenecks
storm ui → Topology Visualization → Component Latency

# Increase parallelism for bottleneck bolts
builder.setBolt("slow-bolt", SlowBolt(), 16)  # Was 8

# Balance across stages
spout: 4, bolt1: 8, bolt2: 16, bolt3: 8, bolt4: 4
```

### 2. Batching

```python
class BatchedBolt(Bolt):
    def initialize(self, conf, context):
        self.batch = []
        self.batch_size = 100

    def process(self, tup):
        self.batch.append(tup.values)

        if len(self.batch) >= self.batch_size:
            # Process batch
            results = self.process_batch(self.batch)

            # Emit batch results
            for result in results:
                self.emit(result)

            self.batch = []

        self.ack(tup)
```

### 3. Caching

```python
class CachedLookupBolt(Bolt):
    def initialize(self, conf, context):
        from functools import lru_cache

        @lru_cache(maxsize=10000)
        def cached_lookup(key):
            return database.lookup(key)

        self.lookup = cached_lookup
```

### 4. Monitoring

```bash
# Monitor topology metrics
storm metrics <topology-name>

# Key metrics to watch:
- Complete latency (end-to-end)
- Process latency (per bolt)
- Capacity (should be < 1.0)
- Failed tuples
- Acked tuples
```

## Summary

Real-time data analysis with Apache Storm enables processing of IoT streaming data with sub-second latency. Building topologies involves designing spouts for data ingestion, bolts for processing, and appropriate stream groupings for data flow control.

Windowed computations (tumbling, sliding, session) enable time-based aggregations. Integration with Kafka provides reliable message buffering and decoupling. Common IoT use cases include traffic management, predictive maintenance, energy optimization, healthcare monitoring, and fraud detection.

Performance optimization through parallelism tuning, batching, caching, and monitoring ensures Storm topologies can handle millions of events per second while maintaining low latency and high reliability.

## Key Takeaways for Exams

1. **IoT Topology Design:** Spout (ingestion) → Parse → Validate → Detect → Aggregate → Alert → Store

2. **Windowed Computations:** Tumbling (non-overlapping), Sliding (overlapping), Session (activity-based)

3. **Kafka Integration:** Kafka provides reliable buffering, message persistence, replay capability, spike handling

4. **Fields Grouping:** Essential for per-entity stateful aggregation (per sensor, per machine, per user)

5. **Alert Generation:** Threshold-based + statistical (z-score) + ML models with cooldown to prevent spam

6. **Use Cases:** Traffic management, predictive maintenance, energy optimization, patient monitoring, fraud detection

7. **Performance:** Parallelism tuning, batching emissions, caching lookups, monitoring metrics

8. **Reliability:** Tuple tracking, ack/fail mechanism, timeout configuration, guaranteed processing

9. **Real-time Characteristics:** Sub-second latency, continuous processing, instant alerts, live dashboards

10. **Storm Advantage:** True streaming (no batching), ultra-low latency, millions of tuples/second, fault-tolerant
