# Binary Trees and Traversals

## Introduction

A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. This fundamental data structure forms the backbone of numerous computer science applications, from expression parsing and syntax trees in compilers to Huffman coding in compression algorithms and binary search trees in databases. Understanding binary trees is essential for any computer science student, as they provide an efficient way to organize and access data in a hierarchical manner.

The concept of tree traversals is equally crucial in computer science. Traversal refers to the process of visiting all nodes in a tree in a systematic way. Unlike linear data structures where elements are accessed sequentially, trees require special traversal algorithms to ensure each node is visited exactly once. The order in which nodes are visited determines the utility of the traversal for specific applications—such as obtaining a sorted sequence from a binary search tree or evaluating an expression tree.

In this topic, we will explore the definition and properties of binary trees, various types of binary trees, and most importantly, the four fundamental traversal techniques: inorder, preorder, postorder, and level-order traversals. We will also analyze their time and space complexities and examine practical applications where each traversal proves most useful.

## Key Concepts

### Binary Tree Definition and Terminology

A binary tree is either empty or consists of a root node and two disjoint binary trees called the left subtree and right subtree. The fundamental terminology includes:

- **Root**: The topmost node of the tree (has no parent)
- **Parent**: A node that has children
- **Child**: A node descended from a parent
- **Leaf**: A node with no children (also called external node)
- **Internal Node**: A node with at least one child
- **Depth**: The length of the path from root to a node (root has depth 0)
- **Height**: The length of the longest path from root to a leaf
- **Siblings**: Nodes sharing the same parent
- **Ancestor/Descendant**: A node on the path from root to another node

### Types of Binary Trees

**Full Binary Tree**: Every node has either 0 or 2 children. No node has exactly one child.

**Complete Binary Tree**: All levels except possibly the last are completely filled, and all nodes are as far left as possible. This property makes it suitable for array representation and heap data structures.

**Perfect Binary Tree**: All internal nodes have exactly two children, and all leaf nodes are at the same level. A perfect binary tree of height h has 2^(h+1) - 1 nodes.

**Balanced Binary Tree**: The height difference between left and right subtrees of any node is at most 1. AVL trees maintain this property through rotations.

### Binary Tree Representation

**Linked Representation**: Each node contains data, a pointer to the left child, and a pointer to the right child. This is the most common representation.

```
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
```

**Array Representation**: For complete binary trees, nodes can be stored in an array where for a node at index i:
- Left child is at 2i + 1
- Right child is at 2i + 2
- Parent is at floor((i-1)/2)

### Tree Traversals

Traversals are classified based on when the root node is processed relative to its left and right subtrees.

#### Inorder Traversal (LNR: Left → Node → Right)

In inorder traversal, we first traverse the left subtree, then visit the root node, and finally traverse the right subtree. For a binary search tree (BST), this produces nodes in ascending order.

**Recursive Algorithm**:
```
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}
```

**Iterative Algorithm using Stack**:
```
void inorderIterative(Node* root) {
    Stack s;
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

#### Preorder Traversal (NLR: Node → Left → Right)

Preorder traversal visits the root first, then the left subtree, and finally the right subtree. This is useful for creating a copy of a tree, prefix expression evaluation, and directory traversal.

**Recursive Algorithm**:
```
void preorder(Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}
```

**Iterative Algorithm**:
```
void preorderIterative(Node* root) {
    if (root == NULL) return;
    Stack s;
    push(s, root);
    
    while (!isEmpty(s)) {
        Node* node = pop(s);
        printf("%d ", node->data);
        
        if (node->right) push(s, node->right);
        if (node->left) push(s, node->left);
    }
}
```

#### Postorder Traversal (LRN: Left → Right → Node)

Postorder traversal visits both subtrees before the root. This is essential for deleting a tree (children must be deleted before parent), evaluating postfix expressions, and computing directory sizes.

**Recursive Algorithm**:
```
void postorder(Node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}
```

#### Level Order Traversal (Breadth-First Search)

Level order traversal visits nodes level by level from left to right. It requires a queue data structure. This traversal is useful for finding the shortest path in an unweighted tree and level-wide operations.

**Algorithm**:
```
void levelOrder(Node* root) {
    if (root == NULL) return;
    Queue q;
    enqueue(q, root);
    
    while (!isEmpty(q)) {
        Node* node = dequeue(q);
        printf("%d ", node->data);
        
        if (node->left) enqueue(q, node->left);
        if (node->right) enqueue(q, node->right);
    }
}
```

### Complexity Analysis

| Traversal | Time Complexity | Space Complexity (Recursive) | Space Complexity (Iterative) |
|-----------|-----------------|------------------------------|------------------------------|
| Inorder   | O(n)            | O(h) - recursion stack       | O(h) - explicit stack        |
| Preorder  | O(n)            | O(h)                         | O(h)                         |
| Postorder | O(n)            | O(h)                         | O(h)                         |
| Level     | O(n)            | N/A                          | O(w) - queue, w = max width |

Where n = number of nodes, h = height of tree, w = maximum width

For a balanced tree, h = O(log n), while for a skewed tree, h = O(n).

## Examples

### Example 1: Traversing an Expression Tree

Consider the expression tree for (3 + 4) * (5 - 2):

```
        *
       / \
      +   -
     / \ / \
    3  4 5  2
```

- **Inorder (LNR)**: 3 + 4 * 5 - 2 → Output: 3 4 + 5 2 - * (Infix notation with operator precedence)
- **Preorder (NLR)**: * + 3 4 - 5 2 → Output: * + 3 4 - 5 2 (Prefix notation)
- **Postorder (LRN)**: 3 4 + 5 2 - * → Output: 3 4 + 5 2 - * (Postfix notation/Reverse Polish Notation)
- **Level Order**: * + - 3 4 5 2

### Example 2: Binary Search Tree Operations

Given a BST:
```
        50
       /  \
     30    70
    /  \   /  \
   20  40 60  80
```

- **Inorder**: 20 30 40 50 60 70 80 (Sorted order - used for validation and searching)
- **Preorder**: 50 30 20 40 70 60 80 (Creates a copy of tree)
- **Postorder**: 20 40 30 60 80 70 50 (Deletes tree in correct order)
- **Level Order**: 50 30 70 20 40 60 80 (Finds shortest distance from root)

### Example 3: Practical Application - Directory Size Calculation

Consider a file system directory structure:
```
        Documents/
       /    |    \
   Work/  Personal/  Downloads/
   report.doc  photos.zip
```

To calculate total size of a directory:
1. Use postorder traversal (process children before parent)
2. First calculate sizes of subdirectories
3. Then sum with current directory files

If we store directory sizes at each node:
- Postorder processes: Work/, Personal/, Downloads/ first
- Then calculates: Documents/ = size(Work) + size(Personal) + size(Downloads) + own_files

## Exam Tips

1. **Remember Traversal Orders**: Use mnemonics - LNR (Left Node Right) = Inorder, NLR = Preorder, LRN = Postorder. For exam questions, always draw the tree first.

2. **BST Property**: Inorder traversal of a BST always produces sorted output. This is frequently tested to verify if a tree is a valid BST.

3. **Tree Construction**: Given two traversals (e.g., inorder and preorder), you can uniquely reconstruct the tree. However, inorder alone cannot reconstruct a unique tree.

4. **Time-Space Tradeoff**: Recursive traversals use O(h) stack space, while iterative versions use explicit stacks/queues. For skewed trees (worst case), space becomes O(n).

5. **Level Order with Level Information**: To print nodes level-by-level with their levels, use a queue storing pairs of (node, level) or use marker nodes (NULL) to indicate level boundaries.

6. **Expression Tree Applications**: Inorder gives infix (needs parentheses for operators), preorder gives prefix, postorder gives postfix. This is crucial for expression evaluator questions.

7. **Tree Height Formulas**: For a binary tree with n nodes:
   - Minimum height: ⌊log₂n⌋ (complete/balanced)
   - Maximum height: n - 1 (skewed tree)
   - Relationship: h ≤ n-1 and n ≤ 2^(h+1) - 1

8. **Morris Traversal**: An advanced O(1) space traversal technique that modifies the tree temporarily. Know it for extra credit questions.