# Generic Classes in C++ (Templates)

## Introduction

Generic classes, also known as class templates in C++, are one of the most powerful features of the language that enable polymorphism at compile-time. Also called parametric polymorphism, generic classes allow developers to write flexible and reusable code without sacrificing type safety. Instead of writing separate classes for different data types (such as integer, float, or custom objects), we can create a single class template that works with any data type.

The concept of generics became essential in modern C++ programming because it eliminates code duplication while maintaining the performance benefits of compile-time polymorphism. Unlike runtime polymorphism (which uses virtual functions and incurs runtime overhead), template-based generics are resolved at compile-time, resulting in zero runtime overhead. This makes generic classes particularly valuable for implementing data structures like stacks, queues, linked lists, and vectors where the same logic applies regardless of the element type.

In the context of the university's Object Oriented Programming with C++ curriculum, understanding generic classes is crucial for developing industrial-strength applications. Major topics include function templates, class templates, template parameters (type and non-type), default template arguments, and template specialization. These concepts form the foundation for the Standard Template Library (STL), which is extensively used in modern software development.

## Key Concepts

### 1. Class Template Basics

A class template defines a blueprint for creating classes where one or more types can be parameterized. The syntax uses the `template` keyword followed by a parameter list enclosed in angle brackets.

```cpp
template <class T>
class Stack {
private:
 T arr[100];
 int top;
public:
 Stack() { top = -1; }
 void push(T element);
 T pop();
 bool isEmpty();
};
```

In this example, `T` is a template parameter that acts as a placeholder for any data type. When the compiler encounters code like `Stack<int>`, it generates a concrete class with `T` replaced by `int`.

### 2. Class Templates with Multiple Parameters

Class templates can accept multiple template parameters, which can be either type parameters or non-type parameters.

```cpp
template <class T1, class T2>
class Pair {
private:
 T1 first;
 T2 second;
public:
 Pair(T1 a, T2 b) : first(a), second(b) {}
 T1 getFirst() { return first; }
 T2 getSecond() { return second; }
};
```

Multiple type parameters allow for creating flexible generic containers that can hold heterogeneous but related data types.

### 3. Default Template Arguments

Similar to function default arguments, template parameters can have default values. This feature provides backward compatibility and simplifies usage.

```cpp
template <class T = int, int MAX_SIZE = 100>
class Array {
private:
 T elements[MAX_SIZE];
 int size;
public:
 Array() { size = 0; }
 void add(T element) {
 if (size < MAX_SIZE)
 elements[size++] = element;
 }
};
```

With default arguments, we can use `Array<>` (defaults to int with size 100), `Array<double>` (double with size 100), or `Array<string, 50>` (string with size 50).

### 4. Non-Type Template Parameters

Non-type template parameters allow passing compile-time constant values as template arguments. These are particularly useful for specifying sizes and capacities.

```cpp
template <class T, int SIZE = 10>
class CircularBuffer {
private:
 T buffer[SIZE];
 int head, tail, count;
public:
 CircularBuffer() : head(0), tail(0), count(0) {}
 void insert(T item);
 T remove();
 bool isFull() { return count == SIZE; }
};
```

Non-type parameters must be integral types, pointers, or references. They enable compile-time size allocation and optimization opportunities.

### 5. Member Function Templates

Member functions of a class template are themselves templates. They become instantiated only when called with specific types.

```cpp
template <class T>
class Container {
private:
 T data;
public:
 Container(T d) : data(d) {}

 template <class U>
 U convert() {
 return static_cast<U>(data);
 }
};
```

The `convert()` function is a member template that can convert the contained data to any specified type U.

### 6. Template Specialization

Template specialization allows providing different implementations for specific types. There are two types: full specialization and partial specialization.

**Full Specialization:**

```cpp
template <>
class Storage<bool> {
private:
 bool value;
public:
 Storage(bool v) { value = v; }
 void display() {
 std::cout << (value ? "true" : "false");
 }
};
```

**Partial Specialization:**

```cpp
template <class T>
class Storage<T*> {
private:
 void* ptr;
public:
 Storage(T* p) : ptr(p) {}
 T* get() { return static_cast<T*>(ptr); }
};
```

Partial specialization is particularly useful for pointer types, arrays, and references.

### 7. Class Template with Multiple Parameters and Default

```cpp
template <typename T1 = int, typename T2 = double, int MAX = 50>
class BookStore {
private:
 T1 bookId;
 T2 price;
 T1 inventory[MAX];
 int count;
public:
 BookStore(T1 id, T2 p) : bookId(id), price(p), count(0) {}
 void addInventory(T1 id);
 T1 getBookId() { return bookId; }
 T2 getPrice() { return price; }
};
```

## Examples

### Example 1: Generic Stack Implementation

**Problem:** Implement a generic stack class that can store elements of any data type and demonstrate push and pop operations.

**Solution:**

```cpp
#include <iostream>
using namespace std;

template <class T>
class Stack {
private:
 T *arr;
 int top;
 int capacity;
public:
 Stack(int cap = 10) {
 capacity = cap;
 arr = new T[capacity];
 top = -1;
 }

 ~Stack() {
 delete[] arr;
 }

 void push(T element) {
 if (top >= capacity - 1) {
 cout << "Stack Overflow!" << endl;
 return;
 }
 arr[++top] = element;
 }

 T pop() {
 if (top < 0) {
 cout << "Stack Underflow!" << endl;
 return T(); // Return default value
 }
 return arr[top--];
 }

 T peek() {
 if (top < 0) {
 return T();
 }
 return arr[top];
 }

 bool isEmpty() {
 return top < 0;
 }

 int size() {
 return top + 1;
 }
};

int main() {
 Stack<int> intStack(5);
 Stack<string> stringStack(5);

 // Integer stack operations
 intStack.push(10);
 intStack.push(20);
 intStack.push(30);

 cout << "Integer Stack:" << endl;
 cout << "Pop: " << intStack.pop() << endl;
 cout << "Peek: " << intStack.peek() << endl;

 // String stack operations
 stringStack.push("Hello");
 stringStack.push("World");

 cout << "\nString Stack:" << endl;
 cout << "Pop: " << stringStack.pop() << endl;
 cout << "Pop: " << stringStack.pop() << endl;

 return 0;
}
```

**Output:**

```
Integer Stack:
Pop: 30
Peek: 20

String Stack:
Pop: World
Pop: Hello
```

### Example 2: Generic Pair Class with Specialization

**Problem:** Create a generic pair class and demonstrate full template specialization for character pairs.

**Solution:**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Primary template
template <class T1, class T2>
class Pair {
private:
 T1 first;
 T2 second;
public:
 Pair(T1 f, T2 s) : first(f), second(s) {}
 void display() {
 cout << "First: " << first << ", Second: " << second << endl;
 }
 T1 getFirst() { return first; }
 T2 getSecond() { return second; }
};

// Full specialization for char, char
template <>
class Pair<char, char> {
private:
 char first;
 char second;
public:
 Pair(char f, char s) : first(f), second(s) {}
 void display() {
 cout << "Character Pair: '" << first << "' and '" << second << "'" << endl;
 }
 char getFirst() { return first; }
 char getSecond() { return second; }
 string toString() {
 string result;
 result += first;
 result += second;
 return result;
 }
};

int main() {
 // Using primary template
 Pair<int, string> p1(101, "university");
 Pair<double, char> p2(3.14, 'A');

 cout << "Using primary template:" << endl;
 p1.display();
 p2.display();

 // Using specialized template
 Pair<char, char> p3('A', 'Z');
 cout << "\nUsing specialized template:" << endl;
 p3.display();
 cout << "Combined: " << p3.toString() << endl;

 return 0;
}
```

### Example 3: Generic Matrix Class with Non-Type Parameters

**Problem:** Implement a generic matrix class that supports matrix multiplication with compile-time dimension checking.

**Solution:**

```cpp
#include <iostream>
using namespace std;

template <class T, int ROWS = 2, int COLS = 2>
class Matrix {
private:
 T data[ROWS][COLS];
public:
 Matrix() {
 for (int i = 0; i < ROWS; i++)
 for (int j = 0; j < COLS; j++)
 data[i][j] = T();
 }

 void setElement(int row, int col, T value) {
 if (row >= 0 && row < ROWS && col >= 0 && col < COLS)
 data[row][col] = value;
 }

 T getElement(int row, int col) {
 if (row >= 0 && row < ROWS && col >= 0 && col < COLS)
 return data[row][col];
 return T();
 }

 void display() {
 for (int i = 0; i < ROWS; i++) {
 for (int j = 0; j < COLS; j++) {
 cout << data[i][j] << "\t";
 }
 cout << endl;
 }
 }

 template <int COLS2>
 Matrix<T, ROWS, COLS2> multiply(Matrix<T, COLS, COLS2> &other) {
 Matrix<T, ROWS, COLS2> result;

 for (int i = 0; i < ROWS; i++) {
 for (int j = 0; j < COLS2; j++) {
 T sum = T();
 for (int k = 0; k < COLS; k++) {
 sum = sum + data[i][k] * other.getElement(k, j);
 }
 result.setElement(i, j, sum);
 }
 }
 return result;
 }
};

int main() {
 Matrix<int, 2, 2> m1;
 Matrix<int, 2, 2> m2;

 // Initialize m1
 m1.setElement(0, 0, 1); m1.setElement(0, 1, 2);
 m1.setElement(1, 0, 3); m1.setElement(1, 1, 4);

 // Initialize m2
 m2.setElement(0, 0, 5); m2.setElement(0, 1, 6);
 m2.setElement(1, 0, 7); m2.setElement(1, 1, 8);

 cout << "Matrix 1:" << endl;
 m1.display();

 cout << "\nMatrix 2:" << endl;
 m2.display();

 cout << "\nMatrix 1 * Matrix 2:" << endl;
 Matrix<int, 2, 2> result = m1.multiply(m2);
 result.display();

 return 0;
}
```

## Exam Tips

1. **Template Syntax**: Remember the correct syntax - `template <class T>` or `template <typename T>`. Both keywords are interchangeable for type parameters.

2. **Instantiation**: Class templates are not compiled into executable code until they are instantiated with specific types. The compiler generates code on-demand.

3. **Separation of Declaration and Definition**: When implementing template class member functions outside the class declaration, the `template` keyword must precede both the class definition and function definitions.

4. **Default Arguments**: Template default arguments must follow non-default arguments. For example: `template <class T = int, int SIZE = 100>` is valid, but `template <class T, class U = int>` is not if used as `Template<int>`.

5. **Non-Type Parameters**: Remember that non-type template parameters must be compile-time constants (integral types, pointers, or references).

6. **Template Specialization**: Use `template <>` for full specialization and `template <class T>` for partial specialization. Full specialization completely replaces the template for specific types.

7. **STL Connection**: Many STL containers (vector, stack, queue, map) are implemented using class templates. Understanding templates helps in using STL effectively.

8. **Common Errors**: Avoid using floating-point types as non-type template parameters, and remember that each instantiation creates a separate class.
