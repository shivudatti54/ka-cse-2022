# Connected Components

## Overview

A connected component of an undirected graph is a maximal set of vertices such that there is a path between every pair of vertices in the set. Understanding connected components is essential for analyzing the structure of networks and identifying isolated clusters. In directed graphs, strongly connected components (SCCs) are maximal sets of vertices with directed paths in both directions.

## Key Points

- A connected graph has exactly one connected component.
- A disconnected graph has two or more connected components.
- Finding connected components uses DFS/BFS with a loop over all vertices.
- Kosaraju's algorithm finds SCCs in directed graphs using two DFS passes and graph transposition.
- The condensation graph, obtained by collapsing SCCs, is always a DAG.
- Adding an edge can merge two components or SCCs.
- Removing an edge can split a component or SCC.

## Important Definitions

- **Connected Component**: A maximal connected subgraph in an undirected graph.
- **Strongly Connected Component (SCC)**: A maximal set of vertices in a directed graph with directed paths in both directions.
- **Condensation Graph**: A graph obtained by collapsing SCCs into single vertices.

## Key Formulas / Syntax

- DFS/BFS for finding connected components: `FindConnectedComponents(Graph G)`
- Kosaraju's algorithm for finding SCCs: `Kosaraju(Graph G)`

## Comparisons

| Property        | Undirected Graph           | Directed Graph                      |
| --------------- | -------------------------- | ----------------------------------- |
| Definition      | Maximal connected subgraph | Maximal strongly connected subgraph |
| Algorithm       | Single DFS/BFS             | Kosaraju's or Tarjan's              |
| Time complexity | O(V + E)                   | O(V + E)                            |

## Exam Tips

- Know the definition of connected components and SCCs.
- Understand the algorithms for finding connected components and SCCs.
- Remember the time complexity for both undirected and directed graphs.
- Be able to count the number of connected components.
- Emphasize "maximal" in your answers when defining connected components and SCCs.
- Recall that the condensation graph is always a DAG.
