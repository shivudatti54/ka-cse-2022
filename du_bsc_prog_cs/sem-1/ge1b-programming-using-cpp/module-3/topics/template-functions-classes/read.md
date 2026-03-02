# Template Functions and Template Classes in C++

## Introduction

Templates are one of the most powerful features of C++ that enable generic programming. They allow you to write code that works with any data type while maintaining type safety at compile time. In the context of the University of Delhi's Computer Science curriculum, understanding templates is essential for writing flexible, reusable, and efficient code.

Before templates, programmers had to either write separate functions/classes for each data type or use void pointers and manual type casting, which was error-prone and lacked type safety. Templates solve this problem by allowing the compiler to generate type-specific code automatically based on the template definition.

Templates are extensively used in the C++ Standard Template Library (STL), which is a collection of generic algorithms and data structures. When you use containers like `vector`, `list`, or algorithms like `sort`, you are indirectly using templates. This makes templates fundamental to modern C++ programming and a critical topic for your semester examinations.

## Key Concepts

### Function Templates

A function template defines a family of functions with different parameter types. The general syntax uses the `template` keyword followed by a parameter list enclosed in angle brackets:

```cpp
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}
```

Here, `typename T` declares a type parameter that will be replaced by the actual type when the function is called. You can also use `class` instead of `typename` — they are functionally equivalent in this context.

The compiler performs template argument deduction to determine which type to substitute. When you call `maximum(5, 10)`, the compiler deduces `T` as `int` and generates the corresponding function code.

### Class Templates

Class templates extend the same concept to classes, allowing you to create parameterized types. A classic example is a generic stack:

```cpp
template <typename T>
class Stack {
private:
    vector<T> elements;
public:
    void push(const T& elem);
    T pop();
    bool isEmpty() const;
};

template <typename T>
void Stack<T>::push(const T& elem) {
    elements.push_back(elem);
}
```

Note that member functions of a class template are themselves templates and require their own `template` declaration when defined outside the class.

### Multiple Template Parameters

Templates can accept multiple type parameters:

```cpp
template <typename T1, typename T2>
class Pair {
    T1 first;
    T2 second;
public:
    Pair(T1 a, T2 b) : first(a), second(b) {}
};
```

You can also have non-type template parameters, which allow constant values as template arguments:

```cpp
template <typename T, int size>
class Array {
    T arr[size];
};
```

### Template Specialization

Sometimes you need special behavior for a specific type. C++ provides full template specialization for this:

```cpp
template <typename T>
class Storage {
    T data;
public:
    void save(const T& d) { data = d; }
};

// Specialization for char* (C-style strings)
template <>
class Storage<char*> {
    char* data;
public:
    void save(const char* d) { 
        data = new char[strlen(d) + 1];
        strcpy(data, d);
    }
};
```

## Examples

### Example 1: Finding the Maximum Element

Write a function template to find the maximum element in an array of any type.

```cpp
#include <iostream>
using namespace std;

template <typename T>
T findMax(T arr[], int n) {
    T max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int intArr[] = {5, 2, 9, 1, 7};
    double doubleArr[] = {3.5, 1.2, 8.9, 2.7};
    
    cout << "Max int: " << findMax(intArr, 5) << endl;
    cout << "Max double: " << findMax(doubleArr, 4) << endl;
    
    return 0;
}
```

**Output:**
```
Max int: 9
Max double: 8.9
```

The compiler generates two separate functions: one for `int` and one for `double`, each optimized for the specific type.

### Example 2: Generic Pair Class

Create a template class to store pairs of related values.

```cpp
#include <iostream>
#include <string>
using namespace std;

template <typename T1, typename T2>
class Pair {
private:
    T1 first;
    T2 second;
public:
    Pair(T1 f, T2 s) : first(f), second(s) {}
    
    T1 getFirst() const { return first; }
    T2 getSecond() const { return second; }
    
    void display() const {
        cout << "First: " << first << ", Second: " << second << endl;
    }
};

int main() {
    Pair<int, string> student(101, "Aisha");
    Pair<double, char> grade(95.5, 'A');
    
    student.display();
    grade.display();
    
    return 0;
}
```

**Output:**
```
First: 101, Second: Aisha
First: 95.5, Second: A
```

### Example 3: Template Specialization for String Comparison

Implement a template function that finds the smaller of two values, with specialization for C-style strings.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// Primary template
template <typename T>
T smaller(T a, T b) {
    return (a < b) ? a : b;
}

// Template specialization for char*
template <>
char* smaller<char*>(char* a, char* b) {
    return (strcmp(a, b) < 0) ? a : b;
}

int main() {
    int x = 10, y = 20;
    cout << "Smaller of 10, 20: " << smaller(x, y) << endl;
    
    double p = 3.14, q = 2.71;
    cout << "Smaller of 3.14, 2.71: " << smaller(p, q) << endl;
    
    return 0;
}
```

## Exam Tips

1. **Understand the syntax**: Remember that template declarations use `template <typename T>` or `template <class T>`. The keyword `typename` is preferred in modern C++.

2. **Template instantiation is compile-time**: The compiler generates specific code for each type used. This increases compilation time but has no runtime overhead compared to writing separate functions.

3. **Non-type template parameters**: These must be integral types (int, char, bool, etc.) or pointers/references to global entities. Remember they are compile-time constants.

4. **Default template arguments**: Both function and class templates can have default type arguments:
   ```cpp
   template <typename T = int>
   class Container { };
   ```

5. **Member function templates**: Member functions of regular classes can also be templates. This is useful for providing flexible interfaces.

6. **Distinguish between specialization and overloading**: Template specialization provides specific implementations for particular types, while function templates can also be overloaded with regular functions.

7. **Common exam question**: Writing a complete working example of a class template with member functions defined outside the class — remember to include the `template` parameter in both places.

8. **STL connection**: Understand that containers like `vector<T>`, `list<T>`, and algorithms like `sort` are all template-based. Questions often test your understanding through STL usage.