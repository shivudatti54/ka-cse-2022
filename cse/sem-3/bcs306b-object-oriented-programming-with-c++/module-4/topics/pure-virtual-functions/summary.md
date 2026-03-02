# Pure Virtual Functions - Summary

## Key Definitions and Concepts

- **Pure Virtual Function**: A virtual function declared with `= 0` syntax that has no implementation in the base class. Syntax: `virtual return_type function_name() = 0;`
- **Abstract Class**: A class containing at least one pure virtual function; cannot be instantiated but can serve as a base class
- **Interface Class**: An abstract class with only pure virtual functions and no data members; defines a contract without implementation

## Important Formulas and Theorems

There are no specific formulas for pure virtual functions, but the key syntax pattern is:

```cpp
virtual void functionName() = 0;
```

## Key Points

1. Pure virtual functions force derived classes to provide implementations, creating a contract
2. Classes with pure virtual functions become abstract and cannot be instantiated
3. Abstract classes can still contain concrete (implemented) methods alongside pure virtual functions
4. Virtual destructors are essential when using polymorphism to ensure proper cleanup
5. Pointers and references to abstract classes enable runtime polymorphism through the vtable
6. A derived class that doesn't implement all pure virtual functions remains abstract
7. Pure virtual functions can have default implementations in modern C++ (C++11+), but the class remains abstract

## Common Mistakes to Avoid

- Forgetting to mark the base class destructor as virtual when using polymorphism
- Attempting to instantiate an abstract class directly
- Not implementing all pure virtual functions in a concrete derived class
- Using `= 0` with non-virtual functions (causes compilation error)
- Calling pure virtual functions from constructor (leads to undefined behavior)

## Revision Tips

1. Practice writing abstract class hierarchies with pure virtual functions
2. Remember the `= 0` syntax is unique to declaring pure virtual functions
3. Focus on understanding when and why to use abstract classes vs concrete base classes
4. Review the difference between interface classes and abstract classes with partial implementation
5. Understand the relationship between pure virtual functions and runtime polymorphism
