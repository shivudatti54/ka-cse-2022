# **INSERT, DELETE, AND DISPLAY OPERATIONS ON LINKED LISTS**

## **INTRODUCTION**

Linked lists are a fundamental data structure in computer science, consisting of a sequence of nodes, each containing a value and a reference (i.e., a "link") to the next node in the sequence. Operations on linked lists, such as insertion, deletion, and display, are essential for manipulating and traversing the list. In this topic, we will delve into the details of these operations, exploring their algorithms, complexities, and applications.

## **INSERT OPERATION**

The insert operation is used to add a new node to the linked list. There are two types of insert operations:

### **Insert at the beginning**

Inserting a new node at the beginning of the linked list involves updating the `head` reference of the list to point to the new node.

**Algorithm**

1. Create a new node with the given value.
2. Update the `head` reference of the list to point to the new node.
3. Update the `next` reference of the new node to point to the current `head` node.
4. Return the updated list.

**Example**

Suppose we have a linked list `1 -> 2 -> 3` and we want to insert a new node with value `4` at the beginning.

```
      +---------------+
      |  4 (new node)  |
      +---------------+
             |
             |
             v
       +---------------+
       |  1 (head)    |
       |  -> 2        |
       |  -> 3        |
       +---------------+
```

**Time Complexity**

The time complexity of the insert operation at the beginning of the linked list is O(1), since we only need to update the `head` reference and the `next` reference of the new node.

### **Insert at the end**

Inserting a new node at the end of the linked list involves traversing the list until we reach the last node and updating its `next` reference to point to the new node.

**Algorithm**

1. Traverse the list until we reach the last node.
2. Create a new node with the given value.
3. Update the `next` reference of the last node to point to the new node.
4. Return the updated list.

**Example**

Suppose we have a linked list `1 -> 2 -> 3` and we want to insert a new node with value `4` at the end.

```
      +---------------+
      |  1 (head)    |
      |  -> 2        |
      |  -> 3        |
      +---------------+
             |
             |
             v
       +---------------+
       |  4 (new node)  |
       +---------------+
```

**Time Complexity**

The time complexity of the insert operation at the end of the linked list is O(n), where n is the number of nodes in the list, since we need to traverse the list to reach the last node.

## **DELETE OPERATION**

The delete operation is used to remove a node from the linked list. There are two types of delete operations:

### **Delete at a specific node**

Deleting a node at a specific position in the linked list involves updating the `next` references of the adjacent nodes to skip the node to be deleted.

**Algorithm**

1. Traverse the list until we reach the node before the node to be deleted.
2. Update the `next` reference of the node before the node to be deleted to point to the node after the node to be deleted.
3. Update the `next` reference of the node after the node to be deleted to point to the node before the node to be deleted.
4. Return the updated list.

**Example**

Suppose we have a linked list `1 -> 2 -> 3 -> 4` and we want to delete the node with value `2`.

```
      +---------------+
      |  1 (head)    |
      |  -> 2 (node to be deleted)  |
      |  -> 3        |
      |  -> 4        |
      +---------------+
             |
             |
             v
       +---------------+
       |  1 (head)    |
       |  -> 3        |
       |  -> 4        |
       +---------------+
```

**Time Complexity**

The time complexity of the delete operation at a specific node is O(1), since we only need to update the `next` references of the adjacent nodes.

### **Delete at any node**

Deleting a node at any position in the linked list involves finding the node to be deleted and updating its `next` references to point to the adjacent nodes.

**Algorithm**

1. Find the node to be deleted by traversing the list.
2. Update the `next` reference of the node before the node to be deleted to point to the node after the node to be deleted.
3. Update the `next` reference of the node after the node to be deleted to point to the node before the node to be deleted.
4. Return the updated list.

**Example**

Suppose we have a linked list `1 -> 2 -> 3 -> 4` and we want to delete the node with value `3`.

```
      +---------------+
      |  1 (head)    |
      |  -> 2        |
      |  -> 3 (node to be deleted)  |
      |  -> 4        |
      +---------------+
             |
             |
             v
       +---------------+
       |  1 (head)    |
       |  -> 2        |
       |  -> 4        |
       +---------------+
```

**Time Complexity**

The time complexity of the delete operation at any node is O(n), where n is the number of nodes in the list, since we need to traverse the list to find the node to be deleted.

## **DISPLAY OPERATION**

The display operation is used to print the elements of the linked list.

**Algorithm**

1. Traverse the list starting from the head node.
2. Print the value of each node.
3. Return the updated list.

**Example**

Suppose we have a linked list `1 -> 2 -> 3` and we want to display its elements.

```
1
2
3
```

**Time Complexity**

The time complexity of the display operation is O(n), where n is the number of nodes in the list, since we need to traverse the list to print its elements.

## **CASE STUDIES**

1. **Insertion of new nodes at the beginning and end of a linked list**

Suppose we have a linked list `1 -> 2 -> 3` and we want to insert new nodes with values `4` and `5` at the beginning and end, respectively.

```
      +---------------+
      |  4 (new node)  |
      |  -> 1 (head)    |
      |  -> 2        |
      |  -> 3        |
      +---------------+
             |
             |
             v
       +---------------+
       |  5 (new node)  |
       |  -> 4        |
       |  -> 2        |
       |  -> 3        |
       +---------------+
```

2. **Deletion of nodes at specific positions**

Suppose we have a linked list `1 -> 2 -> 3 -> 4` and we want to delete the nodes with values `2` and `4`, respectively.

```
      +---------------+
      |  1 (head)    |
      |  -> 3        |
      |  -> 4 (node to be deleted)  |
      +---------------+
             |
             |
             v
       +---------------+
       |  1 (head)    |
       |  -> 3        |
       +---------------+
```

3. **Displaying the elements of a linked list**

Suppose we have a linked list `1 -> 2 -> 3` and we want to display its elements.

```
1
2
3
```

## **APPLICATIONS**

1. **Database management systems**

Linked lists are used in database management systems to implement data structures such as queues and stacks.

2. **Algorithms and data structures**

Linked lists are used to implement various algorithms and data structures, such as sorting and searching algorithms.

3. **Compilers**

Linked lists are used in compilers to implement data structures such as symbol tables and parse trees.

4. **Network protocols**

Linked lists are used in network protocols to implement data structures such as buffers and queues.

## **FURTHER READING**

- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms)
- [Data Structures and Algorithms in Python](https://www.amazon.com/Data-Structures-Algorithms-Python-Philip-Russell/dp/1784447531)
- [The Algorithm Design Manual](https://dl.acm.org/citation.cfm?id=114735)
- [Introduction to Computer Science](https://mitpress.mit.edu/books/introduction-computer-science)

Note: This is a comprehensive guide to the insert, delete, and display operations on linked lists. The examples and case studies are provided to illustrate the concepts and algorithms used in these operations. The applications section highlights the use of linked lists in various fields and provides further reading suggestions.
