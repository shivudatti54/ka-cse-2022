**9.1 Introduction to Linked Lists**

### Definition and Basic Concept

A linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next element. This structure allows for efficient insertion and deletion of elements at any position in the list.

### Advantages of Linked Lists

• **Efficient Insertion and Deletion**: Linked lists allow for efficient insertion and deletion of elements at any position, without having to shift all the elements after the insertion or deletion point.
• **Dynamic Memory Allocation**: Linked lists can grow or shrink dynamically as elements are added or removed.
• **Flexible Data Structure**: Linked lists can be used to implement various data structures, such as stacks, queues, and trees.

### Disadvantages of Linked Lists

• **Extra Memory Required**: Each element in a linked list requires extra memory to store the pointer to the next element.
• **Slow Search**: Searching for a specific element in a linked list can be slow, especially for large lists.

### Terminology

• **Node**: A node is the basic unit of a linked list, consisting of data and a pointer to the next node.
• **Head**: The head of a linked list is the first node in the list.
• **Tail**: The tail of a linked list is the last node in the list.

### Example of a Linked List

Suppose we have a linked list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

In this example, the first node has a pointer to the second node, the second node has a pointer to the third node, and so on.

### 9.2 Operations on Linked Lists

#### Insertion

Insertion in a linked list involves adding a new node at a specific position in the list. There are two types of insertion:

• **Insertion at the beginning**: Inserting a new node at the beginning of the list.
• **Insertion at the end**: Inserting a new node at the end of the list.

**Example of Insertion at the Beginning**

Suppose we have a linked list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

We want to insert a new node with value 0 at the beginning of the list.

```
0 -> 1 -> 2 -> 3 -> 4 -> 5
```

In this example, we created a new node with value 0 and inserted it at the beginning of the list.

**Example of Insertion at the End**

Suppose we have a linked list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

We want to insert a new node with value 6 at the end of the list.

```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

In this example, we created a new node with value 6 and inserted it at the end of the list.

#### Deletion

Deletion in a linked list involves removing a node at a specific position in the list. There are two types of deletion:

• **Deletion at the beginning**: Deleting the first node in the list.
• **Deletion at the end**: Deleting the last node in the list.

**Example of Deletion at the Beginning**

Suppose we have a linked list with the following nodes:

```
0 -> 1 -> 2 -> 3 -> 4 -> 5
```

We want to delete the first node with value 0.

```
1 -> 2 -> 3 -> 4 -> 5
```

In this example, we deleted the first node with value 0 from the list.

**Example of Deletion at the End**

Suppose we have a linked list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

We want to delete the last node with value 5.

```
1 -> 2 -> 3 -> 4
```

In this example, we deleted the last node with value 5 from the list.

### 9.3 Self-Referential Structures

A self-referential structure is a data structure that contains pointers to its own nodes. This allows for efficient manipulation of the structure, such as inserting or deleting nodes.

#### Definition

A self-referential structure is a data structure that contains a pointer to its own nodes. This allows for efficient manipulation of the structure, such as inserting or deleting nodes.

#### Examples of Self-Referential Structures

• **Linked List**: A linked list is a self-referential structure, as each node contains a pointer to the next node.
• **Tree**: A tree is a self-referential structure, as each node contains a pointer to its children.
• **Graph**: A graph is a self-referential structure, as each node contains a pointer to its neighbors.

### 9.3.1 Properties of Self-Referential Structures

• **Efficient Insertion and Deletion**: Self-referential structures allow for efficient insertion and deletion of nodes, as the structure itself contains pointers to its own nodes.
• **Flexible Data Structure**: Self-referential structures can be used to implement various data structures, such as trees and graphs.

### 9.3.11 Merge Sort Algorithm

The merge sort algorithm is a divide-and-conquer algorithm that uses self-referential structures to sort data.

#### Definition

The merge sort algorithm is a divide-and-conquer algorithm that uses self-referential structures to sort data.

#### Example

Suppose we have a linked list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

We want to sort the data using the merge sort algorithm.

```
1 -> 2 -> 3 -> 4 -> 5
```

In this example, we used the merge sort algorithm to sort the data in ascending order.

#### Pseudocode

```
MergeSort(arr) {
  if arr.length <= 1 {
    return arr
  }
  mid = arr.length / 2
  left = MergeSort(arr[0..mid-1])
  right = MergeSort(arr[mid..arr.length-1])
  return Merge(left, right)
}

Merge(left, right) {
  result = []
  while left.length > 0 && right.length > 0 {
    if left[0] < right[0] {
      result = result + [left[0]]
      left = left[1..]
    } else {
      result = result + [right[0]]
      right = right[1..]
    }
  }
  result = result + left
  result = result + right
  return result
}
```

In this pseudocode, we used a recursive approach to sort the data. We divided the data into two halves, sorted each half recursively, and then merged the two sorted halves into a single sorted list.

### 9.3.12 Fibonacci Series Generation

The Fibonacci series is a self-referential structure that can be used to generate a sequence of numbers.

#### Definition

The Fibonacci series is a self-referential structure that can be used to generate a sequence of numbers.

#### Example

Suppose we want to generate the Fibonacci series up to the 10th term.

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

In this example, we used the Fibonacci series to generate a sequence of numbers.

#### Pseudocode

```
Fibonacci(n) {
  if n == 0 {
    return 0
  } else if n == 1 {
    return 1
  } else {
    return Fibonacci(n-1) + Fibonacci(n-2)
  }
}
```

In this pseudocode, we used a recursive approach to generate the Fibonacci series. We defined a function `Fibonacci(n)` that returns the `n`th term of the series. We used the recurrence relation `F(n) = F(n-1) + F(n-2)` to generate each term.

### 9.4 Common Operations on Linked Lists

#### Insertion

Insertion in a linked list involves adding a new node at a specific position in the list.

#### Deletion

Deletion in a linked list involves removing a node at a specific position in the list.

#### Search

Search in a linked list involves finding a specific node in the list.

#### Traversal

Traversal in a linked list involves visiting each node in the list in a specific order.

### 9.5 Advanced Operations on Linked Lists

#### Reverse Linked List

Reversing a linked list involves reversing the order of the nodes in the list.

#### Skip List

A skip list is a data structure that uses a linked list to store data. It is used to improve the search time complexity of the data structure.

#### Linked List with Linked Nodes

A linked list with linked nodes is a data structure that uses a linked list to store data. It is used to improve the insertion and deletion time complexity of the data structure.

### 9.5.1 Skip List

A skip list is a data structure that uses a linked list to store data. It is used to improve the search time complexity of the data structure.

#### Definition

A skip list is a data structure that uses a linked list to store data. It is used to improve the search time complexity of the data structure.

#### Example

Suppose we have a skip list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

We want to search for the node with value 3.

```
3
```

In this example, we used a skip list to search for the node with value 3.

#### Pseudocode

```
SkipList(arr) {
  // Create a linked list with the given array
  linkedList = LinkedList(arr)

  // Create a skip list with the linked list
  skipList = SkipList(linkedList)

  // Search for the node with value 3 in the skip list
  result = skipList.search(3)
  return result
}
```

In this pseudocode, we used a recursive approach to create a skip list. We created a linked list with the given array and then created a skip list with the linked list. We used the `search()` method to search for the node with value 3 in the skip list.

### 9.5.2 Linked List with Linked Nodes

A linked list with linked nodes is a data structure that uses a linked list to store data. It is used to improve the insertion and deletion time complexity of the data structure.

#### Definition

A linked list with linked nodes is a data structure that uses a linked list to store data. It is used to improve the insertion and deletion time complexity of the data structure.

#### Example

Suppose we have a linked list with linked nodes with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
```

We want to insert a new node with value 6 at the end of the list.

```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

In this example, we used a linked list with linked nodes to insert a new node at the end of the list.

#### Pseudocode

```
LinkedListWithLinkedNodes(arr) {
  // Create a linked list with the given array
  linkedList = LinkedList(arr)

  // Create a linked list with linked nodes
  linkedListWithLinkedNodes = LinkedListWithLinkedNodes(linkedList)

  // Insert a new node with value 6 at the end of the linked list with linked nodes
  linkedListWithLinkedNodes.insert(6)

  return linkedListWithLinkedNodes
}
```

In this pseudocode, we used a recursive approach to create a linked list with linked nodes. We created a linked list with the given array and then created a linked list with linked nodes with the linked list. We used the `insert()` method to insert a new node with value 6 at the end of the linked list with linked nodes.
