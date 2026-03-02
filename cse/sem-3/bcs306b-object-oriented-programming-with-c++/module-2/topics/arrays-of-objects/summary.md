# Arrays of Objects - Summary

## Key Definitions and Concepts

- **Array of Objects:** A collection of multiple objects of the same class stored in contiguous memory locations, accessed using subscript notation.

- **Default Constructor Requirement:** When creating arrays of objects, a default constructor (either explicitly defined or implicitly provided) must exist; otherwise compilation fails.

- **'this' Pointer:** An implicit pointer available within member functions that points to the specific object being operated on.

## Important Formulas and Theorems

- **Declaration Syntax:** `ClassName arrayName[arraySize];`

- **Accessing Members:** `objectArray[index].memberFunction()`

- **Dynamic Array Creation:** `ClassName *ptr = new ClassName[size];`

- **Memory Deallocation:** `delete[] ptr;`

- **Constructor Invocation:** For array of n objects, default constructor is called n times.

## Key Points

- Arrays of objects combine array indexing with OOP principles, enabling organized storage of multiple object instances.

- Each object in the array maintains its own set of data members while sharing member function code.

- Initialization at declaration time can use either default or parameterized constructors.

- Passing arrays of objects to functions can be done by value (calls copy constructor) or by reference (more efficient).

- Dynamic arrays are created using 'new' and must be deallocated using 'delete[]' to prevent memory leaks.

- Destructors are called for each object in reverse order when the array is destroyed or deallocated.

- Loop constructs (for, while) are essential for processing all elements in an array of objects.

## Common Mistakes to Avoid

- Forgetting to define a default constructor when only parameterized constructor exists, leading to compilation errors.

- Using incorrect syntax for accessing members: remember to use dot (.) with objects and arrow (->) with pointers.

- Not using 'delete[]' for dynamic arrays of objects, causing memory leaks.

- Attempting to access array elements beyond bounds, leading to undefined behavior.

## Revision Tips

1. Practice declaring and initializing arrays of objects with different constructor types.

2. Write programs that pass arrays of objects to functions using both pass-by-value and pass-by-reference.

3. Review destructor execution order for arrays of objects.

4. Solve previous year university exam questions on this topic to understand the pattern.

5. Create quick reference notes for syntax of array of objects declaration, initialization, and dynamic creation.
