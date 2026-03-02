# **7 Practical Components of IPCC Sl.No Experiments 1: Full Stack Development with MongoDB**

## **Introduction**

In this study material, we will cover the 7 practical components of IPCC Sl.No Experiments 1, focusing on Full Stack Development with MongoDB. MongoDB is a popular NoSQL database that provides a flexible and scalable data storage solution for modern applications.

## **Component 1: Installation**

### Overview

To start using MongoDB, you need to install it on your local machine or in a cloud environment. Here are the steps to install MongoDB:

- Download the MongoDB Community Server from the official MongoDB website.
- Extract the downloaded zip file to a directory of your choice (e.g., `C:\Program Files\MongoDB` on Windows or `/usr/local/mongodb` on Linux).
- Create a new data directory for MongoDB by running the command ` mongod --dbpath /path/to/data`.
- Start the MongoDB service by running the command `mongod`.

### Example:

```bash
# Download the MongoDB Community Server
wget https://www.mongodb.org/downloads/soft32/microsoft/mongodb-server-64bit-4.4.3.tgz

# Extract the downloaded zip file
tar -xvf mongodb-server-64bit-4.4.3.tgz

# Create a new data directory
mongod --dbpath /path/to/data

# Start the MongoDB service
mongod
```

## **Component 2: The Mongo Shell**

### Overview

The Mongo Shell is a command-line interface for interacting with MongoDB. It allows you to execute MongoDB commands, view database information, and perform data operations.

### Key Features:

- **Connect to a MongoDB instance**: Use the `use` command to connect to a MongoDB instance.
- **Create a new database**: Use the `use` command to create a new database.
- **Insert data**: Use the `db.collection.insert()` method to insert data into a collection.

### Example:

```javascript
// Connect to a MongoDB instance
use mydatabase;

// Create a new collection
db.createCollection("mycollection");

// Insert data into the collection
db.mycollection.insert({ name: "John", age: 30 });
```

## **Component 3: Documents**

### Overview

In MongoDB, a document represents a single record in a collection. Documents are stored in JSON-like format and can contain arrays, objects, and binary data.

### Key Features:

- **Document structure**: Documents can have multiple fields, each with a specific data type (e.g., string, integer, date).
- **Embedded documents**: Documents can contain embedded documents, which are documents stored within a single document.
- **Arrays**: Documents can contain arrays of values.

### Example:

```json
{
  "_id" : ObjectId(),
  "name" : "John",
  "age" : 30,
  "address" : {
    "street" : "123 Main St",
    "city" : "Anytown",
    "state" : "CA",
    "zip" : "12345"
  },
  "hobbies" : ["reading", "writing", "coding"]
}
```

## **Component 4: Collections**

### Overview

In MongoDB, a collection is a single table-like collection of documents. Collections are stored in a separate file and can be created using the `createCollection` method.

### Key Features:

- **Collection structure**: Collections can have multiple fields, each with a specific data type.
- **Collection size**: Collections can store a large number of documents.
- **Collection indexing**: Collections can have indexes to improve query performance.

### Example:

```javascript
// Create a new collection
db.createCollection('mycollection');

// Insert data into the collection
db.mycollection.insert({ name: 'John', age: 30 });
```

## **Component 5: Databases**

### Overview

In MongoDB, a database is a logical container for collections. Databases are stored in a separate file and can be created using the `use` command.

### Key Features:

- **Database structure**: Databases can have multiple collections.
- **Database size**: Databases can store a large number of collections.
- **Database security**: Databases can have access controls to restrict access to certain collections.

### Example:

```javascript
// Connect to a MongoDB instance
use mydatabase;

// Create a new collection
db.createCollection("mycollection");
```

## **Component 6: Query Language**

### Overview

The Query Language is used to retrieve data from MongoDB. It allows you to specify the conditions for which documents to return.

### Key Features:

- **Find method**: The `find` method is used to retrieve documents based on a filter.
- **Filter syntax**: Filters can be used to specify conditions for which documents to return.
- **Aggregate framework**: The aggregate framework allows you to perform complex data processing operations.

### Example:

```javascript
// Find documents based on a filter
db.mycollection.find({ name: 'John' });

// Use the aggregate framework to process data
db.mycollection.aggregate([{ $match: { age: { $gt: 30 } } }, { $sort: { age: -1 } }]);
```

## **Component 7: Full Stack Development**

### Overview

Full stack development with MongoDB involves using the entire stack to build a web application. This includes using MongoDB as the database, a programming language like Node.js, and a web framework like Express.js.

### Key Features:

- **Client-side**: The client-side application is built using a programming language like JavaScript and a web framework like React.
- **Server-side**: The server-side application is built using a programming language like Node.js and a web framework like Express.js.
- **Communication**: The client-side and server-side applications communicate with each other using RESTful APIs.

### Example:

```javascript
// Client-side application (React)
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState('');
  const [age, setAge] = useState(0);

  useEffect(() => {
    axios
      .post('/api/data', { name, age })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [name, age]);

  return (
    <div>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="number" value={age} onChange={(e) => setAge(e.target.value)} />
      <button type="button">Submit</button>
    </div>
  );
}

export default App;

// Server-side application (Express.js)
const express = require('express');
const app = express();
const mongoose = require('mongoose');

app.post('/api/data', (req, res) => {
  const { name, age } = req.body;
  const data = { name, age };
  res.json(data);
});
```

In conclusion, the 7 practical components of IPCC Sl.No Experiments 1 cover the basics of Full Stack Development with MongoDB. By understanding these components, you can build modern web applications that can handle large amounts of data and provide a scalable and secure infrastructure for your application.
