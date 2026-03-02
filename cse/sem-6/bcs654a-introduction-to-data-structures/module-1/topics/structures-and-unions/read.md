# Structures and Unions in C

## Introduction

In C programming, the primitive data types (int, float, char, double) are insufficient to represent complex real-world entities that consist of multiple attributes of different types. For instance, a student record requires name (string), roll number (integer), marks (float), and grade (character). Structures and unions provide mechanisms to create user-defined composite data types that can hold heterogeneous data elements.

## 1. Structure Definition

A structure is a user-defined data type that groups together related data items of different types under a single name. The structure serves as a blueprint or template from which structure variables can be created.

### Syntax

```c
struct structure_name {
 data_type member1;
 data_type member2;
 data_type member3;
 // ... additional members as needed
};
```

### Components:

- **struct**: Keyword that declares a structure type
- **structure_name**: User-defined identifier (follows C naming rules)
- **member**: Individual variables of any valid data type
- ** braces**: Delimit the structure body

## 2. Structure Variables

### Declaration Methods

**Method 1: Declare variable with definition**

```c
struct Point {
 int x;
 int y;
} p1; // p1 is a structure variable
```

**Method 2: Declare variables after definition**

```c
struct Point {
 int x;
 int y;
};

struct Point p1, p2; // Multiple variables
```

**Method 3: Using typedef (Recommended)**

```c
typedef struct {
 char name[50];
 int age;
 float salary;
} Employee;

Employee emp1, emp2; // Clean syntax without struct keyword
```

## 3. Accessing Structure Members

### Dot Operator (.)

Used when working with structure variables directly:

```c
struct Student {
 char name[50];
 int roll_no;
 float marks;
};

struct Student s1;
strcpy(s1.name, "John Doe");
s1.roll_no = 101;
s1.marks = 85.5;
```

### Arrow Operator (->)

Used when working with pointers to structures:

```c
struct Student *ptr = &s1;
ptr->roll_no = 102; // Equivalent to (*ptr).roll_no = 102;
ptr->marks = 90.0; // Cleaner than (*ptr).marks
```

**Proof of Equivalence:**
Given `struct Student *ptr;`, the expression `(*ptr).member` is equivalent to `ptr->member` because the arrow operator is syntactic sugar that dereferences the pointer and accesses the member in a single operation.

## 4. Structure Initialization

### At Declaration Time

```c
// Method 1: Order-based initialization
struct Point p1 = {10, 20};

// Method 2: Designated initializers (C99)
struct Point p2 = {.x = 30, .y = 40};

// Method 3: Partial initialization (remaining members set to zero)
struct Point p3 = {.x = 50};
```

### After Declaration

```c
struct Point p1;
p1.x = 10;
p1.y = 20;

// Using memcpy for copying entire structure
struct Point p2;
p2 = p1; // Valid: entire structure assignment
```

## 5. Memory Allocation

### Memory Layout

Each member of a structure occupies separate memory space. The total size of a structure is not simply the sum of member sizes due to **padding** (also called **alignment**).

```c
struct Example {
 char a; // 1 byte
 int b; // 4 bytes (may have 3 bytes padding after 'a')
 char c; // 1 byte (may have 3 bytes padding before)
};
// Actual size: typically 12 bytes (system-dependent)
```

### Size Calculation

```c
#include <stdio.h>

struct Demo {
 char a;
 int b;
 char c;
};

int main() {
 printf("Size of struct Demo: %zu bytes\n", sizeof(struct Demo));
 return 0;
}
```

**Padding Rationale:** Compilers align data to memory boundaries for efficient CPU access. This is hardware-dependent but improves performance.

### Unpacked Structures (GNU C)

```c
struct Packed {
 char a;
 int b;
 char c;
} __attribute__((packed)); // No padding: 6 bytes
```

## 6. Nested Structures

Structures can contain other structures, enabling hierarchical data representation:

```c
struct Date {
 int day;
 int month;
 int year;
};

struct Employee {
 char name[50];
 struct Date birth_date; // Nested structure
 struct Date join_date;
};

struct Employee emp = {
 "Alice Smith",
 {15, 3, 1990},
 {1, 6, 2015}
};

// Accessing nested members
printf("Born: %d/%d/%d\n",
 emp.birth_date.day,
 emp.birth_date.month,
 emp.birth_date.year);
```

## 7. Arrays of Structures

Multiple records of the same structure type can be stored in an array:

```c
#define MAX_STUDENTS 100

struct Student {
 char name[50];
 int roll_no;
 float marks;
};

struct Student class[MAX_STUDENTS];

// Initialize first student
strcpy(class[0].name, "John");
class[0].roll_no = 1;
class[0].marks = 95.5;

// Using loop
for (int i = 0; i < MAX_STUDENTS; i++) {
 printf("Student %d: %s\n", i+1, class[i].name);
}
```

## 8. Self-Referential Structures

A structure that contains a pointer to its own type is called self-referential. This is fundamental for implementing linked data structures:

```c
struct Node {
 int data;
 struct Node *next; // Pointer to same structure type
};

// Creating nodes
struct Node *head = NULL;
head = (struct Node*)malloc(sizeof(struct Node));
head->data = 10;
head->next = NULL;
```

**Critical Application:** Linked lists, binary trees, graphs - all dynamic data structures rely on self-referential structures.

## 9. Unions

### Definition

A union is a special data type where all members share the **same memory location**. Only one member can contain a value at any given time.

```c
union Data {
 int i;
 float f;
 char c;
};

union Data d;
d.i = 10; // Now d.i is valid
printf("%d\n", d.i);
d.f = 3.14; // Overwrites memory; d.i is now invalid
printf("%f\n", d.f);
```

### Memory Allocation

The union size equals its largest member:

```c
union Data {
 int i; // 4 bytes
 float f; // 4 bytes
 char c; // 1 byte
};
// sizeof(union Data) = 4 bytes (largest member)
```

### Practical Use Cases

**1. Memory-Efficient Variant Types:**

```c
union Value {
 int int_val;
 float float_val;
 char *str_val;
};

struct Variant {
 enum Type {INT, FLOAT, STRING} type;
 union Value value;
};
```

**2. Hardware Register Representation:**

```c
union Register {
 unsigned int word;
 struct {
 unsigned char low_byte;
 unsigned char high_byte;
 } bytes;
};
```

## 10. Differences: Structure vs Union

| Aspect         | Structure                             | Union                                   |
| -------------- | ------------------------------------- | --------------------------------------- |
| Memory         | All members occupy separate space     | All members share same memory           |
| Size           | Sum of all members (+ padding)        | Size of largest member                  |
| Access         | All members accessible simultaneously | Only one member valid at a time         |
| Use Case       | Store multiple attributes together    | Save memory for mutually exclusive data |
| Initialization | Can initialize all members            | Can initialize only first member        |

## Summary

This chapter established the foundation for composite data types in C. Structures enable grouping of heterogeneous data, essential for representing real-world entities and implementing complex data structures. Unions provide memory-efficient solutions when data elements are mutually exclusive. These concepts directly support the study of dynamic data structures (linked lists, trees, graphs) and are fundamental to systems programming, file I/O operations, and network protocol implementations.
