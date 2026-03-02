# Advanced String Manipulation Methods in Java

## Overview

The Java String class provides a comprehensive set of utility methods for text manipulation, validation, and transformation. Beyond basic operations, these advanced methods enable developers to perform complex text processing tasks efficiently. This section covers essential string manipulation techniques that form the foundation of text processing in Java applications.

## 1. Whitespace Removal: trim() vs strip()

The **trim()** method removes leading and trailing whitespace characters (ASCII space, tab, newline, etc.) from a string. However, it does not handle all Unicode whitespace characters.

```java
String s = "   Hello   ";
System.out.println(s.trim()); // Output: "Hello"
```

The **strip()** method (introduced in Java 11) provides improved Unicode whitespace handling and is the recommended approach for modern Java applications:

```java
String s = "\u2003Hello\u2003"; // Unicode em space
System.out.println(s.strip()); // Output: "Hello"
```

Key differences:
- trim() only handles ASCII whitespace (code points 0x0000 to 0x0020)
- strip() handles all Unicode whitespace characters
- Java 11+ provides stripLeading() and stripTrailing() for specific whitespace removal

## 2. Substring Extraction

The **substring()** method extracts a portion of a string using index values. The start index is inclusive, while the end index is exclusive:

```java
String text = "Programming";
System.out.println(text.substring(0, 4)); // "Prog"
System.out.println(text.substring(4));    // "ramming"
```

Important considerations:
- IndexOutOfBoundsException is thrown if indices are invalid
- The original string remains unchanged (strings are immutable)
- substring() creates a new string object

## 3. String Splitting with split()

The **split()** method divides a string into an array based on a regular expression delimiter:

```java
String data = "apple,banana,cherry";
String[] arr = data.split(","); // ["apple", "banana", "cherry"]
```

Edge cases and important features:
- Splitting an empty string returns an array with one empty element
- Leading delimiters create empty string elements at the beginning
- The optional limit parameter controls the number of splits:

```java
String s = "a:b:c:d";
s.split(":", 2); // Returns ["a", "b:c:d"]
```

Special regex characters in delimiters must be escaped (e.g., "\\." for dot).

## 4. Replace Methods: replace() vs replaceAll()

Java provides multiple methods for replacing content:

**replace(char oldChar, char newChar)** - Replaces all occurrences of a character:
```java
"hello".replace('l', 'L'); // "heLLo"
```

**replace(CharSequence target, CharSequence replacement)** - Replaces literal strings:
```java
"hello world".replace("world", "Java"); // "hello Java"
```

**replaceAll(String regex, String replacement)** - Uses regular expressions:
```java
"abc123def456".replaceAll("\\d+", "X"); // "abcXdefX"
```

Critical distinction: replaceAll() interprets the first argument as a regex pattern, requiring proper escaping of special characters.

## 5. Pattern Matching with matches()

The **matches()** method checks if a string conforms to a specified regular expression pattern:

```java
String email = "user@example.com";
boolean valid = email.matches("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
```

Common validation patterns:
- Email: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$
- Phone (US): \\d{3}-\\d{3}-\\d{4}
- URL: https?://[\\w.-]+(?:\\.[\\w.-]+)+[\\w.,@?^=%&:/~+#-]*[\\w@?^=%&/~+#-]?

The matches() method attempts to match the entire string against the pattern (implicitly wrapped with ^ and $).

## 6. String Formatting with format()

The **format()** method (and String.formatted()) creates formatted output using format specifiers:

```java
String result = String.format("Name: %s, Age: %d, Score: %.2f", "Alice", 22, 95.5);
// Output: "Name: Alice, Age: 22, Score: 95.50"
```

Common format specifiers:
- %s - String
- %d - Decimal integer
- %f - Floating-point
- %x - Hexadecimal
- %o - Octal
- %t - Date/Time

Flags and modifiers:
- %-10s - Left-align within 10-character width
- %05d - Zero-pad to 5 digits
- %.2f - 2 decimal places

## 7. Additional Utility Methods

**contains(CharSequence)** - Checks if string contains a substring:
```java
"Java Programming".contains("Java"); // true
```

**isEmpty()** - Returns true if length() is 0:
```java
"".isEmpty(); // true
```

**isBlank()** (Java 11+) - Returns true if empty or contains only whitespace:
```java
"   ".isBlank(); // true
```

**concat(String)** - Appends strings (alternative to +):
```java
"Hello".concat(" World"); // "Hello World"
```

**join(CharSequence, CharSequence...)** - Joins strings with delimiter:
```java
String.join("-", "a", "b", "c"); // "a-b-c"
```

## Summary Table

| Method | Purpose | Return Type | Regex-Based |
|--------|---------|-------------|-------------|
| trim() | Remove ASCII whitespace | String | No |
| strip() | Remove Unicode whitespace | String | No |
| substring() | Extract portion | String | No |
| split() | Divide into array | String[] | Yes |
| replace() | Literal replacement | String | No |
| replaceAll() | Regex replacement | String | Yes |
| matches() | Pattern validation | boolean | Yes |
| format() | Formatted output | String | No |

## Best Practices

1. Use strip() over trim() for modern Java applications
2. Remember that strings are immutable - all methods return new strings
3. Escape special regex characters when using split() and replaceAll()
4. Use matches() for validation, not for extracting matched portions
5. Consider performance when processing large strings - consider StringBuilder for multiple operations
6. Use format() or formatted() for creating consistent, readable output