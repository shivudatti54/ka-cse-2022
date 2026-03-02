# Arrays and Nested Structures

## Introduction to Arrays and Structures

Arrays and structures are fundamental data structures in the C programming language that allow for organized data storage and manipulation. While arrays provide a way to store multiple elements of the same data type, structures enable the grouping of different data types under a single name. When these concepts are combined, they form powerful tools for representing complex real-world data.

**Arrays** are collections of elements of the same type, stored in contiguous memory locations. They provide indexed access to their elements, making them efficient for storing and processing homogeneous data.

**Structures** (or structs) are user-defined data types that allow grouping variables of different types under a single name. Each variable in a structure is called a member, and they can be accessed using the dot (.) operator.

## One-Dimensional Arrays

A one-dimensional array is the simplest form of array, consisting of a single row of elements.

### Declaration and Initialization

```c
// Declaration
int numbers[5]; // Array of 5 integers

// Initialization at declaration
int numbers[5] = {1, 2, 3, 4, 5};

// Partial initialization (remaining elements set to 0)
int numbers[5] = {1, 2}; // [1, 2, 0, 0, 0]

// Size determined by initializer
int numbers[] = {1, 2, 3, 4, 5}; // Size is 5
```

### Accessing Elements

```c
numbers[0] = 10;    // First element
numbers[4] = 50;    // Last element (for size 5)
int value = numbers[2]; // Access third element
```

## Two-Dimensional Arrays

Two-dimensional arrays represent tabular data with rows and columns, essentially creating an array of arrays.

### Declaration and Initialization

```c
// Declaration
int matrix[3][4]; // 3 rows, 4 columns

// Initialization
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Row-major initialization
int matrix[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
```

### Memory Representation

A two-dimensional array is stored in row-major order in memory:

```
Row 0: [1, 2, 3, 4]
Row 1: [5, 6, 7, 8]
Row 2: [9, 10, 11, 12]
```

Memory layout: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`

### Accessing Elements

```c
matrix[0][0] = 10;  // First row, first column
matrix[2][3] = 100; // Last row, last column
int value = matrix[1][2]; // Second row, third column
```

## Multidimensional Arrays

Arrays can have more than two dimensions, though they become increasingly complex to manage.

```c
// 3D array declaration
int cube[2][3][4]; // 2 layers, 3 rows, 4 columns

// Initialization
int cube[2][3][4] = {
    { // Layer 0
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    },
    { // Layer 1
        {13, 14, 15, 16},
        {17, 18, 19, 20},
        {21, 22, 23, 24}
    }
};
```

## Structures

### Basic Structure Declaration and Usage

```c
// Structure declaration
struct Student {
    int rollNo;
    char name[50];
    float marks;
};

// Creating structure variables
struct Student s1;
struct Student s2 = {101, "John Doe", 85.5};

// Accessing members
s1.rollNo = 100;
strcpy(s1.name, "Jane Smith");
s1.marks = 90.0;
```

### Structure Initialization

```c
// Method 1: Declaration with initialization
struct Point {
    int x;
    int y;
} p1 = {10, 20};

// Method 2: Designated initializers (C99)
struct Point p2 = {.x = 5, .y = 15};
```

### Comparison of Structure Variables

Structures cannot be compared directly using relational operators. You must compare individual members:

```c
int areEqual(struct Student s1, struct Student s2) {
    return (s1.rollNo == s2.rollNo &&
            strcmp(s1.name, s2.name) == 0 &&
            s1.marks == s2.marks);
}
```

## Arrays of Structures

Creating arrays where each element is a structure:

```c
struct Student class[50]; // Array of 50 students

// Initializing array of structures
struct Student class[3] = {
    {101, "Alice", 88.5},
    {102, "Bob", 92.0},
    {103, "Charlie", 76.5}
};

// Accessing elements
class[0].rollNo = 100;
strcpy(class[1].name, "Robert");
```

## Arrays within Structures

Structures can contain arrays as members:

```c
struct Employee {
    int id;
    char name[50];
    float salaryHistory[12]; // Array within structure
    char skills[5][20];      // 2D array within structure
};

// Usage
struct Employee emp;
emp.id = 1001;
strcpy(emp.name, "Sarah Johnson");
emp.salaryHistory[0] = 50000.0;
strcpy(emp.skills[0], "Programming");
```

## Nested Structures

Structures can contain other structures as members, creating nested or hierarchical data structures.

### Simple Nested Structure

```c
struct Address {
    char street[50];
    char city[30];
    char state[20];
    int zipCode;
};

struct Person {
    char name[50];
    int age;
    struct Address addr; // Nested structure
};

// Initialization
struct Person p1 = {
    "John Doe",
    30,
    {"123 Main St", "Springfield", "IL", 62701}
};

// Accessing nested members
printf("City: %s\n", p1.addr.city);
p1.addr.zipCode = 62702;
```

### Complex Nesting with Arrays

```c
struct Date {
    int day;
    int month;
    int year;
};

struct Course {
    char code[10];
    char name[50];
    int credits;
};

struct Student {
    int id;
    char name[50];
    struct Date dob;          // Nested structure
    struct Course courses[5]; // Array of nested structures
    struct Address address;   // Another nested structure
};

// Initialization
struct Student student = {
    1001,
    "Emily Chen",
    {15, 8, 2000},
    {
        {"CS101", "Programming", 4},
        {"MATH201", "Calculus", 3}
    },
    {"456 Oak Ave", "Chicago", "IL", 60601}
};
```

### Accessing Deeply Nested Members

```c
// Accessing course name
printf("First course: %s\n", student.courses[0].name);

// Accessing birth year
printf("Birth year: %d\n", student.dob.year);

// Modifying nested members
student.address.zipCode = 60602;
strcpy(student.courses[1].name, "Advanced Calculus");
```

## Memory Layout of Nested Structures

The memory for nested structures is allocated contiguously, with the inner structures placed within the outer structure's memory block.

```
struct Person memory layout:
+-----------------------+
| name[50]             |
+-----------------------+
| age (4 bytes)         |
+-----------------------+
| addr.street[50]       |
+-----------------------+
| addr.city[30]         |
+-----------------------+
| addr.state[20]        |
+-----------------------+
| addr.zipCode (4 bytes)|
+-----------------------+
```

## Operations on Nested Structures

### Passing to Functions

```c
void printPerson(struct Person p) {
    printf("Name: %s\n", p.name);
    printf("Address: %s, %s, %s %d\n",
           p.addr.street, p.addr.city,
           p.addr.state, p.addr.zipCode);
}

// Passing by reference
void updateZipCode(struct Person *p, int newZip) {
    p->addr.zipCode = newZip;
}
```

### Returning from Functions

```c
struct Person createPerson(char *name, int age, char *street,
                          char *city, char *state, int zip) {
    struct Person newPerson;
    strcpy(newPerson.name, name);
    newPerson.age = age;
    strcpy(newPerson.addr.street, street);
    strcpy(newPerson.addr.city, city);
    strcpy(newPerson.addr.state, state);
    newPerson.addr.zipCode = zip;
    return newPerson;
}
```

## Practical Example: Student Database

```c
#include <stdio.h>
#include <string.h>

struct Date {
    int day, month, year;
};

struct Course {
    char code[10];
    char name[50];
    float grade;
};

struct Student {
    int id;
    char name[50];
    struct Date dob;
    struct Course courses[3];
    float gpa;
};

void calculateGPA(struct Student *s) {
    float total = 0;
    for(int i = 0; i < 3; i++) {
        total += s->courses[i].grade;
    }
    s->gpa = total / 3;
}

void printStudent(struct Student s) {
    printf("ID: %d\n", s.id);
    printf("Name: %s\n", s.name);
    printf("DOB: %d/%d/%d\n", s.dob.day, s.dob.month, s.dob.year);
    printf("Courses:\n");
    for(int i = 0; i < 3; i++) {
        printf("  %s: %s (Grade: %.2f)\n",
               s.courses[i].code, s.courses[i].name, s.courses[i].grade);
    }
    printf("GPA: %.2f\n", s.gpa);
}

int main() {
    struct Student s1 = {
        1001,
        "Alice Johnson",
        {12, 5, 2001},
        {
            {"CS101", "Programming", 88.5},
            {"MATH201", "Calculus", 92.0},
            {"PHYS101", "Physics", 85.0}
        },
        0.0 // GPA will be calculated
    };

    calculateGPA(&s1);
    printStudent(s1);

    return 0;
}
```

## Unions vs Structures

While structures allocate memory for all members, unions share memory between members.

| Aspect            | Structure                       | Union                                |
| ----------------- | ------------------------------- | ------------------------------------ |
| Memory Allocation | All members get separate memory | All members share same memory        |
| Total Size        | Sum of all members + padding    | Size of largest member               |
| Member Access     | All members accessible at once  | Only one member accessible at a time |
| Use Case          | Group related data              | Store different types in same memory |

```c
union Data {
    int i;
    float f;
    char str[20];
};

union Data data;
data.i = 10;        // Now stores integer
printf("%d\n", data.i);

data.f = 220.5;     // Now stores float, overwrites integer
printf("%f\n", data.f);
```

## Size of Structures

The size of a structure is affected by padding and alignment requirements. Use `sizeof` operator to get actual size.

```c
struct Example {
    char c;     // 1 byte
    int i;      // 4 bytes
    double d;   // 8 bytes
};

printf("Size: %zu bytes\n", sizeof(struct Example));
// Might print 24 bytes due to padding, not 13
```

## Exam Tips

1. **Memory Layout**: Understand how nested structures are stored in memory and how padding affects their size.

2. **Access Patterns**: Practice accessing deeply nested members using the dot operator and arrow operator for pointers.

3. **Initialization**: Master different ways to initialize nested structures, including designated initializers.

4. **Arrays vs Structures**: Remember that arrays contain same-type elements, while structures can contain different types.

5. **Union Distinction**: Clearly differentiate between unions and structures, especially regarding memory usage.

6. **Pointer Usage**: Practice using pointers with nested structures for efficient parameter passing.

7. **Real-world Modeling**: Think about how nested structures can model real-world entities like students, employees, or products with multiple attributes.

8. **Error Prevention**: Be cautious about array bounds within structures and proper string handling with strcpy().
