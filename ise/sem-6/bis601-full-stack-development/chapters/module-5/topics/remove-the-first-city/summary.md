### Remove the First City

#### Full Stack Development - MongoDB Basics

- **Problem Statement:** Remove the first city from a collection of cities.
- **Objective:** Learn how to use the MongoDB query language to remove the first document from a collection.
- **Key Concepts:**
  - **Aggregation Framework:** A powerful framework for processing and transforming data in MongoDB.
  - **$sort:** Sorts the documents in a collection in ascending or descending order based on a specified field.
  - **$limit:** Limits the number of documents returned by a query.
  - **$skip:** Skips a specified number of documents before returning the next set of documents.

- **Formula:** To remove the first city, we can use the following pipeline:
  ```javascript
  db.cities.aggregate([
    // Sort the cities in ascending order by their index
    { $sort: { _id: 1 } },
    // Limit the result to the first document
    { $limit: 1 },
    // Skip the first document
    { $skip: 1 },
  ]);
  ```

```
* **Definition:** The `_id` field is automatically assigned a unique identifier to each document in a collection.
* **Theorem:** The aggregation framework allows us to process and transform data in a collection in a flexible and efficient manner.

* **Example Use Case:**
  + Use the above formula to remove the first city from a collection of cities.
  + Use the `DB.collection.remove()` method to remove the first city from a collection of cities.
```
