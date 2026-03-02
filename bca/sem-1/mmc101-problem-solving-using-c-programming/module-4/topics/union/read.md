# Union in C Programming


## Table of Contents

- [Union in C Programming](#union-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Declaration](#definition-and-declaration)
  - [Memory Allocation in Union](#memory-allocation-in-union)
  - [Accessing Union Members](#accessing-union-members)
  - [Initialization of Unions](#initialization-of-unions)
  - [Anonymous Unions (C11)](#anonymous-unions-c11)
  - [Union of Structures](#union-of-structures)
- [Examples](#examples)
  - [Example 1: Converting Integer to Bytes](#example-1-converting-integer-to-bytes)
  - [Example 2: Employee Data Type Switching](#example-2-employee-data-type-switching)
  - [Example 3: Point Representation](#example-3-point-representation)
- [Exam Tips](#exam-tips)

## Introduction

A union is a special data type available in C that allows storing different data types in the same memory location. While structures allocate memory for each member separately, a union shares the same memory space for all its members. This unique characteristic makes unions particularly useful in scenarios where memory efficiency is critical or when the same memory location needs to be interpreted in different ways.

In the context of computer science at University of Delhi, understanding unions is essential for several reasons. First, unions are fundamental to implementing low-level programming concepts such as protocol handlers, device registers, and memory-mapped I/O. Second, they demonstrate how memory can be interpreted differently based on context, which is crucial for understanding data representation and memory management. Third, unions are frequently tested in university examinations and are practical tools for solving real-world programming problems involving heterogeneous data that occupies the same memory space.

The concept of union becomes particularly important when studying data structures, operating systems, and embedded systems programming. Students at DU often encounter unions in the context of creating efficient data structures and understanding how compilers manage memory allocation.

## Key Concepts

### Definition and Declaration

A union is defined using the `union` keyword, similar to how structures are defined. The syntax differs only in the keyword used:

```c
union union_name {
    data_type member1;
    data_type member2;
    data_type member3;
};
```

The fundamental difference between a structure and a union lies in memory allocation. In a structure, each member occupies its own memory space, and the total size equals the sum of all member sizes (plus padding). In a union, all members share the same memory location, and the total size equals the size of the largest member only.

Consider the following example:

```c
union Data {
    int i;
    float f;
    char c;
};
```

In this union named `Data`, only 4 bytes (assuming `int` is 4 bytes and is the largest) are allocated, regardless of whether we store an integer, a float, or a character. This is because all three members occupy the same memory space.

### Memory Allocation in Union

The compiler allocates memory equal to the size of the largest member in the union. When you store a value in one member, the values in other members become undefined or contain garbage values. This behavior is both the strength and the caution point of using unions.

For the union defined above:

```c
union Data {
    int i;
    float f;
    char c;
};

int main() {
    union Data d;
    printf("Size of union Data: %zu bytes\n", sizeof(d));
    return 0;
}
```

If `int` is 4 bytes on the system, this will print 4 bytes, which is the size of the largest member. In contrast, a structure containing the same members would require at least 7 bytes (4 + 4 + 1, plus possible padding).

### Accessing Union Members

Union members are accessed using the dot operator (`.`) for regular unions or the arrow operator (`->`) for pointers to unions, exactly as with structures:

```c
union Data d;
d.i = 10;           // Store integer value
printf("%d\n", d.i); // Access as integer

d.f = 3.14;         // Store float value (overwrites integer value)
printf("%f\n", d.f); // Access as float

d.c = 'A';          // Store character (overwrites previous values)
printf("%c\n", d.c); // Access as character
```

IMPORTANT: After storing a value in one member, interpreting the union through another member leads to undefined behavior and garbage values.

### Initialization of Unions

C provides specific rules for initializing unions:

```c
union Data d1 = {10};        // Initializes first member (i = 10)
union Data d2 = {.f = 3.14}; // Designated initializer (f = 3.14)
union Data d3 = d1;          // Copy initialization
```

Only the first member can be initialized using the traditional initializer syntax. Designated initializers (C99 standard) allow initializing any member by name.

### Anonymous Unions (C11)

The C11 standard introduced anonymous unions, which are unions declared without a name. These are particularly useful within structures:

```c
struct Player {
    char name[50];
    union {
        int integer_score;
        float decimal_score;
    };
};

int main() {
    struct Player p;
    strcpy(p.name, "Rahul");
    p.integer_score = 100;  // Direct access without union name
    printf("Score: %d\n", p.integer_score);
    return 0;
}
```

In anonymous unions, members can be accessed directly as if they were members of the enclosing structure, eliminating the need for the union name.

### Union of Structures

A powerful application involves creating unions of structures to efficiently store different types of related data:

```c
struct IntPair {
    int x;
    int y;
};

struct FloatPair {
    float a;
    float b;
};

union NumberPair {
    struct IntPair ip;
    struct FloatPair fp;
};
```

This allows the same memory to be interpreted either as two integers or as two floats.

## Examples

### Example 1: Converting Integer to Bytes

A practical use of union is to break down an integer into its constituent bytes:

```c
#include <stdio.h>

union IntBytes {
    int value;
    unsigned char bytes[4];
};

int main() {
    union IntBytes ib;
    ib.value = 0x12345678;
    
    printf("Integer value: 0x%X\n", ib.value);
    printf("Byte 0: 0x%02X\n", ib.bytes[0]);
    printf("Byte 1: 0x%02X\n", ib.bytes[1]);
    printf("Byte 2: 0x%02X\n", ib.bytes[2]);
    printf("Byte 3: 0x%02X\n", ib.bytes[3]);
    
    return 0;
}
```

Output:
```
Integer value: 0x12345678
Byte 0: 0x78
Byte 1: 0x56
Byte 2: 0x34
Byte 3: 0x12
```

This demonstrates how the same 4 bytes can be viewed either as a single integer or as an array of bytes, which is essential for network programming and low-level system operations.

### Example 2: Employee Data Type Switching

Consider an application where employee bonuses can be calculated either as a fixed amount or as a percentage:

```c
#include <stdio.h>
#include <string.h>

enum BonusType { FIXED, PERCENTAGE };

struct Employee {
    char name[50];
    float salary;
    enum BonusType bonus_type;
    union {
        float fixed_bonus;
        float percentage;
    } bonus;
};

void calculate_bonus(struct Employee *emp) {
    if (emp->bonus_type == FIXED) {
        printf("%s gets fixed bonus: Rs. %.2f\n", emp->name, emp->bonus.fixed_bonus);
    } else {
        float amount = emp->salary * emp->bonus.percentage / 100;
        printf("%s gets percentage bonus: Rs. %.2f (%.1f%% of salary)\n", 
               emp->name, amount, emp->bonus.percentage);
    }
}

int main() {
    struct Employee emp1, emp2;
    
    strcpy(emp1.name, "Priya");
    emp1.salary = 50000;
    emp1.bonus_type = FIXED;
    emp1.bonus.fixed_bonus = 5000;
    
    strcpy(emp2.name, "Amit");
    emp2.salary = 60000;
    emp2.bonus_type = PERCENTAGE;
    emp2.bonus.percentage = 10;
    
    calculate_bonus(&emp1);
    calculate_bonus(&emp2);
    
    return 0;
}
```

Output:
```
Priya gets fixed bonus: Rs. 5000.00
Amit gets percentage bonus: Rs. 6000.00 (10.0% of salary)
```

This example shows how unions enable storing mutually exclusive data efficiently, with the enum indicating which union member is currently valid.

### Example 3: Point Representation

A union can represent a point in either Cartesian or polar coordinates:

```c
#include <stdio.h>
#include <math.h>

struct Cartesian {
    float x;
    float y;
};

struct Polar {
    float radius;
    float angle;
};

union Point {
    struct Cartesian cp;
    struct Polar pp;
};

void print_cartesian(union Point p) {
    printf("Cartesian: (%.2f, %.2f)\n", p.cp.x, p.cp.y);
}

void print_polar(union Point p) {
    printf("Polar: (%.2f, %.2f radians)\n", p.pp.radius, p.pp.angle);
}

int main() {
    union Point p1, p2;
    
    // Using Cartesian
    p1.cp.x = 3.0;
    p1.cp.y = 4.0;
    print_cartesian(p1);
    
    // Using Polar
    p2.pp.radius = 5.0;
    p2.pp.angle = 0.9273; // approximately 53.13 degrees
    print_polar(p2);
    
    return 0;
}
```

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. STRUCTURE VS UNION: The primary distinction is that structures allocate separate memory for each member, while unions share the same memory for all members. This is frequently tested in objective questions.

2. SIZE OF UNION: The size of a union is equal to the size of its largest member, not the sum of all members. Remember to account for padding.

3. MEMORY OVERLAPPING: Understand that writing to one union member overwrites other members because they share the same memory location.

4. INITIALIZATION RULES: Only the first member can be initialized using traditional syntax. Use designated initializers (C99) for initializing other members.

5. PRACTICAL APPLICATIONS: Be familiar with common use cases: byte extraction, type punning, memory-mapped hardware registers, and variant records.

6. ACCESS OPERATORS: Remember to use the dot operator (.) for union variables and arrow operator (->) for pointers to unions, identical to structure usage.

7. ANONYMOUS UNIONS: Know that C11 introduced anonymous unions, which allow accessing union members directly without the union name when inside a structure.

8. INITIALIZATION WITH BRACES: When initializing unions, remember that `_typeunion var = {value};` initializes only the first member.

9. COMMON MISTAKES: Avoid accessing a union member after storing a different type; this leads to undefined behavior and garbage values.

10. TYPEDEF WITH UNIONS: Unions can be typedef'd just like structures for cleaner code.