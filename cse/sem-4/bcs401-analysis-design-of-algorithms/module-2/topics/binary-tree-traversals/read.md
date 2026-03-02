# Binary Tree Traversals

## Table of Contents

- [Binary Tree Traversals](#binary-tree-traversals)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Formal Definition of Binary Tree Traversal](#formal-definition-of-binary-tree-traversal)
  - [Recursive Implementation Analysis](#recursive-implementation-analysis)
  - [Iterative Implementations](#iterative-implementations)
  - [Morris Traversal: O(1) Space Algorithm](#morris-traversal-o1-space-algorithm)
  - [Level-Order Traversal (Breadth-First)](#level-order-traversal-breadth-first)
- [Examples](#examples)
  - [Example 1: Traversing an Expression Tree](#example-1-traversing-an-expression-tree)
  - [Example 2: Tree Construction from Traversals](#example-2-tree-construction-from-traversals)
  - [Example 3: Analysis of Skewed vs. Balanced Tree](#example-3-analysis-of-skewed-vs-balanced-tree)
- [Exam Tips](#exam-tips)

## Introduction

Binary tree traversals constitute fundamental algorithmic procedures in computer science for systematically visiting all nodes in a binary tree structure. A binary tree is a hierarchical data structure composed of nodes, where each node contains at most two children referred to as the left child and right child. The traversal problem requires visiting each node exactly once in a specific order, which is essential for numerous applications including expression tree evaluation, serialization/deserialization of trees, binary search tree operations, and tree-based algorithmic solutions.

From an algorithm design perspective, tree traversals exemplify the principle of systematic exploration of structured data. While the module context mentions brute force approaches, tree traversals represent a more structured algorithmic pattern where the recursive nature of trees naturally leads to elegant divide-and-conquer solutions. The analysis of traversal algorithms provides rich ground for complexity analysis, demonstrating how recursive algorithms interact with tree structures to achieve O(n) time complexity for visiting n nodes.

This topic examines four primary traversal strategies: preorder, inorder, postorder, and level-order traversals. Each strategy produces a distinct node visitation order with specific applications in solving computational problems. The formal analysis of these algorithms involves establishing correctness through induction and deriving tight bounds on time and space complexity.

## Key Concepts

### Formal Definition of Binary Tree Traversal

A binary tree T is either empty (null) or consists of a root node r and two subtrees T_L (left subtree) and T_R (right subtree). A traversal is a systematic procedure that applies an operation visit(r) to each node r in the tree exactly once. The four fundamental traversals differ in the relative order of visiting the root, left subtree, and right subtree:

**Preorder (Root-Left-Right):** visit(r), traverse(T_L), traverse(T_R)

**Inorder (Left-Root-Right):** traverse(T_L), visit(r), traverse(T_R)

**Postorder (Left-Right-Root):** traverse(T_L), traverse(T_R), visit(r)

**Level-order (Breadth-First):** Visit all nodes at depth d before visiting nodes at depth d+1

### Recursive Implementation Analysis

The recursive implementations leverage the recursive definition of binary trees. Consider the preorder traversal algorithm:

```
PREORDER(node):
 if node = null then return
 visit(node)
 PREORDER(node.left)
 PREORDER(node.right)
```

**Theorem:** Preorder traversal visits each of the n nodes in a binary tree exactly once.

_Proof by Structural Induction:_

- **Base Case:** For an empty tree (null), the algorithm returns without visiting any nodes, which is correct as there are no nodes to visit.
- **Inductive Hypothesis:** Assume the algorithm correctly traverses a tree with k nodes.
- **Inductive Step:** Consider a tree with k+1 nodes, having root r, left subtree L with l nodes, and right subtree R with r nodes where l + r + 1 = k + 1. The algorithm first visits r, then recursively traverses L (which by hypothesis visits exactly l nodes), then recursively traverses R (which by hypothesis visits exactly r nodes). Thus, the total visited is 1 + l + r = k + 1 nodes, establishing correctness. ∎

**Time Complexity Analysis:** Each node is visited exactly once, and each recursive call involves O(1) work. For a tree with n nodes, the total time is Θ(n). This is a tight bound as every node must be visited to complete the traversal.

**Space Complexity Analysis:** The recursive implementation uses the system call stack. In the worst case (a skewed tree of height h = n), the recursion depth is n, requiring O(n) space. In the best case (a complete binary tree where height h = ⌊log₂n⌋), the space complexity is O(log n). Therefore, the auxiliary space is O(h) where h is the height of the tree.

### Iterative Implementations

Recursive implementations can be transformed to iterative versions using explicit stacks, which provides better control over memory usage in environments with limited stack space.

**Iterative Inorder Traversal:**

```
ITERATIVE_INORDER(root):
 stack = empty stack
 current = root
 while current ≠ null OR stack not empty:
 while current ≠ null:
 stack.push(current)
 current = current.left
 current = stack.pop()
 visit(current)
 current = current.right
```

**Analysis:** The iterative version maintains the same time complexity Θ(n) but requires explicit stack management. The maximum stack size equals the tree height h, giving O(h) space complexity.

### Morris Traversal: O(1) Space Algorithm

Morris traversal achieves inorder traversal without recursion or explicit stack by temporarily modifying the tree structure using thread pointers.

```
MORRIS_INORDER(root):
 current = root
 while current ≠ null:
 if current.left = null:
 visit(current)
 current = current.right
 else:
 predecessor = current.left
 while predecessor.right ≠ null AND predecessor.right ≠ current:
 predecessor = predecessor.right
 if predecessor.right = null:
 predecessor.right = current
 current = current.left
 else:
 predecessor.right = null
 visit(current)
 current = current.right
```

**Space Complexity:** O(1) - only uses a constant number of pointers regardless of tree height.

**Time Complexity:** Each edge is traversed at most twice (once going left, once going right when creating threads, and again when removing threads), resulting in O(n) time.

### Level-Order Traversal (Breadth-First)

Level-order traversal uses a queue data structure to process nodes breadth-first:

```
LEVEL_ORDER(root):
 if root = null then return
 queue = new Queue
 queue.enqueue(root)
 while queue not empty:
 node = queue.dequeue()
 visit(node)
 if node.left ≠ null: queue.enqueue(node.left)
 if node.right ≠ null: queue.enqueue(node.right)
```

**Complexity Analysis:** Each node is enqueued and dequeued exactly once, with O(1) work per operation. Time complexity is Θ(n). The queue holds at most one level of nodes, which in a complete binary tree is at most n/2 nodes, giving O(n) space in worst case, or O(w) where w is the maximum width of the tree.

## Examples

### Example 1: Traversing an Expression Tree

Consider the expression tree for (3 + 4) \* (5 - 2):

```
 *
 / \
 + -
 / \ / \
 3 4 5 2
```

**Inorder traversal** produces: 3 + 4 \* 5 - 2 (infix notation without parentheses - note operator precedence from tree structure)

**Preorder traversal** produces: \* + 3 4 - 5 2 (prefix notation)

**Postorder traversal** produces: 3 4 + 5 2 - \* (postfix notation - used in stack-based expression evaluation)

The postorder traversal is particularly useful for expression evaluation using a stack: scan left-to-right, push operands, pop two operands when encountering an operator, compute, and push result.

### Example 2: Tree Construction from Traversals

Given a binary tree with preorder: A, B, D, E, C, F and inorder: D, B, E, A, C, F, we can reconstruct the tree.

**Solution:**

- Preorder: Root → Left subtree → Right subtree (first element is root: A)
- Inorder: Left subtree → Root → Right subtree (A divides inorder into left: D,B,E and right: C,F)

From preorder sequence after A, we get B as root of left subtree. In inorder left part D,B,E shows B with D (left) and E (right). Continuing this process recursively, we construct:

```
 A
 / \
 B C
 / \ \
 D E F
```

### Example 3: Analysis of Skewed vs. Balanced Tree

For a tree with n nodes:

| Tree Type            | Height (h) | Recursive Space | Iterative Space (Stack/Queue) |
| -------------------- | ---------- | --------------- | ----------------------------- |
| Skewed (linked list) | n          | O(n)            | O(n)                          |
| Complete binary      | ⌊log₂n⌋    | O(log n)        | O(n/2) worst case             |
| Balanced             | O(log n)   | O(log n)        | O(log n)                      |

For n = 1000 nodes in a complete binary tree: height ≈ 10, recursive space ≈ 10, but queue might hold ≈ 500 nodes at the deepest level.

## Exam Tips

1. **Remember the mnemonics:** Preorder (Root First), Inorder (Root in Middle), Postorder (Root Last), Level-order (Breadth-First - like water filling the tree).

2. **Tree height matters for space complexity:** Always consider whether the tree is balanced, complete, or skewed when analyzing space requirements.

3. **Morris traversal is the only O(1) space inorder traversal:** Know that it modifies tree temporarily but restores it completely.

4. **Postorder is essential for deletion:** When deallocating tree nodes or evaluating postfix expressions, postorder ensures children are processed before parents.

5. **Level-order requires a queue:** Unlike stack-based recursive/iterative depth-first approaches, BFS inherently needs a queue.

6. **Constructing trees from traversals:** With any two of preorder, inorder, and postorder, you can uniquely reconstruct a binary tree (if all node values are distinct).

7. **Expression trees:** Remember that inorder gives infix, preorder gives prefix, and postorder gives postfix notation - each with different evaluation strategies.
