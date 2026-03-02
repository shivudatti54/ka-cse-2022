# Text Book 2: Chapter 6

## MongoDB Basics

### What is MongoDB?

MongoDB is a NoSQL database that stores data in the form of semi-structured documents. It is designed to handle large amounts of data and scale horizontally to accommodate growing data sets.

### Key Features of MongoDB

- **Document-Oriented Database**: MongoDB stores data in the form of JSON-like documents, making it easy to query and manipulate data.
- **Schemaless**: MongoDB does not require a predefined schema, allowing for flexibility in data modeling.
- **Scalable**: MongoDB is designed to scale horizontally, making it suitable for large-scale applications.
- **High Performance**: MongoDB is optimized for high-performance data retrieval and storage.

### Types of MongoDB Collections

- **Document Collection**: A collection of documents, each with its own unique set of fields.
- **Array Collection**: A collection of arrays, where each array element represents a single document.
- **Map Collection**: A collection of key-value pairs, where each key maps to a specific value.

### MongoDB Database

A MongoDB database is a container that holds one or more collections. Databases are used to organize and separate data, making it easier to manage and maintain.

### MongoDB Query Language

MongoDB uses a query language to retrieve data from the database. The query language is based on JSON and allows for complex queries using operators and filters.

#### Query Operators

- `$eq`: Equal to
- `$ne`: Not equal to
- `$gt`: Greater than
- `$lt`: Less than
- `$gte`: Greater than or equal to
- `$lte`: Less than or equal to
- `$in`: Element of an array
- `$nin`: Not an element of an array

#### Query Filters

- `$match`: Filter documents based on conditions
- `$project`: Transform and filter documents
- `$sort`: Sort documents
- `$limit`: Limit the number of documents returned
- `$skip`: Skip a specified number of documents

### Installing MongoDB

MongoDB can be installed on a variety of platforms, including Windows, macOS, and Linux. The installation process typically involves:

1.  Downloading the MongoDB installation package
2.  Running the installer
3.  Configuring the database
4.  Starting the service

### The Mongo Shell

The Mongo Shell is a command-line interface for interacting with the MongoDB database. The shell allows for:

- Creating and managing collections
- Inserting and updating documents
- Querying the database
- Managing database settings

#### Basic Shell Commands

- `use`: Switch to a different database
- `db`: Display the current database
- `show dbs`: List all available databases
- `show collections`: List all collections in the current database

### Best Practices for MongoDB

- **Use Indexes**: Indexes can significantly improve query performance.
- **Use Efficient Data Types**: Choose data types that match the expected data.
- **Limit Data Size**: Large data sizes can impact performance.
- **Monitor Database Performance**: Regularly monitor database performance to identify bottlenecks.
