# Self-Referential Structures - Summary

## Key Definitions and Concepts

- **Self-referential structure**: A struct containing a pointer to another instance of the same type.
- **Node**: Fundamental unit of dynamic data structures, typically implemented as a self-referential struct.
- **Linked allocation**: Memory allocation at runtime using pointers (contrasts with static arrays).
- **Traversal**: Process of accessing elements by following pointers between nodes.
- **Dynamic memory**: Heap-allocated memory managed via `malloc()` and `free()`.

## Important Syntax and Code Patterns

```c
// Basic self-referential structure
struct node {
    int data;
    struct node *next; // Pointer to same structure type
};

// Memory allocation for new node
struct node *new_node = (struct node*)malloc(sizeof(struct node));

// Pointer dereferencing
new_node->data = 10;
new_node->next = NULL;
```

## Key Points

1. Enable creation of dynamic data structures (linked lists, trees, graphs)
2. Require pointers to connect nodes: `struct node *next`
3. Memory is allocated at runtime using `malloc()/calloc()`
4. More memory-efficient than static arrays for sparse data
5. Allow O(1) insertions/deletions at head (vs O(n) in arrays)
6. Require manual memory management to prevent leaks
7. Traversal requires sequential access via pointers (no random access)
8. Base for implementing stacks/queues with dynamic sizing
9. Used in OS file systems, music playlists, and browser history
10. Static allocation uses fixed memory, linked allocation grows dynamically

## Common Mistakes to Avoid

1. **Dangling pointers**: Forgetting to set `next` to `NULL` after allocation
2. **Memory leaks**: Not using `free()` after deleting nodes
3. **Segmentation faults**: Accessing `next` pointer without NULL check
4. **Shallow copy errors**: Copying pointer addresses instead of node data
5. **Infinite loops**: Incorrect termination condition in traversal

## Revision Tips

1. **Code tracing**: Practice dry-running insertion/deletion algorithms
2. **Diagram practice**: Draw memory diagrams for common operations
3. **Pointer drills**: Master arrow (`->`) vs dot (`.`) operator usage
4. **Compare & contrast**: Make table comparing arrays vs linked lists
5. **Exam focus**: Memorize node structure syntax and malloc/free patterns

**Exam Alert**: Frequently tested in questions about linked list operations, memory diagrams, and comparing static/dynamic allocation.
