# **Arrays, Pointers, References, and Dynamic Allocation Operators: Quick Revision Notes**

### Arrays

- **Definition**: A collection of elements of the same data type stored in contiguous memory locations.
- **Types of Arrays**:
  - **Static Arrays**: Declared with fixed size, initialized at compile-time.
  - **Dynamic Arrays**: Declared with unspecified size, initialized at runtime.
- **Array Initialization**:
  - **Direct Initialization**: Using the assignment operator.
  - **Initializers**: Using the initializer list.

### Pointers

- **Definition**: A memory address that stores the location of a variable or data type.
- **Types of Pointers**:
  - **Raw Pointers**: Pointers that store raw memory addresses.
  - **Dereference Operator** (`*`): Used to access the value stored at a memory address.
- **Pointer Arithmetic**:
  - **Increment**: `ptr++`
  - **Decrement**: `ptr--`
  - **Pointer addition**: `ptr + 1`

### References

- **Definition**: An alias for a variable, used to refer to a variable without taking its address.
- **Types of References**:
  - **Constant References**: Used for constants, preventing modification.
  - **Non-Constant References**: Used for non-constants, allowing modification.
- **Reference Initialization**:
  - **Explicit Initialization**: `ref = var;`
  - **Implicit Initialization**: `const ref var;`

### Dynamic Allocation Operators

- **`new` Operator**: Allocates memory for an object on the heap.
- **`delete` Operator**: Deallocates memory previously allocated using `new`.
- **`new[]` Operator**: Allocates memory for an array on the heap.
- **`delete[]` Operator**: Deallocates memory previously allocated using `new[]`.

### Arrays of Objects

- **Definition**: An array of objects, where each element is an instance of a class.
- **Example**: `MyClass objects[10];`
- **Initialization**: `new MyClass[10];`

### Pointers to Objects

- **Definition**: A pointer that stores the address of an object.
- **Example**: `MyClass* ptr;`
- **Dereference**: `*ptr`

### The `this` Pointer

- **Definition**: A pointer to the current object being referred to.
- **Example**: `MyClass* thisPtr = this;`
- **Use case**: `this->function();`

### Pointers to Derived Types

- **Definition**: A pointer to an object of a derived type.
- **Example**: `BaseClass* ptr;`
- **Use case**: `ptr->function();`
- **Note**: If `ptr` points to a base class object, it can be treated as a base class object, but not as a derived class object.

**Important Formulas and Theorems**

- **The Rule of 3**: If you define any of the copy constructor, move constructor, or copy assignment operator, you must define all three.
- **The Rule of 5**: If you define any of the copy constructor, move constructor, move assignment operator, copy assignment operator, or destructor, you must define all five.
