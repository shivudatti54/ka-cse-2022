# **Operations: Insert-Delete-Display**

## **Introduction**

Linked lists are a fundamental data structure in computer science, and operations on linked lists are crucial to understand. In this section, we will explore the three main operations on linked lists: Insert, Delete, and Display.

## **Insert Operation**

The Insert operation is used to add a new element to the linked list. This can be done at the beginning, middle, or end of the list.

### Types of Insertion

- **Insertion at the beginning**: This is done by updating the head of the linked list to point to the new node.
- **Insertion at the middle**: This is done by updating the middle node's next pointer to point to the new node.
- **Insertion at the end**: This is done by updating the last node's next pointer to point to the new node.

### Example

---

Suppose we have a linked list `1 -> 2 -> 3 -> 4` and we want to insert a new node with the value `5` at the beginning.

| Operation               | Step-by-Step Explanation                                    |
| ----------------------- | ----------------------------------------------------------- |
| Insert at the beginning | Set the head of the linked list to point to the new node.   |
|                         | Update the next pointer of the new node to point to the     |
|                         | existing head.                                              |
|                         | Update the existing head's next pointer to point to the new |
|                         | node.                                                       |

After the insertion, the linked list becomes `5 -> 1 -> 2 -> 3 -> 4`.

### Code Example

Here is a simple implementation of the Insert operation in Python:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Example usage
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Print the linked list
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
```

## **Delete Operation**

The Delete operation is used to remove an element from the linked list.

### Types of Deletion

- **Deletion at the beginning**: This is done by updating the head of the linked list to point to the next node.
- **Deletion at the middle**: This is done by updating the previous node's next pointer to point to the next node.
- **Deletion at the end**: This is done by updating the last node's next pointer to `None`.

### Example

---

Suppose we have a linked list `1 -> 2 -> 3 -> 4` and we want to delete the node with the value `2`.

| Operation               | Step-by-Step Explanation                                     |
| ----------------------- | ------------------------------------------------------------ |
| Delete at the beginning | Set the head of the linked list to point to the next node.   |
|                         | Update the next pointer of the next node to point to the     |
|                         | existing head.                                               |
|                         | Update the existing head's next pointer to point to the next |
|                         | node.                                                        |

After the deletion, the linked list becomes `1 -> 3 -> 4`.

### Code Example

Here is a simple implementation of the Delete operation in Python:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Example usage
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Delete node with value 2
linked_list.delete(2)

# Print the linked list
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
```

## **Display Operation**

The Display operation is used to print the elements of the linked list.

### Example

---

Suppose we have a linked list `1 -> 2 -> 3 -> 4` and we want to display its elements.

| Operation | Step-by-Step Explanation                               |
| --------- | ------------------------------------------------------ |
| Display   | Start from the head node and traverse the linked list. |
|           | Print the data of each node.                           |

After the display, the output will be `1 -> 2 -> 3 -> 4`.

### Code Example

Here is a simple implementation of the Display operation in Python:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Display the linked list
linked_list.display()
```

In conclusion, the Insert, Delete, and Display operations are essential for managing linked lists. Understanding these operations is crucial for implementing various algorithms and data structures in computer science.
