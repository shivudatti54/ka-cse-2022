# Self-Referential Structures

## Introduction

Self-referential structures are a fundamental concept in C programming that enable the creation of **dynamic data structures** like linked lists, trees, and graphs. These structures contain at least one member that is a **pointer to the same type of structure**, allowing them to reference instances of themselves. This recursive definition forms the backbone of memory-efficient, flexible data organizations.

In static data structures like arrays, memory is allocated contiguously and size is fixed. Self-referential structures overcome these limitations by using **dynamic memory allocation**, enabling data structures to grow/shrink at runtime. This is critical for implementing linked lists (Module 3's core topic) and other advanced data organizations in the syllabus.

The importance of self-referential structures extends to real-world systems:

- File system directories (tree structures)
- Browser history navigation (doubly linked lists)
- Social network friend connections (graph nodes)

## Key Concepts

### 1. Definition & Syntax

A self-referential structure contains a pointer to a structure of its own type:

```c
struct node {
 int data; // Data field (can be any type)
 struct node *next; // Pointer to another node
};
```

- `next` is a **pointer member** that stores the address of another `node` structure
- The structure is incomplete until runtime when memory is allocated dynamically

### 2. Memory Allocation

Self-referential structures use **heap memory** via `malloc()`/`calloc()`:

```c
struct node *n1 = (struct node*)malloc(sizeof(struct node));
n1->data = 10;
n1->next = NULL;
```

- `malloc` allocates memory for one node at runtime
- `->` operator accesses structure members through pointers

### 3. Linked List Foundation

A singly linked list is built using self-referential nodes:

```
[HEAD] -> [10|➔] -> [20|➔] -> [30|NULL]
```

- Each node's `next` points to the subsequent node
- Last node's `next` is `NULL` (list termination)

### 4. Static vs. Dynamic Allocation

| Feature           | Static Allocation      | Linked Allocation       |
| ----------------- | ---------------------- | ----------------------- |
| Memory Location   | Stack                  | Heap                    |
| Size              | Fixed at compile time  | Flexible at runtime     |
| Access            | Direct (array indices) | Sequential via pointers |
| Memory Efficiency | Wastes unused space    | Optimal usage           |

## Examples

### Example 1: Creating a 3-Node Linked List

**Objective**: Create a linked list with nodes containing 10, 20, 30.

**Step-by-Step**:

1. Allocate memory for nodes:

```c
struct node *head = malloc(sizeof(struct node));
struct node *second = malloc(sizeof(struct node));
struct node *third = malloc(sizeof(struct node));
```

2. Assign data and links:

```c
head->data = 10;
head->next = second;

second->data = 20;
second->next = third;

third->data = 30;
third->next = NULL; // Marks end of list
```

**Visualization**:

```
HEAD
 │
 ▼
[10|➔]───▶[20|➔]───▶[30|∅]
```

### Example 2: Inserting a Node at Beginning

**Objective**: Add a node with data=5 at the list's start.

**Algorithm**:

1. Create new node:

```c
struct node *new_node = malloc(sizeof(struct node));
new_node->data = 5;
```

2. Reassign pointers:

```c
new_node->next = head; // New node points to old head
head = new_node; // Update head to new node
```

**Result**:

```
HEAD
 │
 ▼
[5|➔]───▶[10|➔]───▶[20|➔]───▶[30|∅]
```

### Example 3: Traversing a Linked List

**Objective**: Print all elements of the list.

**Code**:

```c
void display(struct node *head) {
 struct node *temp = head;

 while(temp != NULL) {
 printf("%d -> ", temp->data);
 temp = temp->next;
 }
 printf("NULL\n");
}
```

**Output**:

```
5 -> 10 -> 20 -> 30 -> NULL
```

## Diagrams (Textual Representation)

### Diagram 1: Node Structure

```
+-----------------+
| data | // Stores the value (int, float, etc.)
+-----------------+
| *next | // Pointer to next node
+-----------------+
```

### Diagram 2: Linked List in Memory

```
Heap Memory Layout:
0x1000: [10 | 0x1008]
0x1008: [20 | 0x1010]
0x1010: [30 | NULL]

Stack:
head pointer → 0x1000
```

## Exam Tips

1. **Definition Questions**:

- "A structure containing a pointer to a structure of the same type."
- Always mention the pointer member and its role in linking nodes.

2. **Syntax Focus**:

- Practice writing self-referential structure declarations. Common error: Forgetting `struct node*` in the pointer declaration.

3. **Pointer Arithmetic**:

- In traversal operations, use `temp = temp->next` (not `temp++`). Linked lists don't use contiguous memory!

4. **Memory Management**:

- For every `malloc()`, there should be a corresponding `free()` to prevent memory leaks (often asked in 6-mark questions).

5. **Common Errors**:

- Segmentation faults occur when accessing `next` without checking `NULL`.
- Forgetting to update multiple pointers during insert/delete operations.

6. **Comparison Questions**:

- Static vs. Dynamic allocation: Focus on memory flexibility and access speed differences.

7. **Code Tracing**:

- Be prepared to draw pointer diagrams for code snippets involving multiple insertions/deletions.
