# Class Fundamentals - Summary

## Key Definitions and Concepts

- **Class**: A user-defined data type that serves as a blueprint/template for creating objects. It encapsulates data (fields) and behavior (methods).

- **Object**: An instance of a class, created using the `new` keyword that allocates memory on the heap and calls a constructor.

- **Instance Variables**: Variables declared inside a class but outside any method. Each object has its own copy, representing the state of the object.

- **Class Variables**: Variables declared with the `static` keyword, shared among all instances of the class. Only one copy exists regardless of object count.

- **Methods**: Functions defined inside a class that describe the behavior of objects. Can be instance methods or static methods.

- **Encapsulation**: An OOP principle that bundles data and methods together while restricting direct access to some components using access modifiers.

- **Access Modifiers**: Keywords (public, private, protected, default) that control the visibility of class members.

## Important Formulas and Theorems

- Object creation syntax: `ClassName objectRef = new ConstructorName(arguments);`

- Static member access: `ClassName.staticMember` (without creating any object)

- Memory allocation: Instance variables allocated per object on heap; static variables allocated in method area shared across objects

## Key Points

- A class contains fields (data), constructors (initialization), and methods (behavior)

- Private fields with public getters/setters exemplify encapsulation

- The `this` keyword refers to the current object and resolves naming conflicts

- Static members belong to the class, not to individual objects

- Constructors have the same name as the class and no return type

- Multiple constructors can exist through constructor overloading

- Default values are assigned to instance variables automatically if not explicitly initialized

## Common Mistakes to Avoid

- Confusing instance variables with static variables and using them incorrectly

- Forgetting to initialize local variables before use (compilation error)

- Attempting to access instance members from static contexts like main()

- Using instance variable names as parameter names without using `this` keyword

- Creating objects without using `new` keyword (results in compilation error)

## Revision Tips

- Practice writing complete class definitions from scratch to reinforce syntax

- Draw memory diagrams showing how objects and static variables are stored

- Solve previous year DU exam questions on class definitions and object creation

- Remember the rule: static methods cannot access instance data directly

- Focus on encapsulation and proper access modifier selection in code