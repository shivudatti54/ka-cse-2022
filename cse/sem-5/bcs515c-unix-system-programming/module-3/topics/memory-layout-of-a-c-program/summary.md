# Memory Layout of a C Program - Summary

## Key Definitions and Concepts

- **Memory Layout**: The organized arrangement of different program components in memory when a C program executes
- **Text Segment**: Read-only region containing executable code instructions
- **Data Segment**: Stores initialized global and static variables
- **BSS Segment**: Stores uninitialized global and static variables (zero-initialized)
- **Heap**: Dynamic memory region growing upward, managed by malloc()/free()
- **Stack**: LIFO region growing downward, stores function calls, local variables, return addresses
- **Stack Frame**: Activation record pushed when a function is called

## Important Formulas and Concepts

- Memory Layout Order (Low to High): Text → Data → BSS → Heap → Stack
- Stack grows toward lower addresses
- Heap grows toward higher addresses
- Variables in Data/BSS have program scope (static lifetime)
- Variables on stack have function scope (automatic lifetime)
- Heap memory must be explicitly freed

## Key Points

1. The text segment contains executable code and is typically read-only for security
2. Initialized global/static variables go to Data segment; uninitialized go to BSS
3. The BSS segment is zero-initialized by the operating system for efficiency
4. Heap allocation uses malloc(), calloc(), realloc(); deallocation uses free()
5. Stack memory is automatic - allocated on function call, deallocated on return
6. Recursive function calls create multiple stack frames
7. Local variables (auto) are stored on stack; static variables in Data/BSS
8. Pointers can reference any memory region but must be validated before use

## Common Mistakes to Avoid

1. **Forgetting to free heap memory**: Always pair malloc() with free()
2. **Using dangling pointers**: Never access memory after freeing it
3. **Buffer overflows**: Never write beyond array bounds
4. **Null pointer dereference**: Always check pointers before use
5. **Stack overflow**: Avoid excessive recursion or large stack allocations

## Revision Tips

1. Draw the memory layout diagram repeatedly until you can reproduce it from memory
2. Practice identifying which segment each variable belongs to in sample C programs
3. Remember the mnemonic: "Text Data BSS Heap Stack - Top Down" (but Stack is actually at the top physically)
4. Understand the difference between static (Data/BSS) and automatic (stack) storage durations
5. Review pointer concepts alongside memory layout as they are closely related
