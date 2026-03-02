# **Inheritance Basics in Java**

## **Key Points**

- Inheritance is a mechanism in Java where one class can inherit the properties and behavior of another class.
- The class that is being inherited from is called the **superclass** or **parent class**.
- The class that is doing the inheriting is called the **subclass** or **child class**.
- The subclass inherits all the fields and methods of the superclass.
- The subclass can also add new fields and methods or override the ones inherited from the superclass.
- The `super` keyword is used to access the superclass's fields and methods.
- The constructor of the subclass can be used to initialize the superclass's fields.

## **Types of Inheritance**

- **Single Inheritance**: One subclass inherits from one superclass.
- **Multiple Inheritance**: One subclass can inherit from multiple superclasses.
- **Multilevel Inheritance**: A subclass inherits from a superclass, which itself inherits from another superclass.
- **Hierarchical Inheritance**: Multiple subclasses inherit from a single superclass.

## **Constructors and Initialization**

- The constructor of the subclass can be used to initialize the superclass's fields.
- The `super()` keyword is used to call the superclass's constructor.
- If a subclass does not explicitly call the superclass's constructor, the compiler will insert a call to the superclass's no-arg constructor.

## **Important Formulas and Definitions**

- **Inheritance Factor**: The ratio of the number of classes in the inheritance hierarchy to the number of classes in the superclass.
- **Polymorphism**: The ability of an object to take on multiple forms.

## **Key Theorems**

- **The Inheritance Theorem**: If A inherits from B, and C inherits from B, then A is-a C.
- **The Polymorphism Theorem**: If A is-a B, and C is-a B, then A is-a C.
