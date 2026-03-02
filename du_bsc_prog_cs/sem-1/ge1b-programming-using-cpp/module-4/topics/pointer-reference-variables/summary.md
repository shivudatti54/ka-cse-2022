# Pointer Reference Variables
## Ge1B Programming Using Cpp - Delhi University NEP 2024

### Introduction

Pointers and reference variables are fundamental concepts in C++ that provide indirect access to memory locations. Mastering these concepts is essential for efficient memory management and building complex data structures in C++ programming.

### Key Concepts

**1. Pointer Variables**
- A pointer stores the memory address of another variable
- Syntax: `data_type *pointer_name;`
- The `&` (address-of) operator returns the address of a variable
- The `*` (dereference) operator accesses the value at a stored address

**2. Declaration and Initialization**
```cpp
int num = 10;
int *ptr = &num;  // Initialize with address
int *ptr2 = nullptr;  // Null pointer initialization
```

**3. Pointer Arithmetic**
- Allowed operations: ++, --, +, -
- Arithmetic is based on data type size
- Useful for array traversal

**4. Pointers and Arrays**
- Array name acts as a constant pointer to first element
- `arr[i]` equivalent to `*(arr + i)`
- Pointers can iterate through array elements

**5. Reference Variables**
- An alias (alternative name) for an existing variable
- Declaration: `data_type &ref_name = variable;`
- Must be initialized at declaration
- No separate memory allocation

**6. Passing Parameters**
- **Pass-by-value**: Copy of data passed
- **Pass-by-reference**: Using references or pointers to modify original data
- **Pass-by-pointer**: Address passed, original modified via dereferencing

**7. Dynamic Memory Allocation**
- `new` allocates memory on heap
- `delete` releases allocated memory
- Prevents memory leaks by proper deallocation

### Differences: Pointers vs References

| Feature | Pointer | Reference |
|---------|---------|-----------|
| Memory | Separate address storage | Alias to existing variable |
| Reassignment | Can be reassigned | Cannot be reassigned |
| Null value | Can be nullptr | Must refer to valid variable |
| Syntax | Requires dereferencing (*) | Direct usage |

### Conclusion

Pointers provide powerful low-level memory manipulation capabilities essential for system programming and data structures, while references offer a safer alternative for parameter passing and aliasing. Understanding when to use each—along with proper memory management—is crucial for writing efficient C++ programs. Practice pointer manipulations and dynamic memory allocation to gain proficiency for examinations.