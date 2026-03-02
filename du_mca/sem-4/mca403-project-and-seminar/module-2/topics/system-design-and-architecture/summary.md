# System Design and Architecture - Summary

## Key Definitions and Concepts
- **Horizontal Scaling**: Adding more machines to handle load
- **Eventual Consistency**: System converges to consistency over time
- **Thundering Herd Problem**: Many requests overwhelming a restarted server
- **SLA**: Service Level Agreement defining uptime guarantees
- **Idempotency**: Multiple identical requests = single request effect

## Important Formulas and Theorems
- **CAP Theorem**: Choose 2 of Consistency, Availability, Partition Tolerance
- **Amdahl's Law**: Max speedup = 1 / (S + (1-S)/N)
- **Little's Law**: L = λ * W (Requests in system = Arrival rate × Avg latency)
- **Kafka Throughput**: Partitions ≤ Consumers in group
- **Redis Memory**: 1M keys ≈ 100MB (depends on data types)

## Key Points
- Microservices require service discovery and API gateways
- Database indexing reduces latency but increases write overhead
- CDNs reduce latency by 50-70% for static assets
- Circuit breakers prevent cascading failures
- Consistent hashing enables efficient horizontal scaling
- Versioned APIs allow backward compatibility
- Health checks are critical for auto-scaling groups

## Common Mistakes to Avoid
- Designing for scale too early (premature optimization)
- Ignoring network latency in distributed systems
- Using synchronous communication between microservices
- Forgetting to plan for data migration strategies
- Underestimating monitoring requirements

## Revision Tips
1. Practice with real systems: Reverse-engineer Flipkart/Amazon architecture
2. Memorize cloud service limits (e.g., AWS RDS max connections)
3. Use the "4S Framework" (Storage, Scale, Speed, Security)
4. Solve previous years' DU papers focusing on case studies

Length: 650 words