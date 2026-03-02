# Template Functions and Classes in C++

## Introduction

In the world of software development, writing duplicate code for similar operations on different data types is both inefficient and error-prone. Imagine having to write separate functions to find the maximum of two integers, two floats, and two characters—each essentially performing the same logical operation. This is where **templates** in C++ come to the rescue, embodying the powerful paradigm of **generic programming**.

Templates are a cornerstone of modern C++ and were introduced to enable developers to write reusable, type-safe code without sacrificing performance. They allow you to write a single definition that works with multiple data types, with the compiler generating the appropriate code at compile-time. This compile-time polymorphism (also known as parametric polymorphism) ensures zero runtime overhead compared to runtime polymorphism mechanisms like virtual functions.

For University of Delhi's BSc (H) Computer Science students, mastering templates is essential not only for academic success but also for understanding the Standard Template Library (STL), which forms the backbone of competitive programming and industry-grade C++ development. This topic carries significant weight in end-semester examinations, typically accounting for 10-15 marks.

## Key Concepts

### 1. Template Functions

A **template function** defines a family of functions with the same logic but different parameter types. The syntax uses the `template` keyword followed by a parameter list enclosed in angle brackets.

**Syntax:**
```cpp
template <typename T>
return_type function_name(parameters) {
    // function body
}
```

You can also use `class` instead of `typename`—both are functionally equivalent:
```cpp
template <class T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}
```

The compiler performs **template argument deduction** to infer the type when you call the function:
```cpp
int x = 5, y = 10;
cout << maximum(x, y);          // T deduced as int
cout << maximum(3.14, 2.71);    // T deduced as double
cout << maximum('A', 'Z');      // T deduced as char
```

### 2. Template Classes

Similar to functions, **template classes** allow you to create generic containers and data structures. A classic example is a generic array or stack class.

**Syntax:**
```cpp
template <typename T>
class ClassName {
private:
    T member;
public:
    T getMember();
    void setMember(T value);
};
```

**Implementation outside the class:**
```cpp
template <typename T>
T ClassName<T>::getMember() {
    return member;
}
```

**Instantiation:**
```cpp
Stack<int> intStack;
Stack<string> stringStack;
Stack<double> doubleStack;
```

### 3. Template Parameters

Templates support three types of parameters:

**a) Type Parameters (typename/class):**
```cpp
template <typename T>
```

**b) Non-Type Parameters:**
These must be compile-time constants—integers, pointers, or references:
```cpp
template <typename T, int size>
class Array {
    T arr[size];
public:
    int getSize() { return size; }
};

Array<int, 100> fixedArray;
```

**c) Default Type Parameters:**
```cpp
template <typename T = int>
class DefaultExample {
    T value;
};
DefaultExample<> obj;  // Uses int by default
```

### 4. Multiple Template Parameters

You can have multiple template parameters:
```cpp
template <typename T1, typename T2>
class Pair {
    T1 first;
    T2 second;
public:
    Pair(T1 f, T2 s) : first(f), second(s) {}
    void display() { cout << first << " " << second; }
};

Pair<string, int> p("Age", 25);
```

### 5. Template Specialization

When you need special behavior for a specific type, use **template specialization**:

**Full Specialization:**
```cpp
template <>
class Data<char> {
public:
    void process(char c) {
        cout << "Processing char: " << c << endl;
    }
};
```

**Partial Specialization (for classes only):**
```cpp
template <typename T>
class PointerWrapper<T*> {
    // Specialized for pointer types
};
```

## Examples

### Example 1: Generic Maximum Function

**Problem:** Write a template function to find the maximum of two values.

**Solution:**
```cpp
#include <iostream>
using namespace std;

template <typename T>
T findMaximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int i1 = 10, i2 = 20;
    cout << "Max of integers: " << findMaximum(i1, i2) << endl;
    
    double d1 = 3.14, d2 = 2.71;
    cout << "Max of doubles: " << findMaximum(d1, d2) << endl;
    
    string s1 = "Apple", s2 = "Banana";
    cout << "Max of strings: " << findMaximum(s1, s2) << endl;
    
    return 0;
}
```

**Output:**
```
Max of integers: 20
Max of doubles: 3.14
Max of strings: Banana
```

### Example 2: Generic Stack Class

**Problem:** Implement a generic stack class that can store any data type.

**Solution:**
```cpp
#include <iostream>
using namespace std;

template <typename T, int MAX = 100>
class Stack {
private:
    T arr[MAX];
    int top;
public:
    Stack() { top = -1; }
    
    bool push(T value) {
        if (top >= MAX - 1) {
            cout << "Stack Overflow!" << endl;
            return false;
        }
        arr[++top] = value;
        return true;
    }
    
    T pop() {
        if (top < 0) {
            cout << "Stack Underflow!" << endl;
            return T();  // Return default value
        }
        return arr[top--];
    }
    
    bool isEmpty() { return (top < 0); }
};

int main() {
    Stack<int> intStack;
    intStack.push(10);
    intStack.push(20);
    cout << "Popped: " << intStack.pop() << endl;
    
    Stack<string> stringStack;
    stringStack.push("Hello");
    stringStack.push("World");
    cout << "Popped: " << stringStack.pop() << endl;
    
    return 0;
}
```

### Example 3: Template Specialization for Character Processing

**Problem:** Create a template class with specialized behavior for character types.

**Solution:**
```cpp
#include <iostream>
#include <string>
using namespace std;

template <typename T>
class Processor {
public:
    void process(T value) {
        cout << "Processing value: " << value << endl;
    }
};

// Template specialization for char
template <>
class Processor<char> {
public:
    void process(char value) {
        cout << "Processing character: " << value 
             << " (ASCII: " << int(value) << ")" << endl;
    }
};

int main() {
    Processor<int> intProc;
    intProc.process(42);
    
    Processor<string> strProc;
    strProc.process("Template");
    
    Processor<char> charProc;
    charProc.process('A');
    
    return 0;
}
```

## Exam Tips

1. **Remember the syntax:** The `template` keyword must precede the function/class definition. Both `typename` and `class` are interchangeable for type parameters.

2. **Template instantiation happens at compile-time:** Unlike runtime polymorphism, templates generate code during compilation. This is why template errors are compile-time errors.

3. **Non-type parameters must be constants:** Remember that non-type template parameters (like array size) must be compile-time constants—variables won't work.

4. **All template code typically goes in header files:** Since the compiler needs to see the complete template definition to generate code, template definitions are usually placed in header files (.hpp or .h).

5. **Distinguish between function and class templates:** Function templates can use implicit type deduction, while class templates always require explicit type specification during instantiation.

6. **Specialization syntax matters:** Full specialization uses `template <>`, while partial specialization requires specifying which parameters remain templated.

7. **STL uses templates extensively:** Understanding templates helps in comprehending vector, map, set, and other STL containers—frequently tested in exams.

8. **Common exam questions:** Expect questions on writing template functions for sorting/swapping, implementing generic data structures like linked lists or stacks, and explaining template specialization.

9. **Remember the difference between overloading and templates:** Overloading creates multiple functions at compile-time explicitly; templates create functions automatically based on usage.

10. **Code tracing questions:** Be prepared to trace what happens when template functions are called with different types—pay attention to type compatibility.