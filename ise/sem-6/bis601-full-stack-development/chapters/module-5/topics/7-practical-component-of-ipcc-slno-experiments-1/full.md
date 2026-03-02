# **7 Practical Components of IPCC Sl.No Experiments 1: Full Stack Development with MongoDB**

## **Introduction**

The Intergovernmental Panel on Climate Change (IPCC) has made significant contributions to our understanding of climate change and its impacts. In the context of full stack development with MongoDB, this topic refers to the practical components of building a robust and scalable database-driven application. In this comprehensive guide, we will delve into the 7 practical components of IPCC Sl.No Experiments 1, exploring the basics of MongoDB, documents, collections, databases, query language, installation, and the mongo shell.

## **Component 1: MongoDB Basics**

MongoDB is a NoSQL database that stores data in a flexible and scalable manner. It is a document-based database, meaning that it stores data in the form of JSON-like documents.

### Key Features of MongoDB

- **Schema-less**: MongoDB does not require a predefined schema for data storage, making it ideal for dynamic and flexible data models.
- **Document-oriented**: MongoDB stores data in the form of documents, which can contain nested fields and arrays.
- **Scalability**: MongoDB is designed to scale horizontally, making it suitable for large and complex applications.

### Example: Creating a Simple Document in MongoDB

```bash
// Create a new database
use climate_change

// Create a new collection
db.createCollection("locations")

// Insert a new document into the collection
db.locations.insertOne({
    "city": "New York",
    "country": "USA",
    "population": 8405837
})
```

## **Component 2: Documents**

In MongoDB, a document represents a single record or entry in a collection. Documents are JSON-like objects that can contain fields, subfields, and arrays.

### Document Structure

A document in MongoDB has the following structure:

```json
{
    "_id": <ObjectId>,
    "field1": <value>,
    "field2": <value>,
    ...
}
```

### Example: Creating a Complex Document in MongoDB

```bash
// Create a new collection
db.createCollection("users")

// Insert a new document into the collection
db.users.insertOne({
    "_id": ObjectId(),
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "123-456-7890"
        },
        {
            "type": "mobile",
            "number": "098-765-4321"
        }
    ]
})
```

## **Component 3: Collections**

A collection in MongoDB is a group of documents that share the same data structure. Collections are the core storage units for MongoDB.

### Creating a Collection

To create a new collection in MongoDB, you can use the `createCollection()` method.

```bash
db.createCollection("locations")
```

### Example: Inserting Documents into a Collection

```bash
// Insert multiple documents into the collection
db.locations.insertMany([
    {
        "city": "New York",
        "country": "USA",
        "population": 8405837
    },
    {
        "city": "Los Angeles",
        "country": "USA",
        "population": 3990456
    }
])
```

## **Component 4: Databases**

In MongoDB, a database is a container for one or more collections. Databases are the top-level storage units for MongoDB.

### Creating a Database

To create a new database in MongoDB, you can use the `use()` method.

```bash
use climate_change
```

### Example: Creating a Collection in a Specific Database

```bash
// Create a new collection in the climate_change database
db.createCollection("locations")
```

## **Component 5: Query Language**

The query language in MongoDB is used to retrieve and manipulate data in a collection. MongoDB provides several query operators and methods to filter, sort, and aggregate data.

### Query Operators

MongoDB provides several query operators to filter data, including:

- `$eq`: Equal to
- `$ne`: Not equal to
- `$gt`: Greater than
- `$lt`: Less than
- `$gte`: Greater than or equal to
- `$lte`: Less than or equal to

### Example: Using Query Operators to Filter Data

```bash
// Find all documents where the population is greater than 1 million
db.locations.find({ population: { $gt: 1000000 } })
```

## **Component 6: Installation**

To install MongoDB, you can download the community server version from the official MongoDB website.

### Installing MongoDB Community Server

1.  Download the MongoDB Community Server version that matches your operating system and architecture.
2.  Extract the downloaded archive to a directory of your choice.
3.  Start the MongoDB server by running the following command:

```bash
bin/mongod --configsvr --port 27017 --bind_ip <your_ip_address>
```

## **Component 7: The Mongo Shell**

The mongo shell is a command-line interface for interacting with MongoDB. It allows you to execute queries, insert documents, and manage collections and databases.

### Starting the Mongo Shell

To start the mongo shell, you can use the following command:

```bash
bin/mongo
```

### Example: Using the Mongo Shell to Execute a Query

```bash
// Connect to the local database
use climate_change

// Find all documents where the population is greater than 1 million
db.locations.find({ population: { $gt: 1000000 } })
```

## **Further Reading**

- MongoDB Documentation: <https://docs.mongodb.com/>
- MongoDB Community: <https://community.mongodb.com/>
- MongoDB University: <https://university.mongodb.com/>

By following this comprehensive guide, you have gained a deep understanding of the 7 practical components of IPCC Sl.No Experiments 1, including MongoDB basics, documents, collections, databases, query language, installation, and the mongo shell. With this knowledge, you are equipped to build robust and scalable database-driven applications using MongoDB.
