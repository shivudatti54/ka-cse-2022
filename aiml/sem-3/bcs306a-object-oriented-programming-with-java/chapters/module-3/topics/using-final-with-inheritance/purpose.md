# Learning Purpose: Using `final` with Inheritance

**1. Why is this topic important?**
Understanding the `final` keyword is crucial for designing robust and secure class hierarchies in Java. It allows developers to explicitly restrict inheritance and polymorphism, thereby enforcing design intent, preventing unintended modifications, and enhancing application stability. Mastering this concept is key to writing maintainable and secure object-oriented code.

**2. What will students learn?**
Students will learn to apply the `final` keyword to a class to prevent it from being extended (inherited from). They will also learn to apply `final` to a method to prevent it from being overridden in any subclass. This includes understanding the compile-time errors that occur when these rules are violated, reinforcing the concepts of access control and class design.

**3. How does it connect to other concepts?**
This topic builds directly upon core inheritance and polymorphism principles (Modules 1 & 2). It connects to access modifiers (`public`, `private`, `protected`) by adding another layer of control over a class's API. It is also a foundational concept for understanding immutable classes (like `String`), security, and frameworks that rely on a fixed structure.

**4. Real-world applications**
The `final` keyword is used extensively in the Java API itself; the `String` class is `final` for critical security and performance reasons. It is applied in library and framework design to create stable, reliable base classes that cannot be altered, ensuring consistent behavior. Developers use it to create immutable value objects and to define truly fixed constants.