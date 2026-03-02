# **Function Composition and Inverse Functions**

## **Introduction**

In this topic, we will explore the concepts of function composition and inverse functions, which are fundamental ideas in discrete mathematical structures. Function composition is a way of combining two or more functions to produce a new function, while inverse functions are functions that "undo" the action of another function.

## **Function Composition**

### Definition

Function composition is the process of combining two or more functions to produce a new function. Given two functions f and g, the composition of f and g is denoted by (f ∘ g)(x) and is defined as:

(f ∘ g)(x) = f(g(x))

### Properties

- **Associativity**: Function composition is associative, meaning that the order in which we compose functions does not matter: (f ∘ g) ∘ h = f ∘ (g ∘ h)
- **Identity**: The identity function is the identity for function composition, meaning that (f ∘ id)(x) = f(x) for any function f
- **Composition is not commutative**: In general, f ∘ g ≠ g ∘ f

### Examples

- Let f(x) = 2x and g(x) = x + 1. Then, (f ∘ g)(x) = f(g(x)) = f(x + 1) = 2(x + 1) = 2x + 2
- Let f(x) = x^2 and g(x) = x + 1. Then, (f ∘ g)(x) = f(g(x)) = f(x + 1) = (x + 1)^2 = x^2 + 2x + 1

### Key Concepts

- **Domain and codomain**: The domain and codomain of a composite function are the unions of the domains and codomains of the individual functions.
- **Range**: The range of a composite function is the range of the inner function.

### Code Example

Here is an example of function composition in Python:

```python
def f(x):
    return 2 * x

def g(x):
    return x + 1

def composite_f_g(x):
    return f(g(x))

print(composite_f_g(2))  # Output: 6
```

## **Inverse Functions**

### Definition

An inverse function is a function that "undoes" the action of another function. Given a function f, the inverse function f^{-1} is defined as:

f^{-1}(f(x)) = x for all x in the domain of f

### Properties

- **Bijectivity**: Inverse functions are bijective, meaning that they are both one-to-one and onto.
- **Inverse of the inverse**: The inverse of the inverse of a function is the original function: (f^{-1})^{-1}(f^{-1}(x)) = f(x)

### Examples

- Let f(x) = x^2. Then, the inverse function f^{-1}(x) = √x
- Let f(x) = 2x + 1. Then, the inverse function f^{-1}(x) = (x - 1) / 2

### Key Concepts

- **Domain and codomain**: The domain and codomain of an inverse function are the ranges and domains of the original function.
- **Range**: The range of an inverse function is the domain of the original function.

### Code Example

Here is an example of an inverse function in Python:

```python
def f(x):
    return x^2

def inverse_f(x):
    return x ** 0.5

print(inverse_f(4))  # Output: 2.0
```

### Composition of Inverse Functions

When we compose an inverse function with a function, the result is the identity function. For example:

(f \circ f^{-1})(x) = f(f^{-1}(x)) = x

### Conclusion

In conclusion, function composition and inverse functions are fundamental concepts in discrete mathematical structures. Function composition allows us to combine two or more functions to produce a new function, while inverse functions "undo" the action of another function. Understanding these concepts is crucial for solving problems in algebra, calculus, and other areas of mathematics.
