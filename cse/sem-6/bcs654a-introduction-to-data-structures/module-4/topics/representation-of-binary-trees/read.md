# Representation of Binary Trees

## Introduction

Binary trees are hierarchical data structures where each node has at most two children: left and right. Their representation in memory is critical for implementing tree operations efficiently. Two primary methods exist: **linked representation** (using nodes with pointers) and **sequential representation** (using arrays).

The choice of representation affects:

- **Memory efficiency**: Arrays may waste space for incomplete trees
- **Access speed**: Array indices allow O(1) parent/child access
- **Implementation complexity**: Pointers require careful memory management

Linked representation is preferred for dynamic trees with frequent insertions/deletions, while array-based methods excel in complete binary trees (used in heaps). Understanding both methods is essential for algorithm design and optimization in areas like database indexing, compiler construction, and 3D graphics rendering.

## Key Concepts

### 1. Linked Representation

Each node contains:

- Data field
- Left child pointer
- Right child pointer

**C Structure**:

```c
struct TreeNode {
 int data;
 struct TreeNode* left;
 struct TreeNode* right;
};
```

**Example Tree**:

```
 A
 / \
 B C
 / \
 D E
```

**Memory Layout**:

```
A -> left=B, right=C
B -> left=D, right=E
C -> left=NULL, right=NULL
D -> NULL pointers
E -> NULL pointers
```

**Advantages**:

- Dynamic size adjustment
- Natural representation of hierarchical relationships
- Efficient for non-complete trees

**Disadvantages**:

- Extra memory for pointers (4/8 bytes per pointer)
- No random access to parent/children

### 2. Array Representation

Two approaches exist based on tree completeness:

#### a) Complete Binary Trees

- Store elements level by level, left to right
- Index calculations:
- Parent of node at i: ⌊(i-1)/2⌋
- Left child of i: 2i + 1
- Right child of i: 2i + 2

**Example** (Tree with 5 nodes):

```
Indices: 0 1 2 3 4
Values: A B C D E
```

**Tree Structure**:

```
 A (0)
 / \
 B(1) C(2)
 / \
D(3) E(4)
```

#### b) Incomplete Binary Trees

- Use modified array with size parameter
- Empty positions marked with special value (e.g., -1)

**Example**:

```
Indices: 0 1 2 3 4 5
Values: A B -1 D E -1
```

**Tree Structure**:

```
 A
 /
 B
 / \
 D E
```

**Space Complexity**:

- Worst case: O(2^h) for height h
- Efficient only for near-complete trees

## Examples

### Example 1: Linked Representation Construction

**Problem**: Create the following tree using linked nodes:

```
 10
 / \
 5 20
 / \
 3 7
```

**Solution**:

1. Create root node (10)
2. Create left child (5) and right child (20)
3. Add left (3) and right (7) to node 5

**C Code**:

```c
struct TreeNode* createTree() {
 struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 root->data = 10;

 root->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 root->left->data = 5;

 root->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 root->right->data = 20;

 root->left->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 root->left->left->data = 3;
 root->left->left->left = root->left->left->right = NULL;

 root->left->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
 root->left->right->data = 7;
 root->left->right->left = root->left->right->right = NULL;

 return root;
}
```

### Example 2: Array Representation of Complete Tree

**Problem**: Represent this complete tree as an array:

```
 15
 / \
 10 20
 / \ /
 5 12 18
```

**Solution**:

1. Level order traversal: 15, 10, 20, 5, 12, 18
2. Array indices:

```
Index: 0 1 2 3 4 5
Value: 15 10 20 5 12 18
```

**Child Access**:

- Left child of 10 (index 1): 2\*1+1 = 3 (value 5)
- Right child of 10: 2\*1+2 = 4 (value 12)
- Parent of 18 (index 5): ⌊(5-1)/2⌋ = 2 (value 20)

### Example 3: Array for Incomplete Tree

**Problem**: Store this tree using modified array:

```
 25
 \
 30
 /
 28
```

**Solution**:

1. Calculate required size: Height=2 → Max nodes=7 (2^3-1)
2. Mark empty positions with -1:

```
Indices: 0 1 2 3 4 5 6
Values: 25 -1 30 -1 -1 28 -1
```

## Exam Tips

1. **Representation Choice**: Linked vs Array

- Use linked for dynamic trees with frequent modifications
- Use array for complete trees (heaps) or when parent/child access needed

2. **Index Formulas** (Must Memorize):

- Parent(i) = ⌊(i-1)/2⌋
- LeftChild(i) = 2i+1
- RightChild(i) = 2i+2

3. **Space Analysis**:

- Linked: O(n) space + pointer overhead
- Array: O(2^h) space (h = tree height)

4. **Conversion Questions**:

- Practice converting between tree diagrams and array representations
- Handle incomplete trees with placeholder values

5. ** Favorite**:

- Drawing memory diagrams for both representations
- Calculating parent/child indices in array
- Time complexity analysis of operations

6. **Real-World Links**:

- Array: Heap data structure, priority queues
- Linked: File systems, XML parsing

7. **Common Mistakes**:

- Off-by-one errors in index calculations
- Forgetting to initialize pointers to NULL
- Incorrect level order insertion in arrays
