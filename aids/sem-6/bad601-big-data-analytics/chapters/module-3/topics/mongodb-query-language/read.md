# **MongoDB Query Language**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Query Language Basics](#query-language-basics)
3. [Query Operators](#query-operators)
4. [Aggregation Framework](#aggregation-framework)
5. [Query Examples](#query-examples)

## **Introduction**

MongoDB Query Language is used to retrieve and manipulate data in MongoDB documents. It is a powerful language that allows users to query and update data in a flexible and efficient manner.

## **Query Language Basics**

- The MongoDB Query Language is used to query and update data in MongoDB documents.
- It is based on the following syntax: `db.collection.find()`
- The `find()` method returns all documents in the specified collection that match the specified filter.

### Example:

```javascript
db.collection.find({ name: 'John', age: 30 });
```

This example queries the `collection` for documents where the `name` field is "John" and the `age` field is 30.

## **Query Operators**

MongoDB Query Language supports a range of query operators that can be used to filter data. Here are some common query operators:

- `==` - Equality operator
- `!=` - Inequality operator
- `>`, `<`, `>=` , `<=` - Comparison operators
- `in` - In operator
- `not in` - Not in operator
- `regex` - Regular expression operator
- `position` - Position operator

### Example:

```javascript
db.collection.find({ name: 'John' });
```

This example queries the `collection` for documents where the `name` field is "John".

## **Aggregation Framework**

The Aggregation Framework is a powerful tool that allows you to process and transform data in MongoDB. It is composed of pipeline stages that can be used to filter, transform, and aggregate data.

### Example:

```javascript
db.collection.aggregate([{ $match: { name: 'John' } }, { $proj: { _id: 0, name: 1, age: 1 } }]);
```

This example aggregates data in the `collection` by matching documents where the `name` field is "John", and then projects the `name` and `age` fields.

## **Query Examples**

### Example 1:

```javascript
db.collection.find({ name: { $regex: '^J' } });
```

This example queries the `collection` for documents where the `name` field starts with the letter "J".

### Example 2:

```javascript
db.collection.find({ age: { $gt: 30 } });
```

This example queries the `collection` for documents where the `age` field is greater than 30.

### Example 3:

```javascript
db.collection.find({ $or: [{ name: 'John' }, { name: 'Jane' }] });
```

This example queries the `collection` for documents where the `name` field is either "John" or "Jane".

### Example 4:

```javascript
db.collection.find({ name: { $regex: '^J.*e' } });
```

This example queries the `collection` for documents where the `name` field starts with "Je" and ends with "e".
