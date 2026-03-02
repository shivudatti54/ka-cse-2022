# Apache Spark Streaming - Summary

## Key Definitions and Concepts

- **Spark Streaming**: Extension of Apache Spark for processing real-time data streams using micro-batching
- **DStream (Discretized Stream)**: Fundamental abstraction representing a continuous series of RDDs, where each RDD contains data from a specific time interval
- **Micro-batch Processing**: Spark Streaming's approach of dividing streams into small batches (typically 1-5 seconds) processed by the Spark engine
- **StreamingContext**: Main entry point for Spark Streaming functionality that coordinates receivers, batch creation, and job scheduling
- **Checkpointing**: Mechanism for saving streaming metadata and state to persistent storage for fault tolerance

## Important Formulas and Concepts

- **Window Calculations**: Window length defines the total time span considered; sliding interval defines how often windows are computed
- **reduceByKeyAndWindow Optimization**: Uses inverse functions to efficiently add new data and remove expired data without reprocessing entire windows
- **Throughput**: Measured in records/second, influenced by batch interval, parallelism, and receiver configuration

## Key Points

- Spark Streaming processes data in micro-batches (not true streaming), providing exactly-once semantics
- DStreams are sequences of RDDs organized by time intervals, maintaining RDD lineage for fault tolerance
- Stateless transformations process each batch independently; stateful transformations maintain accumulated state
- Window operations require checkpointing and use sliding intervals to compute results over moving time windows
- Checkpointing is essential for stateful transformations and driver failure recovery
- Spark Streaming integrates with Kafka, Flume, Twitter, sockets, and custom receivers
- The Receiver abstraction runs within executors to collect and buffer incoming data
- Backpressure handling prevents system overload when data arrives faster than it can be processed

## Common Mistakes to Avoid

- Forgetting to enable checkpointing when using stateful transformations, leading to state loss on driver restart
- Setting batch intervals too small, causing excessive overhead, or too large, causing high latency
- Not understanding that DStreams are lazily evaluated—output operations trigger actual processing
- Confusing window length with sliding interval; these are distinct parameters with different effects
- Neglecting to call `ssc.awaitTermination()` which causes the streaming context to exit immediately

## Revision Tips

1. Practice writing Spark Streaming applications from scratch, including creating StreamingContext and defining transformation chains

2. Trace through window operation examples manually, calculating which data points fall into each window interval

3. Review the checkpointing configuration needed for different scenarios—metadata-only for stateless jobs, full checkpointing for stateful jobs

4. Understand the relationship between Spark Streaming and Spark Core—DStream operations compile to RDD operations, making the connection explicit
5. Review Kafka integration patterns, particularly offset management and the role of Write-Ahead Logs for fault tolerance