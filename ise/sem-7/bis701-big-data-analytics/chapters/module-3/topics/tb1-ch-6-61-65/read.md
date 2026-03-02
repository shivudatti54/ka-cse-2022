# **TB1: Ch 6: 6.1-6.5**

## **6.1: What is MongoDB?**

### Definition

MongoDB is a NoSQL, document-based database that stores data in JSON-like documents called BSON (Binary Serialized Object Notation). It is designed to scale horizontally, making it suitable for large-scale applications.

### Features

- Schema-less: No fixed schema is required, allowing for flexibility in data modeling.
- Scalability: Horizontal scaling makes it easy to add more nodes to the cluster as the data grows.
- High performance: Optimized for high-throughput and low-latency queries.
- Large data capacity: Can store large amounts of data, including multimedia files.

### Example

Suppose we have a web application that stores user information, including name, email, and address. In a relational database, we would need to create separate tables for each field. In MongoDB, we can store this data in a single document like this:

```json
{
  "_id" : ObjectId,
  "name" : "John Doe",
  "email" : "john.doe@example.com",
  "address" : {
    "street" : "123 Main St",
    "city" : "Anytown",
    "state" : "CA,
    "zip" : "12345"
  }
}
```

### Key Concepts

- **Document-based database**: Stores data in self-contained documents.
- **NoSQL**: A database that does not use the traditional structured query language (SQL).
- **Schema-less**: No fixed schema is required.

## **6.2: Why MongoDB?**

### Advantages

- **Scalability**: MongoDB can handle large amounts of data and scale horizontally.
- **Flexibility**: No fixed schema allows for flexibility in data modeling.
- **High performance**: Optimized for high-throughput and low-latency queries.
- **Easy integration**: Can be easily integrated with other technologies, such as Python and JavaScript.

### Disadvantages

- **Complexity**: MongoDB requires a different mindset and skillset than traditional relational databases.
- **Data consistency**: MongoDB does not guarantee data consistency, which can be a concern for certain applications.

### Example

Suppose we have a web application that needs to handle large amounts of log data. In a relational database, we would need to create a separate table for each log event. In MongoDB, we can store the log data in a single document like this:

```json
[
  {
    "_id" : ObjectId,
    "timestamp" : ISODate("2022-01-01T00:00:00.000Z"),
    "level" : "INFO",
    "message" : "User logged in"
  },
  {
    "_id" : ObjectId,
    "timestamp" : ISODate("2022-01-01T00:01:00.000Z"),
    "level" : "ERROR",
    "message" : "Database connection failed"
  }
]
```

### Key Concepts

- **Scalability**: Ability to handle large amounts of data and scale horizontally.
- **Flexibility**: No fixed schema allows for flexibility in data modeling.

## **6.3: Terms used in RDBMS and MongoDB**

### RDBMS Terms

- **Schema**: A set of rules that defines the structure of the data.
- **Table**: A collection of related data.
- **Row**: A single entry in a table.
- **Column**: A single field in a table.
- **Primary key**: A unique identifier for each row.

### MongoDB Terms

- **Collection**: A group of related documents.
- **Document**: A self-contained piece of data.
- **Field**: A single piece of data within a document.
- **ObjectId**: A unique identifier for each document.

### Comparison

| RDBMS Term  | MongoDB Term    |
| ----------- | --------------- |
| Schema      | No fixed schema |
| Table       | Collection      |
| Row         | Document        |
| Column      | Field           |
| Primary key | ObjectId        |

### Key Concepts

- **Schema**: A set of rules that defines the structure of the data.
- **Collection**: A group of related documents.

## **6.4: MongoDB Data Types**

### Built-in Data Types

- **String**: A sequence of characters.
- **Int32**: A 32-bit integer.
- **Int64**: A 64-bit integer.
- **Double**: A floating-point number.
- **Boolean**: A true or false value.

### Custom Data Types

- **ObjectId**: A unique identifier for each document.
- **Date**: A date value.
- **Array**: A collection of values.

### Example

Suppose we have a document that stores a user's information, including name, email, and address. We can use the following data types:

```json
{
  "_id" : ObjectId,
  "name" : String,
  "email" : String,
  "address" : {
    "street" : String,
    "city" : String,
    "state" : String,
    "zip" : Int32
  },
  "createdAt" : Date,
  "updatedAt" : Date
}
```

### Key Concepts

- **Built-in data types**: String, Int32, Int64, Double, Boolean.
- **Custom data types**: ObjectId, Date, Array.

## **6.5: MongoDB Querying**

### Querying Basics

- **Filtering**: Selecting specific documents based on conditions.
- **Sorting**: Ordering documents in a specific order.
- **Limting**: Limiting the number of documents returned.

### Query Operators

- **Equals**: `$eq`
- **Not equals**: `$ne`
- **In**: `$in`
- **Not in**: `$nin`
- **Greater than**: `$gt`
- **Less than**: `$lt`
- **Greater than or equal to**: `$gte`
- **Less than or equal to**: `$lte`

### Example

Suppose we have a collection of users and we want to find all users with an email address containing "john". We can use the following query:

```json
db.users.find({ email: { $regex: "john" } })
```

### Key Concepts

- **Filtering**: Selecting specific documents based on conditions.
- **Sorting**: Ordering documents in a specific order.
- **Limting**: Limiting the number of documents returned.
