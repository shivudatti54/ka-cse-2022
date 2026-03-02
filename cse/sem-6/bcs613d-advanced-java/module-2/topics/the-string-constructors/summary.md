# The String Constructors

## Overview

Java String class provides multiple constructors for creating string objects from various sources including character arrays, byte arrays, other strings, StringBuffer, and StringBuilder. Understanding different constructors helps choose the most appropriate string creation method based on data source.

## Key Points

- **Default Constructor**: new String() creates empty string
- **String(char[] value)**: Creates string from character array
- **String(byte[] bytes)**: Creates string from byte array using default charset
- **String(String original)**: Creates copy of another string
- **String(char[] value, int offset, int count)**: Creates string from portion of char array
- **String(byte[] bytes, String charsetName)**: Creates string with specific character encoding
- **String(StringBuffer buffer)**: Creates string from StringBuffer
- **String(StringBuilder builder)**: Creates string from StringBuilder

## Important Concepts

- String literals use string pool, constructors create heap objects
- Constructor with charset useful for internationalization
- Copying constructor rarely needed due to immutability
- Partial array constructors useful for substring creation
- byte array constructors handle encoding/decoding

## Notes

- Prefer string literals over constructors for constant values
- For exams, know that new String("text") creates heap object, not pool
- Remember different constructor signatures and their use cases
