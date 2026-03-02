# Modifying a String - Summary

## Key Definitions and Concepts

- **Immutability**: Strings cannot be changed after creation; modifications create new objects
- **StringBuilder**: Mutable class for efficient string manipulation (non-thread-safe)
- **StringBuffer**: Thread-safe version of StringBuilder with synchronized methods
- **Concatenation**: Combining strings using `+` operator or `concat()` method
- **Substring**: Extract portion of string using `substring(start, end)`
- **Trim**: Remove whitespace with `trim()`

## Important Formulas and Theorems

```java
// 1. Concatenation in loops (INEFFICIENT):
String result = "";
for(int i=0; i<1000; i++) {
    result += i; // Creates new String object each iteration
}

// 2. Efficient concatenation:
StringBuilder sb = new StringBuilder();
for(int i=0; i<1000; i++) {
    sb.append(i);
}

// 3. String modification methods:
str.replace(oldChar, newChar)
str.substring(beginIndex, endIndex)
str.toLowerCase()
str.trim()
```

## Key Points

1. Strings are immutable: Any modification creates new object in memory
2. Use `+` operator for simple concatenation, but avoid in loops
3. `StringBuilder` (non-threaded) and `StringBuffer` (thread-safe) classes provide mutable alternatives
4. `substring()` creates new string from original's character array (shared until Java 7u6)
5. `trim()` removes leading/trailing whitespace (ASCII ≤32)
6. `valueOf()` converts primitives/objects to String representation
7. `toUpperCase()`/`toLowerCase()` handle locale-sensitive case changes
8. String modification methods return new objects; original remains unchanged
9. Concatenation performance: O(n²) with `+` in loops vs O(n) with StringBuilder
10. Always prefer `StringBuilder` over `StringBuffer` unless thread safety required

## Common Mistakes to Avoid

1. Using string concatenation (`+`) in loops → Memory inefficiency
2. Assuming `substring()` always creates new char array (pre-Java 7u6 shares parent array)
3. Forgetting that `StringBuffer` has performance overhead due to synchronization
4. Ignoring case sensitivity in comparisons after modification

## Revision Tips

1. Practice creating conversion tables: Method vs Return Type vs Modification Type
2. Memorize method signatures:
   - `substring(int begin, int end)`
   - `replace(CharSequence target, CharSequence replacement)`
3. Compare `StringBuilder` vs `StringBuffer` with thread-safety examples
4. Analyze code snippets with string pools:
   ```java
   String s1 = "Hello";
   String s2 = s1.substring(0,3); // "Hel"
   String s3 = s1.concat("World"); // New object
   ```
