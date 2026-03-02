# Joining Strings - Summary

## Key Definitions and Concepts

- **String Immutability**: Strings cannot be modified after creation; concatenation creates new objects
- **StringJoiner**: Utility class (java.util) for constructing sequences with delimiter, prefix, and suffix
- **String.join()**: Static method for joining CharSequence elements with specified delimiter
- **Delimiter**: Character/string separating joined elements (e.g., comma in CSV)
- **Performance Overhead**: Excessive memory usage from `+` operator in loops due to intermediate objects

## Important Formulas and Methods

```java
// Basic joining with delimiter
String joined = String.join(", ", "A", "B", "C"); // "A, B, C"

// StringJoiner with prefix/suffix
StringJoiner sj = new StringJoiner(":", "[", "]");
sj.add("X").add("Y"); // "[X:Y]"

// Collection joining
List<String> colors = Arrays.asList("Red", "Green", "Blue");
String result = String.join("|", colors); // "Red|Green|Blue"
```

## Key Points

- Always prefer `String.join()` or `StringJoiner` over `+` operator for multiple concatenations
- Java 8+ provides optimized string joining methods with O(n) time complexity
- `StringJoiner` allows custom prefixes/suffixes (essential for JSON/CSV formatting)
- For non-trivial joins, combine with Stream API: `.collect(Collectors.joining())`
- Underlying implementation uses `StringBuilder` for efficient concatenation
- Empty elements are included by default (use `filter()` with streams to exclude)
- Methods handle `null` values gracefully by converting to "null" string

## Common Mistakes to Avoid

1. **Using `+=` in loops**:
   ```java
   // Wrong: Creates 10 intermediate strings
   String s = "";
   for(int i=0; i<10; i++) s += i;
   ```
2. **Ignoring existing methods**:

   ```java
   // Instead of manual loop:
   String.join("", IntStream.range(0,10).mapToObj(String::valueOf).toArray())
   ```

3. **Mixing parameter order**:
   ```java
   // Correct order: delimiter first
   String.join(", ", list); // Right
   String.join(list, ", "); // Compilation error
   ```

## Revision Tips

1. **Practice method signatures**:
   - `String.join(CharSequence delimiter, CharSequence... elements)`
   - `StringJoiner(CharSequence delimiter, CharSequence prefix, CharSequence suffix)`

2. **Compare approaches**:
   - Create CSV using: `+` operator vs `StringJoiner` vs `StringBuilder`

3. **Remember performance hierarchy**:
   Single-line joins: `String.join()` > Complex joins: `StringJoiner` > Massive data: `StringBuilder`

4. **Experiment with edge cases**:
   - Joining empty list
   - Null elements in collection
   - Multi-character delimiters
