# Pointers to Class Members - Summary

## Key Definitions and Concepts

- **Pointer to Data Member**: A pointer that stores the offset of a data member within a class, declared as `type ClassName::*pointerName`.

- **Pointer to Member Function**: A pointer that references a member function of a class, declared as `ReturnType (ClassName::*pointerName)(Parameters)`.

- **Member Pointer Operators**: `.*` (dot star) for dereferencing with objects, `->*` (arrow star) for dereferencing with pointers to objects.

- **Offset Storage**: Pointers to data members store relative offsets from the class base address, not absolute memory addresses.

## Important Formulas and Syntax

```
Declaration:  ClassName::*pointerName
Initialization: pointerName = &ClassName::memberName
Dereferencing: object.*pointer  or  objectPointer->*pointer
```

## Key Points

1. Pointers to class members require class qualification in their type declaration to maintain type safety.

2. Static class members use regular pointers, not member pointers, as they are not bound to objects.

3. The operators ._ and ->_ must be used for member pointer dereferencing; regular \* operator will not work.

4. Pointer-to-member types are distinct from regular pointer types even if they point to similar data/function signatures.

5. nullptr can be assigned to member pointers to indicate they point to no member.

6. Pointers to members enable implementing callbacks, function tables, and generic algorithms that operate on class members.

7. Template programming extensively uses pointers to members for member adaptation in STL algorithms.

8. The complete function signature including return type and all parameters must be specified for member function pointers.

## Common Mistakes to Avoid

1. Using regular `*` operator instead of `.*` or `->*` when dereferencing member pointers.

2. Forgetting to use parentheses when calling member functions through pointers: `(obj.*ptr)(args)`.

3. Confusing static member pointers with non-static member pointers; they have different types.

4. Not checking for nullptr before dereferencing pointer-to-member variables.

5. Omitting the class name when declaring pointer-to-member types, resulting in syntax errors.

## Revision Tips

1. Practice writing declarations for both data member and function member pointers with various signatures.

2. Create small programs to reinforce the syntax and usage of ._ and ->_ operators.

3. Understand that pointers to data members store offsets by tracing through simple class examples.

4. Remember the typedef pattern for simplifying complex pointer-to-member declarations.

5. Review the difference between regular function pointers and member function pointers to clarify the conceptual distinction.
