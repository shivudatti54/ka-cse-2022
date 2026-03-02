# Structure Initialization in C

## Introduction to Structures

A **structure** in C is a user-defined data type that allows you to combine data items of different types. Structures are used to represent a record and are particularly useful in Data Structures for creating complex data types like nodes in linked lists, trees, and graphs.

**Syntax:**

```c
struct structure_name {
 data_type member1;
 data_type member2;
 // ... more members
};
```

## Declaring and Initializing Structures

### Method 1: Declaration and Initialization Separately

```c
struct Student {
 int roll_no;
 char name[50];
 float marks;
};

int main() {
 struct Student s1; // Declaration

 // Initialization
 s1.roll_no = 101;
 strcpy(s1.name, "John Doe");
 s1.marks = 85.5;
}
```

### Method 2: Initialization at Declaration

```c
struct Student {
 int roll_no;
 char name[50];
 float marks;
};

int main() {
 struct Student s1 = {101, "John Doe", 85.5};
}
```

### Method 3: Designated Initializers (C99 onwards)

```c
struct Student s1 = {
 .roll_no = 101,
 .name = "John Doe",
 .marks = 85.5
};
```

### Method 4: Partial Initialization

```c
struct Student s1 = {101}; // Only roll_no is initialized, others are set to 0
```

### Method 5: Using typedef

```c
typedef struct {
 int roll_no;
 char name[50];
 float marks;
} Student;

int main() {
 Student s1 = {101, "John Doe", 85.5}; // No need for 'struct' keyword
}
```

## Initialization Methods in Detail

### 1. Zero Initialization

```c
struct Student s1 = {0}; // All members are initialized to 0
```

This sets:

- Numeric members to 0
- Character arrays to empty string
- Pointers to NULL

### 2. Member-wise Initialization

```c
struct Point {
 int x;
 int y;
};

struct Point p1 = {10, 20}; // x=10, y=20
struct Point p2 = {10}; // x=10, y=0
struct Point p3 = {.y = 20}; // x=0, y=20
```

### 3. Array of Structures Initialization

```c
struct Student students[3] = {
 {101, "Alice", 85.5},
 {102, "Bob", 78.3},
 {103, "Charlie", 92.1}
};
```

### 4. Nested Structure Initialization

```c
struct Date {
 int day;
 int month;
 int year;
};

struct Employee {
 int emp_id;
 char name[50];
 struct Date join_date;
};

struct Employee emp1 = {
 1001,
 "John Smith",
 {15, 6, 2020} // Nested initialization
};

// Or using designated initializers
struct Employee emp2 = {
 .emp_id = 1002,
 .name = "Jane Doe",
 .join_date = {.day = 20, .month = 8, .year = 2021}
};
```

## Structure Initialization in Data Structures

### Linked List Node Initialization

```c
struct Node {
 int data;
 struct Node* next;
};

// Method 1: Step by step
struct Node* createNode(int value) {
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 newNode->data = value;
 newNode->next = NULL;
 return newNode;
}

// Method 2: Compound literal (C99)
struct Node* head = &(struct Node){10, NULL};
```

### Tree Node Initialization

```c
struct TreeNode {
 int data;
 struct TreeNode* left;
 struct TreeNode* right;
};

struct TreeNode* createTreeNode(int value) {
 struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 node->data = value;
 node->left = NULL;
 node->right = NULL;
 return node;
}

// Usage
struct TreeNode* root = createTreeNode(50);
```

### Graph Node Initialization

```c
struct GraphNode {
 int vertex;
 struct GraphNode* next;
};

struct Graph {
 int numVertices;
 struct GraphNode** adjLists;
};

struct Graph* createGraph(int vertices) {
 struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
 graph->numVertices = vertices;
 graph->adjLists = (struct GraphNode**)malloc(vertices * sizeof(struct GraphNode*));

 for (int i = 0; i < vertices; i++) {
 graph->adjLists[i] = NULL;
 }

 return graph;
}
```

## Common Initialization Patterns

### Pattern 1: Self-Referential Structure (for Linked Lists)

```c
struct Node {
 int data;
 struct Node* next; // Pointer to same type
};

struct Node n1 = {10, NULL};
struct Node n2 = {20, &n1}; // n2 points to n1
```

### Pattern 2: Structure with Function Pointers

```c
struct Stack {
 int items[100];
 int top;
 void (*push)(struct Stack*, int);
 int (*pop)(struct Stack*);
};

void pushFunc(struct Stack* s, int value) {
 s->items[++(s->top)] = value;
}

int popFunc(struct Stack* s) {
 return s->items[(s->top)--];
}

struct Stack myStack = {
 .top = -1,
 .push = pushFunc,
 .pop = popFunc
};
```

## Important Rules and Best Practices

### Rules:

1. **Order matters** in non-designated initialization

```c
struct Point {int x; int y;};
struct Point p = {10, 20}; // x=10, y=20 (order dependent)
```

2. **Excess initializers cause error**

```c
struct Point p = {10, 20, 30}; // ERROR: too many initializers
```

3. **Uninitialized members** get zero value

```c
struct Point p = {10}; // x=10, y=0
```

4. **Cannot initialize with variables** in global scope

```c
int a = 10;
struct Point p = {a, 20}; // ERROR if global, OK if local
```

### Best Practices:

1. **Always initialize structures** to avoid garbage values

```c
struct Node* node = (struct Node*)malloc(sizeof(struct Node));
node->data = 0; // Good practice
node->next = NULL; // Always initialize pointers
```

2. **Use designated initializers** for clarity (C99+)

```c
struct Config config = {
 .timeout = 30,
 .retries = 3,
 .debug = true
};
```

3. **Use initialization functions** for complex structures

```c
void initStudent(struct Student* s, int roll, char* name, float marks) {
 s->roll_no = roll;
 strncpy(s->name, name, 49);
 s->name[49] = '\0';
 s->marks = marks;
}
```

## Complete Example

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define structure for a linked list node
struct Student {
 int roll_no;
 char name[50];
 float marks;
 struct Student* next;
};

// Function to create and initialize a student node
struct Student* createStudent(int roll, char* name, float marks) {
 struct Student* newStudent = (struct Student*)malloc(sizeof(struct Student));

 if (newStudent == NULL) {
 printf("Memory allocation failed\n");
 return NULL;
 }

 newStudent->roll_no = roll;
 strncpy(newStudent->name, name, 49);
 newStudent->name[49] = '\0';
 newStudent->marks = marks;
 newStudent->next = NULL;

 return newStudent;
}

int main() {
 // Different initialization methods

 // Method 1: Direct initialization
 struct Student s1 = {101, "Alice", 85.5, NULL};

 // Method 2: Using initialization function
 struct Student* s2 = createStudent(102, "Bob", 78.3);

 // Method 3: Designated initializers
 struct Student s3 = {
 .roll_no = 103,
 .name = "Charlie",
 .marks = 92.1,
 .next = NULL
 };

 // Print details
 printf("Student 1: %d, %s, %.2f\n", s1.roll_no, s1.name, s1.marks);
 printf("Student 2: %d, %s, %.2f\n", s2->roll_no, s2->name, s2->marks);
 printf("Student 3: %d, %s, %.2f\n", s3.roll_no, s3.name, s3.marks);

 // Free dynamically allocated memory
 free(s2);

 return 0;
}
```

## Exam Tips

1. Understand all initialization methods and their syntax
2. Know the difference between initialization and assignment
3. Remember that uninitialized members are set to 0
4. Be able to initialize nested structures
5. Understand self-referential structures for linked lists
6. Practice writing initialization code for common data structures
7. Know when to use malloc for dynamic structures vs static declaration
8. Remember to initialize pointers to NULL to avoid dangling pointers
