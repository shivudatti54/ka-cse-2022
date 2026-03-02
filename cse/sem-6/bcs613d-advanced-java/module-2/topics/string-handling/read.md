# String Handling in Java

## Introduction to Strings in Java

A **String** in Java is an object that represents a sequence of characters. Strings are one of the most commonly used classes in Java programming, essential for handling text data. Unlike primitive data types, String is a class in the `java.lang` package.

```java
String greeting = "Hello, World!";
String name = "Alice";
```

## Key Characteristics of Java Strings

| Property            | Description                                         |
| ------------------- | --------------------------------------------------- |
| **Immutable**       | Once created, string content cannot be changed      |
| **Object Type**     | String is a class, not a primitive type             |
| **String Pool**     | Literal strings are stored in a special memory area |
| **Thread-Safe**     | Immutability makes strings inherently thread-safe   |
| **Character Array** | Internally represented as `char[]` array            |

## String Creation Methods

### Method 1: Using String Literals

```java
String str1 = "Hello";
String str2 = "Hello"; // References same object in string pool

// Both reference the same object in memory
System.out.println(str1 == str2); // true
```

### Method 2: Using `new` Keyword

```java
String str1 = new String("Hello");
String str2 = new String("Hello"); // Creates new object

// Different objects in heap memory
System.out.println(str1 == str2); // false
System.out.println(str1.equals(str2)); // true
```

### Method 3: From Character Array

```java
char[] charArray = {'H', 'e', 'l', 'l', 'o'};
String str = new String(charArray);
System.out.println(str); // Hello
```

### Method 4: From Byte Array

```java
byte[] byteArray = {72, 101, 108, 108, 111};
String str = new String(byteArray);
System.out.println(str); // Hello
```

## String Immutability

Strings in Java are **immutable**, meaning their content cannot be modified after creation. Any operation that appears to modify a string actually creates a new string object.

```java
String original = "Hello";
String modified = original.concat(" World");

System.out.println(original); // Hello (unchanged)
System.out.println(modified); // Hello World (new object)
```

### Why Are Strings Immutable?

1. **String Pool Optimization**: Allows multiple references to share same object
2. **Security**: Prevents unauthorized modification of sensitive data
3. **Thread Safety**: No synchronization needed for read operations
4. **Hashcode Caching**: Hashcode can be cached and reused

## String Comparison

### Using `==` Operator (Reference Comparison)

```java
String str1 = "Hello";
String str2 = "Hello";
String str3 = new String("Hello");

System.out.println(str1 == str2); // true (same reference in pool)
System.out.println(str1 == str3); // false (different objects)
```

### Using `equals()` Method (Content Comparison)

```java
String str1 = "Hello";
String str2 = new String("Hello");

System.out.println(str1.equals(str2)); // true (same content)
```

### Using `equalsIgnoreCase()` Method

```java
String str1 = "Hello";
String str2 = "hello";

System.out.println(str1.equals(str2)); // false
System.out.println(str1.equalsIgnoreCase(str2)); // true
```

### Using `compareTo()` Method

```java
String str1 = "Apple";
String str2 = "Banana";

int result = str1.compareTo(str2);
// Returns: negative if str1 < str2, 0 if equal, positive if str1 > str2

System.out.println(result); // Negative value (Apple comes before Banana)
```

## Common String Methods

### Length and Character Access

```java
String str = "Hello World";

// Get length
int length = str.length(); // 11

// Get character at index
char ch = str.charAt(0); // 'H'
char lastChar = str.charAt(str.length() - 1); // 'd'
```

### Case Conversion

```java
String str = "Hello World";

String upper = str.toUpperCase(); // "HELLO WORLD"
String lower = str.toLowerCase(); // "hello world"
```

### Substring Extraction

```java
String str = "Hello World";

String sub1 = str.substring(0, 5); // "Hello"
String sub2 = str.substring(6); // "World"
String sub3 = str.substring(6, 11); // "World"
```

### String Searching

```java
String str = "Hello World";

// Check if string contains substring
boolean contains = str.contains("World"); // true

// Find index of character/substring
int index1 = str.indexOf('o'); // 4 (first occurrence)
int index2 = str.lastIndexOf('o'); // 7 (last occurrence)
int index3 = str.indexOf("World"); // 6

// Check start and end
boolean starts = str.startsWith("Hello"); // true
boolean ends = str.endsWith("World"); // true
```

### String Trimming and Stripping

```java
String str = " Hello World ";

String trimmed = str.trim(); // "Hello World" (removes leading/trailing spaces)
String stripped = str.strip(); // "Hello World" (Java 11+, better Unicode support)

// Remove only leading or trailing whitespace (Java 11+)
String leadStripped = str.stripLeading(); // "Hello World "
String tailStripped = str.stripTrailing(); // " Hello World"
```

### String Replacement

```java
String str = "Hello World";

String replaced1 = str.replace('o', '0'); // "Hell0 W0rld"
String replaced2 = str.replace("World", "Java"); // "Hello Java"
String replaced3 = str.replaceAll("l+", "L"); // "HeLo WorLd" (regex)
String replaced4 = str.replaceFirst("l", "L"); // "HeLlo World"
```

### String Splitting

```java
String str = "apple,banana,orange,grape";

String[] fruits = str.split(",");
// fruits[0] = "apple"
// fruits[1] = "banana"
// fruits[2] = "orange"
// fruits[3] = "grape"

// Split with limit
String[] limited = str.split(",", 2);
// limited[0] = "apple"
// limited[1] = "banana,orange,grape"
```

### String Joining

```java
// Using String.join() (Java 8+)
String joined = String.join(", ", "apple", "banana", "orange");
System.out.println(joined); // "apple, banana, orange"

// Joining array
String[] fruits = {"apple", "banana", "orange"};
String result = String.join(" | ", fruits);
System.out.println(result); // "apple | banana | orange"
```

## String Concatenation

### Using `+` Operator

```java
String str1 = "Hello";
String str2 = "World";
String result = str1 + " " + str2; // "Hello World"

// Concatenation with other types
String msg = "Count: " + 10; // "Count: 10"
```

### Using `concat()` Method

```java
String str1 = "Hello";
String str2 = str1.concat(" World");
System.out.println(str2); // "Hello World"
```

### Using StringBuilder (Efficient for Multiple Concatenations)

```java
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" ");
sb.append("World");
String result = sb.toString(); // "Hello World"
```

## String Conversion Methods

### Converting to String

```java
// From int
int num = 123;
String str1 = String.valueOf(num); // "123"
String str2 = Integer.toString(num); // "123"

// From double
double d = 3.14;
String str3 = String.valueOf(d); // "3.14"

// From boolean
boolean b = true;
String str4 = String.valueOf(b); // "true"

// From char array
char[] chars = {'H', 'e', 'l', 'l', 'o'};
String str5 = String.valueOf(chars); // "Hello"
```

### Converting from String

```java
String str = "123";

// To int
int num = Integer.parseInt(str); // 123

// To double
String dStr = "3.14";
double d = Double.parseDouble(dStr); // 3.14

// To boolean
String bStr = "true";
boolean b = Boolean.parseBoolean(bStr); // true
```

## String Pool and Intern

### String Pool

String pool is a special memory area in Java heap where string literals are stored. This helps optimize memory by reusing immutable string objects.

```java
String str1 = "Hello"; // Created in string pool
String str2 = "Hello"; // Reuses same object from pool

System.out.println(str1 == str2); // true
```

### intern() Method

The `intern()` method adds a string to the pool or returns reference if already present.

```java
String str1 = new String("Hello"); // Created in heap
String str2 = "Hello"; // In string pool

System.out.println(str1 == str2); // false

String str3 = str1.intern(); // Returns reference from pool
System.out.println(str3 == str2); // true
```

## Practical Examples

### Example 1: Email Validation

```java
public class EmailValidator {
 public static boolean isValidEmail(String email) {
 if (email == null || email.isEmpty()) {
 return false;
 }

 // Simple validation
 return email.contains("@") &&
 email.indexOf("@") > 0 &&
 email.indexOf("@") < email.length() - 1;
 }

 public static void main(String[] args) {
 System.out.println(isValidEmail("test@example.com")); // true
 System.out.println(isValidEmail("invalid")); // false
 System.out.println(isValidEmail("@example.com")); // false
 }
}
```

### Example 2: Word Count

```java
public class WordCounter {
 public static int countWords(String text) {
 if (text == null || text.trim().isEmpty()) {
 return 0;
 }

 String[] words = text.trim().split("\\s+");
 return words.length;
 }

 public static void main(String[] args) {
 String text = "Hello World from Java";
 System.out.println("Word count: " + countWords(text)); // 4
 }
}
```

### Example 3: Palindrome Checker

```java
public class PalindromeChecker {
 public static boolean isPalindrome(String str) {
 if (str == null) {
 return false;
 }

 // Remove spaces and convert to lowercase
 String cleaned = str.replaceAll("\\s+", "").toLowerCase();

 // Compare with reversed string
 String reversed = new StringBuilder(cleaned).reverse().toString();
 return cleaned.equals(reversed);
 }

 public static void main(String[] args) {
 System.out.println(isPalindrome("racecar")); // true
 System.out.println(isPalindrome("hello")); // false
 System.out.println(isPalindrome("A man a plan a canal Panama")); // true
 }
}
```

## Performance Considerations

### String vs StringBuilder vs StringBuffer

```java
// Inefficient: Creates multiple String objects
String result = "";
for (int i = 0; i < 1000; i++) {
 result += i; // Creates new String object each time
}

// Efficient: Uses StringBuilder
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
 sb.append(i);
}
String result = sb.toString();
```

## Exam Tips

1. **String Immutability**: Remember strings are immutable - operations create new objects
2. **equals() vs ==**: Use `equals()` for content comparison, `==` for reference comparison
3. **String Pool**: Literal strings are stored in string pool for reuse
4. **Index Range**: Valid indices are 0 to length()-1
5. **Common Methods**: Master charAt(), substring(), indexOf(), replace(), split()
6. **Performance**: Use StringBuilder for multiple concatenations
7. **Null Safety**: Always check for null before calling string methods
8. **Case Sensitivity**: Remember equals() is case-sensitive; use equalsIgnoreCase() when needed

## Further Reading

For more information on Java String handling, StringBuilder, StringBuffer, and advanced string manipulation techniques, refer to the official Java API documentation.
