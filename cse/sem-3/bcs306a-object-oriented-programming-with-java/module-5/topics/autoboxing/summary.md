# Autoboxing in Java - Summary

## Key Definitions

- **Autoboxing**: The automatic conversion of primitive types to their corresponding wrapper classes performed by the Java compiler
- **Unboxing**: The automatic conversion of wrapper class objects back to their corresponding primitive types
- **Wrapper Classes**: Immutable classes that encapsulate primitive values (Integer, Double, Boolean, Character, etc.)
- **Caching**: The internal optimization where wrapper objects for certain values (typically -128 to 127) are reused

## Important Formulas

- Autoboxing syntax: `WrapperClass obj = primitiveValue;` (converted to `WrapperClass.obj = WrapperClass.valueOf(primitiveValue)`)
- Unboxing syntax: `primitiveType var = wrapperObject;` (converted to `primitiveType var = wrapperObject.primitiveValue()`)

## Key Points

1. Autoboxing and unboxing were introduced in Java 5 (JDK 1.5) to simplify conversion between primitives and wrapper classes
2. The eight wrapper classes are: Boolean, Byte, Character, Short, Integer, Long, Float, and Double
3. The compiler uses valueOf() for autoboxing and xxxValue() methods for unboxing
4. Integer and other numeric wrappers cache objects for values from -128 to 127
5. Always use .equals() for comparing wrapper objects, not the == operator
6. Unboxing a null wrapper reference throws NullPointerException
7. Autoboxing is essential for using primitives with Java Collections
8. Autoboxing has performance implications due to object allocation overhead

## Common Mistakes

1. Using == to compare wrapper objects instead of .equals() method, leading to incorrect comparisons for values outside the cache range
2. Forgetting that unboxing null wrapper references causes NullPointerException
3. Assuming autoboxing always creates new objects (ignoring the cache for small values)
4. Not considering performance impact when autoboxing occurs in tight loops
5. Confusing when autoboxing vs unboxing will occur based on context (variable assignment vs method parameters)