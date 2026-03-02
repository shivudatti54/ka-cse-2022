# Pointers and Structures in C


## Table of Contents

- [Pointers and Structures in C](#pointers-and-structures-in-c)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Declaring Pointers to Structures](#declaring-pointers-to-structures)
  - [Accessing Structure Members Through Pointers](#accessing-structure-members-through-pointers)
  - [Passing Structures to Functions](#passing-structures-to-functions)
  - [Dynamic Memory Allocation for Structures](#dynamic-memory-allocation-for-structures)
  - [Arrays of Structures and Pointers](#arrays-of-structures-and-pointers)
  - [Self-Referential Structures](#self-referential-structures)
- [Examples](#examples)
  - [Example 1: Accessing Structure Members Using Pointers](#example-1-accessing-structure-members-using-pointers)
  - [Example 2: Passing Structure Pointer to Function](#example-2-passing-structure-pointer-to-function)
  - [Example 3: Dynamic Allocation of Structure and Linked List Node](#example-3-dynamic-allocation-of-structure-and-linked-list-node)
- [Exam Tips](#exam-tips)

## Introduction

Pointers and structures together form one of the most powerful combinations in C programming. While structures allow us to group related data of different types into a single unit, pointers provide the capability to manipulate these complex data types efficiently through memory addresses. This synergy is fundamental to implementing advanced data structures like linked lists, trees, and dynamic memory management systems.

In the context of the University of Delhi's Computer Science curriculum, understanding the relationship between pointers and structures is essential for several reasons. First, it enables efficient passing of large structure variables to functions without the overhead of copying the entire structure. Second, it forms the foundation for building dynamic data structures that can grow and shrink during program execution. Third, many system-level programming tasks in operating systems and embedded systems rely heavily on this concept. This topic builds directly on your understanding of both structures (introduced in earlier modules) and pointers, combining them to solve complex programming problems.

## Key Concepts

### Declaring Pointers to Structures

A pointer to a structure is declared by placing an asterisk (*) before the structure variable name. The general syntax involves first defining the structure, then declaring a pointer variable of that structure type. For example, if we have a structure named "Student" with members like name, roll number, and marks, we can declare a pointer to this structure as: `struct Student *ptr;`

It is important to note that the pointer must point to a valid memory location before it can be used. This means we must either assign it the address of an existing structure variable using the address-of operator (&), or allocate memory dynamically using functions like malloc() or calloc(). Attempting to dereference an uninitialized or NULL pointer leads to undefined behavior and typically causes program crashes.

### Accessing Structure Members Through Pointers

There are two primary methods for accessing structure members when working with pointers. The first method uses the dot operator (.) in combination with the dereference operator (*). Since the dot operator has higher precedence than the dereference operator, we must use parentheses: `(*ptr).memberName`. Without parentheses, the expression would be interpreted as `*(ptr.memberName)`, which is incorrect because you cannot apply the dot operator to a pointer.

The second and more elegant method uses the arrow operator (→), which was specifically introduced in C to simplify pointer-to-structure manipulation. The arrow operator combines dereferencing and member access into a single operation. The expression `ptr->memberName` is equivalent to `(*ptr).memberName` but is more readable and less prone to errors. The arrow operator should be read as "pointing to" the member, making the code more intuitive.

### Passing Structures to Functions

When passing structures to functions, we have three options: passing by value, passing by pointer, and passing by reference (using reference parameters in C++, but in C we simulate this with pointers). Passing by value creates a complete copy of the structure, which is memory-intensive and time-consuming for large structures. Additionally, any modifications made to the parameter inside the function do not affect the original structure.

Passing structures by pointer is the preferred approach in most scenarios, especially for large structures or when the function needs to modify the original data. When a pointer to a structure is passed, only the memory address (typically 4 bytes on 32-bit systems or 8 bytes on 64-bit systems) is passed, regardless of the structure's size. This approach is highly efficient and allows the function to directly modify the original structure's members. The arrow operator is typically used inside such functions to access and modify the structure members.

### Dynamic Memory Allocation for Structures

Dynamic allocation of structures is crucial for creating data structures that can grow and shrink during program execution. The sizeof operator is used to determine the amount of memory required for a structure, and malloc() or calloc() allocates the requested memory from the heap. The general pattern involves: first calculating the size using sizeof(struct StructureName), then allocating memory, checking for NULL to ensure allocation succeeded, and finally assigning the allocated address to a pointer variable.

When dynamically allocated structures are no longer needed, the free() function must be called to release the memory back to the system. Failure to do so results in memory leaks, where allocated memory becomes inaccessible but is not returned to the operating system. This is particularly problematic in long-running programs or embedded systems with limited memory.

### Arrays of Structures and Pointers

Arrays of structures are commonly used to store collections of related data, such as a database of employees or students. When working with arrays of structures, the array name itself acts as a pointer to the first element of the array. This means we can use pointer arithmetic to traverse the array efficiently. For example, if we have an array of Student structures, the expression `studentArray + i` gives the address of the i-th element, and `(studentArray + i)->rollNumber` accesses the roll number of the i-th student.

Understanding this relationship between array names and pointers is essential for writing efficient code that processes collections of structure data. It allows us to iterate through structures without copying them, using only pointer arithmetic and the arrow operator.

### Self-Referential Structures

Self-referential structures contain a pointer to a structure of the same type, making them ideal for building linked data structures like linked lists, trees, and graphs. A typical node in a singly linked list is defined with at least two members: a data field (which can be a simple type or another structure) and a pointer to the next node. The pointer field allows each node to "link" to the next node, forming a chain of connected elements.

This concept is fundamental to understanding dynamic data structures. The next pointer of the last node is set to NULL to indicate the end of the list. By manipulating these pointers, we can insert nodes at the beginning, end, or middle of a list; delete nodes; and traverse the entire list. Self-referential structures combined with dynamic memory allocation enable the creation of data structures of arbitrary size, limited only by available memory.

## Examples

### Example 1: Accessing Structure Members Using Pointers

Consider a program that manages employee data using a structure pointer:

```c
#include <stdio.h>
#include <string.h>

struct Employee {
    int emp_id;
    char name[50];
    float salary;
};

int main() {
    struct Employee emp;
    struct Employee *ptr;
    
    // Initialize the structure
    emp.emp_id = 1001;
    strcpy(emp.name, "Aisha Khan");
    emp.salary = 55000.50;
    
    // Point to the structure
    ptr = &emp;
    
    // Method 1: Using dot operator with dereference
    printf("Employee ID: %d\n", (*ptr).emp_id);
    printf("Name: %s\n", (*ptr).name);
    printf("Salary: %.2f\n", (*ptr).salary);
    
    // Method 2: Using arrow operator (preferred)
    printf("\nUsing Arrow Operator:\n");
    printf("Employee ID: %d\n", ptr->emp_id);
    printf("Name: %s\n", ptr->name);
    printf("Salary: %.2f\n", ptr->salary);
    
    return 0;
}
```

The output demonstrates that both methods produce identical results, but the arrow operator is more concise and readable. In this example, ptr points to emp, and both `(*ptr).emp_id` and `ptr->emp_id` access the same memory location containing the employee ID.

### Example 2: Passing Structure Pointer to Function

This example demonstrates modifying structure data through a function using a pointer:

```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

// Function to modify point coordinates using pointer
void translate(struct Point *p, int dx, int dy) {
    // Using arrow operator to access and modify members
    p->x = p->x + dx;
    p->y = p->y + dy;
}

// Function to display point coordinates
void display(struct Point *p) {
    printf("Point coordinates: (%d, %d)\n", p->x, p->y);
}

int main() {
    struct Point p1 = {10, 20};
    
    printf("Original: ");
    display(&p1);
    
    // Translate the point by (5, -3)
    translate(&p1, 5, -3);
    
    printf("After translation: ");
    display(&p1);
    
    return 0;
}
```

The output shows that the translate function successfully modifies the original structure:
- Original: Point coordinates: (10, 20)
- After translation: Point coordinates: (15, 17)

This demonstrates that passing the structure by pointer allows the function to modify the original data, unlike pass-by-value which would leave the original unchanged.

### Example 3: Dynamic Allocation of Structure and Linked List Node

This example shows how to dynamically allocate a structure and use it in a linked list context:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    int roll_no;
    char name[30];
    float marks;
    struct Student *next;  // Self-referential pointer
};

int main() {
    struct Student *head, *newNode, *temp;
    int n;
    
    printf("Enter number of students: ");
    scanf("%d", &n);
    
    head = NULL;
    
    for (int i = 0; i < n; i++) {
        // Dynamically allocate memory for new node
        newNode = (struct Student *)malloc(sizeof(struct Student));
        
        if (newNode == NULL) {
            printf("Memory allocation failed!\n");
            return 1;
        }
        
        printf("Enter details for student %d:\n", i + 1);
        printf("Roll No: ");
        scanf("%d", &newNode->roll_no);
        printf("Name: ");
        scanf("%s", newNode->name);
        printf("Marks: ");
        scanf("%f", &newNode->marks);
        
        newNode->next = NULL;
        
        // Insert at beginning of list
        newNode->next = head;
        head = newNode;
    }
    
    // Display the linked list
    printf("\nStudent List:\n");
    temp = head;
    while (temp != NULL) {
        printf("Roll No: %d, Name: %s, Marks: %.2f\n", 
               temp->roll_no, temp->name, temp->marks);
        temp = temp->next;
    }
    
    // Free allocated memory
    temp = head;
    while (temp != NULL) {
        struct Student *temp2 = temp;
        temp = temp->next;
        free(temp2);
    }
    
    return 0;
}
```

This comprehensive example demonstrates several key concepts: dynamic memory allocation for structures, self-referential structures for linked lists, the arrow operator for member access, and proper memory deallocation to prevent memory leaks. Each student node is dynamically created, linked to form a chain, and then all nodes are freed before program termination.

## Exam Tips

For your DU semester examinations, keep these important points in mind:

1. Remember that the arrow operator (→) has higher precedence than the dot operator (.), so `*ptr.member` is incorrect—you must use `(*ptr).member` or the preferred `ptr->member`.

2. When passing large structures to functions, always pass by pointer to avoid copying overhead and enable modification of the original data.

3. Always initialize pointers before use—uninitialized pointers contain garbage addresses and cause segmentation faults.

4. After malloc() or calloc(), always check for NULL to handle allocation failures gracefully.

5. For self-referential structures, the pointer within the structure must point to the same structure type, enabling chain-like data structures.

6. The structure pointer arithmetic works similarly to array pointers—adding 1 to a structure pointer moves it by sizeof(struct) bytes.

7. In function prototypes involving structure pointers, the struct keyword and name must be included: `void func(struct Employee *ptr);`

8. Don't forget to free() dynamically allocated memory to prevent memory leaks, especially in programs that run for extended periods.

9. Understand the difference between accessing members of a structure variable directly (emp.name) versus through a pointer (ptr->name or (*ptr).name).

10. When using typedef with structures, remember that the typedef name can be used to declare pointer types: `Emp *ptr;` is valid if Emp is a typedef for struct Employee.