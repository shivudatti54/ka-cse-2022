# StringBuilder

## Overview

StringBuilder is a mutable sequence of characters introduced in Java 5, providing better performance than StringBuffer in single-threaded environments. It offers the same API as StringBuffer but without synchronization overhead, making it ideal for string manipulation operations where thread safety is not required.

## Key Points

- **Mutable**: Content can be modified after creation without new object creation
- **Not Thread-Safe**: No synchronized methods for better performance
- **Faster**: Better performance than StringBuffer in single-threaded scenarios
- **Same API**: Methods identical to StringBuffer (append, insert, delete, reverse)
- **Initial Capacity**: Default 16 characters, grows dynamically as needed
- **Method Chaining**: Most methods return 'this' for fluent interface
- **capacity() vs length()**: capacity is total space, length is used space
- **toString()**: Converts StringBuilder to immutable String

## Important Concepts

- Use StringBuilder for single-threaded string building
- Growth formula: new capacity = (old capacity + 1) \* 2
- More efficient than String concatenation in loops
- Supports insertion, deletion, reversal operations
- Common in HTML/XML generation, logging, file paths

## Notes

- Key difference from StringBuffer: StringBuilder is NOT synchronized
- For exams, remember StringBuilder is faster but not thread-safe
- Use StringBuilder over String + concatenation for performance in loops
