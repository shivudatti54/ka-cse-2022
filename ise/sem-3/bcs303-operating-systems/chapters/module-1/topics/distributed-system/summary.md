# Distributed System - Summary

## Key Definitions and Concepts

- **Distributed System**: A collection of independent computers that appear to users as a single coherent system, connected via a computer network

- **Transparency**: The property that hides the distribution of resources from users; includes access, location, migration, replication, concurrency, and failure transparency

- **Middleware**: Software layer providing common services between distributed applications, hiding network and OS heterogeneity

- **RPC (Remote Procedure Call)**: A protocol enabling programs to execute procedures on remote systems as if they were local

## Important Formulas and Theorems

- **CAP Theorem**: In distributed systems, only two of Consistency, Availability, and Partition tolerance can be guaranteed simultaneously

- **ACID Properties** (for distributed transactions): Atomicity, Consistency, Isolation, Durability

## Key Points

- Distributed systems consist of multiple autonomous nodes communicating exclusively through message passing

- Key advantages include scalability through horizontal growth, fault tolerance via redundancy, resource sharing across geographic boundaries, and improved performance through parallel processing

- Major challenges involve network unreliability, security vulnerabilities at multiple entry points, complexity in design and maintenance, and maintaining data consistency across nodes

- Client-server architecture has dedicated servers managing resources while clients provide user interfaces

- Peer-to-peer architecture allows all nodes to function as both clients and servers

- Distributed operating systems provide single-system image while network operating systems maintain separate identities on each node

- Distributed file systems present unified namespace across physical storage locations

- DNS, World Wide Web, and distributed databases are classic examples of distributed systems

## Common Mistakes to Avoid

- Confusing distributed systems with parallel systems—parallel systems share memory while distributed systems communicate via messages

- Believing distributed systems always outperform centralized systems—they introduce overhead from communication and coordination

- Ignoring the CAP theorem tradeoffs—systems must choose between consistency and availability during network partitions

- Mixing up network OS and distributed OS—network OS maintains separate identities while distributed OS provides unified view

## Revision Tips

1. Create comparison tables distinguishing distributed from centralized systems, and client-server from P2P architectures

2. Memorize the six types of transparency and be able to give examples of each

3. Review real-world examples like Google Search and BitTorrent to understand practical implementations

4. Focus on understanding why certain design choices are made in distributed systems rather than memorizing definitions

5. Practice explaining distributed system concepts in simple language—this helps in both theory and practical questions