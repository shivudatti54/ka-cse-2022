# 5 Implement Functions: Count – Sort – Limit – Skip – Aggregate using MongoDB

### BIG DATA ANALYTICS

#### Introduction

- MongoDB is a NoSQL database that allows for flexible schema design and high scalability.
- This topic covers five essential functions in MongoDB:
  - Count
  - Sort
  - Limit
  - Skip
  - Aggregate

#### Key Points

- **Count**
  - Counts the number of documents in a collection.
  - Formula: `db.collection.count()`
  - Theorem: The count function returns the total number of documents in the collection.
- **Sort**
  - Sorts documents in a collection in ascending or descending order.
  - Formula: `db.collection.find().sort({field: 1})`
  - Definition: Sorting is the process of rearranging documents in a specific order based on one or more fields.

- **Limit**
  - Returns a specified number of documents from a collection.
  - Formula: `db.collection.find().limit(num)`
  - Definition: Limiting is the process of selecting a subset of documents from a collection based on a specific number.

- **Skip**
  - Skips a specified number of documents from the beginning of a collection.
  - Formula: `db.collection.find().skip(num)`
  - Definition: Skipping is the process of omitting a specified number of documents from the beginning of a collection.

- **Aggregate**
  - Performs complex data processing operations on a collection.
  - Formula: `db.collection.aggregate(pipeline)`
  - Definition: Aggregation is the process of combining and analyzing data from a collection using a pipeline of operations.

#### Pig Latin Scripts to Sort

- The Pig Latin function for sorting is built-in in Pig Latin.
- Formula: `sort(input)`

#### Key Terms

- **Pipeline**: A sequence of operations in MongoDB that are applied to a collection to produce a final result.
- **Field**: A single piece of data within a document.
- **Document**: A single piece of data within a collection.
- **Collection**: A group of related documents in MongoDB.
