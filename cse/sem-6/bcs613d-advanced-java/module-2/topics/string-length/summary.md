# String Length - Summary

## Key Definitions and Concepts

- **String**: Immutable sequence of Unicode characters in Java, represented by `String` class
- **`.length()`**: Instance method returning number of characters in string (including spaces/special chars)
- **Empty String**: `""` (length = 0)
- **Immutability**: Original string remains unchanged after length operation
- **Unicode**: Supports international characters (each Unicode character counts as 1)

## Important Formulas and Theorems

```java
int len = str.length();  // Basic syntax
```

- **Empty String Check**: `if(str.length() == 0)` or `if(str.isEmpty())`
- **Length vs Capacity**:
  - Strings: `length()` (content size)
  - Arrays: `length` property (total allocated size)
  - `StringBuilder`: `capacity()` (storage allocated)

## Key Points

1. `length()` is a **method** for strings vs `length` **property** for arrays
2. Returns `int` value (max possible: 2³¹-1, though practical limits are much lower)
3. Time Complexity: O(1) - Java stores length as internal field
4. **Empty Check**: Prefer `isEmpty()` over `length() == 0` for readability
5. **Null Safety**: Always check `if(str != null)` before `str.length()` to prevent `NullPointerException`
6. **White Space Counts**: `"  "` has length 2
7. **Unicode Handling**:
   - Code points: `codePointCount(0, str.length())` for complex characters
   - Example: "🚀" has length 2 (UTF-16 surrogate pair) but 1 code point
8. **Memory Impact**: Long strings affect memory (2 bytes per char in UTF-16)
9. **Validation Use**: Essential for form fields (e.g., PAN card must be 10 chars)
10. **Loop Control**: Always use as loop condition: `for(int i=0; i<str.length(); i++)`

## Common Mistakes to Avoid

1. **Null Handling**
   ```java
   String s = null;
   int len = s.length(); // Throws NullPointerException
   ```
2. **Array Confusion**
   ```java
   char[] arr = {'a','b'};
   String s = "ab";
   System.out.println(arr.length); // 2 (correct)
   System.out.println(s.length()); // 2 (correct)
   System.out.println(s.length);   // COMPILE ERROR
   ```
3. **Off-by-One Errors**
   ```java
   String s = "hello";
   char last = s.charAt(s.length()); // Index 5 (valid range: 0-4)
   ```
4. **Ignoring Whitespace**
   ```java
   "  ".length(); // Returns 2 (often mistaken for 0)
   ```

## Revision Tips

1. **Code Comparison**: Write 3 variants - null string, empty string, and regular string
   ```java
   String s1 = null;
   String s2 = "";
   String s3 = "";
   ```
2. **Array vs String**: Create comparison table:
   | Feature | String | Array |
   |----------------|---------------|-------------|
   | Get Length | .length() | .length |
   | Mutable | No | Yes |
3. **Exception Drill**: Practice scenarios causing:
   - `NullPointerException` (null string)
   - `StringIndexOutOfBoundsException` (invalid index access)
4. **Real-world Problem**: Write validation method:
   ```java
   boolean isValidPAN(String pan) {
       return pan != null && pan.length() == 10;
   }
   ```
