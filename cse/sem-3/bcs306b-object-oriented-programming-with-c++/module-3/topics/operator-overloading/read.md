# Operator Overloading in C++

## Introduction

Operator overloading is one of the most powerful features of C++ that allows the programmer to redefine the behavior of existing operators when they are applied to user-defined data types (classes). In simple terms, operator overloading enables programmers to use standard operators like +, -, \*, /, etc., with objects of custom classes, making the code more intuitive and readable.

Consider a scenario where you have created a class to represent complex numbers. Without operator overloading, adding two complex numbers would require calling a member function like `c1.add(c2)`. However, with operator overloading, you can simply write `c1 + c2`, which is far more natural and resembles mathematical notation. This feature bridges the gap between built-in data types and user-defined types, providing a uniform interface for operations.

Operator overloading is particularly important in C++ because it enhances code readability and maintainability. It allows mathematical, logical, and stream operators to work naturally with objects, making the code self-documenting. This feature is extensively used in the university's Object Oriented Programming with C++ curriculum and is a favorite topic in university examinations, often carrying significant weightage in both theory and practical components.

## Key Concepts

### Fundamentals of Operator Overloading

In C++, most operators can be overloaded, but there are certain operators that cannot be overloaded. The operators that cannot be overloaded are: `::` (scope resolution), `.*` (pointer to member), `.` (member access), and `?:` (ternary/conditional).

To overload an operator, you use the `operator` keyword followed by the operator symbol. The general syntax is:

```cpp
return_type operator op(arguments) {
 // body
}
```

Where `op` is the operator to be overloaded (such as +, -, \*, /, etc.).

### Rules for Operator Overloading

1. **Precedence and Associativity**: When you overload an operator, you cannot change its precedence or associativity. The operator retains its original characteristics in terms of how it binds with other operators.

2. **Arity**: You cannot change the number of operands an operator takes. A unary operator remains unary, and a binary operator remains binary.

3. **Cannot Create New Operators**: You cannot create new operator symbols. You can only overload existing C++ operators.

4. **At Least One User-Defined Type**: At least one operand of the overloaded operator must be a user-defined type (class or enum). You cannot overload operators to work exclusively with built-in types.

5. **Special Operators**: Certain operators like `=`, `&`, `,` (comma), and `&&` have default implementations for classes, but you can redefine them if needed.

### Types of Operator Overloading

#### 1. Unary Operators

Unary operators operate on a single operand. Examples include unary minus (-), increment (++), decrement (--), and logical NOT (!). Unary operators can be overloaded as either member functions (with no arguments) or friend functions (with one argument).

```cpp
class Counter {
private:
 int value;
public:
 Counter(int v = 0) : value(v) {}

 // Overloading unary minus as member function
 Counter operator-() {
 return Counter(-value);
 }

 // Overloading prefix increment
 Counter operator++() {
 ++value;
 return *this;
 }

 // Overloading postfix increment (int parameter distinguishes it)
 Counter operator++(int) {
 Counter temp = *this;
 value++;
 return temp;
 }

 void display() {
 cout << value << endl;
 }
};
```

#### 2. Binary Operators

Binary operators work on two operands. Examples include addition (+), subtraction (-), multiplication (\*), division (/), comparison operators (==, !=, <, >, <=, >=), and stream operators (<<, >>).

Binary operators should typically be overloaded as friend functions or as member functions with one argument. The left operand becomes the object through which the member function is called, and the right operand is passed as an argument.

```cpp
class Complex {
private:
 float real, imag;
public:
 Complex(float r = 0, float i = 0) : real(r), imag(i) {}

 // Overloading + as member function
 Complex operator+(const Complex& c) {
 Complex temp;
 temp.real = real + c.real;
 temp.imag = imag + c.imag;
 return temp;
 }

 // Friend function declaration for << operator
 friend ostream& operator<<(ostream&, const Complex&);
};

ostream& operator<<(ostream& out, const Complex& c) {
 out << c.real << " + " << c.imag << "i";
 return out;
}
```

### Friend Functions for Operator Overloading

Friend functions are used when you need to access private members of a class from an overloaded operator function. They are particularly useful when:

- The left operand is not a class object (e.g., `5 + obj`)
- You want symmetric treatment of both operands

```cpp
class Vector {
private:
 int x, y;
public:
 Vector(int x = 0, int y = 0) : x(x), y(y) {}

 friend Vector operator+(const Vector&, const Vector&);
};

Vector operator+(const Vector& v1, const Vector& v2) {
 return Vector(v1.x + v2.x, v1.y + v2.y);
}
```

### Overloading Stream Operators (<< and >>)

The stream insertion operator (`<<`) and stream extraction operator (`>>`) are always overloaded as friend functions because the left operand is a stream object (ostream or istream), not a class object.

```cpp
class Date {
private:
 int day, month, year;
public:
 Date(int d = 1, int m = 1, int y = 2000) : day(d), month(m), year(y) {}

 friend ostream& operator<<(ostream&, const Date&);
 friend istream& operator>>(istream&, Date&);
};

ostream& operator<<(ostream& out, const Date& dt) {
 out << dt.day << "/" << dt.month << "/" << dt.year;
 return out;
}

istream& operator>>(istream& in, Date& dt) {
 cout << "Enter day, month, year: ";
 in >> dt.day >> dt.month >> dt.year;
 return in;
}
```

### Assignment Operator Overloading

The assignment operator (`=`) is automatically provided by the compiler for classes. However, when a class contains pointer members that point to dynamically allocated memory, you must overload the assignment operator to perform a deep copy. This is essential to avoid the shallow copy problem.

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

 // Destructor
 ~String() {
 delete[] str;
 }

 // Overloaded assignment operator
 String& operator=(const String& s) {
 if (this != &s) {
 delete[] str;
 length = s.length;
 str = new char[length + 1];
 strcpy(str, s.str);
 }
 return *this;
 }
};
```

## Examples

### Example 1: Complex Number Arithmetic

**Problem**: Create a class `Complex` with real and imaginary parts. Overload +, -, \*, and / operators to perform complex number arithmetic.

**Solution**:

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
 float real, imag;
public:
 Complex(float r = 0, float i = 0) : real(r), imag(i) {}

 // Overload +
 Complex operator+(const Complex& c) {
 return Complex(real + c.real, imag + c.imag);
 }

 // Overload -
 Complex operator-(const Complex& c) {
 return Complex(real - c.real, imag - c.imag);
 }

 // Overload *
 Complex operator*(const Complex& c) {
 Complex temp;
 temp.real = real * c.real - imag * c.imag;
 temp.imag = real * c.imag + imag * c.real;
 return temp;
 }

 // Overload /
 Complex operator/(const Complex& c) {
 Complex temp;
 float denominator = c.real * c.real + c.imag * c.imag;
 temp.real = (real * c.real + imag * c.imag) / denominator;
 temp.imag = (imag * c.real - real * c.imag) / denominator;
 return temp;
 }

 void display() {
 cout << real << " + " << imag << "i" << endl;
 }
};

int main() {
 Complex c1(3, 2), c2(1, 4), c3;

 c3 = c1 + c2;
 cout << "Addition: ";
 c3.display();

 c3 = c1 - c2;
 cout << "Subtraction: ";
 c3.display();

 c3 = c1 * c2;
 cout << "Multiplication: ";
 c3.display();

 c3 = c1 / c2;
 cout << "Division: ";
 c3.display();

 return 0;
}
```

**Output**:

```
Addition: 4 + 6i
Subtraction: 2 + -2i
Multiplication: -5 + 14i
Division: 0.647059 + -0.823529i
```

### Example 2: Distance Class with Increment/Decrement

**Problem**: Create a class `Distance` with feet and inches. Overload prefix and postfix increment operators to add 1 inch (handling overflow to feet).

**Solution**:

```cpp
#include <iostream>
using namespace std;

class Distance {
private:
 int feet, inches;
public:
 Distance(int f = 0, int i = 0) : feet(f), inches(i) {
 normalize();
 }

 void normalize() {
 if (inches >= 12) {
 feet += inches / 12;
 inches = inches % 12;
 }
 }

 // Prefix increment
 Distance& operator++() {
 inches++;
 normalize();
 return *this;
 }

 // Postfix increment
 Distance operator++(int) {
 Distance temp = *this;
 inches++;
 normalize();
 return temp;
 }

 void display() {
 cout << feet << "' " << inches << "\"" << endl;
 }
};

int main() {
 Distance d1(5, 11), d2;

 cout << "Initial: ";
 d1.display();

 d2 = ++d1;
 cout << "After ++d1: ";
 d1.display();
 cout << "d2 = ++d1: ";
 d2.display();

 d1 = Distance(5, 11);
 d2 = d1++;
 cout << "After d1++: ";
 d1.display();
 cout << "d2 = d1++: ";
 d2.display();

 return 0;
}
```

**Output**:

```
Initial: 5' 11"
After ++d1: 6' 0"
d2 = ++d1: 6' 0"
After d1++: 6' 0"
d2 = d1++: 5' 11"
```

### Example 3: Rational Number Class

**Problem**: Create a class `Rational` with numerator and denominator. Overload comparison operators (==, <, >) and stream operators.

**Solution**:

```cpp
#include <iostream>
using namespace std;

class Rational {
private:
 int num, den;
 void simplify() {
 int gcd = 1;
 int min = (num < 0) ? -num : num;
 for (int i = 2; i <= min; i++) {
 if (num % i == 0 && den % i == 0)
 gcd = i;
 }
 num /= gcd;
 den /= gcd;
 }
public:
 Rational(int n = 0, int d = 1) : num(n), den(d) {
 simplify();
 }

 // Overload ==
 bool operator==(const Rational& r) {
 return num * r.den == den * r.num;
 }

 // Overload <
 bool operator<(const Rational& r) {
 return num * r.den < den * r.num;
 }

 // Overload >
 bool operator>(const Rational& r) {
 return num * r.den > den * r.num;
 }

 // Friend declarations for stream operators
 friend ostream& operator<<(ostream&, const Rational&);
 friend istream& operator>>(istream&, Rational&);
};

ostream& operator<<(ostream& out, const Rational& r) {
 out << r.num << "/" << r.den;
 return out;
}

istream& operator>>(istream& in, Rational& r) {
 cout << "Enter numerator: ";
 in >> r.num;
 cout << "Enter denominator: ";
 in >> r.den;
 r.simplify();
 return in;
}

int main() {
 Rational r1(1, 2), r2(3, 4), r3;

 cout << "r1 = " << r1 << ", r2 = " << r2 << endl;

 if (r1 == r2)
 cout << "r1 == r2" << endl;
 else
 cout << "r1 != r2" << endl;

 if (r1 < r2)
 cout << "r1 < r2" << endl;

 if (r1 > r2)
 cout << "r1 > r2" << endl;

 cin >> r3;
 cout << "r3 = " << r3 << endl;

 return 0;
}
```

## Exam Tips

1. **Remember the Four Unoverloadable Operators**: The scope resolution (`::`), pointer to member (`.*`), member access (`.`), and conditional (`?:`) operators cannot be overloaded under any circumstances.

2. **Distinguish Between Prefix and Postfix**: For prefix operators (`++obj`), return the updated object by reference. For postfix operators (`obj++`), return a copy of the original object before modification. The `int` parameter in postfix is only for distinction, not used.

3. **Use Friend Functions When Needed**: When the left operand is not of the class type (like `5 + obj`), or when you need symmetric operations, use friend functions. Friend functions can access private members directly.

4. **Stream Operators Must Be Friends**: The `<<` and `>>` operators must be overloaded as friend functions because the left operand is a stream object, not your class object.

5. **Deep Copy for Dynamic Memory**: Always overload the assignment operator (`=`) when your class contains pointers to dynamically allocated memory to prevent memory leaks and shallow copy problems.

6. **Return Appropriate Types**: Arithmetic operators should return the class type by value. Comparison operators should return `bool`. Assignment operators should return reference to the class type (`*this`).

7. **Follow the Rule of Three**: If you overload one of the destructor, copy constructor, or assignment operator, you should consider overloading all three to ensure proper resource management.

8. **Keep Operators Consistent**: If you overload `+`, also overload `+=`. If you overload `==`, also overload `!=` for consistency. This makes the class interface complete and intuitive.
