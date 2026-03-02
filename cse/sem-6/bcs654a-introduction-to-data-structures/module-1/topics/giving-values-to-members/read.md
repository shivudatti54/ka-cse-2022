# Giving Values to Members

## Introduction

In the study of data structures, structures (also known as records) serve as fundamental composite data types that allow the grouping of heterogeneous data elements under a single name. After declaring a structure type and creating structure variables, the next essential skill is learning how to assign values to the individual members of these variables. This process, known as "giving values to members," is crucial for building and manipulating complex data structures in C programming.

Understanding the various methods of assigning values to structure members is essential because different scenarios call for different approaches. Whether you need to initialize a structure at the time of declaration, assign values during program execution, or accept input from users, each method has its appropriate use case. This knowledge forms the foundation for implementing more advanced data structures like linked lists, trees, and graphs where structure members frequently hold important data values.

## Key Concepts

### Methods of Assigning Values to Structure Members

There are several methods available in C for giving values to structure members:

**1. Assignment at the Time of Declaration (Initialization)**

Structure variables can be initialized at the time of declaration by enclosing the values in curly braces:

```c
struct Student {
 int rollno;
 char name[30];
 float marks;
};

// Initialization at declaration
struct Student s1 = {101, "John", 85.5};
```

The values are assigned to members in the order they were declared in the structure definition.

**2. Assignment Using the Dot Operator**

After a structure variable has been declared, individual members can be assigned values using the dot operator (`.`):

```c
struct Student s2;
s2.rollno = 102;
strcpy(s2.name, "Alice");
s2.marks = 92.5;
```

This method allows assigning values to some members while leaving others for later assignment.

**3. Using Input Functions**

Values can be assigned to structure members through user input using functions like `scanf()`:

```c
printf("Enter roll number: ");
scanf("%d", &s1.rollno);
printf("Enter name: ");
scanf("%s", s1.name);
printf("Enter marks: ");
scanf("%f", &s1.marks);
```

**4. Copy Assignment Between Structures**

An entire structure can be assigned to another structure of the same type using the assignment operator:

```c
struct Student s3 = {103, "Bob", 78.0};
struct Student s4;
s4 = s3; // Copies all members from s3 to s4
```

**5. Using Pointers to Access Members**

When working with structure pointers, members can be accessed using the arrow operator (`->`):

```c
struct Student *ptr = &s1;
ptr->rollno = 105;
strcpy(ptr->name, "David");
```

### Important Rules

- Members are accessed using the dot operator (`.`) for regular variables and arrow operator (`->`) for pointers
- String members require using `strcpy()` or `scanf()` for assignment
- Individual members can be assigned independently without affecting other members
- Structure assignment copies all member values (shallow copy for pointers)

## Examples

### Example 1: Employee Record Management

```c
#include <stdio.h>
#include <string.h>

struct Employee {
 int emp_id;
 char name[50];
 float salary;
 char department[30];
};

int main() {
 struct Employee emp1, emp2;

 // Method 1: Initialization at declaration
 struct Employee emp3 = {1001, "Raj Kumar", 55000.00, "Engineering"};

 // Method 2: Using dot operator
 emp1.emp_id = 1002;
 strcpy(emp1.name, "Priya Singh");
 emp1.salary = 48000.00;
 strcpy(emp1.department, "Marketing");

 // Method 3: Using scanf for input
 printf("Enter employee ID: ");
 scanf("%d", &emp2.emp_id);
 printf("Enter name: ");
 scanf("%s", emp2.name);
 printf("Enter salary: ");
 scanf("%f", &emp2.salary);
 printf("Enter department: ");
 scanf("%s", emp2.department);

 // Display all employees
 printf("\nEmployee 1: %d, %s, %.2f, %s\n",
 emp1.emp_id, emp1.name, emp1.salary, emp1.department);
 printf("Employee 2: %d, %s, %.2f, %s\n",
 emp2.emp_id, emp2.name, emp2.salary, emp2.department);
 printf("Employee 3: %d, %s, %.2f, %s\n",
 emp3.emp_id, emp3.name, emp3.salary, emp3.department);

 return 0;
}
```

### Example 2: Complex Number Representation

```c
#include <stdio.h>

struct Complex {
 float real;
 float imaginary;
};

int main() {
 struct Complex c1, c2, sum;

 // Initialize first complex number
 c1.real = 3.5;
 c1.imaginary = 2.5;

 // Initialize second complex number using braces
 c2 = {5.5, 4.5}; // Assignment using compound literal style

 // Calculate sum of complex numbers
 sum.real = c1.real + c2.real;
 sum.imaginary = c1.imaginary + c2.imaginary;

 printf("First complex number: %.1f + %.1fi\n", c1.real, c1.imaginary);
 printf("Second complex number: %.1f + %.1fi\n", c2.real, c2.imaginary);
 printf("Sum: %.1f + %.1fi\n", sum.real, sum.imaginary);

 return 0;
}
```

### Example 3: Using Pointers with Structures

```c
#include <stdio.h>
#include <string.h>

struct Book {
 int book_id;
 char title[50];
 char author[30];
 float price;
};

void displayBook(struct Book *b) {
 printf("Book ID: %d\n", b->book_id);
 printf("Title: %s\n", b->title);
 printf("Author: %s\n", b->author);
 printf("Price: %.2f\n", b->price);
}

int main() {
 struct Book b1;
 struct Book *ptr = &b1;

 // Using arrow operator through pointer
 ptr->book_id = 201;
 strcpy(ptr->title, "Data Structures");
 strcpy(ptr->author, "Cormen");
 ptr->price = 450.00;

 displayBook(ptr);

 return 0;
}
```

## Exam Tips

1. **Remember the syntax**: Use dot (`.`) for structure variables and arrow (`->`) for structure pointers when accessing members.

2. **String assignment**: Never use assignment operator (`=`) for character arrays. Use `strcpy()` function instead.

3. **Initialization order**: When initializing structures at declaration, values are assigned in the order of member declarations in the structure definition.

4. **Partial initialization**: If fewer values are provided during initialization, remaining members are automatically initialized to zero.

5. **Structure assignment**: You can copy entire structures of the same type using the assignment operator, but this performs a shallow copy.

6. **Address operator**: When using `scanf()` with structure members, remember to use the address-of operator (`&`) for non-array members.

7. **Memory consideration**: Array members within structures (like `char name[50]`) do not require `&` when used with `scanf()` since the array name already represents the base address.
