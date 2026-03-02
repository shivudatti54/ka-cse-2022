# Linked Lists

### Singly Linked Lists

- Definition: A linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next.
- Types of Singly Linked Lists:
  - **Singly Linked List**: Each element points to the next element.
  - **Circularly Linked List**: The last element points to the first element.

### Lists and Chains

- **List**: A collection of elements of the same type.
- **Chain**: A collection of elements of different types.

### Representing Chains in C

- Definition: A data structure that represents a linked list where each element can be of any type.
- Example: `struct Node *head;`
- Implementation:

      ```c

  typedef struct Node {
  int data;
  struct Node\* next;
  } Node;

// Function to create a new node
Node* createNode(int data) {
Node* newNode = (Node\*)malloc(sizeof(Node));
newNode->data = data;
newNode->next = NULL;
return newNode;
}

// Function to insert a node at the end
void insertNode(Node\*_ head, int data) {
Node_ newNode = createNode(data);
if (*head == NULL) {
*head = newNode;
} else {
Node* last = *head;
while (last->next != NULL) {
last = last->next;
}
last->next = newNode;
}
}

```

### Linked Stacks and Queues

*   **Linked Stack**:
    *   Definition: A stack that uses a linked list to store elements.
    *   Operations: `push`, `pop`, `peek`
*   **Linked Queue**:
    *   Definition: A queue that uses a linked list to store elements.
    *   Operations: `enqueue`, `dequeue`, `peek`

### Important Formulas and Theorems

*   **Time Complexity of Linked List Operations**:
    *   `insert` (Singly Linked List): O(n)
    *   `insert` (Circularly Linked List): O(1)
    *   `delete` (Singly Linked List): O(n)
    *   `delete` (Circularly Linked List): O(1)
*   **Space Complexity of Linked List Operations**:
    *   `insert` (Singly Linked List): O(1)
    *   `insert` (Circularly Linked List): O(1)
    *   `delete` (Singly Linked List): O(1)
    *   `delete` (Circularly Linked List): O(1)
```
