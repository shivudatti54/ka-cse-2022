# When Constructors and Destructors Are Executed - Summary

## Key Definitions and Concepts

- **Constructor:** Special member function called automatically when an object is created to initialize the object
- **Destructor:** Special member function called automatically when an object is destroyed to perform cleanup
- **Global Objects:** Declared outside any function, constructed before `main()`, destroyed after `main()` ends
- **Local Objects:** Created within function scope, destroyed when function/block exits
- **Static Objects:** Constructed once, destroyed when program terminates
- **Dynamic Objects:** Created with `new`, destroyed with `delete`

## Important Formulas and Theorems

- **Reverse Order Rule:** Destructors execute in the exact reverse order of constructors (LIFO)
- **Inheritance Order:** Base class constructors → Derived class constructors; Derived class destructors → Base class destructors
- **Member Order:** Member objects are constructed in declaration order within the class
- **Virtual Base Classes:** Called before non-virtual base classes, only once per inheritance hierarchy

## Key Points

1. Global objects are constructed before `main()` and destroyed after `main()` completes

2. Local objects are destroyed when they go out of scope, in reverse order of construction

3. Static local objects are constructed only once on first function call

4. Base class constructors execute before derived class constructors in inheritance

5. Member objects are constructed before the containing class constructor (in declaration order)

6. Virtual base classes are constructed before direct non-virtual base classes

7. Use `virtual` destructors for polymorphic base classes to ensure proper cleanup

8. Always match `new` with `delete` and `new[]` with `delete[]`

9. Objects in arrays are destroyed in reverse order (last element first)

10. Static objects are destroyed in reverse order of construction after `main()` ends

## Common Mistakes to Avoid

1. Not using virtual destructors in polymorphic classes - leads to undefined behavior

2. Using `delete` instead of `delete[]` for arrays - destructor called only for first element

3. Assuming constructor order follows initializer list order (it follows declaration order)

4. Forgetting to call `delete` for dynamically allocated objects - causes memory leaks

5. Returning references to local objects - object is destroyed after function returns

## Revision Tips

1. Draw execution timeline diagrams for different scenarios to visualize object lifecycle

2. Practice tracing constructor/destructor sequences for various inheritance combinations

3. Remember the mnemonic: "Construction walks in, Destruction walks out" - constructors proceed forward, destructors reverse

4. For university exams, focus on predicting output questions involving object creation and destruction sequences

5. Always verify base class has virtual destructor when using inheritance with pointers
