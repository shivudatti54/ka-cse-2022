# BST Operations

## Introduction to Binary Search Trees

A **Binary Search Tree (BST)** is a specialized binary tree data structure that follows a specific ordering property. In a BST, for any given node:

- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than the node's value
- Both left and right subtrees are also binary search trees

This ordering property makes BSTs extremely efficient for search operations, with average time complexity of O(log n) for insertion, deletion, and search operations.

## Basic Structure of BST Nodes

Each node in a BST typically contains three components:

- Data value (key)
- Pointer to left child
- Pointer to right child

In C, this can be represented as:

```c
struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};
```

## Key BST Operations

### 1. Insertion Operation

The insertion operation adds a new node to the BST while maintaining the BST property.

**Algorithm:**

1. Start from the root node
2. Compare the new value with the current node's value
3. If the new value is less, go to the left subtree
4. If the new value is greater, go to the right subtree
5. Repeat until you find an empty position (NULL pointer)
6. Insert the new node at that position

**Example:**
Insert values: 50, 30, 70, 20, 40, 60, 80

```
Step 1: Insert 50
    50

Step 2: Insert 30 (30 < 50, so left child)
    50
   /
  30

Step 3: Insert 70 (70 > 50, so right child)
    50
   /  \
  30   70

Step 4: Insert 20 (20 < 50, then 20 < 30, so left of 30)
    50
   /  \
  30   70
 /
20

Step 5: Insert 40 (40 < 50, then 40 > 30, so right of 30)
    50
   /  \
  30   70
 /  \
20   40

Step 6: Insert 60 (60 > 50, then 60 < 70, so left of 70)
    50
   /  \
  30   70
 /  \  /
20  40 60

Step 7: Insert 80 (80 > 50, then 80 > 70, so right of 70)
    50
   /  \
  30   70
 /  \  / \
20  40 60 80
```

**C Implementation:**

```c
struct TreeNode* insert(struct TreeNode* root, int value) {
    if (root == NULL) {
        struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newNode->data = value;
        newNode->left = NULL;
        newNode->right = NULL;
        return newNode;
    }

    if (value < root->data) {
        root->left = insert(root->left, value);
    } else if (value > root->data) {
        root->right = insert(root->right, value);
    }

    return root;
}
```

### 2. Search Operation

The search operation checks if a value exists in the BST by leveraging the BST property.

**Algorithm:**

1. Start from the root node
2. Compare the search value with the current node's value
3. If equal, return the node (found)
4. If less, search in the left subtree
5. If greater, search in the right subtree
6. If NULL is reached, value doesn't exist

**Example:**
Search for 40 in the BST created above:

- 40 < 50 → go left to 30
- 40 > 30 → go right to 40
- Found!

**C Implementation:**

```c
struct TreeNode* search(struct TreeNode* root, int value) {
    if (root == NULL || root->data == value) {
        return root;
    }

    if (value < root->data) {
        return search(root->left, value);
    } else {
        return search(root->right, value);
    }
}
```

### 3. Finding Minimum and Maximum Values

**Minimum Value:**
The minimum value is always in the leftmost node of the BST.

**Maximum Value:**
The maximum value is always in the rightmost node of the BST.

**C Implementation:**

```c
// Find minimum value
struct TreeNode* findMin(struct TreeNode* root) {
    if (root == NULL) return NULL;
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Find maximum value
struct TreeNode* findMax(struct TreeNode* root) {
    if (root == NULL) return NULL;
    while (root->right != NULL) {
        root = root->right;
    }
    return root;
}
```

### 4. Deletion Operation

Deletion is the most complex BST operation with three cases to consider:

**Case 1: Node to be deleted has no children (Leaf node)**

- Simply remove the node by setting its parent's pointer to NULL

**Case 2: Node to be deleted has one child**

- Replace the node with its child

**Case 3: Node to be deleted has two children**

- Find the inorder successor (minimum value in right subtree) or inorder predecessor (maximum value in left subtree)
- Copy the value of the inorder successor to the node
- Delete the inorder successor

**Example:**
Delete node with value 30 from our BST:

```
Original BST:
    50
   /  \
  30   70
 /  \  / \
20  40 60 80

Case: Node has two children (20 and 40)
Find inorder successor: 40 (minimum in right subtree)
Copy 40 to 30's position, then delete original 40

Result:
    50
   /  \
  40   70
 /     / \
20    60 80
```

**C Implementation:**

```c
struct TreeNode* deleteNode(struct TreeNode* root, int value) {
    if (root == NULL) return root;

    if (value < root->data) {
        root->left = deleteNode(root->left, value);
    } else if (value > root->data) {
        root->right = deleteNode(root->right, value);
    } else {
        // Node with only one child or no child
        if (root->left == NULL) {
            struct TreeNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct TreeNode* temp = root->left;
            free(root);
            return temp;
        }

        // Node with two children
        struct TreeNode* temp = findMin(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}
```

### 5. Counting Nodes

Count the total number of nodes in the BST using recursive traversal.

**C Implementation:**

```c
int countNodes(struct TreeNode* root) {
    if (root == NULL) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}
```

## Traversal Methods

BSTs support all binary tree traversal methods:

| Traversal Type | Order             | Application                    |
| -------------- | ----------------- | ------------------------------ |
| Inorder        | Left, Root, Right | Returns values in sorted order |
| Preorder       | Root, Left, Right | Useful for copying trees       |
| Postorder      | Left, Right, Root | Useful for deleting trees      |
| Level-order    | Level by level    | Breadth-first search           |

**Inorder Traversal (Sorted Output):**

```c
void inorder(struct TreeNode* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}
// Output: 20 30 40 50 60 70 80
```

## Time Complexity Analysis

| Operation | Average Case | Worst Case (Skewed Tree) |
| --------- | ------------ | ------------------------ |
| Insertion | O(log n)     | O(n)                     |
| Search    | O(log n)     | O(n)                     |
| Deletion  | O(log n)     | O(n)                     |
| Min/Max   | O(log n)     | O(n)                     |

## Balanced vs Unbalanced BSTs

| Characteristic  | Balanced BST                        | Unbalanced BST              |
| --------------- | ----------------------------------- | --------------------------- |
| Shape           | Approximately equal height subtrees | Resembles a linked list     |
| Time Complexity | O(log n) for all operations         | O(n) for all operations     |
| Examples        | AVL trees, Red-Black trees          | Basic BST without balancing |

## Applications of BSTs

1. **Database Systems:** For efficient indexing and searching
2. **File Systems:** For directory structures
3. **Symbol Tables:** In compilers and interpreters
4. **Priority Queues:** Using heap data structure (special type of BST)
5. **Network Routing:** For storing routing tables

## Exam Tips

1. **Remember the BST property:** Left < Root < Right for all nodes
2. **Practice drawing:** Visualize insertion, deletion, and search operations
3. **Understand deletion cases:** The three cases for deletion are crucial
4. **Time complexity:** Know when BST operations become O(n) vs O(log n)
5. **Recursive thinking:** Most BST operations are naturally recursive
6. **Edge cases:** Always consider empty trees and single-node trees
7. **Memory management:** Remember to free memory in deletion operations
