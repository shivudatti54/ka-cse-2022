# Tuples and Sets Operations - Summary

## Key Definitions and Concepts

- **Tuple**: An ordered, immutable sequence of elements in Python. Created using parentheses `()` or the `tuple()` constructor.
- **Set**: An unordered, mutable collection of unique elements. Created using curly braces `{}` or the `set()` constructor.
- **Frozen Set**: An immutable version of a set; hashable and can be used as dictionary keys or set elements.
- **Tuple Packing**: Combining multiple values into a single tuple.
- **Tuple Unpacking**: Extracting individual values from a tuple into separate variables.

## Important Formulas and Operations

| Operation | Tuple Syntax | Set Syntax |
|-----------|--------------|------------|
| Creation | `t = (1, 2, 3)` or `tuple([1,2,3])` | `s = {1, 2, 3}` or `set([1,2,3])` |
| Concatenation/Union | `t1 + t2` | `s1 \| s2` or `s1.union(s2)` |
| Repetition | `t * n` | Not applicable |
| Membership | `x in t` | `x in s` |
| Length | `len(t)` | `len(s)` |

**Set-Specific Operations:**
- Intersection: `s1 & s2` or `s1.intersection(s2)`
- Difference: `s1 - s2` or `s1.difference(s2)`
- Symmetric Difference: `s1 ^ s2` or `s1.symmetric_difference(s2)`

## Key Points

- Tuples are **immutable** (cannot be modified after creation); sets are **mutable**
- Tuples support indexing and slicing like lists; sets do not support indexing
- Tuples can be used as **dictionary keys**; lists and sets cannot
- Single-element tuple requires a **trailing comma**: `(42,)`
- Empty set must be created with `set()`, not `{}` (which creates dict)
- Set membership testing is **O(1)**; list membership is **O(n)**
- Tuples have only **two methods**: `.count()` and `.index()`
- Sets automatically **remove duplicates**
- Frozen sets are **hashable**; regular sets are not

## Common Mistakes to Avoid

1. **Forgetting the trailing comma** for single-element tuples: `(42)` is not a tuple
2. **Using `{}` for empty sets**: This creates a dictionary, use `set()` instead
3. **Assuming set order**: Sets are unordered—do not rely on element ordering
4. **Trying to modify tuples**: Remember immutability—will raise TypeError
5. **Using mutable objects as dictionary keys**: Tuples with mutable elements (like lists) are not hashable

## Revision Tips

1. **Practice tuple unpacking** with extended unpacking: `a, *b, c = (1, 2, 3, 4, 5)`
2. **Memorize time complexities**: Set lookup is O(1), List lookup is O(n)
3. **Remember method names**: All set methods end with appropriate names (union, intersection, difference)
4. **Understand when to use each**: Tuples for fixed data, sets for unique collections and operations
5. **Solve previous year questions** on tuple packing/unpacking and set operations