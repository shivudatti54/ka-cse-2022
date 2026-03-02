# Distributed Systems - Summary

## Key Definitions

- **Distributed System**: A collection of independent computers that appear to users as a single coherent system, linked by a network with software producing an integrated computing facility
- **Transparency**: The degree to which a distributed system hides its distributed nature from users and applications
- **Middleware**: Software layer providing common services to distributed applications, handling communication, transactions, and security
- **Remote Procedure Call (RPC)**: Communication paradigm allowing programs to call procedures on remote machines as if they were local

## Important Formulas

- No specific mathematical formulas are central to distributed systems theory, but understanding the CAP theorem trade-offs is essential: Consistency + Availability + Partition Tolerance = Pick 2

## Key Points

- Distributed systems consist of multiple autonomous nodes connected via a network, each with local resources
- The primary goal is to present a single-system image while managing distributed resources
- Eight types of transparency exist: access, location, migration, replication, concurrency, failure, performance, and scaling
- Client-server remains the most common architecture, though peer-to-peer is growing for decentralized applications
- Distributed operating systems provide tighter integration than network operating systems
- Communication occurs through message passing, RPC, or distributed shared memory paradigms
- Partial failure is the fundamental challenge—components can fail independently
 synchronization across nodes- Clock requires special algorithms due to network delays
- Middleware abstracts hardware and OS heterogeneity to provide uniform application interfaces

## Common Mistakes

- Confusing distributed systems with parallel systems (multiple CPUs in one machine) or network operating systems
- Assuming network reliability—distributed systems must handle network partitions gracefully
- Ignoring the CAP theorem trade-offs when designing distributed applications
- Underestimating the complexity of maintaining consistency in distributed databases
- Overlooking security considerations inherent in multiple entry points and network communication