# Distributed Systems - Summary

## Key Definitions and Concepts

- **Distributed System**: A collection of independent computers linked by a network that appears to users as a single coherent system, with resources and processes transparent to users.

- **Transparency**: The property that masks the distribution of resources from users. Types include access, location, migration, replication, concurrency, performance, and failure transparency.

- **Middleware**: Software layer between the OS and applications that provides common services like communication, transaction management, and security for distributed applications.

- **Remote Procedure Call (RPC)**: A communication paradigm allowing programs to execute code on remote machines through procedure call semantics.

- **Two-Phase Commit**: A protocol ensuring atomicity in distributed transactions by requiring all participants to prepare before committing.

## Important Formulas and Theorems

- **CAP Theorem**: States that a distributed system can provide only two of three guarantees—Consistency, Availability, and Partition tolerance simultaneously.

- **ACID Properties**: Atomicity (all or nothing), Consistency (valid state transitions), Isolation (concurrent transactions appear serial), Durability (committed changes survive failures).

## Key Points

1. Distributed systems consist of multiple autonomous computers that cooperate to provide a single system image to users.

2. The seven transparency types mask different aspects of distribution—location, access, migration, replication, concurrency, failure, and performance.

3. Distributed operating systems provide a single system image, while network operating systems maintain separate images on each machine.

4. Distributed systems offer advantages including resource sharing, reliability, scalability, flexibility, and openness.

5. Disadvantages include complexity in design, security vulnerabilities, network dependency, and difficult debugging.

6. Three main types: distributed computing systems (high-performance computing), distributed information systems (integration), and distributed pervasive systems (ubiquitous computing).

7. Communication in distributed systems uses message passing, RPC, or distributed shared memory models.

8. Middleware provides essential services and abstractions for building distributed applications.

## Common Mistakes to Avoid

1. Confusing network operating systems with distributed operating systems—network OS lacks single system image.

2. Believing distributed systems eliminate all failures—failures still occur but must be handled transparently.

3. Ignoring security challenges—distributed systems present more attack surfaces than centralized systems.

4. Overlooking performance overhead—communication between machines introduces latency compared to local operations.

5. Assuming transparency is always complete—some trade-offs exist between transparency and performance in real systems.

## Revision Tips

1. Create a comparison table between distributed OS and network OS to remember key differences.

2. Memorize the seven transparency types using a mnemonic or organized list.

3. Study real examples like NFS and DNS to understand how theory applies in practice.

4. Review the CAP theorem and ACID properties as they frequently appear in exams.

5. Practice drawing and explaining distributed system architectures from the perspective of different stakeholders (users, developers, administrators).