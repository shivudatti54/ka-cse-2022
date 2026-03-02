# Default Function Arguments in C++

## Introduction

Default function arguments (also known as default parameters) are one of the most practical and widely-used features introduced in C++ that was not available in the C programming language. A default argument is a value provided in a function declaration that is automatically assigned by the compiler if the calling function does not provide a value for that argument. This feature allows functions to be called with fewer arguments than they are defined to accept, making function calls more flexible and concise.

In the context of Object-Oriented Programming, default arguments play a significant role in constructor overloading, function overloading, and simplifying class interfaces. They reduce the need to write multiple overloaded functions that differ only in the number of parameters. the university's 2022 scheme for BCS306B emphasizes understanding default arguments as a key C++ enhancement over C, and questions on this topic frequently appear in examinations.

Default arguments are specified in the function declaration (prototype) and are assigned from right to left. This means that if a function has multiple parameters, default values must be assigned starting from the rightmost parameter. Understanding this rule and the various nuances associated with default arguments is critical for writing robust and error-free C++ programs.

## Key Concepts

### 1. What Are Default Function Arguments?

A default function argument is a value specified for a parameter in a function declaration. When the caller omits the corresponding argument, the compiler substitutes the default value automatically.

```cpp
// Function declaration with default arguments
void display(int x, int y = 10, int z = 20);
```

In the above example, `y` has a default value of `10` and `z` has a default value of `20`. The function can be called in the following ways:

```cpp
display(5); // x=5, y=10, z=20
display(5, 15); // x=5, y=15, z=20
display(5, 15, 25); // x=5, y=15, z=25
```

### 2. Rules for Default Arguments

**Rule 1: Right-to-Left Assignment**
Default arguments must be specified from the rightmost parameter towards the left. You cannot provide a default value for a parameter on the left while leaving one on the right without a default.

```cpp
// VALID declarations
void func(int a, int b = 5, int c = 10);
void func(int a, int b, int c = 10);

// INVALID declarations
void func(int a = 5, int b, int c); // ERROR
void func(int a, int b = 5, int c); // ERROR
```

**Rule 2: Declaration vs Definition**
Default arguments should be specified in the function declaration (prototype), not in the function definition, when both are present. If a function has no separate declaration, the defaults can be specified in the definition.

```cpp
// In header or before main - declaration with defaults
void greet(string name = "Student", int times = 1);

// In definition - no defaults repeated
void greet(string name, int times) {
 for (int i = 0; i < times; i++)
 cout << "Hello, " << name << endl;
}
```

**Rule 3: No Redefinition of Defaults**
Default values cannot be redefined. Specifying defaults in both the declaration and definition results in a compilation error.

**Rule 4: Default Arguments and Function Overloading**
Care must be taken when combining default arguments with function overloading, as ambiguity may arise.

```cpp
void print(int a, int b = 10);
void print(int a); // Ambiguity when calling print(5)
```

### 3. Advantages of Default Function Arguments

- **Reduces the need for multiple overloaded functions**: A single function with default arguments can serve the purpose of several overloaded versions.
- **Improves code readability**: Functions have a clear and simple interface.
- **Backward compatibility**: Adding new parameters with default values does not break existing function calls.
- **Simplifies constructor design**: In OOP, constructors with default arguments reduce the number of constructors needed in a class.

### 4. Default Arguments in Constructors

Default arguments are extremely useful in class constructors. A single constructor with default arguments can act as a default constructor, a parameterized constructor, or a partially parameterized constructor.

```cpp
class Rectangle {
 int length, breadth;
public:
 Rectangle(int l = 1, int b = 1) {
 length = l;
 breadth = b;
 }
 int area() { return length * breadth; }
};

int main() {
 Rectangle r1; // length=1, breadth=1
 Rectangle r2(5); // length=5, breadth=1
 Rectangle r3(5, 10); // length=5, breadth=10
 return 0;
}
```

### 5. Default Arguments with Expressions

Default argument values need not be constants; they can be expressions involving previously declared variables, global variables, or function calls.

```cpp
int globalVar = 100;

int getDefault() {
 return 50;
}

void compute(int a, int b = globalVar, int c = getDefault()) {
 cout << a << " " << b << " " << c << endl;
}
```

### 6. Scope and Lifetime Considerations

Default arguments are evaluated at the point of each function call, not at the point of declaration. This means if a global variable used as a default argument changes its value, the new value will be used for subsequent calls.

## Examples

### Example 1: Simple Interest Calculator

```cpp
#include <iostream>
using namespace std;

// Function with default arguments
float simpleInterest(float principal, float rate = 5.0, float time = 1.0) {
 return (principal * rate * time) / 100;
}

int main() {
 cout << "SI with all arguments: " << simpleInterest(10000, 8.5, 3) << endl;
 // Output: SI with all arguments: 2550

 cout << "SI with default time (1 year): " << simpleInterest(10000, 8.5) << endl;
 // Output: SI with default time (1 year): 850

 cout << "SI with default rate & time: " << simpleInterest(10000) << endl;
 // Output: SI with default rate & time: 500

 return 0;
}
```

**Step-by-step explanation:**

1. The function `simpleInterest` has three parameters: `principal` (no default), `rate` (default 5.0), and `time` (default 1.0).
2. First call `simpleInterest(10000, 8.5, 3)`: All arguments provided → SI = (10000 × 8.5 × 3)/100 = 2550.
3. Second call `simpleInterest(10000, 8.5)`: `time` uses default value 1.0 → SI = (10000 × 8.5 × 1)/100 = 850.
4. Third call `simpleInterest(10000)`: `rate` uses 5.0 and `time` uses 1.0 → SI = (10000 × 5 × 1)/100 = 500.

### Example 2: Class with Default Constructor Arguments

```cpp
#include <iostream>
using namespace std;

class Box {
 double length, width, height;
public:
 // Constructor with default arguments
 Box(double l = 1.0, double w = 1.0, double h = 1.0) {
 length = l;
 width = w;
 height = h;
 }

 double volume() {
 return length * width * height;
 }

 void display() {
 cout << "Dimensions: " << length << " x " << width << " x " << height << endl;
 cout << "Volume: " << volume() << endl;
 }
};

int main() {
 Box b1; // Uses all defaults: 1.0, 1.0, 1.0
 Box b2(5.0); // l=5.0, w=1.0, h=1.0
 Box b3(5.0, 3.0); // l=5.0, w=3.0, h=1.0
 Box b4(5.0, 3.0, 2.0); // All specified

 cout << "Box b1: "; b1.display();
 // Output: Dimensions: 1 x 1 x 1, Volume: 1

 cout << "Box b2: "; b2.display();
 // Output: Dimensions: 5 x 1 x 1, Volume: 5

 cout << "Box b3: "; b3.display();
 // Output: Dimensions: 5 x 3 x 1, Volume: 15

 cout << "Box b4: "; b4.display();
 // Output: Dimensions: 5 x 3 x 2, Volume: 30

 return 0;
}
```

**Step-by-step explanation:**

1. The `Box` class has a single constructor with three default parameters.
2. `b1` is created with no arguments — all defaults (1.0, 1.0, 1.0) are used. This acts as a **default constructor**.
3. `b2` is created with one argument — `length = 5.0`, others use defaults.
4. `b3` is created with two arguments — `length = 5.0`, `width = 3.0`, `height` defaults to 1.0.
5. `b4` is created with all three arguments explicitly provided.
6. This single constructor effectively replaces four separate overloaded constructors.

### Example 3: Demonstrating Invalid Usage and Ambiguity

```cpp
#include <iostream>
using namespace std;

// CORRECT: Defaults assigned from right to left
void display(int a, int b = 20, int c = 30) {
 cout << "a=" << a << " b=" << b << " c=" << c << endl;
}

// The following would cause AMBIGUITY if uncommented:
// void display(int a) {
// cout << "Single argument: " << a << endl;
// }

int main() {
 display(10); // a=10, b=20, c=30
 display(10, 25); // a=10, b=25, c=30
 display(10, 25, 35); // a=10, b=25, c=35

 // display(); // ERROR: 'a' has no default, must be provided

 return 0;
}
```

**Step-by-step explanation:**

1. `display(10)` — only `a` is provided; `b` and `c` take default values 20 and 30.
2. `display(10, 25)` — `a=10`, `b=25` (overrides default), `c=30` (uses default).
3. `display(10, 25, 35)` — all values explicitly provided.
4. Calling `display()` would be an error because parameter `a` has no default value.
5. If another overloaded function `display(int a)` existed, calling `display(10)` would create ambiguity — the compiler cannot decide which function to call.

## Exam Tips

1. **Frequently Asked Question**: university often asks "Explain default function arguments with an example" as a 5-10 mark question. Always include the right-to-left rule, a code example, and the output.

2. **Remember the Right-to-Left Rule**: This is the most commonly tested concept. Always emphasize that defaults must be assigned from the rightmost parameter. An incorrect declaration like `void f(int a = 5, int b)` is invalid.

3. **Declaration vs Definition**: If asked where default values should be specified, answer: in the **function declaration (prototype)**, not in the definition when both exist separately.

4. **Distinguish from Function Overloading**: Be prepared to explain how default arguments can replace function overloading, and also how they can cause ambiguity when combined with overloading.

5. **Constructor Applications**: Many questions combine default arguments with constructors. Show how a single constructor with default arguments can replace multiple overloaded constructors.

6. **Write Complete Programs**: university examiners prefer complete programs with `#include`, `main()`, and expected output. Always include output comments in your code.

7. **Common Pitfall Questions**: Be ready for questions asking you to identify errors in code where defaults are not right-to-left, or where defaults are repeated in both declaration and definition.
