# Pointers to Class Members

## Introduction

Pointers to class members are a powerful but often underutilized feature of C++ that provides flexible access to class members through indirection. Unlike regular pointers that point to regular variables or functions, pointers to class members must be qualified with the class name to indicate which class they belong to. This distinction is crucial because member pointers incorporate the class scope into their type system.

In C++, a pointer to a class member can point to either a data member or a member function of a class. These pointers are essential for implementing callback mechanisms, generic programming, and creating flexible APIs that can work with different class members without hardcoding specific member names. Understanding pointers to class members is fundamental for advanced C++ programming and is particularly useful in scenarios involving function objects, member function adapters, and design patterns like Command Pattern.

The syntax for declaring and using pointers to class members differs significantly from regular pointers. A pointer to an int data member of class MyClass, for example, has the type `int MyClass::*`, while a pointer to a member function taking no arguments and returning void has the type `void (MyClass::*)()`. This type system ensures type safety and allows the compiler to verify that pointers are used correctly with objects of the appropriate class.

## Key Concepts

### Pointer to Data Members

A pointer to a data member stores the offset of a data member within a class rather than an actual memory address. This offset is relative to the beginning of the class object. The declaration syntax requires the class name followed by the scope resolution operator (::), an asterisk, and the data member name.

```cpp
class Box {
public:
 double width;
 double height;
 double depth;
};

int main() {
 // Declare pointer to double data member of Box class
 double Box::*ptrToMember = &Box::width;

 Box myBox;
 myBox.*ptrToMember = 5.0; // Access width through pointer
 std::cout << myBox.width; // Output: 5

 return 0;
}
```

The pointer-to-member stores the offset (in bytes) from the beginning of the class object. When dereferencing with an object, the compiler adds this offset to the object's base address to access the actual member. This is why pointers to members require an object on the left side of the dereferencing operator (._ or ->_).

### Pointer to Member Functions

Pointers to member functions are more complex than pointers to data members because member functions require the `this` pointer to be passed implicitly. The syntax involves specifying the complete function signature including return type, class name, and parameter list.

```cpp
class Calculator {
public:
 int add(int a, int b) { return a + b; }
 int subtract(int a, int b) { return a - b; }
 void display() { std::cout << "Calculator operations\n"; }
};

int main() {
 // Declare pointer to member function
 int (Calculator::*funcPtr)(int, int) = &Calculator::add;

 Calculator calc;
 int result = (calc.*funcPtr)(10, 5); // Calls add(10, 5)
 std::cout << result; // Output: 15

 // Change to different function
 funcPtr = &Calculator::subtract;
 result = (calc.*funcPtr)(10, 5); // Calls subtract(10, 5)
 std::cout << result; // Output: 5

 return 0;
}
```

The operators `.*` (dot star) and `->*` (arrow star) are used to dereference pointers to members with objects and pointers to objects respectively.

### Using with Pointers to Objects

When working with pointers to objects rather than objects themselves, the `->*` operator must be used:

```cpp
Calculator* calcPtr = new Calculator();
int (Calculator::*funcPtr)(int, int) = &Calculator::add;
int result = (calcPtr->*funcPtr)(10, 5);
```

### Typedefs for Pointer-to-Member Types

Using typedefs improves readability when working with pointer-to-member types:

```cpp
typedef int (Calculator::*CalcFunc)(int, int);
typedef double Box::*BoxDataPtr;

CalcFunc operations[] = { &Calculator::add, &Calculator::subtract };
BoxDataPtr memberPtr = &Box::width;
```

### Pointers to Static Members

Static members do not belong to any particular object, so pointers to static members are regular pointers, not member pointers:

```cpp
class MyClass {
public:
 static int staticData;
 static void staticFunc() {}
};

int* ptrToStatic = &MyClass::staticData; // Regular int*
void (*funcPtr)() = &MyClass::staticFunc; // Regular function pointer
```

## Examples

### Example 1: Implementing a Simple Callback System

```cpp
#include <iostream>
#include <vector>

class Button {
public:
 typedef void (Button::*ClickHandler)();

 void setOnClick(ClickHandler handler) {
 handler = handler;
 }

 void click() {
 if (handler) {
 (this->*handler)();
 }
 }

 void onClickMethod() {
 std::cout << "Button clicked!\n";
 }

private:
 ClickHandler handler;
};

int main() {
 Button myButton;
 myButton.setOnClick(&Button::onClickMethod);
 myButton.click(); // Output: Button clicked!
 return 0;
}
```

### Example 2: Array of Pointers to Member Functions

```cpp
#include <iostream>

class MathOperations {
public:
 int add(int a, int b) { return a + b; }
 int multiply(int a, int b) { return a * b; }
 int power(int a, int b) {
 int result = 1;
 for (int i = 0; i < b; i++)
 result *= a;
 return result;
 }
};

typedef int (MathOperations::*MathFunc)(int, int);

int main() {
 MathOperations math;
 MathFunc operations[] = {
 &MathOperations::add,
 &MathOperations::multiply,
 &MathOperations::power
 };

 for (int i = 0; i < 3; i++) {
 std::cout << (math.*operations[i])(2, 3) << " ";
 }
 // Output: 6 8
 return 0;
}
```

### Example 3: Generic Member Access Function

```cpp
#include <iostream>

class Employee {
public:
 std::string name;
 int age;
 double salary;
};

template<typename T, typename M>
M getMemberValue(T& obj, M T::*member) {
 return obj.*member;
}

int main() {
 Employee emp;
 emp.name = "John";
 emp.age = 30;
 emp.salary = 50000.0;

 std::string Employee::*namePtr = &Employee::name;
 int Employee::*agePtr = &Employee::age;
 double Employee::*salaryPtr = &Employee::salary;

 std::cout << "Name: " << getMemberValue(emp, namePtr) << "\n";
 std::cout << "Age: " << getMemberValue(emp, agePtr) << "\n";
 std::cout << "Salary: " << getMemberValue(emp, salaryPtr) << "\n";

 return 0;
}
```

## Exam Tips

1. **Syntax Difference**: Remember that pointers to class members require the class name in the type declaration (e.g., `int MyClass::*ptr` for data members and `void (MyClass::*func)()` for member functions).

2. **Operators**: Use `.*` for objects and `->*` for pointers to objects when dereferencing member pointers. Do not confuse these with the regular `*` operator.

3. **Address Operator**: When taking the address of a member, always use the fully qualified form: `&ClassName::memberName`.

4. **Static vs Non-Static**: Static members use regular pointers, not member pointers, because they are not associated with any particular object instance.

5. **Type Safety**: The compiler enforces type compatibility between member pointer types. A pointer to an int member cannot be used to access a double member.

6. **Template Applications**: Pointers to members are extensively used in STL algorithms with bind functions and mem_fun adaptors.

7. **Common Mistakes**: Students often forget to use parentheses when calling member functions through pointers: `(obj.*ptr)(args)` not `obj.*ptr(args)`.

8. **Offset Concept**: Understand that pointers to data members store offsets, not actual addresses, which is why they need an object for dereferencing.

9. **typedef Usage**: Using typedefs makes code more readable when dealing with complex member pointer types.

10. **Assignment**: A pointer to member can be assigned NULL (nullptr) and should be checked before dereferencing to avoid undefined behavior.
