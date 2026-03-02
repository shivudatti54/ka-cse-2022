# **Inheritance Basics in Java**

## **Definitions and Theorems**

- **Inheritance**: A mechanism in Java where one class can inherit the properties and behavior of another class.
- **Superclass** (Parent Class): The class being inherited from.
- **Subclass** (Child Class): The class that inherits from the superclass.
- **Hiding**: Inheritance in Java is not true inheritance, but rather hiding of fields and methods from the superclass.

## **Key Points**

- **Using the Super Keyword**:
  - Access super class members using `super` keyword.
  - Constructor call: `super(parameters)`
  - Method call: `super.methodName(parameters)`
- **Multilevel Hierarchy**:
  - A subclass can inherit from another subclass.
  - A nested class can inherit from an outer class.
- **Constructors**:
  - In a subclass, a constructor must call the superclass constructor using `super(parameters)`.
  - If no superclass constructor is called, the default constructor is used.

## **Important Formulas and Concepts**

- **Inheritance Chain**: The sequence of inheritance from a superclass to a subclass.
- **Method Overriding**: A subclass provides a different implementation of a method that is already defined in its superclass.

## **Key Terms**

- **Polymorphism**: The ability of an object to take on multiple forms.
- **Encapsulation**: The concept of bundling data and methods that operate on that data within a single unit.

## **Quick Revision Tips**

- Focus on understanding the concepts of inheritance, super keyword, super class, and methods.
- Practice creating simple class hierarchies and constructors.
- Review method overriding and polymorphism concepts.
