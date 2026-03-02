# Introduction to Distributed Systems - Summary

## Key Definitions

- **Distributed System**: A collection of independent computers that appear to users as a single coherent system, communicating through message passing over a network.

- **Transparency**: The degree to which the distribution of components is hidden from users and applications, presenting the system as a single entity.

- **Scalability**: The ability of a system to handle growth in users, data, or geographic distribution without significant performance degradation.

- **Heterogeneity**: The diversity of hardware, operating systems, programming languages, and network technologies that must interoperate in a distributed system.

- **Openness**: The property of a system that allows it to be extended and implemented in various ways through standard interfaces and protocols.

## Important Formulas

- **CAP Theorem**: A distributed system can provide only two of three guarantees simultaneously: Consistency, Availability, and Partition tolerance. Formally: `CAP = {Consistency, Availability, Partition Tolerance} |Result| = 2`

- **Amdahl's Law** (for parallel processing): `Speedup = 1 / (S + (1-S)/N)` where S is the sequential portion and N is the number of processors. This limits the benefits of distribution due to inherently sequential components.

## Key Points

1. Distributed systems achieve goals including resource sharing, openness, concurrency, and scalability that centralized systems cannot efficiently provide.

2. The eight types of transparency are: access, location, migration, relocation, replication, failure, concurrency, and persistence.

3. Client-server architecture is the simplest model; peer-to-peer eliminates central authority but complicates coordination.

4. Asynchronous systems, with no bounds on message delays or processing times, present the greatest algorithmic challenges.

5. Partial failures are characteristic of distributed systems—some components may fail while others continue functioning normally.

6. The CAP theorem forces designers to choose between consistency and availability during network partitions.

7. Byzantine failures, where nodes behave arbitrarily or maliciously, are the most challenging to handle and require consensus protocols.

8. Real-world distributed systems (DNS, distributed databases, blockchain) demonstrate practical solutions to the theoretical challenges.

## Common Mistakes

1. **Confusing transparency with invisibility**: Transparency does not mean users cannot know about distribution; it means the complexity of distribution is abstracted away.

2. **Misunderstanding CAP theorem**: Many assume all three properties can be achieved simultaneously; in practice, partition tolerance is mandatory, forcing a C vs. A choice.

3. **Ignoring network assumptions**: Algorithms designed for synchronous systems often fail catastrophically in asynchronous environments.

4. **Overlooking partial failures**: Beginners often think in terms of complete system failure, missing the more common case where some nodes fail while others operate normally.

5. **Equating distributed systems with cloud computing**: Cloud computing is an application of distributed systems, but distributed systems encompass much broader concepts including peer-to-peer networks, grid computing, and blockchain.