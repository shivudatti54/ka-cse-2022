# Structures, Unions, and Enumerations

## Introduction
Structures, unions, and enumerations form the backbone of custom data type creation in C programming. Structures allow grouping of heterogeneous data types under a single name, enabling complex data modeling crucial for database systems, game development, and OS kernels. Unions provide memory-efficient alternatives by sharing memory space between members, particularly valuable in embedded systems and protocol design. Enumerations enhance code readability through named integer constants, widely used in state machines and configuration management.

These constructs gain critical importance in system programming where memory optimization and type safety are paramount. For MCA students, mastering these concepts is essential for working with complex data structures, hardware interaction, and implementing algorithms efficiently. Modern applications like IoT device programming (using unions for sensor data) and enterprise software development (using structures for customer records) heavily rely on these fundamentals.

## Key Concepts

**1. Structures**
- *Definition*: User-defined type combining variables of different types
```c
struct Student {
    char name[50];
    int roll_no;
    float marks;
};
```
- Memory allocation: Sum of all members' sizes + padding
- Nested structures: Structures containing other structures
- Arrays of structures: `struct Student class[60];`

**2. Unions**
- Memory overlay concept: All members share same memory location
```c
union SensorData {
    int temperature;
    float pressure;
    char status;
};
```
- Size equals largest member's size
- Type punning: Accessing same memory as different type (C99-compliant)

**3. Enumerations**
- Named integer constants with type safety
```c
enum Weekdays {MON=1, TUE, WED, THU, FRI};
```
- Underlying type: `int` by default (C standard)
- Scope rules: Enumerators have file/block scope

**4. Typedef Usage**
- Creating type aliases:
```c
typedef struct {
    int x,y;
} Point;
```

## Examples

**1. Structure Implementation**
Problem: Create a student database with roll numbers and marks
```c
#include <stdio.h>

struct Student {
    int roll;
    float marks;
};

int main() {
    struct Student s1 = {101, 87.5};
    printf("Roll: %d\nMarks: %.2f", s1.roll, s1.marks);
    return 0;
}
```
Output:
```
Roll: 101
Marks: 87.50
```

**2. Union Memory Demo**
Problem: Show union members share memory
```c
union Test {
    int i;
    char c[4];
};

int main() {
    union Test t;
    t.i = 0x12345678;
    printf("Byte 3: %x", t.c[3]);
    return 0;
}
```
Output (Little Endian):
```
Byte 3: 12
```

**3. Enumeration Application**
Problem: Implement traffic light states
```c
enum TrafficLight {RED, YELLOW, GREEN};

void handle_light(enum TrafficLight curr) {
    switch(curr) {
        case RED: printf("Stop"); break;
        case GREEN: printf("Go"); break;
        case YELLOW: printf("Slow down"); break;
    }
}
```

## Exam Tips
1. Structure padding questions often appear: Use `sizeof` operator with different data type orders
2. Union memory diagrams are common: Draw memory layout for given union definitions
3. Enumeration conversion rules: Remember enums are compatible with `int` but provide type checking
4. Nested structure initialization: Use compound literals `struct A a = {.b = {.x=5}};`
5. Difference between struct and union: Always worth 5 marks - emphasize memory allocation
6. Typedef with structures: Be prepared to write type-safe declarations
7. Bit fields in structures: May appear in embedded systems context questions