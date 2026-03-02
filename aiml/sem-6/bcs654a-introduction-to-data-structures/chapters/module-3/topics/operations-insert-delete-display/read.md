# **Operations: Insert-Delete-Display**

## **Introduction**

In the context of linked lists, operations are essential to maintain and manipulate the data stored in the list. These operations enable us to add, remove, and display elements in the list efficiently. In this section, we will delve into the three primary operations: insert, delete, and display.

## **Insert Operation**

The insert operation is used to add a new node to the linked list. This operation can be performed at the beginning, middle, or end of the list.

### Types of Insertion

- **Insertion at the beginning**: This involves adding a new node at the head of the list.
- **Insertion at the middle**: This involves adding a new node at a specific position in the middle of the list.
- **Insertion at the end**: This involves adding a new node at the tail of the list.

### Example: Insertion at the beginning

Suppose we have a singly linked list with the following nodes:

- `A -> B -> C -> D`
- Where `A` is the head of the list and `D` is the tail.

To insert a new node `E` at the beginning, we update the head of the list:

- `E -> A -> B -> C -> D`

### Code Example

```c
// Structure for a node in the linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to insert a new node at the beginning
void insertAtBeginning(struct Node** head, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}
```

## **Delete Operation**

The delete operation is used to remove a node from the linked list. This operation can be performed at any position in the list.

### Types of Deletion

- **Deletion at a specific position**: This involves removing a node at a specific position in the list.
- **Deletion at the beginning**: This involves removing the head of the list.
- **Deletion at the end**: This involves removing the tail of the list.

### Example: Deletion at a specific position

Suppose we have a singly linked list with the following nodes:

- `A -> B -> C -> D -> E`

To delete the node `C`, we update the `next` pointer of `B` to point to `D`:

- `A -> B -> D -> E`

### Code Example

```c
// Function to delete a node at a specific position
void deleteAtPosition(struct Node** head, int position) {
    if (position == 0) {
        struct Node* temp = *head;
        *head = (*head)->next;
        free(temp);
    } else {
        struct Node* current = *head;
        for (int i = 0; i < position - 1; i++) {
            if (current->next == NULL) {
                break;
            }
            current = current->next;
        }
        if (current->next == NULL) {
            return;
        }
        struct Node* temp = current->next;
        current->next = current->next->next;
        free(temp);
    }
}
```

## **Display Operation**

The display operation is used to print the elements in the linked list.

### Example

Suppose we have a singly linked list with the following nodes:

- `A -> B -> C -> D`

To display the elements, we traverse the list starting from the head:

- `A`
- `B`
- `C`
- `D`

### Code Example

```c
// Function to display the elements in the linked list
void display(struct Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}
```

## **Key Concepts**

- **Insertion**: Adding a new node to the linked list.
- **Deletion**: Removing a node from the linked list.
- **Display**: Printing the elements in the linked list.
- **Types of insertion**: Insertion at the beginning, middle, and end of the list.
- **Types of deletion**: Deletion at a specific position, beginning, and end of the list.
