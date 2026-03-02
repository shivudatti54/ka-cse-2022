# StringBuffer

## Overview

StringBuffer is a thread-safe, mutable sequence of characters introduced in Java 1.0 for situations requiring efficient string modifications in multi-threaded environments. Unlike immutable String objects, StringBuffer can be modified after creation through methods like append(), insert(), and delete().

## Key Points

- **Mutable**: Content can be changed after creation without creating new objects
- **Thread-Safe**: All methods are synchronized for multi-threaded safety
- **Growable**: Automatically expands capacity using formula (old capacity + 1) \* 2
- **Initial Capacity**: Default is 16 characters, can specify in constructor
- **append() Method**: Adds data to end, supports method chaining
- **insert() Method**: Inserts data at specified position
- **delete() and deleteCharAt()**: Remove characters from buffer
- **reverse()**: Reverses the character sequence in-place

## Important Concepts

- capacity() returns total space, length() returns used space
- Synchronized methods make StringBuffer slower than StringBuilder
- Use for multi-threaded environments where thread safety is required
- Supports method chaining as methods return 'this' reference
- More efficient than String for multiple modifications

## Notes

- Key difference from StringBuilder: StringBuffer is synchronized (thread-safe)
- For exams, remember StringBuffer methods are synchronized while StringBuilder are not
- Use StringBuffer for multi-threading, StringBuilder for single-threading performance
