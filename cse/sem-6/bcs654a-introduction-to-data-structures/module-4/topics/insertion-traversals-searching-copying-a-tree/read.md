# Binary Tree Operations: Insertion, Traversals, Searching, and Copying

## Introduction

A binary tree is a hierarchical data structure in which each node has at most two children, commonly referred to as the left child and the right child. This chapter explores the fundamental operations performed on binary trees: node insertion, tree traversal, element searching, and tree copying. These operations form the foundation for understanding more advanced tree-based data structures such as Binary Search Trees (BST), AVL Trees, and Heaps.

## TreeNode Structure Definition

In C, a binary tree node is typically defined using a self-referential structure:

```c
struct TreeNode {
 int data;
 struct TreeNode* left;
 struct TreeNode* right;
};
```

**Component Analysis:**

- **data**: An integer field storing the value contained in the node
- **left**: A pointer to the left child node (or NULL if no left child exists)
- **right**: A pointer to the right child node (or NULL if no right child exists)

This structure follows the recursive definition of a binary tree: a tree consists of a root node and two disjoint trees known as the left and right subtrees.

## 1. Tree Insertion

### Theory

Insertion in a general binary tree (as opposed to a Binary Search Tree) involves adding a new node at the first available position in level order. This maintains the completeness property of the tree as much as possible, ensuring the tree remains balanced in terms of levels.

### Algorithm (Level-Order Insertion)

```
function insert(root, value):
 1. Create a new node with the given value
 2. If root is NULL, return the new node as the new root
 3. Initialize a queue with root
 4. While queue is not empty:
 a. Dequeue a node
 b. If left child is NULL:
 i. Set left child to new node
 ii. Return root
 c. Else, enqueue left child
 d. If right child is NULL:
 i. Set right child to new node
 ii. Return root
 e. Else, enqueue right child
```

### Implementation

```c
struct TreeNode* insert(struct TreeNode* root, int value) {
 if (root == NULL) {
 struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 newNode->data = value;
 newNode->left = NULL;
 newNode->right = NULL;
 return newNode;
 }

 // Use queue for level-order insertion
 struct TreeNode* queue[100];
 int front = 0, rear = 0;
 queue[rear++] = root;

 while (front < rear) {
 struct TreeNode* current = queue[front++];

 if (current->left == NULL) {
 current->left = createNode(value);
 return root;
 } else {
 queue[rear++] = current->left;
 }

 if (current->right == NULL) {
 current->right = createNode(value);
 return root;
 } else {
 queue[rear++] = current->right;
 }
 }
 return root;
}
```

**Time Complexity**: O(n) where n is the number of nodes (we may need to traverse all nodes to find the insertion point)
**Space Complexity**: O(n) for the queue in worst case

## 2. Tree Traversals

Traversal refers to the process of visiting each node in the tree exactly once. There are three primary traversal strategies, distinguished by the order in which the root node is processed relative to its subtrees.

### 2.1 Preorder Traversal (Root-Left-Right)

**Algorithm**: Process root → Traverse left subtree → Traverse right subtree

```c
void preorder(struct TreeNode* root) {
 if (root == NULL) return;
 printf("%d ", root->data); // Visit root
 preorder(root->left); // Traverse left subtree
 preorder(root->right); // Traverse right subtree
}
```

**Use Cases**: Creating a copy of the tree, getting prefix expression of an expression tree

### 2.2 Inorder Traversal (Left-Root-Right)

**Algorithm**: Traverse left subtree → Process root → Traverse right subtree

```c
void inorder(struct TreeNode* root) {
 if (root == NULL) return;
 inorder(root->left); // Traverse left subtree
 printf("%d ", root->data); // Visit root
 inorder(root->right); // Traverse right subtree
}
```

**Use Cases**: Getting nodes in sorted order (for BST), getting infix expression of an expression tree

### 2.3 Postorder Traversal (Left-Right-Root)

**Algorithm**: Traverse left subtree → Traverse right subtree → Process root

```c
void postorder(struct TreeNode* root) {
 if (root == NULL) return;
 postorder(root->left); // Traverse left subtree
 postorder(root->right); // Traverse right subtree
 printf("%d ", root->data); // Visit root
}
```

**Use Cases**: Deleting a tree (must delete children before parent), getting postfix expression of an expression tree

### Traversal Example

For a tree with root value 10, left child 5, right child 15, and 5's left child 3:

```
 10
 / \
 5 15
 /
 3
```

- **Preorder**: 10, 5, 3, 15
- **Inorder**: 3, 5, 10, 15
- **Postorder**: 3, 5, 15, 10

**Time Complexity**: O(n) for all traversals (each node visited exactly once)
**Space Complexity**: O(h) where h is the height of the tree (due to recursion stack)

## 3. Tree Searching

### Theory

Searching in a general binary tree requires examining nodes systematically until the target value is found or all nodes have been visited. Unlike Binary Search Trees, we cannot leverage the ordering property to eliminate half the search space.

### Algorithm

```c
struct TreeNode* search(struct TreeNode* root, int key) {
 // Base case: root is NULL or key is found at root
 if (root == NULL || root->data == key) {
 return root;
 }

 // Search in left subtree
 struct TreeNode* result = search(root->left, key);
 if (result != NULL) {
 return result;
 }

 // Search in right subtree
 return search(root->right, key);
}
```

### Iterative Version

```c
struct TreeNode* searchIterative(struct TreeNode* root, int key) {
 while (root != NULL) {
 if (root->data == key) {
 return root;
 } else if (key < root->data) {
 root = root->left;
 } else {
 root = root->right;
 }
 }
 return NULL;
}
```

**Time Complexity**: O(n) in worst case (traversing all nodes)
**Space Complexity**: O(h) for recursive version, O(1) for iterative version

## 4. Tree Copying

### Theory

Creating a copy of a binary tree involves creating new nodes with identical values while preserving the original tree's structure. This is known as a deep copy—the new tree is completely independent of the original.

### Algorithm

Tree copying is naturally expressed using preorder traversal: create the root, then recursively copy the left subtree, then recursively copy the right subtree.

```c
struct TreeNode* copyTree(struct TreeNode* root) {
 if (root == NULL) {
 return NULL;
 }

 // Create new node with same data
 struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 newNode->data = root->data;

 // Recursively copy subtrees
 newNode->left = copyTree(root->left);
 newNode->right = copyTree(root->right);

 return newNode;
}
```

### Verification Function

To verify the copy was successful, compare both structure and data:

```c
int areIdentical(struct TreeNode* tree1, struct TreeNode* tree2) {
 if (tree1 == NULL && tree2 == NULL) {
 return 1;
 }
 if (tree1 == NULL || tree2 == NULL) {
 return 0;
 }
 return (tree1->data == tree2->data) &&
 areIdentical(tree1->left, tree2->left) &&
 areIdentical(tree1->right, tree2->right);
}
```

**Time Complexity**: O(n) where n is the number of nodes (each node visited once)
**Space Complexity**: O(h) for recursion stack + O(n) for new tree nodes

## Complexity Summary

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Insertion | O(n)            | O(n)             |
| Preorder  | O(n)            | O(h)             |
| Inorder   | O(n)            | O(h)             |
| Postorder | O(n)            | O(h)             |
| Search    | O(n)            | O(h)             |
| Copy      | O(n)            | O(n)             |

where n = number of nodes, h = height of tree

## Conclusion

The fundamental operations on binary trees—insertion, traversal, searching, and copying—demonstrate the recursive nature of tree structures. These operations provide the building blocks for more advanced tree applications and are essential for understanding hierarchical data organization in computer science.
