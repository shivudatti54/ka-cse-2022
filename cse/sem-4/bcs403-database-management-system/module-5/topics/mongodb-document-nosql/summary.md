# Document-Based NoSQL Systems and MongoDB - Summary

## Key Definitions and Concepts

- **NoSQL Database**: A non-relational database designed for flexible schemas, horizontal scalability, and handling unstructured or semi-structured data; includes document, key-value, column-family, and graph databases.

- **Document Database**: A NoSQL database that stores data as documents (typically JSON/BSON format) with key-value pairs, allowing nested structures and varying schemas within collections.

- **MongoDB**: A popular document-based NoSQL database that stores data in BSON format, provides horizontal scalability through sharding, and high availability through replica sets.

- **BSON**: Binary JSON, the binary-encoded serialization format used by MongoDB that extends JSON with additional data types like Date, ObjectId, and binary data.

- **Collection**: A group of MongoDB documents, analogous to a table in relational databases but without a fixed schema.

- **Shard Key**: A field or fields used to partition data across shards in a MongoDB cluster for horizontal scaling.

## Important Formulas and Theorems

- **Aggregation Pipeline**: Data processing pipeline using stages like $match, $group, $project, $sort to transform documents
- **Index Types**: Single-field (1 field), Compound (multiple fields), Multikey (array fields), Text (full-text search), Hashed (distribution)
- **Replica Set**: Primary + Secondary nodes with automatic failover using oplog for replication

## Key Points

1. MongoDB stores data in flexible, JSON-like BSON documents with dynamic schemas, eliminating the need for predefined table structures.

2. The **\_id** field serves as the primary key and is automatically created as ObjectId if not explicitly provided.

3. MongoDB supports rich query operators including comparison ($gt, $lt, $eq), logical ($and, $or), and array operators ($in, $all, $elemMatch).

4. Indexes significantly improve query performance but add overhead to write operations; choose indexes based on actual query patterns.

5. Aggregation framework processes documents through multiple stages enabling complex transformations and analytics.

6. Replica sets provide high availability with automatic failover, with one primary and multiple secondary nodes maintaining identical data.

7. Sharding enables horizontal scaling by distributing data across multiple servers based on shard key selection.

8. MongoDB trades strong consistency for eventual consistency in distributed deployments, prioritizing availability.

## Common Mistakes to Avoid

1. Creating too many indexes without analyzing query patterns, causing unnecessary overhead on write operations.

2. Choosing poorly distributed shard keys leading to hot-spotting and unbalanced clusters.

3. Storing deeply nested documents excessively, making queries and updates inefficient.

4. Not using projection to limit returned fields, causing unnecessary data transfer and memory usage.

5. Ignoring the flexible schema nature and treating MongoDB like a relational database with rigid structures.

## Revision Tips

1. Practice CRUD operations in MongoDB shell to reinforce syntax and query operators.

2. Understand index trade-offs by using explain() to analyze query execution plans.

3. Review aggregation pipeline examples to understand stage ordering and optimization.

4. Remember the differences between embedded documents and normalized references for schema design decisions.

5. Focus on understanding when MongoDB is preferable over relational databases and vice versa.
