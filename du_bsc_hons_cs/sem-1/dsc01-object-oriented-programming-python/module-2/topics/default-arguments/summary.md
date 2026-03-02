# Default Arguments in Python - Summary

## Key Definitions and Concepts

- **Default Arguments**: Parameters in function definitions that have predefined values; used when callers do not provide explicit values
- **Mutable Default Argument**: A default argument that uses a mutable object (list, dict), which can cause unexpected behavior due to single evaluation
- **Sentinel Pattern**: Using `None` as default value and creating new mutable objects inside the function body

## Important Formulas and Patterns

```python
# Standard default argument syntax
def function_name(param1, param2=default_value):
    pass

# Correct mutable default argument pattern
def function_name(param, mutable=None):
    if mutable is None:
        mutable = []  # Create new list each call
    return mutable
```

## Key Points

- Default arguments must follow non-default arguments in function definitions (positional order rule)
- Default values are evaluated once when the function is defined, not at each call
- Mutable default arguments (lists, dictionaries) persist across function calls, causing bugs
- Use `None` as sentinel value for mutable defaults to avoid unexpected behavior
- Default arguments enhance function flexibility and reduce code duplication
- In OOP, `__init__` methods commonly use default arguments for optional parameters
- Default arguments can be combined with *args and **kwargs for maximum flexibility
- Keyword arguments allow overriding specific defaults without affecting others

## Common Mistakes to Avoid

1. Placing default arguments before non-default arguments (SyntaxError)
2. Using mutable objects like `[]` or `{}` directly as default arguments
3. Assuming default arguments are re-evaluated on each function call
4. Forgetting that all parameters after a provided argument must also be provided when using positional arguments

## Revision Tips

1. Practice writing functions with various combinations of default arguments
2. Create examples demonstrating the mutable default argument pitfall and its fix
3. Review class constructor examples using default arguments
4. Solve previous years' DU examination questions on default arguments
5. Remember: when in doubt with mutable defaults, use `None` and create new objects inside the function