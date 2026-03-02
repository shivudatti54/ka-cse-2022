# Structure Declaration in C

## 1. Introduction

A structure is a composite data type that groups together variables (called members or fields) of different data types under a single name. While arrays store collections of similar elements, structures are ideal for representing records with heterogeneous data. For example, a student record might contain a name (character array), age (integer), GPA (float), and student ID (string or integer).

The fundamental distinction between structures and arrays lies in data type homogeneity: arrays require all elements to be of the same type, whereas structures can combine variables of different types. This capability makes structures essential for modeling real-world entities with multiple attributes.

## 2. Syntax of Structure Declaration

The general syntax for declaring a structure in C is:

```c
struct structure_tag {
 data_type member1;
 data_type member2;
 // ... additional members
};
```

The `struct` keyword initiates the structure definition. The `structure_tag` (also called the tag) serves as a unique identifier for the structure type. Within the curly braces, each member is declared with its respective data type, followed by a mandatory semicolon after the closing brace.

**Example: Declaring a Book structure**

```c
struct Book {
 char title[100];
 char author[50];
 int publicationYear;
 float price;
};
```

## 3. Declaring Structure Variables

There are three primary methods for declaring structure variables:

### 3.1 Simultaneous Declaration

```c
struct Book {
 char title[100];
 char author[50];
 int publicationYear;
 float price;
} book1, book2;
```

### 3.2 Separate Declaration

```c
struct Book {
 char title[100];
 char author[50];
 int publicationYear;
 float price;
};

struct Book book1, book2;
```

### 3.3 Using typedef

The `typedef` keyword creates an alias, eliminating the need for the `struct` keyword:

```c
typedef struct {
 char title[100];
 char author[50];
 int publicationYear;
 float price;
} Book;

Book book1, book2;
```

## 4. Accessing Structure Members

Structure members are accessed using the dot operator (`.`) for variables and the arrow operator (`->`) for pointers:

```c
// Writing to members
book1.publicationYear = 2023;
strcpy(book1.title, "Introduction to Algorithms");
book1.price = 89.99;

// Reading from members
printf("Title: %s\n", book1.title);
printf("Price: %.2f\n", book1.price);
```

## 5. Initialization

Structures can be initialized at declaration using initializer lists:

```c
struct Book book1 = {"Data Structures", "Cormen", 2022, 75.50};

// C99 designated initializers
struct Book book2 = {.title = "Algorithms", .price = 60.00};
```

## 6. Self-Referential Structures

Self-referential structures contain a pointer to the same structure type—a fundamental concept for linked data structures:

```c
struct Node {
 int data;
 struct Node *next;
};
```

**Important**: The member must be a pointer, not a direct instance, to prevent infinite recursion.

## 7. Nested Structures

Structures can contain other structures as members:

```c
struct Date {
 int day;
 int month;
 int year;
};

struct Student {
 char name[50];
 int rollNumber;
 struct Date birthDate;
 struct Date admissionDate;
};
```

Accessing nested members requires multiple dot operators:

```c
student1.birthDate.day = 15;
```

## 8. Memory Considerations

The structure declaration creates a template; memory allocates only when variables are instantiated. The compiler may insert padding for alignment, so the structure size isn't simply the sum of member sizes:

```c
printf("Size of Book: %zu\n", sizeof(struct Book));
```

## 9. Key Characteristics Summary

- Structure declaration creates a blueprint; no memory is allocated until variables are instantiated
- Multiple variables can be declared from a single structure definition
- Anonymous structures (without tags) are possible when using `typedef`
- Self-referential structures require pointer members to the same type
- Member access uses `.` for variables and `->` for pointers
- Nested structures enable hierarchical data modeling
- The semicolon after the closing brace is mandatory

These mechanisms provide the foundation for implementing complex data structures and representing real-world entities in C programming.
