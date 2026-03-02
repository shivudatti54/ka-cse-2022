# Templates and Generic Programming in C++

## Introduction to Generic Programming

Generic programming is a programming paradigm that emphasizes writing code in terms of types that will be specified later. This allows developers to write functions and classes that work with any data type without rewriting code for each specific type.

In C++, templates are the primary mechanism for implementing generic programming. They enable you to define a family of functions or classes that operate on different data types while maintaining type safety.

**Key Benefits:**

- Code reusability
- Type safety
- Performance (no runtime overhead)
- Flexibility

## Function Templates

Function templates allow you to write a single function that can work with different data types. The compiler generates the appropriate function for each type used.

### Basic Syntax

```cpp
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}
```

**How it works:**

```
+-------------------+    +-------------------+
| Template Function | -> | int maximum(int, int) |
+-------------------+    +-------------------+
                         | double maximum(double, double) |
                         +-------------------+
                         | char maximum(char, char) |
                         +-------------------+
```

### Example with Multiple Types

```cpp
template <typename T1, typename T2>
void printPair(T1 first, T2 second) {
    std::cout << first << " : " << second << std::endl;
}
```

## Class Templates

Class templates allow you to define classes that can work with any data type. This is particularly useful for container classes like vectors, stacks, and queues.

### Basic Syntax

```cpp
template <typename T>
class Box {
private:
    T content;
public:
    void setContent(T newContent) {
        content = newContent;
    }
    T getContent() {
        return content;
    }
};
```

### Template Specialization

Sometimes you need special behavior for specific types. Template specialization allows you to define custom implementations for particular data types.

```cpp
// General template
template <typename T>
class Calculator {
public:
    T add(T a, T b) { return a + b; }
};

// Specialization for char*
template <>
class Calculator<char*> {
public:
    char* add(char* a, char* b) {
        // Custom string concatenation logic
        return strcat(a, b);
    }
};
```

## Template Parameters

Templates can have multiple parameters, including non-type parameters.

### Multiple Type Parameters

```cpp
template <typename T, typename U>
class Pair {
private:
    T first;
    U second;
public:
    Pair(T f, U s) : first(f), second(s) {}
    // ...
};
```

### Non-Type Template Parameters

```cpp
template <typename T, int size>
class FixedArray {
private:
    T arr[size];
public:
    // ...
};
```

## Template Metaprogramming

Template metaprogramming is a technique that uses templates to perform computations at compile time rather than runtime.

### Factorial Example

```cpp
template <int N>
struct Factorial {
    static const int value = N * Factorial<N - 1>::value;
};

template <>
struct Factorial<0> {
    static const int value = 1;
};

// Usage: Factorial<5>::value equals 120
```

## Standard Template Library (STL) and Templates

The STL is built heavily on templates. Understanding templates is crucial for using STL effectively.

**Common STL Template Components:**

- Containers: `vector<T>`, `list<T>`, `map<K, V>`
- Algorithms: `sort()`, `find()`
- Iterators

## Advanced Template Concepts

### Variadic Templates

Variadic templates allow functions and classes to accept any number of template arguments.

```cpp
template <typename... Args>
void printAll(Args... args) {
    (std::cout << ... << args) << std::endl; // Fold expression (C++17)
}
```

### Type Traits

Type traits provide information about types at compile time.

```cpp
#include <type_traits>

template <typename T>
void process(T value) {
    if constexpr (std::is_integral_v<T>) {
        // Integer-specific processing
    } else if constexpr (std::is_floating_point_v<T>) {
        // Float-specific processing
    }
}
```

## Comparison: Templates vs Traditional Approaches

| Aspect           | Templates           | Function Overloading | Void Pointers        |
| ---------------- | ------------------- | -------------------- | -------------------- |
| Type Safety      | High                | High                 | Low                  |
| Code Reusability | High                | Medium               | High                 |
| Performance      | High (compile-time) | High                 | Low (runtime checks) |
| Readability      | Medium              | High                 | Low                  |
| Compilation Time | Higher              | Lower                | Lower                |

## Common Template Pitfalls and Solutions

1. **Template Bloat**: Multiple instantiations can increase code size
   - Solution: Use explicit instantiation for common types

2. **Complex Error Messages**: Template errors can be hard to read
   - Solution: Use static_assert for better error messages

3. **Separation of Declaration and Definition**: Templates typically need to be defined in header files
   - Solution: Use `.tpp` files or explicit instantiation

## Exam Tips

1. **Remember the syntax**: `template <typename T>` is the standard syntax, though `template <class T>` is also valid and identical.

2. **Understand instantiation**: Templates are blueprints; the compiler generates actual code when you use them with specific types.

3. **Know the difference**: Between function templates (generate functions) and class templates (generate classes).

4. **Specialization matters**: Be able to recognize when template specialization is needed and how to implement it.

5. **STL connection**: Recognize how templates enable the Standard Template Library's flexibility.

6. **Compile-time vs runtime**: Template metaprogramming happens at compile time, providing performance benefits.

7. **Type safety**: Templates maintain type safety unlike void pointer approaches.
