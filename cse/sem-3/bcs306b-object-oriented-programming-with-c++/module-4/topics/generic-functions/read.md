# Generic Functions in C++

## Introduction

Generic functions, also known as function templates, represent one of the most powerful features of C++ that enable polymorphism at compile-time. Generic programming allows developers to write flexible, reusable code that works with multiple data types without sacrificing performance. Unlike runtime polymorphism through virtual functions, generic functions achieve type flexibility through template metaprogramming, where the compiler generates type-specific code during compilation.

In the context of Object-Oriented Programming with C++, generic functions play a crucial role in achieving code reusability and type safety. The concept was introduced to address the limitations of writing separate functions for different data types. For instance, instead of writing separate functions for finding the maximum of two integers, doubles, or characters, a single generic function can handle all these cases elegantly. This approach not only reduces code duplication but also eliminates the runtime overhead associated with runtime polymorphism.

the university's 2022 Scheme emphasizes the understanding of generic programming paradigms as essential skills for modern software development. This topic forms the foundation for understanding the Standard Template Library (STL), which extensively uses generic functions and classes to provide standard algorithms and data structures.

## Key Concepts

### Function Templates

A function template defines a family of functions that can operate with different data types. The basic syntax involves using the `template` keyword followed by a list of template parameters enclosed in angle brackets:

```cpp
template<typename T>
T maximum(T a, T b) {
 return (a > b) ? a : b;
}
```

The `typename` keyword (or alternatively `class`) declares a template parameter that represents a placeholder for a data type. When the compiler encounters a call to this function, it generates the appropriate version of the function for the specific type being used. This process is called template instantiation.

Template parameters can be of two types: type parameters (declared using `typename` or `class`) and non-type parameters (which represent constant values). The compiler performs type checking at the point of instantiation, ensuring type safety throughout the generic function.

### Template Parameter List

The template parameter list can contain multiple parameters, allowing for more complex generic functions:

```cpp
template<typename T1, typename T2, typename T3>
T3 combine(T1 a, T2 b) {
 // Conversion and combination logic
}
```

Default template arguments can also be specified, similar to default function arguments:

```cpp
template<typename T = int>
T square(T value) {
 return value * value;
}
```

### Function Template Overloading

Function templates can be overloaded with regular functions or with other function templates. The compiler follows a specific resolution process to determine which version to use:

1. First, it attempts exact matches with regular functions
2. If no regular function matches, it tries to find a matching function template
3. Template argument deduction is performed to find the best match
4. If multiple templates match, the most specialized one is selected

```cpp
// Template version
template<typename T>
void display(T value) {
 cout << "Template: " << value << endl;
}

// Overloaded version for specific type
void display(int value) {
 cout << "Integer: " << value << endl;
}
```

### Explicit Specialization

When the generic template logic doesn't work correctly for a specific data type, explicit specialization (also called full specialization) allows providing a custom implementation for that particular type:

```cpp
// Primary template
template<typename T>
T maximum(T a, T b) {
 return (a > b) ? a : b;
}

// Explicit specialization for const char*
template<>
const char* maximum<const char*>(const char* a, const char* b) {
 return (strcmp(a, b) > 0) ? a : b;
}
```

The syntax `template<>` indicates that all template parameters are being explicitly specified, and no further template parameters remain to be deduced.

### Partial Specialization

While function templates don't support partial specialization directly (unlike class templates), overloading serves a similar purpose. Multiple function templates with different parameter lists achieve the same effect:

```cpp
// For pointer types
template<typename T>
T* maximum(T* a, T* b) {
 return (*a > *b) ? a : b;
}
```

### Template Parameters with Expressions

Non-type template parameters allow passing compile-time constants as template arguments:

```cpp
template<typename T, int size>
T sum(T arr[]) {
 T total = T();
 for(int i = 0; i < size; i++) {
 total += arr[i];
 }
 return total;
}
```

This feature is particularly useful for fixed-size array operations and compile-time computations.

## Examples

### Example 1: Generic Swap Function

Write a generic function to swap two values of any data type.

**Solution:**

```cpp
#include <iostream>
using namespace std;

// Generic swap function using templates
template<typename T>
void swap(T& a, T& b) {
 T temp = a;
 a = b;
 b = temp;
}

int main() {
 // Swap integers
 int x = 10, y = 20;
 cout << "Before swap - x: " << x << ", y: " << y << endl;
 swap(x, y);
 cout << "After swap - x: " << x << ", y: " << y << endl;

 // Swap doubles
 double p = 3.14, q = 2.71;
 cout << "\nBefore swap - p: " << p << ", q: " << q << endl;
 swap(p, q);
 cout << "After swap - p: " << p << ", q: " << q << endl;

 // Swap characters
 char c1 = 'A', c2 = 'Z';
 cout << "\nBefore swap - c1: " << c1 << ", c2: " << c2 << endl;
 swap(c1, c2);
 cout << "After swap - c1: " << c1 << ", c2: " << c2 << endl;

 return 0;
}
```

**Output:**

```
Before swap - x: 10, y: 20
After swap - x: 20, y: 10

Before swap - p: 3.14, q: 2.71
After swap - p: 2.71, q: 3.14

Before swap - c1: A, c2: Z
After swap - c1: Z, c2: A
```

The function template works by taking references to two variables of type T, creating a temporary variable of the same type, and performing the swap operation. The compiler generates three separate functions at compile-time, one for each data type used.

### Example 2: Generic Array Maximum Finder

Write a function template to find the maximum element in an array.

**Solution:**

```cpp
#include <iostream>
using namespace std;

// Function template to find maximum element in array
template<typename T>
T findMax(T arr[], int n) {
 T max = arr[0];
 for(int i = 1; i < n; i++) {
 if(arr[i] > max) {
 max = arr[i];
 }
 }
 return max;
}

int main() {
 // Integer array
 int intArr[] = {5, 8, 2, 15, 7, 1, 9};
 int intSize = sizeof(intArr) / sizeof(intArr[0]);
 cout << "Maximum integer: " << findMax(intArr, intSize) << endl;

 // Double array
 double doubleArr[] = {3.5, 7.2, 1.8, 9.5, 2.3};
 int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);
 cout << "Maximum double: " << findMax(doubleArr, doubleSize) << endl;

 // Character array
 char charArr[] = {'a', 'z', 'm', 'b', 'x'};
 int charSize = sizeof(charArr) / sizeof(charArr[0]);
 cout << "Maximum character: " << findMax(charArr, charSize) << endl;

 return 0;
}
```

**Output:**

```
Maximum integer: 15
Maximum double: 9.5
Maximum character: z
```

This example demonstrates how the same function template can handle different array types. The template parameter T is deduced from the array type, and the comparison operator (>) must be defined for type T to work correctly.

### Example 3: Multiple Template Parameters with Return Type

Write a generic function that accepts two different types and returns a result based on their combination.

**Solution:**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Template with multiple type parameters
template<typename T1, typename T2>
class Pair {
public:
 T1 first;
 T2 second;
 Pair(T1 f, T2 s) : first(f), second(s) {}
};

// Function to create a Pair
template<typename T1, typename T2>
Pair<T1, T2> makePair(T1 a, T2 b) {
 return Pair<T1, T2>(a, b);
}

// Generic function with different return type
template<typename R, typename T1, typename T2>
R addAndConvert(T1 a, T2 b) {
 return static_cast<R>(a + b);
}

int main() {
 // Using makePair
 auto p1 = makePair(10, "Hello");
 cout << "First: " << p1.first << ", Second: " << p1.second << endl;

 auto p2 = makePair(3.14, 100);
 cout << "First: " << p2.first << ", Second: " << p2.second << endl;

 // Using conversion function
 int result1 = addAndConvert<int>(5.7, 3.2);
 cout << "\nInteger result: " << result1 << endl;

 double result2 = addAndConvert<double>(10, 20);
 cout << "Double result: " << result2 << endl;

 return 0;
}
```

**Output:**

```
First: 10, Second: Hello
First: 3.14, Second: 100

Integer result: 8
Double result: 30
```

This example demonstrates multiple template parameters, explicit template argument specification, and automatic type conversion between different numeric types during template instantiation.

## Exam Tips

1. **Understand Template Syntax**: Remember that `typename` and `class` are interchangeable in template parameter declarations. The syntax `template<class T>` and `template<typename T>` are equivalent.

2. **Template Argument Deduction**: The compiler automatically deduces template arguments from function arguments. Know when explicit specification is necessary—when return types cannot be deduced or when non-type parameters are used.

3. **Distinguish Overloading from Specialization**: Function template overloading uses different template parameter lists, while specialization uses `template<>` with specific type arguments. Remember that function templates cannot be partially specialized.

4. **Type Safety in Generic Functions**: Generic functions require that operations used (like comparison operators, arithmetic operators) be defined for the type being used. This is a common source of compilation errors.

5. **Performance Benefits**: Emphasize in exams that templates provide performance benefits similar to manually written type-specific code because template instantiation occurs at compile-time, not runtime.

6. **Common Applications**: Be familiar with common generic function patterns: swap, comparison, searching, and arithmetic operations. These frequently appear in practical questions.

7. **STL Connection**: Understand that STL algorithms like `sort`, `find`, and `for_each` are implemented using function templates and are crucial for the next module.

8. **Error Interpretation**: Learn to interpret template-related compiler errors, which often indicate type mismatches or missing operator definitions for template type parameters.
