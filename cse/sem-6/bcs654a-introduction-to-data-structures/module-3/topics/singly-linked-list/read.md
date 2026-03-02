# Singly Linked List

## Overview

A **Singly Linked List** is a linked list where each node contains data and a pointer to the **next** node only. Traversal is possible in only **one direction** (forward).

```
HEAD
 ↓
┌────┬────┐ ┌────┬────┐ ┌────┬────┐
│ 10 │ ──┼───→│ 20 │ ──┼───→│ 30 │NULL│
└────┴────┘ └────┴────┘ └────┴────┘
```

## Node Structure

```c
struct Node {
 int data;
 struct Node *next;
};
```

## Complete Operations

### 1. Insert at Beginning

```c
void insertAtBeginning(struct Node **head, int data) {
 struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
 newNode->data = data;
 newNode->next = *head;
 *head = newNode;
}
```

**Time: O(1)** | **Space: O(1)**

### 2. Insert at End

```c
void insertAtEnd(struct Node **head, int data) {
 struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
 newNode->data = data;
 newNode->next = NULL;

 // If list is empty
 if(*head == NULL) {
 *head = newNode;
 return;
 }

 // Traverse to last node
 struct Node *temp = *head;
 while(temp->next != NULL) {
 temp = temp->next;
 }
 temp->next = newNode;
}
```

**Time: O(n)** | **Space: O(1)**

### 3. Insert at Position

```c
void insertAtPosition(struct Node **head, int data, int position) {
 struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
 newNode->data = data;

 // Insert at beginning
 if(position == 0) {
 newNode->next = *head;
 *head = newNode;
 return;
 }

 // Find node before position
 struct Node *temp = *head;
 for(int i = 0; i < position - 1 && temp != NULL; i++) {
 temp = temp->next;
 }

 if(temp == NULL) {
 printf("Position out of bounds\n");
 free(newNode);
 return;
 }

 newNode->next = temp->next;
 temp->next = newNode;
}
```

**Time: O(n)** | **Space: O(1)**

### 4. Delete from Beginning

```c
void deleteFromBeginning(struct Node **head) {
 if(*head == NULL) {
 printf("List is empty\n");
 return;
 }

 struct Node *temp = *head;
 *head = (*head)->next;
 free(temp);
}
```

**Time: O(1)** | **Space: O(1)**

### 5. Delete from End

```c
void deleteFromEnd(struct Node **head) {
 if(*head == NULL) {
 printf("List is empty\n");
 return;
 }

 // Only one node
 if((*head)->next == NULL) {
 free(*head);
 *head = NULL;
 return;
 }

 // Find second to last node
 struct Node *temp = *head;
 while(temp->next->next != NULL) {
 temp = temp->next;
 }

 free(temp->next);
 temp->next = NULL;
}
```

**Time: O(n)** | **Space: O(1)**

### 6. Delete by Value

```c
void deleteByValue(struct Node **head, int value) {
 if(*head == NULL) return;

 // If head node has the value
 if((*head)->data == value) {
 struct Node *temp = *head;
 *head = (*head)->next;
 free(temp);
 return;
 }

 // Find node before the one to delete
 struct Node *temp = *head;
 while(temp->next != NULL && temp->next->data != value) {
 temp = temp->next;
 }

 if(temp->next == NULL) {
 printf("Value not found\n");
 return;
 }

 struct Node *toDelete = temp->next;
 temp->next = temp->next->next;
 free(toDelete);
}
```

**Time: O(n)** | **Space: O(1)**

### 7. Reverse the List

```c
void reverse(struct Node **head) {
 struct Node *prev = NULL;
 struct Node *current = *head;
 struct Node *next = NULL;

 while(current != NULL) {
 next = current->next; // Store next
 current->next = prev; // Reverse link
 prev = current; // Move prev forward
 current = next; // Move current forward
 }
 *head = prev;
}
```

**Time: O(n)** | **Space: O(1)**

### 8. Find Middle Element

```c
struct Node* findMiddle(struct Node *head) {
 if(head == NULL) return NULL;

 struct Node *slow = head;
 struct Node *fast = head;

 while(fast != NULL && fast->next != NULL) {
 slow = slow->next; // Move 1 step
 fast = fast->next->next; // Move 2 steps
 }

 return slow;
}
```

**Time: O(n)** | **Space: O(1)**

### 9. Detect Cycle (Floyd's Algorithm)

```c
int hasCycle(struct Node *head) {
 if(head == NULL) return 0;

 struct Node *slow = head;
 struct Node *fast = head;

 while(fast != NULL && fast->next != NULL) {
 slow = slow->next;
 fast = fast->next->next;

 if(slow == fast) {
 return 1; // Cycle detected
 }
 }
 return 0; // No cycle
}
```

**Time: O(n)** | **Space: O(1)**

## Time Complexity Summary

| Operation             | Time | Notes                     |
| --------------------- | ---- | ------------------------- |
| Insert at Beginning   | O(1) | Direct access via head    |
| Insert at End         | O(n) | Must traverse to end      |
| Insert at Position    | O(n) | Must traverse to position |
| Delete from Beginning | O(1) | Direct access via head    |
| Delete from End       | O(n) | Must find second to last  |
| Delete by Value       | O(n) | Must search for value     |
| Search                | O(n) | Must traverse             |
| Reverse               | O(n) | Single pass               |
| Find Middle           | O(n) | Two-pointer technique     |
| Detect Cycle          | O(n) | Floyd's algorithm         |

## Optimizing with Tail Pointer

Maintain a tail pointer to make insert at end O(1):

```c
struct LinkedList {
 struct Node *head;
 struct Node *tail;
 int size;
};

void insertAtEnd(struct LinkedList *list, int data) {
 struct Node *newNode = createNode(data);

 if(list->head == NULL) {
 list->head = list->tail = newNode;
 } else {
 list->tail->next = newNode;
 list->tail = newNode;
 }
 list->size++;
}
```

## Common Patterns

### 1. Two Pointer Technique

- Slow and fast pointers
- Used for: finding middle, detecting cycles

### 2. Dummy Node

- Simplifies edge cases at head

```c
struct Node dummy;
dummy.next = head;
// Operate on dummy.next
return dummy.next;
```

### 3. Runner Technique

- One pointer ahead by k nodes
- Used for: finding kth from end, splitting list

## Important Edge Cases

1. **Empty List** - head is NULL
2. **Single Node** - head->next is NULL
3. **Two Nodes** - Consider both when deleting
4. **Position Out of Bounds** - Invalid index handling
5. **Delete from Empty List** - Check before operation

## Key Points

1. Singly linked lists support forward traversal only
2. Insert/delete at head is O(1)
3. Operations at end require traversal O(n)
4. Always handle empty list and single node cases
5. Free memory when deleting nodes (in C/C++)
6. Use two-pointer technique for many problems
