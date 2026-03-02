# **MongoDB CRUD Operations**

### Introduction

CRUD (Create, Read, Update, Delete) operations are the fundamental operations in a database. MongoDB provides these operations to manage data. In this section, we will learn about CRUD operations in MongoDB.

### Create (Insert) Operation

---

The create operation is used to insert a new document into a collection. The syntax for create operation is as follows:

```javascript
db.collection.insertOne(document);
```

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    const document = {
      name: 'John Doe',
      age: 30,
      city: 'New York',
    };

    collection.insertOne(document, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document inserted:', result.ops[0]);
      }
    });
  }
});
```

### Read Operation

---

The read operation is used to retrieve data from a collection. There are two types of read operations:

- **Find**: It is used to retrieve all documents from a collection.
- **FindOne**: It is used to retrieve one document from a collection.

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Find all documents
    collection.find().toArray(function (err, documents) {
      if (err) {
        console.log(err);
      } else {
        console.log('All documents:', documents);
      }
    });

    // Find one document
    collection.findOne({ name: 'John Doe' }, function (err, document) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document:', document);
      }
    });
  }
});
```

### Update Operation

---

The update operation is used to update a document in a collection. The syntax for update operation is as follows:

```javascript
db.collection.updateOne(filter, update);
```

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Update a document
    collection.updateOne({ name: 'John Doe' }, { $set: { age: 31 } }, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document updated:', result.ops[0]);
      }
    });
  }
});
```

### Delete Operation

---

The delete operation is used to delete a document from a collection. The syntax for delete operation is as follows:

```javascript
db.collection.deleteOne(filter);
```

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Delete a document
    collection.deleteOne({ name: 'John Doe' }, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document deleted:', result.deletedCount);
      }
    });
  }
});
```

### Projection Operation

---

The projection operation is used to specify which fields to include in the result of a query. The syntax for projection operation is as follows:

```javascript
db.collection.find(filter).projection({ fields: 1 });
```

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Find all documents and include only the name field
    collection
      .find()
      .projection({ name: 1 })
      .toArray(function (err, documents) {
        if (err) {
          console.log(err);
        } else {
          console.log('Documents:', documents);
        }
      });
  }
});
```

### Aggregate Operation

---

The aggregate operation is used to perform complex queries on a collection. The syntax for aggregate operation is as follows:

```javascript
db.collection.aggregate([pipeline]);
```

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Aggregate documents to get the top 5 documents with the highest age
    collection
      .aggregate([{ $sort: { age: -1 } }, { $limit: 5 }])
      .toArray(function (err, documents) {
        if (err) {
          console.log(err);
        } else {
          console.log('Top 5 documents:', documents);
        }
      });
  }
});
```

### MongoDB Node.js Driver

---

The MongoDB Node.js driver is a library that provides a convenient way to interact with MongoDB from Node.js applications. The driver supports CRUD operations, aggregation, and other advanced features.

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Create a new document
    const document = {
      name: 'John Doe',
      age: 30,
      city: 'New York',
    };
    collection.insertOne(document, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document inserted:', result.ops[0]);
      }
    });
  }
});
```

### Schema Initialization

---

The schema initialization is a process of defining the structure of the data in a MongoDB collection. The schema defines the fields and data types of the documents in the collection.

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function(err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Initialize the schema
    collection CreateIndex({ name: 1 }, function(err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Index created:', result);
      }
    });
  }
});
```

### Reading from MongoDB

---

Reading from MongoDB involves retrieving data from a collection. The `find()` method is used to retrieve data from a collection.

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Find all documents
    collection.find().toArray(function (err, documents) {
      if (err) {
        console.log(err);
      } else {
        console.log('All documents:', documents);
      }
    });
  }
});
```

### Writing to MongoDB

---

Writing to MongoDB involves inserting data into a collection. The `insertOne()` method is used to insert a single document into a collection.

**Example:**

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const collection = db.collection('myCollection');

    // Create a new document
    const document = {
      name: 'John Doe',
      age: 30,
      city: 'New York',
    };
    collection.insertOne(document, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document inserted:', result.ops[0]);
      }
    });
  }
});
```
