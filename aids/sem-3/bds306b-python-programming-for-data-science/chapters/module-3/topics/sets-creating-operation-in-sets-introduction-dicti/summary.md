# **Sets: Creating, Operations, Introduction to Dictionaries**

## **Sets**

- A set is an unordered collection of unique elements.
- It is represented using curly brackets `{}` and elements are separated by commas.
- Example: `a = {1, 2, 3, 4, 5}`

### Creating Sets

- Using the `set()` function: `a = set([1, 2, 2, 3, 4, 5])`
- Using the `{}` syntax: `a = {1, 2, 2, 3, 4, 5}`
- Using the `union()` function: `a = set([1, 2, 3]); b = set([3, 4, 5]); a = a.union(b)`

### Operations in Sets

- Union: combines all elements from two sets: `a = set([1, 2, 3]); b = set([3, 4, 5]); a = a.union(b)`
- Intersection: returns common elements from two sets: `a = set([1, 2, 3]); b = set([3, 4, 5]); a = a.intersection(b)`
- Difference: returns elements in first set but not in second: `a = set([1, 2, 3]); b = set([3, 4, 5]); a = a.difference(b)`
- Symmetric Difference: returns elements in either set but not both: `a = set([1, 2, 3]); b = set([3, 4, 5]); a = a.symmetric_difference(b)`

### Introduction to Dictionaries

---

- A dictionary is an unordered collection of key-value pairs.
- It is represented using curly brackets `{}` and key-value pairs are separated by commas.
- Example: `person = {"name": "John", "age": 30}`

### Creating Dictionaries

- Using the `dict()` function: `person = dict(name="John", age=30)`
- Using the `{}` syntax: `person = {"name": "John", "age": 30}`

### Operations in Dictionaries

- Get value: `person["name"]` returns "John"
- Set value: `person["name"] = "Jane"`
- Delete key-value pair: `del person["age"]`

### Nested Dictionaries

- A nested dictionary is a dictionary inside another dictionary.
- Example: `person = {"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "Anytown"}}`

### Looping over Dictionaries

- Using the `.items()` method: `for key, value in person.items(): print(key, value)`
- Using the `.keys()` method: `for key in person.keys(): print(key)`
- Using the `.values()` method: `for value in person.values(): print(value)`
