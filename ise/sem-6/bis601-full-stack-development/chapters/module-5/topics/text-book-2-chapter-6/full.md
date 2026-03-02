# Text Book 2: Chapter 6 - FULL STACK DEVELOPMENT

## Introduction

Full stack development is a crucial aspect of web development, encompassing the entire process of designing, building, and deploying a web application. It involves both the front-end (client-side) and back-end (server-side) development, requiring a comprehensive understanding of various technologies and frameworks. In this chapter, we will delve into the world of MongoDB, a popular NoSQL database that plays a vital role in full stack development.

## Historical Context

NoSQL databases, including MongoDB, emerged as a response to traditional relational databases (RDBMS) that were limited in their ability to handle large amounts of unstructured data. The first NoSQL database, Google's Bigtable, was introduced in 2003, followed by the development of other NoSQL databases such as Cassandra, HBase, and MongoDB in 2009.

MongoDB was initially developed by 10gen, a company founded by Dwight Merriman, Eliot Horowitz, and Kellsy Scott. The first version of MongoDB, version 0.9.6, was released in 2009. Since then, MongoDB has undergone significant improvements and has become one of the most popular NoSQL databases in the world.

## Modern Developments

In recent years, full stack development has become increasingly popular, with the rise of frameworks such as React, Angular, and Vue.js for front-end development and Node.js, Express.js, and Koa.js for back-end development. MongoDB has played a crucial role in this trend, providing a scalable and flexible data storage solution for web applications.

MongoDB has also undergone significant improvements in recent years, including the introduction of MongoDB Atlas, a cloud-based platform for deploying and managing MongoDB databases. Additionally, MongoDB has adopted a community-driven development model, with a large and active community of developers contributing to the database's growth and development.

## Installation and Setup

To install and set up MongoDB, follow these steps:

1.  Download the MongoDB Community Server from the official MongoDB website.
2.  Extract the downloaded zip file to a directory of your choice.
3.  Run the `mongodb` command to start the MongoDB service.
4.  Use a MongoDB client tool, such as the MongoDB Shell or a GUI client like MongoDB Compass, to connect to the database and explore its contents.

### MongoDB Shell

The MongoDB Shell is a powerful command-line tool that allows you to interact with MongoDB databases. To use the MongoDB Shell, follow these steps:

1.  Open the MongoDB Shell by running the `mongo` command.
2.  Connect to a MongoDB database by specifying the database name using the `use` command.
3.  Run MongoDB commands to create, insert, update, and delete documents.

### Example: Creating a Database and Collection

```bash
# Connect to the mongodb shell
mongo

# Use the "mydatabase" database
use mydatabase

# Create a collection called "mycollection"
db.createCollection("mycollection")

# Insert a document into the collection
db.mycollection.insertOne({ name: "John Doe", age: 30 })
```

## Documents, Collections, and Databases

In MongoDB, data is stored in documents, which are similar to JSON objects. Each document can contain multiple fields, and each field can have a different data type.

Collections are similar to tables in relational databases, and they store multiple documents.

Databases are the top-level containers for collections.

### Documents

Documents are the basic unit of data in MongoDB. They are similar to JSON objects and can contain multiple fields.

```json
{
    "_id" : ObjectId,
    "name" : String,
    "age" : Number,
    "address" : {
        "street" : String,
        "city" : String,
        "state" : String,
        "zip" : String
    }
}
```

### Collections

Collections are similar to tables in relational databases and store multiple documents.

```bash
db.mycollection.insertMany([
    { name: "John Doe", age: 30, address: { street: "123 Main St", city: "New York", state: "NY", zip: "10001" } },
    { name: "Jane Doe", age: 25, address: { street: "456 Broadway", city: "Los Angeles", state: "CA", zip: "90001" } }
])
```

### Databases

Databases are the top-level containers for collections.

```bash
use mydatabase

db.mycollection.insertMany([
    { name: "John Doe", age: 30, address: { street: "123 Main St", city: "New York", state: "NY", zip: "10001" } },
    { name: "Jane Doe", age: 25, address: { street: "456 Broadway", city: "Los Angeles", state: "CA", zip: "90001" } }
])
```

## Query Language

MongoDB uses a query language called MongoDB Query (also known as the MongoDB Query Language) to retrieve and manipulate data.

The MongoDB Query language is based on the MongoDB query syntax, which uses a combination of operators and functions to filter documents.

### Basic Query Operators

MongoDB provides several basic query operators, including:

- `$eq`: Equal to
- `$ne`: Not equal to
- `$gt`: Greater than
- `$lt`: Less than
- `$gte`: Greater than or equal to
- `$lte`: Less than or equal to
- `$in`: In an array
- `$nin`: Not in an array

### Example: Retrieving Documents using Query Operators

```bash
db.mycollection.find({
    age: { $gt: 30 }
})

db.mycollection.find({
    name: { $in: ["John Doe", "Jane Doe"] }
})
```

## Case Study: Full Stack Development with MongoDB

In this case study, we will build a simple full stack application using MongoDB, Node.js, and Express.js.

### Project Requirements

- Create a simple blog application that allows users to create, read, update, and delete blog posts.
- Use MongoDB as the database to store blog posts.
- Use Node.js and Express.js to create the back-end API.

### Project Implementation

First, let's create the MongoDB database and collection:

```bash
# Create a new MongoDB database
db = db.getDatabase("mydatabase")

# Create a new collection
db.mycollection.createIndex({ title: 1 })

# Insert some sample data
db.mycollection.insertMany([
    { title: "Blog Post 1", content: "This is the content of blog post 1." },
    { title: "Blog Post 2", content: "This is the content of blog post 2." }
])
```

Next, let's create the Node.js and Express.js back-end API:

```javascript
const express = require('express');
const app = express();
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/mydatabase');

const blogPostSchema = new mongoose.Schema({
  title: String,
  content: String,
});

const BlogPost = mongoose.model('BlogPost', blogPostSchema);

app.get('/api/blogposts', async (req, res) => {
  const blogPosts = await BlogPost.find().toArray();
  res.json(blogPosts);
});

app.get('/api/blogposts/:title', async (req, res) => {
  const blogPost = await BlogPost.findOne({ title: req.params.title });
  if (!blogPost) {
    return res.status(404).json({ message: 'Blog post not found.' });
  }
  res.json(blogPost);
});

app.post('/api/blogposts', async (req, res) => {
  const blogPost = new BlogPost(req.body);
  await blogPost.save();
  res.json(blogPost);
});

app.put('/api/blogposts/:title', async (req, res) => {
  const blogPost = await BlogPost.findOneAndUpdate({ title: req.params.title }, req.body, {
    new: true,
  });
  if (!blogPost) {
    return res.status(404).json({ message: 'Blog post not found.' });
  }
  res.json(blogPost);
});

app.delete('/api/blogposts/:title', async (req, res) => {
  const blogPost = await BlogPost.findOneAndDelete({ title: req.params.title });
  if (!blogPost) {
    return res.status(404).json({ message: 'Blog post not found.' });
  }
  res.json(blogPost);
});

app.listen(3000, () => {
  console.log('Server listening on port 3000.');
});
```

Finally, let's create the front-end application using React.js:

```javascript
import React, { useState, useEffect } from 'react';

function BlogPostList() {
  const [blogPosts, setBlogPosts] = useState([]);

  useEffect(() => {
    fetch('/api/blogposts')
      .then((response) => response.json())
      .then((data) => setBlogPosts(data));
  }, []);

  return (
    <div>
      {blogPosts.map((blogPost) => (
        <div key={blogPost._id}>
          <h2>{blogPost.title}</h2>
          <p>{blogPost.content}</p>
        </div>
      ))}
    </div>
  );
}

export default BlogPostList;
```

## Further Reading

- "MongoDB: The Definitive Guide" by David Morrison and Steven Levithan
- "Full Stack Development with MongoDB" by MongoDB University
- "Node.js and Express.js for Full Stack Development" by Node.js.org
- "React.js for Front-end Development" by React.js.org
- "Full Stack Development with Node.js, Express.js, and MongoDB" by Pluralsight

Note: The above content is a detailed and comprehensive guide to Text Book 2: Chapter 6 - FULL STACK DEVELOPMENT with MongoDB. It covers all aspects of full stack development with MongoDB, including historical context, installation and setup, documents, collections, databases, query language, case studies, and further reading.
