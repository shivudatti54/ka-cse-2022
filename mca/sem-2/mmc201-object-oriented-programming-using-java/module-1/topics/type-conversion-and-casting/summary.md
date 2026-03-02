# Type Conversion and Casting - Summary

## Key Definitions and Concepts

- **Type Conversion:** The process of converting a value from one data type to another in Java
- **Implicit Conversion (Widening):** Automatic conversion by compiler when no data loss occurs; follows hierarchy: byte → short → char → int → long → float → double
- **Explicit Conversion (Narrowing/Casting):** Manual conversion using cast operator `(targetType) value`; may result in data loss
- **Binary Numeric Promotion:** Automatic promotion of operands in arithmetic expressions to larger types
- **Upcasting:** Converting subclass reference to superclass reference (implicit and safe)
- **Downcasting:** Converting superclass reference to subclass reference (explicit and requires instanceof check)

## Important Formulas and Theorems

- **Cast Operator Syntax:** `(TargetType) expression`
- **Binary Promotion Rules:** byte, short, char → int → long → float → double
- **String to Primitive:** `PrimitiveType.parsePrimitiveType(String)`
- **String to Wrapper:** `WrapperType.valueOf(String)`

## Key Points

- Implicit conversions (widening) occur automatically from smaller to larger types without data loss
- Explicit casting is required when converting from larger to smaller types or between incompatible types
- In arithmetic expressions, byte, short, and char are always promoted to int before calculation
- Reference type casting operates on objects in inheritance hierarchies, not primitive values
- Always use instanceof operator before downcasting to prevent ClassCastException
- String to number conversion uses wrapper class methods and may throw NumberFormatException
- Upcasting is always safe and implicit; downcasting is risky and requires explicit syntax and runtime checking

## Common Mistakes to Avoid

- Forgetting that byte, short, and char are promoted to int in arithmetic operations, causing compilation errors when assigning results back to these types
- Attempting downcasting without using instanceof, leading to runtime ClassCastException
- Confusing parseXxx() with valueOf() methods—remember parseXxx() returns primitive while valueOf() returns wrapper
- Assuming all narrowing conversions will work correctly without checking the range of values
- Not handling NumberFormatException when converting strings to numbers

## Revision Tips

- Memorize the widening hierarchy order as it's frequently tested in exams
- Practice writing code with both primitive and reference type casting scenarios
- Always check for instanceof before performing downcast operations in your code
- Remember that string concatenation with + automatically converts other types to strings
- Review previous year university exam questions on type casting to understand the question patterns
