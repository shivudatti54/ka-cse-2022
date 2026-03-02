# NoSQL Databases Types - Summary

## Key Definitions and Concepts
- **Document Database**: Stores semi-structured data as self-describing documents
- **Column-Family Store**: Groups columns into logical families for vertical partitioning
- **Edge**: A directed relationship between nodes in graph databases
- **Eventual Consistency**: Guarantees updates propagate through system eventually

## Important Formulas and Theorems
- **CAP Theorem**: A distributed system can only guarantee 2/3 of Consistency, Availability, Partition Tolerance
- **BASE Properties**: Basically Available, Soft state, Eventual consistency
- **Time Complexity for Graph Traversals**: O(1) for adjacent nodes vs O(n) in RDBMS joins

## Key Points
- Document databases excel at hierarchical data storage
- Key-value stores provide fastest read/write operations
- Column-family databases optimize for write-heavy workloads
- Graph databases minimize JOIN operations through native relationships
- NoSQL systems typically sacrifice ACID for horizontal scalability
- Cassandra uses tunable consistency levels (ONE, QUORUM, ALL)
- Polyglot persistence: Using multiple database types in one system

## Common Mistakes to Avoid
- Using document databases for complex transactions
- Choosing graph databases for simple key-value needs
- Ignoring consistency requirements when selecting AP systems
- Overlooking operational complexity of sharding
- Assuming all NoSQL databases are schema-less (some require schema definitions)

## Revision Tips
- Create comparison tables: Features vs Use Cases vs Limitations
- Practice writing sample queries for each database type
- Study real-world implementations (e.g., Amazon DynamoDB paper)
- Focus on CAP theorem decision trees
- Use flashcards for database-type characteristics

Length: 400-800 words