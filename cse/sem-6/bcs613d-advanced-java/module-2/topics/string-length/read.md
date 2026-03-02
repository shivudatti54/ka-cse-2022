# String Length in Java

## Introduction

In Java programming, strings are fundamental objects used to represent sequences of characters. The `String` class provides numerous methods for string manipulation, with `length()` being one of the most frequently used. Understanding string length is critical for tasks like input validation, memory optimization, and avoiding runtime errors.

The `length()` method returns the number of characters in a string, including spaces, special characters, and escape sequences. This value is essential for:

1. Validating user input (e.g., password length checks)
2. Controlling loops that process individual characters
3. Preventing `StringIndexOutOfBoundsException` errors
4. Optimizing memory usage in applications

Mastery of string length is foundational for advanced string operations like substring extraction, parsing, and working with `StringBuilder`.

---

## Key Concepts

### 1. The String Class and Immutability

- Strings in Java are immutable objects (contents cannot change after creation).
- The `length()` method operates on the **logical length** of the string, not the capacity of the underlying character array.

### 2. Syntax of the `length()` Method

```java
public int length()
```

- Returns: The count of 16-bit Unicode characters in the string.
- Time Complexity: O(1) (precomputed value stored in the String object).

**Example:**

```java
String greeting = "Hello ";
int len = greeting.length(); // Returns 9
```

### 3. Comparison with Array Length

| Feature     | String `length()`  | Array `.length`    |
| ----------- | ------------------ | ------------------ |
| Invocation  | Method call        | Property access    |
| Example     | `str.length()`     | `arr.length`       |
| Null Safety | Throws NPE if null | Compile-time error |

### 4. Edge Cases

- **Empty String**: `""` returns `0`
- **Null String**: Throws `NullPointerException`
- **Whitespace**: `" "` returns `3`
- **Unicode Characters**: Each Unicode code point counts as 1 character.

---

## Examples

### Example 1: Basic Length Validation

**Problem**: Validate a password with minimum 8 characters.

```java
String password = "@2023";
if (password.length() >= 8) {
 System.out.println("Valid password");
} else {
 System.out.println("Password too short");
}
```

**Output**:
`Valid password`

### Example 2: String Reversal Using Length

**Problem**: Reverse a string using a loop.

```java
String original = "JAVA";
String reversed = "";
for (int i = original.length() - 1; i >= 0; i--) {
 reversed += original.charAt(i);
}
System.out.println(reversed); // Output: AVAJ
```

### Example 3: Handling Edge Cases

```java
String empty = "";
String whitespace = " ";
System.out.println(empty.length()); // 0
System.out.println(whitespace.length()); // 3

String nullStr = null;
// System.out.println(nullStr.length()); // Throws NullPointerException
```

---

## Real-World Applications

1. **Form Validation**: Enforcing username/password length constraints.
2. **Text Processing**: Truncating long strings for UI displays.
3. **Data Parsing**: Validating fixed-length formats like CSV records.
4. **Network Protocols**: Ensuring message lengths comply with specifications.

---

## Exam Tips

1. **Method vs Property**: `str.length()` for strings vs `arr.length` for arrays.
2. **Return Type**: Always returns `int` (maximum value: `Integer.MAX_VALUE`).
3. **Null Handling**: Always check `if(str != null)` before calling `length()`.
4. **Empty Check**: Use `str.isEmpty()` instead of `length() == 0` for clarity.
5. **Loop Control**: Use `length()-1` as the upper bound for string traversals.
6. **Common Error**: `StringIndexOutOfBoundsException` when using `charAt(length())`.
7. ** Focus**: Expect questions combining `length()` with loops or validation logic.
