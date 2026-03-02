# Operations on Linked Lists

## Fundamental Operations

Linked lists support various operations for manipulating data. Understanding these operations is crucial for working with linked lists effectively.

## 1. Creating a Node

Before performing any operation, we need to create nodes.

```c
struct Node* createNode(int data) {
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 if (newNode == NULL) {
 printf("Memory allocation failed\\n");
 exit(1);
 }
 newNode->data = data;
 newNode->next = NULL;
 return newNode;
}
```

## 2. Insertion Operations

### Insert at Beginning

**Time Complexity:** O(1)

```c
void insertAtBeginning(struct Node** head, int data) {
 struct Node* newNode = createNode(data);
 newNode->next = *head;
 *head = newNode;
}
```

### Insert at End

**Time Complexity:** O(n)

```c
void insertAtEnd(struct Node** head, int data) {
 struct Node* newNode = createNode(data);
 if (*head == NULL) {
 *head = newNode;
 return;
 }
 struct Node* temp = *head;
 while (temp->next != NULL) {
 temp = temp->next;
 }
 temp->next = newNode;
}
```

### Insert at Position

**Time Complexity:** O(n)

```c
void insertAtPosition(struct Node** head, int data, int position) {
 struct Node* newNode = createNode(data);
 if (position == 1) {
 newNode->next = *head;
 *head = newNode;
 return;
 }
 struct Node* temp = *head;
 for (int i = 1; i < position - 1 && temp != NULL; i++) {
 temp = temp->next;
 }
 if (temp == NULL) {
 printf("Invalid position\\n");
 return;
 }
 newNode->next = temp->next;
 temp->next = newNode;
}
```

## 3. Deletion Operations

### Delete from Beginning

**Time Complexity:** O(1)

```c
void deleteFromBeginning(struct Node** head) {
 if (*head == NULL) return;
 struct Node* temp = *head;
 *head = (*head)->next;
 free(temp);
}
```

### Delete from End

**Time Complexity:** O(n)

```c
void deleteFromEnd(struct Node** head) {
 if (*head == NULL) return;
 if ((*head)->next == NULL) {
 free(*head);
 *head = NULL;
 return;
 }
 struct Node* temp = *head;
 while (temp->next->next != NULL) {
 temp = temp->next;
 }
 free(temp->next);
 temp->next = NULL;
}
```

### Delete by Value

**Time Complexity:** O(n)

```c
void deleteByValue(struct Node** head, int key) {
 if (*head == NULL) return;
 if ((*head)->data == key) {
 struct Node* temp = *head;
 *head = (*head)->next;
 free(temp);
 return;
 }
 struct Node* temp = *head;
 while (temp->next != NULL && temp->next->data != key) {
 temp = temp->next;
 }
 if (temp->next == NULL) return;
 struct Node* toDelete = temp->next;
 temp->next = temp->next->next;
 free(toDelete);
}
```

## 4. Searching Operations

### Search by Value

**Time Complexity:** O(n)

```c
int search(struct Node* head, int key) {
 struct Node* current = head;
 int position = 1;
 while (current != NULL) {
 if (current->data == key) {
 return position;
 }
 current = current->next;
 position++;
 }
 return -1; // Not found
}
```

## 5. Traversal Operations

### Display List

**Time Complexity:** O(n)

```c
void display(struct Node* head) {
 if (head == NULL) {
 printf("List is empty\\n");
 return;
 }
 struct Node* temp = head;
 while (temp != NULL) {
 printf("%d -> ", temp->data);
 temp = temp->next;
 }
 printf("NULL\\n");
}
```

## 6. Utility Operations

### Count Nodes

```c
int countNodes(struct Node* head) {
 int count = 0;
 struct Node* temp = head;
 while (temp != NULL) {
 count++;
 temp = temp->next;
 }
 return count;
}
```

### Reverse List

**Time Complexity:** O(n)

```c
void reverse(struct Node** head) {
 struct Node *prev = NULL, *current = *head, *next = NULL;
 while (current != NULL) {
 next = current->next;
 current->next = prev;
 prev = current;
 current = next;
 }
 *head = prev;
}
```

## Time Complexity Summary

| Operation             | Time Complexity |
| --------------------- | --------------- |
| Insert at beginning   | O(1)            |
| Insert at end         | O(n)            |
| Insert at position    | O(n)            |
| Delete from beginning | O(1)            |
| Delete from end       | O(n)            |
| Delete by value       | O(n)            |
| Search                | O(n)            |
| Display               | O(n)            |
| Reverse               | O(n)            |

## Space Complexity

All operations have O(1) space complexity (not counting the space for the list itself).

## Exam Tips

1. Understand pointer manipulation thoroughly
2. Remember to check for NULL before operations
3. Know time complexity of each operation
4. Practice drawing step-by-step diagrams
5. Remember to free deleted nodes
6. Handle edge cases: empty list, single node
7. Understand the difference between operations on different types of linked lists
