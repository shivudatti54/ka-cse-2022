# **Chapter 8 Summary**

### Inheritance Basics

- Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class.
- The class that is being inherited from is called the **superclass** or **parent class**, while the class that is doing the inheriting is called the **subclass** or **child class**.
- The keyword used to specify inheritance in Java is **extends**.

### Using super

- The **super** keyword is used to access the superclass members (methods and variables) in the subclass.
- The **super** keyword can also be used to call the superclass constructor from the subclass constructor.

### Creating a Multilevel Hierarchy

- A multilevel hierarchy is a classification of classes where a subclass of a subclass inherits its properties and behavior.
- To create a multilevel hierarchy, a subclass can extend another subclass.

### When Constructors Are Invoked

- In a multilevel hierarchy, the constructor of the superclass is called before the constructor of the subclass.
- The constructor of the subclass can also call the constructor of the superclass using the **super** keyword.

### Key Points

- Inheritance allows one class to inherit the properties and behavior of another class.
- The **super** keyword is used to access superclass members and call the superclass constructor.
- A multilevel hierarchy can be created by subclassing a subclass.

### Important Formulas and Definitions

- Definition: Inheritance - a fundamental concept in OOP that allows one class to inherit the properties and behavior of another class.
- Formula: `class Subclass extends Superclass { ... }`

### Important Theorems

- Theorem: In a multilevel hierarchy, the constructor of the superclass is called before the constructor of the subclass.

Note: These notes are concise and to the point, covering the key points and important concepts for quick revision before exams.
