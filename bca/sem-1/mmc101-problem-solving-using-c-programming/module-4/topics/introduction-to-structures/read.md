# Introduction To Structures


## Table of Contents

- [Introduction To Structures](#introduction-to-structures)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Declaration of a Structure](#definition-and-declaration-of-a-structure)
  - [Structure Variables](#structure-variables)
  - [Accessing Structure Members](#accessing-structure-members)
  - [Initializing Structures](#initializing-structures)
  - [Size of a Structure](#size-of-a-structure)
  - [Memory Layout](#memory-layout)
- [Examples](#examples)
  - [Example 1: Student Record Management](#example-1-student-record-management)
  - [Example 2: Complex Number Addition](#example-2-complex-number-addition)
  - [Example 3: Date Structure and Validation](#example-3-date-structure-and-validation)
- [Exam Tips](#exam-tips)

## Introduction

In C programming, arrays provide a way to store multiple elements of the same data type. However, real-world problems often require grouping together related data items of different types. For instance, consider a student record that contains name (string), roll number (integer), marks (float), and grade (character). Since these data items are of different types, arrays cannot be used to store such heterogeneous data. This is where structures come into play.

A structure is a user-defined data type that allows you to combine data items of different types under a single name. It is one of the most powerful features of C that enables programmers to create complex data types representing real-world entities. Structures provide a way to organize related data that logically belongs together, making programs more readable, maintainable, and efficient.

In the context of the University of Delhi's Computer Science curriculum, structures form the foundation for understanding advanced data structures like linked lists, trees, and graphs. They are extensively used in file handling, database systems, and system programming. Understanding structures is essential for solving complex programming problems and is frequently tested in both internal assessments and end-semester examinations.

## Key Concepts

### Definition and Declaration of a Structure

A structure is defined using the `struct` keyword followed by a structure tag (name) and a block containing member declarations. The general syntax is:

```c
struct structure_tag_name {
    data_type member1;
    data_type member2;
    data_type member3;
    // ... more members
};
```

Each member in a structure can be of any data type, including basic types (int, float, char), arrays, pointers, or even other structures.

### Structure Variables

After defining a structure, you can declare variables of that structure type in several ways:

**Method 1: Declare variable after structure definition**
```c
struct Student {
    char name[50];
    int roll_no;
    float marks;
};

struct Student s1, s2;
```

**Method 2: Declare variable during structure definition**
```c
struct Employee {
    int emp_id;
    char name[30];
    float salary;
} emp1, emp2;
```

**Method 3: Using typedef for convenience**
```c
typedef struct {
    char title[50];
    char author[30];
    int pages;
} Book;

Book b1, b2;
```

### Accessing Structure Members

Structure members are accessed using the dot (.) operator (member access operator) when working with structure variables. The syntax is:

```c
variable_name.member_name
```

For example:
```c
struct Student {
    char name[50];
    int roll_no;
    float marks;
};

struct Student s1;
strcpy(s1.name, "Rahul Kumar");
s1.roll_no = 101;
s1.marks = 85.5;
```

### Initializing Structures

Structures can be initialized at the time of declaration using curly braces:

```c
struct Point {
    int x;
    int y;
};

struct Point p1 = {10, 20};
struct Point p2 = {.x = 30, .y = 40};  // Designated initializers (C99)
```

### Size of a Structure

The size of a structure is not simply the sum of sizes of its members due to **padding**. The compiler adds padding bytes between members to align data at appropriate memory addresses for efficient access. This concept is important from an exam perspective.

```c
struct Example {
    char a;    // 1 byte + 3 padding bytes
    int b;     // 4 bytes
    char c;    // 1 byte + 7 padding bytes (for alignment)
};

printf("%zu", sizeof(struct Example));  // May output 12 or 16 depending on compiler
```

### Memory Layout

Structures store members sequentially in memory. The address of the structure variable points to its first member. Understanding this layout is crucial for topics like file handling and dynamic memory allocation.

## Examples

### Example 1: Student Record Management

Write a program to store and display information of 3 students using structures.

```c
#include <stdio.h>
#include <string.h>

struct Student {
    char name[50];
    int roll_no;
    float marks;
};

int main() {
    struct Student s[3];
    int i;
    
    // Input details for 3 students
    for (i = 0; i < 3; i++) {
        printf("\nEnter details for Student %d:\n", i + 1);
        printf("Name: ");
        gets(s[i].name);  // Using gets for simplicity
        printf("Roll Number: ");
        scanf("%d", &s[i].roll_no);
        printf("Marks: ");
        scanf("%f", &s[i].marks);
        getchar();  // Consume newline character
    }
    
    // Display details
    printf("\n=== Student Details ===\n");
    for (i = 0; i < 3; i++) {
        printf("\nStudent %d:\n", i + 1);
        printf("Name: %s\n", s[i].name);
        printf("Roll Number: %d\n", s[i].roll_no);
        printf("Marks: %.2f\n", s[i].marks);
    }
    
    return 0;
}
```

**Output:**
```
Enter details for Student 1:
Name: Alice Sharma
Roll Number: 101
Marks: 92.5

Enter details for Student 2:
Name: Bob Singh
Roll Number: 102
Marks: 78.0

Enter details for Student 3:
Name: Carol Gupta
Roll Number: 103
Marks: 88.75

=== Student Details ===

Student 1:
Name: Alice Sharma
Roll Number: 101
Marks: 92.50

Student 2:
Name: Bob Singh
Roll Number: 102
Marks: 78.00

Student 3:
Name: Carol Gupta
Roll Number: 103
Marks: 88.75
```

### Example 2: Complex Number Addition

Write a program to add two complex numbers using structures.

```c
#include <stdio.h>

struct Complex {
    int real;
    int imaginary;
};

int main() {
    struct Complex c1, c2, sum;
    
    // Input first complex number
    printf("Enter first complex number (real imaginary): ");
    scanf("%d %d", &c1.real, &c1.imaginary);
    
    // Input second complex number
    printf("Enter second complex number (real imaginary): ");
    scanf("%d %d", &c2.real, &c2.imaginary);
    
    // Addition
    sum.real = c1.real + c2.real;
    sum.imaginary = c1.imaginary + c2.imaginary;
    
    // Display result
    printf("\nSum = %d + %di\n", sum.real, sum.imaginary);
    
    return 0;
}
```

**Sample Input:**
```
Enter first complex number (real imaginary): 5 3
Enter second complex number (real imaginary): 2 4
```

**Sample Output:**
```
Sum = 7 + 7i
```

### Example 3: Date Structure and Validation

Write a program to store a date and check if it is valid.

```c
#include <stdio.h>

struct Date {
    int day;
    int month;
    int year;
};

int checkValid(struct Date d) {
    if (d.year < 1 || d.year > 9999)
        return 0;
    if (d.month < 1 || d.month > 12)
        return 0;
    if (d.day < 1)
        return 0;
    
    // Days in each month
    int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    // Leap year check
    if (d.year % 400 == 0 || (d.year % 4 == 0 && d.year % 100 != 0))
        daysInMonth[2] = 29;
    
    if (d.day > daysInMonth[d.month])
        return 0;
    
    return 1;
}

int main() {
    struct Date d;
    
    printf("Enter date (day month year): ");
    scanf("%d %d %d", &d.day, &d.month, &d.year);
    
    if (checkValid(d))
        printf("Valid Date\n");
    else
        printf("Invalid Date\n");
    
    return 0;
}
```

## Exam Tips

1. **Structure vs Array**: Remember structures can hold different data types while arrays hold elements of the same type. This distinction is frequently tested in DU exams.

2. **Structure Padding**: Be prepared for questions on memory padding and structure size. The compiler adds padding bytes for alignment, so the size of a structure may be greater than the sum of its members.

3. **Access Operator**: Always use the dot (.) operator for accessing structure members through structure variables. For pointers to structures, use the arrow (->) operator (covered in Pointer and Structures topic).

4. **Initialization Methods**: Know both traditional initialization (`struct Student s = {"John", 101, 90.5}`) and designated initializers (`struct Student s = {.name = "John", .roll_no = 101}`).

5. **typedef Usage**: The `typedef` keyword is often used with structures to create shorter, more readable type names. This is a favorite exam topic.

6. **Difference between struct and union**: Understand that structures allocate separate memory for each member, while unions share the same memory location for all members (covered in Union topic).

7. **Passing Structures to Functions**: Structures can be passed to functions by value or by reference. For large structures, passing by reference (using pointers) is more efficient.

8. **Common Errors**: A common mistake is forgetting to declare a structure variable after defining the structure template. Both definition and declaration are necessary.

9. **Naming Conventions**: Structure tag names and variables are different. `struct Student` defines the type, while `s1` is a variable of that type.

10. **Real-world Applications**: Be ready to solve problems involving employee records, student databases, bank account information, and coordinate systems using structures.