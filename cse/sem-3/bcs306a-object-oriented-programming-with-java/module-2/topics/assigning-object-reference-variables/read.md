# Assigning Object Reference Variables in Java

## Table of Contents

- [Assigning Object Reference Variables in Java](#assigning-object-reference-variables-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding References vs Objects](#understanding-references-vs-objects)
  - [Assignment of Reference Variables](#assignment-of-reference-variables)
  - [Reference Comparison: == vs equals()](#reference-comparison--vs-equals)
  - [Shallow Copy vs Deep Copy](#shallow-copy-vs-deep-copy)
  - [The this Reference](#the-this-reference)
  - [Passing References to Methods](#passing-references-to-methods)
- [Examples](#examples)
  - [Example 1: Demonstrating Reference Assignment](#example-1-demonstrating-reference-assignment)
  - [Example 2: Creating Independent Copies](#example-2-creating-independent-copies)
  - [Example 3: Passing References to Methods](#example-3-passing-references-to-methods)
- [Exam Tips](#exam-tips)

## Introduction

In Java, understanding how object reference variables work is fundamental to mastering object-oriented programming. Unlike primitive data types where variables hold actual values, object variables store **references** (memory addresses) to objects stored in the heap memory. When we assign one reference variable to another, we are not creating a new object but rather making two variables point to the same object in memory. This concept is crucial for writing efficient Java programs and avoiding common pitfalls related to object aliasing, memory management, and program behavior.

The assignment of object reference variables forms the backbone of many Java operations, from simple variable assignments to complex data structures like linked lists and trees. Understanding this topic helps programmers comprehend how changes to one variable affect another, when objects become eligible for garbage collection, and how to design programs that avoid unintended side effects. In the context of the university's OOP with Java curriculum, this topic appears in Module 2 and is essential for building strong programming foundations.

## Key Concepts

### Understanding References vs Objects

In Java, when you declare a class variable, you are creating a reference variable that can point to an object of that class. The actual object resides in the heap memory, while the variable holds a reference (essentially a pointer) to that memory location. Consider this example:

```java
class Box {
 int width;
 int height;
}

Box b1 = new Box(); // Creates object in heap, b1 holds reference
Box b2 = b1; // b2 now points to the SAME object as b1
```

In this case, both `b1` and `b2` reference the same object in memory. Any modifications through `b1` will be visible through `b2` and vice versa.

### Assignment of Reference Variables

The assignment operator (`=`) when used with reference variables copies the reference, not the object itself. This creates an **alias** or **aliasing** - two different reference variables pointing to the same object. This is fundamentally different from creating a copy of the object. The implications are significant:

- Changes made through either reference affect the same underlying object
- There is still only one object in memory
- Both references can be used interchangeably to access the object

### Reference Comparison: == vs equals()

When comparing objects, we must distinguish between reference comparison and content comparison. The `==` operator compares whether two references point to the same memory location (same object). The `equals()` method, when properly overridden, compares whether two objects have equivalent content. For String comparison, Java provides this distinction explicitly.

### Shallow Copy vs Deep Copy

When you need an actual copy of an object (not just another reference), you must create a new object and copy the field values:

**Shallow Copy**: Copies the primitive values and copies the references of objects. If an object contains references to other objects, those references are copied but the referenced objects are shared.

**Deep Copy**: Creates a complete independent copy including all objects referenced within the original object. No shared references exist between original and copy.

### The this Reference

The `this` keyword is a reference variable that refers to the current object. It is automatically available to all non-static methods and can be used to:

- Differentiate between instance variables and parameters with the same name
- Pass the current object as an argument to other methods
- Invoke one constructor from another constructor (constructor chaining)

### Passing References to Methods

When passing objects to methods, Java passes references by value. This means the method receives a copy of the reference, not the reference itself. However, since it's a copy of the reference pointing to the same object, the method can modify the object's state. However, the method cannot make the caller's reference point to a different object.

## Examples

### Example 1: Demonstrating Reference Assignment

```java
class Student {
 String name;
 int marks;

 Student(String n, int m) {
 name = n;
 marks = m;
 }
}

public class ReferenceDemo {
 public static void main(String[] args) {
 Student s1 = new Student("Rahul", 85);
 Student s2 = s1; // Reference assignment - both point to same object

 System.out.println("Before modification:");
 System.out.println("s1.name: " + s1.name);
 System.out.println("s2.name: " + s2.name);

 // Modify through s2
 s2.name = "Priya";

 System.out.println("\nAfter modifying through s2:");
 System.out.println("s1.name: " + s1.name); // Will print "Priya"
 System.out.println("s2.name: " + s2.name); // Will print "Priya"

 System.out.println("\ns1 == s2: " + (s1 == s2)); // true
 }
}
```

**Output:**

```
Before modification:
s1.name: Rahul
s2.name: Rahul

After modifying through s2:
s1.name: Priya
s2.name: Priya

s1 == s2: true
```

This demonstrates that after reference assignment, both variables point to the same object in memory.

### Example 2: Creating Independent Copies

```java
class Point {
 int x, y;

 Point(int x, int y) {
 this.x = x;
 this.y = y;
 }

 // Method to create a deep copy
 Point copy() {
 return new Point(this.x, this.y);
 }
}

public class CopyDemo {
 public static void main(String[] args) {
 Point p1 = new Point(10, 20);
 Point p2 = p1; // Reference copy - same object
 Point p3 = p1.copy(); // New independent object

 System.out.println("Original: p1(" + p1.x + ", " + p1.y + ")");
 System.out.println("Reference: p2(" + p2.x + ", " + p2.y + ")");
 System.out.println("Copy: p3(" + p3.x + ", " + p3.y + ")");

 p1.x = 100;

 System.out.println("\nAfter modifying p1.x to 100:");
 System.out.println("p1.x = " + p1.x);
 System.out.println("p2.x = " + p2.x + " (affected - same object)");
 System.out.println("p3.x = " + p3.x + " (unchanged - independent copy)");
 }
}
```

### Example 3: Passing References to Methods

```java
class Account {
 int balance = 1000;
}

public class PassByReferenceDemo {

 static void modifyBalance(Account acc, int amount) {
 acc.balance += amount; // Modifies the object's state
 acc = new Account(); // Only modifies local copy of reference
 acc.balance = 5000; // This doesn't affect caller's reference
 }

 public static void main(String[] args) {
 Account myAccount = new Account();
 System.out.println("Before: " + myAccount.balance);

 modifyBalance(myAccount, 500);
 System.out.println("After: " + myAccount.balance); // Prints 1500
 }
}
```

## Exam Tips

1. **Remember: Object variables store references, not objects** - This is the fundamental concept that explains all reference assignment behavior in Java.

2. **Assignment (=) copies references, not objects** - When you write `obj2 = obj1`, both variables point to the same object in heap memory.

3. **Use == for reference comparison, equals() for content comparison** - Unless overridden, equals() behaves like == (compares references).

4. **The this keyword always refers to the current object** - It cannot be reassigned and is automatically available in instance methods.

5. **Pass-by-value for references** - Methods receive a copy of the reference; they cannot reassign the caller's reference but can modify the object's state.

6. **Shallow copy shares nested objects** - If your class contains references to other objects, a shallow copy will share those references.

7. **Create deep copies explicitly** - You must manually create new objects for all nested objects if you want complete independence.

8. **Garbage collection eligibility** - When reference variables are reassigned, the original object may become eligible for garbage collection if no references remain.

9. **String objects are immutable** - When you "modify" a String, you actually create a new String object; this is a special case in Java.

10. **Distinguish between declaring, creating, and assigning** - These are three distinct operations: `Box b;` (declaration), `b = new Box();` (creation and assignment), `Box c = b;` (reference assignment).
