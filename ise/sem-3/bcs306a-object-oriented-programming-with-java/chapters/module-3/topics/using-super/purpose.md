### Learning Purpose: Using `super`

**1. Why is this topic important?**
The `super` keyword is a fundamental mechanism in Java for achieving code reusability and establishing a clear hierarchy between classes. It is essential for implementing inheritance correctly, preventing code duplication, and ensuring that parent class constructors and overridden methods are utilized properly. Mastering `super` is crucial for building well-organized, maintainable, and bug-free object-oriented applications.

**2. What will students learn?**
Students will learn the two primary uses of the `super` keyword:

- **To call a superclass constructor:** They will understand how to use `super()` to initialize the inherited state of an object from within a subclass constructor.
- **To access superclass members:** They will learn how to use `super.method()` to call an overridden method from the parent class, allowing them to extend functionality rather than replace it entirely.

**3. How does it connect to other concepts?**
This topic is a direct application of **inheritance** (Module 2). It is impossible to build robust class hierarchies without `super`. It also connects closely with **method overriding** and **constructors**. Understanding `super` provides a foundation for later concepts like polymorphism, where the relationship between subclass and superclass methods is key.

**4. Real-world applications**
`super` is used whenever a class extends another. For example, a `SavingsAccount` subclass would use `super(accountNumber, balance)` to call the `BankAccount` constructor before adding its own specific features. In GUI development, a custom panel might use `super.paintComponent(g)` to ensure the parent class's drawing routine runs before adding its own custom graphics.
