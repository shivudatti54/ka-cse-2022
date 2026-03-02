# Dictionaries and Operations in Python - Summary

## Key Definitions and Concepts

- **Dictionary**: An unordered, mutable collection of key-value pairs where keys must be unique and immutable (strings, numbers, tuples)
- **Key-Value Pair**: The fundamental unit of a dictionary, where each key maps to a specific value
- **View Objects**: Dynamic objects returned by `keys()`, `values()`, and `items()` that reflect changes to the dictionary

## Important Formulas and Theorems

- **Dictionary Creation**: `{key1: value1, key2: value2}` or `dict(key1=value1, key2=value2)`
- **Lookup Complexity**: O(1) average case for key lookups (hash table implementation)
- **Membership Test**: `key in dict` uses O(1) hash lookup

## Key Points

- Dictionaries maintain insertion order since Python 3.7+
- Keys must be immutable; values can be of any type
- `.get(key, default)` is safer than `dict[key]` to avoid KeyError
- Dictionary methods: `keys()`, `values()`, `items()`, `get()`, `pop()`, `popitem()`, `update()`, `copy()`, `clear()`, `setdefault()`
- Dictionary comprehension syntax: `{k: v for k, v in iterable if condition}`
- Nested dictionaries enable complex hierarchical data structures
- `dict.popitem()` removes and returns the last inserted pair (LIFO order)
- `.update()` method merges another dictionary into the existing one

## Common Mistakes to Avoid

1. Using mutable objects (lists) as dictionary keys - leads to TypeError
2. Forgetting that dictionary keys are case-sensitive ("Name" ≠ "name")
3. Using `.get()` without understanding it returns `None` by default when key missing
4. Not handling KeyError when using square bracket access for non-existent keys
5. Confusing shallow copy with deep copy in nested dictionaries

## Revision Tips

1. Practice creating dictionaries from different data sources (lists, tuples, strings)
2. Write programs to convert between dictionaries and other data structures
3. Memorize the dictionary method signatures and their return types
4. Solve at least 5-10 dictionary-based coding problems before the exam
5. Understand the hash table concept behind dictionary performance