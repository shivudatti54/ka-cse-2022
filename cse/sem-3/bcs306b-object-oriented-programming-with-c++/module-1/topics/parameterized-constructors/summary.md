# Parameterized Constructors - Summary

## Key Definitions and Concepts

- **Parameterized Constructor**: A constructor that accepts arguments to initialize data members with specific values at object creation time. It has the same name as the class but no return type.

- **Constructor Overloading**: Multiple constructors in a class with different parameter lists, allowing flexible object initialization through various means.

- **Copy Constructor**: A special constructor that takes a reference to another object of the same class, creating a new object as a copy. Essential for deep copying objects with pointer members.

- **Initialization List**: A colon-separated list following the constructor's parameter list that directly initializes data members, preferred for const and reference members.

## Important Formulas and Theorems

- **Constructor Syntax**: `ClassName(parameters) { // initialization code }`

- **Copy Constructor Syntax**: `ClassName(const ClassName &obj) { // copy members }`

- **Initialization List Syntax**: `ClassName(params) : member1(val1), member2(val2) { }`

- **Rule of Three**: If a class requires a custom destructor, copy constructor, or copy assignment operator, it likely needs all three (extended to Rule of Five in modern C++).

## Key Points

- Constructors are automatically invoked when objects are created and cannot return values.

- Constructor overloading enables multiple initialization patterns for the same class.

- Default arguments in constructors reduce the need for multiple overloaded versions.

- Initialization lists are more efficient than assignment in constructor bodies.

- The copy constructor is called when objects are passed by value, returned by value, or explicitly copied.

- For classes with pointer members, shallow copy (default) can cause memory issues; custom deep copy constructor is required.

- The `explicit` keyword prevents unintended implicit type conversions via constructors.

- Data members are initialized in declaration order, regardless of initialization list order.

## Common Mistakes to Avoid

1. **Forgetting to implement copy constructor for pointer members** - Leads to shallow copy issues, double-free errors, and undefined behavior.

2. **Using assignment instead of initialization for const members** - Const members must be initialized in the initialization list.

3. **Mismatching initialization list order with member declaration order** - Can lead to subtle bugs as initialization happens in declaration order.

4. **Not providing any constructor when default initialization is needed** - If you define any constructor, the default constructor is not automatically provided.

5. **Returning values from constructors** - Constructors cannot have a return type, not even void.

## Revision Tips

1. Practice writing classes with multiple constructors to understand overloading clearly.

2. Always implement deep copy constructors when your class uses dynamic memory allocation.

3. Remember that const data members and references MUST be initialized via initialization lists.

4. Understand the difference between initialization and assignment: initialize in initialization list, assign in constructor body.

5. Review previous university question papers to understand the exam pattern and common questions on this topic.
