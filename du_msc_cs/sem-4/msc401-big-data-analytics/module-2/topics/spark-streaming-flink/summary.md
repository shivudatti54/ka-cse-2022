# Spark Streaming and Apache Flink - Summary

## Key Definitions and Concepts

- **DStream (Discretized Stream)**: Spark Streaming's abstraction representing a continuous sequence of RDDs, where each RDD contains data from a specific time interval (batch interval).
- **Micro-batching**: Spark Streaming's approach of treating streams as a sequence of small batch jobs, providing near-real-time processing with Spark's fault-tolerance guarantees.
- **Event Time**: The timestamp embedded in each event indicating when it actually occurred at the source, distinct from processing time.
- **Watermarks**: Timestamps in Flink that declare no events earlier than the watermark timestamp will arrive, enabling deterministic window completion despite out-of-order events.
- **Exactly-Once Processing**: A guarantee that each event is processed exactly once, with no duplicates or missed events, achieved through checkpointing and transactional sinks.
- **Stateful Stream Processing**: Maintaining and updating application state across streaming events, essential for aggregations, joins, and pattern detection.

## Important Formulas and Concepts

- **Window computation efficiency**: Spark's `reduceByKeyAndWindow` uses inclusion-exclusion: `new_count = old_count + added - removed`, reducing complexity from O(window/slide) to O(1) per batch.
- **Watermark lateness**: Events with timestamps < (watermark - max_lateness) are considered late and can be handled via side outputs.
- **Latency targets**: Spark Streaming ~100ms-1s; Flink ~1ms-100ms (true streaming).

## Key Points

1. Spark Streaming extends Spark's batch processing model to streaming via micro-batching; Flink is built natively for continuous stream processing.

2. Both frameworks provide exactly-once guarantees but achieve them through different mechanisms—checkpointing in Spark, distributed snapshots in Flink.

3. Flink's event-time processing with watermarks is superior for applications where event ordering matters and late data handling is required.

4. Structured Streaming in Spark 2.0+ represents a significant evolution, offering table-based semantics and improved event-time support.

5. Window operations differ significantly: Spark offers basic tumbling/sliding; Flink additionally provides session windows and global windows with flexible triggering.

6. State management in Flink is more sophisticated, supporting keyed state, operator state, and broadcast state with RocksDB backend for large state.

7. For MSc research, Flink's architecture supports complex event processing (CEP) library and FlinkML for streaming machine learning.

## Common Mistakes to Avoid

1. **Confusing processing time with event time**: Using processing time when event time is required leads to incorrect results when events are delayed or reordered.

2. **Ignoring checkpoint configuration**: Without proper checkpointing, stateful streaming applications lose all state on failure.

3. **Setting inappropriate watermark thresholds**: Too aggressive (events frequently dropped); too lenient (late results). Must match data characteristics.

4. **Not handling backpressure**: Without proper configuration, streaming applications can overwhelm downstream systems or run out of memory.

5. **Forgetting to set parallelism**: Running with parallelism=1 defeats distributed processing benefits and creates bottlenecks.

## Revision Tips

1. **Practice coding**: Implement basic streaming word count in both frameworks to internalize the API differences.

2. **Draw architecture diagrams**: Visualize the data flow from sources through transformations to sinks in both Spark Streaming and Flink.

3. **Compare systematically**: Create a comparison table covering latency, state management, fault tolerance, windowing, and event-time support.

4. **Understand theoretical foundations**: Review the Chandy-Lamport distributed snapshots algorithm used in Flink checkpoints.

5. **Review exam patterns**: Focus on conceptual questions about when to choose each framework and the trade-offs involved.