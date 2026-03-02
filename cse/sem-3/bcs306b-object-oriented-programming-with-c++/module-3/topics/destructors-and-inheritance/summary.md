# Destructors and Inheritance - Summary

## Key Definitions and Concepts

- **Destructor**: A special member function that performs cleanup when an object is destroyed; has the same name as the class preceded by ~
- **Virtual Destructor**: A destructor declared with virtual keyword, enabling polymorphic deletion through base class pointers
- **Pure Virtual Destructor**: A virtual destructor with = 0 specifier that still requires an implementation
- **Polymorphic Deletion**: Deleting derived class objects through base class pointers

## Important Formulas and Theorems

- **Order of Destructor Execution**: Derived class destructor → Members of derived → Base class destructor → Members of base (reverse of construction)
- **Virtual Destructor Rule**: Base class destructor must be virtual when derived objects may be deleted through base class pointers

## Key Points

- Destructors have no return type, no parameters, and cannot be overloaded
- Constructors run from base to derived; destructors run in reverse order
- Non-virtual destructors in polymorphic scenarios cause undefined behavior and memory leaks
- Virtual destructors add vtable overhead but are essential for correct cleanup
- Pure virtual destructors must have an implementation (function body)
- Destructors are automatically invoked when objects go out of scope or delete is called
- Static objects are destroyed after main() ends in reverse construction order

## Common Mistakes to Avoid

- Forgetting to make base class destructor virtual when using polymorphism
- Using delete instead of delete[] for dynamically allocated arrays
- Not releasing dynamically allocated memory in destructors, causing leaks
- Assuming destructor of derived class will automatically call base class destructor without virtual keyword
- Defining a pure virtual destructor without providing implementation

## Revision Tips

1. Always visualize constructor and destructor call order: base → derived (constructors), derived → base (destructors)
2. Remember: "Virtual for delete" - if you delete through base pointer, make destructor virtual
3. Practice identifying memory leaks in code where base pointer deletes derived object
4. Remember that virtual keyword in base makes all derived destructors virtual automatically
