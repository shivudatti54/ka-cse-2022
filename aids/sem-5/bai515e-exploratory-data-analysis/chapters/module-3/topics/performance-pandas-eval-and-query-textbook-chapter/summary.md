# **Performance Pandas: eval and query**

## **Key Points**

### Evaluating Operations

- `eval()` function evaluates a string as a Python expression and returns the result
- Advantages:
  - Can handle complex expressions
  - Can be faster than using `apply()` or loops
- Disadvantages:
  - Security risks (e.g., eval() can execute arbitrary code)
  - Limited support for vectorized operations

### Querying Data

- `query()` function filters data based on a condition specified in a string
- Advantages:
  - Easy to use and understand
  - Supports vectorized operations
- Disadvantages:
  - Can be slower than using `loc[]` or `query()` with a dictionary

### Important Formulas and Definitions

- **Evaluation of expressions:**
  - `eval()`: evaluates a string as a Python expression and returns the result
  - `numexpr()`: evaluates a string as a numerical expression and returns the result (faster than `eval()`)
- **String manipulation:**
  - `str.startswith()`, `str.endswith()`, `str.find()`: string methods for searching and manipulating strings
- **Filtering data:**
  - `loc[]`: label-based indexing for selecting data
  - `query()`: condition-based filtering for selecting data

### Theorems

- **Security theorem:** `eval()` can execute arbitrary code, making it a security risk
- **Performance theorem:** `eval()` can be faster than using `apply()` or loops for simple expressions, but slower for complex expressions

## **Revision Tips**

- Practice using `eval()` and `query()` functions to improve performance
- Be aware of the security risks associated with `eval()`
- Use `numexpr()` for faster numerical evaluation
- Use `loc[]` or a dictionary for faster condition-based filtering
