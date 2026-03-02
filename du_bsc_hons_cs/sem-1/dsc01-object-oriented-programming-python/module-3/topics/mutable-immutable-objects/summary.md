# Mutable and Immutable Objects in Python - Summary

## Key Definitions and Concepts

- **Mutable Objects**: Objects whose state or contents can be modified after creation without creating a new object. Examples: `list`, `dict`, `set`.
- **Immutable Objects**: Objects that cannot be changed after creation; any apparent modification creates a new object. Examples: `int`, `float`, `str`, `tuple`, `frozenset`.
- **Object Identity**: The unique identifier of an object, accessible via `id()`, representing its memory address.
- **Aliasing**: When two variables reference the same object in memory.

## Important Formulas and Techniques

- `id(object)` - Returns the identity of an object
- `type(object)` - Returns the type/class of an object
- `is` operator - Checks if two references point to the same object
- `==` operator - Checks if two objects have the same value

## Key Points

1. Python variables are references to objects, not the objects themselves.
2. Lists, dictionaries, and sets are mutable; integers, floats, strings, and tuples are immutable.
3. Modifying a mutable object affects all references to that object.
4. "Modifying" an immutable object creates a new object; the original remains unchanged.
5. Tuples are immutable but can contain mutable objects (lists, dicts).
6. Function parameters: mutable objects can be modified; immutable objects cannot.
7. Small integers (-5 to 256) and strings are cached for performance.
8. Default mutable arguments in functions cause the "mutable default argument" bug.

## Common Mistakes to Avoid

- Using mutable default arguments in function definitions
- Assuming tuple modification is possible (tuple elements cannot be changed)
- Confusing `is` (identity check) with `==` (equality check)
- Forgetting that seemingly independent variables might share the same object

## Revision Tips

1. Practice identifying whether various Python types are mutable or immutable.
2. Write code using `id()` to observe object identity changes.
3. Trace through function calls with mutable and immutable arguments.
4. Review the special case of tuples containing mutable objects.
5. Memorize the classification: Lists, Dicts, Sets = Mutable; Numbers, Strings, Tuples, Booleans = Immutable.