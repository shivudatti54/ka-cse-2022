# Hive Data Types - Summary

## Key Definitions and Concepts

- **Primitive Types**: Basic data types including numeric (TINYINT, SMALLINT, INT, BIGINT, FLOAT, DOUBLE, DECIMAL), string (STRING, VARCHAR, CHAR), date/time (DATE, TIMESTAMP), boolean, and binary types.

- **Complex Types**: Advanced data types for modeling structured data - ARRAY (ordered collection), MAP (key-value pairs), STRUCT (named fields), and UNIONTYPE (one of several types).

- **Type Conversion**: Process of converting values from one data type to another, either implicitly (automatic) or explicitly using CAST function.

## Important Formulas and Techniques

- ARRAY access: `array[index]` - zero-indexed
- MAP access: `map['key']`
- STRUCT access: `struct.field`
- CAST syntax: `CAST(expression AS target_type)`
- Complex type flattening: `LATERAL VIEW EXPLODE(array_col) AS element`

## Key Points

- INT is the default integer type in Hive; integer literals are treated as INT unless explicitly cast.

- STRING has no length limit and can store up to 2GB of data, making it the preferred string type.

- Complex types enable modeling JSON-like nested data structures directly in Hive tables.

- LATERAL VIEW is essential for querying complex types - it enables row generation from array/map elements.

- Failed CAST operations return NULL instead of errors - important for debugging.

- DECIMAL should be used for financial data requiring exact precision rather than FLOAT/DOUBLE.

- TIMESTAMP provides nanosecond precision for time-based data.

- Complex types can be nested to any depth for representing highly structured data.

## Common Mistakes to Avoid

- Using wrong index (arrays are zero-indexed, not one-indexed)
- Forgetting that MAP keys must be primitive types
- Attempting direct comparison of complex types (only equality works)
- Not using LATERAL VIEW when querying elements inside ARRAY/MAP
- Confusing VARCHAR (variable length) with CHAR (fixed length padded with spaces)

## Revision Tips

- Practice creating tables with all data types and writing queries to access nested elements.
- Remember the numeric type promotion hierarchy: TINYINT → SMALLINT → INT → BIGINT → FLOAT → DOUBLE.
- Review the three notation styles: bracket [] for arrays/maps, dot . for structs, index for arrays.
- Study type conversion examples using CAST function with different source and target types.
- Complete the learning objectives from PURPOSE_MD to ensure thorough understanding.