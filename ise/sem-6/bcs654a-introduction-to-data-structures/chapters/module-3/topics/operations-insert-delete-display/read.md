# **Operations: Insert-Delete-Display**

## **Introduction**

In the context of linked lists, operations are essential for maintaining and manipulating the data. These operations include insertion, deletion, and display. In this section, we will delve into each of these operations and explore their implications on the linked list structure.

## **Insert Operation**

The insert operation is used to add a new node to the linked list. This operation can be performed at different positions in the list, including the beginning, middle, or end.

### Types of Insertion

- **Append**: Inserting a new node at the end of the linked list.
- **Prepend**: Inserting a new node at the beginning of the linked list.
- **Middle**: Inserting a new node at a specific position in the middle of the linked list.

### How to Perform Insertion

1.  Create a new node with the given data.
2.  Traverse the linked list to the position where the new node will be inserted.
3.  Update the `next` pointer of the node at the insertion position to point to the new node.
4.  Update the `next` pointer of the new node to point to the next node in the list.

**Example of Insertion**

Suppose we have a linked list with the following structure:

```
Node 1 -> Node 2 -> Node 3
```

If we want to insert a new node with value 4 at the end of the list, the resulting structure will be:

```
Node 1 -> Node 2 -> Node 3 -> Node 4
```

If we want to insert a new node with value 0 at the beginning of the list, the resulting structure will be:

```
Node 0 -> Node 1 -> Node 2 -> Node 3
```

## **Delete Operation**

The delete operation is used to remove a node from the linked list. This operation can be performed on any node in the list.

### Types of Deletion

- **Single Node Deletion**: Deleting a node with only one child.
- **Node with Two Children**: Deleting a node with two children.
- **Node with No Children**: Deleting a node with no children.

### How to Perform Deletion

1.  Traverse the linked list to find the node to be deleted.
2.  Check if the node to be deleted has any children.
3.  If the node to be deleted has one child, update the `next` pointer of the previous node to point to the child node.
4.  If the node to be deleted has two children, create a new node with the data of the node to be deleted and update the `next` pointer of the previous node to point to the new node.
5.  If the node to be deleted has no children, simply remove the node from the list.

**Example of Deletion**

Suppose we have a linked list with the following structure:

```
Node 1 -> Node 2 -> Node 3 -> Node 4
```

If we want to delete the node with value 3, the resulting structure will be:

```
Node 1 -> Node 2 -> Node 4
```

## **Display Operation**

The display operation is used to print the elements of the linked list.

### How to Perform Display

1.  Traverse the linked list starting from the head node.
2.  Print the data of each node as you traverse the list.

**Example of Display**

Suppose we have a linked list with the following structure:

```
Node 1 -> Node 2 -> Node 3 -> Node 4
```

If we want to display the elements of the list, the output will be:

```
1
2
3
4
```

## **Key Concepts**

- **Insertion**: Adding a new node to the linked list.
- **Deletion**: Removing a node from the linked list.
- **Display**: Printing the elements of the linked list.
- **Node**: The basic unit of a linked list, consisting of data and a pointer to the next node.
- **Head**: The first node in the linked list.

By understanding these operations and how to perform them, you can effectively manipulate and maintain linked lists.
