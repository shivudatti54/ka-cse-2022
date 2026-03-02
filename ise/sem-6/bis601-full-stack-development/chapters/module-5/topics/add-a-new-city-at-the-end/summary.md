# Add a New City

## **Overview**

Adding a new city to a MongoDB database involves several steps:

### Key Concepts

- **Documents**: The basic unit of data storage in MongoDB.
- **Collection**: A group of documents stored together.
- **Database**: A container for collections.

### Steps to Add a New City

- **Create a new collection**: If you don't already have a collection for cities, create one.
- **Specify the schema**: Define the structure of the city document using fields such as `name`, `country`, `latitude`, and `longitude`.
- **Insert the document**: Use the `insertOne()` or `insertMany()` method to add the new city document to the collection.

### Example Code

```javascript
// Import the MongoDB driver
const { MongoClient, InsertOne } = require('mongodb').MongoClient;

// Connect to the MongoDB server
const url = 'mongodb://localhost:27017';
const dbName = 'cities';

// Specify the collection
const collectionName = 'cities';

// Create a new city document
const city = {
  name: 'New City',
  country: 'USA',
  latitude: 37.7749,
  longitude: -122.4194,
};

// Insert the document into the collection
async function addCity() {
  try {
    const client = new MongoClient(url);
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection(collectionName);
    const result = await collection.insertOne(city);
    console.log('New city added:', result.ops[0]._id);
  } catch (err) {
    console.error(err);
  } finally {
    client.close();
  }
}

addCity();
```

### Important Formulas and Definitions

- **GridFS**: A mechanism for storing large files in a grid-based structure.
- **MongoDB Query Language**: A language used to query and manipulate data in MongoDB.

### Theorems and Concepts

- **Document-oriented database**: A database that stores data in the form of documents, each representing a single entity.
- **Collection-oriented database**: A database that groups related documents into collections.

### Revision Notes

- **Documents**: The basic unit of data storage in MongoDB.
- **Collection**: A group of documents stored together.
- **Database**: A container for collections.
- **InsertOne() and insertMany() methods**: Used to add new documents to a collection.
- **GridFS**: A mechanism for storing large files in a grid-based structure.
- **MongoDB Query Language**: A language used to query and manipulate data in MongoDB.
