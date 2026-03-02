# Stream Processing - Summary

## Key Definitions and Concepts

- **Stream Processing**: A computing paradigm that processes continuous data streams in real-time as data arrives, without storing in permanent storage
- **Batch Processing**: Traditional approach that processes finite datasets stored on disk in scheduled jobs, with higher latency
- **Windowing**: Technique to compute aggregates over finite subsets of infinite streams using tumbling, sliding, or session windows
- **Exactly-Once Processing**: Guarantee that each event is processed exactly once, ensuring no duplicates or missing data
- **Stateful Stream Processing**: Maintaining intermediate state (counters, aggregates) across events for computations like joins and windowed aggregations

## Important Formulas and Concepts

- **Tumbling Windows**: Fixed-size, non-overlapping windows — windows[0-5), windows[5-10), windows[10-15)
- **Sliding Windows**: Overlapping windows defined by size and slide interval — if size=10, slide=5: windows[0-10), windows[5-15), windows[10-20)
- **Session Windows**: Group events separated by gap less than threshold — dynamically sized based on activity gaps

## Key Points

- Stream processing addresses latency requirements that batch processing cannot meet, enabling real-time analytics and instant responses
- Apache Kafka serves as the de facto standard for data ingestion and durable streaming in modern architectures
- Apache Flink provides the most comprehensive stream processing capabilities including exactly-once guarantees, event-time processing, and sophisticated windowing
- Windowing transforms infinite streams into finite datasets for aggregation and analysis
- Cloud providers offer fully managed services (Kinesis, Dataflow, Stream Analytics) that reduce operational overhead
- Stream processing enables critical applications including fraud detection, IoT monitoring, and real-time personalization

## Common Mistakes to Avoid

- Confusing processing time (when event is processed) with event time (when event occurred) — leads to incorrect results with late-arriving data
- Using tumbling windows when sliding windows are needed — results in missed patterns that span window boundaries
- Underestimating state storage requirements for stateful stream processing — can cause memory issues at scale
- Choosing a framework without considering operational complexity and team expertise

## Revision Tips

1. Practice drawing stream processing architectures and labeling components (ingestion, processing, storage, output)
2. Write SQL-like queries for different window types to reinforce understanding
3. Review case studies of real-world stream processing deployments for application context
4. Compare framework features using a comparison table for quick revision