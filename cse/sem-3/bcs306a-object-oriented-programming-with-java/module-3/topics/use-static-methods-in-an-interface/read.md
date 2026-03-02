# Use Static Methods in an Interface

## Table of Contents

- [Use Static Methods in an Interface](#use-static-methods-in-an-interface)
- [Introduction](#introduction)
- [What are Static Methods in Interfaces?](#what-are-static-methods-in-interfaces)
  - [Example: Defining a Static Method in an Interface](#example-defining-a-static-method-in-an-interface)
- [Key Differences between Static Methods, Default Methods, and Abstract Methods](#key-differences-between-static-methods-default-methods-and-abstract-methods)
- [Calling a Static Method in an Interface](#calling-a-static-method-in-an-interface)
  - [Example: Calling a Static Method in an Interface](#example-calling-a-static-method-in-an-interface)
- [Benefits of Using Static Methods in Interfaces](#benefits-of-using-static-methods-in-interfaces)
- [Use of Static Methods in Interfaces vs. Traditional Utility Classes](#use-of-static-methods-in-interfaces-vs-traditional-utility-classes)
- [Designing and Developing an Interface with a Static Method](#designing-and-developing-an-interface-with-a-static-method)
  - [Example: Designing an Interface with a Static Method](#example-designing-an-interface-with-a-static-method)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

Java 8 introduced the ability to define static methods in interfaces, allowing for more flexibility and utility in interface design. In this topic, we will explore the purpose and use of static methods in interfaces, their benefits, and how to define and call them.

## What are Static Methods in Interfaces?

---

Static methods in interfaces are used to provide a way to encapsulate utility methods that are related to the interface. These methods can be called without creating an instance of the interface. They are implicitly public and must have a body.

### Example: Defining a Static Method in an Interface

```java
public interface MyInterface {
 // Abstract method (implicitly public)
 void regularMethod();

 // Static method (must have a body)
 static void staticUtilityMethod() {
 System.out.println("This is a static utility method in the interface.");
 // Implementation logic here
 }
}
```

## Key Differences between Static Methods, Default Methods, and Abstract Methods

---

| Method Type     | Purpose                                        | Body Required | Instance Required |
| --------------- | ---------------------------------------------- | ------------- | ----------------- |
| Static Method   | Utility method related to the interface        | Yes           | No                |
| Default Method  | Provides a default implementation for a method | Yes           | Yes               |
| Abstract Method | Defines a contract for classes to implement    | No            | Yes               |

## Calling a Static Method in an Interface

---

Static methods in interfaces can be called using the interface name, without creating an instance.

### Example: Calling a Static Method in an Interface

```java
public class Main {
 public static void main(String[] args) {
 MyInterface.staticUtilityMethod();
 }
}
```

## Benefits of Using Static Methods in Interfaces

---

- Provides a way to encapsulate utility methods related to the interface
- Can be called without creating an instance of the interface
- Helps to promote cleaner, more cohesive code design

## Use of Static Methods in Interfaces vs. Traditional Utility Classes

---

| Approach                     | Benefits                                                                                             | Drawbacks                                           |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Static Methods in Interfaces | Provides a way to encapsulate utility methods related to the interface, promotes cleaner code design | Limited to utility methods related to the interface |
| Traditional Utility Classes  | Can contain any type of method, not limited to utility methods                                       | Can lead to tight coupling and cluttered code       |

## Designing and Developing an Interface with a Static Method

---

When designing an interface with a static method, consider the following:

- Identify the utility methods related to the interface
- Define the static method with a clear and concise name
- Ensure the static method is implicitly public and has a body
- Call the static method using the interface name

### Example: Designing an Interface with a Static Method

```java
public interface Validator {
 // Abstract method (implicitly public)
 boolean isValid(String input);

 // Static method (must have a body)
 static boolean isNullOrEmpty(String input) {
 return input == null || input.isEmpty();
 }
}

public class Main {
 public static void main(String[] args) {
 System.out.println(Validator.isNullOrEmpty("")); // true
 System.out.println(Validator.isNullOrEmpty("Hello")); // false
 }
}
```

## Exam Tips

---

- Be prepared to explain the purpose and use of static methods in interfaces
- Understand how to define and call static methods in interfaces
- Focus on the benefits of using static methods in interfaces, such as providing utility functions without requiring instance creation

## Key Takeaways

---

- Static methods in interfaces provide a way to encapsulate utility methods related to the interface
- Static methods can be called without creating an instance of the interface
- Use of static methods in interfaces promotes cleaner, more cohesive code design
- Consider the benefits and drawbacks of using static methods in interfaces vs. traditional utility classes when designing your code.
