# Modifying a String

## Introduction

In Java, strings are immutable objects - their values cannot be changed after creation. This fundamental characteristic makes string modification a critical concept requiring specialized techniques. When we perform operations that appear to modify strings, we're actually creating new string objects while the original remains unchanged.

Understanding string modification is essential for:

1. Writing memory-efficient applications
2. Optimizing performance in string-heavy operations
3. Choosing between String, StringBuilder, and StringBuffer classes
4. Preventing unintended object creation in loops

The art of string manipulation forms the foundation for advanced operations like pattern matching, data validation, and text processing in enterprise applications. Proper modification techniques become crucial when working with large datasets, network protocols, or user input processing.

## Key Concepts

### 1. String Immutability

- Once created, cannot be modified
- Every modification creates new object
- Original remains in string pool

```java
String s = "";
s.concat(" Belgaum"); // Returns new string " Belgaum"
System.out.println(s); // Still prints ""
```

### 2. Concatenation Methods

- `+` operator (compiler uses StringBuilder internally)
- `concat()` method
- `StringBuilder/Buffer` append()

**Memory Diagram:**

```
Original: "Hello" (hash 1234)
After concat: "Hello World" (hash 5678)
```

### 3. Substring Operations

```java
String original = "Advanced Java";
String sub = original.substring(0, 8); // "Advanced"
```

### 4. Replacement Methods

- `replace(char old, char new)`
- `replace(CharSequence target, CharSequence replacement)`

### 5. Case Modification

```java
String lower = "".toUpperCase(); // ""
String upper = "JAVA".toLowerCase(); // "java"
```

### 6. Trimming Whitespace

```java
String clean = " Data ".trim(); // "Data"
```

### 7. Value Conversion

```java
String num = String.valueOf(123); // "123"
String bool = String.valueOf(true); // "true"
```

## String vs StringBuilder vs StringBuffer

| Feature       | String        | StringBuilder      | StringBuffer      |
| ------------- | ------------- | ------------------ | ----------------- |
| Mutability    | Immutable     | Mutable            | Mutable           |
| Thread Safety | Yes           | No                 | Yes               |
| Performance   | Slow for mods | Fast               | Moderate          |
| Storage       | String Pool   | Heap               | Heap              |
| Best Use Case | Fixed values  | Single-thread mods | Multi-thread mods |

## Examples

### Example 1: Efficient Concatenation in Loops

**Problem:** Build a string with numbers 0-9999

**Bad Approach (String):**

```java
String result = "";
for(int i=0; i<10000; i++) {
 result += i; // Creates 10,000 objects!
}
```

**Good Approach (StringBuilder):**

```java
StringBuilder sb = new StringBuilder();
for(int i=0; i<10000; i++) {
 sb.append(i);
}
String result = sb.toString(); // Single object
```

**Performance Comparison:**

- String: O(n²) time complexity
- StringBuilder: O(n) time complexity

### Example 2: Complex Modification Chain

**Task:** Convert " Advanced Java 2022 " to "ADVANCED_JAVA_2022"

```java
String input = " Advanced Java 2022 ";

// Processing chain
String output = input.trim()
 .toUpperCase()
 .replace(' ', '_');

System.out.println(output); // ADVANCED_JAVA_2022
```

**Step Breakdown:**

1. `trim()`: Removes leading/trailing spaces → "Advanced Java 2022"
2. `toUpperCase()`: Converts to uppercase → "ADVANCED JAVA 2022"
3. `replace()`: Changes spaces to underscores → "ADVANCED_JAVA_2022"

### Example 3: StringBuffer in Multithreading

```java
StringBuffer buffer = new StringBuffer();

Runnable task = () -> {
 for(int i=0; i<100; i++) {
 buffer.append(Thread.currentThread().getId())
 .append(" ");
 }
};

Thread t1 = new Thread(task);
Thread t2 = new Thread(task);
t1.start();
t2.start();
t1.join();
t2.join();

System.out.println(buffer.length()); // 200 entries safely added
```

## Exam Tips

1. **Immutability First:** Always start answers by stating String's immutable nature
2. **Concatenation Cost:** For loop-based modifications, always recommend StringBuilder
3. **Method Chaining:** Use method chaining for multiple operations: `str.trim().toLowerCase().replace()`
4. **Thread Safety:** Use StringBuffer only when thread safety is explicitly required
5. **Substring Indexes:** Remember substring(endIndex) is exclusive: (0,3) → chars 0,1,2
6. **Empty vs Null:** `new String()` creates empty string (""), not null
7. **Pattern Question:** For "modify string" questions, always show both String and StringBuilder approaches with performance comparison

**Common Question Pattern:**
"Compare String and StringBuffer classes with example programs to demonstrate their usage in string modification."
_(Prepare 3 differences with code examples for each class)_
