# Static Class Members - Summary

## Key Definitions and Concepts

- **Static Data Member:** A class variable shared by all objects of the class, having only one copy in memory regardless of the number of objects created.

- **Static Member Function:** A function that belongs to the class rather than to any object, callable without creating an instance of the class.

- **Static Initialization:** The process of defining and providing initial value to static members outside the class (required for most static members).

## Important Formulas and Theorems

- Static members follow the single-copy principle: `sizeof(class)` excludes static members.
- Static member initialization: `ReturnType ClassName::staticMember = value;`
- Static function call syntax: `ClassName::functionName()` or `object.functionName()`

## Key Points

- Static data members are allocated in the data segment, not on object stack
- There is only one copy of a static member shared by all class objects
- Static member functions cannot access non-static (instance) members directly
- Static member functions do not have a 'this' pointer
- Static members can be accessed using both object name and class name with scope resolution operator
- Static data members are initialized to zero by default if not explicitly initialized
- Since C++11, const static data members can be initialized inside the class
- Static member functions cannot be virtual, const, or volatile

## Common Mistakes to Avoid

- Forgetting to define static members outside the class (causes linker error)
- Trying to access non-static members from static member functions
- Initializing static members in constructor (each object gets separate copy in constructor)
- Confusing static with const - they are different concepts
- Using 'this' pointer in static member functions (not available)

## Revision Tips

1. Practice writing complete programs with static members to reinforce the concept
2. Remember the syntax: declaration inside class, definition outside class
3. Focus on what static functions CANNOT do (access non-static members, use 'this')
4. Understand the difference between class-level and object-level data
5. Review previous university question papers for pattern of questions on this topic
