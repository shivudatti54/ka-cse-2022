# Character Extraction in Java - Summary

## Overview

Character extraction in Java involves retrieving individual characters or character sequences from String objects. The String class provides multiple methods for this purpose, each suited to different scenarios based on performance requirements and use case.

## Primary Extraction Methods

| Method | Return Type | Use Case | Time Complexity |
|--------|-------------|----------|-----------------|
| `charAt(int index)` | char | Single character access | O(1) |
| `toCharArray()` | char[] | Bulk character processing | O(n) |
| `getChars()` | void | Range extraction to array | O(n) |
| `getBytes()` | byte[] | Byte-level representation | O(n) |
| `substring()` | String | Partial string extraction | O(n) |

## Critical Concepts

### Zero-Based Indexing
Java strings use zero-based indexing. Valid indices range from 0 to `length() - 1`. Accessing indices outside this range throws `StringIndexOutOfBoundsException`.

### String Immutability
All String objects are immutable in Java. Extraction methods never modify the original string; instead, they return new objects or primitive values. This ensures thread safety but requires awareness of memory allocation.

### Method-Specific Details

- **charAt()**: Ideal for sequential character traversal. Use in loops for searching, counting, or pattern detection
- **toCharArray()**: Creates independent copy; modifications to array don't affect original string
- **getChars()**: More efficient than multiple charAt() calls when extracting character ranges
- **getBytes()**: Essential for I/O operations and network communication
- **substring()**: Returns new String; original remains unchanged

## Error Handling

Always handle potential exceptions:
```java
// Safe access pattern
if (index >= 0 && index < str.length()) {
    char c = str.charAt(index);
}
```

## Exam Preparation Points

1. Remember that charAt() operates in O(1) constant time
2. Understand the difference between charAt() (single char) and substring() (new String)
3. Know that toCharArray() creates a new array - modifying it doesn't change the original
4. Practice writing loops that traverse strings using charAt()
5. Understand the memory implications of immutability

## Best Practices

- Use charAt() for single character access in performance-critical code
- Use toCharArray() when you need to modify characters extensively
- Use getChars() for extracting ranges efficiently
- Always validate indices before accessing characters from user input