# Data Conversion Using valueOf()

## Overview

The valueOf() method in Java provides type conversion from various data types to their String representation or wrapper objects. It's a static method available in String class and wrapper classes (Integer, Double, etc.) for converting primitives, objects, and character arrays to appropriate types.

## Key Points

- **String.valueOf()**: Converts primitives, objects, and char arrays to String
- **Integer.valueOf()**: Converts String to Integer wrapper object
- **Radix Parameter**: Integer.valueOf(String, radix) parses string in specified base (binary, octal, hex)
- **Automatic null Handling**: String.valueOf(null) returns "null" string
- **Object Conversion**: Calls toString() method on objects
- **Character Array**: String.valueOf(char[]) converts array to string
- **Partial Array**: String.valueOf(char[], offset, count) converts portion of array

## Important Concepts

- valueOf() differs from parsing methods (parseInt returns primitive, valueOf returns wrapper)
- Radix parameter allows parsing binary (2), octal (8), hexadecimal (16) numbers
- String.valueOf() is null-safe unlike toString() which throws NullPointerException
- Wrapper classes cache values for performance (Integer -128 to 127)
- Use valueOf() instead of constructor for wrapper objects (recommended)

## Notes

- Remember Integer.valueOf() returns wrapper object, Integer.parseInt() returns primitive int
- For exams, know radix parameter usage: Integer.valueOf("1111", 2) = 15
- String.valueOf() is safer than toString() for null handling
