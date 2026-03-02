# Overloading new and delete - Summary

## Key Definitions and Concepts

- **new operator**: Allocates memory and constructs an object; can be overloaded to customize memory allocation behavior
- **delete operator**: Destructs an object and deallocates memory; can be overloaded to customize memory deallocation
- **Memory Pool**: Pre-allocated block of memory from which smaller allocations are served, reducing fragmentation and allocation overhead
- **Placement new**: Special form of new that constructs an object at a specified memory address

## Important Formulas and Theorems

```cpp
// Basic overload signatures
void* operator new(size_t size);           // Returns pointer to allocated memory
void operator delete(void* ptr);            // Takes pointer to deallocate

// Array versions
void* operator new[](size_t size);
void operator delete[](void* ptr);

// With additional parameters (placement syntax)
void* operator new(size_t size, AdditionalArgs...);
```

## Key Points

- The `size_t` parameter in `operator new` is automatically passed by the compiler based on the type being allocated
- Class-specific `new` and `delete` operators are implicitly static, even when declared as non-static members
- The compiler automatically calls constructors after `operator new` and destructors before `operator delete`
- Global overloading affects all allocations in the program, while class-specific overloading affects only that class
- Array versions `new[]` and `delete[]` must be overloaded separately if needed
- Custom `new` should throw `bad_alloc` on failure (or use the nothrow version)
- Always overload both `new` and `delete` together for proper memory management
- Placement new allows construction at predetermined memory locations

## Common Mistakes to Avoid

1. **Forgetting to return correct type**: `operator new` must return `void*`, not the actual object type
2. **Not handling size correctly**: Always use the `size` parameter, even if you think you know the size
3. **Mismatching new and delete**: Using `delete` on memory allocated with `new[]` causes undefined behavior
4. **Not providing matching delete**: When overloading new with extra parameters, provide matching delete to avoid memory leaks
5. **Forgetting to free memory**: Custom allocation means you must ensure corresponding deallocation

## Revision Tips

1. Practice writing both global and class-specific overloads until the syntax becomes automatic
2. Trace through examples to understand the order of constructor/destructor calls with custom operators
3. Remember that overloaded new/delete replace only the memory management, not object construction/destruction
4. Review the memory pool example to understand practical applications
5. Be familiar with debugging applications that track allocation/deallocation patterns
