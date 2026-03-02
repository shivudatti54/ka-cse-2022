# Introduction to Distributed Systems - Summary

## Key Definitions

- **Distributed System**: A collection of independent computers that appear to users as a single coherent system, communicating via message passing over a network

- **Transparency**: The ability of a distributed system to hide its distributed nature from users, presenting a unified view

- **Middleware**: Software layer between applications and operating system that provides common services for distributed computing

- **CAP Theorem**: States that a distributed system can guarantee only two of Consistency, Availability, and Partition tolerance simultaneously

## Important Formulas

- No specific mathematical formulas in this introductory topic

## Key Points

- Distributed systems provide resource sharing, openness, scalability, concurrency, and fault tolerance as primary benefits

- Transparency levels include access, location, migration, replication, and concurrency transparency

- Client-server is the most common architecture; peer-to-peer distributes responsibilities equally among nodes

- Network issues (latency, failures, duplication) create fundamental challenges in distributed computing

- Middleware simplifies development by handling heterogeneity, distribution, and communication complexities

- The CAP theorem forces designers to make trade-offs based on application requirements

- Distributed systems must balance consistency, availability, and partition tolerance based on business needs

## Common Mistakes

1. Confusing distributed systems with parallel systems - parallel systems use shared memory while distributed systems use message passing

2. Believing that transparency can be fully achieved - practical systems can only approximate transparency

3. Ignoring the CAP theorem trade-offs when designing distributed applications

4. Underestimating network-related challenges and assuming reliable communication

5. Failing to distinguish between synchronous and asynchronous communication models in distributed systems