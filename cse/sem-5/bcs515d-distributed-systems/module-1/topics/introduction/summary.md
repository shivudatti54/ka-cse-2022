# Introduction to Distributed Systems - Summary

## Key Definitions
- **Distributed System**: A collection of independent computers that appear to users as a single coherent system; nodes communicate solely through message passing
- **Middleware**: Software layer that abstracts heterogeneity of underlying networks, operating systems, and programming languages
- **Transparency**: The hiding of the distributed nature of a system from users and applications; includes access, location, migration, relocation, replication, failure, and concurrency types

## Important Formulas
- No specific mathematical formulas apply to this introductory topic; however, understanding the CAP theorem trade-offs (Consistency + Availability + Partition Tolerance = choose any 2) is essential

## Key Points
1. Distributed systems consist of multiple autonomous nodes that coordinate through message passing, without shared memory
2. The five fundamental goals are resource sharing, openness, concurrency, scalability, and transparency
3. Middleware provides location transparency and handles communication complexities between heterogeneous components
4. Common architectures include client-server, three-tier, peer-to-peer, and microservices
5. Real-world examples include DNS (hierarchical), World Wide Web (client-server), and distributed databases (partitioned)
6. Distributed systems face inherent challenges: heterogeneity, openness, security, scalability, and failure handling
7. The CAP theorem states that during network partitions, systems must choose between consistency and availability
8. Distributed systems evolved from centralized mainframes due to needs for scalability, reliability, and cost-effectiveness

## Common Mistakes
1. Confusing distributed systems with parallel computing systems—parallel systems share memory while distributed systems use message passing
2. Assuming transparency is all-or-nothing; different applications require different levels and types of transparency
3. Overlooking the trade-offs involved in distributed system design—no solution optimizes all desired properties simultaneously
4. Underestimating the impact of network characteristics—latency, bandwidth, and reliability significantly affect system behavior