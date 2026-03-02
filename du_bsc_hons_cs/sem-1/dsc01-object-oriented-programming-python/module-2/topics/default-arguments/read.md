# Default Arguments in Python
## Introduction

In Python, functions can be defined with default argument values. These default values are used when a function is called without providing a value for a particular argument. This feature allows for more flexibility in function definitions and can simplify code by reducing the number of arguments that need to be passed.

Default arguments are useful when we want to provide a common value for a function argument, but still allow the user to override it if needed. They are also useful when we want to add new arguments to a function without breaking existing code that calls the function.

## Key Concepts

### Defining Default Arguments

In Python, default arguments are defined using the `=` operator in the function definition. The syntax for defining a default argument is:
```python
def function_name(argument_name=default_value):
    # function body
```
For example:
```python
def greet(name="World"):
    print(f"Hello, {name}!")
```
In this example, the `greet` function takes a `name` argument with a default value of `"World"`.

### Using Default Arguments

When calling a function with default arguments, we can choose to provide a value for the argument or not. If we don't provide a value, the default value will be used.

For example:
```python
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
```
### Mutability of Default Arguments

One important thing to note about default arguments in Python is that they are only evaluated once, when the function is defined. This means that if we use a mutable object as a default argument, it will be shared across all calls to the function.

For example:
```python
def append_to_list(x, lst=[]):
    lst.append(x)
    return lst

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2]
print(append_to_list(3))  # Output: [1, 2, 3]
```
In this example, the `append_to_list` function uses a list as a default argument. Because lists are mutable, the default argument is shared across all calls to the function, and the list grows with each call.

To avoid this behavior, we can use a trick like this:
```python
def append_to_list(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
```
By setting the default argument to `None` and then checking for `None` inside the function, we can ensure that a new list is created each time the function is called.

## Examples

### Example 1: Using Default Arguments to Simplify Code

Suppose we have a function that calculates the area of a rectangle:
```python
def rectangle_area(width, height):
    return width * height
```
We can add a default argument to make the function more convenient to use:
```python
def rectangle_area(width, height=1):
    return width * height
```
Now we can call the function with only one argument to calculate the area of a square:
```python
print(rectangle_area(4))  # Output: 4
```
### Example 2: Using Default Arguments to Provide a Common Value

Suppose we have a function that sends an email:
```python
def send_email(to, from_, subject, body):
    # email sending code
```
We can add a default argument to provide a common value for the `from_` argument:
```python
def send_email(to, from_="support@example.com", subject, body):
    # email sending code
```
Now we can call the function without providing a value for the `from_` argument:
```python
send_email("user@example.com", "Hello", "This is a test email")
```
## Exam Tips

1. Be careful when using mutable objects as default arguments, as they can be shared across all calls to the function.
2. Use default arguments to simplify code and provide common values for function arguments.
3. When calling a function with default arguments, make sure to provide values for all required arguments.
4. Use the `None` trick to avoid shared mutable default arguments.
5. Default arguments are only evaluated once, when the function is defined.
6. Use default arguments to add new arguments to a function without breaking existing code.
7. Be aware of the order of arguments when defining a function with default arguments.