# **Default Function Arguments**

## **Introduction**

In C++, a default function argument is a parameter with a default value assigned to it. This allows a function to be called with or without providing a value for the parameter. In this topic, we will learn about default function arguments, their uses, and how to declare them in C++.

## **What are Default Function Arguments?**

A default function argument is a parameter with a default value assigned to it. When a function is declared with a default argument, the compiler will use the default value if the parameter is not provided when calling the function.

## **Why are Default Function Arguments Useful?**

Default function arguments are useful in several scenarios:

- **Providing a default behavior**: By providing a default value, you can ensure that a function behaves in a specific way if no value is provided.
- **Reducing code duplication**: If multiple functions require the same default value, you can define it once and use it in all functions.
- **Improving code readability**: Default function arguments can make your code more readable by reducing the number of parameters that need to be passed.

## **Declaring Default Function Arguments**

To declare a default function argument, you use the `=` operator after the parameter name. The default value can be any expression, including literals, variables, or other function calls.

```cpp
void greet(std::string name = "World") {
    std::cout << "Hello, " << name << "!" << std::endl;
}
```

In this example, the `greet` function takes a `std::string` parameter named `name`. The default value is `"World"`, which means that if you call the function without providing a value for `name`, the default value will be used.

## **Key Concepts**

- **Default argument syntax**: `parameter_name (= default_value)`.
- **Default argument order**: Default arguments must be declared after non-default arguments.
- **Function overload**: You can have multiple functions with different default arguments, which allows for function overloading.

## **Example Use Cases**

### Example 1: Using a Default Argument to Provide a Default Value

```cpp
#include <iostream>

void greet(std::string name = "World") {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    greet();  // Outputs: Hello, World!
    greet("John");  // Outputs: Hello, John!
    return 0;
}
```

### Example 2: Using a Default Argument to Reduce Code Duplication

```cpp
#include <iostream>

void printMessage(std::string message = "Default message") {
    std::cout << message << std::endl;
}

int main() {
    printMessage();  // Outputs: Default message
    printMessage("Custom message");  // Outputs: Custom message
    return 0;
}
```

### Example 3: Using a Default Argument to Improve Code Readability

```cpp
#include <iostream>

void printMessage(std::string message = "Hello") {
    std::cout << message << std::endl;
}

int main() {
    printMessage();  // Outputs: Hello
    printMessage("Goodbye");  // Outputs: Goodbye
    return 0;
}
```

## **Best Practices**

- **Use default arguments sparingly**: Only use default arguments when they improve code readability or reduce code duplication.
- **Avoid using default arguments for required parameters**: If a parameter is required, do not provide a default value.
- **Document default arguments**: Clearly document the default arguments used in your functions to avoid confusion.
