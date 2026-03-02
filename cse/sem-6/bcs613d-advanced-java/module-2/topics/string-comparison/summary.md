# String Comparison

## Overview

String comparison and searching are fundamental operations in Java for tasks like data validation, text processing, and pattern matching. The String class provides methods for exact equality checking, lexicographic ordering, partial matching, and pattern-based searches using regular expressions.

## Key Points

- **equals() and equalsIgnoreCase()**: Check exact string equality, case-sensitive or case-insensitive
- **compareTo()**: Lexicographic comparison returning negative, zero, or positive integer for sorting
- **contentEquals()**: Compare string with any CharSequence (String, StringBuffer, StringBuilder)
- **regionMatches()**: Compare specific regions of two strings with optional case sensitivity
- **indexOf() and lastIndexOf()**: Find position of character or substring, first or last occurrence
- **contains()**: Check if string contains a substring
- **startsWith() and endsWith()**: Check string prefix or suffix
- **matches()**: Use regular expressions for advanced pattern matching

## Important Concepts

- compareTo() returns negative if string precedes, zero if equal, positive if follows
- indexOf() returns -1 if not found, otherwise zero-based index
- All comparison methods are case-sensitive except those with "IgnoreCase" suffix
- String interning affects == comparisons but not equals()
- Safe null handling: use "".equals(str) instead of str.equals("")

## Notes

- Remember equals() returns boolean, compareTo() returns int
- Use indexOf() with start position parameter to find multiple occurrences
- For exams, know that matches() uses regex while contains() uses literal substring
