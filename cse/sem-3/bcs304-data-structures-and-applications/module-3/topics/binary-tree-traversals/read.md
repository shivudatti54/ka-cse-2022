# Binary Tree Traversals

## Introduction

Binary tree traversals constitute a fundamental algorithmic paradigm in data structures, representing systematic methods for visiting all nodes in a binary tree in a specific order. Unlike linear data structures where traversal is inherently sequential, trees present a multi-dimensional structure requiring deliberate algorithmic strategies to explore all nodes exactly once. The importance of tree traversals extends far beyond academic exercises; they serve as the backbone for numerous computational tasks including expression tree evaluation, serialization of tree structures, syntax tree construction in compilers, and hierarchical data processing in file systems and organization charts.

The fundamental challenge in tree traversal arises from the non-linear nature of tree structures. Each node (except the root) has exactly one parent, while potentially having two children, creating a branching structure that admits multiple valid visitation orders. This mathematical property gives rise to several canonical traversal strategies, each producing a distinct node sequence and serving different practical purposes. Understanding these traversal methods requires both theoretical comprehension of their algorithmic foundations and practical ability to implement them efficiently.

## Key Concepts

### Formal Definition and Mathematical Foundation

A binary tree is a finite set of nodes that is either empty or consists of a root node and two disjoint binary trees called the left subtree and right subtree. Let T be a binary tree with root node r, left subtree L, and right subtree R. A traversal is a systematic procedure that visits each node in T exactly once, producing a linear sequence of nodes. The canonical traversals are defined recursively as follows:

- **Preorder (Root-Left-Right)**: Visit(r), Traverse(L), Traverse(R)
- **Inorder (Left-Root-Right)**: Traverse(L), Visit(r), Traverse(R)
- **Postorder (Left-Right-Root)**: Traverse(L), Traverse(R), Visit(r)
- **Level-order (Breadth-First)**: Visit all nodes at depth d before visiting nodes at depth d+1

### Recursive Implementations with Complexity Analysis

The recursive formulations naturally translate to elegant code, but understanding their complexity requires careful analysis.

**Preorder Traversal:**

```c
void preorder(Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}
```

**Inorder Traversal:**

```c
void inorder(Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}
```

**Postorder Traversal:**

```c
void postorder(Node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}
```

**Theorem**: All four recursive traversals visit each node exactly once, resulting in Θ(n) time complexity where n is the number of nodes.

_Proof_: Each recursive call is invoked exactly once for every node in the tree. The base case (null pointer) returns immediately without any processing. For a tree with n nodes, there are precisely n calls to the Visit operation, and each edge (parent-child relationship) is traversed exactly twice (once descending, once ascending). Since a binary tree with n nodes has exactly n-1 edges, the total work is proportional to n, establishing Θ(n) time complexity. ∎

**Space Complexity**: The recursive implementations utilize the system call stack, requiring O(h) space where h is the height of the tree. In the worst case (skewed tree), h = n, yielding O(n) space; in a balanced tree, h = log₂n, yielding O(log n) space.

### Iterative Traversals Using Explicit Data Structures

The recursive implementations, while elegant, consume stack space proportional to tree height. Iterative versions using explicit stacks provide better control over space complexity.

**Iterative Inorder Traversal:**

```c
void iterativeInorder(Node* root) {
    Stack* s = createStack();
    Node* current = root;

    while (current != NULL || !isEmpty(s)) {
        while (current != NULL) {
            push(s, current);
            current = current->left;
        }
        current = pop(s);
        printf("%d ", current->data);
        current = current->right;
    }
}
```

**Iterative Preorder Traversal:**

```c
void iterativePreorder(Node* root) {
    if (root == NULL) return;
    Stack* s = createStack();
    push(s, root);

    while (!isEmpty(s)) {
        Node* node = pop(s);
        printf("%d ", node->data);
        if (node->right) push(s, node->right);
        if (node->left) push(s, node->left);
    }
}
```

**Iterative Postorder Traversal (Two-Stack Method):**

```c
void iterativePostorder(Node* root) {
    if (root == NULL) return;
    Stack* s1 = createStack();
    Stack* s2 = createStack();
    push(s1, root);

    while (!isEmpty(s1)) {
        Node* node = pop(s1);
        push(s2, node);
        if (node->left) push(s1, node->left);
        if (node->right) push(s1, node->right);
    }

    while (!isEmpty(s2)) {
        printf("%d ", pop(s2)->data);
    }
}
```

### Morris Traversal: O(1) Space Complexity

Morris Inorder Traversal achieves O(1) space complexity by utilizing temporary links to traverse the tree without a stack or recursion. The algorithm creates temporary edges to threaded paths back to ancestors.

```c
void morrisInorder(Node* root) {
    Node* current = root;

    while (current != NULL) {
        if (current->left == NULL) {
            printf("%d ", current->data);
            current = current->right;
        } else {
            Node* predecessor = current->left;
            while (predecessor->right != NULL && predecessor->right != current) {
                predecessor = predecessor->right;
            }

            if (predecessor->right == NULL) {
                predecessor->right = current;
                current = current->left;
            } else {
                predecessor->right = NULL;
                printf("%d ", current->data);
                current = current->right;
            }
        }
    }
}
```

_Time Complexity Analysis_: Each edge is traversed at most three times (going left, finding predecessor, returning via threaded link, going right), resulting in O(n) time. The space complexity is O(1) as no auxiliary data structure is used.

### Level-Order Traversal (Breadth-First Search)

Level-order traversal visits nodes breadth-wise, using a queue data structure to ensure nodes are processed level by level.

```c
void levelOrder(Node* root) {
    if (root == NULL) return;
    Queue* q = createQueue();
    enqueue(q, root);

    while (!isEmpty(q)) {
        Node* node = dequeue(q);
        printf("%d ", node->data);
        if (node->left) enqueue(q, node->left);
        if (node->right) enqueue(q, node->right);
    }
}
```

**Time Complexity**: O(n) - each node is enqueued and dequeued exactly once.
**Space Complexity**: O(w) where w is the maximum width of the tree (maximum number of nodes at any level). In the worst case, w = n/2 for a complete binary tree.

## Examples

### Example 1: Trace Traversals on a Given Tree

Consider the following binary tree:

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

**Preorder (Root-Left-Right)**: 1 → 2 → 4 → 5 → 3 → 6
Starting at root 1, we visit 1 first, then recursively traverse left subtree (2,4,5), then right subtree (3,6).

**Inorder (Left-Root-Right)**: 4 → 2 → 5 → 1 → 3 → 6
We traverse left subtree completely, visit root, then right subtree. For Binary Search Trees, inorder produces sorted order.

**Postorder (Left-Right-Root)**: 4 → 5 → 2 → 6 → 3 → 1
We traverse both subtrees completely before visiting the root. Useful for deleting tree nodes (children freed before parent).

**Level-order**: 1 → 2 → 3 → 4 → 5 → 6
Level by level: depth 0 (1), depth 1 (2,3), depth 2 (4,5,6).

### Example 2: Expression Tree Evaluation

Expression trees represent arithmetic expressions where internal nodes are operators and leaf nodes are operands. Evaluating the expression requires postorder traversal.

For the expression: (3 + 4) \* (5 - 2)

```
        *
       / \
      +   -
     / \ / \
    3  4 5  2
```

Postorder traversal yields: 3 4 + 5 2 - *
Evaluating: Push 3, Push 4 → Pop both, compute 3+4=7, Push 7 → Push 5, Push 2 → Pop 2, Pop 5, compute 5-2=3, Push 3 → Pop 3, Pop 7, compute 7*3 = 21

### Example 3: Finding Boundary of Binary Tree

The boundary traversal prints: root, left boundary (excluding leaves), all leaves (left to right), right boundary (excluding leaves, bottom to top).

For the tree:

```
        1
       / \
      2   3
     / \   \
    4   5   6
   /       \
  7         8
```

Boundary traversal: 1 → 2 → 4 → 7 → 5 → 8 → 6 → 3

## Exam Tips

1. **Traversal Order Memorization**: Remember the recursive definitions using mnemonic: "Root Left Right" (Preorder), "Left Root Right" (Inorder), "Left Right Root" (Postorder).

2. **BST Property**: For Binary Search Trees, inorder traversal always produces nodes in sorted (ascending) order - this is frequently tested.

3. **Space Complexity Comparison**: Recursive: O(h), Iterative with stack: O(h), Morris: O(1), Level-order: O(w). Know when each is preferable.

4. **Postorder for Dependency Resolution**: When evaluating dependencies or deleting tree nodes, postorder ensures children are processed before parents.

5. **Iterative Postorder Trick**: The two-stack method is easier to implement than the single-stack method; understand both for examination purposes.

6. **Threaded Binary Trees**: Some trees have null pointers used to store predecessor/successor links, enabling traversal without stack - review this concept for advanced questions.

7. **Trace Complex Trees**: Practice tracing traversals on trees with 10+ nodes, drawing the tree and marking visited nodes to avoid confusion during examinations.
