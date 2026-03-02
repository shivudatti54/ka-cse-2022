# Insert, Delete, and Display Operations on Linked Lists

## Introduction

The three fundamental operations on linked lists are:

1. **Insertion** - Adding new nodes
2. **Deletion** - Removing existing nodes
3. **Display** - Traversing and printing the list

These operations form the basis of linked list manipulation and are essential for understanding more complex data structures.

## Node Structure

```c
struct Node {
 int data;
 struct Node* next;
};
```

## 1. INSERTION Operations

Insertion can be performed at three positions:

### A. Insert at Beginning (Insert at Head)

**Algorithm:**

1. Create a new node
2. Set new node's data
3. Point new node's next to current head
4. Update head to point to new node

**Time Complexity:** O(1)

```c
void insertAtBeginning(struct Node** head, int data) {
 // Create new node
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 if (newNode == NULL) {
 printf("Memory allocation failed\n");
 return;
 }

 // Set data and link
 newNode->data = data;
 newNode->next = *head;

 // Update head
 *head = newNode;

 printf("Inserted %d at beginning\n", data);
}
```

**Visualization:**

```
Before: 20 -> 30 -> 40 -> NULL
Insert 10 at beginning
After: 10 -> 20 -> 30 -> 40 -> NULL
```

### B. Insert at End (Insert at Tail)

**Algorithm:**

1. Create a new node
2. Set new node's data and next to NULL
3. If list is empty, make new node the head
4. Else, traverse to last node
5. Update last node's next to point to new node

**Time Complexity:** O(n) - need to traverse to end

```c
void insertAtEnd(struct Node** head, int data) {
 // Create new node
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 if (newNode == NULL) {
 printf("Memory allocation failed\n");
 return;
 }

 newNode->data = data;
 newNode->next = NULL;

 // If list is empty
 if (*head == NULL) {
 *head = newNode;
 printf("Inserted %d as first node\n", data);
 return;
 }

 // Traverse to last node
 struct Node* current = *head;
 while (current->next != NULL) {
 current = current->next;
 }

 // Link last node to new node
 current->next = newNode;
 printf("Inserted %d at end\n", data);
}
```

### C. Insert at Specific Position

**Algorithm:**

1. Create a new node
2. If position is 1, insert at beginning
3. Traverse to (position - 1)th node
4. Set new node's next to current node's next
5. Set current node's next to new node

**Time Complexity:** O(n) - need to traverse to position

```c
void insertAtPosition(struct Node** head, int data, int position) {
 // Create new node
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 if (newNode == NULL) {
 printf("Memory allocation failed\n");
 return;
 }

 newNode->data = data;

 // Insert at beginning
 if (position == 1) {
 newNode->next = *head;
 *head = newNode;
 printf("Inserted %d at position %d\n", data, position);
 return;
 }

 // Traverse to (position - 1)th node
 struct Node* current = *head;
 for (int i = 1; i < position - 1 && current != NULL; i++) {
 current = current->next;
 }

 // Check if position is valid
 if (current == NULL) {
 printf("Invalid position\n");
 free(newNode);
 return;
 }

 // Insert node
 newNode->next = current->next;
 current->next = newNode;
 printf("Inserted %d at position %d\n", data, position);
}
```

**Visualization:**

```
Before: 10 -> 20 -> 40 -> NULL
Insert 30 at position 3
After: 10 -> 20 -> 30 -> 40 -> NULL
```

## 2. DELETION Operations

### A. Delete from Beginning

**Algorithm:**

1. Check if list is empty
2. Save the current head in a temp pointer
3. Update head to point to next node
4. Free the old head

**Time Complexity:** O(1)

```c
void deleteFromBeginning(struct Node** head) {
 // Check if list is empty
 if (*head == NULL) {
 printf("List is empty\n");
 return;
 }

 // Save current head
 struct Node* temp = *head;
 int deletedData = temp->data;

 // Update head
 *head = temp->next;

 // Free old head
 free(temp);
 printf("Deleted %d from beginning\n", deletedData);
}
```

### B. Delete from End

**Algorithm:**

1. Check if list is empty
2. If only one node, delete it and set head to NULL
3. Else, traverse to second last node
4. Free last node
5. Set second last node's next to NULL

**Time Complexity:** O(n)

```c
void deleteFromEnd(struct Node** head) {
 // Check if list is empty
 if (*head == NULL) {
 printf("List is empty\n");
 return;
 }

 // If only one node
 if ((*head)->next == NULL) {
 int deletedData = (*head)->data;
 free(*head);
 *head = NULL;
 printf("Deleted %d from end\n", deletedData);
 return;
 }

 // Traverse to second last node
 struct Node* current = *head;
 while (current->next->next != NULL) {
 current = current->next;
 }

 // Delete last node
 int deletedData = current->next->data;
 free(current->next);
 current->next = NULL;
 printf("Deleted %d from end\n", deletedData);
}
```

### C. Delete from Specific Position

**Algorithm:**

1. Check if list is empty
2. If position is 1, delete from beginning
3. Traverse to (position - 1)th node
4. Save node to delete in temp
5. Update links to skip the node
6. Free the deleted node

**Time Complexity:** O(n)

```c
void deleteFromPosition(struct Node** head, int position) {
 // Check if list is empty
 if (*head == NULL) {
 printf("List is empty\n");
 return;
 }

 // Delete first node
 if (position == 1) {
 struct Node* temp = *head;
 int deletedData = temp->data;
 *head = temp->next;
 free(temp);
 printf("Deleted %d from position %d\n", deletedData, position);
 return;
 }

 // Traverse to (position - 1)th node
 struct Node* current = *head;
 for (int i = 1; i < position - 1 && current != NULL; i++) {
 current = current->next;
 }

 // Check if position is valid
 if (current == NULL || current->next == NULL) {
 printf("Invalid position\n");
 return;
 }

 // Delete node
 struct Node* temp = current->next;
 int deletedData = temp->data;
 current->next = temp->next;
 free(temp);
 printf("Deleted %d from position %d\n", deletedData, position);
}
```

### D. Delete by Value

**Algorithm:**

1. Check if list is empty
2. If head contains the value, delete from beginning
3. Traverse to find the node with the value
4. Update links and free the node

```c
void deleteByValue(struct Node** head, int value) {
 if (*head == NULL) {
 printf("List is empty\n");
 return;
 }

 // If head node contains the value
 if ((*head)->data == value) {
 struct Node* temp = *head;
 *head = temp->next;
 free(temp);
 printf("Deleted node with value %d\n", value);
 return;
 }

 // Search for the value
 struct Node* current = *head;
 while (current->next != NULL && current->next->data != value) {
 current = current->next;
 }

 // Value not found
 if (current->next == NULL) {
 printf("Value %d not found in list\n", value);
 return;
 }

 // Delete the node
 struct Node* temp = current->next;
 current->next = temp->next;
 free(temp);
 printf("Deleted node with value %d\n", value);
}
```

## 3. DISPLAY Operation

### Traversal and Display

**Algorithm:**

1. Start from head
2. While current node is not NULL:

- Print current node's data
- Move to next node

**Time Complexity:** O(n)

```c
void display(struct Node* head) {
 // Check if list is empty
 if (head == NULL) {
 printf("List is empty\n");
 return;
 }

 printf("Linked List: ");
 struct Node* current = head;
 while (current != NULL) {
 printf("%d", current->data);
 if (current->next != NULL) {
 printf(" -> ");
 }
 current = current->next;
 }
 printf(" -> NULL\n");
}
```

### Additional Display Functions

```c
// Count nodes
int countNodes(struct Node* head) {
 int count = 0;
 struct Node* current = head;
 while (current != NULL) {
 count++;
 current = current->next;
 }
 return count;
}

// Display with node count
void displayWithCount(struct Node* head) {
 display(head);
 printf("Total nodes: %d\n", countNodes(head));
}

// Display in reverse (using recursion)
void displayReverse(struct Node* head) {
 if (head == NULL) {
 return;
 }
 displayReverse(head->next);
 printf("%d ", head->data);
}
```

## Complete Program Example

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
 int data;
 struct Node* next;
};

// All insertion functions
void insertAtBeginning(struct Node** head, int data);
void insertAtEnd(struct Node** head, int data);
void insertAtPosition(struct Node** head, int data, int position);

// All deletion functions
void deleteFromBeginning(struct Node** head);
void deleteFromEnd(struct Node** head);
void deleteFromPosition(struct Node** head, int position);
void deleteByValue(struct Node** head, int value);

// Display function
void display(struct Node* head);

int main() {
 struct Node* head = NULL;
 int choice, data, position;

 while (1) {
 printf("\n=== Linked List Operations ===\n");
 printf("1. Insert at Beginning\n");
 printf("2. Insert at End\n");
 printf("3. Insert at Position\n");
 printf("4. Delete from Beginning\n");
 printf("5. Delete from End\n");
 printf("6. Delete from Position\n");
 printf("7. Delete by Value\n");
 printf("8. Display\n");
 printf("9. Exit\n");
 printf("Enter choice: ");
 scanf("%d", &choice);

 switch (choice) {
 case 1:
 printf("Enter data: ");
 scanf("%d", &data);
 insertAtBeginning(&head, data);
 break;
 case 2:
 printf("Enter data: ");
 scanf("%d", &data);
 insertAtEnd(&head, data);
 break;
 case 3:
 printf("Enter data: ");
 scanf("%d", &data);
 printf("Enter position: ");
 scanf("%d", &position);
 insertAtPosition(&head, data, position);
 break;
 case 4:
 deleteFromBeginning(&head);
 break;
 case 5:
 deleteFromEnd(&head);
 break;
 case 6:
 printf("Enter position: ");
 scanf("%d", &position);
 deleteFromPosition(&head, position);
 break;
 case 7:
 printf("Enter value to delete: ");
 scanf("%d", &data);
 deleteByValue(&head, data);
 break;
 case 8:
 display(head);
 break;
 case 9:
 printf("Exiting...\n");
 return 0;
 default:
 printf("Invalid choice\n");
 }
 }

 return 0;
}

// [Include all function definitions here]
```

## Time Complexity Summary

| Operation             | Time Complexity |
| --------------------- | --------------- |
| Insert at Beginning   | O(1)            |
| Insert at End         | O(n)            |
| Insert at Position    | O(n)            |
| Delete from Beginning | O(1)            |
| Delete from End       | O(n)            |
| Delete from Position  | O(n)            |
| Delete by Value       | O(n)            |
| Display               | O(n)            |

## Space Complexity

All operations have O(1) space complexity (excluding the list itself).

## Exam Tips

1. Understand pointer manipulation for insertion and deletion
2. Always check for NULL before dereferencing
3. Remember to free deleted nodes to prevent memory leaks
4. Know the time complexity of each operation
5. Practice drawing diagrams for each operation
6. Handle edge cases: empty list, single node, invalid position
7. Understand the difference between head pointer and double pointer (\*\*head)
8. Be able to write code without syntax errors
