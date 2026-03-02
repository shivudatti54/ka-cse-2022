# Singly Linked Lists - Summary

## Key Definitions and Concepts

- **Singly Linked List**: A linear data structure where each node contains data and a pointer to the next node, forming a chain-like structure.
- **Node**: The fundamental building block consisting of a data field and a next pointer field.
- **Head Pointer**: A pointer variable that stores the address of the first node in the list.
- **NULL Pointer**: A special pointer value indicating the end of the list (last node's next field).

## Important Formulas and Theorems

- **Node Structure**: struct Node { datatype data; struct Node *next; };
- **Memory Allocation**: newNode = (struct Node*)malloc(sizeof(struct Node));
- **Memory Deallocation**: free(pointerToNode);
- **Time Complexity - Insertion at beginning**: O(1)
- **Time Complexity - Insertion at end**: O(n)
- **Time Complexity - Deletion at beginning**: O(1)
- **Time Complexity - Deletion at end**: O(n)
- **Time Complexity - Search/Traversal**: O(n)

## Key Points

- Linked lists provide dynamic memory allocation, unlike fixed-size arrays.
- Each node contains two fields: data and next pointer.
- The last node's next pointer must point to NULL to indicate the end of the list.
- Insertion at the beginning requires updating only the head pointer.
- Insertion at the end requires traversing the entire list unless a tail pointer is maintained.
- Always free memory after deletion to prevent memory leaks.
- Linked lists do not allow random access; traversal from head is necessary.
- No memory wastage occurs as nodes are allocated on-demand.

## Common Mistakes to Avoid

- Forgetting to set the new node's next pointer during insertion, causing dangling links.
- Not checking for NULL before accessing a pointer, leading to segmentation faults.
- Losing the reference to the next node before updating pointers during deletion.
- Forgetting to update the head pointer when inserting/deleting the first node.
- Not freeing memory after deletion, resulting in memory leaks.

## Revision Tips

1. Practice writing the complete node structure definition and basic operations from memory.
2. Draw diagrams for each operation to visualize pointer changes clearly.
3. Memorize the time complexities of all operations for quick recall during exams.
4. Review previous year DU question papers to understand the exam pattern and important topics.
5. Write and execute small programs to reinforce conceptual understanding of pointer manipulations.