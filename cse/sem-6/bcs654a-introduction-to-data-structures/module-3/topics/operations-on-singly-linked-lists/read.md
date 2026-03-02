# Singly Linked Lists: Operations and Implementation

## Introduction

A singly linked list is a linear data structure consisting of nodes, where each node contains data and a pointer to the next node in the sequence. Unlike arrays, linked lists provide dynamic memory allocation, allowing efficient insertion and deletion without requiring contiguous memory blocks.

### Node Structure in C

```c
struct Node {
 int data; // Stores the actual information
 struct Node* next; // Pointer to the next node in the list
};
```

The `data` field holds the element value, while `next` pointer maintains the link to the subsequent node. The last node's `next` pointer is set to NULL, indicating the end of the list.

## Why Linked Lists Over Arrays?

| Aspect             | Array                  | Linked List               |
| ------------------ | ---------------------- | ------------------------- |
| Size               | Fixed at compile time  | Dynamic, grows at runtime |
| Insertion/Deletion | O(n) shifting required | O(1) at known position    |
| Memory             | Contiguous block       | Scattered allocation      |
| Access             | Random access O(1)     | Sequential access O(n)    |

## Fundamental Operations

### 1. Insertion Operations

**Insert at Beginning (O(1)):**

- Create a new node with the data
- Set new node's next pointer to current head
- Update head pointer to new node

```c
void insertAtBeginning(struct Node** head, int data) {
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 newNode->data = data;
 newNode->next = *head;
 *head = newNode;
}
```

**Insert at End (O(n)):**

- Traverse to the last node
- Set last node's next to new node
- New node's next becomes NULL

**Insert at Position (O(n)):**

- Traverse to position (n-1)
- Adjust pointers to include new node

### 2. Deletion Operations

**Delete from Beginning (O(1)):**

- Store head in temporary variable
- Move head to next node
- Free the old head memory

**Delete from End (O(n)):**

- Traverse to second-last node
- Free last node
- Set second-last's next to NULL

**Delete by Value (O(n)):**

- Find node containing value (track previous)
- Adjust previous node's next pointer
- Free the deleted node's memory

### 3. Traversal and Search

**Traversal (O(n)):**
Starting from head, visit each node sequentially until NULL is reached:

```c
void traverse(struct Node* head) {
 while (head != NULL) {
 printf("%d -> ", head->data);
 head = head->next;
 }
 printf("NULL\n");
}
```

**Linear Search (O(n)):**
Compare each node's data with target value until found or list ends.

## Advanced Operations

### 4. Reversing a Linked List

Using three pointers (prev, current, next), we reverse the direction of each link:

```c
struct Node* reverse(struct Node* head) {
 struct Node* prev = NULL;
 struct Node* current = head;
 struct Node* next = NULL;

 while (current != NULL) {
 next = current->next; // Save next
 current->next = prev; // Reverse link
 prev = current; // Move prev forward
 current = next; // Move current forward
 }
 return prev; // New head
}
```

**Time Complexity: O(n), Space Complexity: O(1)**

### 5. Finding Middle Element

Using Floyd's Tortoise and Hare algorithm with slow and fast pointers:

- Slow pointer moves one step at a time
- Fast pointer moves two steps at a time
- When fast reaches end, slow is at middle

```c
struct Node* findMiddle(struct Node* head) {
 struct Node* slow = head;
 struct Node* fast = head;

 while (fast != NULL && fast->next != NULL) {
 slow = slow->next;
 fast = fast->next->next;
 }
 return slow;
}
```

**Time Complexity: O(n), Space Complexity: O(1)**

### 6. Cycle Detection

Floyd's Cycle Detection Algorithm determines if a cycle exists:

- If slow and fast pointers meet, cycle exists
- Start fast from intersection point to find cycle length
- Use two pointers separated by cycle length to find cycle start

**Proof of Correctness:**
Let distance from head to cycle start be 'a', cycle length be 'c'. When slow enters cycle, fast is ahead. In each iteration, fast gains one position on slow. After at most 'c' iterations, they must meet, proving cycle existence.

**Time Complexity: O(n), Space Complexity: O(1)**

## Important Theorems

**Theorem 1:** In a linked list of n nodes, any operation requiring traversal has Ω(n) time complexity in the worst case.

**Theorem 2:** The space complexity for reversing a linked list iteratively is O(1), as only three pointers are used regardless of input size.

## Edge Cases to Handle

1. Empty list (head = NULL)
2. Single node list
3. Insertion/deletion at first position
4. Insertion/deletion at last position
5. Position out of bounds
6. Memory allocation failure
7. Attempting to delete from empty list

## Memory Management

- Always allocate memory using `malloc()` before insertion
- Always free memory using `free()` after deletion
- Check for NULL after malloc to handle allocation failure
- Set freed node pointers to NULL where applicable
