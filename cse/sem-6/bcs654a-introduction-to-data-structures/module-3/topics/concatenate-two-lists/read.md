# Concatenating Two Linked Lists

## Introduction

Concatenation of linked lists is an important operation where two separate linked lists are joined together to form a single linked list. This operation is commonly used in various applications such as merging data, combining results, and building larger data structures.

**Definition:** List concatenation is the operation of joining the end of one linked list to the beginning of another linked list.

## Concept

Given two linked lists:

- **List 1:** 10 → 20 → 30 → NULL
- **List 2:** 40 → 50 → 60 → NULL

After concatenation:

- **Result:** 10 → 20 → 30 → 40 → 50 → 60 → NULL

## Node Structure

```c
struct Node {
 int data;
 struct Node* next;
};
```

## Algorithm

### Algorithm: Concatenate Two Linked Lists

**Input:**

- head1: pointer to the first node of List 1
- head2: pointer to the first node of List 2

**Output:**

- Pointer to the concatenated list

**Steps:**

1. **Check if List 1 is empty**

- If head1 is NULL, return head2
- This means List 2 becomes the result

2. **Traverse to the last node of List 1**

- Start from head1
- Move to the next node until next is NULL
- Keep track of the current node

3. **Link the last node of List 1 to the first node of List 2**

- Set the next pointer of last node of List 1 to head2

4. **Return head1**

- This is the head of the concatenated list

## Implementation

### Method 1: Simple Concatenation

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
 int data;
 struct Node* next;
};

// Function to concatenate two linked lists
struct Node* concatenate(struct Node* head1, struct Node* head2) {
 // If first list is empty, return second list
 if (head1 == NULL) {
 return head2;
 }

 // If second list is empty, return first list
 if (head2 == NULL) {
 return head1;
 }

 // Traverse to the last node of first list
 struct Node* current = head1;
 while (current->next != NULL) {
 current = current->next;
 }

 // Link the last node of first list to first node of second list
 current->next = head2;

 // Return the head of first list
 return head1;
}

// Helper function to create a new node
struct Node* createNode(int data) {
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 newNode->data = data;
 newNode->next = NULL;
 return newNode;
}

// Helper function to print linked list
void printList(struct Node* head) {
 struct Node* current = head;
 while (current != NULL) {
 printf("%d ", current->data);
 if (current->next != NULL) {
 printf("-> ");
 }
 current = current->next;
 }
 printf("-> NULL\n");
}
```

### Method 2: Using Tail Pointer (Optimized)

If you maintain a tail pointer for each list, concatenation becomes O(1):

```c
struct LinkedList {
 struct Node* head;
 struct Node* tail;
 int size;
};

// Optimized concatenation with tail pointer
struct LinkedList* concatenateOptimized(struct LinkedList* list1,
 struct LinkedList* list2) {
 if (list1->head == NULL) {
 return list2;
 }

 if (list2->head == NULL) {
 return list1;
 }

 // Link tail of first list to head of second list
 list1->tail->next = list2->head;

 // Update tail of first list
 list1->tail = list2->tail;

 // Update size
 list1->size += list2->size;

 return list1;
}
```

### Method 3: Recursive Concatenation

```c
struct Node* concatenateRecursive(struct Node* head1, struct Node* head2) {
 // Base case: if first list is empty
 if (head1 == NULL) {
 return head2;
 }

 // Recursive case: concatenate rest of list1 with list2
 head1->next = concatenateRecursive(head1->next, head2);

 return head1;
}
```

## Complete Example Program

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
 int data;
 struct Node* next;
};

// Create a new node
struct Node* createNode(int data) {
 struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
 if (newNode == NULL) {
 printf("Memory allocation failed\n");
 exit(1);
 }
 newNode->data = data;
 newNode->next = NULL;
 return newNode;
}

// Insert at end
void insertAtEnd(struct Node** head, int data) {
 struct Node* newNode = createNode(data);

 if (*head == NULL) {
 *head = newNode;
 return;
 }

 struct Node* current = *head;
 while (current->next != NULL) {
 current = current->next;
 }
 current->next = newNode;
}

// Concatenate two lists
struct Node* concatenate(struct Node* head1, struct Node* head2) {
 if (head1 == NULL) return head2;
 if (head2 == NULL) return head1;

 struct Node* current = head1;
 while (current->next != NULL) {
 current = current->next;
 }
 current->next = head2;

 return head1;
}

// Print list
void printList(struct Node* head) {
 struct Node* current = head;
 while (current != NULL) {
 printf("%d", current->data);
 if (current->next != NULL) printf(" -> ");
 current = current->next;
 }
 printf(" -> NULL\n");
}

int main() {
 struct Node* list1 = NULL;
 struct Node* list2 = NULL;

 // Create first list: 10 -> 20 -> 30
 insertAtEnd(&list1, 10);
 insertAtEnd(&list1, 20);
 insertAtEnd(&list1, 30);

 // Create second list: 40 -> 50 -> 60
 insertAtEnd(&list2, 40);
 insertAtEnd(&list2, 50);
 insertAtEnd(&list2, 60);

 printf("List 1: ");
 printList(list1);

 printf("List 2: ");
 printList(list2);

 // Concatenate lists
 struct Node* result = concatenate(list1, list2);

 printf("Concatenated List: ");
 printList(result);

 return 0;
}
```

## Time and Space Complexity

### Time Complexity:

- **Simple method:** O(n) where n is the length of the first list
- We traverse the entire first list to find the last node
- **With tail pointer:** O(1)
- Direct access to the last node

### Space Complexity:

- **Iterative:** O(1) - only uses a few pointers
- **Recursive:** O(n) - due to recursion stack for first list

## Variations and Applications

### 1. Concatenate and Sort

```c
struct Node* concatenateAndSort(struct Node* head1, struct Node* head2) {
 struct Node* result = concatenate(head1, head2);
 // Apply sorting algorithm (e.g., merge sort)
 return mergeSort(result);
}
```

### 2. Concatenate Multiple Lists

```c
struct Node* concatenateMultiple(struct Node* lists[], int n) {
 if (n == 0) return NULL;

 struct Node* result = lists[0];
 for (int i = 1; i < n; i++) {
 result = concatenate(result, lists[i]);
 }
 return result;
}
```

### 3. Concatenate with Removing Duplicates

```c
struct Node* concatenateUnique(struct Node* head1, struct Node* head2) {
 struct Node* result = concatenate(head1, head2);
 removeDuplicates(result);
 return result;
}
```

## Important Points

1. **Check for NULL lists:**

- Handle cases where one or both lists are empty
- Return the non-empty list if one is NULL

2. **Preserve original lists:**

- The simple concatenation modifies the first list
- If you need to preserve originals, create copies first

3. **Memory management:**

- No new nodes are created in simple concatenation
- Both lists share nodes after concatenation
- Be careful when freeing memory

4. **Circular lists:**

- Special handling needed for circular linked lists
- Must break the circle before concatenation

## Common Mistakes to Avoid

1. **Not handling NULL cases**

```c
// BAD - will crash if head1 is NULL
current->next = head2;

// GOOD - check first
if (head1 == NULL) return head2;
```

2. **Losing reference to second list**

```c
// BAD - loses head2 reference
head2 = concatenate(head1, head2);

// GOOD - use result variable
struct Node* result = concatenate(head1, head2);
```

3. **Not reaching the last node**

```c
// BAD - stops one node early
while (current->next->next != NULL)

// GOOD
while (current->next != NULL)
```

## Exam Tips

1. Remember to check for NULL pointers before concatenation
2. Understand the time complexity: O(n) for simple method
3. Know how to optimize using tail pointer to O(1)
4. Be able to write both iterative and recursive versions
5. Practice drawing diagrams showing the concatenation process
6. Remember that concatenation modifies the first list
7. Understand how this differs from merging sorted lists
