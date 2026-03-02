# Array of Structures


## Table of Contents

- [Array of Structures](#array-of-structures)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Defining an Array of Structures](#defining-an-array-of-structures)
  - [Memory Layout and Size Calculation](#memory-layout-and-size-calculation)
  - [Initialization of Array of Structures](#initialization-of-array-of-structures)
  - [Accessing Members of Array Elements](#accessing-members-of-array-elements)
  - [Passing Array of Structures to Functions](#passing-array-of-structures-to-functions)
  - [Operations on Array of Structures](#operations-on-array-of-structures)
- [Examples](#examples)
  - [Example 1: Student Record Management System](#example-1-student-record-management-system)
  - [Example 2: Sorting Array of Structures](#example-2-sorting-array-of-structures)
  - [Example 3: Search and Update Operation](#example-3-search-and-update-operation)
- [Exam Tips](#exam-tips)

## Introduction

Array of Structures is one of the most powerful data organization techniques in C programming that combines the power of arrays with the flexibility of structures. When you need to store and manage multiple records of heterogeneous data—such as student information, employee details, or inventory items—array of structures provides an elegant and efficient solution. This topic builds directly upon your understanding of basic structures and introduces a new dimension of data management that is essential for solving real-world computational problems.

In the context of problem solving using C programming, array of structures becomes indispensable when dealing with database-like operations. Consider a scenario where you need to maintain records for 1000 students in a university system. Each student record contains multiple fields: roll number (integer), name (string), marks in five subjects (array of floats), and grade (character). Managing such data using primitive data types alone would be chaotic and error-prone. Array of structures allows you to define a unified structure template and then create an array of instances, each representing one student's complete record.

The importance of this topic extends beyond academic requirements. In practical software development, particularly in systems programming, database management, and file handling, array of structures forms the backbone of data manipulation. Understanding this concept thoroughly will prepare you for advanced topics like linked lists, data structures, and database systems. For the University of Delhi examination, questions on array of structures frequently appear, testing your ability to manipulate complex data and implement search, sort, and update operations on collections of records.

## Key Concepts

### Defining an Array of Structures

An array of structures is declared by combining the structure definition with array notation. The syntax follows a two-step process: first define the structure template using the struct keyword, then declare an array of that structure type. For example, to create an array capable of holding information for 50 students, you would write:

```c
struct Student {
    int rollno;
    char name[30];
    float marks[5];
    char grade;
};

struct Student class[50];
```

This declaration creates an array named "class" containing 50 elements, where each element is a complete Student structure. The memory allocation follows a contiguous layout—each Student structure occupies a fixed number of bytes, and these structures are arranged sequentially in memory. This contiguity provides excellent cache performance and allows efficient sequential access.

### Memory Layout and Size Calculation

Understanding the memory layout of an array of structures is crucial for effective programming and debugging. The total memory required can be calculated using the formula: sizeof(struct Student) multiplied by the number of elements. However, due to structure padding—a compiler optimization technique—the actual size might differ from the simple sum of individual member sizes. The compiler aligns structure members to specific memory addresses (typically 2, 4, or 8-byte boundaries) for performance, which may introduce padding bytes between members.

Consider a structure with the following members: int age (4 bytes), char grade (1 byte), and double salary (8 bytes). Without padding, you might expect 13 bytes, but the compiler will typically align double to an 8-byte boundary, resulting in padding after age and possibly after grade, making the structure size 24 bytes instead. This understanding becomes critical when working with file I/O operations and when calculating offsets for direct memory access.

### Initialization of Array of Structures

Array of structures can be initialized at the time of declaration using curly braces, similar to regular array initialization. There are multiple approaches: initializing all elements, initializing only some elements (remaining get zero-initialized), and using designated initializers in C99. The initialization syntax requires nested braces, with each inner brace representing one structure element:

```c
struct Book library[3] = {
    {101, "Data Structures", "Kal", 450.00},
    {102, "Operating Systems", "Galvin", 620.50},
    {103, "Computer Networks", "Tanenbaum", 580.00}
};
```

This method provides a clean way to populate initial data, particularly useful for small arrays and testing purposes. For larger arrays, initialization is typically done through user input using scanf or by reading from files.

### Accessing Members of Array Elements

Accessing individual members within an array of structures requires a two-level access mechanism: first specify the array index, then use the member access operator (dot operator) to reach the specific member. The syntax follows the pattern: array_name[index].member_name. For instance, to access the name of the third student in the class array, you would write class[2].name. The index in C arrays starts from 0, so the third element is accessed using index 2.

This nested access pattern extends naturally to multi-dimensional scenarios. If a structure contains an array as a member (such as marks[5]), you can access individual marks using notation like class[2].marks[3], representing the fourth mark of the third student. This hierarchical access is one of the most powerful features of structures combined with arrays.

### Passing Array of Structures to Functions

When passing an array of structures to functions, you have several options, each with different implications for performance and data modification. The most common approaches include passing as a pointer to the structure, passing as a sized array, and passing using variable-length array notation. Understanding these approaches is essential for writing efficient functions that manipulate large collections of records.

Passing as a pointer is the most memory-efficient method because it avoids copying the entire array:

```c
void displayAll(struct Student *ptr, int n) {
    for (int i = 0; i < n; i++) {
        printf("Roll No: %d\n", (ptr + i)->rollno);
        printf("Name: %s\n", (ptr + i)->name);
    }
}
```

The function receives a pointer to the first structure, and pointer arithmetic allows accessing subsequent elements. The arrow operator (->) combines dereferencing with member access, making the code more readable when working with pointers to structures.

### Operations on Array of Structures

The real power of array of structures becomes evident when performing bulk operations. Common operations include searching for specific records based on certain criteria, sorting records according to various fields, updating records, and deleting records. These operations form the foundation of any record-keeping system.

Linear search through an array of structures involves iterating through each element and checking the target condition. For a class of n students, finding a student by roll number requires comparing the rollno field of each element until a match is found. The time complexity is O(n) in the worst case, which is acceptable for small to medium-sized arrays but becomes inefficient for very large datasets.

Sorting array of structures typically uses the standard sorting algorithms (bubble sort, selection sort, quick sort) with appropriate comparison functions. The comparison must consider the structure's fields, and the swap operation must exchange entire structure instances. Using pointers to structures can significantly improve sorting performance by reducing the amount of data copied during swaps.

## Examples

### Example 1: Student Record Management System

Write a program to accept records for n students and display all records where marks are greater than 75.

Solution:

```c
#include <stdio.h>
#include <string.h>

struct Student {
    int rollno;
    char name[30];
    float marks;
};

int main() {
    int n;
    printf("Enter number of students: ");
    scanf("%d", &n);
    
    struct Student class[n];
    
    // Accepting records
    for (int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Roll Number: ");
        scanf("%d", &class[i].rollno);
        printf("Name: ");
        scanf("%s", class[i].name);
        printf("Marks: ");
        scanf("%f", &class[i].marks);
    }
    
    // Displaying records with marks > 75
    printf("\nStudents scoring above 75 marks:\n");
    printf("----------------------------------------\n");
    
    for (int i = 0; i < n; i++) {
        if (class[i].marks > 75) {
            printf("Roll No: %d\n", class[i].rollno);
            printf("Name: %s\n", class[i].name);
            printf("Marks: %.2f\n", class[i].marks);
            printf("----------------------------------------\n");
        }
    }
    
    return 0;
}
```

This example demonstrates the fundamental operations: structure definition, array declaration with runtime size, data input using scanf, and conditional filtering during output. The key point to note is how the structure variable class[i] is used with the dot operator to access individual members.

### Example 2: Sorting Array of Structures

Write a program to sort an array of employee structures based on salary in descending order using bubble sort.

Solution:

```c
#include <stdio.h>
#include <string.h>

struct Employee {
    int empid;
    char name[30];
    float salary;
};

int main() {
    int n = 5;
    struct Employee emp[5] = {
        {101, "Rahul", 45000.00},
        {102, "Priya", 52000.00},
        {103, "Amit", 38000.00},
        {104, "Sneha", 61000.00},
        {105, "Vikram", 42000.00}
    };
    
    // Bubble Sort
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (emp[j].salary < emp[j + 1].salary) {
                // Swap entire structures
                struct Employee temp = emp[j];
                emp[j] = emp[j + 1];
                emp[j + 1] = temp;
            }
        }
    }
    
    // Display sorted records
    printf("Employees sorted by salary (descending):\n");
    printf("ID\tName\t\tSalary\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%s\t\t%.2f\n", emp[i].empid, emp[i].name, emp[i].salary);
    }
    
    return 0;
}
```

This example illustrates an important concept: structure assignment in C allows direct copying of entire structures using the assignment operator. The statements `struct Employee temp = emp[j];` and subsequent assignments successfully copy all members at once. The output will show employees sorted from highest to lowest salary, with Sneha (61000) appearing first and Amit (38000) appearing last.

### Example 3: Search and Update Operation

Write a program to search for a book by ISBN and update its price.

Solution:

```c
#include <stdio.h>
#include <string.h>

struct Book {
    int isbn;
    char title[40];
    char author[30];
    float price;
};

void searchAndUpdate(struct Book *ptr, int n, int searchIsbn) {
    int found = 0;
    
    for (int i = 0; i < n; i++) {
        if ((ptr + i)->isbn == searchIsbn) {
            printf("Book found!\n");
            printf("Title: %s\n", (ptr + i)->title);
            printf("Author: %s\n", (ptr + i)->author);
            printf("Current Price: %.2f\n", (ptr + i)->price);
            
            printf("Enter new price: ");
            scanf("%f", &(ptr + i)->price);
            
            printf("Price updated successfully!\n");
            found = 1;
            break;
        }
    }
    
    if (!found) {
        printf("Book with ISBN %d not found.\n", searchIsbn);
    }
}

int main() {
    struct Book library[3] = {
        {1001, "C Programming", "Dennis Ritchie", 350.00},
        {1002, "Data Structures", "Cormen", 650.00},
        {1003, "Algorithm Design", "Kleinberg", 720.00}
    };
    
    int isbn;
    printf("Enter ISBN to search: ");
    scanf("%d", &isbn);
    
    searchAndUpdate(library, 3, isbn);
    
    return 0;
}
```

This example demonstrates passing array of structures to functions using pointer notation, the arrow operator for member access through pointers, and the ability to modify original data through pointers. The function receives the base address of the array and uses pointer arithmetic to traverse and modify elements. Note how the address-of operator is used with (ptr + i)->price to store the scanned new price in the original structure.

## Exam Tips

For the University of Delhi semester examinations, the following points will help you score higher on array of structures questions:

MEMORY CALCULATIONS ARE FREQUENTLY ASKED: Questions requiring you to calculate the total memory occupied by an array of structures appear regularly. Remember to consider structure padding and alignment. If a structure contains int (4 bytes), char (1 byte), and double (8 bytes), calculate the padded size first, then multiply by array size.

POINTER ARITHMETIC WITH STRUCTURES: Understand that when you add 1 to a structure pointer, it moves by the size of the entire structure, not individual members. The expression (ptr + i) is equivalent to &ptr[i], and accessing members can be done as (ptr + i)->member or ptr[i].member.

DRAW MEMORY DIAGRAMS: For questions involving array initialization and access, drawing a simple memory diagram showing array indices and member offsets helps avoid errors. This is particularly useful for debugging your code during the exam.

STRUCTURE ASSIGNMENT ALLOWS DIRECT COPYING: Unlike arrays, structures can be assigned using the = operator, which copies all members. This is a key difference that makes sorting operations simpler—swap entire structure variables rather than individual members.

VARIABLE LENGTH ARRAY (VLA) IS SUPPORTED IN C99: You can declare arrays with runtime-determined sizes like struct Student class[n]; where n is read from user. However, some compilers may not fully support VLAs, so know the alternative of using dynamic memory allocation with malloc for portable code.

SEARCH AND SORT ALGORITHMS EXTEND NATURALLY: The logic for linear search, binary search, bubble sort, and selection sort remains the same when applied to arrays of structures—you only need to modify the comparison condition to compare specific structure members.

MEMBER ACCESS OPERATORS HAVE PRECEDENCE: The dot (.) operator has higher precedence than the arrow (->) operator. When accessing members through pointers, always use parentheses appropriately: (*ptr).member is equivalent to ptr->member, but the latter is preferred for readability.

PRACTICE WRITING COMPLETE PROGRAMS: Most exam questions require you to write complete, compilable programs. Practice declaring structures, creating arrays, writing input/output functions, and implementing search/sort operations. Pay attention to including proper header files and return statements.