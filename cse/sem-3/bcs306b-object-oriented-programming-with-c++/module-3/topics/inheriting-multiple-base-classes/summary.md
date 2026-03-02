# Multiple Inheritance in C++ - Summary

## Key Definitions and Concepts

- **Multiple Inheritance**: A feature where a derived class inherits from two or more base classes, combining properties from different class hierarchies.
- **Diamond Problem**: An ambiguity that occurs when a class inherits from two classes that share a common base, creating duplicate subobjects.
- **Virtual Inheritance**: A technique using the `virtual` keyword to ensure only one instance of a common base class exists in the most derived object.
- **Ambiguity Resolution**: Using the scope resolution operator (::) to explicitly specify which base class member to access when name conflicts occur.

## Important Formulas and Theorems

- **Constructor Execution Order**: Virtual base classes → Direct non-virtual base classes (in declaration order) → Most derived class constructor.
- **Destructor Execution Order**: Reverse of constructor execution - most derived class first, then base classes in reverse declaration order.
- **Virtual Base Initialization**: Only the most derived class initializes virtual base classes; intermediate classes cannot initialize them.

## Key Points

- Multiple inheritance syntax: `class Derived : public Base1, public Base2 { };`
- Each base class can have independent access specifier (public, protected, private).
- Base class constructors are called in the order of declaration in the inheritance list.
- Ambiguous members must be qualified with class name using the :: operator.
- Virtual inheritance solves diamond problem by ensuring single shared base subobject.
- With virtual inheritance, the most derived class must initialize the virtual base class.
- Non-virtual diamond creates two separate base class subobjects causing duplication and ambiguity.

## Common Mistakes to Avoid

- Forgetting that non-virtual diamond inheritance creates duplicate base subobjects.
- Attempting to initialize virtual base classes in intermediate class constructors (only most derived can do this).
- Not resolving ambiguity when base classes have members with the same name.
- Assuming constructor order follows the initializer list order (it follows declaration order).
- Using multiple inheritance when composition would be more appropriate.

## Revision Tips

- Practice drawing inheritance diagrams for various multiple inheritance scenarios.
- Trace through constructor/destructor calls for different inheritance patterns.
- Remember: virtual base constructors execute first and only once, regardless of number of inheritance paths.
- For exam questions, always draw the inheritance hierarchy first to visualize relationships.
- Focus on the difference between virtual and non-virtual inheritance and their effects on object structure.
