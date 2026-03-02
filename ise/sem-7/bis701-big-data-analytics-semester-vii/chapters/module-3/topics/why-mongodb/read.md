# MongoDB Document Store

## Introduction to MongoDB

MongoDB is a leading document-oriented NoSQL database that provides high performance, high availability, and easy scalability. Unlike traditional relational databases that store data in tables with fixed schemas, MongoDB stores data in flexible, JSON-like documents called BSON, making it ideal for handling unstructured or semi-structured data common in big data applications.

MongoDB falls under the document store category of NoSQL databases and is particularly well-suited for:
- Content management systems
- Real-time analytics
- Mobile applications
- Catalogs and user profiles
- Internet of Things (IoT) applications

## Key Concepts

### Documents and BSON

At the core of MongoDB is the **document**, which is a data structure composed of field-value pairs. Documents are similar to JSON objects but are stored in a binary representation called BSON (Binary JSON).

**BSON** extends JSON with additional data types and optimizations for efficiency:
- Supports dates, binary data, and other specific types
- Allows for faster encoding and decoding
- Provides better storage efficiency

Example document:
```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zip": "10001"
  },
  "hobbies": ["reading", "swimming", "coding"]
}
```

### Collections

Documents are organized into **collections**, which are analogous to tables in relational databases. However, unlike tables, collections don't enforce a schema, meaning documents within a collection can have different structures.

```
+-----------------+
|   Database      |
|   +-----------+ |
|   | Collection| |
|   | +-------+ | |
|   | |Document| | |
|   | +-------+ | |
|   | +-------+ | |
|   | |Document| | |
|   | +-------+ | |
|   +-----------+ |
+-----------------+
```

### Databases

A MongoDB instance can host multiple **databases**, each acting as a physical container for collections. Each database has its own set of files on the filesystem.

## MongoDB Architecture

### Replication

MongoDB uses **replica sets** to provide high availability. A replica set is a group of MongoDB instances that maintain the same data set.

```
Primary Node (Reads/Writes)
     ↑
     | Replication
     ↓
Secondary Node 1 (Reads)   Secondary Node 2 (Reads)
     ↑                           ↑
     └─────── Arbiter ───────────┘
```

- **Primary node**: Handles all write operations
- **Secondary nodes**: Replicate data from primary and can handle read operations
- **Arbiter**: Doesn't store data but participates in elections

### Sharding

For horizontal scaling, MongoDB uses **sharding**, which distributes data across multiple machines.

```
+----------------+      +----------------+      +----------------+
|  Config Server |      |  Mongos Router |      |   Shard 1      |
|  (Metadata)    |<---->|  (Query Router)|<---->|   (Data)       |
+----------------+      +----------------+      +----------------+
                              ↑
                              | Client
                              | Requests
                              ↓
                         +----------------+      +----------------+
                         |   Shard 2      |      |   Shard 3      |
                         |   (Data)       |      |   (Data)       |
                         +----------------+      +----------------+
```

- **Shards**: Store portions of the data
- **Config servers**: Store metadata about chunk distribution
- **Mongos routers**: Act as query routers for client applications

## MongoDB Query Language

### Basic CRUD Operations

**Create Operations:**
```javascript
// Insert a single document
db.users.insertOne({
  name: "Alice",
  age: 25,
  email: "alice@example.com"
});

// Insert multiple documents
db.users.insertMany([
  {name: "Bob", age: 30},
  {name: "Charlie", age: 35}
]);
```

**Read Operations:**
```javascript
// Find all documents
db.users.find();

// Find with filter
db.users.find({age: {$gt: 25}});

// Projection (select specific fields)
db.users.find({}, {name: 1, email: 1});
```

**Update Operations:**
```javascript
// Update a single document
db.users.updateOne(
  {name: "Alice"},
  {$set: {age: 26}}
);

// Update multiple documents
db.users.updateMany(
  {age: {$lt: 30}},
  {$inc: {age: 1}}
);
```

**Delete Operations:**
```javascript
// Delete a single document
db.users.deleteOne({name: "Alice"});

// Delete multiple documents
db.users.deleteMany({age: {$gt: 40}});
```

### Query Operators

MongoDB provides rich query operators for filtering data:

| Operator Type | Examples | Description |
|---------------|----------|-------------|
| Comparison | `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin` | Compare values |
| Logical | `$and`, `$or`, `$not`, `$nor` | Combine multiple conditions |
| Element | `$exists`, `$type` | Check field existence or type |
| Evaluation | `$regex`, `$expr`, `$jsonSchema` | Evaluate expressions |
| Array | `$all`, `$elemMatch`, `$size` | Work with array fields |

Example using multiple operators:
```javascript
db.users.find({
  $and: [
    {age: {$gt: 25}},
    {age: {$lt: 40}},
    {hobbies: {$in: ["reading", "swimming"]}}
  ]
});
```

## Aggregation Framework

The aggregation framework processes data records and returns computed results. It's similar to the SQL GROUP BY clause but much more powerful.

### Aggregation Pipeline Stages

The aggregation pipeline consists of stages that process documents:

```
Collection → $match → $group → $sort → $project → Output
```

Common stages include:
- `$match`: Filters documents (like WHERE in SQL)
- `$group`: Groups documents by specified identifier
- `$sort`: Sorts documents
- `$project`: Reshapes documents (like SELECT in SQL)
- `$unwind`: Deconstructs an array field
- `$lookup`: Performs a left outer join

### Aggregation Example

```javascript
db.orders.aggregate([
  // Stage 1: Filter documents
  {
    $match: {
      status: "completed",
      orderDate: {$gte: ISODate("2023-01-01")}
    }
  },
  
  // Stage 2: Group by customer and calculate totals
  {
    $group: {
      _id: "$customerId",
      totalAmount: {$sum: "$amount"},
      averageAmount: {$avg: "$amount"},
      orderCount: {$sum: 1}
    }
  },
  
  // Stage 3: Sort by total amount descending
  {
    $sort: {totalAmount: -1}
  },
  
  // Stage 4: Project specific fields
  {
    $project: {
      customerId: "$_id",
      totalAmount: 1,
      averageAmount: 1,
      orderCount: 1,
      _id: 0
    }
  }
]);
```

## Indexing in MongoDB

Indexes support efficient query execution. Without indexes, MongoDB must perform a collection scan.

### Index Types

| Index Type | Description | Use Case |
|------------|-------------|----------|
| Single Field | Index on a single field | Simple queries on specific fields |
| Compound | Index on multiple fields | Queries that filter on multiple fields |
| Multikey | Index on array fields | Queries that search within arrays |
| Text | Supports text search | Full-text search operations |
| Geospatial | Supports geographic queries | Location-based queries |
| Hashed | Uses hashed values | Sharding and equality matches |

### Creating Indexes

```javascript
// Create a single field index
db.users.createIndex({email: 1}); // 1 for ascending, -1 for descending

// Create a compound index
db.users.createIndex({lastName: 1, firstName: 1});

// Create a text index
db.articles.createIndex({content: "text"});

// Create a unique index
db.users.createIndex({username: 1}, {unique: true});
```

## MongoDB vs. Relational Databases

| Aspect | MongoDB (Document Store) | Relational Databases |
|--------|--------------------------|---------------------|
| Data Model | Document-oriented | Table-oriented |
| Schema | Dynamic schema | Fixed schema |
| Relationships | Embedded documents or references | Foreign keys and joins |
| Scalability | Horizontal scaling (sharding) | Vertical scaling |
| Query Language | MongoDB Query Language | SQL |
| Transactions | Supported (multi-document) | Fully supported |
| Joins | Limited ($lookup) | Extensive support |

## Integration with Big Data Ecosystem

MongoDB integrates well with various big data tools:

- **Spark**: MongoDB Connector for Spark allows reading from and writing to MongoDB
- **Hadoop**: MongoDB Hadoop Connector enables MapReduce jobs with MongoDB
- **Kafka**: Change streams can be used to capture data changes and stream to Kafka

## Exam Tips

1. **Understand BSON**: Remember that MongoDB uses BSON, not JSON, for storage
2. **Know the difference**: Be clear on how document databases differ from relational databases
3. **Aggregation pipeline**: Practice writing aggregation queries with multiple stages
4. **Indexing strategies**: Understand when to use different types of indexes
5. **Sharding and replication**: Know the components and purposes of sharding and replica sets
6. **Use cases**: Be prepared to discuss when MongoDB is appropriate vs. when it's not