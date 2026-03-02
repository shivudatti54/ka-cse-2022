# Data Structure Operations


## Table of Contents

- [Data Structure Operations](#data-structure-operations)
- [Introduction](#introduction)
- [1. Traversal Operation](#1-traversal-operation)
  - [1.1 Definition and Significance](#11-definition-and-significance)
  - [1.2 Traversal of Linear Arrays](#12-traversal-of-linear-arrays)
  - [1.3 Time Complexity Analysis for Traversal](#13-time-complexity-analysis-for-traversal)
  - [1.4 Traversal of Singly Linked List](#14-traversal-of-singly-linked-list)
- [2. Searching Operations](#2-searching-operations)
  - [2.1 Linear Search (Sequential Search)](#21-linear-search-sequential-search)
  - [2.2 Binary Search](#22-binary-search)
- [3. Insertion Operation](#3-insertion-operation)
  - [3.1 Insertion in Arrays](#31-insertion-in-arrays)
  - [3.2 Insertion in Singly Linked List](#32-insertion-in-singly-linked-list)
- [4. Deletion Operation](#4-deletion-operation)
  - [4.1 Deletion in Arrays](#41-deletion-in-arrays)
  - [4.2 Deletion in Singly Linked List](#42-deletion-in-singly-linked-list)
- [5. Sorting Operation](#5-sorting-operation)
  - [5.1 Bubble Sort](#51-bubble-sort)
  - [5.2 Merge Sort (Divide and Conquer Approach)](#52-merge-sort-divide-and-conquer-approach)
- [6. Merging Operation](#6-merging-operation)
  - [6.1 Algorithm Description](#61-algorithm-description)
  - [6.2 Complexity Analysis](#62-complexity-analysis)
- [Summary Table: Operation Complexities](#summary-table-operation-complexities)
- [Multiple Choice Questions](#multiple-choice-questions)

## Introduction

Data structures provide the fundamental mechanisms for organizing, storing, and manipulating data efficiently in computational systems. Regardless of the specific implementation—whether array, linked list, tree, or graph—a **common set of fundamental operations** can be performed on any data structure. Understanding these operations and analyzing their computational efficiency (both time and space complexity) is essential to the study of data structures and algorithm design.

The six fundamental operations that form the backbone of data structure manipulations are:

1. **Traversal** — Systematically accessing each element exactly once to process or inspect it.
2. **Searching** — Locating a specific element or determining its absence from the structure.
3. **Insertion** — Adding a new element to the structure at a specified position.
4. **Deletion** — Removing an existing element from the structure.
5. **Sorting** — Arranging elements in a specified order (ascending or descending).
6. **Merging** — Combining two or more sorted structures into a single sorted structure.

This chapter provides a comprehensive analysis of each operation, examining algorithmic approaches, correctness proofs, and rigorous time complexity analysis essential for standard-level engineering and students.

---

## 1. Traversal Operation

### 1.1 Definition and Significance

**Traversal** is defined as the systematic process of visiting every element of a data structure exactly once in a predetermined sequence without repetition or omission. The purpose of traversal is to perform operations such as printing, counting, summing, searching, or any user-defined processing on each element.

Traversal serves as a foundational operation upon which many complex algorithms are built. It is often the first step in more sophisticated operations like searching, sorting, and merging.

### 1.2 Traversal of Linear Arrays

For a linear array of `n` elements indexed from `0` to `n-1`, the simplest traversal approach utilizes iterative access through sequential memory locations.

**Algorithm (Array Traversal):**

```
procedure TRAVERSE(arr[0...n-1])
 for i ← 0 to n-1 do
 process arr[i]
 end for
end procedure
```

**C Implementation:**

```c
#include <stdio.h>

void traverse(int arr[], int n) {
    printf("Array elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = 5;
    traverse(arr, n);
    return 0;
}
```

**Output:** `Array elements: 10 20 30 40 50`

### 1.3 Time Complexity Analysis for Traversal

**Theorem:** The time complexity of traversing an array of `n` elements is Θ(n).

**Proof:** The traversal algorithm executes a single loop that iterates exactly `n` times. Within each iteration, a constant-time operation (accessing and processing arr[i]) is performed. Therefore:

$$T(n) = c \cdot n = \Theta(n)$$

where `c` represents the constant time for processing each element. This linear relationship holds for both best-case (first element processed), average-case, and worst-case scenarios, as all `n` elements must be visited.

### 1.4 Traversal of Singly Linked List

In a linked list, elements are stored in nodes dispersed throughout memory, connected through pointers. Traversal requires following these pointers sequentially.

**C Implementation:**

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void traverseList(struct Node* head) {
    struct Node* current = head;
    printf("Linked List: ");
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
```

**Time Complexity:** O(n) — Each node is visited exactly once by following the `next` pointers.

---

## 2. Searching Operations

**Searching** is the process of determining whether a specific element (termed the "key" or "target") exists within a data structure and, if found, returning its location or a reference to it. The efficiency of searching algorithms is critical in database systems, information retrieval, and computational applications.

### 2.1 Linear Search (Sequential Search)

#### 2.1.1 Algorithm Description

Linear search is the most straightforward searching technique, applicable to both sorted and unsorted data. The algorithm examines each element sequentially from the beginning until either the target is found or the entire structure is exhausted.

**Algorithm:**

```
procedure LINEAR_SEARCH(arr[0...n-1], key)
 for i ← 0 to n-1 do
 if arr[i] = key then
 return i
 end if
 end for
 return -1
end procedure
```

#### 2.1.2 Implementation

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;
        }
    }
    return -1;
}
```

#### 2.1.3 Comprehensive Complexity Analysis

**Theorem:** The time complexity of linear search is O(n).

**Proof by Case Analysis:**

| Case        | Condition                         | Comparisons | Complexity |
| ----------- | --------------------------------- | ----------- | ---------- |
| **Best**    | Target at index 0                 | 1           | Θ(1)       |
| **Average** | Target uniformly distributed      | n/2         | Θ(n)       |
| **Worst**   | Target at last position or absent | n           | Θ(n)       |

For the average case, assuming uniform distribution:
$$E[comparisons] = \frac{1}{n} \sum_{i=1}^{n} i = \frac{n+1}{2} = \Theta(n)$$

### 2.2 Binary Search

#### 2.2.1 Prerequisites and Algorithm Description

Binary search is applicable only to **sorted arrays** and achieves logarithmic time complexity by repeatedly dividing the search interval in half.

**Algorithm:**

```
procedure BINARY_SEARCH(arr[0...n-1], key)
 low ← 0
 high ← n - 1
 while low ≤ high do
 mid ← floor((low + high) / 2)
 if arr[mid] = key then
 return mid
 else if arr[mid] < key then
 low ← mid + 1
 else
 high ← mid - 1
 end if
 end while
 return -1
end procedure
```

#### 2.2.2 Time Complexity Analysis Using Recurrence Relation

**Theorem:** The time complexity of binary search is Θ(log n).

**Proof:** Let T(n) denote the number of comparisons required to search in an array of size n. Each iteration performs one comparison and reduces the problem size to approximately n/2. Thus:

$$T(n) = T(n/2) + 1$$

Solving this recurrence relation:

- Using iteration method: T(n) = T(n/2^k) + k
- When n/2^k = 1, we have k = log₂n
- Therefore: T(n) = T(1) + log₂n = Θ(log n)

By the Master Theorem, where a=1, b=2, f(n)=1, we have n^(log_b a) = n^0 = 1, and f(n) = Θ(1) = Θ(n^(log_b a) · log^k n) with k=0, confirming T(n) = Θ(log n).

#### 2.2.3 Comparative Analysis

| Algorithm     | Time (Best) | Time (Average) | Time (Worst) | Space | Prerequisite |
| ------------- | ----------- | -------------- | ------------ | ----- | ------------ |
| Linear Search | Θ(1)        | Θ(n)           | Θ(n)         | O(1)  | None         |
| Binary Search | Θ(1)        | Θ(log n)       | Θ(log n)     | O(1)  | Sorted array |

---

## 3. Insertion Operation

**Insertion** involves adding a new element to the data structure. The complexity varies significantly based on the data structure type and insertion position.

### 3.1 Insertion in Arrays

#### 3.1.1 Algorithm Description

Insertion at the end of an array is O(1), while insertion at the beginning requires shifting all elements.

**Algorithm for Insertion at Position i:**

```
procedure INSERT_ARRAY(arr[0...n-1], position, element)
 if n = MAX_SIZE then
 return ERROR // Overflow
 end if
 for j ← n-1 down to position do
 arr[j+1] ← arr[j]
 end for
 arr[position] ← element
 n ← n + 1
end procedure
```

#### 3.1.2 Complexity Analysis

**Theorem:** Time complexity of inserting an element at position `k` in an array of size `n` is Θ(n-k).

**Proof:** The algorithm shifts elements from position `k` through `n-1` one position to the right. The number of shifts equals n-k. All other operations (assignment, index checks) are constant time. Therefore, T(n,k) = c·(n-k) = Θ(n-k).

| Insertion Position | Shifts Required | Complexity |
| ------------------ | --------------- | ---------- |
| End (k = n)        | 0               | Θ(1)       |
| Beginning (k = 0)  | n               | Θ(n)       |
| Average (k = n/2)  | n/2             | Θ(n)       |

### 3.2 Insertion in Singly Linked List

#### 3.2.1 Algorithm for Insertion at Beginning

```c
struct Node* insertAtBeginning(struct Node* head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = head;
    return newNode;
}
```

**Time Complexity:** O(1) — Constant time as only pointer rearrangement is required.

#### 3.2.2 Algorithm for Insertion at End

```c
void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;

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

**Time Complexity:** O(n) — Requires traversal to find the last node.

---

## 4. Deletion Operation

**Deletion** involves removing an existing element from the data structure. Similar to insertion, the complexity depends on the data structure and deletion position.

### 4.1 Deletion in Arrays

**Algorithm:**

```
procedure DELETE_ARRAY(arr[0...n-1], position)
 if position < 0 or position ≥ n then
 return ERROR // Invalid position
 end if
 element ← arr[position]
 for j ← position to n-2 do
 arr[j] ← arr[j+1]
 end for
 n ← n - 1
 return element
end procedure
```

**Time Complexity:** Θ(n - position) — Shifting elements left to fill the gap.

### 4.2 Deletion in Singly Linked List

#### 4.2.1 Deletion from Beginning

```c
struct Node* deleteFromBeginning(struct Node* head) {
    if (head == NULL) return NULL;
    struct Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}
```

**Time Complexity:** O(1)

#### 4.2.2 Deletion from End

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

**Time Complexity:** O(n)

---

## 5. Sorting Operation

**Sorting** arranges elements in a specified order (ascending or descending). Sorting algorithms are fundamental to computer science with applications in database management, search optimization, and data analysis.

### 5.1 Bubble Sort

#### 5.1.1 Algorithm Description

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

**Algorithm:**

```
procedure BUBBLE_SORT(arr[0...n-1])
 for i ← 0 to n-2 do
 swapped ← false
 for j ← 0 to n-2-i do
 if arr[j] > arr[j+1] then
 swap(arr[j], arr[j+1])
 swapped ← true
 end if
 end for
 if not swapped then
 break
 end if
 end for
end procedure
```

#### 5.1.2 Complexity Analysis

**Theorem:** The time complexity of bubble sort is Θ(n²).

**Proof:** The outer loop runs n-1 times. For each iteration i of the outer loop, the inner loop performs n-1-i comparisons. Total comparisons:

$$\sum_{i=0}^{n-2} (n-1-i) = \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2} = \Theta(n^2)$$

| Case    | Complexity | Explanation                                     |
| ------- | ---------- | ----------------------------------------------- |
| Best    | Θ(n)       | Array already sorted; one pass detects no swaps |
| Average | Θ(n²)      | Approximately n²/2 comparisons and swaps        |
| Worst   | Θ(n²)      | Array in reverse order                          |

**Space Complexity:** O(1) — In-place sorting algorithm.

### 5.2 Merge Sort (Divide and Conquer Approach)

#### 5.2.1 Algorithm Description

Merge sort divides the array into halves, recursively sorts each half, and merges the sorted halves.

**Algorithm:**

```
procedure MERGE_SORT(arr, left, right)
 if left < right then
 mid ← floor((left + right) / 2)
 MERGE_SORT(arr, left, mid)
 MERGE_SORT(arr, mid+1, right)
 MERGE(arr, left, mid, right)
 end if
end procedure
```

#### 5.2.2 Time Complexity Analysis Using Recurrence

**Theorem:** The time complexity of merge sort is Θ(n log n).

**Proof:** The recurrence relation is:
$$T(n) = 2T(n/2) + \Theta(n)$$

Using the Master Theorem: a=2, b=2, f(n)=n

- n^(log_b a) = n^(log_2 2) = n¹
- f(n) = Θ(n) matches case 2 of Master Theorem
- Therefore: T(n) = Θ(n log n)

---

## 6. Merging Operation

**Merging** combines two or more sorted structures into a single sorted structure. This operation is fundamental to the merge sort algorithm and external sorting techniques.

### 6.1 Algorithm Description

```
procedure MERGE(arr, left, mid, right)
 L ← arr[left...mid]
 R ← arr[mid+1...right]
 i ← 0, j ← 0, k ← left
 while i < length(L) and j < length(R) do
 if L[i] ≤ R[j] then
 arr[k] ← L[i]; i ← i + 1
 else
 arr[k] ← R[j]; j ← j + 1
 end if
 k ← k + 1
 end while
 copy remaining elements of L
 copy remaining elements of R
end procedure
```

### 6.2 Complexity Analysis

**Theorem:** The time complexity of merging two sorted arrays of sizes n₁ and n₂ is Θ(n₁ + n₂).

**Proof:** Each element from both arrays is compared and copied exactly once. The while loop executes min(n₁, n₂) times, and the remaining elements from the non-exhausted array are copied in constant time proportional to the remaining count. Total operations: n₁ + n₂ = Θ(n₁ + n₂).

---

## Summary Table: Operation Complexities

| Operation | Array (Best) | Array (Worst) | Linked List (Best) | Linked List (Worst) |
| --------- | ------------ | ------------- | ------------------ | ------------------- |
| Traversal | Θ(n)         | Θ(n)          | Θ(n)               | Θ(n)                |
| Search    | Θ(1)         | Θ(n)          | Θ(n)               | Θ(n)                |
| Insertion | Θ(1)         | Θ(n)          | Θ(1)               | Θ(n)                |
| Deletion  | Θ(1)         | Θ(n)          | Θ(1)               | Θ(n)                |
| Sorting   | Θ(n log n)   | Θ(n²)         | Θ(n log n)         | Θ(n²)               |

---

## Multiple Choice Questions

**Question 1:** For a linear search algorithm applied to an array of 1000 elements, what is the maximum number of comparisons required in the worst case?

(A) 500  
(B) 999  
(C) 1000  
(D) 1001

**Answer:** (C) 1000  
**Explanation:** In the worst case of linear search, the target element is at the last position or not present. The algorithm must compare all 1000 elements before concluding the search, requiring exactly 1000 comparisons.

---

**Question 2:** What is the time complexity of inserting an element at the beginning of a singly linked list of size n?

(A) Θ(1)  
(B) Θ(n)  
(C) Θ(n²)  
(D) Θ(log n)

**Answer:** (A) Θ(1)  
**Explanation:** Insertion at the beginning of a singly linked list requires only creating a new node and updating the head pointer. No traversal is needed regardless of list size, making it a constant-time operation Θ(1).

---

**Question 3:** Using binary search on a sorted array of 2048 elements, what is the maximum number of iterations needed to find any element?

(A) 10  
(B) 11  
(C) 12  
(D) 2048

**Answer:** (B) 11  
**Explanation:** Binary search has a time complexity of Θ(log₂n). For n = 2048 = 2¹¹, log₂(2048) = 11. Therefore, at most 11 comparisons (iterations) are required, as the search space is halved each iteration.

---

**Question 4:** In bubble sort, if the input array is already sorted in ascending order, what is the time complexity?

(A) Θ(n)  
(B) Θ(n log n)  
(C) Θ(n²)  
(D) Θ(1)

**Answer:** (A) Θ(n)  
**Explanation:** With the optimization of early termination when no swaps occur, bubble sort makes exactly one pass through the array (n-1 comparisons), detects no swaps, and terminates. This results in best-case time complexity of Θ(n).

---

**Question 5:** Two sorted arrays of sizes 500 and 700 are merged. What is the time complexity of this merge operation?

(A) Θ(500)  
(B) Θ(700)  
(C) Θ(1200)  
(D) Θ(500 × 700)

**Answer:** (C) Θ(1200)  
**Explanation:** Merging two sorted arrays of sizes n₁ and n₂ requires Θ(n₁ + n₂) time. Here, 500 + 700 = 1200, giving Θ(1200) or simply Θ(n) where n = n₁ + n₂.
