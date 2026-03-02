# **Copy Constructors**

### Definition and Purpose

- A copy constructor is a special member function of a class that creates a copy of an existing object.
- Its purpose is to copy the contents of one object to another, without modifying the original object.

### Key Points

- A copy constructor has the same name as the class, followed by an underscore and the parameter name `const Type&` (where `Type` is the class type).
- The copy constructor is used to create a copy of an object when passing it to a function by value, or when returning it from a function.
- The copy constructor is also used to copy an object to another object of the same class.

### Important Formulas and Definitions

- **Copy Constructor Formula**: `Class(const Class& other) { /* copy constructor implementation */ }`
- **Rule of Five**: "If you see any of these five things, you're wrong. Don't make that mistake again."
  - Default constructor
  - Copy constructor
  - Move constructor
  - Copy assignment operator
  - Move assignment operator

### Theorems and Principles

- **Copy Constructor Theorem**: "If `Class A` and `Class B` are two classes with a common base class `Base`, then `A(const A)` and `B(const B)` are valid copy constructors."
- **Copy Constructor Principle**: "A copy constructor should only copy the public and protected members of the class, not the private members."

### Example Use Cases

- Passing an object to a function by value: `myObject.copyFunction(myObject);`
- Returning an object from a function: `return myObject;`
- Copying an object to another object of the same class: `myObject2 = myObject;`

### Important C++ Concepts

- **Scope Resolution Operator**: `::` (used to access class members outside their scope)
- **Member Access Operator**: `.` (used to access class members within their scope)
- **Const Correctness**: using `const` keywords to ensure that objects are not modified unnecessarily.
