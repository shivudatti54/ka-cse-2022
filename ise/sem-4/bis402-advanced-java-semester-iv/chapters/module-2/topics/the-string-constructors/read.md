# String Constructors and Operations in Java

## Introduction to String Handling

In Java, strings are objects that represent sequences of characters. Java provides extensive support for string manipulation through the `String`, `StringBuffer`, and `StringBuilder` classes. Understanding how to create and manipulate strings is fundamental to Java programming.

Strings in Java are immutable - once created, their values cannot be changed. This immutability provides several benefits including thread safety and security, but also means that operations that appear to modify strings actually create new string objects.

## String Constructors

The String class provides multiple constructors to create string objects in different ways:

### 1. Default and Parameterized Constructors

```java
// Empty string constructor
String emptyString = new String();

// From character array
char[] charArray = {'H', 'e', 'l', 'l', 'o'};
String fromCharArray = new String(charArray);

// From byte array (using platform's default charset)
byte[] byteArray = {72, 101, 108, 108, 111};
String fromByteArray = new String(byteArray);

// From another string (creates copy)
String original = "Hello";
String copy = new String(original);
```

### 2. Advanced Constructors

```java
// From portion of character array
char[] chars = {'J', 'a', 'v', 'a', 'P', 'r', 'o', 'g', 'r', 'a', 'm'};
String substringFromArray = new String(chars, 4, 7); // "Program"

// From byte array with specific charset
try {
    byte[] bytes = "Hello".getBytes("UTF-8");
    String fromBytesWithCharset = new String(bytes, "UTF-8");
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}

// From StringBuffer
StringBuffer buffer = new StringBuffer("Hello");
String fromBuffer = new String(buffer);

// From StringBuilder
StringBuilder builder = new StringBuilder("World");
String fromBuilder = new String(builder);
```

## String Length

The `length()` method returns the number of characters in a string:

```java
String text = "Java Programming";
int length = text.length(); // Returns 16
```

**Important**: `length` is a method for strings, but a field for arrays:
- `string.length()` - method call
- `array.length` - field access

## Special String Operations

### 1. String Literals vs. String Objects

```
Memory Diagram:
+-------------------+     +-----------------+
| String Pool       |     | Heap Memory     |
+-------------------+     +-----------------+
| "Hello" (literal) |     | new String()    |
| "World" (literal) |     | new String()    |
+-------------------+     +-----------------+
```

```java
String literal1 = "Hello";       // Uses string pool
String literal2 = "Hello";       // Reuses same object from pool
String object1 = new String("Hello"); // Creates new object in heap
String object2 = new String("Hello"); // Creates another new object

System.out.println(literal1 == literal2);   // true - same object
System.out.println(object1 == object2);     // false - different objects
System.out.println(literal1.equals(object1)); // true - same content
```

### 2. String Concatenation

```java
// Using + operator
String result = "Hello" + " " + "World"; // "Hello World"

// Using concat() method
String part1 = "Hello";
String part2 = "World";
String combined = part1.concat(" ").concat(part2);

// With other data types (automatic conversion)
String message = "Value: " + 42; // "Value: 42"
String calculation = "Result: " + (10 + 20); // "Result: 30"
```

## Character Extraction

Java provides several methods to extract characters from strings:

### 1. Basic Character Access

```java
String text = "Java Programming";

// Get character at specific position
char firstChar = text.charAt(0); // 'J'
char fifthChar = text.charAt(4); // ' ' (space)

// Get all characters as array
char[] allChars = text.toCharArray();

// Get bytes
byte[] bytes = text.getBytes();
```

### 2. Substring Extraction

```java
String text = "Java Programming";

// Extract from index to end
String substring1 = text.substring(5); // "Programming"

// Extract from start index to end index-1
String substring2 = text.substring(0, 4); // "Java"
String substring3 = text.substring(5, 16); // "Programming"
```

## String Comparison

Java provides multiple ways to compare strings:

### Comparison Methods Comparison Table

| Method | Returns | Case-Sensitive | Null Handling | Usage |
|--------|---------|----------------|---------------|--------|
| `equals()` | boolean | Yes | Null-safe | Content equality check |
| `equalsIgnoreCase()` | boolean | No | Null-safe | Case-insensitive equality |
| `compareTo()` | int | Yes | Throws NPE | Sorting order |
| `compareToIgnoreCase()` | int | No | Throws NPE | Case-insensitive sorting |
| `==` | boolean | N/A | N/A | Reference equality |

```java
String str1 = "Java";
String str2 = "java";
String str3 = "Java";
String str4 = new String("Java");

// Content comparison
boolean equal1 = str1.equals(str2); // false - different case
boolean equal2 = str1.equalsIgnoreCase(str2); // true - ignore case
boolean equal3 = str1.equals(str3); // true - same content

// Reference comparison
boolean sameRef1 = (str1 == str3); // true - same pool object
boolean sameRef2 = (str1 == str4); // false - different objects

// Lexicographical comparison
int result1 = str1.compareTo(str2); // Negative - "Java" < "java"
int result2 = str1.compareToIgnoreCase(str2); // 0 - equal ignoring case
```

## Searching and Modifying Strings

### 1. Search Operations

```java
String text = "Java Programming is fun with Java";

// Check if contains substring
boolean contains = text.contains("Programming"); // true

// Find first occurrence
int firstIndex = text.indexOf("Java"); // 0
int secondIndex = text.indexOf("Java", 1); // 21

// Find last occurrence
int lastIndex = text.lastIndexOf("Java"); // 21

// Check prefixes and suffixes
boolean starts = text.startsWith("Java"); // true
boolean ends = text.endsWith("Java"); // false
```

### 2. Modification Operations

Though strings are immutable, these methods return new modified strings:

```java
String original = "  Java Programming  ";

// Trim whitespace
String trimmed = original.trim(); // "Java Programming"

// Replace characters
String replaced = original.replace('a', 'o'); // "  Jovo Progromming  "

// Replace sequences
String replacedSeq = original.replace("Java", "Python"); // "  Python Programming  "

// Case conversion
String upper = original.toUpperCase(); // "  JAVA PROGRAMMING  "
String lower = original.toLowerCase(); // "  java programming  "
```

## valueOf() Method

The `valueOf()` method converts various data types to String representation:

```java
// Convert primitive types
String intStr = String.valueOf(123); // "123"
String doubleStr = String.valueOf(45.67); // "45.67"
String boolStr = String.valueOf(true); // "true"

// Convert character array
char[] chars = {'H', 'i'};
String charStr = String.valueOf(chars); // "Hi"

// Convert portion of character array
String partialCharStr = String.valueOf(chars, 0, 1); // "H"

// Convert objects (calls toString() method)
String objStr = String.valueOf(new Object()); // "java.lang.Object@hashcode"
```

## StringBuffer Class

StringBuffer is a mutable sequence of characters that is thread-safe:

### Key Features:
- **Mutable**: Can be modified after creation
- **Thread-safe**: Synchronized methods
- **Better performance** for multiple modifications

### Common Methods:

```java
StringBuffer buffer = new StringBuffer(); // Initial capacity: 16
StringBuffer bufferWithContent = new StringBuffer("Hello");

// Append operations
buffer.append("Java");
buffer.append(" ").append("Programming"); // "Java Programming"

// Insert operations
buffer.insert(4, " "); // Insert space at position 4: "Java Programming"

// Delete operations
buffer.delete(5, 16); // Remove "Programming": "Java "
buffer.deleteCharAt(4); // Remove space: "Java"

// Reverse
buffer.reverse(); // "avaJ"

// Set operations
buffer.setCharAt(0, 'j'); // "java"
buffer.setLength(2); // Truncate to "ja"

// Capacity management
int capacity = buffer.capacity(); // Current capacity
buffer.ensureCapacity(50); // Ensure minimum capacity
```

## StringBuilder Class

StringBuilder is similar to StringBuffer but not thread-safe, offering better performance:

### Key Differences from StringBuffer:
- **Not synchronized** (not thread-safe)
- **Better performance** in single-threaded environments
- **Same API** as StringBuffer

```java
StringBuilder builder = new StringBuilder();
builder.append("Hello").append(" ").append("World");
String result = builder.toString(); // "Hello World"
```

### Performance Comparison Table

| Operation | String | StringBuffer | StringBuilder |
|-----------|--------|--------------|---------------|
| Concatenation (few operations) | Fast | Moderate | Fast |
| Multiple modifications | Slow (creates new objects) | Fast | Faster |
| Thread safety | Yes (immutable) | Yes | No |
| Memory usage | High (many objects) | Efficient | Efficient |

## Best Practices and Performance Considerations

1. **Use String literals** for constant values to benefit from string pooling
2. **Use StringBuilder** for multiple string manipulations in single-threaded environments
3. **Use StringBuffer** when thread safety is required
4. **Avoid concatenation in loops** with String class:

```java
// Inefficient
String result = "";
for (int i = 0; i < 1000; i++) {
    result += i; // Creates new string each time
}

// Efficient
StringBuilder builder = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    builder.append(i);
}
String result = builder.toString();
```

## Exam Tips

1. **Remember that strings are immutable** - operations like `concat()`, `substring()`, and `replace()` return new strings
2. **Understand the difference between `==` and `equals()`** - `==` checks reference equality, `equals()` checks content equality
3. **Know when to use StringBuffer vs StringBuilder** - StringBuffer for thread safety, StringBuilder for performance
4. **Be familiar with all string constructors** and when to use each type
5. **Practice character extraction methods** - `charAt()`, `getChars()`, `toCharArray()`
6. **Memorize the comparison methods table** - different methods serve different purposes
7. **Understand string pool concept** and how literal strings are managed
8. **Remember that `length()` is a method** for strings but a field for arrays