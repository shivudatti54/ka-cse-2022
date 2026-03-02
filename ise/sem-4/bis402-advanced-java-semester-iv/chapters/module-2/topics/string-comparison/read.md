# String Comparison and Searching in Java

## Introduction

String comparison and searching are fundamental operations in Java programming, essential for tasks like data validation, text processing, and pattern matching. The Java String class provides numerous methods to perform these operations efficiently. Understanding these methods is crucial for effective string manipulation.

## String Comparison Methods

### 1. equals() and equalsIgnoreCase()

The most basic comparison methods check for exact string equality.

```java
String str1 = "Hello";
String str2 = "hello";

System.out.println(str1.equals(str2));        // false
System.out.println(str1.equalsIgnoreCase(str2)); // true
```

### 2. compareTo() and compareToIgnoreCase()

These methods compare strings lexicographically (dictionary order) and return:

- Negative integer if the string precedes the argument
- Zero if strings are equal
- Positive integer if the string follows the argument

```java
String a = "apple";
String b = "banana";

System.out.println(a.compareTo(b));        // negative
System.out.println(b.compareTo(a));        // positive
System.out.println(a.compareTo("apple"));  // zero
```

### 3. contentEquals()

Compares a string with any CharSequence (String, StringBuffer, StringBuilder):

```java
String str = "Hello";
StringBuffer sb = new StringBuffer("Hello");

System.out.println(str.contentEquals(sb)); // true
```

### 4. regionMatches()

Compares specific regions of strings:

```java
String str1 = "Hello World";
String str2 = "World Hello";

// Compare region of str1 (index 6) with str2 (index 0)
boolean result = str1.regionMatches(6, str2, 0, 5);
System.out.println(result); // true (compares "World")
```

## String Searching Methods

### 1. indexOf() and lastIndexOf()

Find the position of characters or substrings:

```java
String text = "Java programming is fun";

// Find first occurrence
int firstIndex = text.indexOf('a');        // 1
int firstJava = text.indexOf("Java");      // 0

// Find last occurrence
int lastIndex = text.lastIndexOf('a');     // 10
int lastJava = text.lastIndexOf("Java");   // 0

// Find from specific position
int fromIndex = text.indexOf('a', 5);      // 10
```

### 2. contains()

Checks if a substring exists:

```java
String message = "Welcome to Java Programming";
boolean hasJava = message.contains("Java"); // true
boolean hasPython = message.contains("Python"); // false
```

### 3. startsWith() and endsWith()

Check prefix and suffix:

```java
String filename = "document.pdf";

boolean isPdf = filename.endsWith(".pdf");    // true
boolean startsWithDoc = filename.startsWith("doc"); // true
```

### 4. matches()

Uses regular expressions for pattern matching:

```java
String email = "user@example.com";
boolean isValidEmail = email.matches("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}");
```

## Comparison Table

| Method                | Returns | Case-Sensitive | Use Case                      |
| --------------------- | ------- | -------------- | ----------------------------- |
| equals()              | boolean | Yes            | Exact equality check          |
| equalsIgnoreCase()    | boolean | No             | Case-insensitive equality     |
| compareTo()           | int     | Yes            | Sorting/ordering              |
| compareToIgnoreCase() | int     | No             | Case-insensitive ordering     |
| contentEquals()       | boolean | Yes            | Compare with any CharSequence |
| regionMatches()       | boolean | Configurable   | Partial string comparison     |

## Performance Considerations

```
ASCII Diagram: String Comparison Process

+----------------+    +-----------------+    +-----------------+
|   String A     |    | Character-by-   |    |   Result        |
| "Hello"        | -> | Character       | -> | (boolean/int)   |
|   String B     |    | Comparison      |    |                 |
| "Hello"        |    |                 |    |                 |
+----------------+    +-----------------+    +-----------------+
```

For large-scale string operations:

- Use `StringBuilder` for repeated modifications
- Consider using `Collator` for locale-specific comparisons
- Precompile regex patterns for repeated `matches()` calls

## Common Pitfalls

1. **Null Pointer Exception**: Always check for null before comparison
2. **Case Sensitivity**: Remember that most comparison methods are case-sensitive
3. **Internationalization**: Use appropriate methods for locale-specific comparisons

```java
// Safe comparison with null check
public static boolean safeEquals(String a, String b) {
    return (a == b) || (a != null && a.equals(b));
}
```

## Exam Tips

1. **Remember return types**: `equals()` returns boolean, `compareTo()` returns int
2. **Index positions**: Java uses 0-based indexing - first character is at position 0
3. **Empty strings**: `"".equals(str)` is safer than `str.equals("")` for null safety
4. **String literals vs objects**: Understand how string interning affects `==` comparisons
5. **Method chaining**: Most string methods return new strings (strings are immutable)
