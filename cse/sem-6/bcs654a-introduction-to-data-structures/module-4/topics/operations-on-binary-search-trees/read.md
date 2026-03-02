# Binary Search Trees (BST)

## Definition

A **Binary Search Tree** is a binary tree with the following property:

- All nodes in the **left subtree < root**
- All nodes in the **right subtree > root**
- Both subtrees are also BSTs

```
 8
 / \
 3 10
 / \ \
 1 6 14
 / \ /
 4 7 13
```

## BST Property

For any node with value X:

- All values in left subtree < X
- All values in right subtree > X

This enables **O(log n)** search in balanced trees.

## Operations

### Search

```c
struct Node* search(struct Node *root, int key) {
 if(root == NULL || root->data == key)
 return root;

 if(key < root->data)
 return search(root->left, key);
 else
 return search(root->right, key);
}
```

### Insert

```c
struct Node* insert(struct Node *root, int key) {
 if(root == NULL)
 return createNode(key);

 if(key < root->data)
 root->left = insert(root->left, key);
 else if(key > root->data)
 root->right = insert(root->right, key);

 return root;
}
```

### Find Minimum/Maximum

```c
struct Node* findMin(struct Node *root) {
 while(root && root->left)
 root = root->left;
 return root;
}

struct Node* findMax(struct Node *root) {
 while(root && root->right)
 root = root->right;
 return root;
}
```

### Delete

Three cases:

1. **Leaf node** - Simply remove
2. **One child** - Replace with child
3. **Two children** - Replace with inorder successor

```c
struct Node* delete(struct Node *root, int key) {
 if(root == NULL)
 return root;

 if(key < root->data)
 root->left = delete(root->left, key);
 else if(key > root->data)
 root->right = delete(root->right, key);
 else {
 // Found the node

 // Case 1 & 2: No child or one child
 if(root->left == NULL) {
 struct Node *temp = root->right;
 free(root);
 return temp;
 }
 if(root->right == NULL) {
 struct Node *temp = root->left;
 free(root);
 return temp;
 }

 // Case 3: Two children
 struct Node *successor = findMin(root->right);
 root->data = successor->data;
 root->right = delete(root->right, successor->data);
 }
 return root;
}
```

## Time Complexity

| Operation | Average  | Worst (Skewed) |
| --------- | -------- | -------------- |
| Search    | O(log n) | O(n)           |
| Insert    | O(log n) | O(n)           |
| Delete    | O(log n) | O(n)           |
| Min/Max   | O(log n) | O(n)           |

**Space: O(h)** for recursion stack

## Inorder Gives Sorted Order

Inorder traversal of BST gives elements in **ascending order**.

```
 5
 / \
 3 7
 / \ \
 2 4 8

Inorder: 2, 3, 4, 5, 7, 8 (sorted!)
```

## Validate BST

```c
int isBSTUtil(struct Node *root, int min, int max) {
 if(root == NULL)
 return 1;

 if(root->data <= min || root->data >= max)
 return 0;

 return isBSTUtil(root->left, min, root->data) &&
 isBSTUtil(root->right, root->data, max);
}

int isBST(struct Node *root) {
 return isBSTUtil(root, INT_MIN, INT_MAX);
}
```

## Finding Kth Smallest

```c
int kthSmallest(struct Node *root, int *k) {
 if(root == NULL)
 return -1;

 int left = kthSmallest(root->left, k);
 if(*k == 0) return left;

 (*k)--;
 if(*k == 0) return root->data;

 return kthSmallest(root->right, k);
}
```

## Applications

1. **Dictionary** - Word lookup
2. **Database Indexing** - Fast search
3. **Priority Queue** - Can implement with BST
4. **Symbol Tables** - Compiler design
5. **Auto-complete** - Prefix searching

## Key Points

1. **BST Property**: left < root < right
2. **Inorder = Sorted**: Always!
3. **Height matters**: Balanced = O(log n), Skewed = O(n)
4. **Delete is tricky**: Handle 3 cases
5. **No duplicates** in standard BST
