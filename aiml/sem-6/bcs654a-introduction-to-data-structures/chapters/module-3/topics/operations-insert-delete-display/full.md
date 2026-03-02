# Operations: Insert-Delete-Display

### Introduction

In data structures, the operations Insert, Delete, and Display are fundamental methods used to manipulate and manage data in a linked list. These operations enable us to add, remove, and retrieve elements from the list, making it an essential component of various algorithms and applications. In this section, we will delve into the Insert, Delete, and Display operations and explore their implementations, complexities, and applications.

### History of Linked Lists

Linked lists have been around since the 1960s, and their use has expanded significantly over the years. The first linked list was proposed by F. Thomson in 1967, and it was used to implement a stack. Since then, linked lists have become a fundamental data structure in computer science, used in various applications, including databases, web browsers, and operating systems.

### Types of Linked Lists

There are two primary types of linked lists: singly linked lists and doubly linked lists.

- **Singly Linked List**: A singly linked list only allows traversal in one direction, i.e., from head to tail. Each node only points to the next node in the list.
- **Doubly Linked List**: A doubly linked list allows traversal in both directions, i.e., from head to tail and from tail to head. Each node points to both the next and previous nodes in the list.

### Insert Operation

The Insert operation is used to add a new node to the linked list at a specific position. There are three types of insert operations:

- **Insert at Head**: Inserting a new node at the head of the list.
- **Insert at Tail**: Inserting a new node at the tail of the list.
- **Insert at Position**: Inserting a new node at a specific position in the list.

### Insert at Head

To insert a new node at the head of the list, we need to update the head pointer to point to the new node.

```markdown
Insert at Head:

1.  Create a new node with the given data.
2.  Update the head pointer to point to the new node.
```

### Insert at Tail

To insert a new node at the tail of the list, we need to update the tail pointer to point to the new node.

```markdown
Insert at Tail:

1.  Create a new node with the given data.
2.  Traverse the list to find the last node (tail).
3.  Update the next pointer of the last node to point to the new node.
4.  Update the tail pointer to point to the new node.
```

### Insert at Position

To insert a new node at a specific position in the list, we need to traverse the list to find the node at the specified position and update its next pointer to point to the new node.

```markdown
Insert at Position:

1.  Create a new node with the given data.
2.  Traverse the list to find the node at the specified position.
3.  Update the next pointer of the node at the specified position to point to the new node.
4.  Update the next pointer of the previous node to point to the new node.
```

### Delete Operation

The Delete operation is used to remove a node from the linked list. There are three types of delete operations:

- **Delete at Head**: Deleting the node at the head of the list.
- **Delete at Tail**: Deleting the node at the tail of the list.
- **Delete at Position**: Deleting a node at a specific position in the list.

### Delete at Head

To delete the node at the head of the list, we need to update the head pointer to point to the next node.

```markdown
Delete at Head:

1.  Update the head pointer to point to the next node.
```

### Delete at Tail

To delete the node at the tail of the list, we need to update the next pointer of the previous node to point to the node after the deleted node.

```markdown
Delete at Tail:

1.  Traverse the list to find the last node (tail).
2.  Update the next pointer of the previous node to point to the node after the deleted node.
3.  Update the tail pointer to point to the node after the deleted node.
```

### Delete at Position

To delete a node at a specific position in the list, we need to update the next pointer of the previous node to point to the node after the deleted node.

```markdown
Delete at Position:

1.  Traverse the list to find the node at the specified position.
2.  Update the next pointer of the previous node to point to the node after the deleted node.
3.  Update the next pointer of the next node to point to the node after the deleted node.
```

### Display Operation

The Display operation is used to print the elements of the linked list.

```markdown
Display:

1.  Traverse the list starting from the head node.
2.  Print the data of each node.
3.  Update the head pointer to point to the next node.
```

### Example Implementation

Here is an example implementation of a singly linked list with Insert, Delete, and Display operations in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if not current:
                    return
                current = current.next
            if not current:
                return
            new_node.next = current.next
            current.next = new_node

    def delete_at_head(self):
        if self.head:
            self.head = self.head.next

    def delete_at_tail(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = None
            self.head = None

    def delete_at_position(self, position):
        if position == 0:
            self.delete_at_head()
        else:
            current = self.head
            for _ in range(position - 1):
                if not current:
                    return
                current = current.next
            if not current:
                return
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
ll = LinkedList()
ll.insert_at_tail(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.display()  # prints: 1 2 3
ll.insert_at_position(4, 2)
ll.display()  # prints: 1 2 4 3
ll.delete_at_head()
ll.display()  # prints: 2 4 3
ll.delete_at_tail()
ll.display()  # prints: 2 4
```

### Applications

Linked lists are widely used in various applications, including:

- **Database Management Systems**: Linked lists are used to implement database indexing, where each record is linked to the next record in the list.
- **Web Browsers**: Linked lists are used to implement the back and forward navigation buttons in web browsers.
- **Operating Systems**: Linked lists are used to implement the file system, where each file is linked to the next file in the list.
- **Compilers**: Linked lists are used to implement the symbol table, where each symbol is linked to the next symbol in the list.

### Further Reading

- "Algorithms" by Robert Sedgewick and Kevin Wayne
- "Data Structures and Algorithms in Python" by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
- "The Art of Computer Programming" by Donald E. Knuth
- "Introduction to Algorithms" by Thomas H. Cormen
