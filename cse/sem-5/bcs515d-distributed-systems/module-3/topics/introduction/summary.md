# Introduction to Distributed Systems - Summary

## Key Definitions

- **Distributed System**: A collection of autonomous computers linked by a network that appear to users as a single coherent system.
- **Node/Site**: An individual computer within a distributed system.
- **Transparency**: The property that hides the distributed nature of the system from users.
- **Middleware**: Software layer that provides services to bridge heterogeneity in distributed systems.

## Important Formulas

No specific formulas are applicable to this introductory topic. However, key relationships exist between:
- CAP Theorem: Consistency, Availability, Partition Tolerance
- These properties cannot all be simultaneously guaranteed in distributed systems.

## Key Points

1. Distributed systems consist of multiple independent computers communicating via message passing over a network.

2. The four fundamental characteristics are concurrency, no shared memory, independent failure, and absence of global clock.

3. The primary goals are resource sharing, transparency, openness, scalability, and fault tolerance.

4. Distributed systems types include distributed computing systems, distributed information systems, and distributed pervasive systems.

5. Major challenges include heterogeneity, security, scalability, and failure handling.

6. The web, distributed databases, and blockchain represent prominent examples of distributed systems.

7. Transparency comes in multiple forms: access, location, replication, migration, and concurrency transparency.

8. The "8 fallacies of distributed computing" identify common misconceptions that lead to system failures.

## Common Mistakes

1. Confusing distributed systems with parallel systems—parallel systems typically share memory while distributed systems do not.

2. Assuming network reliability—networks are inherently unreliable and messages can be lost, duplicated, or delayed.

3. Ignoring failure modes—designing systems without considering how individual component failures affect the whole.

4. Overlooking the importance of transparency—failing to understand why hiding distribution is crucial for usability and maintainability.