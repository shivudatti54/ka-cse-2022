# **Remove the First City**

## **Introduction**

In this section, we will learn how to remove the first city from a collection in MongoDB. MongoDB is a NoSQL database that stores data in JSON-like documents called BSON (Binary Serialized Object Notation).

## **What is a Collection?**

A collection is a group of related documents in MongoDB. Each document represents a single record or entry, and can have multiple fields or keys.

## **What is a Document?**

A document is a single record or entry in a collection. It is a JSON-like object that can have multiple fields or keys.

## **What is MongoDB Query Language?**

MongoDB Query Language is used to filter and manipulate data in MongoDB. It is based on a JSON-like syntax and allows you to query and update data in a flexible and efficient manner.

## **Removing the First City**

To remove the first city from a collection, we will use the following MongoDB Query Language syntax:

```javascript
db.collection.remove({ _id: 0 });
```

- `_id` is the field that we want to use to identify the document.
- `0` is the index of the first document in the collection.

## **Example**

Let's consider the following collection:

```json
[
  {
    "_id": 0,
    "name": "New York",
    "city": "Empire City"
  },
  {
    "_id": 1,
    "name": "Los Angeles",
    "city": "Hollywood City"
  },
  {
    "_id": 2,
    "name": "Chicago",
    "city": "Windy City"
  },
  {
    "_id": 3,
    "name": "Houston",
    "city": "Space City"
  }
]
```

To remove the first city, we will use the following MongoDB Query Language syntax:

```javascript
db.cities.remove({ _id: 0 });
```

After running this query, the collection will be updated as follows:

```json
[
  {
    "_id": 1,
    "name": "Los Angeles",
    "city": "Hollywood City"
  },
  {
    "_id": 2,
    "name": "Chicago",
    "city": "Windy City"
  },
  {
    "_id": 3,
    "name": "Houston",
    "city": "Space City"
  }
]
```

Note that the first document is removed from the collection.

## **Best Practices**

When removing documents from a collection, it is essential to consider the following best practices:

- Always use the `_id` field to identify the document that you want to remove.
- Use the `remove` method to remove documents from the collection.
- Be cautious when removing documents, as this action cannot be undone.

## **Conclusion**

In this section, we learned how to remove the first city from a collection in MongoDB. We also covered the best practices for removing documents from a collection. By mastering this topic, you will be able to efficiently manage your data in MongoDB.
