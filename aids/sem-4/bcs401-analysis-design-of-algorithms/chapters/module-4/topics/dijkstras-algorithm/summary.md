# Dijkstra's Algorithm - Summary

## Key Definitions and Concepts

- **Single-Source Shortest Path Problem**: Finding the shortest path from one source vertex to all other vertices in a weighted graph.
- **Greedy Method**: An algorithmic paradigm that makes locally optimal choices at each step hoping for a global optimum.
- **Relaxation**: The operation of updating a vertex's distance if a shorter path is found through an intermediate vertex.
- **Priority Queue**: A data structure that always provides access to the vertex with minimum distance value.

## Important Formulas and Theorems

- **Relaxation Formula**: If dist[u] + w(u,v) < dist[v], then set dist[v] = dist[u] + w(u,v)
- **Time Complexity with Array**: O(V²) — suitable for dense graphs
- **Time Complexity with Binary Heap**: O((V + E) log V) — suitable for sparse graphs
- **Time Complexity with Fibonacci Heap**: O(E + V log V) — optimal for very sparse graphs

## Key Points

- DIJKSTRA'S ALGORITHM FINDS SHORTEST PATHS FROM A SINGLE SOURCE TO ALL OTHER VERTICES.

- THE ALGORITHM WORKS ONLY WITH NON-NEGATIVE EDGE WEIGHTS — this is essential for correctness.

- IT IS A GREEDY ALGORITHM because it always selects the vertex with minimum current distance.

- THE ALGORITHM MAINTAINS A SET S of vertices whose shortest distance has been finalized.

- EACH VERTEX IS SELECTED EXACTLY ONCE when its minimum distance is determined.

- DISTANCE VALUES CAN ONLY DECREASE during algorithm execution, never increase.

- A VERTEX ADDED TO S HAS ITS FINAL SHORTEST PATH DISTANCE determined.

## Common Mistakes to Avoid

- APPLYING DIJKSTRA'S TO GRAPHS WITH NEGATIVE WEIGHTS — this produces incorrect results.

- FORGETTING TO INITIALIZE SOURCE DISTANCE TO ZERO and all others to infinity.

- NOT CHECKING WHETHER A VERTEX IS ALREADY IN SET S before relaxing edges.

- CONFUSING DIJKSTRA WITH BFS — BFS is for unweighted graphs only.

- NOT UPDATING THE PRIORiTY QUEUE properly when distances are improved.

## Revision Tips

- PRACTICE TRACING THE ALGORITHM on at least 3-4 different graph examples to build confidence.

- MEMORIZE THE RELAXATION FORMULA as it is the core operation tested in exams.

- UNDERSTAND WHY NEGATIVE WEIGHTS BREAK THE ALGORITHM — this frequently appears in multiple choice questions.

- BE ABLE TO DRAW THE EXECUTION TABLE showing dist values and selected vertices at each iteration.

- COMPARE WITH KRUSKAL'S AND PRIM'S to understand the greedy method pattern across different algorithms.