# **Chapter 8 Revision Notes: Object Oriented Programming with JAVA**

## **Inheritance Basics**

- Inheritance is a mechanism that allows one class to inherit properties and behavior from another class.
- The class that inherits is called the **subclass** or **derived class**, and the class from which it inherits is called the **superclass** or **base class**.
- The subclass can have its own properties and behavior, as well as inherit those of the superclass.

## **Using the `super` Keyword**

- The `super` keyword is used to access the members of the superclass.
- It can be used to call the superclass's constructors, methods, and variables.
- Example: `super.methodName();`

## **Creating a Multilevel Hierarchy**

- A multilevel hierarchy is a type of inheritance where a class inherits from another class, and that class also inherits from a third class.
- Example: `public class Animal { ... }`, `public class Mammal extends Animal { ... }`, `public class Dog extends Mammal { ... }`

## **Constructors and Initialization**

- A constructor is a special method in a class that is used to initialize objects of that class.
- In a subclass, the constructor can call the superclass's constructor using the `super` keyword.
- Example: `public class Animal { public Animal() { ... } }`, `public class Mammal extends Animal { public Mammal() { super(); ... } }`

## **Important Formulas and Definitions**

- **Inheritance Formula:** `public class Subclass extends Superclass { ... }`
- **Multilevel Inheritance Formula:** `public class Subclass extends Superclass { ... }`, `public class Subsubclass extends Subclass { ... }`
- **Constructor Formula:** `public class Subclass extends Superclass { public Subclass() { super(); ... } }`

## **Important Theorems**

- **Inheritance Theorem:** A subclass inherits all the properties and behavior of its superclass.
- **Multilevel Inheritance Theorem:** A subclass inherits the properties and behavior of its superclass, and also inherits from another subclass.
