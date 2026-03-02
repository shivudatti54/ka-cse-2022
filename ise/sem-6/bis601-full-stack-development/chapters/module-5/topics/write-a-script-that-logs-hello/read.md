# **Write a Script that Logs "Hello"**

## **Introduction**

In this section, we will learn how to write a script that logs "Hello" using MongoDB. This is an essential skill for any MongoDB developer, and we will cover the basics of how to interact with MongoDB using the shell and programming languages.

## **What is MongoDB?**

MongoDB is a NoSQL database that allows for flexible and efficient data storage. It is particularly useful for handling large amounts of semi-structured data. MongoDB is designed to be scalable, flexible, and easy to use.

## **The MongoDB Shell**

The MongoDB shell is a command-line interface that allows you to interact with your MongoDB database. It is the most common way to use MongoDB, and is used by most developers.

## **Logging "Hello"**

To write a script that logs "Hello", we will use the MongoDB shell. Here is an example of how to do this:

```bash
use hello
db.createCollection("logs")
db.logs.insertOne({"message": "Hello"})
```

In this example, we first use the `use` command to select the database we want to use. We then use the `createCollection` command to create a new collection called "logs". Finally, we use the `insertOne` command to insert a new document into the "logs" collection with the message "Hello".

## **Using a Programming Language**

If you want to write a script that logs "Hello" using a programming language, you can use the MongoDB Node.js driver. Here is an example of how to do this in Node.js:

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';

MongoClient.connect(url, function (err, client) {
  if (err) {
    console.log(err);
  } else {
    console.log('Connected to MongoDB');
    const db = client.db();
    const collection = db.collection('logs');
    collection.insertOne({ message: 'Hello' }, function (err, result) {
      if (err) {
        console.log(err);
      } else {
        console.log('Document inserted successfully');
      }
    });
  }
});
```

## **Key Concepts**

- **Database**: A database is a container for multiple collections.
- **Collection**: A collection is a group of related documents.
- **Document**: A document is a single entry in a collection.
- **InsertOne**: The `insertOne` command is used to insert a single document into a collection.
- **Use**: The `use` command is used to select a database.

## **Exercises**

1.  Create a new database and collection using the MongoDB shell.
2.  Insert a new document into the collection using the `insertOne` command.
3.  Use a programming language to connect to the MongoDB database and insert a new document.

## **Conclusion**

In this section, we learned how to write a script that logs "Hello" using MongoDB. We covered the basics of how to interact with MongoDB using the shell and programming languages. We also covered key concepts such as databases, collections, and documents. With this knowledge, you can now write your own scripts that interact with MongoDB.

## **Key Takeaways**

- MongoDB is a NoSQL database that allows for flexible and efficient data storage.
- The MongoDB shell is a command-line interface that allows you to interact with your MongoDB database.
- To log "Hello", you can use the `insertOne` command in the MongoDB shell.
- You can also use a programming language such as Node.js to connect to the MongoDB database and insert a new document.

## **Additional Resources**

- MongoDB documentation: [https://docs.mongodb.com/](https://docs.mongodb.com/)
- MongoDB tutorial: [https://docs.mongodb.com/tutorial/getting-started/](https://docs.mongodb.com/tutorial/getting-started/)
- MongoDB shell reference: [https://docs.mongodb.com/manual/shell/](https://docs.mongodb.com/manual/shell/)
