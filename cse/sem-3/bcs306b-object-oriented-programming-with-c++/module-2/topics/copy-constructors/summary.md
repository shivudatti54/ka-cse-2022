# Copy Constructors - Summary

## Key Definitions and Concepts

- **Copy Constructor**: A special constructor that creates a new object as a copy of an existing object of the same class, taking a const reference parameter.
- **Shallow Copy**: Default copy behavior where pointer values are copied (both objects share the same memory).
- **Deep Copy**: User-defined copy where new memory is allocated and actual data is copied (each object has independent memory).
- **Memberwise Copy**: The default copying mechanism where each member variable is copied directly.

## Important Formulas and Concepts

```cpp
// Copy constructor syntax
ClassName(const ClassName& obj);
```

- Copy constructor is called during object initialization: `ClassName obj2 = obj1;` or `ClassName obj2(obj1);`
- Copy constructor is called when passing objects by value to functions
- Copy constructor is called when returning objects by value from functions

## Key Points

1. The parameter of a copy constructor must be a reference to avoid infinite recursion.

2. Always use const reference to allow copying from both const and non-const objects.

3. Default copy constructor performs shallow copy, which is dangerous for classes with pointer members.

4. Classes managing dynamic memory, files, or other resources need user-defined copy constructors for deep copy.

5. Copy constructor is different from assignment operator: one creates new objects, the other modifies existing ones.

6. The Rule of Three states: if you define any of destructor, copy constructor, or assignment operator, define all three.

7. Copy constructor is invoked when initializing an object from another existing object.

8. Making copy constructor private prevents object copying.

9. In inheritance, derived class copy constructor must explicitly call base class copy constructor.

10. C++11 provides delete specifier to disable copy constructor: `ClassName(const ClassName&) = delete;`

## Common Mistakes to Avoid

- Forgetting to implement copy constructor for classes with pointer members, leading to shallow copy bugs
- Not using const reference parameter, which causes compilation errors or inefficient passing
- Confusing copy constructor with assignment operator
- Forgetting to allocate new memory in deep copy constructor
- Not handling destructor properly after implementing deep copy

## Revision Tips

1. Practice writing copy constructors for classes with various member types (primitive, pointer, reference).

2. Trace through code examples to understand when copy constructor is called vs assignment operator.

3. Remember the Rule of Three as a checklist for any class with resource management.

4. Understand the difference between pass-by-value and pass-by-reference and their impact on copy constructor invocation.

5. Review the difference between shallow and deep copy with memory diagrams.
