# Minimum Cost Spanning Trees

## Overview

A Minimum Cost Spanning Tree (MST) is a spanning tree of a weighted, connected, undirected graph with the smallest total edge weight. MSTs are fundamental in network design, connecting all nodes at the minimum total cost. Kruskal's and Prim's algorithms are two popular methods for finding MSTs.

## Key Points

- **Kruskal's Algorithm**: Sorts edges by weight, adding the lightest edge that does not create a cycle.
- **Prim's Algorithm**: Starts from any vertex, always adding the cheapest edge connecting the MST to a non-MST vertex.
- **Union-Find**: A data structure used in Kruskal's for cycle detection, optimized with path compression and union by rank.
- **Time Complexity**: Kruskal's = O(E log E), Prim's with matrix = O(V^2), Prim's with binary heap = O(E log V).
- **MST Properties**: An MST always has exactly V - 1 edges, and its total weight is unique for a given graph.
- **Cut Property**: The minimum weight edge crossing any cut must be in the MST, justifying both algorithms' greedy approach.

## Important Definitions

- **Minimum Cost Spanning Tree (MST)**: A spanning tree with the smallest total edge weight.
- **Union-Find**: A data structure for managing sets and detecting cycles.
- **Cut**: A partition of vertices into two sets.

## Key Formulas / Syntax

- **Kruskal's Algorithm Steps**:
  1. Sort all edges by weight.
  2. Initialize an empty MST and Union-Find.
  3. Iterate through sorted edges, adding the lightest edge that does not create a cycle.
- **Prim's Algorithm Steps**:
  1. Start from any vertex.
  2. Initialize an empty MST and priority queue.
  3. Always add the cheapest edge connecting the MST to a non-MST vertex.

## Comparisons

| Feature         | Kruskal's                 | Prim's                      |
| --------------- | ------------------------- | --------------------------- |
| Approach        | Edge-based                | Vertex-based                |
| Data Structure  | Union-Find                | Priority queue/array        |
| Starting Point  | No specific start         | Starts from a chosen vertex |
| Edge Processing | Global (sorted edge list) | Local (neighbors of MST)    |

## Exam Tips

- Know both Kruskal's and Prim's algorithms and be prepared to trace them on any given weighted graph.
- Understand key concepts: sorting edges, Union-Find, cycle detection, and the greedy approach.
- Memorize time complexities for both algorithms.
- Recall MST properties: V - 1 edges, unique total weight, and the cut property.
- Be able to draw the final MST and state its total weight.
