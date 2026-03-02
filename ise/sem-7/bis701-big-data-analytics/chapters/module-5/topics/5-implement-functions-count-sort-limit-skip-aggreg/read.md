# **5 Implement Functions: Count – Sort – Limit – Skip – Aggregate using MongoDB 6**

## **Introduction**

In this study material, we will explore five essential functions in MongoDB: Count, Sort, Limit, Skip, and Aggregate. These functions are used to manipulate and analyze data in a MongoDB database. We will also write Pig Latin scripts to sort data using these functions.

## **Count Function**

The Count function is used to count the number of documents in a collection.

- Definition: `db.collection.count()`
- Syntax: `db.collection.count([filter])`
- Examples:
  - Count all documents in a collection: `db.collection.count()`
  - Count documents with a specific filter: `db.collection.count({field: "value"})`

## **Sort Function**

The Sort function is used to sort documents in a collection based on one or more fields.

- Definition: `db.collection.sort([field1, field2, ...])`
- Syntax: `db.collection.sort({ field1: 1, field2: -1 })`
- Examples:
  - Sort documents in ascending order: `db.collection.sort({ field: 1 })`
  - Sort documents in descending order: `db.collection.sort({ field: -1 })`

## **Limit Function**

The Limit function is used to limit the number of documents returned by a query.

- Definition: `db.collection.find().limit(n)`
- Syntax: `db.collection.find().limit(10)`
- Examples:
  - Return the first 10 documents: `db.collection.find().limit(10)`
  - Return the last 10 documents: `db.collection.find().sort({ field: -1 }).limit(10)`

## **Skip Function**

The Skip function is used to skip a specified number of documents in a result set.

- Definition: `db.collection.find().skip(n)`
- Syntax: `db.collection.find().skip(10)`
- Examples:
  - Skip the first 10 documents: `db.collection.find().skip(10)`
  - Skip the last 10 documents: `db.collection.find().sort({ field: -1 }).skip(10)`

## **Aggregate Function**

The Aggregate function is used to perform complex data processing operations on a collection.

- Definition: `db.collection.aggregate()`
- Syntax: `db.collection.aggregate([pipeline])`
- Examples:
  - Group documents by field: `db.collection.aggregate([ { $group: { _id: "$field", count: { $sum: 1 } } } ])`
  - Filter documents by field: `db.collection.aggregate([ { $match: { field: "value" } } ])`

## **Pig Latin Scripts to Sort**

Pig Latin is a programming language that can be used to sort data. Here are some Pig Latin scripts to sort data using the Count, Sort, Limit, Skip, and Aggregate functions:

- Count: `COUNT [field]`
- Sort: `SORT [field1, field2, ...]`
- Limit: `LIMIT [n]`
- Skip: `SKIP [n]`
- Aggregate: `AGGREGATE [pipeline]`

Here's an example Pig Latin script that sorts documents by a specific field:

```pig
SORT [field]
```

This script sorts documents in ascending order by the specified field.

```pig
LIMIT [n]
```

This script limits the number of documents returned to the specified value.

```pig
SKIP [n]
```

This script skips the specified number of documents in the result set.

```pig
AGGREGATE [pipeline]
```

This script performs complex data processing operations using the pipeline.

Note: The above Pig Latin scripts assume that the data is stored in a MongoDB collection named "collection". Replace "collection" with the actual name of your collection.

## **Conclusion**

In this study material, we explored five essential functions in MongoDB: Count, Sort, Limit, Skip, and Aggregate. We also wrote Pig Latin scripts to sort data using these functions. These functions are useful for manipulating and analyzing data in a MongoDB database.
