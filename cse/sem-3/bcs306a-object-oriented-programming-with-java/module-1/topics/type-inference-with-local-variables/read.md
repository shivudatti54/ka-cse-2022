# Type Inference with Local Variables (var keyword) in Java

## Table of Contents

- [Type Inference with Local Variables (var keyword) in Java](#type-inference-with-local-variables-var-keyword-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [What is Type Inference?](#what-is-type-inference)
  - [Rules for Using var](#rules-for-using-var)
  - [Lambdas and var](#lambdas-and-var)
  - [Limitations of var](#limitations-of-var)
- [Examples](#examples)
  - [Example 1: Basic Type Inference](#example-1-basic-type-inference)
  - [Example 2: Working with Collections](#example-2-working-with-collections)
  - [Example 3: Complex Type Inference with Methods](#example-3-complex-type-inference-with-methods)
- [Exam Tips](#exam-tips)

## Introduction

Type inference is one of the most significant features introduced in Java 10, revolutionizing how developers declare local variables. Prior to Java 10, developers were required to explicitly specify the type of every variable during declaration, which sometimes led to verbose code, especially with complex generic types. The `var` keyword was introduced as part of Java 10 to enable local variable type inference, allowing the compiler to automatically infer the type of a variable from its initializer expression.

This feature represents a paradigm shift in Java programming, drawing inspiration from languages like Python, JavaScript, and Kotlin that already employed similar mechanisms. The introduction of `var` does not make Java a dynamically typed language; rather, it maintains Java's strong static typing while reducing boilerplate code. At compile time, the Java compiler analyzes the right-hand side of the assignment and determines the appropriate type, which is then fixed for the entire scope of the variable.

Understanding type inference is crucial for modern Java development, as it improves code readability, reduces redundancy, and aligns Java with contemporary programming practices. For students preparing for examinations, a thorough understanding of `var` is essential, as questions on this topic frequently appear in both theory and practical examinations.

## Key Concepts

### What is Type Inference?

Type inference is the ability of the compiler to automatically determine the data type of a variable based on the value being assigned to it. In Java 10 and later versions, the `var` keyword can be used in place of a concrete type declaration for local variables. When the compiler encounters `var`, it examines the initializer expression on the right side and infers the most appropriate type.

For example, when you write `var x = 10;`, the compiler infers that `x` is of type `int`. Similarly, `var name = "John";` infers `String`, and `var list = new ArrayList<String>();` infers `ArrayList<String>`. The inferred type is permanent and cannot be changed throughout the variable's scope.

### Rules for Using var

The Java Language Specification (JLS) defines strict rules for using `var`:

1. **Initializer is Mandatory**: The variable must be initialized at the time of declaration. You cannot declare `var x;` without an initializer, as the compiler has nothing to infer the type from.

2. **Only for Local Variables**: `var` can only be used for local variables (variables declared inside methods, constructors, or initializer blocks). It cannot be used for instance variables, method parameters, or return types.

3. **Null Initialization Not Allowed**: You cannot initialize a `var` variable with `null` because the compiler cannot infer the type from a null value. For example, `var x = null;` will result in a compilation error.

4. **Not a Keyword**: `var` is not a reserved keyword in Java. This means you can still use `var` as an identifier name for variables, methods, or classes without breaking existing code. However, using `var` as an identifier is discouraged for clarity.

5. **Works with Diamond Operator**: When using the diamond operator `<>` with generics, `var` can infer the type from the context. For example, `var list = new ArrayList<>();` will create an `ArrayList<Object>` in Java 10, but in Java 11 and later, it can infer from the assignment context.

6. **Cannot be Used with Multiple Variables**: You cannot declare multiple variables in a single statement using `var`. For example, `var a = 1, b = 2;` is invalid.

### Lambdas and var

In Java 11, the use of `var` was extended to lambda parameters. This allows developers to add type annotations to lambda parameters when needed. For example:

```java
// Without var
Function<String, Integer> f = s -> s.length();

// With var (to add annotations)
Function<String, Integer> f = (@NonNull var s) -> s.length();
```

### Limitations of var

Understanding where `var` cannot be used is equally important:

- Cannot be used for field declarations
- Cannot be used for method parameter types
- Cannot be used for return types of methods
- Cannot be used in compound declarations
- Cannot be used without initialization
- Cannot be used with arrays (in some contexts)
- Cannot be used when the initializer is a poly expression that could have multiple target types

## Examples

### Example 1: Basic Type Inference

Consider a scenario where we need to calculate the area and circumference of a circle:

```java
public class CircleDemo {
 public static void main(String[] args) {
 // Using explicit types
 double radius = 5.5;
 double area = Math.PI * radius * radius;
 double circumference = 2 * Math.PI * radius;

 System.out.println("Radius: " + radius);
 System.out.println("Area: " + area);
 System.out.println("Circumference: " + circumference);

 // Using var (equivalent)
 var r = 5.5;
 var circleArea = Math.PI * r * r;
 var circum = 2 * Math.PI * r;

 System.out.println("Radius: " + r);
 System.out.println("Area: " + circleArea);
 System.out.println("Circumference: " + circum);
 }
}
```

In the `var` version, the compiler infers:

- `r` → `double`
- `circleArea` → `double`
- `circum` → `double`

### Example 2: Working with Collections

```java
import java.util.*;

public class CollectionDemo {
 public static void main(String[] args) {
 // Creating a List with explicit type
 List<String> names = new ArrayList<String>();
 names.add("Alice");
 names.add("Bob");

 // Using var with diamond operator (Java 10)
 var namesList = new ArrayList<String>();
 namesList.add("Charlie");
 namesList.add("David");

 // Iterating using var in for-each loop
 for (var name : namesList) {
 System.out.println("Name: " + name + ", Length: " + name.length());
 }

 // Using var with Map
 var studentMap = new HashMap<Integer, String>();
 studentMap.put(1, "Emma");
 studentMap.put(2, "Frank");

 // Iterating over Map entries
 for (var entry : studentMap.entrySet()) {
 System.out.println("ID: " + entry.getKey() + ", Name: " + entry.getValue());
 }
 }
}
```

### Example 3: Complex Type Inference with Methods

```java
import java.util.stream.*;

public class StreamDemo {
 public static void main(String[] args) {
 var numbers = Arrays.asList(10, 20, 30, 40, 50);

 // Using var with streams
 var sum = numbers.stream()
 .filter(n -> n > 25)
 .mapToInt(Integer::intValue)
 .sum();

 System.out.println("Sum of numbers > 25: " + sum);

 // Using var for result of method chaining
 var doubledList = numbers.stream()
 .map(n -> n * 2)
 .collect(Collectors.toList());

 // The inferred type of doubledList is List<Integer>
 System.out.println("Doubled: " + doubledList);

 // Using var with custom objects
 var person = new Person("John", 25);
 System.out.println("Person: " + person.getName() + ", Age: " + person.getAge());
 }
}

class Person {
 private String name;
 private int age;

 public Person(String name, int age) {
 this.name = name;
 this.age = age;
 }

 public String getName() { return name; }
 public int getAge() { return age; }
}
```

## Exam Tips

1. **Remember the Core Rule**: The `var` keyword requires an initializer at the time of declaration. This is the most frequently tested concept in university examinations.

2. **Scope of var**: Always remember that `var` can only be used for local variables inside methods, constructors, or initializer blocks. It cannot be used for instance variables.

3. **Not Dynamically Typed**: Despite using `var`, Java remains statically typed. The type is inferred at compile time and cannot change during runtime.

4. **Avoid Ambiguous Cases**: In expressions where the target type is ambiguous, avoid using `var`. For example, `var x = "hello";` works, but be cautious with complex generic expressions.

5. **Practical Advantage**: Understand that `var` reduces code verbosity without sacrificing type safety. This is an important conceptual point for theory questions.

6. **Null and var**: Remember that `var` cannot be initialized to `null`. This often appears as a trick question in examinations.

7. **Backward Compatibility**: Since `var` is not a reserved keyword, existing Java code using `var` as an identifier continues to work without modification.

8. **Diamond Operator with var**: In Java 10, `var list = new ArrayList<>();` creates `ArrayList<Object>`, while in Java 11+, it can infer types more accurately when context provides additional type information.

9. **Lambda Parameter Enhancement**: Java 11 introduced the ability to use `var` in lambda parameters to add annotations. This is a nuanced point that may appear in advanced questions.

10. **Code Readability**: While `var` reduces boilerplate, excessive use can make code harder to understand. The recommendation is to use `var` when the type is obvious from the right-hand side.
