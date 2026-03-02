# **Data Types in MongoDB**

### Overview

- In MongoDB, data types determine the type of data that can be stored in a field or collection.
- Understanding data types is crucial for efficient data storage and retrieval.

### Built-in Data Types

- **String**: a sequence of characters (e.g., "hello World")
- **Number**: a numeric value (e.g., 123.45)
- **Boolean**: a true or false value (e.g., true or false)
- **Array**: an ordered list of values (e.g., [1, 2, 3])
- **Object**: an unordered collection of key-value pairs (e.g., {key1: "value1", key2: "value2"})
- **Date/Time**: a date or time value (e.g., ISODate("2022-01-01T12:00:00.000Z"))
- **Binary**: a binary data value (e.g., a hexadecimal string)

### Special Data Types

- **ObjectId**: a unique identifier for a document (default field)
- **Min/Max**: a range of values (e.g., 10.5.0 to 20.5.0)
- **Regex**: a regular expression pattern (e.g., /pattern/ for matching)

### Data Type Size Limitations

- **String**: maximum of 16,777,215 characters (16 MB)
- **Number**: maximum of 31,622,368 (32 MB)
- **Object**: maximum of 16 MB (key-value pairs)

### Formula/Definition/Theorem

- **Schema**: a definition of the structure of a collection (not a formula, but a concept)

### Key Concepts

- **Data typing**: the process of assigning a data type to a field or collection.
- **Data validation**: ensuring that data conforms to its assigned data type.

### Important Notes

- MongoDB is a flexible, dynamic document-oriented database.
- Data types can be changed after data is inserted.
- Indexing can be applied to optimize queries based on data types.
