# Data Types, Variables, and Operators in C++

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Welcome to one of the foundational topics in C++ programming — **Data Types, Variables, and Operators**. This chapter forms the bedrock of any program you will write in C++ and is essential for the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF.

### Why This Topic Matters

Every piece of data in a C++ program must be stored somewhere in memory, and the way we store and manipulate that data determines how efficiently our program runs. Consider these real-world scenarios:

- **Banking Systems**: When you check your account balance, the system uses `double` or `long double` data types to store currency values with decimal precision. Using `int` would lose the cents!
- **Game Development**: Player health is typically stored as an `int` or `float`, while game states use `bool` values (true/false).
- **Text Processing**: When processing user names or messages, `char` arrays or `std::string` objects are used.
- **Scientific Computing**: Complex calculations require `double` or `long double` for high precision.

Understanding data types, variables, and operators is not just academic — it's the practical skill that distinguishes a novice programmer from a competent developer.

### Delhi University Syllabus Alignment

This content aligns with the **NEP 2024 UGCF** syllabus for BSc (Hons) Computer Science, covering:
- Primitive and derived data types
- Variables and constants
- Type modifiers and qualifiers
- Complete operator coverage including precedence

---

## 2. Data Types in C++

Data types specify the type of data that a variable can hold. C++ is a **statically typed** language, meaning the data type must be known at compile time.

### 2.1 Classification of Data Types

```
C++ Data Types
├── Primitive (Built-in) Data Types
│   ├── Integral
│   │   ├── int
│   │   ├── char
│   │   ├── bool
│   │   └── wchar_t
│   ├── Floating-Point
│   │   ├── float
│   │   └── double
│   └── void
├── Derived Data Types
│   ├── Array
│   ├── Pointer
│   ├── Reference
│   └── Function
└── User-Defined Data Types
    ├── Structure (struct)
    ├── Class (class)
    ├── Union (union)
    └── Enumeration (enum)
```

### 2.2 Primitive Data Types (Fundamental Types)

#### 2.2.1 Integer Types (`int`)

The `int` type stores whole numbers (integers). The size and range depend on the system architecture.

| Type | Typical Size | Typical Range |
|------|--------------|---------------|
| `short` or `short int` | 2 bytes | -32,768 to 32,767 |
| `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 |
| `long` or `long int` | 4 or 8 bytes | Platform-dependent |
| `long long` | 8 bytes | ±9.2 × 10¹⁸ |

**Example:**
```cpp
#include <iostream>
#include <climits>  // For INT_MAX, INT_MIN
#include <cstdint>  // For fixed-width integers

int main() {
    int population = 1400000000;        // India's population
    short age = 25;
    long long nationalDebt = 15000000000000LL;
    
    // Fixed-width integers (C++11)
    int32_t score = 100;
    int64_t transactionId = 9876543210LL;
    
    std::cout << "Population: " << population << std::endl;
    std::cout << "Max int: " << INT_MAX << std::endl;
    std::cout << "Min int: " << INT_MIN << std::endl;
    
    return 0;
}
```

#### 2.2.2 Floating-Point Types

Floating-point numbers represent real numbers with fractional parts.

| Type | Typical Size | Precision | Typical Range |
|------|--------------|-----------|---------------|
| `float` | 4 bytes | ~7 digits | ±3.4 × 10³⁸ |
| `double` | 8 bytes | ~15 digits | ±1.8 × 10³⁰⁸ |
| `long double` | 8, 12, or 16 bytes | ≥ double | Platform-dependent |

**Example:**
```cpp
#include <iostream>
#include <iomanip>  // For setprecision

int main() {
    float pi_float = 3.14159265358979f;    // Note the 'f' suffix
    double pi_double = 3.14159265358979;
    long double pi_long = 3.14159265358979L; // Note the 'L' suffix
    
    std::cout << std::setprecision(15);  // Display 15 digits
    
    std::cout << "float pi:     " << pi_float << std::endl;
    std::cout << "double pi:    " << pi_double << std::endl;
    std::cout << "long double:  " << pi_long << std::endl;
    
    // Scientific notation
    double speedOfLight = 2.99792458e8;  // 299,792,458 m/s
    
    return 0;
}
```

> **Critical Note**: Never use `float` for monetary calculations due to precision errors. Use `double` or `long double` instead.

#### 2.2.3 Character Type (`char`)

The `char` type stores a single character (1 byte). It technically stores an integer (ASCII code), which is why arithmetic operations are valid on `char`.

```cpp
char grade = 'A';           // Stores ASCII 65
char number = '5';          // Stores ASCII 53 (not the value 5)
char special = '#';        // Stores ASCII 35

// Character arithmetic
char c = 'A';
std::cout << c + 1;        // Outputs 66 (B)
```

#### 2.2.4 Boolean Type (`bool`)

The `bool` type represents boolean values: `true` (1) or `false` (0).

```cpp
bool isActive = true;
bool isComplete = false;

// Boolean can accept integers (non-zero = true, zero = false)
bool flag = 42;    // true
bool zero = 0;     // false
```

#### 2.2.5 Void Type (`void`)

The `void` type represents "no type" and is used in several contexts:
- Function return type: `void func()` — function returns nothing
- Function parameters: `void func(void)` — function takes no arguments
- Generic pointer: `void* ptr` — pointer to unknown type

---

## 3. Type Modifiers

C++ provides modifiers that alter the meaning of base data types to fit various needs more precisely.

### 3.1 Sign Modifiers

| Modifier | Description |
|----------|-------------|
| `signed` | Allows both positive and negative values (default for `int`) |
| `unsigned` | Allows only non-negative values (0 and positive) |

```cpp
signed int temp = -10;     // Range: -2,147,483,648 to 2,147,483,647
unsigned int count = 100;  // Range: 0 to 4,294,967,295

// Practical example: array indices must be unsigned
unsigned int index = 0;    // Valid for array indexing
```

### 3.2 Size Modifiers

| Modifier | Description |
|----------|-------------|
| `short` | Reduces size (typically 2 bytes) |
| `long` | Increases size (typically 8 bytes on 64-bit systems) |
| `long long` | Guarantees at least 64 bits |

```cpp
short smallNumber = 32767;      // Max for short
long bigNumber = 9223372036854775807LL;
long long veryBig = 9e18;       // Up to ~9 × 10¹⁸
```

### 3.3 Combining Modifiers

You can combine modifiers for specific needs:

```cpp
unsigned long long maxValue = 18446744073709551615ULL;
// Commonly used for: timestamps, large counters, hash values
```

---

## 4. Type Qualifiers

Type qualifiers provide additional information about how a variable may be used.

### 4.1 `const` Qualifier

The `const` qualifier declares variables as compile-time constants whose values cannot be changed after initialization.

```cpp
const int MAX_SIZE = 100;        // Cannot be modified
const double PI = 3.14159265358979;

// const with pointers
const int* ptr1 = &x;            // Pointer to const int
int const* ptr2 = &x;            // Same as above (const applies to int)
int* const ptr3 = &x;            // Constant pointer to int
const int* const ptr4 = &x;      // Constant pointer to constant int

// const in function parameters
void printArray(const int arr[], int size);
```

### 4.2 `volatile` Qualifier

The `volatile` qualifier tells the compiler that a variable's value may change at any time without any action being taken by the code the compiler finds nearby. This prevents the compiler from optimizing away reads.

```cpp
// Typical use: memory-mapped hardware registers
volatile uint8_t* statusRegister = (volatile uint8_t*)0x40021000;

// Typical use: variable modified by interrupt service routine
volatile bool dataReady = false;
```

### 4.3 `mutable` Qualifier

The `mutable` qualifier allows modification of a class member variable even if the object is declared as `const`.

```cpp
class Counter {
public:
    Counter() : count(0) {}
    
    int getCount() const {  // This is a const member function
        return count;       // Cannot modify 'count' normally
    }
    
    void increment() const {
        count++;            // ERROR: cannot modify in const function
    }
    
    void increment() const {
        count++;            // OK if count is mutable
    }
    
private:
    mutable int count;      // Can be modified even in const objects
};
```

---

## 5. Variables in C++

A **variable** is a named storage location in memory that holds a value which can be modified during program execution.

### 5.1 Variable Declaration, Definition, and Initialization

```cpp
int age;              // Declaration + Definition (uninitialized)
int height = 175;     // Declaration + Definition + Initialization (copy initialization)
int width(50);        // Direct initialization (constructor syntax)
int depth{30};        // Brace initialization (C++11) - preferred

// Type deduction with 'auto' (C++11)
auto price = 99.99;          // double
auto name = "Alice";         // const char*
auto flag = true;            // bool
```

### 5.2 Variable Scope

Variables in C++ have different lifetimes and visibility based on where they are declared:

```cpp
#include <iostream>

int globalVar = 100;  // Global scope - accessible everywhere

void demonstrateScope() {
    int localVar = 50;           // Function scope (automatic storage)
    static int staticVar = 10;  // Static storage - persists between calls
    
    std::cout << "Local: " << localVar << std::endl;
    std::cout << "Static: " << staticVar << std::endl;
    staticVar++;  // Value persists across function calls
}

int main() {
    // Block scope
    {
        int blockVar = 25;
        std::cout << blockVar << std::endl;
    }
    // std::cout << blockVar;  // ERROR: blockVar not accessible here
    
    demonstrateScope();  // Output: 50, 10
    demonstrateScope();  // Output: 50, 11 (staticVar retained)
    
    std::cout << "Global: " << globalVar << std::endl;
    
    return 0;
}
```

### 5.3 Storage Classes

C++ provides four storage class specifiers:

| Specifier | Storage | Lifetime | Scope | Initial Value |
|-----------|---------|----------|-------|---------------|
| `auto` (default for local) | Stack | Automatic | Block | Undefined |
| `register` | Register (if possible) | Automatic | Block | Undefined |
| `static` | Data segment | Program duration | Block/File | Zero |
| `extern` | Data segment | Program duration | File | Zero |
| `mutable` | Data segment | Object duration | Class | Undefined |

```cpp
// File1.cpp
int global = 10;  // Definition

// File2.cpp
extern int global;  // Declaration - refers to global from File1.cpp

void example() {
    auto int local = 5;      // Explicit auto (rarely needed)
    register int counter;   // Hint to store in register
    static int callCount = 0;  // Persists across function calls
    callCount++;
}
```

---

## 6. Constants in C++

Constants are fixed values that cannot be modified during program execution.

### 6.1 Literal Constants

**Integer Literals:**
```cpp
42          // decimal
052         // octal (leading 0)
0x2A        // hexadecimal (leading 0x)
0b101010    // binary (C++14)
42ULL       // unsigned long long
42L         // long
```

**Floating-Point Literals:**
```cpp
3.14159     // double
3.14F       // float
3.14L       // long double
6.02e23     // scientific notation (double)
6.02e23f    // scientific notation (float)
```

**Character and String Literals:**
```cpp
'A'         // char
'\n'        // escape sequence
'\x41'      // hex escape
"Hello"     // const char[6] (includes null terminator)
R"(Hello
World)"    // Raw string literal (C++11)
```

### 6.2 `const` Variables

```cpp
const int DAYS_IN_WEEK = 7;
const double GRAVITY = 9.81;
```

### 6.3 Enumerated Constants (`enum`)

```cpp
// Traditional enum
enum Color { RED, GREEN, BLUE };
Color favorite = RED;  // Note: enum values are integers

// enum class (C++11) - strongly typed
enum class Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY };
Day today = Day::FRIDAY;

// With specified underlying type
enum class Status : uint8_t { PENDING = 0, SUCCESS = 1, FAILED = 2 };
```

### 6.4 `#define` Macros (Preprocessor)

```cpp
#define PI 3.14159
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// Note: Prefer const/enum over #define for type safety
```

---

## 7. Operators in C++

Operators are symbols that perform operations on operands (variables, literals, expressions).

### 7.1 Arithmetic Operators

| Operator | Name | Example |
|----------|------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulus (remainder) | `a % b` |

**Important Notes:**
- Integer division truncates the fractional part
- Modulus works only with integers
- Division by zero is undefined behavior

```cpp
int a = 10, b = 3;
std::cout << a + b << std::endl;   // 13
std::cout << a - b << std::endl;   // 7
std::cout << a * b << std::endl;   // 30
std::cout << a / b << std::endl;   // 3 (integer division)
std::cout << a % b << std::endl;   // 1 (remainder)

// Floating-point division
double x = 10.0, y = 3.0;
std::cout << x / y << std::endl;   // 3.33333...
```

### 7.2 Increment and Decrement Operators

| Operator | Name | Description |
|----------|------|-------------|
| `++x` | Pre-increment | Increment, then return value |
| `x++` | Post-increment | Return value, then increment |
| `--x` | Pre-decrement | Decrement, then return value |
| `x--` | Post-decrement | Return value, then decrement |

```cpp
int a = 5, b;

b = ++a;  // a becomes 6, b gets 6 (pre-increment)
std::cout << "a=" << a << ", b=" << b << std::endl;  // a=6, b=6

a = 5;
b = a++;  // b gets 5, then a becomes 6 (post-increment)
std::cout << "a=" << a << ", b=" << b << std::endl;  // a=6, b=5
```

### 7.3 Relational Operators

| Operator | Name | Example |
|----------|------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal | `a >= b` |
| `<=` | Less than or equal | `a <= b` |

All relational operators return `bool` (true/false).

```cpp
int x = 10, y = 20;
std::cout << (x == y) << std::endl;  // 0 (false)
std::cout << (x != y) << std::endl;  // 1 (true)
std::cout << (x > y) << std::endl;   // 0 (false)
std::cout << (x < y) << std::endl;   // 1 (true)
```

### 7.4 Logical Operators

| Operator | Name | Description |
|----------|------|-------------|
| `&&` | Logical AND | True if both are true |
| `||` | Logical OR | True if at least one is true |
| `!` | Logical NOT | Inverts boolean value |

```cpp
bool p = true, q = false;

std::cout << (p && q) << std::endl;  // 0 (false)
std::cout << (p || q) << std::endl;  // 1 (true)
std::cout << (!p) << std::endl;      // 0 (false)

// Short-circuit evaluation
int a = 5;
bool result = (a > 0) && (a < 100);  // Both evaluated
result = (a > 10) && (a++ < 100);    // a++ NOT executed (short-circuit)
```

### 7.5 Bitwise Operators

These operators perform operations on individual bits of integer operands.

| Operator | Name | Description |
|----------|------|-------------|
| `&` | Bitwise AND | 1 if both bits are 1 |
| `|` | Bitwise OR | 1 if at least one bit is 1 |
| `^` | Bitwise XOR | 1 if bits are different |
| `~` | Bitwise NOT | Inverts all bits (ones complement) |
| `<<` | Left shift | Shifts bits left, fills with zeros |
| `>>` | Right shift | Shifts bits right (sign-extended for signed) |

```cpp
int a = 12;   // 1100 in binary
int b = 10;   // 1010 in binary

std::cout << (a & b) << std::endl;   // 8  (1000)
std::cout << (a | b) << std::endl;   // 14 (1110)
std::cout << (a ^ b) << std::endl;   // 6  (0110)
std::cout << (~a) << std::endl;      // -13 (two's complement)
std::cout << (a << 2) << std::endl;  // 48 (110000)
std::cout << (a >> 2) << std::endl;  // 3  (0011)

// Practical use: checking/setting flags
const int FLAG_READ = 1;    // 0001
const int FLAG_WRITE = 2;  // 0010
const int FLAG_EXEC = 4;   // 0100

int permissions = FLAG_READ | FLAG_WRITE;  // 0011 (read + write)
bool canRead = permissions & FLAG_READ;    // true
bool canExec = permissions & FLAG_EXEC;    // false
```

### 7.6 Assignment Operators

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `a = b` | `a = b` |
| `+=` | `a += b` | `a = a + b` |
| `-=` | `a -= b` | `a = a - b` |
| `*=` | `a *= b` | `a = a * b` |
| `/=` | `a /= b` | `a = a / b` |
| `%=` | `a %= b` | `a = a % b` |
| `<<=` | `a <<= b` | `a = a << b` |
| `>>=` | `a >>= b` | `a = a >> b` |
| `&=` | `a &= b` | `a = a & b` |
| `^=` | `a ^= b` | `a = a ^ b` |
| `\|=` | `a \|= b` | `a = a \| b` |

```cpp
int x = 10;
x += 5;   // x = 15
x -= 3;   // x = 12
x *= 2;   // x = 24
x /= 4;   // x = 6
x %= 5;   // x = 1
```

### 7.7 Conditional (Ternary) Operator

The ternary operator `? :` is a shorthand for if-else statements.

```cpp
// condition ? expression1 : expression2

int a = 10, b = 20;
int max = (a > b) ? a : b;      // max = 20
int min = (a < b) ? a : b;     // min = 10

// Can be nested (but avoid for readability)
int x = 5, y = 10, z = 15;
int largest = (x > y) ? ((x > z) ? x : z) : ((y > z) ? y : z);
```

### 7.8 Comma Operator

The comma operator evaluates expressions from left to right and returns the value of the rightmost expression.

```cpp
int a, b;
a = (b = 5, b + 10);  // b = 5, then a = 5 + 10 = 15

// Common use in for loops
for (int i = 0, j = 10; i < j; i++, j--) {
    std::cout << i << " " << j << std::endl;
}
```

### 7.9 `sizeof` Operator

The `sizeof` operator returns the size (in bytes) of a type or variable at compile time.

```cpp
#include <iostream>

int main() {
    std::cout << "sizeof(int): " << sizeof(int) << " bytes" << std::endl;
    std::cout << "sizeof(double): " << sizeof(double) << " bytes" << std::endl;
    std::cout << "sizeof(char): " << sizeof(char) << " bytes" << std::endl;
    
    int arr[10];
    std::cout << "sizeof(arr): " << sizeof(arr) << " bytes" << std::endl;
    std::cout << "Array length: " << sizeof(arr) / sizeof(arr[0]) << std::endl;
    
    return 0;
}
```

---

## 8. Type Casting in C++

Type casting converts one data type to another. C++ supports both implicit and explicit type conversion.

### 8.1 Implicit Type Casting (Type Promotion)

The compiler automatically converts types in certain situations:
- Smaller to larger types (e.g., `int` to `double`)
- `char` or `short` to `int`
- Integer types to floating-point types

```cpp
int i = 10;
double d = i;        // Implicit: int → double (10 → 10.0)

char c = 'A';
int x = c;           // Implicit: char → int (65)

// In expressions
int a = 5, b = 2;
double result = a / b;  // Integer division gives 2, then implicit to 2.0
```

### 8.2 Explicit Type Casting (C-Style)

```cpp
double pi = 3.14159;
int truncated = (int)pi;     // C-style cast: 3
int truncated2 = int(pi);    // Functional notation: 3

// More complex example
int x = 10, y = 3;
double avg = (double)x / y;  // Cast x to double for true division
```

### 8.3 C++ Type Cast Operators (Modern C++)

C++ provides safer type cast operators:

```cpp
// static_cast - compile-time type checking
double d = 3.14;
int i = static_cast<int>(d);    // 3

// const_cast - add/remove const qualifier
const int* constPtr = &i;
int* ptr = const_cast<int*>(constPtr);

// reinterpret_cast - low-level reinterpreting of bits
int* intPtr = &i;
char* charPtr = reinterpret_cast<char*>(intPtr);

// dynamic_cast - runtime checked cast (for polymorphism)
class Base { virtual void foo() {} };
class Derived : public Base {};
Base* basePtr = new Derived;
Derived* derivedPtr = dynamic_cast<Derived*>(basePtr);  // Safe downcast
```

---

## 9. Operator Precedence and Associativity

When an expression contains multiple operators, **precedence** determines the order of evaluation. **Associativity** determines the order when operators have the same precedence.

### 9.1 Precedence Table (Highest to Lowest)

| Precedence | Operators | Associativity |
|------------|-----------|---------------|
| 1 (highest) | `::` (scope resolution) | Left-to-right |
| 2 | `()` `[]` `.` `->` `++` `--` (postfix) | Left-to-right |
| 3 | `++` `--` `!` `~` `+` `-` `(type)` `*` `&` `sizeof` | Right-to-left |
| 4 | `*` `/` `%` | Left-to-right |
| 5 | `+` `-` | Left-to-right |
| 6 | `<<` `>>` | Left-to-right |
| 7 | `<` `<=` `>` `>=` | Left-to-right |
| 8 | `==` `!=` | Left-to-right |
| 9 | `&` (bitwise AND) | Left-to-right |
| 10 | `^` (bitwise XOR) | Left-to-right |
| 11 | `|` (bitwise OR) | Left-to-right |
| 12 | `&&` | Left-to-right |
| 13 | `\|\|` | Left-to-right |
| 14 | `? :` (conditional) | Right-to-left |
| 15 | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `^=` `\|=` | Right-to-left |
| 16 (lowest) | `,` | Left-to-right |

### 9.2 Understanding Precedence with Examples

```cpp
int result = 2 + 3 * 4;     // 2 + (3 * 4) = 14 (not (2 + 3) * 4 = 20)
bool flag = 5 > 3 + 2;      // 5 > (3 + 2) = false (5 > 5 = false)
int x = 10 + 20 - 5;        // Left-associative: (10 + 20) - 5 = 25
int y = 2 * 3 / 4;          // Left-associative: (2 * 3) / 4 = 1 (integer)

// Use parentheses for clarity!
int a = ((2 + 3) * 4) - (10 / 2);  // Explicit order: 20 - 5 = 15
```

> **Delhi University Exam Tip**: Always use parentheses when unsure! It makes code clearer and prevents unexpected results.

---

## 10. Key Takeaways

1. **Data Types are Fundamental**: C++ provides primitive (int, float, double, char, bool, void), derived (array, pointer, reference), and user-defined (struct, class, enum) data types.

2. **Type Modifiers and Qualifiers**: Use `signed`/`unsigned`, `short`/`long`/`long long` to modify ranges, and `const`/`volatile`/`mutable` to add compile-time and runtime constraints.

3. **Variables Have Scope and Lifetime**: Understand the difference between automatic (local), static, and global variables to manage memory effectively.

4. **Operators Form the Core of Computation**: Master arithmetic, relational, logical, bitwise, and assignment operators to manipulate data efficiently.

5. **Type Casting is Essential**: Know when to use implicit conversion (automatic) vs. explicit conversion (`static_cast`, C-style casts) to prevent data loss.

6. **Precedence and Associativity Matter**: Always verify the order of operations in complex expressions, or use parentheses for explicit ordering.

7. **Use Constants Appropriately**: Prefer `const` variables and enums over `#define` macros for type safety and better debugging.

---

## 11. Assessment Questions

### 11.1 Multiple Choice Questions (MCQs)

**Level 1: Basic Understanding**

1. What is the size of `int` on a typical 32-bit system?
   - a) 2 bytes
   - b) 4 bytes ✓
   - c) 8 bytes
   - d) 16 bytes

2. Which operator is used to get the address of a variable?
   - a) `*`
   - b) `&` ✓
   - c) `&&`
   - d) `||`

3. What is the result of `10 / 3` in C++ when both operands are integers?
   - a) 3.333
   - b) 3 ✓
   - c) 3.0
   - d) Error

4. Which data type is suitable for storing a single character?
   - a) `int`
   - b) `float`
   - c) `char` ✓
   - d) `bool`

**Level 2: Intermediate Application**

5. What does `volatile` qualifier indicate?
   - a) Variable cannot be modified
   - b) Variable may change unexpectedly ✓
   - c) Variable is constant
   - d) Variable is static

6. What is the output of `sizeof('A')` in C++?
   - a) 1 byte
   - b) 2 bytes
   - c) 4 bytes ✓
   - d) 8 bytes

7. Which operator has the highest precedence among these?
   - a) `+`
   - b) `*` ✓
   - c) `>`
   - d) `=`

8. What is the correct way to declare a constant pointer to an integer?
   - a) `const int* ptr`
   - b) `int const* ptr`
   - c) `int* const ptr` ✓
   - d) Both a and b

**Level 3: Advanced Analysis**

9. Given `int a = 5; int b = a++;`, what are the values of a and b respectively?
   - a) 5, 5
   - b) 6, 5 ✓
   - c) 5, 6
   - d) 6, 6

10. Which cast is safe for downcasting in class inheritance hierarchy?
    - a) `static_cast`
    - b) `const_cast`
    - c) `reinterpret_cast`
    - d) `dynamic_cast` ✓

11. What will `cout << (5 > 3 && 2 < 4)` display?
    - a) 0
    - b) 1 ✓
    - c) true
    - d) false

12. What is the value of the expression `true + false + 3`?
    - a) 4 ✓
    - b) 3
    - c) true
    - d) Compilation error

13. Which storage class persists across function calls?
    - a) `auto`
    - b) `register`
    - c) `static` ✓
    - d) `extern`

14. What is the output of `10 << 2`?
    - a) 12
    - b) 20
    - c) 40 ✓
    - d) 5

15. What does `enum class Color { RED, GREEN, BLUE };` prevent?
    - a) Memory usage
    - b) Implicit conversion to int ✓
    - c) Compilation speed
    - d) Operator overloading

### 11.2 Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **Data Type** | Specifies the type of data a variable can hold |
| **Primitive Types** | Basic built-in types: int, float, double, char, bool, void |
| **Type Modifier** | Alters the meaning of base types (signed, unsigned, short, long) |
| **const Qualifier** | Declares a variable whose value cannot be changed after initialization |
| **volatile Qualifier** | Indicates a variable may change unexpectedly (prevents optimization) |
| **Variable** | Named storage location in memory with a specific type |
| **Scope** | Region of code where a variable is accessible |
| **Lifetime** | Time period during which a variable exists in memory |
| **Operator Precedence** | Rule determining the order of evaluation when multiple operators are present |
| **Associativity** | Direction (left-to-right or right-to-left) operators of same precedence are evaluated |
| **Implicit Type Casting** | Automatic type conversion by the compiler |
| **Explicit Type Casting** | Manual type conversion using cast operators |
| **sizeof Operator** | Returns the size in bytes of a type or variable |
| **Increment Operator (++)** | Increases value by 1 (pre or post) |
| **Modulus Operator (%)** | Returns remainder of integer division |
| **Bitwise AND (&)** | Sets bit to 1 if both corresponding bits are 1 |
| **Bitwise OR (\|)** | Sets bit to 1 if at least one corresponding bit is 1 |
| **Logical NOT (!)** | Inverts boolean value (true→false, false→true) |
| **Ternary Operator (? :)** | Conditional operator: condition ? value_if_true : value_if_false |
| **Static Variable** | Variable with static storage duration, retains value between function calls |
| **Global Variable** | Variable declared outside all functions, accessible throughout the program |
| **Literal Constant** | Fixed value appearing directly in source code (e.g., 42, "hello") |
| **Enumeration (enum)** | User-defined type consisting of named constant integer values |
| **Comma Operator** | Evaluates left operand, discards result, returns right operand value |

---

*This comprehensive study material covers all essential concepts for the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF curriculum on Data Types, Variables, and Operators in C++.*