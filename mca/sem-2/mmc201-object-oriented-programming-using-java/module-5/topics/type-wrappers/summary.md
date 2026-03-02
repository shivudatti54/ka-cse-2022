# Type Wrappers in Java - Summary

## Key Definitions

- **Type Wrapper**: A class that encapsulates a primitive value within an object, enabling primitives to be treated as objects.
- **Autoboxing**: The automatic conversion from a primitive type to its corresponding wrapper class performed by the Java compiler.
- **Unboxing**: The automatic conversion from a wrapper object to its corresponding primitive type.
- **Immutability**: A property of wrapper classes where their objects cannot be modified after creation; all wrapper classes are final.

## Important Formulas

- `Integer.valueOf(String s)` - Returns Integer object from String
- `Integer.parseInt(String s)` - Returns int primitive from String
- `wrapperObject.intValue()` - Returns primitive int from Integer
- `Double.MIN_VALUE` / `Double.MAX_VALUE` - Minimum and maximum double values
- `Character.isDigit(char c)` - Checks if character is a digit
- `Boolean.parseBoolean(String s)` - Converts String to boolean primitive

## Key Points

1. Java provides eight wrapper classes: Integer, Long, Float, Double, Short, Byte, Character, Boolean.

2. All wrapper classes are in the java.lang package and are automatically imported.

3. Numeric wrapper classes (Integer, Long, Float, Double, Short, Byte) extend the abstract class Number.

4. Autoboxing and unboxing were introduced in Java 5 to simplify primitive-to-object conversions.

5. Wrapper objects should be compared using `.equals()` method, not the `==` operator.

6. Wrapper classes provide constants like MIN_VALUE and MAX_VALUE for determining numeric ranges.

7. Collections and generics require wrapper classes because they can only store objects, not primitives.

8. Wrapper classes enable handling of null values, which primitives cannot represent.

9. Each numeric wrapper class provides conversion methods between different numeric types.

## Common Mistakes

1. Using `==` to compare wrapper objects instead of `.equals()`, leading to incorrect comparison results.

2. Confusing `valueOf()` (returns wrapper) with `parseXxx()` (returns primitive) when writing conversion code.

3. Assuming wrapper objects created from literals are always cached—only certain values within specific ranges may be cached.

4. Forgetting that autoboxing can throw NullPointerException when a null wrapper object is unboxed.

5. Not accounting for the performance overhead of autoboxing/unboxing in tight loops or performance-critical code.