# The typename and export Keywords in C++

## Introduction

The C++ programming language provides several powerful features for generic programming through templates. Among these, the `typename` and `export` keywords play crucial roles in template metaprogramming and code organization. Understanding these keywords is essential for any C++ developer, as they directly impact how templates are declared, defined, and instantiated.

The `typename` keyword was introduced in the C++ standard to resolve ambiguity between type names and static members within template contexts. Prior to its introduction, compilers could not distinguish whether a dependent name referred to a type or a data/function member. The `export` keyword, on the other hand, was designed to separate template declarations from their definitions, allowing for faster compilation. However, due to implementation difficulties and limited browser support, `export` was deprecated in C++11 and completely removed from the standard in C++17.

This topic is highly relevant for university examinations as questions on template syntax and proper usage of `typename` frequently appear in both internal assessments and end-semester examinations. A thorough understanding of these keywords will help you write correct, standards-compliant C++ code and avoid common template-related compilation errors.

## Key Concepts

### The typename Keyword

#### Purpose and Need

The `typename` keyword serves a specific purpose in C++ templates: it tells the compiler that a qualified name inside a template refers to a type, not a static member or enum value. This becomes necessary when dealing with dependent names—names that depend on template parameters.

Consider a scenario where you have a template class that contains a nested type. When accessing this nested type through a template parameter, the compiler cannot determine whether the name refers to a type or a static member without additional context.

#### Syntax and Usage

The general syntax for using `typename` is:

```cpp
template<typename T>
class MyClass {
 typename T::NestedType member; // T::NestedType is a type
};
```

The keyword `typename` precedes the qualified type name, indicating to the compiler that `T::NestedType` should be treated as a type rather than a static member.

#### Dependent Names and thetypename

When a name depends on a template parameter, it is called a dependent name. The compiler does not know whether a dependent name refers to a type or a value until the template is instantiated. The `typename` keyword provides the necessary disambiguation.

```cpp
template<typename Container>
void printFirstElement(Container& c) {
 // ERROR: iterator could be a type or a static member
 // Container::iterator it = c.begin();

 // CORRECT: using typename to specify it's a type
 typename Container::iterator it = c.begin();
 std::cout << *it << std::endl;
}
```

In this example, `Container::iterator` is a dependent name because it depends on the template parameter `Container`. Without the `typename` keyword, the compiler would not know whether `iterator` is a type (as in `std::vector<int>::iterator`) or a static data member.

#### Where typename is Required

The `typename` keyword is required in the following contexts:

1. **Nested type names**: When accessing typedefs, classes, or enums inside a template parameter type
2. **Return types**: When using dependent names as function return types
3. **Template arguments**: When using dependent names as template arguments
4. **Base class qualification**: When referring to types from base classes that depend on template parameters

```cpp
template<typename T>
class Derived : public Base<T> {
 // Required when referring to base class types
 typename Base<T>::value_type member;

 // Required in function return types
 typename std::map<T, int>::iterator findElement(const T& key);
};
```

#### Important Exceptions

Note that `typename` is not required in certain contexts where the compiler can infer the meaning:

- **Base class lists**: `class Derived : public T::BaseClass { };` (no typename needed)
- **Member initialization lists**: `Derived() : T::BaseClass() { }` (no typename needed)

However, when using the scope resolution operator (`::`) to access a type in a template context, `typename` is generally required.

### The export Keyword

#### Historical Context

The `export` keyword was introduced in C++03 as a mechanism to separate template declarations from their definitions. The primary goal was to improve compilation times by allowing template definitions to be compiled separately from their declarations.

When a template is declared with `export`, its definition could be provided in a different translation unit, and the compiler would not need to see the full definition until link time. This was intended to address the "header-only" requirement that plagues C++ template code.

#### Syntax

```cpp
// In header file
export template<typename T>
class MyTemplate {
 void memberFunction();
};

// Definition can be in a separate .cpp file
template<typename T>
void MyTemplate<T>::memberFunction() {
 // Implementation
}
```

#### Why export Was Deprecated and Removed

Despite its promising design, the `export` keyword faced several issues:

1. **Poor compiler support**: Very few compilers implemented `export` correctly. Only a handful of compilers, such as Comeau C++ and Intel C++, provided partial support.

2. **Complexity**: The implementation complexity for compilers was enormous, requiring sophisticated template instantiation management across translation units.

3. **Alternative solutions**: Header inclusion, though not ideal, worked adequately for most use cases. The inclusion model became the de facto standard.

4. **Linkage issues**: The keyword created subtle linkage and instantiation problems that were difficult to debug.

Due to these reasons, `export` was deprecated in C++11 and removed entirely from C++17. Modern C++ code should not use `export`.

#### Current Alternatives

Since `export` is no longer available, C++ developers use the traditional header inclusion model for templates. This means that template definitions are typically placed in header files and included wherever needed. While this can lead to longer compilation times, it is the standard approach in modern C++.

```cpp
// Traditional approach (current standard)
template<typename T>
class MyTemplate {
 void memberFunction();
};

// Usually placed in a .hpp or .h file
template<typename T>
void MyTemplate<T>::memberFunction() {
 // Implementation
}
```

## Examples

### Example 1: Using typename with Nested Types

**Problem**: Write a template function that accesses the value type of a container.

**Solution**:

```cpp
#include <iostream>
#include <vector>
#include <list>

template<typename Container>
void printSize(Container& c) {
 // Using typename to specify that value_type is a type
 typename Container::value_type element;

 // Or using std::iterator_traits for more generic code
 typedef typename std::iterator_traits<typename Container::iterator>::value_type ElemType;
 ElemType val = *c.begin();

 std::cout << "Container size: " << c.size() << std::endl;
 std::cout << "First element: " << val << std::endl;
}

int main() {
 std::vector<int> v = {10, 20, 30};
 std::list<double> l = {1.1, 2.2, 3.3};

 printSize(v);
 printSize(l);

 return 0;
}
```

**Explanation**: The `typename` keyword is essential when accessing `Container::value_type` because the compiler cannot determine whether this is a type or a static member until the template is instantiated with a specific container type.

### Example 2: Using typename in Template Template Parameters

**Problem**: Create a template that accepts only container types with specific properties.

**Solution**:

```cpp
#include <iostream>
#include <vector>
#include <deque>

template<typename T, template<typename, typename> class Container>
class Wrapper {
 Container<T, std::allocator<T>> data;
public:
 void add(const T& item) {
 data.push_back(item);
 }

 void display() {
 typename Container<T, std::allocator<T>>::iterator it;
 for (it = data.begin(); it != data.end(); ++it) {
 std::cout << *it << " ";
 }
 std::cout << std::endl;
 }
};

int main() {
 Wrapper<int, std::vector> w;
 w.add(5);
 w.add(10);
 w.add(15);
 w.display();

 return 0;
}
```

**Explanation**: The `typename` is required before `Container<T, std::allocator<T>>::iterator` because the compiler must be told that `iterator` is a nested type, not a static member variable or function.

### Example 3: Demonstrating the Difference Between typename and export

**Problem**: Explain why `export` was problematic and show the modern approach.

**Solution**:

```cpp
// OLD APPROACH (C++03 with export - NOT recommended)
// File: mytemplate.h (declaration)
// export template<typename T>
// class MyTemplate {
// void process();
// };

// File: mytemplate.cpp (definition - would not link properly in most compilers)
// template<typename T>
// void MyTemplate<T>::process() {
// // Implementation
// }

// MODERN APPROACH (C++11 and later)
// File: mytemplate.hpp
#ifndef MYTEMPLATE_HPP
#define MYTEMPLATE_HPP

template<typename T>
class MyTemplate {
public:
 void process();

 // Alternative: define inline
 void display() {
 std::cout << "Display called" << std::endl;
 }
};

// Definition in header (traditional approach)
template<typename T>
void MyTemplate<T>::process() {
 // Implementation here
 // This is the standard approach in modern C++
}

#endif

// Main program
#include "mytemplate.hpp"

int main() {
 MyTemplate<int> obj;
 obj.process();
 obj.display();
 return 0;
}
```

**Explanation**: The `export` keyword was intended to allow template definitions in separate files, but due to poor compiler support and complexity, it was removed. The modern approach uses header inclusion, which is universally supported.

## Exam Tips

1. **Remember the basic rule**: Use `typename` whenever you access a nested type through a template parameter using the scope resolution operator (`::`).

2. **Avoid export in answers**: If asked about `export`, explain that it was deprecated in C++11 and removed in C++17. Do not write code using `export` in examination answers.

3. **Common compilation error**: If you see an error like "need 'typename' before 'Type::Member'" or "dependent name is not a type," add the `typename` keyword before the dependent name.

4. **Where not to use typename**: Remember that `typename` is not needed in base class lists or member initialization lists.

5. **typedef and typename**: When using `typedef` with dependent names, you must also use `typename`:

```cpp
typedef typename T::value_type ValueType; // Correct
```

6. **using declarations**: Modern C++ allows using declarations that can simplify code:

```cpp
template<typename T>
using Ptr = typename T::pointer; // typename required here
```

7. **Short notes preparation**: Be prepared to write short notes on both keywords, explaining their purposes and the current standard practices.

8. **Difference between typename and class**: In template parameter lists, `typename` and `class` are interchangeable:

```cpp
template<typename T> // same as template<class T>
```

However, inside the template body, only `typename` can be used to declare types.
