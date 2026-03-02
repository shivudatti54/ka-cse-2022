# Tree Traversals

## Overview

**Traversal** means visiting all nodes of a tree exactly once. There are two main categories:

1. **Depth-First Traversal** (DFS) - Inorder, Preorder, Postorder
2. **Breadth-First Traversal** (BFS) - Level Order

## Sample Tree

```
        1
       / \
      2   3
     / \
    4   5
```

## 1. Inorder Traversal (LNR)

**Order**: Left → Node → Right

```c
void inorder(struct Node *root) {
    if(root == NULL) return;
    inorder(root->left);     // L
    printf("%d ", root->data); // N
    inorder(root->right);    // R
}
```

**Output**: 4, 2, 5, 1, 3

**Key**: For BST, gives **sorted order**!

## 2. Preorder Traversal (NLR)

**Order**: Node → Left → Right

```c
void preorder(struct Node *root) {
    if(root == NULL) return;
    printf("%d ", root->data); // N
    preorder(root->left);    // L
    preorder(root->right);   // R
}
```

**Output**: 1, 2, 4, 5, 3

**Key**: Used to **create a copy** of tree

## 3. Postorder Traversal (LRN)

**Order**: Left → Right → Node

```c
void postorder(struct Node *root) {
    if(root == NULL) return;
    postorder(root->left);   // L
    postorder(root->right);  // R
    printf("%d ", root->data); // N
}
```

**Output**: 4, 5, 2, 3, 1

**Key**: Used to **delete** a tree (children before parent)

## 4. Level Order Traversal (BFS)

**Order**: Level by level, left to right

```c
void levelOrder(struct Node *root) {
    if(root == NULL) return;

    struct Queue q;
    initQueue(&q);
    enqueue(&q, root);

    while(!isEmpty(&q)) {
        struct Node *current = dequeue(&q);
        printf("%d ", current->data);

        if(current->left)
            enqueue(&q, current->left);
        if(current->right)
            enqueue(&q, current->right);
    }
}
```

**Output**: 1, 2, 3, 4, 5

**Key**: Uses **Queue**, visits nodes top to bottom

## Iterative Traversals Using Stack

### Iterative Inorder

```c
void inorderIterative(struct Node *root) {
    struct Stack s;
    init(&s);
    struct Node *current = root;

    while(current != NULL || !isEmpty(&s)) {
        // Go to leftmost
        while(current != NULL) {
            push(&s, current);
            current = current->left;
        }

        // Visit node
        current = pop(&s);
        printf("%d ", current->data);

        // Go right
        current = current->right;
    }
}
```

### Iterative Preorder

```c
void preorderIterative(struct Node *root) {
    if(root == NULL) return;

    struct Stack s;
    init(&s);
    push(&s, root);

    while(!isEmpty(&s)) {
        struct Node *current = pop(&s);
        printf("%d ", current->data);

        // Push right first (so left is processed first)
        if(current->right)
            push(&s, current->right);
        if(current->left)
            push(&s, current->left);
    }
}
```

## Comparison Table

| Traversal   | Order      | Use Case                  | Data Structure |
| ----------- | ---------- | ------------------------- | -------------- |
| Inorder     | L-N-R      | Sorted output (BST)       | Stack          |
| Preorder    | N-L-R      | Copy tree, prefix expr    | Stack          |
| Postorder   | L-R-N      | Delete tree, postfix expr | Stack          |
| Level Order | Level-wise | BFS, shortest path        | Queue          |

## Time & Space Complexity

| Traversal           | Time | Space |
| ------------------- | ---- | ----- |
| All DFS (recursive) | O(n) | O(h)  |
| All DFS (iterative) | O(n) | O(h)  |
| Level Order         | O(n) | O(w)  |

h = height, w = max width of tree

## Construct Tree from Traversals

- **Preorder + Inorder** → Unique tree
- **Postorder + Inorder** → Unique tree
- **Preorder + Postorder** → Only for full binary tree

## Key Points

1. DFS uses **Stack** (implicit in recursion)
2. BFS uses **Queue**
3. Inorder of BST = Sorted
4. Preorder root is always first
5. Postorder root is always last
