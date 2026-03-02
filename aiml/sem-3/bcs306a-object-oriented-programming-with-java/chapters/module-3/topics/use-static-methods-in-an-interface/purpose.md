### Module 3: Use static Methods in an Interface

#### 1. Why is this topic important?
This topic is crucial as it modernizes the design of interfaces, a core pillar of object-oriented programming (OOP). Prior to Java 8, interfaces could only declare abstract methods, limiting their utility. Understanding static methods allows students to write more organized, utility-focused code directly within interfaces, reducing the need for separate utility classes and promoting better software design practices.

#### 2. What will students learn?
Students will learn the syntax and rules for defining `static` methods inside a Java interface. They will understand that these methods belong to the interface itself and are called using the interface name (e.g., `InterfaceName.staticMethod()`). Crucially, they will learn that static methods are not inherited by implementing classes, which differentiates them from default methods and prevents potential method conflicts in the inheritance hierarchy.

#### 3. How does it connect to other concepts?
This concept builds directly on knowledge of interfaces, abstract methods, and the `static` keyword learned with classes. It contrasts with `default` methods, which are instance methods provided by the interface. This feature is a key part of the evolution of Java interfaces towards becoming more complete abstract types, working in tandem with lambda expressions and streams introduced in later modules.

#### 4. Real-world applications
Static methods in interfaces are widely used to create helper or utility functions logically grouped with the interface. For example, an `EmailValidator` interface could contain a static `isValid(String email)` method to perform validation without requiring an instance. The Java API itself uses this, such as the `Comparator.comparing()` method, which provides a convenient, static way to create comparator instances.