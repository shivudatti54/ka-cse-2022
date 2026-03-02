# Find and Log the Index of a Specific City

## **Overview**

This topic focuses on finding and logging the index of a specific city in a MongoDB database.

## **Key Points**

- **Find a City by Name**: Use the `find()` method to search for a document that matches the specified city name.
- **Index Creation**: Create a global or local index on the city name field to enable efficient querying.
- **Index Logging**: Log the index name, type, and fields used in the query to track the optimization plan.

## **Import Formulas and Definitions**

- **Indexing Formula**: `indexName = fieldName + '_index'` (global index) or `indexName = collectionName + '_' + fieldName + '_index'` (local index)
- **Query Optimization Theorem**: "The query optimizer chooses the most efficient index for the query."
- **Index Type**:
  - **Global Index**: Available to all collections in the database.
  - **Local Index**: Available only to the collection where it was created.

## **Revision Tips**

- Practice creating and querying indexes using the `find()` method.
- Familiarize yourself with the `index()` method to create indexes on specific fields.
- Review the query optimization process to understand how indexes impact performance.

## **Quick Reference**

| **Method**  | **Description**                                                  |
| ----------- | ---------------------------------------------------------------- |
| `find()`    | Searches for a document that matches the specified filter.       |
| `index()`   | Creates a global or local index on a specific field.             |
| `explain()` | Returns a document that describes the query plan and index used. |
