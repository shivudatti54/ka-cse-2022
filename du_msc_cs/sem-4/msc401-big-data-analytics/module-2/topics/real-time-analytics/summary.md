# Real-Time Analytics - Summary

## Key Definitions and Concepts

- **Data Stream**: An infinite sequence of data elements arriving continuously over time, each typically carrying a timestamp
- **Stream Processing**: Computing over data streams, applying transformations and aggregations as events arrive
- **Event Time**: The timestamp when an event actually occurred in the source system
- **Processing Time**: The timestamp when an event is received and processed by the analytics system
- **Watermark**: A threshold mechanism indicating that all events with timestamps below the watermark have been processed, enabling window completion
- **Tumbling Window**: Non-overlapping, fixed-size time windows for periodic aggregations
- **Sliding Window**: Overlapping windows with a defined size and slide interval for trend analysis
- **Session Window**: Activity-based windows grouping events separated by gaps
- **Complex Event Processing (CEP)**: Detecting patterns across multiple events using temporal and logical constraints

## Important Formulas and Theorems

- **Watermark Progress**: A watermark of time T guarantees no events with timestamp < T will arrive
- **Window Bounds**: For tumbling windows starting at S with duration D, windows cover [S + kD, S + (k+1)D) for integer k
- **Sliding Window Overlap**: For window size W and slide S, overlap = W - S (if S < W)
- **Stream Join Window**: Join produces results for pairs (e1, e2) where |timestamp(e1) - timestamp(e2)| ≤ window_size

## Key Points

- Real-time analytics processes data in motion, enabling immediate responses to events as they occur
- Stream processing systems handle unbounded data with bounded resources through windowing
- Event time semantics are crucial for accurate analytics when network delays cause out-of-order arrivals
- Watermarks balance latency (how fast results are produced) against completeness (handling late events)
- Window selection significantly impacts analytics accuracy: tumbling for periodic metrics, sliding for trends, sessions for user behavior
- CEP extends stream processing to detect complex patterns across multiple correlated events
- Stream joins require windowing to bound computation and handle the infinite nature of streams
- Lambda architecture separates batch and speed layers; kappa architecture uses unified stream processing

## Common Mistakes to Avoid

- Confusing event time with processing time—using processing time when event time is required leads to incorrect results with delayed events
- Choosing inappropriate window sizes—too small windows miss patterns, too large windows increase latency
- Ignoring late event handling—without proper watermark strategies, results may be incomplete or inconsistent
- Overlooking state management—stream processors must efficiently maintain and checkpoint state across distributed processing
- Misunderstanding watermark semantics—watermarks are thresholds, not guarantees; some late events may still arrive after watermarks

## Revision Tips

1. Practice drawing timeline diagrams showing event arrival, watermark progression, and window computation for various scenarios
2. Write pseudo-code for different window types (tumbling, sliding, session) to reinforce understanding of boundary conditions
3. Review CEP pattern examples from fraud detection and monitoring domains to understand pattern expression
4. Compare lambda vs. kappa architectures with concrete examples of when each is preferable
5. Memorize the trade-offs: event time accuracy vs. processing time simplicity; low latency vs. complete results with watermarks