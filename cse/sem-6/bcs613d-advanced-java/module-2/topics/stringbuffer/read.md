# StringBuffer and StringBuilder: Mastering Mutable Strings in Java

## Introduction to Mutable String Classes

In Java, while the `String` class provides immutable sequences of characters, there are scenarios where we need to modify strings efficiently without creating new objects repeatedly. This is where `StringBuffer` and `StringBuilder` classes come into play. Both classes create mutable sequences of characters, meaning they can be modified after creation without the overhead of creating new string objects.

**Key Concept**: Unlike `String` objects which are immutable (cannot be changed), `StringBuffer` and `StringBuilder` objects are mutable and can be modified through various methods.

## StringBuffer Class

### What is StringBuffer?

`StringBuffer` is a thread-safe, mutable sequence of characters. It was introduced in Java 1.0 and is designed for situations where multiple threads might be accessing the same string buffer simultaneously.

### Key Features of StringBuffer

1. **Mutable**: Content can be changed after creation
2. **Thread-safe**: All methods are synchronized
3. **Growable**: Automatically expands when needed
4. **Efficient**: Better performance than String for multiple modifications

### StringBuffer Constructors

```java
// Creates an empty StringBuffer with initial capacity of 16 characters
StringBuffer sb1 = new StringBuffer();

// Creates StringBuffer with specified initial capacity
StringBuffer sb2 = new StringBuffer(50);

// Creates StringBuffer with the same content as the specified String
StringBuffer sb3 = new StringBuffer("Hello");
```

### Important Methods of StringBuffer

#### 1. append() Method

Adds data to the end of the buffer

```java
StringBuffer sb = new StringBuffer("Hello");
sb.append(" World"); // "Hello World"
sb.append(123); // "Hello World123"
sb.append(3.14); // "Hello World1233.14"
```

#### 2. insert() Method

Inserts data at specified position

```java
StringBuffer sb = new StringBuffer("Hello World");
sb.insert(5, " Beautiful"); // "Hello Beautiful World"
sb.insert(0, "Start: "); // "Start: Hello Beautiful World"
```

#### 3. delete() and deleteCharAt() Methods

Remove characters from the buffer

```java
StringBuffer sb = new StringBuffer("Hello World");
sb.delete(5, 11); // "Hello"
sb.deleteCharAt(4); // "Hell"
```

#### 4. reverse() Method

Reverses the character sequence

```java
StringBuffer sb = new StringBuffer("Hello");
sb.reverse(); // "olleH"
```

#### 5. replace() Method

Replaces characters in specified range

```java
StringBuffer sb = new StringBuffer("Hello World");
sb.replace(6, 11, "Java"); // "Hello Java"
```

#### 6. capacity() and length() Methods

```java
StringBuffer sb = new StringBuffer(20);
System.out.println(sb.capacity()); // 20
System.out.println(sb.length()); // 0

sb.append("Hello");
System.out.println(sb.capacity()); // 20
System.out.println(sb.length()); // 5
```

### How StringBuffer Grows Internally

```
Initial State: [H][e][l][l][o][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ] (capacity: 16, length: 5)
After append(" World"): [H][e][l][l][o][ ][W][o][r][l][d][ ][ ][ ][ ][ ] (capacity: 16, length: 11)
After append(" Java"): New capacity = (current capacity + 1) * 2 = (16 + 1) * 2 = 34
```

## StringBuilder Class

### What is StringBuilder?

`StringBuilder` is a mutable sequence of characters introduced in Java 5. It's similar to `StringBuffer` but is not thread-safe, making it faster in single-threaded environments.

### Key Features of StringBuilder

1. **Mutable**: Like StringBuffer, content can be modified
2. **Not thread-safe**: No synchronized methods
3. **Faster**: Better performance than StringBuffer in single-threaded scenarios
4. **Same API**: Methods are identical to StringBuffer

### StringBuilder Constructors

```java
// Creates empty StringBuilder with initial capacity of 16
StringBuilder sb1 = new StringBuilder();

// Creates StringBuilder with specified capacity
StringBuilder sb2 = new StringBuilder(50);

// Creates StringBuilder with specified string content
StringBuilder sb3 = new StringBuilder("Hello");
```

## StringBuffer vs StringBuilder: Detailed Comparison

| Feature           | StringBuffer                  | StringBuilder                        |
| ----------------- | ----------------------------- | ------------------------------------ |
| **Thread Safety** | Synchronized (thread-safe)    | Not synchronized (not thread-safe)   |
| **Performance**   | Slower due to synchronization | Faster (no synchronization overhead) |
| **Introduced in** | Java 1.0                      | Java 5                               |
| **When to Use**   | Multi-threaded environments   | Single-threaded environments         |
| **Methods**       | All methods are synchronized  | No synchronized methods              |

### Performance Comparison Example

```java
// StringBuffer performance test
long startTime = System.currentTimeMillis();
StringBuffer sb = new StringBuffer();
for (int i = 0; i < 100000; i++) {
 sb.append("test");
}
long endTime = System.currentTimeMillis();
System.out.println("StringBuffer time: " + (endTime - startTime) + "ms");

// StringBuilder performance test
startTime = System.currentTimeMillis();
StringBuilder sbuild = new StringBuilder();
for (int i = 0; i < 100000; i++) {
 sbuild.append("test");
}
endTime = System.currentTimeMillis();
System.out.println("StringBuilder time: " + (endTime - startTime) + "ms");
```

## When to Use Which Class?

### Use String When:

- You need immutable strings
- String content won't change frequently
- Thread safety is required (String is inherently thread-safe)

### Use StringBuffer When:

- You need mutable strings in multi-threaded environments
- Multiple threads might modify the same string buffer
- Thread safety is more important than performance

### Use StringBuilder When:

- You need mutable strings in single-threaded environments
- Performance is critical
- No thread safety concerns

## Practical Examples and Use Cases

### Example 1: Building HTML Content

```java
public String buildHTMLTable(List<String> data) {
 StringBuilder html = new StringBuilder();
 html.append("<table>");
 for (String item : data) {
 html.append("<tr><td>").append(item).append("</td></tr>");
 }
 html.append("</table>");
 return html.toString();
}
```

### Example 2: Efficient String Manipulation

```java
public String processString(String input) {
 StringBuilder result = new StringBuilder();
 for (char c : input.toCharArray()) {
 if (Character.isLetter(c)) {
 result.append(Character.toUpperCase(c));
 }
 }
 return result.toString();
}
```

### Example 3: Multi-threaded String Building

```java
class SharedStringProcessor {
 private StringBuffer sharedBuffer = new StringBuffer();

 public synchronized void appendData(String data) {
 sharedBuffer.append(data);
 }

 public String getResult() {
 return sharedBuffer.toString();
 }
}
```

## Memory Management and Efficiency

### Capacity Management

Both `StringBuffer` and `StringBuilder` manage memory efficiently by:

1. Starting with an initial capacity
2. Automatically increasing capacity when needed
3. Using the formula: `new capacity = (old capacity + 1) * 2`

```java
StringBuilder sb = new StringBuilder(); // Initial capacity: 16
System.out.println(sb.capacity()); // 16

// When capacity is exceeded, it doubles
for (int i = 0; i < 20; i++) {
 sb.append("x");
}
System.out.println(sb.capacity()); // 34 (16+1)*2
```

### Avoiding Unnecessary Object Creation

Unlike String concatenation which creates multiple objects:

```java
// Inefficient - creates multiple String objects
String result = "";
for (int i = 0; i < 1000; i++) {
 result += i; // Creates new String each time
}

// Efficient - uses single StringBuilder
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
 sb.append(i); // Modifies existing object
}
String result = sb.toString();
```

## Method Chaining

Both classes support method chaining as most methods return `this`:

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello").append(" ").append("World").insert(5, ",").reverse();
System.out.println(sb.toString()); // "dlroW ,olleH"
```

## Conversion Between String and StringBuffer/StringBuilder

```java
// String to StringBuffer/StringBuilder
String str = "Hello";
StringBuffer sb = new StringBuffer(str);
StringBuilder sbuild = new StringBuilder(str);

// StringBuffer/StringBuilder to String
String result1 = sb.toString();
String result2 = sbuild.toString();
```

## Exam Tips

1. **Remember the key difference**: StringBuffer is synchronized (thread-safe), StringBuilder is not
2. **Performance**: StringBuilder is faster in single-threaded scenarios
3. **Method signatures**: Both have identical methods, but StringBuffer methods are synchronized
4. **Capacity vs Length**: capacity() returns total space, length() returns used space
5. **Use cases**: Use StringBuffer for multi-threading, StringBuilder for single-threading
6. **Memory efficiency**: Both are more efficient than String for multiple modifications
7. **Constructor parameters**: Can initialize with capacity, string, or default (16 characters)
