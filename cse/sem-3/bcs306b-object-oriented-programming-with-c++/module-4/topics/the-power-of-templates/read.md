# The Power of Templates in C++

## Introduction

Templates are one of the most powerful features of C++ that enable generic programming. Introduced in the C++ Standard Template Library (STL), templates provide a mechanism for creating reusable code that works with any data type. Unlike other programming languages that require separate implementations for each data type, C++ templates allow programmers to write a single, abstract definition that can be instantiated for any specific type at compile-time. This capability significantly reduces code duplication, improves maintainability, and enhances program performance through early type checking and optimization.

The concept of templates addresses a fundamental challenge in software development: writing algorithms and data structures that are independent of the data types they operate on. Consider a simple swap function - without templates, you would need separate implementations for integers, floats, characters, and any other type. With templates, a single function template can handle all these cases elegantly. This generic approach forms the foundation of modern C++ programming and is extensively used in the STL containers, algorithms, and iterators.

In the context of the university's Object-Oriented Programming with C++ course, understanding templates is essential for mastering STL and writing efficient, type-safe code. Templates represent the bridge between static typing and generic programming, offering the best of both worlds: compile-time type safety and runtime efficiency.

## Key Concepts

### Function Templates

A function template defines a family of functions with different parameter types. The compiler generates specific function instances (specializations) based on the arguments passed during function calls. The syntax for declaring a function template uses the `template` keyword followed by a template parameter list enclosed in angle brackets.

```cpp
template<typename T>
T maximum(T a, T b) {
 return (a > b) ? a : b;
}
```

The `typename` keyword (or alternatively `class`) introduces a type parameter `T` that acts as a placeholder for the actual type. When the compiler encounters a call like `maximum(5, 10)`, it automatically generates a specialization where `T` is replaced with `int`. This process is called template argument deduction.

Function templates can have multiple type parameters, and you can also include non-type parameters such as integers, pointers, or references:

```cpp
template<typename T, int size>
T multiply(T value) {
 return value * size;
}
```

### Class Templates

Class templates extend the concept of generics to user-defined types, enabling the creation of parameterized families of classes. This is particularly useful for implementing generic containers like stacks, queues, vectors, and linked lists. The syntax follows the same pattern as function templates.

```cpp
template<typename T>
class Stack {
private:
 T arr[100];
 int top;
public:
 Stack() : top(-1) {}
 void push(T element);
 T pop();
 bool isEmpty();
};
```

Class templates can also have default template arguments, providing default types when not specified:

```cpp
template<typename T = int, int capacity = 100>
class DynamicArray {
 // Implementation
};
```

### Template Specialization

Sometimes you need a different implementation for a specific type. Template specialization allows you to override the generic template for particular types. There are two types: full (complete) specialization and partial specialization.

Full specialization provides a specific implementation for a particular type:

```cpp
template<>
class Stack<bool> {
 // Specialized implementation for bool
 // that uses bit manipulation for efficiency
};
```

Partial specialization is available only for class templates and allows specialization of some template parameters while leaving others generic:

```cpp
template<typename T>
class PointerContainer<T*> {
 // Specialized for pointer types
};
```

### Variadic Templates

C++11 introduced variadic templates that accept a variable number of arguments. This powerful feature enables recursive template recursion and perfect forwarding:

```cpp
template<typename T>
T sum(T value) {
 return value;
}

template<typename T, typename... Args>
T sum(T first, Args... args) {
 return first + sum(args...);
}
```

## Examples

### Example 1: Generic Array Sorting

```cpp
#include <iostream>
using namespace std;

template<typename T>
void bubbleSort(T arr[], int n) {
 for (int i = 0; i < n - 1; i++) {
 for (int j = 0; j < n - i - 1; j++) {
 if (arr[j] > arr[j + 1]) {
 T temp = arr[j];
 arr[j] = arr[j + 1];
 arr[j + 1] = temp;
 }
 }
 }
}

template<typename T>
void display(T arr[], int n) {
 for (int i = 0; i < n; i++) {
 cout << arr[i] << " ";
 }
 cout << endl;
}

int main() {
 int intArr[] = {64, 34, 25, 12, 22, 11, 90};
 double doubleArr[] = {64.5, 34.2, 25.1, 12.5};

 int n1 = sizeof(intArr) / sizeof(intArr[0]);
 int n2 = sizeof(doubleArr) / sizeof(doubleArr[0]);

 cout << "Integer array before sorting: ";
 display(intArr, n1);
 bubbleSort(intArr, n1);
 cout << "Integer array after sorting: ";
 display(intArr, n1);

 cout << "\nDouble array before sorting: ";
 display(doubleArr, n2);
 bubbleSort(doubleArr, n2);
 cout << "Double array after sorting: ";
 display(doubleArr, n2);

 return 0;
}
```

**Output:**

```
Integer array before sorting: 64 34 25 12 22 11 90
Integer array after sorting: 11 12 22 25 34 64 90

Double array before sorting: 64.5 34.2 25.1 12.5
Double array after sorting: 12.5 25.1 34.2 64.5
```

### Example 2: Generic Pair Class

```cpp
#include <iostream>
using namespace std;

template<typename T1, typename T2>
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
 Pair<int, string> student(101, "Amit");
 Pair<double, char> coordinates(45.5, 'N');
 Pair<string, string> dictionary("Hello", "A greeting");

 student.display();
 coordinates.display();
 dictionary.display();

 return 0;
}
```

**Output:**

```
First: 101, Second: Amit
First: 45.5, Second: N
First: Hello, Second: A greeting
```

### Example 3: Template Specialization for Character Handling

```cpp
#include <iostream>
#include <cstring>
using namespace std;

template<typename T>
T maximum(T a, T b) {
 return (a > b) ? a : b;
}

// Specialization for character pointers (C-style strings)
template<>
const char* maximum<const char*>(const char* a, const char* b) {
 return (strcmp(a, b) > 0) ? a : b;
}

int main() {
 int x = 10, y = 20;
 cout << "Max of integers: " << maximum(x, y) << endl;

 char c1 = 'A', c2 = 'Z';
 cout << "Max of chars: " << maximum(c1, c2) << endl;

 const char* str1 = "Apple";
 const char* str2 = "Banana";
 cout << "Max string: " << maximum(str1, str2) << endl;

 return 0;
}
```

**Output:**

```
Max of integers: 20
Max of chars: Z
Max string: Banana
```

## Exam Tips

1. **Template Syntax**: Remember the correct syntax: `template<typename T>` or `template<class T>`. Both `typename` and `class` are interchangeable for type parameters in modern C++.

2. **Template Argument Deduction**: The compiler automatically deduces template arguments from function arguments. For class templates, you must explicitly specify arguments unless default arguments are provided.

3. **Template vs. Macros**: Unlike C macros, templates provide type safety. The compiler performs type checking before generating code, preventing many runtime errors.

4. **Separation of Declaration and Definition**: When templates are used across multiple files, the entire template definition must be visible at the point of instantiation. This typically requires including the implementation in the header file.

5. **STL Foundation**: Most STL containers (vector, list, stack, queue) and algorithms are template-based. Understanding templates helps in effectively using the STL.

6. **Non-type Parameters**: Remember that template parameters can be values (integers, pointers) besides types. This enables creating fixed-size containers at compile time.

7. **Specialization Syntax**: For function templates, only full specialization is available. For class templates, both full and partial specialization are supported.

8. **Virtual Functions and Templates**: Templates cannot be virtual. This is a common misconception - virtual functions require fixed dispatch at runtime, while templates are resolved at compile time.

9. **Default Template Arguments**: Class templates can have default template arguments (like `template<typename T = int>`), but function templates cannot have default type arguments.

10. **Code Reusability**: The primary advantage of templates is code reusability without sacrificing performance - the generated code is as efficient as manually written type-specific code.
