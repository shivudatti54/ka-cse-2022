# Constructors and Destructors

## Introduction
Constructors and destructors are special member functions in C++ that manage object lifecycle. They are automatically invoked when objects are created and destroyed, ensuring proper initialization and cleanup of resources. These form essential components of object-oriented programming and are fundamental to the Delhi University BSc Physical Science (CS) NEP 2024 syllabus.

## Constructors

**Definition and Purpose**
- Special member functions with the same name as the class
- Automatically called when an object is created
- Initialize data members and allocate resources
- Have no return type (not even void)

**Types of Constructors**

- **Default Constructor**: Takes no parameters; provided automatically if no constructor defined
- **Parameterized Constructor**: Accepts arguments for initialization; enables object initialization with specific values
- **Copy Constructor**: Creates a new object as a copy of existing object; takes reference to same-type object as parameter
- **Conversion Constructor**: Single-argument constructor enables implicit type conversion
- **Constructor Overloading**: Multiple constructors with different parameter lists

**Key Features**
- Can be defined inside or outside the class
- Initialization lists provide efficient member initialization
- `explicit` keyword prevents implicit conversions

## Destructors

**Definition and Purpose**
- Special member function with tilde (~) prefix before class name
- Automatically invoked when object goes out of scope or is deleted
- Releases allocated resources, closes files, frees memory
- Cannot be overloaded—only one destructor per class

**Characteristics**
- No return type, no parameters
- Virtual destructors needed for base class pointers to derived objects
- Execution order: derived class destructor runs first, then base class

## Important Concepts

- **Rule of Three**: If a class needs destructor, it likely needs custom copy constructor and copy assignment operator
- **RAII (Resource Acquisition Is Initialization)**: Constructor acquires resources; destructor releases them
- **Dynamic Memory**: Classes using `new` should define destructor to prevent memory leaks

## Conclusion
Constructors and destructors are fundamental to C++ object management. Mastery of these concepts is essential for the Delhi University exam, as they form the basis for proper memory management, resource handling, and object-oriented design. Understanding when and how to implement different constructor types and destructors is crucial for writing robust C++ programs.

---
*Based on Delhi University BSc Physical Science (CS) NEP 2024 Syllabus*