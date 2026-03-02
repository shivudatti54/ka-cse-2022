# **Depth First Search**

## **Table of Contents**

1. [Introduction](#introduction)
2. [What is Depth First Search?](#what-is-depth-first-search)
3. [Types of Depth First Search](#types-of-depth-first-search)
4. [How Depth First Search Works](#how-depth-first-search-works)
5. [Example Use Cases](#example-use-cases)
6. [Code Implementation](#code-implementation)

## **Introduction**

Depth First Search (DFS) is a fundamental algorithm used in graph theory and search problems. It is a popular choice for solving problems that involve traversing or searching through a graph or tree. In this study material, we will explore the concepts, types, and implementation of Depth First Search.

## **What is Depth First Search?**

Depth First Search is a traversal algorithm that visits a node in a graph or tree and explores as far as possible along each branch before backtracking. The algorithm starts at the root node and explores the graph depth-first, visiting each node and edge in a particular order.

## **Types of Depth First Search**

There are several types of Depth First Search algorithms, including:

- **In-Order DFS**: Visits the left subtree, the current node, and then the right subtree.
- **Pre-Order DFS**: Visits the current node, then the left subtree, and finally the right subtree.
- **Post-Order DFS**: Visits the left subtree, the right subtree, and then the current node.

## **How Depth First Search Works**

The following are the steps involved in a Depth First Search algorithm:

1.  **Choose a starting node**: Select a node in the graph to start the search from.
2.  **Mark the node as visited**: Keep track of the nodes that have been visited to avoid revisiting them.
3.  **Explore the neighbors**: Visit each neighbor of the current node and mark them as visited.
4.  **Backtrack**: If the current node has no unvisited neighbors, backtrack to the previous node and repeat the process.

## **Example Use Cases**

Depth First Search has several applications in computer science and other fields, including:

- **Topological sorting**: Sorts the nodes of a directed acyclic graph (DAG) based on their finish times.
- **Finding connected components**: Identifies connected subgraphs in an undirected graph.
- **Testing whether a graph is connected**: Determines whether a graph contains a path between any two nodes.

## **Code Implementation**

Here is an example implementation of a Depth First Search algorithm in Python:

```python
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def dfs(self, start_node):
        visited = [False] * self.vertices
        traversal_order = []

        def dfs_helper(node):
            visited[node] = True
            traversal_order.append(node)
            for neighbor in self.adjacency_list[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)

        dfs_helper(start_node)
        return traversal_order


# Create a graph with 5 vertices
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

# Perform DFS traversal starting from node 0
traversal_order = graph.dfs(0)
print("Depth First Search Traversal Order:", traversal_order)
```

This code defines a Graph class with methods to add edges and perform a Depth First Search traversal. The `dfs` method uses a recursive helper function to explore the graph depth-first. The example use case demonstrates how to create a graph, add edges, and perform a DFS traversal starting from node 0.
