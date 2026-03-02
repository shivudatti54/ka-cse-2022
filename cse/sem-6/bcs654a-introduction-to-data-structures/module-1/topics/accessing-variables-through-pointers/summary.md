# Accessing Variables through Pointers - Summary

## Key Definitions and Concepts

- **Pointer**: Variable that stores memory address of another variable
- **Address-of operator (`&`)**: Returns memory address of a variable (`int x; int *p = &x;`)
- **Dereference operator (`*`)**: Accesses value at stored memory address (`*p = 10;`)
- **NULL pointer**: Special pointer value indicating it points to nothing (`int *p = NULL;`)
- **Pointer arithmetic**: Operations to navigate memory addresses (`ptr++, ptr--, ptr + n`)

## Important Formulas and Theorems

```c
1. Pointer declaration: data_type *pointer_name;  // e.g., int *ptr;
2. Address assignment: pointer = &variable;       // ptr = &x;
3. Value access: *pointer = value;                // *ptr = 25;
4. Pointer arithmetic: ptr + n = ptr + (n * sizeof(data_type))
```

## Key Points

- Pointers enable dynamic memory management through `malloc()` and `free()`
- `&` operator is used to get address, `*` operator dereferences pointers
- Uninitialized pointers contain garbage values (always initialize to NULL)
- Pointer variables store addresses, while dereferenced pointers access values
- Pointer arithmetic depends on data type size (int: +4 bytes per increment)
- NULL pointers prevent undefined behavior when no valid address exists
- Multiple indirection possible through pointer-to-pointer variables (`int **pptr`)
- Example workflow:
  ```c
  int x = 5;       // Variable
  int *p = &x;     // Pointer declaration & assignment
  *p = 10;         // Modify x through pointer
  ```

## Common Mistakes to Avoid

1. **Dereferencing uninitialized pointers**: Causes segmentation faults
   ```c
   int *p;  // Wrong
   *p = 5;  // Crash!
   ```
2. **Confusing `*` in declaration vs dereference**:
   ```c
   int *p;  // Declaration
   *p = 5;  // Dereference
   ```
3. **Incorrect pointer arithmetic**:
   ```c
   int arr[3] = {1,2,3};
   int *p = arr;
   p++;  // Correctly moves to arr[1]
   p += 2; // Now points to arr[3] (out of bounds)
   ```
4. **Not checking for NULL before dereference**:
   ```c
   if(p != NULL) { *p = 10; }  // Safe
   ```

## Revision Tips

1. **Practice code tracing**: Draw memory diagrams showing variables, addresses, and pointers
2. **Use flashcards** for operator meanings:
   - `&var` → "Address of var"
   - `*ptr` → "Value at ptr"
3. **Solve pointer manipulation problems**:
   ```c
   int a=2, b=3, *p1=&a, *p2=&b;
   *p1 = *p2 + 5;  // What's the new value of a?
   ```
4. **Review previous questions**:
   - Focus on pointer declaration/initialization (2 marks)
   - Pointer arithmetic in arrays (5 marks)
   - Debugging pointer-related code snippets (common in exams)
