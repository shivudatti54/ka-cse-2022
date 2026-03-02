# **Sets and Dictionaries Revision Notes**

## **Sets**

- A set is an unordered collection of unique elements.
- Sets are used to store multiple values in a single variable.
- Sets are represented by the `set()` function in Python.
- Example: `my_set = {1, 2, 3, 4, 5}`

## **Set Operations**

- `Union`: Combines all elements from both sets without duplicates.
  - Formula: `A ∪ B = {x | x ∈ A or x ∈ B}`
- `Intersection`: Returns elements common to both sets.
  - Formula: `A ∩ B = {x | x ∈ A and x ∈ B}`
- `Difference`: Returns elements in set A but not in set B.
  - Formula: `A - B = {x | x ∈ A and x ∉ B}`
- `Symmetric Difference`: Returns elements in either set A or set B, but not both.
  - Formula: `A Δ B = (A ∪ B) - (A ∩ B)`

## **Dictionaries**

- A dictionary is an unordered collection of key-value pairs.
- Dictionaries are used to store data with labels (keys) and values.
- Dictionaries are represented by the `dict()` function in Python.
- Example: `my_dict = {'name': 'John', 'age': 30}`

## **Dictionary Operations**

- `Create a new dictionary`: `my_dict = {'key1': 'value1', 'key2': 'value2'}`
- `Update a dictionary`: `my_dict['key1'] = 'new_value1'`
- `Delete a key-value pair`: `del my_dict['key2']`

## **Nested Dictionaries**

- A nested dictionary is a dictionary within another dictionary.
- Example: `my_nested_dict = {'key1': {'key11': 'value11', 'key12': 'value12'}, 'key2': 'value2'}`

## **Looping over Dictionaries**

- Use `for key, value in dict.items():` to loop over key-value pairs.
- Use `for key in dict.keys():` to loop over keys only.
- Use `for value in dict.values():` to loop over values only.

## **Important Formulas and Definitions**

- **Set Theory**: A branch of mathematics that deals with sets and their properties.
- **Mathematical Operations**: Union, intersection, difference, symmetric difference.

## **Theorems**

- **Abaçus' Theorem**: A fundamental theorem in set theory that describes the relationship between the number of elements in two sets.
