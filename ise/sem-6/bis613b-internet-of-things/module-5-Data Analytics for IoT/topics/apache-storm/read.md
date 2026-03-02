# Apache Storm


## Table of Contents

- [Apache Storm](#apache-storm)
- [Overview](#overview)
- [What is Apache Storm?](#what-is-apache-storm)
  - [Key Characteristics](#key-characteristics)
- [Storm Architecture](#storm-architecture)
  - [Cluster Architecture](#cluster-architecture)
  - [Storm Components](#storm-components)
- [Storm Topology](#storm-topology)
  - [Topology Structure](#topology-structure)
  - [Spouts](#spouts)
- [Read from Kafka](#read-from-kafka)
- [Emit tuple with message ID for tracking](#emit-tuple-with-message-id-for-tracking)
- [Message successfully processed](#message-successfully-processed)
- [Message failed, replay](#message-failed-replay)
  - [Bolts](#bolts)
- [Filter anomalies](#filter-anomalies)
- [Emit to alert stream](#emit-to-alert-stream)
- [Emit to normal stream](#emit-to-normal-stream)
  - [Stream Groupings](#stream-groupings)
- [Tuple Processing Model](#tuple-processing-model)
  - [Tuple Structure](#tuple-structure)
- [Tuple example](#tuple-example)
  - [Tuple Tree](#tuple-tree)
  - [Guaranteed Processing](#guaranteed-processing)
- [Process tuple](#process-tuple)
- [Emit new tuple anchored to input](#emit-new-tuple-anchored-to-input)
- [Acknowledge successful processing](#acknowledge-successful-processing)
- [Processing failed, trigger replay](#processing-failed-trigger-replay)
- [IoT Topology Example: Temperature Monitoring](#iot-topology-example-temperature-monitoring)
  - [Complete Topology](#complete-topology)
- [Spout: Read sensor data from Kafka](#spout-read-sensor-data-from-kafka)
- [Bolt 1: Parse JSON data](#bolt-1-parse-json-data)
- [Bolt 2: Filter anomalies](#bolt-2-filter-anomalies)
- [Bolt 3: Aggregate by sensor (uses fields grouping)](#bolt-3-aggregate-by-sensor-uses-fields-grouping)
- [Bolt 4: Generate alerts](#bolt-4-generate-alerts)
- [Bolt 5: Store to database](#bolt-5-store-to-database)
  - [Implementation Details](#implementation-details)
- [Emit to alert stream](#emit-to-alert-stream)
- [Emit to warning stream](#emit-to-warning-stream)
- [Normal reading](#normal-reading)
- [Aggregate statistics per sensor](#aggregate-statistics-per-sensor)
- [Emit every 100 readings](#emit-every-100-readings)
- [Storm Configuration](#storm-configuration)
  - [Topology Configuration](#topology-configuration)
- [Parallelism](#parallelism)
- [Reliability](#reliability)
- [Performance](#performance)
- [Debugging](#debugging)
  - [Parallelism Settings](#parallelism-settings)
- [Topology-level workers](#topology-level-workers)
- [Component-level parallelism](#component-level-parallelism)
- [Advantages of Storm](#advantages-of-storm)
- [Limitations of Storm](#limitations-of-storm)
- [Storm vs Spark Streaming](#storm-vs-spark-streaming)
- [Summary](#summary)
- [Key Takeaways for Exams](#key-takeaways-for-exams)

## Overview

Apache Storm is a distributed real-time computation system designed for processing unbounded streams of data. Developed at BackType and open-sourced by Twitter in 2011, Storm enables reliable processing of continuous data streams with guaranteed message processing, fault tolerance, and horizontal scalability. For IoT applications generating millions of events per second from sensors and devices, Storm provides the infrastructure needed for real-time analytics, instant anomaly detection, and immediate response to critical events—capabilities essential when millisecond-level latency is required.

## What is Apache Storm?

Apache Storm is a free, open-source distributed real-time computation system that makes it easy to reliably process unbounded streams of data. Storm does for real-time processing what Hadoop did for batch processing.

### Key Characteristics

**1. Real-Time Processing:**

- Processes data as it arrives
- Sub-second latency
- Continuous computation
- No batch windows

**2. Guaranteed Message Processing:**

- At-least-once semantics
- Tracks tuple lineage
- Automatic retries on failure
- Configurable timeout

**3. Fault Tolerance:**

- Automatic worker restart
- Reassignment of failed tasks
- No data loss
- Self-healing cluster

**4. Scalability:**

- Horizontal scaling
- Linear performance growth
- Handles millions of tuples/second
- Distributed architecture

**5. Programming Simplicity:**

- Simple abstraction (Spouts, Bolts)
- Multiple language support (Java, Python, etc.)
- Easy topology definition
- Rich API

## Storm Architecture

### Cluster Architecture

```
┌──────────────────────────────────────────────────────┐
│                 Storm Cluster                        │
├──────────────────────────────────────────────────────┤
│                     Nimbus                           │
│                 (Master Node)                        │
│         - Job Submission                             │
│         - Task Assignment                            │
│         - Monitoring                                 │
└────────────────┬─────────────────────────────────────┘
                 │
         ┌───────┴────────┐
         │   ZooKeeper    │ (Coordination)
         │   Cluster      │
         └───────┬────────┘
                 │
     ┌───────────┼───────────┬───────────┐
     │           │           │           │
     ▼           ▼           ▼           ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ Super-  │ │ Super-  │ │ Super-  │ │ Super-  │
│ visor 1 │ │ visor 2 │ │ visor 3 │ │ visor 4 │
│         │ │         │ │         │ │         │
│ Worker  │ │ Worker  │ │ Worker  │ │ Worker  │
│ Worker  │ │ Worker  │ │ Worker  │ │ Worker  │
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

### Storm Components

**1. Nimbus (Master Node):**

- Distributes code across cluster
- Assigns tasks to supervisors
- Monitors topology health
- Handles failures
- Similar to Hadoop JobTracker

**2. Supervisor (Worker Node):**

- Runs on each machine
- Manages worker processes
- Executes assigned tasks
- Reports heartbeat to Nimbus
- Restarts failed workers

**3. ZooKeeper:**

- Coordinates between Nimbus and Supervisors
- Stores cluster state
- Manages configuration
- Provides distributed synchronization
- Enables fault tolerance

**4. Worker Process:**

- JVM process on supervisor
- Executes subset of topology
- Contains multiple executors
- Runs spouts and bolts

**5. Executor:**

- Thread within worker process
- Runs tasks of single component
- Can have multiple tasks
- Basic unit of parallelism

**6. Task:**

- Actual instance of spout or bolt
- Processes tuples
- Multiple tasks per executor

## Storm Topology

A topology is a directed acyclic graph (DAG) of spouts and bolts representing the data flow and processing logic.

### Topology Structure

```
Input Stream
     │
     ▼
┌─────────┐
│ Spout   │ (Data Source)
└────┬────┘
     │
     ├──────────┬──────────┐
     ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│ Bolt 1 │ │ Bolt 2 │ │ Bolt 3 │ (Processing)
└────┬───┘ └────┬───┘ └────┬───┘
     │          │          │
     └──────────┴────┬─────┘
                     ▼
                ┌─────────┐
                │ Bolt 4  │ (Aggregation)
                └────┬────┘
                     │
                     ▼
                Output Stream
```

### Spouts

Spouts are sources of streams—they read data from external sources and emit tuples into the topology.

**Characteristics:**

- Entry point of data
- Reliable or unreliable
- Can replay failed tuples
- Multiple spouts in topology

**Example Spout (Python):**

```python
from storm import Spout

class SensorSpout(Spout):
    def initialize(self, conf, context):
        self.kafka_consumer = KafkaConsumer('iot-sensors')

    def nextTuple(self):
        # Read from Kafka
        message = self.kafka_consumer.poll()
        if message:
            # Emit tuple with message ID for tracking
            self.emit([message.value], message_id=message.offset)

    def ack(self, tup_id):
        # Message successfully processed
        pass

    def fail(self, tup_id):
        # Message failed, replay
        self.kafka_consumer.seek(tup_id)
```

### Bolts

Bolts process input streams and produce new streams—they contain the processing logic.

**Characteristics:**

- Receive tuples from spouts/bolts
- Process and transform data
- Emit zero or more tuples
- Can have multiple outputs

**Example Bolt (Python):**

```python
from storm import Bolt

class TemperatureFilterBolt(Bolt):
    def process(self, tup):
        sensor_id = tup.values[0]
        temperature = tup.values[1]

        # Filter anomalies
        if temperature > 50 or temperature < 0:
            # Emit to alert stream
            self.emit([sensor_id, temperature, "ANOMALY"])
        else:
            # Emit to normal stream
            self.emit([sensor_id, temperature, "NORMAL"])
```

### Stream Groupings

Stream groupings define how tuples are distributed between tasks.

**1. Shuffle Grouping:**

- Random distribution
- Load balancing
- Use when no specific routing needed

```python
builder.setBolt("process", ProcessBolt(), 4) \
       .shuffleGrouping("sensor-spout")
```

**2. Fields Grouping:**

- Group by field values
- Same field always to same task
- Use for aggregations

```python
builder.setBolt("aggregate", AggregateBolt(), 4) \
       .fieldsGrouping("filter", ["sensor_id"])
```

**3. All Grouping:**

- Send to all tasks
- Broadcast pattern
- Use for reference data

```python
builder.setBolt("enrich", EnrichBolt(), 4) \
       .allGrouping("config-spout")
```

**4. Global Grouping:**

- Send to single task (lowest ID)
- Use for global aggregation

```python
builder.setBolt("global-counter", CountBolt(), 1) \
       .globalGrouping("events")
```

**5. Direct Grouping:**

- Producer chooses destination
- Custom routing logic

**6. None Grouping:**

- Equivalent to shuffle
- No specific requirement

## Tuple Processing Model

### Tuple Structure

A tuple is the basic unit of data in Storm:

```python
# Tuple example
tuple = {
    'values': ['sensor123', 25.5, '2024-01-15T10:00:00'],
    'stream': 'default',
    'source_component': 'sensor-spout',
    'source_task': 1
}
```

### Tuple Tree

Storm tracks tuple lineage to guarantee processing:

```
Root Tuple (from Spout)
    │
    ├─► Bolt 1 emits Tuple A
    │        └─► Bolt 3 emits Tuple A1
    │        └─► Bolt 3 emits Tuple A2
    │
    └─► Bolt 2 emits Tuple B
             └─► Bolt 4 emits Tuple B1
```

### Guaranteed Processing

**Ack/Fail Mechanism:**

```python
class ProcessBolt(Bolt):
    def process(self, tup):
        try:
            # Process tuple
            result = process_data(tup.values)

            # Emit new tuple anchored to input
            self.emit([result], anchors=[tup])

            # Acknowledge successful processing
            self.ack(tup)

        except Exception as e:
            # Processing failed, trigger replay
            self.fail(tup)
```

**Timeout:**

- Default 30 seconds per tuple tree
- Configurable via topology config
- Timeout triggers fail and replay

## IoT Topology Example: Temperature Monitoring

### Complete Topology

```python
from storm import Topology

class TemperatureMonitoringTopology(Topology):
    # Spout: Read sensor data from Kafka
    sensor_spout = {
        'class': 'SensorSpout',
        'parallelism': 2
    }

    # Bolt 1: Parse JSON data
    parse_bolt = {
        'class': 'ParseBolt',
        'parallelism': 4,
        'grouping': {'sensor_spout': 'shuffle'}
    }

    # Bolt 2: Filter anomalies
    filter_bolt = {
        'class': 'AnomalyFilterBolt',
        'parallelism': 4,
        'grouping': {'parse_bolt': 'shuffle'}
    }

    # Bolt 3: Aggregate by sensor (uses fields grouping)
    aggregate_bolt = {
        'class': 'AggregationBolt',
        'parallelism': 8,
        'grouping': {'filter_bolt': {'type': 'fields', 'fields': ['sensor_id']}}
    }

    # Bolt 4: Generate alerts
    alert_bolt = {
        'class': 'AlertBolt',
        'parallelism': 2,
        'grouping': {'aggregate_bolt': 'shuffle'}
    }

    # Bolt 5: Store to database
    db_bolt = {
        'class': 'DatabaseBolt',
        'parallelism': 4,
        'grouping': {'aggregate_bolt': 'shuffle'}
    }
```

### Implementation Details

**SensorSpout:**

```python
class SensorSpout(Spout):
    def initialize(self, conf, context):
        self.kafka = KafkaConsumer(
            'iot-sensors',
            bootstrap_servers=['localhost:9092']
        )

    def nextTuple(self):
        for message in self.kafka:
            self.emit([message.value], message_id=message.offset)
            time.sleep(0.001)  # Prevent tight loop
```

**ParseBolt:**

```python
class ParseBolt(Bolt):
    def process(self, tup):
        json_data = tup.values[0]
        data = json.loads(json_data)

        sensor_id = data['sensor_id']
        temperature = float(data['temperature'])
        timestamp = data['timestamp']

        self.emit([sensor_id, temperature, timestamp], anchors=[tup])
        self.ack(tup)
```

**AnomalyFilterBolt:**

```python
class AnomalyFilterBolt(Bolt):
    def process(self, tup):
        sensor_id, temperature, timestamp = tup.values

        if temperature > 50 or temperature < 0:
            # Emit to alert stream
            self.emit([sensor_id, temperature, timestamp, "CRITICAL"],
                     anchors=[tup], stream="alerts")
        elif temperature > 40 or temperature < 5:
            # Emit to warning stream
            self.emit([sensor_id, temperature, timestamp, "WARNING"],
                     anchors=[tup], stream="warnings")
        else:
            # Normal reading
            self.emit([sensor_id, temperature, timestamp, "NORMAL"],
                     anchors=[tup])

        self.ack(tup)
```

**AggregationBolt:**

```python
class AggregationBolt(Bolt):
    def initialize(self, conf, context):
        self.counts = {}
        self.sums = {}

    def process(self, tup):
        sensor_id, temperature, timestamp, status = tup.values

        # Aggregate statistics per sensor
        if sensor_id not in self.counts:
            self.counts[sensor_id] = 0
            self.sums[sensor_id] = 0.0

        self.counts[sensor_id] += 1
        self.sums[sensor_id] += temperature

        # Emit every 100 readings
        if self.counts[sensor_id] % 100 == 0:
            avg = self.sums[sensor_id] / self.counts[sensor_id]
            self.emit([sensor_id, avg, self.counts[sensor_id]],
                     anchors=[tup])

        self.ack(tup)
```

## Storm Configuration

### Topology Configuration

```python
import storm

topology_config = {
    # Parallelism
    'topology.workers': 4,
    'topology.max.spout.pending': 1000,

    # Reliability
    'topology.message.timeout.secs': 30,
    'topology.max.task.parallelism': 10,

    # Performance
    'topology.executor.receive.buffer.size': 1024,
    'topology.executor.send.buffer.size': 1024,
    'topology.transfer.buffer.size': 32,

    # Debugging
    'topology.debug': False,
}
```

### Parallelism Settings

```python
# Topology-level workers
conf.setNumWorkers(4)

# Component-level parallelism
builder.setSpout("sensor-spout", SensorSpout(), 2)  # 2 executors
builder.setBolt("process-bolt", ProcessBolt(), 8)    # 8 executors
```

**Parallelism Hierarchy:**

```
Workers (JVM processes)
  └─► Executors (threads)
       └─► Tasks (bolt/spout instances)
```

## Advantages of Storm

1. **Real-Time:** True stream processing, no batching delay
2. **Fast:** Processes millions of tuples per second
3. **Scalable:** Horizontal scaling by adding nodes
4. **Fault-Tolerant:** Automatic failover and recovery
5. **Guaranteed Processing:** At-least-once semantics
6. **Easy to Use:** Simple programming model
7. **Language Agnostic:** Multiple language support

## Limitations of Storm

1. **State Management:** Limited built-in state support
2. **Exactly-Once:** Only at-least-once by default
3. **Complex Debugging:** Distributed debugging challenges
4. **Resource Intensive:** Requires dedicated cluster
5. **Learning Curve:** Understanding topology concepts

## Storm vs Spark Streaming

| Aspect               | Storm             | Spark Streaming |
| -------------------- | ----------------- | --------------- |
| **Processing Model** | True streaming    | Micro-batch     |
| **Latency**          | Sub-second        | Seconds         |
| **Throughput**       | Good              | Excellent       |
| **State Management** | Limited           | Built-in        |
| **Fault Tolerance**  | Record-level      | Batch-level     |
| **Exactly-Once**     | External support  | Native support  |
| **Use Case**         | Ultra-low latency | High throughput |

## Summary

Apache Storm is a distributed real-time computation system for processing unbounded data streams. Its architecture consists of Nimbus (master), Supervisors (workers), and ZooKeeper (coordination), executing topologies—DAGs of Spouts (data sources) and Bolts (processing logic).

Storm provides guaranteed message processing through tuple tracking and ack/fail mechanisms, ensuring at-least-once semantics. Stream groupings (shuffle, fields, all, global) control tuple distribution between tasks, enabling various processing patterns.

For IoT applications, Storm excels at real-time analytics requiring sub-second latency, continuous anomaly detection, instant alerting, and live dashboards. It handles millions of tuples per second with fault tolerance and horizontal scalability.

## Key Takeaways for Exams

1. **Storm Definition:** Distributed real-time computation system for unbounded streams

2. **Architecture:** Nimbus (master) + Supervisors (workers) + ZooKeeper (coordination)

3. **Topology:** DAG of Spouts (data sources) and Bolts (processing logic)

4. **Spouts:** Read from external sources, emit tuples, can replay on failure

5. **Bolts:** Process tuples, transform data, emit to downstream bolts

6. **Stream Groupings:** Shuffle (random), Fields (by key), All (broadcast), Global (single task)

7. **Guaranteed Processing:** Tuple tracking, ack/fail mechanism, configurable timeout

8. **Parallelism:** Workers (processes) → Executors (threads) → Tasks (instances)

9. **IoT Use Cases:** Real-time monitoring, anomaly detection, instant alerts, live dashboards

10. **Storm vs Spark Streaming:** Storm=true streaming (sub-second), Spark=micro-batch (seconds)
