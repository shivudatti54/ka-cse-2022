# **Linked Lists: Singly Linked, Lists and Chains**

## **Introduction**

A linked list is a linear collection of data elements, where each element points to the next. This structure allows for efficient insertion and deletion of elements at any position in the list. In this section, we will explore singly linked lists, lists and chains, representing chains in C, linked stacks and queues, and polynomials.

## **Definition of Linked Lists**

A linked list is a linear collection of data elements, where each element is a separate object, called a "node". Each node contains two items:

- Data: The actual data stored in the node.
- Link: A reference (i.e., a "link") to the next node in the sequence.

### Types of Linked Lists

- **Singly Linked List**: Each node points to the next node in the sequence.
- **Doubly Linked List**: Each node points to both the previous and next nodes in the sequence.
- **Circularly Linked List**: The last node points back to the first node, forming a circle.

## **Singly Linked List**

A singly linked list is the most common type of linked list. Each node contains a data field and a link to the next node.

### Operations on Singly Linked Lists

- **Insertion**: Adding a new node to the list.
- **Deletion**: Removing a node from the list.
- **Traversal**: Visiting each node in the list.

### Example of a Singly Linked List in C

```c
// Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Linked list structure
typedef struct LinkedList {
    Node* head;
} LinkedList;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a new node at the end of the list
void insertNode(LinkedList* list, int data) {
    Node* newNode = createNode(data);
    if (list->head == NULL) {
        list->head = newNode;
    } else {
        Node* current = list->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

// Function to print the list
void printList(LinkedList* list) {
    Node* current = list->head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Example usage
int main() {
    LinkedList list;
    list.head = NULL;

    insertNode(&list, 1);
    insertNode(&list, 2);
    insertNode(&list, 3);

    printList(&list); // Output: 1 -> 2 -> 3 -> NULL

    return 0;
}
```

## **Lists and Chains**

A list is a collection of data elements in a specific order, and a chain is a list of pointers to nodes in a linked list.

### Lists and Chains

- **Linked List**: A linear collection of data elements, where each element points to the next.
- **Chain**: A list of pointers to nodes in a linked list.

### Example of Lists and Chains

```c
// Linked list structure
typedef struct LinkedList {
    Node* head;
} LinkedList;

// Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to create a new linked list
LinkedList* createLinkedList() {
    LinkedList* list = (LinkedList*)malloc(sizeof(LinkedList));
    list->head = NULL;
    return list;
}

// Example usage
int main() {
    LinkedList* list = createLinkedList();

    Node* node1 = createNode(1);
    Node* node2 = createNode(2);

    node1->next = node2;

    list->head = node1;

    // Chain of pointers to nodes
    Node** chain = (Node**)malloc(sizeof(Node*) * 3);
    *chain = list->head;
    chain[1] = (*chain)->next;
    chain[2] = ((Node**)chain[1])->next;

    printf("%d\n", (*chain)[0]->data); // Output: 1
    printf("%d\n", ((Node**)chain[1])->data); // Output: 2
    printf("%d\n", ((Node**)chain[2])->data); // Output: NULL

    return 0;
}
```

## **Representing Chains in C**

A chain is a list of pointers to nodes in a linked list. We can represent a chain in C using an array of pointers to nodes.

### Example of Representing Chains in C

```c
// Chain structure
typedef struct Chain {
    Node** nodes;
} Chain;

// Function to create a new chain
Chain* createChain(int size) {
    Chain* chain = (Chain*)malloc(sizeof(Chain));
    chain->nodes = (Node**)malloc(sizeof(Node*) * size);
    return chain;
}

// Example usage
int main() {
    Chain* chain = createChain(3);

    Node* node1 = createNode(1);
    Node* node2 = createNode(2);
    Node* node3 = createNode(3);

    chain->nodes[0] = node1;
    chain->nodes[1] = node2;
    chain->nodes[2] = node3;

    printf("%d\n", chain->nodes[0]->data); // Output: 1
    printf("%d\n", chain->nodes[1]->data); // Output: 2
    printf("%d\n", chain->nodes[2]->data); // Output: 3

    return 0;
}
```

## **Linked Stacks and Queues**

A linked stack is a data structure that follows the Last-In-First-Out (LIFO) principle, while a linked queue follows the First-In-First-Out (FIFO) principle.

### Linked Stack

- **Last-In-First-Out (LIFO)**: The most recently added element is the first one to be removed.
- **Operations**: Push, Pop, Peek.

### Linked Queue

- **First-In-First-Out (FIFO)**: The first element added is the first one to be removed.
- **Operations**: Enqueue, Dequeue, Peek.

### Example of Linked Stack and Queue in C

```c
// Linked stack structure
typedef struct Stack {
    Node* top;
} Stack;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to create a new stack
Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = NULL;
    return stack;
}

// Function to push a new node onto the stack
void push(Stack* stack, int data) {
    Node* newNode = createNode(data);
    newNode->next = stack->top;
    stack->top = newNode;
}

// Function to pop a node from the stack
int pop(Stack* stack) {
    if (stack->top == NULL) {
        printf("Stack is empty\n");
        return -1;
    }
    int data = stack->top->data;
    Node* temp = stack->top;
    stack->top = stack->top->next;
    free(temp);
    return data;
}

// Function to peek the top node on the stack
int peek(Stack* stack) {
    if (stack->top == NULL) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->top->data;
}

// Linked queue structure
typedef struct Queue {
    Node* front;
    Node* rear;
} Queue;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to create a new queue
Queue* createQueue() {
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->front = NULL;
    queue->rear = NULL;
    return queue;
}

// Function to enqueue a new node into the queue
void enqueue(Queue* queue, int data) {
    Node* newNode = createNode(data);
    if (queue->rear == NULL) {
        queue->front = newNode;
        queue->rear = newNode;
    } else {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
}

// Function to dequeue a node from the queue
int dequeue(Queue* queue) {
    if (queue->front == NULL) {
        printf("Queue is empty\n");
        return -1;
    }
    int data = queue->front->data;
    Node* temp = queue->front;
    queue->front = queue->front->next;
    if (queue->front == NULL) {
        queue->rear = NULL;
    }
    free(temp);
    return data;
}

// Function to peek the front node on the queue
int peek(Queue* queue) {
    if (queue->front == NULL) {
        printf("Queue is empty\n");
        return -1;
    }
    return queue->front->data;
}

// Example usage
int main() {
    Stack* stack = createStack();
    push(stack, 1);
    push(stack, 2);
    push(stack, 3);

    printf("%d\n", pop(stack)); // Output: 3
    printf("%d\n", peek(stack)); // Output: 2

    Queue* queue = createQueue();
    enqueue(queue, 1);
    enqueue(queue, 2);
    enqueue(queue, 3);

    printf("%d\n", dequeue(queue)); // Output: 1
    printf("%d\n", peek(queue)); // Output: 2

    return 0;
}
```

## **Polynomials**

A polynomial is a mathematical expression consisting of variables and coefficients combined using various operations.

### Example of Polynomials

- **Linear Polynomial**: ax + b
- **Quadratic Polynomial**: ax^2 + bx + c
- **Cubic Polynomial**: ax^3 + bx^2 + cx + d

### Operations on Polynomials

- **Addition**: Combining two or more polynomials.
- **Subtraction**: Subtracting one polynomial from another.
- **Multiplication**: Multiplying a polynomial by a constant or another polynomial.
- **Division**: Dividing a polynomial by another polynomial.

### Example of Polynomials in C

```c
// Polynomial structure
typedef struct Polynomial {
    int* coefficients;
    int degree;
    int exponent;
} Polynomial;

// Function to create a new polynomial
Polynomial* createPolynomial(int degree) {
    Polynomial* poly = (Polynomial*)malloc(sizeof(Polynomial));
    poly->coefficients = (int*)malloc(sizeof(int) * (degree + 1));
    poly->degree = degree;
    poly->exponent = 0;
    return poly;
}

// Function to add two polynomials
Polynomial* addPolynomials(Polynomial* poly1, Polynomial* poly2) {
    Polynomial* result = createPolynomial(poly1->degree + poly2->degree);
    for (int i = 0; i <= poly1->degree; i++) {
        result->coefficients[i] = poly1->coefficients[i] + poly2->coefficients[i];
    }
    return result;
}

// Function to subtract two polynomials
Polynomial* subtractPolynomials(Polynomial* poly1, Polynomial* poly2) {
    Polynomial* result = createPolynomial(poly1->degree - poly2->degree);
    for (int i = 0; i <= poly1->degree; i++) {
        result->coefficients[i] = poly1->coefficients[i] - poly2->coefficients[i];
    }
    return result;
}

// Function to multiply a polynomial by a constant
Polynomial* multiplyPolynomial(Polynomial* poly, int constant) {
    Polynomial* result = createPolynomial(poly->degree + 1);
    for (int i = 0; i <= poly->degree; i++) {
        result->coefficients[i] = poly->coefficients[i] * constant;
    }
    return result;
}

// Function to divide two polynomials
Polynomial* dividePolynomials(Polynomial* poly1, Polynomial* poly2) {
    // Implementation of polynomial division algorithm
    // ...
}

// Example usage
int main() {
    Polynomial* poly1 = createPolynomial(2);
    poly1->coefficients[0] = 1;
    poly1->coefficients[1] = 2;
    poly1->coefficients[2] = 3;

    Polynomial* poly2 = createPolynomial(2);
    poly2->coefficients[0] = 1;
    poly2->coefficients[1] = 2;
    poly2->coefficients[2] = 3;

    Polynomial* poly3 = addPolynomials(poly1, poly2);
    printf("%d + %d x + %d x^2\n", poly3->coefficients[0], poly3->coefficients[1], poly3->coefficients[2]);

    Polynomial* poly4 = multiplyPolynomial(poly1, 2);
    printf("%d + %d x + %d x^2\n", poly4->coefficients[0], poly4->coefficients[1], poly4->coefficients[2]);

    Polynomial* poly5 = dividePolynomials(poly1, poly2);
    printf("%d + %d x + %d x^2\n", poly5->coefficients[0], poly5->coefficients[1], poly5->coefficients[2]);

    return 0;
}
```

This study material covers the basics of linked lists, lists and chains, representing chains in C, linked stacks and queues, and polynomials. It includes definitions, explanations, examples, and code snippets to help you understand and implement these concepts.
