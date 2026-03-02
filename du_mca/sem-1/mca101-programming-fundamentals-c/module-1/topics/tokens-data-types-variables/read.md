# Programming Fundamentals C: Tokens, Data Types, and Variables

## A Comprehensive Study Material for MCA - Delhi University (Revised June 2024)

---

## 1. Introduction

C programming language, developed by Dennis Ritchie at Bell Labs in 1972, remains one of the most influential and foundational programming languages in computer science. Despite being several decades old, C continues to serve as the backbone for operating systems (UNIX, Linux), embedded systems, database engines, and high-performance applications. Understanding the fundamental building blocks of C—tokens, data types, and variables—is essential for any MCA student at Delhi University, as these concepts form the bedrock of all subsequent programming endeavors.

This study material comprehensively covers the tokens, data types, and variables as prescribed in the Delhi University MCA syllabus (Revised June 2024). The content addresses the limitations of previous versions by providing in-depth C-specific explanations, detailed memory representations, practical code examples, and coverage of type modifiers and storage classes that were previously missing.

---

## 2. Tokens in C

In the C programming language, a **token** is the smallest individual unit of a program that the compiler recognizes. Think of tokens as the "words" of the C language—without them, the compiler cannot parse and understand your code. C language defines six categories of tokens:

### 2.1 Keywords (Reserved Words)

Keywords are predefined, reserved identifiers that have special meaning to the C compiler. They cannot be used as variable names, function names, or any other user-defined identifiers. The C standard (C89/C90, C99, C11, C17) defines a set of keywords.

**Commonly Used Keywords:**

| Category | Keywords |
|----------|----------|
| Data Types | int, float, double, char, void, long, short, signed, unsigned |
| Control Flow | if, else, switch, case, default, while, do, for, break, continue, goto, return |
| Storage Classes | auto, register, static, extern, const, volatile, typedef |
| Structure/Union | struct, union, enum |
| Others | sizeof, typedef |

**Example demonstrating keywords:**
```c
int main()          // 'int' is a keyword (return type)
{
    auto int count; // 'auto' is a storage class keyword
    static float pi = 3.14f;  // 'static' and 'float' are keywords
    const int MAX = 100;       // 'const' is a qualifier
    
    for(count = 0; count < MAX; count++)  // 'for' is a keyword
    {
        // code
    }
    return 0;  // 'return' is a keyword
}
```

### 2.2 Identifiers

An **identifier** is a user-defined name given to variables, functions, arrays, structures, unions, or other user-defined items. Identifiers must follow specific rules:

**Rules for Valid Identifiers:**
- Must begin with a letter (A-Z, a-z) or underscore (_)
- Cannot be a keyword
- Can contain letters, digits (0-9), and underscores
- Case-sensitive (e.g., `count`, `Count`, and `COUNT` are three different identifiers)
- Cannot contain spaces or special characters like @, #, $, %
- Should not exceed 31 characters (implementation-dependent)

**Good vs Bad Identifiers:**

| Good Identifiers | Bad Identifiers | Reason |
|-----------------|-----------------|--------|
| `studentName` | `student name` | Contains space |
| `maxValue` | `max-value` | Contains hyphen |
| `counter1` | `1counter` | Begins with digit |
| `_privateVar` | `int` | Uses keyword |

**Delhi University Examination Tip:** Always follow meaningful naming conventions. Use camelCase or snake_case consistently throughout your program.

### 2.3 Constants

Constants are fixed values that do not change during program execution. In C, constants can be of various types:

**Integer Constants:**
```c
 decimal: 25, -100, 32767
 octal:   031, 0777 (prefixed with 0)
 hex:     0x25, 0xFF (prefixed with 0x or 0X)
```

**Floating-Point Constants:**
```c
3.14          // double by default
3.14f         // float (suffix 'f' or 'F')
3.14L         // long double (suffix 'L' or 'l')
1.5e10        // exponential notation (1.5 × 10¹⁰)
```

**Character Constants:**
```c
'A'           // single character
'\n'          // escape sequence (newline)
'\t'          // tab
'\\'          // backslash character
'\x41'        // hexadecimal escape sequence
```

**String Constants:**
```c
"Hello"           // string literal
"Delhi University" 
"Line1\nLine2"    // string with newline escape
```

### 2.4 Operators

Operators are symbols that tell the compiler to perform specific mathematical, logical, or relational operations. C supports a rich set of operators:

**Categories of Operators:**

1. **Arithmetic Operators:** `+`, `-`, `*`, `/`, `%`
2. **Relational Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`
3. **Logical Operators:** `&&`, `||`, `!`
4. **Bitwise Operators:** `&`, `|`, `^`, `~`, `<<`, `>>`
5. **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`
6. **Increment/Decrement:** `++`, `--`
7. **Conditional Operator:** `? :`
8. **Special Operators:** `sizeof`, `&` (address-of), `*` (dereference)

**Example demonstrating operators:**
```c
int a = 10, b = 3;
int sum = a + b;      // Arithmetic: 13
int quotient = a / b; // Arithmetic: 3
int remainder = a % b; // Arithmetic: 1
int isEqual = (a == b); // Relational: 0 (false)
int logical = (a > 5) && (b < 5); // Logical: 1 (true)
a++;                  // Increment: a becomes 11
```

### 2.5 Special Symbols

C uses various special symbols that serve specific purposes:

| Symbol | Purpose |
|--------|---------|
| `[]` | Array subscript |
| `()` | Function call, grouping |
| `{}` | Block structure |
| `,` | Separator in lists |
| `;` | Statement terminator |
| `:` | Label identifier, ternary operator |
| `*` | Pointer declaration, multiplication |
| `#` | Preprocessor directive |

---

## 3. Data Types in C

Data types in C specify the type of data that a variable can hold. Understanding data types is crucial for memory management and performing operations correctly. C provides a rich hierarchy of data types.

### 3.1 Primary (Fundamental) Data Types

These are the basic data types in C, also known as primitive or built-in types:

| Data Type | Size (Typical) | Range | Description |
|-----------|----------------|-------|-------------|
| `char` | 1 byte | -128 to 127 (signed) or 0 to 255 (unsigned) | Stores single character |
| `int` | 2 or 4 bytes | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647 | Integer values |
| `float` | 4 bytes | ±3.4e±38 (with 6 decimal digits) | Single-precision floating point |
| `double` | 8 bytes | ±1.7e±308 (with 15 decimal digits) | Double-precision floating point |
| `void` | 0 bytes | No value | Represents absence of type |

**Note:** The actual sizes depend on the system architecture (16-bit, 32-bit, 64-bit) and compiler. Use `sizeof()` operator to determine exact sizes on your system.

### 3.2 Type Modifiers

C provides modifiers that alter the meaning of the base data types:

| Modifier | Applicable To | Effect |
|----------|---------------|--------|
| `short` | int, long | Reduces size (typically 2 bytes) |
| `long` | int, double | Increases size (4 or 8 bytes) |
| `long long` | int | 8 bytes on most systems |
| `signed` | char, int | Allows negative values (default for int) |
| `unsigned` | char, int | Only positive values (0 to 2ⁿ-1) |

**Commonly Used Data Types with Modifiers:**

```c
short int age;           // Typically 2 bytes
long int population;     // Typically 4 or 8 bytes
long long int bigNumber; // Typically 8 bytes
unsigned int count;      // 0 to 4,294,967,295
signed int value;        // Same as int (default)
unsigned char byte;      // 0 to 255
long double precision;   // Extended precision (10+ bytes)
```

### 3.3 Type Qualifiers

Type qualifiers provide additional information about variables:

| Qualifier | Purpose |
|-----------|---------|
| `const` | Declares variables whose value cannot be changed after initialization |
| `volatile` | Informs compiler that variable may be modified by external factors |
| `restrict` | (C99) Indicates pointer is the only reference to the object |

**Example:**
```c
const int MAX_SIZE = 100;  // Cannot be modified
MAX_SIZE = 200;            // ERROR: assignment of read-only variable

volatile int hardwareReg;  // May change unexpectedly (e.g., hardware register)
```

### 3.4 Derived Data Types

Derived data types are created from primary data types:

- **Arrays:** Collection of elements of the same type
- **Pointers:** Variables that store memory addresses
- **Functions:** Reusable code blocks that return a value

### 3.5 User-Defined Data Types

C allows creation of custom data types:

- **Structures (`struct`):** Collection of dissimilar types
- **Unions (`union`):** Shared memory for different types
- **Enumerations (`enum`):** Set of named integer constants

### 3.6 Memory Representation

Understanding how data types are stored in memory is essential for MCA students:

**Integer (int) - 4 bytes (32-bit system):**
```
Memory Address    Binary Representation    Decimal Value
0x1000            00000000 00000000        0
                  00000000 00000001        1
0x1004            11111111 11111111        -1 (two's complement)
                  11111111 11111110        -2
```

**Character (char) - 1 byte:**
```
'A' = 65 = 01000001
'B' = 66 = 01000010
'a' = 97 = 01100001
```

**Floating-Point (IEEE 754 - 32-bit):**
```
Sign (1 bit) | Exponent (8 bits) | Mantissa (23 bits)
    0        |     10000001      |    01000000000000000000000
```

### 3.7 Determining Sizes

Use `sizeof` operator to find the size of any data type on your system:

```c
#include <stdio.h>

int main() {
    printf("Size of char: %zu byte(s)\n", sizeof(char));
    printf("Size of int: %zu byte(s)\n", sizeof(int));
    printf("Size of float: %zu byte(s)\n", sizeof(float));
    printf("Size of double: %zu byte(s)\n", sizeof(double));
    printf("Size of long int: %zu byte(s)\n", sizeof(long int));
    printf("Size of long double: %zu byte(s)\n", sizeof(long double));
    
    return 0;
}
```

---

## 4. Variables in C

A **variable** is a named memory location that stores a value which can be modified during program execution. Variables are fundamental to programming as they provide a way to work with data.

### 4.1 Declaration vs Definition

**Declaration:** Announces the variable's name and type without allocating memory (for external declarations):
```c
extern int age;  // Declaration - tells compiler variable exists elsewhere
```

**Definition:** Allocates memory for the variable:
```c
int age;        // Definition - allocates 4 bytes (typically)
int age = 25;   // Definition with initialization
```

### 4.2 Variable Naming

**Syntax for Variable Declaration:**
```
[data_type] [variable_name] [= initial_value];
```

**Examples:**
```c
int count;
float salary;
char grade = 'A';
double pi = 3.14159265358979;
```

### 4.3 Initialization

Variables can be initialized at the time of declaration:

```c
int x = 10;           // Direct initialization
int y = x + 5;        // Initialization using expression
int z;                // Uninitialized (contains garbage value)
z = 20;               // Assignment (not initialization)
```

**Important:** Always initialize variables before use. Using uninitialized variables leads to undefined behavior (garbage values).

### 4.4 Storage Classes in C

Storage classes define the **scope**, **lifetime**, **storage location**, and **initialization** of variables. This is a critical topic often tested in Delhi University examinations:

| Storage Class | Keyword | Storage | Default Initial Value | Scope | Lifetime |
|---------------|---------|---------|----------------------|-------|----------|
| Automatic | `auto` | Stack | Garbage | Block | Function |
| Register | `register` | CPU Register | Garbage | Block | Function |
| Static | `static` | Data Segment | Zero | Block/File | Program |
| External | `extern` | Data Segment | Zero | File | Program |

**Detailed Explanation:**

**1. Auto Storage Class:**
```c
void function() {
    auto int count = 0;  // 'auto' is default for local variables
    count++;            // Created when function is called
}                       // Destroyed when function ends
```
- Most commonly used storage class for local variables
- Memory is allocated on the stack

**2. Register Storage Class:**
```c
void function() {
    register int i;      // Request storage in CPU register
    for(i = 0; i < 100; i++) {
        // Operations
    }
}
```
- Suggests compiler to store in CPU register for faster access
- Cannot use `&` (address-of) operator on register variables
- Limited to integer types typically

**3. Static Storage Class:**
```c
void counter() {
    static int count = 0;  // Initialized only once
    count++;
    printf("Count: %d\n", count);
}

int main() {
    counter();  // Output: Count: 1
    counter();  // Output: Count: 2
    counter();  // Output: Count: 3
    return 0;
}
```
- Retains value between function calls
- Initialized to zero if not explicitly initialized
- Memory allocated in data segment (not stack)

**4. External (Extern) Storage Class:**
```c
// file1.c
#include <stdio.h>
int globalVar = 100;  // Definition

void display() {
    printf("Global: %d\n", globalVar);
}

// file2.c
#include <stdio.h>
extern int globalVar;  // Declaration (reference to file1.c)

int main() {
    printf("Accessing: %d\n", globalVar);
    return 0;
}
```
- Declares a variable defined elsewhere in the program
- Used for sharing variables across multiple source files
- Lifetime is entire program duration

### 4.5 Scope and Lifetime

**Scope** defines where a variable can be accessed:
- **Block Scope:** Variables declared inside a block `{}`
- **Function Scope:** Labels only visible within function
- **File Scope:** Variables declared outside functions (global variables)

**Lifetime (Storage Duration):**
- **Automatic:** Created on block entry, destroyed on exit
- **Static:** Exists for entire program duration
- **Dynamic:** Created/destroyed using malloc/free

### 4.6 Constants vs Variables

| Aspect | Variable | Constant |
|--------|----------|----------|
| Value | Can change during execution | Cannot change after initialization |
| Declaration | `int x;` | `const int x = 10;` or `#define X 10` |
| Memory | Allocated in RAM | Depends on implementation |
| Use | For modifiable data | For fixed values like PI, MAX_SIZE |

---

## 5. Comprehensive Code Examples

### Example 1: Demonstrating Tokens, Variables, and Data Types

```c
#include <stdio.h>

// Global variable - file scope, static storage
const float PI = 3.14159f;
int globalCounter = 0;

// Function prototype
void demonstrateTokens(int count, float rate);

int main() {
    // Keywords: int, float, return, const
    // Identifiers: main, count, rate, result, etc.
    
    // Primary data types
    int studentRoll = 101;           // Integer
    char grade = 'A';                 // Character
    float percentage = 85.5f;         // Float
    double preciseValue = 3.14159265358979; // Double
    
    // Type modifiers
    unsigned int positiveNumber = 500;
    long int largeNumber = 123456789L;
    short int smallNumber = 100;
    
    // Constants
    const int MAX_ATTEMPTS = 3;
    enum days {SUN, MON, TUE, WED, THU, FRI, SAT};
    enum days today = MON;
    
    // Operators used
    int sum = studentRoll + positiveNumber;       // Arithmetic
    int isPass = (percentage >= 60);              // Relational
    int logicalAnd = (grade == 'A') && isPass;    // Logical
    
    // Printing results
    printf("=== Data Types Demo ===\n");
    printf("Integer: %d\n", studentRoll);
    printf("Character: %c\n", grade);
    printf("Float: %.2f\n", percentage);
    printf("Double: %.15lf\n", preciseValue);
    printf("Unsigned: %u\n", positiveNumber);
    printf("Long: %ld\n", largeNumber);
    printf("Short: %hd\n", smallNumber);
    printf("Enum value: %d (MON=1)\n", today);
    
    printf("\n=== Operators Demo ===\n");
    printf("Sum: %d\n", sum);
    printf("Is Pass: %d\n", isPass);
    printf("Logical AND: %d\n", logicalAnd);
    
    // Function call
    demonstrateTokens(10, 2.5f);
    
    return 0;  // Return keyword
}

void demonstrateTokens(int count, float rate) {
    // Auto storage class (default for local)
    auto int localVar = 100;
    
    // Static variable - retains value between calls
    static int staticVar = 0;
    staticVar++;
    
    printf("\n=== Function Scope Demo ===\n");
    printf("Local (auto): %d\n", localVar);
    printf("Static: %d\n", staticVar);
    printf("Global (via parameter): count=%d, rate=%.2f\n", count, rate);
    printf("Constant PI: %.5f\n", PI);
}
```

### Example 2: Memory Representation and Storage Classes

```c
#include <stdio.h>

// Global variables - extern storage class by default
int globalVar = 50;           // Default: 0 if not initialized (static duration)
int externVar;                 // Zero-initialized automatically

// Static global - file scope, static storage
static int staticGlobal = 100; // Only accessible in this file

void function1(void);
void function2(void);

int main() {
    printf("=== Storage Classes Demonstration ===\n\n");
    
    // Automatic variables (auto - default for local)
    auto int autoVar = 10;
    printf("Auto variable: %d (stored in stack)\n", autoVar);
    
    // Register variable
    register int regVar = 20;
    printf("Register variable: %d (stored in CPU register)\n", regVar);
    
    // Static local variable
    static int staticLocal = 0;
    printf("\n--- Calling function1 multiple times ---\n");
    function1();  // staticLocal becomes 1
    function1();  // staticLocal becomes 2
    function1();  // staticLocal becomes 3
    
    printf("\n--- Calling function2 ---\n");
    function2();
    
    printf("\n=== Memory Addresses ===\n");
    printf("Global variable address: %p\n", (void*)&globalVar);
    printf("Static global address: %p\n", (void*)&staticGlobal);
    printf("Auto variable address: %p\n", (void*)&autoVar);
    printf("Static local address: %p\n", (void*)&staticLocal);
    
    return 0;
}

void function1(void) {
    static int count = 0;  // Initialized only once, retains value
    count++;
    printf("function1 called: count = %d\n", count);
}

void function2(void) {
    // External variable usage - declared in main or another file
    extern int externVar;
    externVar = 75;
    printf("Extern variable: %d (defined in main file scope)\n", externVar);
}
```

---

## 6. Key Takeaways

1. **Tokens** are the smallest units of C programming: keywords (reserved), identifiers (user-defined), constants (fixed values), operators (operations), and special symbols (syntax elements).

2. **Data Types** define the type and size of data:
   - Primary: `int`, `char`, `float`, `double`, `void`
   - Modifiers: `short`, `long`, `signed`, `unsigned`
   - Qualifiers: `const`, `volatile`, `restrict`

3. **Variables** are named memory locations with:
   - Declaration: announces the variable
   - Definition: allocates memory
   - Initialization: assigns initial value

4. **Storage Classes** determine variable behavior:
   - `auto`: default local, stack memory
   - `register`: faster access, CPU register
   - `static`: retains value, data segment
   - `extern`: global scope, cross-file access

5. Use `sizeof()` operator to determine exact data type sizes on your system.

6. Always initialize variables before use to avoid undefined behavior.

7. Constants should be declared with `const` keyword or `#define` macro.

---

## 7. Multiple Choice Questions

### Level 1: Basic Understanding

1. **Which of the following is NOT a token in C?**
   - (a) Keywords
   - (b) Identifiers
   - (c) Objects
   - (d) Operators
   
   **Answer:** (c) Objects

2. **What is the size of `int` on a typical 32-bit system?**
   - (a) 1 byte
   - (b) 2 bytes
   - (c) 4 bytes
   - (d) 8 bytes
   
   **Answer:** (c) 4 bytes

3. **Which keyword is used to declare a constant variable?**
   - (a) constant
   - (b) static
   - (c) const
   - (d) immutable
   
   **Answer:** (c) const

### Level 2: Intermediate Concepts

4. **What is the output of the following code?**
   ```c
   #include <stdio.h>
   int main() {
       int x = 10;
       {
           int x = 20;
           printf("%d ", x);
       }
       printf("%d", x);
       return 0;
   }
   ```
   - (a) 10 20
   - (b) 20 10
   - (c) 20 20
   - (d) 10 10
   
   **Answer:** (b) 20 10

5. **Which storage class variable retains its value between function calls?**
   - (a) auto
   - (b) register
   - (c) static
   - (d) extern
   
   **Answer:** (c) static

6. **What is the range of `unsigned char`?**
   - (a) -128 to 127
   - (b) 0 to 127
   - (c) 0 to 255
   - (d) -255 to 255
   
   **Answer:** (c) 0 to 255

### Level 3: Advanced Application

7. **What will be printed?**
   ```c
   #include <stdio.h>
   void func() {
       static int x = 5;
       x++;
       printf("%d ", x);
   }
   int main() {
       func();  // First call
       func();  // Second call
       func();  // Third call
       return 0;
   }
   ```
   - (a) 5 5 5
   - (b) 6 6 6
   - (c) 6 7 8
   - (d) 5 6 7
   
   **Answer:** (c) 6 7 8

8. **Which of the following is correct about `register` storage class?**
   - (a) Variables are stored in stack
   - (b) Cannot use address-of operator (&)
   - (c) Has file scope
   - (d) Default for global variables
   
   **Answer:** (b) Cannot use address-of operator (&)

9. **What does `sizeof(int)` return if int is 4 bytes and we are on a 64-bit system?**
   - (a) 2
   - (b) 4
   - (c) 8
   - (d) Depends on compiler
   
   **Answer:** (b) 4

### Level 4: Critical Thinking

10. **Consider the following code:**
    ```c
    #include <stdio.h>
    int main() {
        const int x = 10;
        int *ptr = &x;
        *ptr = 20;
        printf("%d", x);
        return 0;
    }
    ```
    This code will:
    - (a) Print 10
    - (b) Print 20
    - (c) Generate compilation error
    - (d) Cause undefined behavior
    
    **Answer:** (d) Cause undefined behavior (modifying const through pointer)

11. **Which operator is used to determine the size of a data type?**
    - (a) size
    - (b) sizeof
    - (c) sizeOf
    - (d) dimension
    
    **Answer:** (b) sizeof

12. **In IEEE 754, a float (32-bit) consists of:**
    - (a) 1 bit sign, 8 bits exponent, 23 bits mantissa
    - (b) 1 bit sign, 23 bits exponent, 8 bits mantissa
    - (c) 8 bits sign, 1 bit exponent, 23 bits mantissa
    - (d) 32 bits mantissa
    
    **Answer:** (a) 1 bit sign, 8 bits exponent, 23 bits mantissa

---

## References

1. Kernighan, B. W., & Ritchie, D. M. (1988). *The C Programming Language* (2nd ed.). Prentice Hall.
2. Prata, S. (2004). *C Primer Plus* (5th ed.). Sams Publishing.
3. Delhi University MCA Syllabus, Revised June 2024 - Programming Fundamentals C.
4. ISO/IEC 9899:2011 (C11 Standard)

---

*This study material is specifically designed for MCA students at Delhi University as per the Revised June 2024 syllabus. For additional practice, refer to laboratory manuals and previous year question papers.*