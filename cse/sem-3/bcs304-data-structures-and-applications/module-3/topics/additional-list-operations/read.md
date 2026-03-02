# Additional Linked List Operations

## Introduction

The preceding chapters established foundational linked list operations including node creation, insertion at various positions, deletion, and traversal. This chapter extends these fundamentals to present advanced operations that are essential for solving complex computational problems efficiently. These operations form the backbone of numerous algorithms in operating systems, compiler design, and applications requiring dynamic data management. Understanding these operations with mathematical rigor prepares students for competitive programming and technical interviews.

## 1. Concatenation of Two Linked Lists

### 1.1 Theoretical Foundation

**Definition**: Given two singly linked lists L₁ and L₂, concatenation (or appending) creates a new list L such that all nodes of L₁ appear before all nodes of L₂. The operation preserves the relative order of elements within each original list.

**Theorem 1.1 (Concatenation Complexity)**: The time complexity of concatenating two linked lists of lengths n and m is O(n), where n is the length of the first list.

**Proof**: The algorithm requires traversing the entire first list to locate its last node. Since each node visit involves O(1) operations, and we must visit exactly n nodes in the worst case, the total time complexity is Θ(n). The space complexity is O(1) as we only use a constant number of pointer variables regardless of input size. ∎

### 1.2 Algorithm and Implementation

```c
struct Node* concatenate(struct Node* list1, struct Node* list2) {
    // Base case: if either list is empty
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    // Traverse to the last node of the first list
    struct Node* current = list1;
    while (current->next != NULL) {
        current = current->next;
    }

    // Append the second list
    current->next = list2;
    return list1;
}
```

### 1.3 Mathematical Analysis

**Space Complexity**: O(1) auxiliary space (three pointer variables: list1, list2, current)

**Time Complexity**: O(n) where n = |list1|

**Correctness Proof**: We prove correctness by showing that after execution, (i) all nodes of list1 remain in original order, (ii) all nodes of list2 follow list1's nodes, and (iii) no nodes are lost or duplicated.

_Lemma_: After the while loop terminates, `current` points to the last node of list1.

_Proof of Lemma_: The loop invariant states: "At the start of each iteration, `current` points to a node in list1 that has not yet been confirmed as the last node." Initially, `current` points to the head (first node). Each iteration advances `current` to its next node. The loop terminates when `current->next == NULL`, which by definition means `current` has no successor; therefore `current` is the last node. ∎

_Theorem Proof_: Following the lemma, we set `current->next = list2`, connecting the last node's next pointer to list2's head. This preserves list1's structure while attaching list2 after it. No nodes are orphaned since all pointers are maintained. ∎

---

## 2. Reversing a Linked List In-Place

### 2.1 Theoretical Foundation

**Definition**: In-place reversal transforms a linked list L = [a₁, a₂, ..., aₙ] into its reverse L' = [aₙ, aₙ₋₁, ..., a₁] by only modifying the `next` pointers, without allocating new nodes.

**Theorem 2.1 (Reversal Complexity)**: In-place reversal of a linked list of length n requires Θ(n) time and O(1) auxiliary space.

**Proof**: The algorithm visits each node exactly once in a single pass. For each of the n nodes, it performs a constant number of pointer updates (three assignments). Therefore, total time = n × O(1) = O(n). Only three pointers (prev, current, next) are used regardless of n, giving O(1) space. ∎

### 2.2 Algorithm and Implementation

```c
struct Node* reverseList(struct Node* head) {
    struct Node* prev = NULL;      // Will become new head
    struct Node* current = head;   // Node being processed
    struct Node* next = NULL;      // Temporary storage

    while (current != NULL) {
        // Step 1: Save the next node
        next = current->next;

        // Step 2: Reverse the pointer
        current->next = prev;

        // Step 3: Advance both pointers
        prev = current;
        current = next;
    }

    return prev; // prev is the new head
}
```

### 2.3 Proof of Correctness

**Loop Invariant**: At the start of each iteration, (i) `prev` points to the reversed portion containing nodes aᵢ₊₁ through aₙ, (ii) `current` points to node aᵢ which is yet to be processed, and (iii) all nodes before `prev` are correctly linked in reverse order.

_Initialization_: Before the first iteration, `prev = NULL` (empty reversed list), `current = head` (pointing to a₁). The invariant holds vacuously.

_Maintenance_: Each iteration reverses the pointer of `current` to point to `prev`, then advances both pointers. This extends the reversed portion by one node (adding aᵢ to the end of the reversed list) and maintains the invariant for the next iteration.

_Termination_: The loop terminates when `current == NULL`. At this point, `prev` points to the last processed node, which was the original first node a₁. All n nodes are now in the reversed portion, proving correctness. ∎

### 2.4 Visual Trace with Pointer States

```
Original List: [A] → [B] → [C] → [D] → NULL

Iteration 1: prev=NULL, curr=A, next=B
  After: NULL ← [A]   [B] → [C] → [D] → NULL

Iteration 2: prev=A, curr=B, next=C
  After: NULL ← [A] ← [B]   [C] → [D] → NULL

Iteration 3: prev=B, curr=C, next=D
  After: NULL ← [A] ← [B] ← [C]   [D] → NULL

Iteration 4: prev=C, curr=D, next=NULL
  After: NULL ← [A] ← [B] ← [C] ← [D]

Final: prev=D (new head)
Result: [D] → [C] → [B] → [A] → NULL
```

---

## 3. Finding the Middle Element

### 3.1 Theoretical Foundation

**Theorem 3.1 (Two-Pointer Technique)**: In a linked list of length n, a slow pointer advancing one node per iteration and a fast pointer advancing two nodes per iteration will meet at the middle node when the fast pointer reaches the end.

**Proof**: Let the slow pointer position at iteration i be sᵢ and fast pointer position be fᵢ. Starting from position 0, after i iterations: sᵢ = i, fᵢ = 2i (mod n for circular, but for linear we consider positions).

When the fast pointer reaches the end (position ≥ n-1), we have 2i ≥ n-1, giving i ≥ (n-1)/2. At this iteration, the slow pointer is at position ⌈(n-1)/2⌉, which is precisely the middle for odd n, and the second middle for even n. ∎

### 3.2 Implementation

```c
struct Node* findMiddle(struct Node* head) {
    if (head == NULL) return NULL;

    struct Node* slow = head;
    struct Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;           // Move slow by 1
        fast = fast->next->next;     // Move fast by 2
    }

    return slow; // Middle node
}
```

**Complexity Analysis**: Time: O(n), Space: O(1). The fast pointer traverses at most n/2 iterations (visiting approximately n nodes total), yielding linear time.

---

## 4. Finding nth Node from the End

### 4.1 Problem Formulation

**Definition**: Given a linked list and an integer n (1 ≤ n ≤ length of list), find the node that is n positions from the last node. This is commonly called the "n-th node from the end."

### 4.2 Two-Pointer Sliding Window

```c
struct Node* findNthFromEnd(struct Node* head, int n) {
    if (head == NULL || n <= 0) return NULL;

    struct Node* first = head;  // Leading pointer
    struct Node* second = head; // Following pointer

    // Advance first pointer by n positions
    for (int i = 0; i < n; i++) {
        if (first == NULL) return NULL; // n exceeds list length
        first = first->next;
    }

    // Move both pointers until first reaches end
    while (first != NULL) {
        first = first->next;
        second = second->next;
    }

    return second;
}
```

**Theorem 4.1**: The algorithm correctly finds the n-th node from the end in O(L-n+1) operations where L is the list length.

**Proof**: After the first loop, the distance between `first` and `second` is exactly n nodes. When `first` reaches the null (end of list), `second` has traveled L-n positions from the head, which corresponds to position L-n+1 from the end — precisely the n-th node from the end. ∎

**Complexity**: Time: O(L), Space: O(1)

---

## 5. Cycle Detection Using Floyd's Algorithm

### 5.1 Theoretical Foundation

**Definition**: A cycle exists in a linked list if there exists a node that can be reached again by following next pointers. Floyd's algorithm, also known as the Tortoise and Hare algorithm, detects cycles using two pointers moving at different speeds.

**Theorem 5.1 (Cycle Detection)**: If a cycle exists in a linked list, the slow and fast pointers (moving at speeds 1 and 2 respectively) will eventually meet inside the cycle.

**Proof**: Consider a linked list with a cycle of length C, with the fast pointer entering the cycle at position μ from the head, and the slow pointer entering at the same point after μ iterations. Within the cycle, the relative speed difference is 1 node per iteration. Starting from the same position in the cycle, the faster pointer gains 1 position on the slower pointer each iteration. After at most C iterations, the fast pointer will "lap" the slow pointer, causing them to meet. ∎

### 5.2 Implementation

```c
int detectCycle(struct Node* head) {
    if (head == NULL || head->next == NULL) return 0;

    struct Node* slow = head;  // Tortoise: moves 1 step
    struct Node* fast = head;  // Hare: moves 2 steps

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return 1; // Cycle detected
        }
    }

    return 0; // No cycle
}
```

### 5.3 Complexity Analysis

**Time Complexity**: O(n) - In the worst case, the fast pointer traverses the entire list (at most 2n node visits) before either detecting a cycle or reaching NULL.

**Space Complexity**: O(1) - Only two pointer variables are used.

**Finding Cycle Start**: Once detected, the cycle start can be found by resetting one pointer to head and moving both one step at a time until they meet again.

---

## 6. Merging Two Sorted Linked Lists

### 6.1 Problem Definition

Given two sorted linked lists L₁ and L₂, create a merged list L that contains all elements from both lists in sorted order without duplication of the original list nodes.

### 6.2 Algorithm with Proof

```c
struct Node* mergeSortedLists(struct Node* list1, struct Node* list2) {
    // Dummy node simplifies head handling
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

    // Attach remaining elements
    tail->next = (list1 != NULL) ? list1 : list2;

    return dummy.next;
}
```

**Theorem 6.1 (Merge Correctness)**: The algorithm produces a sorted merge of two sorted input lists.

_Proof by Induction on iteration count_: At each iteration, the invariant states: "The merged list in `tail` contains all previously processed elements in sorted order, and both `list1` and `list2` retain their relative ordering." The algorithm compares the first unprocessed elements of both lists and appends the smaller one, preserving sorted order. When one list is exhausted, the remaining list (which is sorted) is appended entirely, maintaining the invariant. Upon termination, all elements are processed, producing a completely sorted merge. ∎

**Complexity**: Time: O(n + m), Space: O(1)

---

## 7. Merge Sort for Linked Lists

### 7.1 Divide and Conquer Approach

Merge sort operates in three phases: (i) Find middle and split, (ii) Recursively sort halves, (iii) Merge sorted halves.

```c
struct Node* getMiddle(struct Node* head) {
    struct Node* slow = head;
    struct Node* fast = head->next; // One ahead for proper middle

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

struct Node* mergeSort(struct Node* head) {
    // Base case: 0 or 1 element
    if (head == NULL || head->next == NULL) {
        return head;
    }

    // Find middle and split
    struct Node* middle = getMiddle(head);
    struct Node* rightHalf = middle->next;
    middle->next = NULL; // Terminate left Recursively sort both half

    // halves
    struct Node* left = mergeSort(head);
    struct Node* right = mergeSort(rightHalf);

    // Merge sorted halves
    return mergeSortedLists(left, right);
}
```

### 7.2 Complexity Analysis

**Theorem 7.1**: Merge sort on linked lists has time complexity O(n log n) and space complexity O(log n) due to recursion stack.

**Proof**: The list is recursively divided halving each level, requiring log₂(n) levels. At each level, the total work in merging is Θ(n). Therefore, T(n) = 2T(n/2) + Θ(n), which by the Master Theorem yields Θ(n log n). The recursion depth is O(log n), contributing to space complexity. ∎

---

## 8. Comprehensive Comparison

| Operation       | Time Complexity | Space Complexity | Key Technique              |
| --------------- | --------------- | ---------------- | -------------------------- |
| Concatenation   | O(n)            | O(1)             | Traverse to end            |
| Reversal        | O(n)            | O(1)             | Three-pointer manipulation |
| Find Middle     | O(n)            | O(1)             | Slow-fast pointers         |
| nth from End    | O(n)            | O(1)             | Sliding window             |
| Cycle Detection | O(n)            | O(1)             | Floyd's algorithm          |
| Merge Sorted    | O(n+m)          | O(1)             | Dummy node technique       |
| Merge Sort      | O(n log n)      | O(log n)         | Divide and conquer         |

---

## 9. Practice Questions

### Question 1 (Hard - Application)

A linked list contains 2n + 1 nodes forming: head → [a₁] → [a₂] → ... → [aₙ] → [b₁] → [b₂] → ... → [bₙ] → NULL. After applying the reverse function that reverses the entire list in-place, show the sequence of pointer modifications for the first three iterations. What will be the new head pointer value after reversal?

### Question 2 (Hard - Analysis)

In Floyd's cycle detection algorithm, if the fast pointer moves k steps (k > 1) instead of 2 steps per iteration, derive the condition on k that guarantees cycle detection. What is the optimal choice of k and why?

### Question 3 (Hard - Numerical)

Two sorted linked lists contain elements [2, 5, 8, 12] and [3, 6, 9, 15, 20]. Trace through the merge algorithm step-by-step, showing the state of the dummy node and both input pointers after each comparison. How many comparisons are made in total?

### Question 4 (Hard - Proof)

Prove that after executing the findNthFromEnd algorithm with n = k, the returned pointer points to the node at position (L - k + 1) from the head, where L is the total number of nodes.
