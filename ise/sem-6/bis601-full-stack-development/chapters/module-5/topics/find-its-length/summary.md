# **Find its Length Revision Notes**

**Definition:**

- In MongoDB, the `length` function is used to find the length of a string, array, or object in a document.

**Formulas:**

- `length()` function: Returns the number of elements in an array or the length of a string or object.

**Theorems:**

- MongoDB's `length()` function is case-sensitive and treats each character individually when calculating the length of a string.

**Key Points:**

- `length()` function can be used with the `$` operator in MongoDB queries.
- To find the length of an array, use `length(arrayName)`.
- To find the length of a string, use `length(stringName)`.
- To find the length of an object, use `length(objectName)`.
- `length()` function does not work with dates, numbers, and booleans.

**Important Notes:**

- `length()` function only returns a number and does not modify the original document.
- `length()` function can be used in agnostic queries, meaning it can be used with any query type (e.g., find, update, delete).

**Example Queries:**

- Find the length of an array: `db.collection.find({ name: "John", age: { $each: length: 25 } })`
- Find the length of a string: `db.collection.find({ name: "John" })`
- Find the length of an object: `db.collection.find({ name: "John", age: length: 25 })`
- Find the length of a specific field in an object: `db.collection.find({ name: { length: 5 } })`
