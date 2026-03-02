# Bi-connected Components

## Overview

A biconnected graph is a connected graph that remains connected even after the removal of any single vertex. Biconnected components are maximal biconnected subgraphs of a graph. Understanding biconnectivity is crucial for assessing the reliability and fault-tolerance of networks.

## Key Points

- A **biconnected graph** has no articulation points and remains connected after any single vertex removal.
- An **articulation point** is a vertex whose removal increases the number of connected components.
- A **bridge** is an edge whose removal increases the number of connected components.
- **Biconnected components** are maximal biconnected subgraphs, with each edge belonging to exactly one component.
- Two biconnected components share at most one vertex, which is an articulation point.

## Important Definitions

- **Articulation Point**: A vertex whose removal increases the number of connected components.
- **Bridge**: An edge whose removal increases the number of connected components.
- **Biconnected Component**: A maximal biconnected subgraph.
- **Biconnected Graph**: A connected graph with no articulation points.

## Key Formulas / Syntax

- `low[v] = min(disc[v], disc[w], low[child])` for computing the low value of a vertex.
- `disc[v]`: The discovery time of vertex v during DFS.
- `low[v]`: The lowest discovery time reachable from the subtree rooted at v.

## Comparisons

| Property   | Articulation Point                                  | Bridge                                            |
| ---------- | --------------------------------------------------- | ------------------------------------------------- |
| Definition | Vertex whose removal increases connected components | Edge whose removal increases connected components |
| Condition  | `low[child] >= disc[vertex]`                        | `low[v] > disc[u]`                                |

## Exam Tips

- Understand how `disc[]` and `low[]` arrays are computed.
- Remember the articulation point condition: root with 2+ children, or non-root with `low[child] >= disc[vertex]`.
- Practice computing `disc[]` and `low[]` arrays for small graphs.
- Recall the time complexity: O(V + E) for all biconnectivity-related algorithms.
- Focus on the relationship between articulation points and biconnected components.
