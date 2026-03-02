# Function Overloading in C++

## Introduction

Function overloading is one of the most powerful features of C++ that enables multiple functions to share the same name but with different parameter lists. This capability falls under the broader concept of polymorphism, specifically compile-time polymorphism (also known as static binding or early binding). In the context of object-oriented programming, function overloading allows developers to create intuitive and readable code by using meaningful function names that describe the action being performed, while the compiler automatically selects the appropriate function to execute based on the arguments provided.

In the university's BCS306B syllabus, function overloading forms a fundamental concept that students must master before moving to advanced OOP topics like operator overloading and virtual functions. The ability to overload functions is essential for implementing type-independent operations, improving code readability, and reducing the number of distinct function names a programmer must remember. This feature is particularly useful when performing similar operations on different data types or when a function needs to handle varying numbers of arguments.

Function overloading is extensively used in C++ standard library implementations, where functions like `abs()`, `max()`, and `sqrt()` are overloaded to work with different numeric types. Understanding this concept is crucial for both examination success and practical software development, as it forms the foundation for many design patterns and coding paradigms in modern C++ programming.

## Key Concepts

### Definition and Basic Syntax

Function overloading is the process of creating multiple functions with the same name but different parameter lists. The compiler distinguishes between these functions by examining the number, type, and order of parameters during compilation. When a function is called, the compiler matches the provided arguments with the available function signatures and selects the most appropriate match through a process called overload resolution.

The basic syntax involves declaring multiple functions with the same name:

```cpp
return_type function_name(parameter_list);
```

For example, a calculator program might have multiple `add()` functions:

```cpp
int add(int a, int b); // Adds two integers
double add(double a, double b); // Adds two doubles
int add(int a, int b, int c); // Adds three integers
```

### Rules for Function Overloading

Several important rules govern function overloading in C++:

1. **Parameter List Difference**: The parameter lists must differ in at least one of the following ways:

- Number of parameters
- Type of parameters
- Order of parameters

2. **Return Type Consideration**: The return type alone is **not** sufficient to differentiate overloaded functions. Two functions with the same name and identical parameter lists but different return types will result in a compilation error.

3. **Default Arguments**: Functions can have default arguments, but this doesn't create unique overloads. Default arguments provide alternative ways to call the same function rather than creating new overloaded versions.

4. **Const Parameters**: A function with a const parameter and another with a non-const parameter of the same type are considered different signatures in certain contexts, particularly with reference and pointer parameters.

### Type of Parameter Variations

Function overloading can be achieved through various parameter type combinations:

- **Type Overloading**: Same number of parameters but different data types
- **Number Overloading**: Different number of parameters
- **Combination Overloading**: Both different types and different numbers of parameters

### Overload Resolution Process

When a function call matches multiple overloaded functions, the compiler follows a specific precedence:

1. **Exact Match**: Function where parameter types exactly match argument types
2. **Promotion**: Integer promotions (char, short to int) and float to double
3. **Standard Conversions**: Built-in type conversions (int to float, etc.)
4. **User-Defined Conversions**: Custom conversion functions
5. **Ellipsis Match**: Functions with variable arguments (last resort)

### Function Overloading vs Function Templates

While both features appear similar, function overloading uses explicit function definitions for each variation, whereas function templates provide a generic blueprint that the compiler uses to generate specific function versions automatically. Templates are covered in detail in Module 5 of the the syllabus.

## Examples

### Example 1: Area Calculation

Write a program to calculate the area of different shapes using function overloading.

```cpp
#include <iostream>
using namespace std;

// Area of circle
double area(double radius) {
 return 3.14159 * radius * radius;
}

// Area of rectangle
double area(double length, double breadth) {
 return length * breadth;
}

// Area of triangle
double area(double base, double height, bool isTriangle) {
 if (isTriangle) {
 return 0.5 * base * height;
 }
 return 0;
}

int main() {
 cout << "Area of circle (radius=5): " << area(5.0) << endl;
 cout << "Area of rectangle (10x5): " << area(10.0, 5.0) << endl;
 cout << "Area of triangle (base=10, height=5): " << area(10.0, 5.0, true) << endl;
 return 0;
}
```

**Output:**

```
Area of circle (radius=5): 78.5397
Area of rectangle (10x5): 50
Area of triangle (base=10, height=5): 25
```

### Example 2: Student Grade Calculator

Create overloaded functions to calculate grades based on different input parameters.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Calculate grade from marks (single subject)
char calculateGrade(int marks) {
 if (marks >= 90) return 'A';
 else if (marks >= 80) return 'B';
 else if (marks >= 70) return 'C';
 else if (marks >= 60) return 'D';
 else return 'F';
}

// Calculate average grade from two subjects
char calculateGrade(int marks1, int marks2) {
 int avg = (marks1 + marks2) / 2;
 return calculateGrade(avg); // Reuse single subject function
}

// Calculate grade from percentage
char calculateGrade(double percentage) {
 if (percentage >= 90) return 'A';
 else if (percentage >= 80) return 'B';
 else if (percentage >= 70) return 'C';
 else if (percentage >= 60) return 'D';
 else return 'F';
}

int main() {
 cout << "Grade from 85 marks: " << calculateGrade(85) << endl;
 cout << "Grade from 75 and 82 marks: " << calculateGrade(75, 82) << endl;
 cout << "Grade from 87.5%: " << calculateGrade(87.5) << endl;
 return 0;
}
```

**Output:**

```
Grade from 85 marks: B
Grade from 75 and 82 marks: B
Grade from 87.5%: B
```

### Example 3: String Manipulation

Overloaded functions for string operations.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Count vowels in a string
int countVowels(string str) {
 int count = 0;
 string vowels = "aeiouAEIOU";
 for (char c : str) {
 if (vowels.find(c) != string::npos)
 count++;
 }
 return count;
}

// Count vowels in a string (case-insensitive by parameter)
int countVowels(const char* str) {
 int count = 0;
 string vowels = "aeiouAEIOU";
 while (*str) {
 if (vowels.find(*str) != string::npos)
 count++;
 str++;
 }
 return count;
}

// Count specific character in string
int countVowels(string str, char target) {
 int count = 0;
 for (char c : str) {
 if (c == target)
 count++;
 }
 return count;
}

int main() {
 string s = "Hello World";
 cout << "Vowels in '" << s << "': " << countVowels(s) << endl;
 cout << "Vowels in 'CSE': " << countVowels("CSE") << endl;
 cout << "Occurrences of 'l' in '" << s << "': " << countVowels(s, 'l') << endl;
 return 0;
}
```

**Output:**

```
Vowels in 'Hello World': 3
Vowels in 'CSE': 2
Occurrences of 'l' in 'Hello World': 3
```

## Exam Tips

1. **Remember the Signature Rule**: Only the parameter list (not return type) determines function overloading. This is a common trick question in university exams.

2. **Distinguish Overloading from Overriding**: Function overloading occurs within the same scope with different parameters, while overriding (covered in Module 4) occurs in different scopes with same parameters.

3. **Default Arguments Don't Create Overloads**: If you have `func(int a, int b=10)` and call `func(5)`, it uses the same function, not a different overloaded version.

4. **Watch for Ambiguous Calls**: When multiple overloaded functions could match equally well, the compiler generates an error. For example, `func(10, 10)` when both `func(int, int)` and `func(double, double)` exist.

5. **Promotion vs Conversion**: Exact matches are preferred, followed by promotions (char→int), then standard conversions (int→float). This hierarchy is frequently tested.

6. **Const Correctness**: Functions differing only in const-ness of parameters (like `void display(const string&)` and `void display(string&)`) are considered different overloads.

7. **Reference and Pointer Parameters**: `void func(int)` and `void func(int&)` are different signatures, as are `void func(int*)` and `void func(int&)`.

8. **Practice Drawing Call Resolution**: For exam questions, systematically check each argument against available function signatures, noting which match and why others don't.
