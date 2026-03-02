# **Create an Array of 5 Cities and Perform Operations in MongoDB**

## **Introduction**

In this tutorial, we will explore how to create an array of 5 cities in MongoDB and perform various operations on it. We will start with the basics of arrays in MongoDB, followed by creating and manipulating arrays, and finally, performing complex operations.

## **Historical Context**

The concept of arrays in MongoDB dates back to the early days of MongoDB, where it was introduced as a way to store multiple values associated with a single document. Since then, arrays have become an essential data structure in MongoDB, allowing developers to store and manipulate complex data.

## **Requirements**

To complete this tutorial, you will need:

- MongoDB installed on your local machine
- A basic understanding of MongoDB and its data structures
- A text editor or IDE of your choice

## **Step 1: Creating an Array of 5 Cities**

To create an array of 5 cities in MongoDB, we can use the following MongoDB shell command:

```bash
db.cities.insertMany([
  { name: "New York", population: 8405837 },
  { name: "Los Angeles", population: 3990456 },
  { name: "Chicago", population: 2695594 },
  { name: "Houston", population: 2320268 },
  { name: "Phoenix", population: 1721000 }
])
```

This command inserts five documents into the `cities` collection, each with a `name` and `population` field.

## **Step 2: Querying the Array**

To query the array, we can use the following MongoDB shell command:

```bash
db.cities.find()
```

This command returns all documents in the `cities` collection, which includes the array of cities.

Alternatively, we can use the `$in` operator to query the array:

```bash
db.cities.find({ name: { $in: ["New York", "Los Angeles"] } })
```

This command returns only the documents with `name` equal to either "New York" or "Los Angeles".

## **Step 3: Modifying the Array**

To modify the array, we can use the following MongoDB shell command:

```bash
db.cities.updateOne({ name: "New York" }, { $set: { population: 8500000 } })
```

This command updates the document with `name` equal to "New York" by setting the `population` field to 8500000.

## **Step 4: Removing Elements from the Array**

To remove elements from the array, we can use the following MongoDB shell command:

```bash
db.cities.deleteOne({ name: "Los Angeles" })
```

This command deletes the document with `name` equal to "Los Angeles".

## **Step 5: Performing Complex Operations**

To perform complex operations on the array, we can use the following MongoDB shell command:

```bash
db.cities.find({ population: { $gt: 3000000 } })
```

This command returns all documents with a population greater than 3000000.

## **Diagram: Array Operations**

Here is a diagram illustrating the array operations:

```markdown
+---------------+
| Cities |
+---------------+
| | |
| | name |
| | | |
| | -- |
| | population |
| | | |
| | -- |
| | ... |
| +---------+ |
| | |
| | array | |
| | | |
| | -- |
| | element |
| | ... |
| +---------+ |
+---------------+
```

## **Case Study: Storing City Data**

City data is a common use case for arrays in MongoDB. For example, let's say we want to store city data for a web application that allows users to search for cities by name or population. We can create an array of city documents with `name` and `population` fields, and then use the `$in` operator to query the array.

**Example Use Case:**

```javascript
const cities = [
  { name: 'New York', population: 8405837 },
  { name: 'Los Angeles', population: 3990456 },
  { name: 'Chicago', population: 2695594 },
  { name: 'Houston', population: 2320268 },
  { name: 'Phoenix', population: 1721000 },
];

const filter = { name: { $in: ['New York', 'Los Angeles'] } };

db.cities.find(filter);
```

This code creates an array of city documents and then uses the `$in` operator to query the array for cities with names equal to "New York" or "Los Angeles".

## **Conclusion**

In this tutorial, we explored how to create an array of 5 cities in MongoDB and perform various operations on it. We covered the basics of arrays in MongoDB, including creating and manipulating arrays, and performing complex operations. We also discussed the historical context of arrays in MongoDB and provided a diagram illustrating the array operations.

## **Further Reading**

- MongoDB documentation: [Arrays](https://docs.mongodb.com/manual/core/arrays/)
- MongoDB documentation: [Querying Arrays](https://docs.mongodb.com/manual/reference/sql-and-nosql-query operators/#array-queries)
- MongoDB documentation: [Array Operators](https://docs.mongodb.com/manual/reference/sql-and-nosql-query operators/#array-operators)
