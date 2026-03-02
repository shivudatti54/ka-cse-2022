# Uninformed Search Strategies

Uninformed search strategies are a type of search algorithm used in artificial intelligence to find a path between two nodes in a graph or network. These strategies do not use any additional information about the graph, such as heuristic functions, to guide the search.

## Introduction to Uninformed Search

Uninformed search strategies are also known as blind search or uninformed search. They work by exploring all possible paths from the starting node to the goal node, without using any additional information about the graph.

### Types of Uninformed Search Strategies

There are several types of uninformed search strategies, including:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Depth-Limited Search (DLS)
- Iterative Deepening Depth-First Search (IDDFS)

## Breadth-First Search (BFS)

Breadth-First Search is a search strategy that explores all nodes at a given depth before moving on to the next depth level. It uses a queue data structure to keep track of the nodes to be visited.

### Example of BFS

Suppose we have a graph with the following nodes and edges:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

The BFS traversal of this graph would be: A, B, C, D, E, F

### ASCII Diagram of BFS

```
+---+---+---+---+---+
| A | B | C | D | E |
+---+---+---+---+---+
|   | / \ |   | / \ |
|   |/   \|   |/   \|
|  D     E  F     |
+---+---+---+---+---+
```

## Depth-First Search (DFS)

Depth-First Search is a search strategy that explores as far as possible along each branch before backtracking. It uses a stack data structure to keep track of the nodes to be visited.

### Example of DFS

Suppose we have a graph with the following nodes and edges:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

The DFS traversal of this graph would be: A, B, D, E, C, F

### ASCII Diagram of DFS

```
+---+---+---+---+---+
| A | B | C | D | E |
+---+---+---+---+---+
|   | / \ |   | / \ |
|   |/   \|   |/   \|
|  D     E  F     |
+---+---+---+---+---+
```

## Uniform-Cost Search (UCS)

Uniform-Cost Search is a search strategy that explores the nodes with the lowest cost first. It uses a priority queue data structure to keep track of the nodes to be visited.

### Example of UCS

Suppose we have a graph with the following nodes and edges:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

The UCS traversal of this graph would be: A, B, D, E, C, F

### ASCII Diagram of UCS

```
+---+---+---+---+---+
| A | B | C | D | E |
+---+---+---+---+---+
|   | / \ |   | / \ |
|   |/   \|   |/   \|
|  D     E  F     |
+---+---+---+---+---+
```

## Depth-Limited Search (DLS)

Depth-Limited Search is a search strategy that explores the nodes up to a certain depth limit. It uses a stack data structure to keep track of the nodes to be visited.

### Example of DLS

Suppose we have a graph with the following nodes and edges:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

The DLS traversal of this graph with a depth limit of 2 would be: A, B, C

### ASCII Diagram of DLS

```
+---+---+---+---+---+
| A | B | C | D | E |
+---+---+---+---+---+
|   | / \ |   | / \ |
|   |/   \|   |/   \|
|  D     E  F     |
+---+---+---+---+---+
```

## Iterative Deepening Depth-First Search (IDDFS)

Iterative Deepening Depth-First Search is a search strategy that combines the benefits of BFS and DFS. It uses a stack data structure to keep track of the nodes to be visited.

### Example of IDDFS

Suppose we have a graph with the following nodes and edges:

```
    A
   / \
  B   C
 / \   \
D   E   F
```

The IDDFS traversal of this graph would be: A, B, D, E, C, F

### ASCII Diagram of IDDFS

```
+---+---+---+---+---+
| A | B | C | D | E |
+---+---+---+---+---+
|   | / \ |   | / \ |
|   |/   \|   |/   \|
|  D     E  F     |
+---+---+---+---+---+
```

## Comparison of Uninformed Search Strategies

The following table compares the different uninformed search strategies:

| Strategy | Time Complexity | Space Complexity |
| -------- | --------------- | ---------------- |
| BFS      | O(b^d)          | O(b^d)           |
| DFS      | O(b^d)          | O(d)             |
| UCS      | O(b^d)          | O(b^d)           |
| DLS      | O(b^l)          | O(l)             |
| IDDFS    | O(b^d)          | O(d)             |

## Exam Tips

- Make sure to understand the different types of uninformed search strategies and their characteristics.
- Practice solving problems using each of the search strategies.
- Be able to compare and contrast the different search strategies.
- Make sure to understand the time and space complexity of each search strategy.
