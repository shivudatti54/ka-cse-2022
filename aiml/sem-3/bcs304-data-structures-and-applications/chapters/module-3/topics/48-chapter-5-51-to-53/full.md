# **Chapter-5: Data Structures and Applications**

### 5.1: Introduction to Data Structures

---

Data structures are the ways in which we organize and store data in a computer so that it can be efficiently accessed, managed, and modified. They are the building blocks of any software application and are used to solve complex problems in computer science.

## **History of Data Structures**

The concept of data structures dates back to the 1950s when the first computers were developed. However, it wasn't until the 1960s that the term "data structure" was coined by John McCarthy, one of the founders of the programming language Lisp. Since then, data structures have undergone significant changes and advancements, driven by the development of new programming languages, hardware, and software technologies.

## **Types of Data Structures**

There are several types of data structures, including:

- **Arrays**: A collection of elements of the same data type stored in contiguous memory locations.
- **Linked Lists**: A sequence of elements, each of which points to the next element in the sequence.
- **Stacks**: A Last-In-First-Out (LIFO) data structure that follows the principle of last item inserted is the first one to be removed.
- **Queues**: A First-In-First-Out (FIFO) data structure that follows the principle of first item inserted is the first one to be removed.
- **Trees**: A hierarchical data structure consisting of nodes, each of which has a value and zero or more child nodes.
- **Graphs**: A non-linear data structure consisting of nodes and edges that connect the nodes.

### 5.2: Arrays

---

An array is a collection of elements of the same data type stored in contiguous memory locations. The elements of an array are identified by an index or subscript, which is used to access and manipulate the elements.

## **Array Operations**

- **Insertion**: Inserting an element into an array involves shifting the elements to the right and assigning the new element the index of the element being inserted.
- **Deletion**: Deleting an element from an array involves shifting the elements to the left and assigning the index of the element being deleted to the new element.
- **Search**: Searching for an element in an array involves comparing the element to be searched with each element in the array until the element is found.

**Example of Array Operations**

```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Insertion
    arr[3] = 10;
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Deletion
    arr[2] = 9;
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Search
    int target = 4;
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            printf("Element %d found at index %d\n", target, i);
            break;
        }
    }

    return 0;
}
```

### 5.3: Linked Lists

---

A linked list is a sequence of elements, each of which points to the next element in the sequence. Linked lists are useful in situations where elements need to be added or removed frequently.

## **Types of Linked Lists**

- **Singly Linked Lists**: Each element points to the next element in the sequence.
- **Doubly Linked Lists**: Each element points to the next and previous elements in the sequence.
- **Circularly Linked Lists**: The last element points to the first element in the sequence.

## **Linked List Operations**

- **Insertion**: Inserting an element into a linked list involves creating a new node and assigning it the next element in the list.
- **Deletion**: Deleting an element from a linked list involves removing the node corresponding to the element.
- **Search**: Searching for an element in a linked list involves traversing the list until the element is found.

**Example of Linked List Operations**

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

Node* insertNode(Node* head, int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        Node* last = head;
        while (last->next != NULL) {
            last = last->next;
        }
        last->next = newNode;
    }
    return head;
}

Node* deleteNode(Node* head, int data) {
    if (head == NULL) {
        return NULL;
    }
    if (head->data == data) {
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    Node* last = head;
    while (last->next != NULL) {
        if (last->next->data == data) {
            Node* temp = last->next;
            last->next = last->next->next;
            free(temp);
            return head;
        }
        last = last->next;
    }
    return head;
}

int searchNode(Node* head, int data) {
    Node* current = head;
    while (current != NULL) {
        if (current->data == data) {
            return 1;
        }
        current = current->next;
    }
    return 0;
}

int main() {
    Node* head = NULL;
    head = insertNode(head, 1);
    head = insertNode(head, 2);
    head = insertNode(head, 3);
    head = insertNode(head, 4);

    printf("Linked list: ");
    Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");

    head = deleteNode(head, 3);
    printf("Linked list after deletion: ");
    current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");

    int target = 4;
    if (searchNode(head, target)) {
        printf("Element %d found\n", target);
    } else {
        printf("Element %d not found\n", target);
    }

    return 0;
}
```

### Further Reading

---

- "Data Structures and Algorithms in Python" by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
- "Introduction to Algorithms" by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein
- "Data Structures and Algorithms in Java" by Steven S. Skiena
