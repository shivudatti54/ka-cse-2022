# Special String Operations - Summary

## Key Definitions and Concepts

- **String Pool**: Memory area where JVM stores unique string literals to optimize memory
- **Immutability**: Strings cannot be modified after creation (all modifications create new objects)
- **Concatenation**: Combining strings using `+` operator or `concat()` method
- **String Interning**: `intern()` method forces string to be stored in string pool
- **String Conversion**: `toString()` provides object's string representation

## Important Formulas and Theorems

```java
// String Interning
String s1 = new String("Hello").intern();

// Concatenation
String s2 = "Hello" + " World";
String s3 = s1.concat(" Java");

// Conversion
String s4 = String.valueOf(25); // Converts int to "25"
String s5 = Integer.toString(25); // Alternate conversion
```

## Key Points

1. `==` compares object references, `equals()` compares content
2. String pool prevents duplicate storage of identical literals
3. Concatenation with `+` creates intermediate objects (inefficient in loops)
4. `toString()` should be overridden in custom classes for meaningful output
5. `substring(beginIndex,endIndex)` creates new string from original char array
6. `toUpperCase()` and `toLowerCase()` return new string objects
7. `valueOf()` handles null safely (returns "null" string for null objects)
8. String literals are automatically interned, `new String()` creates heap objects

## Common Mistakes to Avoid

1. Using `==` for content comparison instead of `equals()`
   ```java
   String a = "text"; String b = new String("text");
   if(a == b) // False! Use a.equals(b)
   ```
2. Concatenating strings in loops with `+` (use StringBuilder instead)
3. Forgetting that `substring(0,3)` includes index 0-2 (not 0-3)
4. Case-sensitive comparisons without `equalsIgnoreCase()`

## Revision Tips

1. Practice memory diagrams for string pool vs heap allocations
2. Create comparison table: `+` vs `concat()` vs `StringBuilder`
3. Write code samples for all conversion methods:
   ```java
   String.valueOf(true); // "true"
   String.join("-", "A","B","C"); // "A-B-C"
   ```
4. Memorize key method signatures:
   - `String substring(int beginIndex, int endIndex)`
   - `char[] toCharArray()`
   - `static String valueOf(Object obj)`
