# Binary Search Tree (BST): Insert, Delete, and Search Operations

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction to Binary Search Trees

A **Binary Search Tree (BST)** is a hierarchical data structure that organizes data in a binary tree format with a special ordering property. Each node in a BST has at most two children — a left child and a right child — and the tree satisfies the **binary search property**: the value of every node in the left subtree is less than the node's value, and the value of every node in the right subtree is greater than the node's value.

This hierarchical organization enables efficient search, insertion, and deletion operations, making BSTs fundamental to computer science and database systems.

### Real-World Relevance

Binary Search Trees have numerous practical applications:

- **Database Indexing**: Many database systems use BST variants (like B-trees) to index data for fast retrieval
- **Symbol Tables**: Compilers use BSTs to manage variable names and function definitions
- **Priority Queues**: BSTs can implement priority queue operations efficiently
- **Auto-complete Systems**: Dictionary and prefix-based searching often employ BSTs
- **File Systems**: Directory structures can be represented using tree-like hierarchies

### Delhi University Syllabus Context

This topic aligns with the **Data Structures** paper (Paper III) under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science. Students are expected to understand the implementation and analysis of BST operations, which frequently appear in university examinations.

---

## 2. Structure of a BST Node

Before implementing operations, we must define the structure of a node in a BST:

```c
// Structure definition in C
struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

// Helper function to create a new node
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
```

In Python, this can be represented as:

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

---

## 3. Search Operation in BST

### Concept

The search operation leverages the BST property to eliminate half of the remaining tree at each step. If we're searching for a value `x` in a BST:

1. Start at the root node
2. If the current node is `NULL`, the value doesn't exist (return NOT FOUND)
3. If the current node's key equals `x`, we've found the target (return FOUND)
4. If `x` is less than the current node's key, search in the left subtree
5. If `x` is greater than the current node's key, search in the right subtree

### Algorithm (Iterative Approach)

```
SEARCH(root, key):
    while root ≠ NULL:
        if key == root.key:
            return root        // Found
        else if key < root.key:
            root = root.left   // Go left
        else:
            root = root.right  // Go right
    return NULL                 // Not found
```

### Complete Code Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Iterative Search Function
struct Node* search(struct Node* root, int key) {
    // Base case: root is NULL or key is present at root
    while (root != NULL) {
        if (key == root->key) {
            return root;  // Key found
        }
        // Key is greater, go to right subtree
        if (key > root->key) {
            root = root->right;
        }
        // Key is smaller, go to left subtree
        else {
            root = root->left;
        }
    }
    return NULL;  // Key not found
}

// Recursive Search Function
struct Node* searchRecursive(struct Node* root, int key) {
    // Base case: root is NULL or key is at root
    if (root == NULL || root->key == key) {
        return root;
    }
    
    // Key is greater than root's key
    if (key > root->key) {
        return searchRecursive(root->right, key);
    }
    
    // Key is smaller than root's key
    return searchRecursive(root->left, key);
}

int main() {
    // Construct the BST:
    //        50
    //       /  \
    //      30   70
    //     /  \  /  \
    //    20 40 60 80
    
    struct Node* root = createNode(50);
    root->left = createNode(30);
    root->right = createNode(70);
    root->left->left = createNode(20);
    root->left->right = createNode(40);
    root->right->left = createNode(60);
    root->right->right = createNode(80);
    
    // Search for key 40
    struct Node* result = search(root, 40);
    if (result != NULL) {
        printf("Key %d found in the BST\n", result->key);
    } else {
        printf("Key not found in the BST\n");
    }
    
    // Search for key 90
    result = search(root, 90);
    if (result != NULL) {
        printf("Key %d found in the BST\n", result->key);
    } else {
        printf("Key 90 not found in the BST\n");
    }
    
    return 0;
}
```

### Example Walkthrough

**Given BST:**
```
        50
       /  \
     30    70
    /  \  /  \
   20 40 60 80
```

**Search for 60:**
1. Start at root (50). Is 60 == 50? No. Is 60 > 50? Yes → Go right
2. Current node is 70. Is 60 == 70? No. Is 60 > 70? No → Go left
3. Current node is 60. Is 60 == 60? Yes → **Found!**

**Search for 25:**
1. Start at root (50). Is 25 == 50? No. Is 25 > 50? No → Go left
2. Current node is 30. Is 25 == 30? No. Is 25 > 30? No → Go left
3. Current node is 20. Is 25 == 20? No. Is 25 > 20? Yes → Go right
4. Current node is NULL → **Not Found**

---

## 4. Insert Operation in BST

### Concept

Insertion in a BST follows the same path as search. We find the appropriate leaf position where the new node should be added, maintaining the BST property.

### Algorithm

```
INSERT(root, key):
    // Base case: Found empty position
    if root == NULL:
        return createNode(key)
    
    // If key is smaller, insert in left subtree
    if key < root.key:
        root.left = INSERT(root.left, key)
    
    // If key is greater, insert in right subtree
    else if key > root.key:
        root.right = INSERT(root.right, key)
    
    // Return the unchanged node pointer
    return root
```

### Complete Code Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Recursive Insert Function
struct Node* insert(struct Node* node, int key) {
    // If the tree is empty, create a new node
    if (node == NULL) {
        return createNode(key);
    }
    
    // Otherwise, recur down the tree
    if (key < node->key) {
        node->left = insert(node->left, key);
    }
    else if (key > node->key) {
        node->right = insert(node->right, key);
    }
    // If key already exists, do nothing (no duplicates in standard BST)
    
    return node;
}

// Inorder Traversal to verify insertion
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

int main() {
    struct Node* root = NULL;
    
    // Insert elements
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    insert(root, 60);
    insert(root, 80);
    insert(root, 35);  // New element
    
    printf("Inorder traversal after insertion: ");
    inorder(root);
    printf("\n");
    
    return 0;
}
```

### Example Walkthrough

**Insert 35 into the existing BST:**

```
Initial BST:
        50
       /  \
     30    70
    /  \  /  \
   20 40 60 80

Step 1: Compare 35 with 50. 35 < 50 → Go left to 30
Step 2: Compare 35 with 30. 35 > 30 → Go right to 40
Step 3: Compare 35 with 40. 35 < 40 → Go left (NULL)
Step 4: Insert 35 as left child of 40

Final BST:
        50
       /  \
     30    70
    /  \  /  \
   20 40 60 80
     /
    35
```

---

## 5. Delete Operation in BST

### Concept

Deletion is the most complex BST operation. When deleting a node, three cases arise:

1. **Case 1: Node to delete is a leaf** (no children) - Simply remove the node
2. **Case 2: Node to delete has one child** - Replace the node with its child
3. **Case 3: Node to delete has two children** - Find the inorder successor (smallest in right subtree) or inorder predecessor (largest in left subtree), replace the node's value, and delete the successor/predecessor

### Algorithm

```
DELETE(root, key):
    // Base case
    if root == NULL:
        return NULL
    
    // Search for the node to delete
    if key < root.key:
        root.left = DELETE(root.left, key)
    else if key > root.key:
        root.right = DELETE(root.right, key)
    else:
        // Node found - handle three cases
        
        // Case 1: Leaf node
        if root.left == NULL and root.right == NULL:
            free(root)
            return NULL
        
        // Case 2a: Only right child exists
        if root.left == NULL:
            temp = root.right
            free(root)
            return temp
        
        // Case 2b: Only left child exists
        if root.right == NULL:
            temp = root.left
            free(root)
            return temp
        
        // Case 3: Two children
        // Find inorder successor (smallest in right subtree)
        temp = findMin(root.right)
        root.key = temp.key
        // Delete the inorder successor
        root.right = DELETE(root.right, temp.key)
    
    return root

findMin(node):
    while node.left != NULL:
        node = node.left
    return node
```

### Complete Code Implementation in C

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Find minimum value node in a subtree
struct Node* minValueNode(struct Node* node) {
    struct Node* current = node;
    while (current && current->left != NULL) {
        current = current->left;
    }
    return current;
}

// Delete function
struct Node* deleteNode(struct Node* root, int key) {
    // Base case
    if (root == NULL) {
        return root;
    }
    
    // Search for the node to delete
    if (key < root->key) {
        root->left = deleteNode(root->left, key);
    }
    else if (key > root->key) {
        root->right = deleteNode(root->right, key);
    }
    else {
        // Node to delete found
        
        // Case 1: Leaf node (no children)
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }
        
        // Case 2a: Only right child
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        }
        // Case 2b: Only left child
        else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        
        // Case 3: Two children
        // Find inorder successor (smallest in right subtree)
        struct Node* temp = minValueNode(root->right);
        
        // Copy the inorder successor's value to this node
        root->key = temp->key;
        
        // Delete the inorder successor
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}

// Inorder traversal
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

int main() {
    // Construct BST:
    //        50
    //       /  \
    //     30    70
    //    /  \  /  \
    //   20 40 60 80
    
    struct Node* root = createNode(50);
    root->left = createNode(30);
    root->right = createNode(70);
    root->left->left = createNode(20);
    root->left->right = createNode(40);
    root->right->left = createNode(60);
    root->right->right = createNode(80);
    
    printf("Original BST (Inorder): ");
    inorder(root);
    printf("\n");
    
    // Delete leaf node (20)
    root = deleteNode(root, 20);
    printf("After deleting 20 (leaf): ");
    inorder(root);
    printf("\n");
    
    // Delete node with one child (30)
    root = deleteNode(root, 30);
    printf("After deleting 30 (one child): ");
    inorder(root);
    printf("\n");
    
    // Delete node with two children (50 - root)
    root = deleteNode(root, 50);
    printf("After deleting 50 (root with two children): ");
    inorder(root);
    printf("\n");
    
    return 0;
}
```

### Example Walkthrough - Delete Node with Two Children

**Delete 50 (root with two children) from:**
```
        50
       /  \
     30    70
    /  \  /  \
   20 40 60 80
```

**Process:**
1. Node 50 has two children (30 and 70)
2. Find inorder successor: smallest node in right subtree = 60
3. Replace 50 with 60
4. Delete the original 60 (which is a leaf)

**Result:**
```
        60
       /  \
     30    70
    /  \    \
   20 40    80
```

---

## 6. Time and Space Complexity Analysis

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| **Search** | O(log n) | O(n) |
| **Insert** | O(log n) | O(n) |
| **Delete** | O(log n) | O(n) |
| **Space** | O(n) | O(n) |

### Explanation

- **Average Case (O(log n))**: When the tree is balanced (height ≈ log n), operations require traversing from root to a leaf, which takes log n time.
- **Worst Case (O(n))**: When the tree becomes skewed (essentially a linked list), operations require traversing the entire height of the tree.

---

## 7. Advantages and Disadvantages

### Advantages
- Efficient search, insert, and delete operations (O(log n) average)
- Maintains sorted data automatically
- Supports range queries and ordered traversal
- Simple implementation compared to balanced trees

### Disadvantages
- Performance degrades with unbalanced trees
- No automatic balancing mechanism
- Worst-case O(n) operations for sorted data input

---

## 8. Multiple Choice Questions (MCQs)

### Easy Level

1. **What is the worst-case time complexity of searching in a BST?**
   - A) O(1)
   - B) O(log n)
   - C) O(n)
   - D) O(n log n)
   
   **Answer: C) O(n)**

2. **In a BST, all nodes in the left subtree of a node with value 50 will have values:**
   - A) Greater than 50
   - B) Less than 50
   - C) Equal to 50
   - D) Greater than or equal to 50
   
   **Answer: B) Less than 50**

3. **Which traversal of BST produces sorted output in ascending order?**
   - A) Preorder
   - B) Postorder
   - C) Inorder
   - D) Level order
   
   **Answer: C) Inorder**

### Medium Level

4. **In a BST, what is the inorder successor of the node with the minimum value?**
   - A) The node's parent
   - B) NULL (doesn't exist)
   - C) The node's right child
   - D) The maximum node in the tree
   
   **Answer: B) NULL (doesn't exist)**

5. **When deleting a node with two children from a BST, which node replaces the deleted node?**
   - A) Any child
   - B) Inorder predecessor
   - C) Inorder successor
   - D) Parent node
   
   **Answer: C) Inorder successor**

6. **What happens when you insert duplicate values in a standard BST?**
   - A) They are inserted in both subtrees
   - B) The tree ignores duplicates
   - C) It creates a circular dependency
   - D) The tree becomes unbalanced immediately
   
   **Answer: B) The tree ignores duplicates**

### Hard Level

7. **A BST contains nodes with values 10, 5, 15, 3, 7, 12, 20. If we delete node 15 (which has one child), what will be the resulting inorder sequence?**
   - A) 3, 5, 7, 10, 12, 20
   - B) 3, 5, 7, 10, 12, 15, 20
   - C) 20, 12, 10, 7, 5, 3
   - D) 10, 5, 3, 7, 15, 12, 20
   
   **Answer: A) 3, 5, 7, 10, 12, 20**

8. **Which of the following statements is TRUE about BST delete operation?**
   - A) Deleting a leaf node always requires rebalancing
   - B) Deleting an internal node with one child replaces it with its child
   - C) BST delete operation is always O(log n)
   - D) The inorder predecessor is always in the right subtree
   
   **Answer: B) Deleting an internal node with one child replaces it with its child**

---

## 9. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **BST Property** | Left subtree values < Node value < Right subtree values |
| **Search Time (Average)** | O(log n) - when tree is balanced |
| **Search Time (Worst)** | O(n) - when tree is skewed |
| **Inorder Successor** | Leftmost node in the right subtree (minimum value in right subtree) |
| **Inorder Predecessor** | Rightmost node in the left subtree (maximum value in left subtree) |
| **Leaf Node Deletion** | Simply remove the node; no restructuring needed |
| **One Child Deletion** | Replace the node with its child and remove the child |
| **Two Children Deletion** | Replace with inorder successor, then delete successor |
| **Balanced BST Height** | Approximately log₂(n) for n nodes |
| **Skewed BST** | Degenerates to linked list; O(n) operations |

---

## 10. Key Takeaways

1. **Binary Search Tree (BST)** is a hierarchical data structure with the fundamental property: left subtree < node < right subtree

2. **Search Operation**: Uses the BST property to eliminate half the tree at each step; O(log n) average case

3. **Insert Operation**: Follows the search path to find the correct leaf position; maintains BST property; O(log n) average case

4. **Delete Operation**: Three cases - leaf node (simple removal), one child (replace with child), two children (use inorder successor); O(log n) average case

5. **Time Complexity**: All operations are O(log n) in balanced BST, but degrade to O(n) in worst-case skewed trees

6. **Real-World Applications**: Database indexing, symbol tables, auto-complete systems, and file systems

7. **For Delhi University Exams**: Remember the three deletion cases, inorder traversal for sorted output, and the difference between average and worst-case complexity

8. **Important Note**: Standard BST does not maintain balance automatically; for guaranteed O(log n) performance, self-balancing trees (AVL, Red-Black) are used

---

*Prepared according to NEP 2024 UGCF syllabus for BSc (Hons) Computer Science, Delhi University*