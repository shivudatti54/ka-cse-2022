# Introducing Methods


## Table of Contents

- [Introducing Methods](#introducing-methods)
- [Overview of Methods](#overview-of-methods)
- [Basic Structure of a Method](#basic-structure-of-a-method)
  - [Access Modifiers](#access-modifiers)
  - [Non-Access Modifiers](#non-access-modifiers)
  - [Return Type](#return-type)
  - [Method Name](#method-name)
  - [Parameter List](#parameter-list)
- [Types of Methods](#types-of-methods)
  - [Void Methods](#void-methods)
  - [Value-Returning Methods](#value-returning-methods)
- [Method Invocation](#method-invocation)
- [Argument Passing](#argument-passing)
  - [Pass-by-Value](#pass-by-value)
  - [Pass-by-Reference](#pass-by-reference)
- [Benefits of Using Methods](#benefits-of-using-methods)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Overview of Methods

---

Methods in Java are blocks of code that perform a specific task and can be called multiple times from different parts of a program. They are used to organize and reuse code, making it more efficient and easier to maintain.

## Basic Structure of a Method

---

A method in Java has the following basic structure:

```java
access_modifier non_access_modifier return_type method_name (parameter_list) {
 // method body - code to be executed
}
```

### Access Modifiers

Access modifiers control the visibility of a method. There are three types of access modifiers:

- `public`: The method can be accessed from any class.
- `private`: The method can only be accessed within the same class.
- `protected`: The method can be accessed within the same class and by subclasses.

### Non-Access Modifiers

Non-access modifiers provide additional information about a method's behavior. Some common non-access modifiers include:

- `static`: The method belongs to the class, not an instance of the class.
- `final`: The method cannot be overridden by subclasses.
- `abstract`: The method is declared without an implementation and must be implemented by subclasses.

### Return Type

The return type specifies the data type of the value returned by a method. If a method does not return a value, the return type is `void`.

### Method Name

The method name is a unique identifier for the method. It should be descriptive and follow the standard Java naming conventions.

### Parameter List

The parameter list defines the input parameters of a method. Parameters are variables that are passed to the method when it is called.

## Types of Methods

---

There are two main types of methods in Java:

### Void Methods

Void methods do not return a value. They are used to perform a task that does not require returning a value.

```java
public void printHello() {
 System.out.println("Hello");
}
```

### Value-Returning Methods

Value-returning methods return a value. They are used to perform a task that requires returning a value.

```java
public int add(int a, int b) {
 return a + b;
}
```

## Method Invocation

---

A method can be invoked by calling its name followed by parentheses containing the required parameters.

```java
public class MyClass {
 public void printHello() {
 System.out.println("Hello");
 }

 public static void main(String[] args) {
 MyClass obj = new MyClass();
 obj.printHello(); // invokes the printHello method
 }
}
```

## Argument Passing

---

Arguments can be passed to a method using the parameter list. There are two ways to pass arguments:

### Pass-by-Value

Pass-by-value involves passing a copy of the original value. Changes made to the parameter do not affect the original value.

```java
public class MyClass {
 public void increment(int x) {
 x = x + 1;
 }

 public static void main(String[] args) {
 MyClass obj = new MyClass();
 int a = 5;
 obj.increment(a);
 System.out.println(a); // prints 5
 }
}
```

### Pass-by-Reference

Pass-by-reference involves passing a reference to the original value. Changes made to the parameter affect the original value.

```java
public class MyClass {
 public void increment(int[] x) {
 x[0] = x[0] + 1;
 }

 public static void main(String[] args) {
 MyClass obj = new MyClass();
 int[] a = {5};
 obj.increment(a);
 System.out.println(a[0]); // prints 6
 }
}
```

## Benefits of Using Methods

---

Methods provide several benefits, including:

- **Code Reusability**: Methods can be called multiple times from different parts of a program, reducing code duplication.
- **Code Organization**: Methods help to organize code into logical blocks, making it easier to understand and maintain.
- **Encapsulation**: Methods can be used to encapsulate data and behavior, making it harder for other parts of the program to access or modify them directly.

## Exam Tips

---

- Be prepared to identify and explain the different components of a method declaration.
- Understand the purpose and behavior of access and non-access modifiers in method declarations.
- Be able to write simple methods with parameters and return values, and demonstrate their invocation and usage.
- Understand the difference between pass-by-value and pass-by-reference in method argument passing, and be able to explain the implications of each approach.

## Key Takeaways

---

- Methods are blocks of code that perform a specific task and can be called multiple times from different parts of a program.
- Methods have various components, including access modifiers, non-access modifiers, return types, method names, and parameter lists.
- Methods can be used to organize and reuse code, making it more efficient and easier to maintain.
- Methods provide several benefits, including code reusability, code organization, and encapsulation.
