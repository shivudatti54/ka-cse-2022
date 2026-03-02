# **Textbook 2: Chapter Ch - Introduction to Data Structures**

## **Introduction**

Data structures are the fundamental building blocks of programming. They provide a way to store and organize data in a way that makes it easily accessible and manipulable. In this chapter, we will introduce the concept of linked lists, which are a fundamental data structure used in many applications.

## **What is a Linked List?**

A linked list is a linear data structure where each element is a separate object, and each element (called a node) points to the next element in the sequence. This structure allows for efficient insertion and deletion of elements at any position in the list.

## **Key Characteristics of Linked Lists**

- Each element is a separate object.
- Each element points to the next element in the sequence.
- No fixed size for the list.
- Elements can be inserted or deleted at any position.

## **Types of Linked Lists**

### 1. Singly Linked List

A singly linked list is the most common type of linked list. In a singly linked list, each node only points to the next node in the sequence.

**Example of a Singly Linked List**

```markdown
1 -> 2 -> 3 -> 4 -> 5
```

Each node in the list contains a value and a pointer to the next node in the sequence.

### 2. Doubly Linked List

A doubly linked list is a type of linked list where each node not only points to the next node in the sequence but also points to the previous node.

**Example of a Doubly Linked List**

```markdown
1 <- 2 <- 3 <- 4 <- 5
```

Each node in the list contains a value and pointers to both the previous and next nodes in the sequence.

### 3. Self-Referential Linked List

A self-referential linked list is a type of linked list where each node contains a pointer to its own memory address.

**Example of a Self-Referential Linked List**

```markdown
1 -> 2 -> 3 -> 4 -> 5
```

This type of linked list is used to implement recursive algorithms.

## **Operations on Linked Lists**

- **Insertion**: Adding a new node to the end of the list.
- **Deletion**: Removing a node from the list.
- **Traversal**: Printing the elements of the list in a specific order.
- **Search**: Finding a specific node in the list.

## **Common Operations on Linked Lists**

### 1. Insertion

To insert a new node at the beginning of the list, we need to update the `head` pointer.

```markdown
Insert node with value 6 at the beginning of the list:
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

### 2. Deletion

To delete a node from the list, we need to update the `head` pointer and the `next` pointers of the adjacent nodes.

```markdown
Delete node with value 3 from the list:
1 -> 2 -> 4 -> 5
```

### 3. Traversal

To print the elements of the list, we can use a recursive function or an iterative approach.

```markdown
Print the elements of the list:
1
2
3
4
5
```

### 4. Search

To find a specific node in the list, we can use a linear search algorithm.

```markdown
Find node with value 4 in the list:
Node with value 4 found at position 3
```

## **Conclusion**

In this chapter, we introduced the concept of linked lists, including singly linked lists, doubly linked lists, and self-referential linked lists. We also discussed common operations on linked lists, such as insertion, deletion, traversal, and search. With this knowledge, you can implement efficient data structures in your programming projects.
