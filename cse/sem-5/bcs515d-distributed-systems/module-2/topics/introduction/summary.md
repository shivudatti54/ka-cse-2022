# Introduction to Distributed Systems - Summary

## Key Definitions

- **Distributed System**: A collection of independent computers that appear to users as a single coherent system, with components communicating through a network to coordinate their actions.

- **Transparency**: The property of hiding the distributed nature of a system from users and applications, making the system appear as a unified whole.

- **Heterogeneity**: The presence of diverse hardware platforms, operating systems, programming languages, and network protocols within a distributed environment.

- **Scalability**: The ability of a system to handle increased load by adding more resources, either through horizontal scaling (adding more machines) or vertical scaling (upgrading hardware).

- **Fault Tolerance**: The capability of a system to continue operating correctly even when some components fail.

- **Middleware**: Software layer that provides common services and abstractions to mask heterogeneity in distributed systems.

## Important Formulas

The CAP Theorem (Brewer's Theorem):
- **CAP = Consistency + Availability + Partition Tolerance**
- A distributed system can guarantee only two of three properties simultaneously
- Mathematical relationship: `max(CAP properties guaranteed) = 2`

## Key Points

1. Distributed systems consist of multiple independent computers connected by a network, presenting a unified view to users.

2. Eight forms of transparency exist: access, location, migration, replication, concurrency, failure, performance, and size transparency.

3. Primary advantages include resource sharing, openness, scalability, concurrency, fault tolerance, and deployment flexibility.

4. Fundamental challenges encompass heterogeneity, network unreliability, lack of global clock, security vulnerabilities, and system complexity.

5. Client-server architecture separates service providers (servers) from service consumers (clients), while peer-to-peer architecture treats all nodes as equals.

6. The CAP theorem establishes fundamental tradeoffs: systems must choose between consistency and availability during network partitions.

7. Middleware layers abstract platform differences and provide standardized interfaces for distributed application development.

8. Real-world examples include web search engines, online banking systems, and cloud storage services.

## Common Mistakes

1. **Confusing distributed with parallel systems**: Parallel systems aim to solve a single problem faster using multiple processors, while distributed systems coordinate independent computers to provide services.

2. **Assuming networks are reliable**: Networks experience failures, delays, and partitions; distributed system designs must account for these realities rather than assuming perfect communication.

3. **Ignoring partial failures**: Unlike centralized systems where failure is typically total, distributed systems can experience partial failures where some components work while others fail.

4. **Underestimating complexity**: Distributed systems introduce significant complexity in design, development, testing, and maintenance that often exceeds initial projections.