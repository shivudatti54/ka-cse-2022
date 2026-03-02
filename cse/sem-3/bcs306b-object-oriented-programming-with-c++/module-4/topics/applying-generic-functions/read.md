# Applying Generic Functions in C++

## Introduction

Generic programming is a powerful paradigm that allows developers to write flexible and reusable code without sacrificing type safety. In C++, generic functions, commonly known as function templates, enable the creation of functions that can operate on different data types while maintaining the same logic. This approach significantly reduces code duplication and enhances maintainability, making it an essential concept for modern C++ programming.

The concept of generic functions becomes particularly valuable when we need to implement algorithms that work identically across multiple data types. For instance, a sorting algorithm or a maximum finding function should work equally well with integers, floats, or user-defined objects. Rather than writing separate functions for each type, function templates allow us to define a single blueprint that the compiler instantiates for specific types as needed. This topic explores the mechanisms of template functions, their usage, and practical applications in object-oriented programming with C++.

## Key Concepts

### Function Templates

A function template defines a family of functions with different parameter types. The syntax uses the `template` keyword followed by a template parameter list enclosed in angle brackets:

```cpp
template<typename T>
T maximum(T a, T b) {
 return (a > b) ? a : b;
}
```

Here, `typename T` (or `class T`) represents a placeholder for the data type. The compiler generates actual function instances when the function is called with specific types. This process is called template instantiation.

### Template Parameters

Function templates can have multiple template parameters:

```cpp
template<typename T1, typename T2>
void display(T1 a, T2 b) {
 std::cout << a << " " << b << std::endl;
}
```

Default template arguments are also supported in C++:

```cpp
template<typename T = int>
T getValue() {
 return T();
}
```

### Function Template Overloading

Regular functions and function templates can coexist through overloading. The compiler performs overload resolution to determine which version to call:

```cpp
// Function template
template<typename T>
T square(T x) {
 return x * x;
}

// Regular function for specific behavior
double square(double x) {
 return x * x * 3.14159;
}
```

### Template Argument Deduction

The compiler automatically deduces the template arguments based on the function arguments:

```cpp
template<typename T>
void swap(T& a, T& b) {
 T temp = a;
 a = b;
 b = temp;
}

int x = 5, y = 10;
swap(x, y); // Compiler deduces T as int
```

### Explicit Template Arguments

Sometimes automatic deduction fails or we need specific types:

```cpp
template<typename T>
T add(T a, T b) {
 return a + b;
}

int result = add<int>(5.5, 10.3); // Explicitly specify T as int
```

### Non-Type Template Parameters

Templates can accept constant values as parameters:

```cpp
template<typename T, int size>
class Array {
 T arr[size];
public:
 int getSize() { return size; }
};

Array<int, 10> intArray;
```

## Examples

### Example 1: Generic Maximum Function

**Problem:** Create a function template to find the maximum of two values.

```cpp
#include <iostream>
using namespace std;

template<typename T>
T findMaximum(T a, T b) {
 return (a > b) ? a : b;
}

int main() {
 int i1 = 5, i2 = 10;
 double d1 = 3.14, d2 = 2.71;
 char c1 = 'A', c2 = 'Z';

 cout << "Maximum of integers: " << findMaximum(i1, i2) << endl;
 cout << "Maximum of doubles: " << findMaximum(d1, d2) << endl;
 cout << "Maximum of chars: " << findMaximum(c1, c2) << endl;

 return 0;
}
```

**Output:**

```
Maximum of integers: 10
Maximum of doubles: 3.14
Maximum of chars: Z
```

**Explanation:** The compiler generates three separate functions—one for `int`, one for `double`, and one for `char`—each performing the same logical operation.

### Example 2: Generic Array Sorting

**Problem:** Implement a generic bubble sort function that works with any data type.

```cpp
#include <iostream>
using namespace std;

template<typename T>
void bubbleSort(T arr[], int n) {
 for (int i = 0; i < n-1; i++) {
 for (int j = 0; j < n-i-1; j++) {
 if (arr[j] > arr[j+1]) {
 T temp = arr[j];
 arr[j] = arr[j+1];
 arr[j+1] = temp;
 }
 }
 }
}

template<typename T>
void printArray(T arr[], int n) {
 for (int i = 0; i < n; i++) {
 cout << arr[i] << " ";
 }
 cout << endl;
}

int main() {
 int intArr[] = {64, 34, 25, 12, 22, 11, 90};
 double doubleArr[] = {3.5, 1.2, 5.8, 2.1, 4.9};

 int n1 = sizeof(intArr) / sizeof(intArr[0]);
 int n2 = sizeof(doubleArr) / sizeof(doubleArr[0]);

 cout << "Integer array before sort: ";
 printArray(intArr, n1);
 bubbleSort(intArr, n1);
 cout << "Integer array after sort: ";
 printArray(intArr, n1);

 cout << "Double array before sort: ";
 printArray(doubleArr, n2);
 bubbleSort(doubleArr, n2);
 cout << "Double array after sort: ";
 printArray(doubleArr, n2);

 return 0;
}
```

**Output:**

```
Integer array before sort: 64 34 25 12 22 11 90
Integer array after sort: 11 12 22 25 34 64 90
Double array before sort: 3.5 1.2 5.8 2.1 4.9
Double array after sort: 1.2 2.1 3.5 4.9 5.8
```

### Example 3: Generic Function with Multiple Types

**Problem:** Create a function that compares two values and returns information about their relationship.

```cpp
#include <iostream>
#include <string>
using namespace std;

template<typename T1, typename T2>
class Result {
public:
 T1 first;
 T2 second;
 string relationship;

 Result(T1 f, T2 s, string r) : first(f), second(s), relationship(r) {}

 void display() {
 cout << "First Value: " << first << endl;
 cout << "Second Value: " << second << endl;
 cout << "Relationship: " << relationship << endl;
 }
};

template<typename T1, typename T2>
Result<T1, T2> compare(T1 a, T2 b) {
 if (a > b)
 return Result<T1, T2>(a, b, "First is greater");
 else if (a < b)
 return Result<T1, T2>(a, b, "Second is greater");
 else
 return Result<T1, T2>(a, b, "Both are equal");
}

int main() {
 auto r1 = compare(10, 20);
 r1.display();
 cout << endl;

 auto r2 = compare(5.5, 3.3);
 r2.display();
 cout << endl;

 auto r3 = compare(100, 100);
 r3.display();

 return 0;
}
```

**Output:**

```
First Value: 10
Second Value: 20
Relationship: Second is greater

First Value: 5.5
Second Value: 3.3
Relationship: First is greater

First Value: 100
Second Value: 100
Relationship: Both are equal
```

## Exam Tips

1. **Template Syntax**: Remember the exact syntax `template<typename T>` or `template<class T>` - both are equivalent in function templates.

2. **Template Instantiation**: Understand that templates are not actual code until instantiated. The compiler generates code only when the template is called with specific types.

3. **Type Deduction**: The compiler automatically deduces template arguments from function parameters in most cases, but explicit specification may be needed when deduction is ambiguous.

4. **Overloading Resolution**: When both a template function and a regular function match, the regular function takes precedence (specialization).

5. **Default Arguments**: Template parameters can have defaults, similar to function parameters, providing flexibility in template usage.

6. **Separation of Declaration and Definition**: When templates are used across multiple files, the entire template definition must be visible at the point of instantiation, typically using header files.

7. **Type Compatibility**: Ensure that operations used within templates are valid for all types that might be instantiated, or use appropriate constraints (concepts in C++20).
