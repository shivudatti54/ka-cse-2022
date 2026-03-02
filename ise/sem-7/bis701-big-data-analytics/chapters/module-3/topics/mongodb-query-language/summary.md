# **MongoDB Query Language Revision Notes**

### Overview

- MongoDB Query Language (MQL) is a document-oriented query language used to retrieve data from MongoDB databases.
- MQL is based on JavaScript, allowing for flexible and dynamic queries.

### Key Concepts

- **Find() method**: Retrieves a single document or an array of documents that match a query filter.
- **Aggregate() method**: Processes an array of documents and returns a new array of documents.
- **Query Filter**: A JSON object that specifies the conditions for retrieving documents.
- **Projection**: A JSON object that specifies the fields to include in the result set.
- **Sorting**: Used to sort the result set in ascending or descending order.

### Query Filters

- **Equality**: `db.collection.find({ field: "value" })`
- **Inequality**: `db.collection.find({ field: { $ne: "value" } })`
- **Regular Expressions**: `db.collection.find({ field: { $regex: "pattern" } })`
- **Array**: `db.collection.find({ field: { $elemMatch: { value: "value" } } })`

### Aggregation

- **$group**: Groups documents by a specified field.
- **$sum**: Calculates the sum of a specified field.
- **$avg**: Calculates the average of a specified field.
- **$max**: Returns the maximum value of a specified field.
- **$min**: Returns the minimum value of a specified field.

### Projection

- **$project**: Projects fields from the result set.
- **$pick**: Picks specific fields from the result set.
- **$omit**: Omits specific fields from the result set.

### Sorting

- **$sort**: Sorts the result set in ascending or descending order.
- **$limit**: Returns a limited number of documents.

### Important Formulas and Definitions

- **$ne**: Not equal to operator.
- **$eq**: Equal to operator.
- **$regex**: Regular expression operator.
- **$elemMatch**: Matches each document in an array.
- **$group**: Groups documents by a specified field.
- **$sum**: Calculates the sum of a specified field.
- **$avg**: Calculates the average of a specified field.

### Theorems

- **De Morgan's Law**: `$(A \cap B)' = A' \cup B'` (not used in MQL)
- **Distributive Law**: `$(A \cup B)C = AC \cup BC` (not used in MQL)

Note: This summary focuses on key concepts and formulas in MongoDB Query Language. For a more comprehensive understanding, refer to the official MongoDB documentation.
