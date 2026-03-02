# Searching Strings

## Overview

String searching in Java involves finding characters or substrings within strings using methods like indexOf(), lastIndexOf(), contains(), startsWith(), and endsWith(). These methods enable efficient text processing, validation, and pattern matching operations.

## Key Points

- **indexOf(char/String)**: Returns index of first occurrence, -1 if not found
- **indexOf(char/String, fromIndex)**: Search starting from specified position
- **lastIndexOf(char/String)**: Returns index of last occurrence
- **contains(CharSequence)**: Boolean check if substring exists
- **startsWith(String)**: Check if string begins with specified prefix
- **endsWith(String)**: Check if string ends with specified suffix
- **Zero-Based Indexing**: First character is at position 0
- **Return Value -1**: Indicates character or substring not found

## Important Concepts

- indexOf() returns first occurrence position
- lastIndexOf() scans string from end to beginning
- Use indexOf() with fromIndex to find multiple occurrences
- contains() internally uses indexOf() method
- startsWith() and endsWith() useful for file validation

## Notes

- Remember indexOf() returns -1 when not found, not null or exception
- For exams, know how to use indexOf() with starting position parameter
- Practice finding multiple occurrences by updating search start position
