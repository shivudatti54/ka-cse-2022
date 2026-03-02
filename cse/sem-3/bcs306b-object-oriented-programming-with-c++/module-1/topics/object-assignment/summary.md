# Object Assignment in C++ - Summary

## Key Definitions and Concepts

- **Object Assignment**: The process of copying the contents of one object to another using the assignment operator (=)

- **Default Assignment Operator**: C++ provides a built-in assignment operator that performs member-wise (shallow) copy of all data members

- **Copy Constructor**: Special constructor called when a new object is created from an existing object

- **Assignment Operator**: Operator called when assigning to an already existing object

- **Shallow Copy**: Copies pointer addresses rather than the actual data pointed to

- **Deep Copy**: Allocates new memory and copies actual data, ensuring independent copies

## Important Formulas and Theorems

- **Assignment Operator Signature**: `ClassName& operator=(const ClassName& obj)`

- **Rule of Three**: If a class requires any of destructor, copy constructor, or copy assignment operator, it likely requires all three

- **Return Type**: Assignment operators should return a reference to enable chaining: `return *this`

- **Self-Assignment Check**: `if (this != &obj)` prevents unnecessary work and potential data corruption

## Key Points

- Default assignment operator performs shallow copy, which can cause issues with pointer members

- Copy constructor is invoked with syntax like `Class obj2 = obj1;` or `Class obj2(obj1);`

- Assignment operator is invoked with syntax like `obj2 = obj1;` when obj2 already exists

- Always check for self-assignment before performing deep copy operations

- The assignment operator must return `*this` to support chained assignments like `a = b = c`

- Classes managing dynamic memory (new/delete) require custom assignment operators for proper deep copying

- Copy constructor and assignment operator have different use cases but similar implementation logic

## Common Mistakes to Avoid

1. Forgetting to check for self-assignment, which can cause crashes when deleting and reallocating memory

2. Implementing only shallow copy for classes with pointer members, leading to double-free errors

3. Confusing copy constructor with assignment operator - remember copy constructor creates new objects

4. Not freeing old memory before allocating new memory in assignment operator, causing memory leaks

5. Forgetting to implement the Rule of Three when dealing with resource-managing classes

## Revision Tips

1. Practice writing complete classes with proper constructors, destructors, and assignment operators

2. Draw memory diagrams to visualize shallow vs deep copy behavior

3. Remember the key difference: copy constructor = new object, assignment operator = existing object

4. Always use self-assignment check as the first line in assignment operator body for deep copy classes

5. Review previous university exam questions on this topic to understand the question patterns
