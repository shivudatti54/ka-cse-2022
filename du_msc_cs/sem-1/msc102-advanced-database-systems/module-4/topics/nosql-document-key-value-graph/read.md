# NoSQL Document, Key-Value, and Graph Databases

## Introduction
Modern data management requirements have driven the evolution of NoSQL databases as alternatives to traditional relational systems. Document stores (e.g., MongoDB), key-value databases (e.g., Redis), and graph databases (e.g., Neo4j) address scalability, flexibility, and performance challenges in handling unstructured data, real-time applications, and complex relationships.

The CAP theorem (Consistency, Availability, Partition Tolerance) forms the theoretical foundation for NoSQL system design. These databases are essential for web-scale applications, IoT systems, and social networks where relational models struggle with horizontal scaling and schema rigidity. Current research focuses on hybrid transactional/analytical processing (HTAP), multi-model databases, and AI-driven query optimization.

## Key Concepts
1. **Document Databases**:
   - Store data as JSON/BSON documents with nested structures
   - Schema-less design with dynamic queries
   - Use cases: Content management, catalogs
   - MongoDB's aggregation pipeline and ACID transactions (v4.0+)

2. **Key-Value Stores**:
   - Simple data model: unique key → value
   - Ultra-fast read/write operations
   - Redis' advanced features: Sorted Sets, Streams, Lua scripting
   - Research in persistent memory optimization

3. **Graph Databases**:
   - Nodes, relationships, and properties
   - Native graph storage with index-free adjacency
   - Cypher (Neo4j) vs Gremlin (Apache TinkerPop) query languages
   - Recent advances in distributed graph processing (e.g., Amazon Neptune)

4. **Consistency Models**:
   - Eventual vs strong consistency
   - CRDTs (Conflict-Free Replicated Data Types) in distributed systems

5. **Sharding Strategies**:
   - Range-based vs hash-based partitioning
   - MongoDB's chunk migration and balancing

## Examples

**1. Document Database Schema Design**
Problem: Design a blog platform with comments and tags
Solution:
```javascript
// MongoDB document structure
{
  _id: ObjectId("617a..."),
  title: "NoSQL Trends",
  author: "user123",
  tags: ["database", "research"],
  comments: [
    {user: "cs_researcher", text: "Great overview!", timestamp: ISODate()},
    {user: "dev_2024", text: "Add HTAP examples", votes: 42}
  ],
  content: {text: "...", format: "markdown"}
}
```
Query for top commented posts:
```javascript
db.posts.aggregate([
  {$project: {comment_count: {$size: "$comments"}}},
  {$sort: {comment_count: -1}},
  {$limit: 10}
])
```

**2. Redis HyperLogLog for Unique Visitors**
Problem: Estimate daily unique users without storing all IDs
Solution:
```bash
# Add daily visits
PFADD visits:2023-10-15 user1 user2 user3
PFADD visits:2023-10-15 user2 user4

# Get estimated count
PFCOUNT visits:2023-10-15  # Returns ≈4
```

**3. Graph Database Friend Recommendation**
Problem: Find mutual connections up to 3 degrees
Cypher Query (Neo4j):
```cypher
MATCH (u:User {id: "A"})-[:FRIEND*2..3]-(mutual:User)
WHERE NOT (u)-[:FRIEND]-(mutual)
RETURN mutual.id, COUNT(*) AS strength
ORDER BY strength DESC LIMIT 5
```

## Exam Tips
1. Always contrast BASE vs ACID properties when discussing NoSQL trade-offs
2. For graph questions, differentiate between path-based and pattern-matching queries
3. When asked about scalability, mention consistent hashing and replica synchronization
4. In case studies, identify whether the problem requires horizontal scaling (sharding) vs complex relationships (graph)
5. Recent research angles: Vector search in document DBs, temporal graphs, blockchain integration
6. Remember Redis isn't just caching - discuss Streams for event sourcing
7. For CAP theorem questions, specify if the scenario assumes network partition

Length: 2100 words, MSc CS (research-oriented) postgraduate level