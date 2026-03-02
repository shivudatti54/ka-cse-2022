# Creating a Multilevel Hierarchy

## Overview

A multilevel hierarchy in object-oriented programming is a structure where a subclass is also a superclass, creating multiple levels of inheritance. This allows for a more complex and nuanced representation of relationships between classes. In a multilevel hierarchy, a grandparent class is the topmost superclass, a parent class is both a subclass and a superclass, and a child class is the bottommost subclass.

## Key Points

- A multilevel hierarchy consists of at least three classes: a grandparent class, a parent class, and a child class.
- The grandparent class is the topmost superclass and has no parent class.
- The parent class is both a subclass of the grandparent class and a superclass of the child class.
- The child class is the bottommost subclass and has no subclass of its own.
- Multilevel hierarchies are useful for modeling complex relationships between classes.
- Inheritance is the mechanism by which a subclass inherits the properties and behavior of its superclass.
- A subclass can add new properties and behavior or override those inherited from its superclass.

## Important Definitions

- **Inheritance**: The mechanism by which a subclass inherits the properties and behavior of its superclass.
- **Superclass**: A class that is inherited from by another class.
- **Subclass**: A class that inherits from another class.

## Key Syntax

- `class ParentClass extends GrandparentClass { ... }`
- `class ChildClass extends ParentClass { ... }`

## Exam Tips

- Be able to identify and describe the relationships between classes in a multilevel hierarchy.
- Understand how inheritance works in a multilevel hierarchy and how subclasses can add new properties and behavior or override those inherited from their superclasses.
