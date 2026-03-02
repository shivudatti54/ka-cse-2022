# Assigning Object Reference Variables - Summary

## Key Definitions and Concepts

- **Reference Variable**: A variable that holds the memory address of an object rather than the object itself
- **Object Assignment**: Copying a reference from one variable to another, creating two variables pointing to the same object
- **Aliasing**: When two or more reference variables point to the same object in memory
- **Shallow Copy**: Copying object references without creating new instances of referenced objects
- **Deep Copy**: Creating completely independent copies including all nested objects
- **this Reference**: Implicit reference to the current object within instance methods

## Important Formulas and Theorems

- When `obj2 = obj1` is executed, `obj1 == obj2` evaluates to **true**
- Java uses **pass-by-value** for all arguments; for object references, the value (address) is copied
- An object becomes eligible for garbage collection when **zero references** point to it

## Key Points

- Object variables in Java store references (memory addresses), not actual objects
- The assignment operator copies references, creating aliases to the same object
- Changes through any reference affect the single shared object
- The == operator compares memory addresses; equals() compares object content (when overridden)
- Shallow copy shares nested objects; deep copy creates independent nested objects
- The `this` keyword provides access to the current object from within instance methods
- Methods receive copies of references, allowing object state modification but not reference reassignment
- String is immutable in Java, so seemingly "modifying" a String actually creates a new object

## Common Mistakes to Avoid

1. Assuming that assignment creates a new object copy instead of a reference copy
2. Confusing == (reference comparison) with equals() (content comparison) unless equals() is overridden
3. Thinking that passing an object to a method creates a copy of the object
4. Believing that reassigning a parameter reference inside a method affects the caller's reference

## Revision Tips

1. Draw memory diagrams showing how references point to objects in the heap
2. Practice by writing code that creates objects, assigns references, and prints results
3. Remember the golden rule: assignment (=) with objects copies references, not objects
4. For exam questions, always trace through each line and identify what references point to what objects
5. Review String behavior - understand why String appears to behave differently due to immutability
