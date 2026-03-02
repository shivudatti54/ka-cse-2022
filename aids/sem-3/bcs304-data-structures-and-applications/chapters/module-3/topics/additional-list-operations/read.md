# Advanced Linked List Operations

## Introduction to Advanced Operations

In the previous sections, we covered basic linked list operations like insertion, deletion, and display. Advanced operations build upon these fundamentals to solve more complex problems efficiently. These operations are crucial for optimizing performance and implementing sophisticated data structures.

## Concatenating Two Linked Lists

Concatenation combines two linked lists by appending the second list to the end of the first list.

### Algorithm for Concatenation

1. Check if the first list is empty - if so, return the second list
2. Traverse to the end of the first list
3. Set the next pointer of the last node of the first list to point to the head of the second list
4. Return the head of the first list

### Implementation Example

```c
struct Node* concatenate(struct Node* list1, struct Node* list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    struct Node* temp = list1;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = list2;
    return list1;
}
```

### Visual Representation

```
List 1: [A] → [B] → [C] → NULL
List 2: [X] → [Y] → [Z] → NULL

After concatenation:
[A] → [B] → [C] → [X] → [Y] → [Z] → NULL
```

## Reversing a Linked List Without Creating New Nodes

Reversing a linked list is a fundamental operation that rearranges the pointers to reverse the order of elements.

### In-Place Reversal Algorithm

The iterative approach uses three pointers: previous, current, and next.

```c
struct Node* reverseList(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* current = head;
    struct Node* next = NULL;

    while (current != NULL) {
        next = current->next;  // Store next node
        current->next = prev;  // Reverse current node's pointer
        prev = current;        // Move pointers one position ahead
        current = next;
    }
    return prev;  // prev becomes the new head
}
```

### Step-by-Step Visualization

```
Original: [A] → [B] → [C] → [D] → NULL

Step 1: NULL ← [A]   [B] → [C] → [D] → NULL
Step 2: NULL ← [A] ← [B]   [C] → [D] → NULL
Step 3: NULL ← [A] ← [B] ← [C]   [D] → NULL
Step 4: NULL ← [A] ← [B] ← [C] ← [D]

Final: [D] → [C] → [B] → [A] → NULL
```

## Detecting Cycles in Linked Lists

Cycle detection is crucial for preventing infinite loops and ensuring data integrity.

### Floyd's Cycle-Finding Algorithm (Tortoise and Hare)

This algorithm uses two pointers moving at different speeds to detect cycles efficiently.

```c
int hasCycle(struct Node* head) {
    if (head == NULL) return 0;

    struct Node* slow = head;
    struct Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;         // Move slow pointer by one
        fast = fast->next->next;    // Move fast pointer by two

        if (slow == fast) {
            return 1;  // Cycle detected
        }
    }
    return 0;  // No cycle found
}
```

### Cycle Detection Example

```
List with cycle: [A] → [B] → [C] → [D] → [E] → [C] (back to C)

Slow pointer path: A → B → C → D → E → C → D → E → C...
Fast pointer path: A → C → E → D → C → E → D → C...

They meet at node C after several iterations.
```

## Finding the Middle Element

Finding the middle element efficiently is useful for various algorithms like merge sort on linked lists.

### Two-Pointer Technique

```c
struct Node* findMiddle(struct Node* head) {
    if (head == NULL) return NULL;

    struct Node* slow = head;
    struct Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

### Example Execution

```
List: [A] → [B] → [C] → [D] → [E] → NULL

Iteration 1: slow at B, fast at C
Iteration 2: slow at C, fast at E
Fast->next is NULL, so middle is C

List: [A] → [B] → [C] → [D] → NULL

Iteration 1: slow at B, fast at C
Iteration 2: slow at C, fast at NULL
Middle is C (second middle for even length)
```

## Merging Two Sorted Linked Lists

Merging is fundamental for algorithms like merge sort and combining sorted data.

### Merge Algorithm

```c
struct Node* mergeSortedLists(struct Node* list1, struct Node* list2) {
    // Create a dummy node to simplify code
    struct Node dummy;
    struct Node* tail = &dummy;
    dummy.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1->data <= list2->data) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // Append remaining nodes
    if (list1 != NULL) tail->next = list1;
    if (list2 != NULL) tail->next = list2;

    return dummy.next;
}
```

### Merge Process Visualization

```
List 1: [1] → [3] → [5] → NULL
List 2: [2] → [4] → [6] → NULL

Step 1: Compare 1 and 2 → Add 1
Step 2: Compare 3 and 2 → Add 2
Step 3: Compare 3 and 4 → Add 3
Step 4: Compare 5 and 4 → Add 4
Step 5: Add remaining: 5 → 6

Result: [1] → [2] → [3] → [4] → [5] → [6] → NULL
```

## Sorting Linked Lists Using Merge Sort

Merge sort is particularly efficient for linked lists due to its O(n log n) time complexity and minimal memory overhead.

### Implementation Steps

1. **Split**: Find middle and divide list into two halves
2. **Recursively sort**: Both halves
3. **Merge**: The two sorted halves

```c
struct Node* mergeSort(struct Node* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }

    // Find middle and split
    struct Node* middle = findMiddle(head);
    struct Node* nextOfMiddle = middle->next;
    middle->next = NULL;

    // Recursively sort both halves
    struct Node* left = mergeSort(head);
    struct Node* right = mergeSort(nextOfMiddle);

    // Merge sorted halves
    return mergeSortedLists(left, right);
}
```

## Static Allocation vs Linked Allocation

| Aspect                 | Static Allocation (Arrays)   | Linked Allocation (Linked Lists)   |
| ---------------------- | ---------------------------- | ---------------------------------- |
| **Memory Usage**       | Fixed size, may waste memory | Dynamic size, efficient memory use |
| **Insertion/Deletion** | O(n) time complexity         | O(1) at beginning, O(n) elsewhere  |
| **Memory Allocation**  | Compile-time                 | Run-time                           |
| **Access Time**        | O(1) random access           | O(n) sequential access             |
| **Memory Overhead**    | No extra memory              | Extra memory for pointers          |
| **Flexibility**        | Fixed capacity               | Grows/shrinks as needed            |

## Implementation of Stacks and Queues Using Linked Lists

### Stack Implementation

```c
// Push operation
void push(struct Node** top, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *top;
    *top = newNode;
}

// Pop operation
int pop(struct Node** top) {
    if (*top == NULL) return -1; // Stack underflow
    struct Node* temp = *top;
    int data = temp->data;
    *top = (*top)->next;
    free(temp);
    return data;
}
```

### Queue Implementation

```c
// Enqueue operation
void enqueue(struct Node** front, struct Node** rear, int data) {
    struct Node* newNode = createNode(data);
    if (*rear == NULL) {
        *front = *rear = newNode;
    } else {
        (*rear)->next = newNode;
        *rear = newNode;
    }
}

// Dequeue operation
int dequeue(struct Node** front, struct Node** rear) {
    if (*front == NULL) return -1; // Queue underflow
    struct Node* temp = *front;
    int data = temp->data;
    *front = (*front)->next;
    if (*front == NULL) *rear = NULL;
    free(temp);
    return data;
}
```

## Exam Tips

1. **Pointer Manipulation**: Practice drawing diagrams to visualize pointer changes during operations like reversal
2. **Edge Cases**: Always consider empty lists, single-node lists, and lists with cycles
3. **Time Complexity**: Memorize the time complexities of common operations:
   - Access: O(n)
   - Search: O(n)
   - Insertion/Deletion at beginning: O(1)
   - Insertion/Deletion at end: O(n)
4. **Memory Management**: Remember to free allocated memory after operations to prevent memory leaks
5. **Two-Pointer Techniques**: Master the fast-slow pointer approach for cycle detection and finding middle elements
6. **Recursive vs Iterative**: Understand when to use recursive approaches (e.g., reversal) vs iterative approaches
