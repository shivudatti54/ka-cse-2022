# Apache Storm

=====================================

### Overview

Apache Storm is a distributed real-time computation system for processing unbounded streams of data with sub-second latency. It provides guaranteed message processing, fault tolerance, and horizontal scalability, making it essential for IoT applications requiring instant analytics and immediate response to critical events.

### Key Points

- **Architecture:** Nimbus (master node for task distribution), Supervisors (worker nodes), and ZooKeeper (cluster coordination and state management)
- **Topology:** A DAG of Spouts (data sources that emit tuples) and Bolts (processing logic that transforms tuples)
- **Spouts:** Entry points that read from external sources (Kafka, MQTT), emit tuples, and can replay failed tuples for reliability
- **Bolts:** Receive and process tuples, perform transformations, filtering, aggregation, and emit results to downstream bolts
- **Stream Groupings:** Shuffle (random distribution), Fields (group by key), All (broadcast), Global (single task), Direct (producer chooses)
- **Guaranteed Processing:** Tuple tree tracking with ack/fail mechanism; tuples replayed from spout on timeout (default 30 seconds)
- **Parallelism Hierarchy:** Workers (JVM processes) contain Executors (threads) which contain Tasks (spout/bolt instances)

### Important Concepts

- Nimbus distributes code and assigns tasks, similar to Hadoop JobTracker; Supervisors manage worker processes on each machine
- Tuples are the basic data unit; Storm tracks entire tuple trees to guarantee end-to-end processing
- Fields grouping ensures same key always routed to same task, essential for stateful per-entity aggregation
- Storm provides at-least-once processing semantics by default; exactly-once requires external support

### Notes

- Storm vs Spark Streaming is a critical comparison: Storm is true streaming with sub-second latency; Spark Streaming uses micro-batches with seconds of latency
- Know all six stream grouping types and when to use each one
- IoT use cases include real-time monitoring, anomaly detection, instant alerting, and live dashboard updates
