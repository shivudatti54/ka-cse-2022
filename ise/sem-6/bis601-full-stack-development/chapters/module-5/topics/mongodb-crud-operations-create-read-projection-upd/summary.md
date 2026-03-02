# **MongoDB CRUD Operations Revision Notes**

### Overview

- MongoDB is a NoSQL database that uses JSON-like documents
- CRUD operations are the fundamental operations in MongoDB

### Create (Insert)

- Use the `insertOne` or `insertMany` methods to add documents to a collection
- Example: `db.collection.insertOne({ name: 'John', age: 30 })`
- Use the `insertMany` method to add multiple documents at once

### Read

- Use the `find` method to retrieve documents from a collection
- Example: `db.collection.find()`
- Use the `findOne` method to retrieve a single document
- Use the `$match` operator to filter documents
- Use the `$project` operator to transform documents

### Projection

- Use the `$project` operator to select specific fields from documents
- Example: `db.collection.find().project({ name: 1, age: 1 })`

### Update

- Use the `updateOne` or `updateMany` methods to update documents in a collection
- Example: `db.collection.updateOne({ name: 'John' }, { $set: { age: 31 } })`
- Use the `$set` operator to update fields
- Use the `$inc` operator to increment fields

### Delete

- Use the `deleteOne` or `deleteMany` methods to delete documents from a collection
- Example: `db.collection.deleteOne({ name: 'John' })`
- Use the `$deleteMany` operator to delete multiple documents

### Aggregate

- Use the `aggregate` method to perform complex queries on data
- Example: `db.collection.aggregate([...])`

### MongoDB Node.js Driver

- Use the `mongodb` package to interact with MongoDB from Node.js
- Example: `const MongoClient = require('mongodb').MongoClient;`

### Schema Initialization

- Use the `createCollection` method to create a new collection
- Example: `db.createCollection('myCollection', { validator: validateMySchema })`

### Reading from MongoDB

- Use the `findOne`, `find`, and `aggregate` methods to retrieve data from MongoDB
- Example: `db.collection.findOne({ name: 'John' })`

### Important Formulas, Definitions, and Theorems

- **Document**: A single unit of data in a MongoDB database
- **Collection**: A group of documents in a MongoDB database
- **Database**: A container for collections in a MongoDB database
- **Query Language**: A language used to query and manipulate data in MongoDB
- **Validator**: A function used to validate data before inserting or updating it in MongoDB
- **Aggregate**: A pipeline of operations used to process data in MongoDB

### Important Concepts

- **MongoDB CRUD Operations**: The fundamental operations in MongoDB (Create, Read, Update, Delete)
- **MongoDB Query Language**: A language used to query and manipulate data in MongoDB
- **MongoDB Aggregation**: A pipeline of operations used to process data in MongoDB
