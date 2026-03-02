# **Introduction to Data Structures**

**Module: @#@10012025**
**Topic: 6.1 to 6.3**
**Study Material**

---

### 6.1: Arrays

---

**Definition:** An array is a collection of elements of the same data type stored in contiguous memory locations.

**Explanation:** Arrays are a fundamental data structure in programming languages. They allow us to store multiple values of the same type in a single variable.

**Key Concepts:**

- **Indexing:** Elements in an array are accessed using an index, which is a numerical value that represents the position of the element in the array.
- **Size:** The number of elements in an array is known as its size.
- **Initialization:** Arrays can be initialized with a set of values before they are used.

**Example:**

```c
int numbers[5] = {10, 20, 30, 40, 50};
printf("%d ", numbers[0]);  // Output: 10
```

In this example, we declare an array `numbers` with 5 elements and initialize it with the values 10, 20, 30, 40, and 50. We then access the first element of the array using the index 0.

### 6.2: Linked Lists

---

**Definition:** A linked list is a dynamic collection of elements, where each element points to the next element in the list.

**Explanation:** Linked lists are a fundamental data structure in computer science. They allow us to efficiently insert and delete elements from a list.

**Key Concepts:**

- **Node:** Each element in a linked list is called a node, which contains a value and a reference to the next node in the list.
- **Head:** The first node in a linked list is called the head.
- **Tail:** The last node in a linked list is called the tail.
- **Insertion:** To insert a new node in a linked list, we need to update the references of the adjacent nodes.
- **Deletion:** To delete a node in a linked list, we need to update the references of the adjacent nodes.

**Example:**

```c
struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

void insertNode(struct Node** head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void printList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
```

In this example, we define a linked list with a `Node` struct that contains an integer value and a reference to the next node. We then implement functions to insert a new node at the end of the list and print the list.

### 6.3: Stacks and Queues

---

**Definition:** A stack is a Last-In-First-Out (LIFO) data structure, where the last element added is the first one to be removed. A queue is a First-In-First-Out (FIFO) data structure, where the first element added is the first one to be removed.

**Explanation:** Stacks and queues are fundamental data structures in computer science. They allow us to efficiently implement recursive algorithms and model real-world systems.

**Key Concepts:**

- **Stack Operations:** Push, pop, peek
- **Queue Operations:** Enqueue, dequeue, peek

**Example:**

```c
#include <stdio.h>
#include <stdlib.h>

// Stack operations
void push(int* stack, int data) {
    int* temp = (int*)malloc(sizeof(int));
    *temp = data;
    *stack = realloc(*stack, (size_t)++*stack * sizeof(int));
    (*stack)[*stack - 1] = *temp;
}

int pop(int* stack) {
    int data = (*stack)[*stack - 1];
    *stack = realloc(*stack, (size_t)--*stack * sizeof(int));
    free((*stack)[*stack - 1]);
    return data;
}

int peek(int* stack) {
    return (*stack)[*stack - 1];
}

// Queue operations
void enqueue(int* queue, int data) {
    int* temp = (int*)malloc(sizeof(int));
    *temp = data;
    queue = realloc(queue, (size_t)++*queue * sizeof(int));
    (*queue)[*queue - 1] = *temp;
}

int dequeue(int* queue) {
    int data = (*queue)[*queue - 1];
    *queue = realloc(*queue, (size_t)--*queue * sizeof(int));
    free((*queue)[*queue - 1]);
    return data;
}

int peek(int* queue) {
    return (*queue)[*queue - 1];
}
```

In this example, we define functions to implement push, pop, peek, enqueue, dequeue, and peek operations for stacks and queues.
