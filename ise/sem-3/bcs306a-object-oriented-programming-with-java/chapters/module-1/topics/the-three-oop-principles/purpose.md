# Learning Purpose: The Three OOP Principles

### 1. Why is this topic important?

Understanding encapsulation, inheritance, and polymorphism is fundamental to Java and Object-Oriented Programming (OOP). These principles are the blueprint for designing robust, scalable, and maintainable software. They promote code reusability, reduce complexity, and model real-world systems effectively, forming the core of modern software engineering.

### 2. What will students learn?

Students will learn to define and implement the three core OOP principles in Java:

- **Encapsulation:** Bundling data (variables) and methods that operate on that data into a single unit (a class), while restricting access via access modifiers (`private`, `public`).
- **Inheritance:** Creating new classes (subclasses) that derive properties and behaviors from existing classes (superclasses), enabling code reuse and establishing hierarchical relationships.
- **Polymorphism:** Allowing objects of different classes to be treated as objects of a common superclass, primarily through method overriding, enabling flexible and dynamic code.

### 3. How does it connect to other concepts?

This topic is the foundation for all subsequent OOP concepts. It directly connects to creating classes and objects (the building blocks), abstract classes and interfaces (which rely on inheritance and polymorphism), and design patterns, which are sophisticated applications of these principles to solve common design problems.

### 4. Real-world applications

These principles are used everywhere:

- **Encapsulation:** A `BankAccount` class hiding its balance data, exposing only `deposit()` and `withdraw()` methods.
- **Inheritance:** An `ElectricCar` class extending a base `Vehicle` class to inherit fields like `model` and methods like `accelerate()`.
- **Polymorphism:** A graphics program calling a `draw()` method on various `Shape` objects (e.g., `Circle`, `Square`), with each drawing itself correctly.
