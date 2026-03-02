# Constructors and Destructors - Summary

## Key Definitions and Concepts

- **Constructor**: A special member function called automatically when an object is created to initialize member variables. Same name as class, no return type.
- **Destructor**: A special member function called automatically when an object is destroyed. Same name as class preceded by ~, takes no parameters, cannot be overloaded.
- **Copy Constructor**: Creates a new object as a copy of an existing object. Invoked during pass-by-value, return-by-value, and object initialization.
- **Initialization List**: A colon-separated list used to initialize member variables before the constructor body executes, essential for const and reference members.
- **Virtual Destructor**: A destructor marked virtual to ensure proper cleanup of derived class objects through base class pointers.

## Important Formulas and Theorems

- **Constructor Syntax**: `ClassName(parameters) { body }`
- **Destructor Syntax**: `~ClassName() { body }`
- **Copy Constructor Syntax**: `ClassName(const ClassName& obj) { body }`
- **Order of Destruction**: Reverse of construction order - derived class destructors run before base class destructors; members are destroyed in reverse declaration order.

## Key Points

- Constructors can be overloaded; destructors cannot be overloaded
- The compiler provides a default constructor only if no constructor is explicitly defined
- Copy constructors perform shallow copy by default; deep copy requires custom implementation
- Initialization lists are more efficient than assignment in constructor bodies
- Always use virtual destructors in polymorphic base classes
- The `explicit` keyword prevents implicit conversions for single-parameter constructors
- Private constructors are used in Singleton pattern and factory methods
- Constructors can call other constructors (delegating constructors in C++11)
- Destructors should never throw exceptions

## Common Mistakes to Avoid

1. **Forgetting to define a destructor** when class manages dynamic memory, leading to memory leaks
2. **Not making base class destructors virtual** when using polymorphism, causing incomplete cleanup
3. **Using assignment instead of initialization lists** for const and reference members, causing compilation errors
4. **Implementing shallow copy** for classes with pointer members, causing double deletion problems
5. **Defining constructor return types** (even void), which makes them regular methods, not constructors

## Revision Tips

- Practice writing all types of constructors (default, parameterized, copy) for the same class
- Trace through code to understand when copy constructors are invoked
- Remember: Constructors build up (base → derived), destructors tear down (derived → base)
- Create classes with dynamic memory allocation to master destructor usage
- Review previous year DU examination questions on this topic for pattern recognition
- Use debugging tools to observe constructor/destructor call sequences