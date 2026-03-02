# API Usage and Its Effect on Capacity - Summary

## Key Definitions and Concepts

- **API (Application Programming Interface):** A set of protocols enabling communication between software systems; the primary mechanism for inter-service communication in modern architectures.

- **Throughput:** Measured in requests per second (RPS) or transactions per second (TPS); represents the volume of API calls the system processes.

- **Rate Limiting:** Control mechanism that restricts the number of requests a client can make within a time window to prevent system overload.

- **Cache Hit Rate:** Percentage of API requests served from cache rather than requiring backend processing; directly reduces capacity requirements.

- **Connection Pooling:** Technique for managing multiple database or service connections efficiently to reduce connection establishment overhead.

## Important Formulas and Theorems

- **Concurrent Requests = Throughput (RPS) × Response Time (seconds)**
- Determines the average number of simultaneous requests the system must handle.

- **Servers Needed = Maximum Concurrent Requests ÷ Max Concurrent per Server**
- Calculates infrastructure requirements based on connection limits.

- **Cache Hit Rate Impact = Total Requests × (1 - Hit Rate) = Backend Queries**
- Determines backend load reduction from caching.

- **Effective Capacity with Rate Limit = Rate Limit Setting × Utilization Factor**
- Calculates protected capacity when implementing rate limiting.

## Key Points

1. REST APIs are more capacity-efficient than SOAP APIs due to smaller payload sizes and simpler processing requirements.

2. Each API request consumes CPU, memory, network bandwidth, and potentially database connections; capacity planning must account for all these resources.

3. Rate limiting is essential for protecting API infrastructure; token bucket allows bursts while leaky bucket provides predictable processing rates.

4. Caching at multiple levels (client, gateway, server) can reduce backend load by 90% or more with appropriate cache hit rates.

5. Load balancing distributes traffic across instances; least connections works best for heterogeneous servers while round robin suits homogeneous setups.

6. P50, P90, P95, and P99 response time percentiles are more meaningful than averages for capacity planning.

7. API design directly impacts capacity; well-designed APIs with proper data granularity minimize unnecessary resource consumption.

8. Peak traffic handling requires infrastructure designed for maximum load plus safety margins of 20-30%.

## Common Mistakes to Avoid

- Planning capacity based only on average traffic instead of peak loads
- Ignoring cache memory requirements when calculating infrastructure needs
- Setting rate limits too aggressively, causing legitimate traffic rejection
- Underestimating the impact of payload size on network capacity
- Failing to consider connection pooling effects on concurrent connection limits

## Revision Tips

1. Remember the capacity formula: Concurrent Requests = RPS × Response Time - this is fundamental for capacity calculations.

2. Review the three main caching strategies (client, gateway, server) and understand when each is most effective.

3. Compare token bucket versus leaky bucket rate limiting with specific use cases for each.

4. Practice calculating capacity requirements using the worked examples in this topic.

5. Focus on understanding how different API types (REST, SOAP, GraphQL) have different capacity implications rather than memorizing details.
