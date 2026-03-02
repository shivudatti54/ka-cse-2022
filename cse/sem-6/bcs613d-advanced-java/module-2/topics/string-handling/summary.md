# String Handling

## Overview

String handling in Java encompasses creating, comparing, manipulating, and converting string objects. Strings are immutable objects representing character sequences, stored in a special string pool for memory optimization, and provide extensive methods for text processing operations.

## Key Points

- **Immutability**: String content cannot change after creation, operations return new strings
- **String Pool**: Literal strings stored in special memory area for reuse
- **Creation Methods**: String literals, new keyword, from char/byte arrays
- **equals() vs ==**: equals() compares content, == compares references
- **Common Methods**: length(), charAt(), substring(), indexOf(), replace(), split()
- **Case Conversion**: toUpperCase(), toLowerCase() return new strings
- **Trimming**: trim() removes leading/trailing whitespace
- **Concatenation**: Using + operator, concat() method, or StringBuilder

## Important Concepts

- String literals reuse same object from pool
- new String() creates object in heap memory
- intern() method adds string to pool or returns existing reference
- String comparison must use equals() not == for content checking
- Use StringBuilder/StringBuffer for multiple modifications

## Notes

- Remember strings are immutable - all modification methods return new strings
- For exams, understand string pool concept and when objects are shared
- Know when to use String vs StringBuilder vs StringBuffer
