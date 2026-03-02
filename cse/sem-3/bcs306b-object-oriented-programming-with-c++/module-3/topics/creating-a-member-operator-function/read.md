# Creating a Member Operator Function

## Introduction

Operator overloading is one of the most powerful features of C++ that allows programmers to redefine the behavior of existing operators for user-defined data types. When an operator is overloaded as a member function of a class, it provides an intuitive and natural way to perform operations on objects. This approach is particularly useful when the left operand of the operator is an object of the class for which the operator is being overloaded.

Member operator functions are defined inside the class scope and have implicit access to all member variables and functions of the class. This makes them ideal for operations where the left operand must be an object of the class. Understanding how to create member operator functions is essential for writing clean, expressive, and maintainable C++ code. In university examinations, this topic carries significant weightage as it tests the student's understanding of both C++ syntax and object-oriented design principles.

This module explores the syntax, implementation, and practical applications of member operator functions in C++. We will examine various operators that can be overloaded, the rules governing operator overloading, and common pitfalls that students should avoid.

## Key Concepts

### Syntax of Member Operator Function

An operator function is declared using the keyword `operator` followed by the operator symbol to be overloaded. The general syntax is:

```cpp
return_type operator op(argument_list)
{
 // function body
}
```

When implemented as a member function, the operator function takes one explicit argument if the operator is binary (two operands) and takes no arguments if the operator is unary. The left operand is implicitly the object (`this` pointer) through which the operator is called.

### Binary Operators as Member Functions

For binary operators implemented as member functions, the left operand is the calling object, and the right operand is passed as an argument. Consider the example of overloading the addition operator for a `Complex` class:

```cpp
class Complex {
private:
 float real;
 float imag;
public:
 Complex(float r = 0, float i = 0) : real(r), imag(i) {}

 Complex operator+(const Complex& obj) {
 Complex temp;
 temp.real = this->real + obj.real;
 temp.imag = this->imag + obj.imag;
 return temp;
 }
};
```

In this case, when we write `c3 = c1 + c2`, the compiler interprets it as `c3 = c1.operator+(c2)`.

### Unary Operators as Member Functions

Unary operators (like `++`, `--`, `-`, `!`) when overloaded as member functions take no arguments. The operand is the object itself. For instance:

```cpp
class Counter {
private:
 int count;
public:
 Counter(int c = 0) : count(c) {}

 Counter operator++() { // Pre-increment
 ++count;
 return *this;
 }

 Counter operator++(int) { // Post-increment
 Counter temp = *this;
 count++;
 return temp;
 }
};
```

The dummy `int` parameter in post-increment distinguishes it from pre-increment.

### Operators That Cannot Be Overloaded

Certain operators cannot be overloaded in C++: the scope resolution operator `::`, the member access operators `.` and `.*`, the ternary operator `?:``, and the `sizeof` operator. Understanding this limitation is crucial for exam success.

### Friend Functions vs Member Functions

While member operator functions are common, some situations require friend functions. When the left operand is not an object of your class (like `cout << obj`), you need a friend function. However, for operations where the left operand is always your class object, member functions are preferred as they provide encapsulation.

### Assignment Operator

The assignment operator `=` is implicitly provided by the compiler but should be overloaded when deep copying is required, especially for classes with dynamic memory allocation. A proper implementation:

```cpp
class String {
private:
 char* str;
 int length;
public:
 String(const char* s = "") {
 length = strlen(s);
 str = new char[length + 1];
 strcpy(str, s);
 }

 String& operator=(const String& obj) {
 if (this != &obj) {
 delete[] str;
 length = obj.length;
 str = new char[length + 1];
 strcpy(str, obj.str);
 }
 return *this;
 }
};
```

## Examples

### Example 1: Overloading + and - Operators for a Distance Class

**Problem:** Create a class Distance with member variables feet and inches. Overload the + and - operators to add and subtract two Distance objects.

**Solution:**

```cpp
#include <iostream>
using namespace std;

class Distance {
private:
 int feet;
 float inches;
public:
 Distance() : feet(0), inches(0) {}
 Distance(int f, float i) : feet(f), inches(i) {}

 void getData() {
 cout << "Enter feet: ";
 cin >> feet;
 cout << "Enter inches: ";
 cin >> inches;
 normalize();
 }

 void showData() const {
 cout << feet << "' " << inches << "\"";
 }

 void normalize() {
 if (inches >= 12) {
 feet += (int)(inches / 12);
 inches = inches - (int)(inches / 12) * 12;
 }
 }

 // Overloading + operator
 Distance operator+(const Distance& d2) const {
 Distance temp;
 temp.feet = feet + d2.feet;
 temp.inches = inches + d2.inches;
 temp.normalize();
 return temp;
 }

 // Overloading - operator
 Distance operator-(const Distance& d2) const {
 Distance temp;
 float total1 = feet * 12 + inches;
 float total2 = d2.feet * 12 + d2.inches;
 float diff = total1 - total2;
 temp.feet = (int)(diff / 12);
 temp.inches = diff - temp.feet * 12;
 return temp;
 }
};

int main() {
 Distance d1, d2, d3;
 cout << "Enter first distance:\n";
 d1.getData();
 cout << "Enter second distance:\n";
 d2.getData();

 d3 = d1 + d2;
 cout << "\nAddition result: ";
 d3.showData();

 d3 = d1 - d2;
 cout << "\nSubtraction result: ";
 d3.showData();

 return 0;
}
```

**Output:**

```
Enter first distance:
Enter feet: 5
Enter inches: 8
Enter second distance:
Enter feet: 3
Enter inches: 9

Addition result: 9' 5"
Subtraction result: 1' 11"
```

### Example 2: Overloading Comparison Operators

**Problem:** Create a class Matrix with 2x2 matrix operations. Overload == and != operators.

**Solution:**

```cpp
#include <iostream>
using namespace std;

class Matrix {
private:
 int a[2][2];
public:
 Matrix() {
 for (int i = 0; i < 2; i++)
 for (int j = 0; j < 2; j++)
 a[i][j] = 0;
 }

 Matrix(int arr[2][2]) {
 for (int i = 0; i < 2; i++)
 for (int j = 0; j < 2; j++)
 a[i][j] = arr[i][j];
 }

 void display() const {
 for (int i = 0; i < 2; i++) {
 for (int j = 0; j < 2; j++)
 cout << a[i][j] << " ";
 cout << "\n";
 }
 }

 // Overloading == operator
 bool operator==(const Matrix& m) const {
 for (int i = 0; i < 2; i++)
 for (int j = 0; j < 2; j++)
 if (a[i][j] != m.a[i][j])
 return false;
 return true;
 }

 // Overloading != operator
 bool operator!=(const Matrix& m) const {
 return !(*this == m);
 }
};

int main() {
 int arr1[2][2] = {{1, 2}, {3, 4}};
 int arr2[2][2] = {{1, 2}, {3, 4}};
 int arr3[2][2] = {{1, 0}, {0, 1}};

 Matrix m1(arr1), m2(arr2), m3(arr3);

 cout << "Matrix m1:\n";
 m1.display();
 cout << "\nMatrix m2:\n";
 m2.display();
 cout << "\nMatrix m3:\n";
 m3.display();

 if (m1 == m2)
 cout << "\nm1 and m2 are equal\n";
 else
 cout << "\nm1 and m2 are not equal\n";

 if (m1 != m3)
 cout << "m1 and m3 are not equal\n";
 else
 cout << "m1 and m3 are equal\n";

 return 0;
}
```

### Example 3: Overloading [] for Array Class

**Problem:** Create a class IntArray that overloads the subscript operator [] for array access with bounds checking.

**Solution:**

```cpp
#include <iostream>
using namespace std;

class IntArray {
private:
 int* arr;
 int size;
public:
 IntArray(int s = 10) : size(s) {
 arr = new int[size];
 for (int i = 0; i < size; i++)
 arr[i] = 0;
 }

 ~IntArray() {
 delete[] arr;
 }

 // Overloading [] operator
 int& operator[](int index) {
 if (index < 0 || index >= size) {
 cout << "Index out of bounds! Returning first element.\n";
 return arr[0];
 }
 return arr[index];
 }

 // Const version for const objects
 int operator[](int index) const {
 if (index < 0 || index >= size) {
 cout << "Index out of bounds! Returning 0.\n";
 return 0;
 }
 return arr[index];
 }

 void display() const {
 for (int i = 0; i < size; i++)
 cout << arr[i] << " ";
 cout << "\n";
 }
};

int main() {
 IntArray a(5);

 cout << "Initial array: ";
 a.display();

 a[0] = 10;
 a[1] = 20;
 a[2] = 30;
 a[3] = 40;
 a[4] = 50;

 cout << "After assignment: ";
 a.display();

 cout << "Value at a[2]: " << a[2] << "\n";

 // Test out of bounds
 cout << "Testing out of bounds: a[10] = " << a[10] << "\n";

 return 0;
}
```

## Exam Tips

1. **Remember the syntax**: For binary operators as member functions, only one argument is needed (right operand), as the left operand is the calling object itself.

2. **Pre vs Post increment/decrement**: Always include a dummy `int` parameter in the post-increment/decrement version to differentiate from the pre-version.

3. **Return type matters**: For assignment operators, return `*this` to allow chaining like `a = b = c`. For arithmetic operators, returning by value is appropriate.

4. **Const correctness**: Always make member operator functions `const` when they don't modify the object, as this allows them to be called on const objects.

5. **Deep copy for dynamic memory**: When overloading assignment operator for classes with pointers, always implement deep copy and check for self-assignment.

6. **Operators that must be members**: The assignment operator `=`, subscript `[]`, function call `()`, and member access `->` should preferably be member functions.

7. **Cannot overload**: Remember that `::`, `.*`, `.`, and `?:` cannot be overloaded in C++.

8. **Friend function usage**: Use friend functions when the left operand is not an object of your class, such as `cout << obj` or `5 + obj`.

9. **Understand implicit calling**: Know that `a + b` is equivalent to `a.operator+(b)` for member functions.

10. **Practice diagram-based questions**: university frequently asks to predict output or write operator overloading code for given scenarios.
