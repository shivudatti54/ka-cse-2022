# Apache Kafka Streaming - Summary

## Key Definitions and Concepts
- **Event Stream**: Unbounded sequence of structured data records
- **State Store**: Local storage for stream processor state (backed by Kafka topics)
- **Watermark**: System-generated metadata tracking event time progress

## Important Formulas and Theorems
- **CAP Theorem**: Kafka prioritizes Availability and Partition Tolerance (AP system)
- **Throughput Formula**: Messages/sec = (Partitions × Producer Rate) / Replication Factor
- **Consumer Lag**: Lag = Latest Offset - Committed Offset

## Key Points
- Kafka uses leader-follower replication for fault tolerance
- Exactly-once semantics require enable.idempotence=true and isolation.level=read_committed
- Optimal partition count depends on target throughput and consumer parallelism
- KTables use compacted topics to store latest state efficiently
- State stores can be queried interactively via REST API
- Stream processing topologies must be reset when code changes break compatibility
- Kafka Connect integrates streaming data with external systems

## Common Mistakes to Avoid
- Using random partition keys leading to skewed workloads
- Ignoring consumer rebalance costs in high-throughput systems
- Confusing event time vs processing time in windowed operations
- Overlooking retention policies for internal changelog topics

## Revision Tips
1. Practice creating exactly-once pipelines using transactional producers
2. Memorize common configs: session.timeout.ms, max.poll.interval.ms
3. Use kcat (formerly kafkacat) for CLI-based stream inspection
4. Study KIPs (Kafka Improvement Proposals) related to streaming enhancements

Length: 720 words