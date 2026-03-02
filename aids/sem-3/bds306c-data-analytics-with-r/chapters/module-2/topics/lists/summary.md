# Lists in R - Summary

## Key Definitions and Concepts

- LIST: A data structure in R that can contain elements of different types (numeric, character, logical, vectors, matrices, data frames, functions, or other lists)

- NAMED LIST: A list where elements are assigned names, allowing access via the $ operator

- NESTED LIST: A list containing other lists as elements, useful for hierarchical data

## Important Formulas and Theorems

- Creating lists: list(element1, element2, ...) or list(name1 = element1, name2 = element2, ...)

- Accessing by position: list[[n]] returns the nth element

- Accessing by name: list$name or list[["name"]]

- Converting to vector: unlist(list_object)

- Applying functions: lapply(list, func) returns list; sapply(list, func) attempts simplification

## Key Points

- Lists can hold objects of different data types, unlike vectors which must be homogeneous

- Double brackets [[]] extract actual content while single brackets [] return a sub-list

- The $ operator provides convenient access to named list elements

- Setting an element to NULL removes it from the list

- Many R functions (lm(), summary(), read.csv()) return list objects

- lapply() always returns a list; sapply() may return a simplified vector

- unlist() flattens lists but may cause type coercion to a common type

- Lists are indexed starting from 1, not 0

- length() returns the number of top-level elements in a list

## Common Mistakes to Avoid

- Confusing [[]] with [] — using [] returns a list, not the element itself

- Forgetting that unlist() coerces all elements to a common type, potentially losing information

- Attempting to use matrix operations directly on lists without extracting elements first

- Not checking for NULL elements before performing operations, which can cause errors

## Revision Tips

- Practice creating lists with different data types and accessing elements in multiple ways

- Write code to extract components from function return values like lm() output

- Use str() frequently to understand list structure when working with real data

- Create nested lists to understand hierarchical data organization

- Memorize the difference between lapply() and sapply() behavior