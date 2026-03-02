# Dijkstra's Algorithm

## Introduction

Dijkstra's Algorithm is one of the most important greedy algorithms in computer science, used to solve the single-source shortest path problem in a weighted graph. Named after the Dutch computer scientist Edsger Dijkstra who formulated it in 1956, this algorithm finds the shortest path from a source vertex to all other vertices in a graph with non-negative edge weights. The algorithm is fundamentally based on the greedy method, which means it makes locally optimal choices at each step with the hope of finding a global optimum.

In the context of the University of Delhi's Computer Science curriculum, Dijkstra's Algorithm holds significant importance as it appears in the "Greedy Method" module alongside other algorithms like Prim's and Kruskal's. Understanding this algorithm is crucial not only for theoretical knowledge but also for practical applications in network routing, transportation systems, and various optimization problems. The algorithm's elegance lies in its simplicity and efficiency, making it a staple in competitive programming and technical interviews.

The significance of Dijkstra's Algorithm extends beyond just finding shortest paths. It serves as a foundation for understanding how greedy algorithms work, demonstrating the trade-off between immediate optimal choices and overall solution quality. Unlike dynamic programming which explores all possibilities, Dijkstra's greedy approach selects the vertex with minimum distance at each step, making it computationally efficient for sparse graphs.

## Key Concepts

### Graph Representation

Before understanding Dijkstra's Algorithm, one must be familiar with graph representations. A weighted graph G = (V, E) consists of vertices V and edges E, where each edge has an associated weight representing distance, cost, or time. The algorithm works on graphs represented using adjacency lists or adjacency matrices. For practical implementation, adjacency lists with a priority queue provide the best time complexity.

### The Greedy Approach in Dijkstra's

Dijkstra's Algorithm follows the greedy method paradigm by always selecting the vertex with the minimum current distance value from the unvisited vertices set. This greedy choice is justified by the cut property of MSTs—any edge crossing a cut with minimum weight belongs to some minimum spanning tree. For shortest paths, a similar property holds: the vertex with minimum distance is guaranteed to have its final shortest path distance determined when it is selected.

### Algorithm Steps

The algorithm begins by initializing the distance to the source vertex as zero and all other vertices as infinity. A set S is maintained to track vertices whose shortest distance has been finalized. At each iteration, the algorithm selects vertex u from the priority queue (or unvisited set) with the minimum distance value, adds it to S, and relaxes all edges (u, v) where v is not in S. Relaxation checks if going through u provides a shorter path to v than the current known distance.

### Relaxation Operation

The relaxation operation is the key update mechanism in Dijkstra's Algorithm. If the current distance to v is greater than the distance to u plus the weight of edge (u, v), then the distance to v is updated. This operation can be expressed as: if dist[u] + w(u, v) < dist[v], then dist[v] = dist[u] + w(u, v). This step ensures that the algorithm progressively improves its estimates until all shortest paths are found.

### Time Complexity Considerations

The time complexity of Dijkstra's Algorithm depends heavily on the data structures used. With an array implementation, the complexity is O(V²). Using a binary heap brings it down to O((V + E) log V), while a Fibonacci heap can achieve O(E + V log V). For practical purposes and typical DU exam questions, the O(V²) array-based implementation is most commonly expected, though students should be aware of the heap-based optimization.

### Correctness Conditions

Dijkstra's Algorithm guarantees correct results only when all edge weights are non-negative. If negative weights exist, the algorithm may fail because selecting a vertex with minimum distance does not guarantee its final distance is optimal—subsequent paths through negative edges might reduce the total distance. For graphs with negative weights, the Bellman-Ford algorithm is appropriate.

## Examples

### Example 1: Basic Graph with 5 Vertices

Consider a graph with vertices A, B, C, D, E and the following edges with weights:
- A to B: 4, A to C: 2
- B to C: 1, B to D: 5
- C to B: 3, C to D: 4, C to E: 5
- D to E: 2

Find shortest paths from source A.

**Step 1: Initialization**
- dist[A] = 0, dist[B] = ∞, dist[C] = ∞, dist[D] = ∞, dist[E] = ∞
- S = {} (empty), Priority Queue: {(0, A)}

**Step 2: First Iteration**
- Select A (minimum distance 0)
- Add A to S: S = {A}
- Relax edges from A:
  - A to B: dist[A] + 4 = 0 + 4 = 4 < ∞, so dist[B] = 4
  - A to C: dist[A] + 2 = 0 + 2 = 2 < ∞, so dist[C] = 2
- Priority Queue: {(2, C), (4, B)}

**Step 3: Second Iteration**
- Select C (minimum distance 2)
- Add C to S: S = {A, C}
- Relax edges from C:
  - C to B: dist[C] + 3 = 2 + 3 = 5 > 4, no update
  - C to D: dist[C] + 4 = 2 + 4 = 6 < ∞, so dist[D] = 6
  - C to E: dist[C] + 5 = 2 + 5 = 7 < ∞, so dist[E] = 7
- Priority Queue: {(4, B), (6, D), (7, E)}

**Step 4: Third Iteration**
- Select B (minimum distance 4)
- Add B to S: S = {A, C, B}
- Relax edges from B:
  - B to D: dist[B] + 5 = 4 + 5 = 9 > 6, no update
- Priority Queue: {(6, D), (7, E)}

**Step 5: Fourth Iteration**
- Select D (minimum distance 6)
- Add D to S: S = {A, C, B, D}
- Relax edges from D:
  - D to E: dist[D] + 2 = 6 + 2 = 8 > 7, no update
- Priority Queue: {(7, E)}

**Step 6: Fifth Iteration**
- Select E (minimum distance 7)
- Add E to S: S = {A, C, B, D, E}
- No outgoing edges from E

**Final Shortest Distances from A:**
- A to A: 0
- A to B: 4 (path: A → B)
- A to C: 2 (path: A → C)
- A to D: 6 (path: A → C → D)
- A to E: 7 (path: A → C → E)

### Example 2: Unreachable Vertices

Consider a graph where some vertices are not reachable from the source. Suppose vertex X is disconnected from the source S. The algorithm will initialize dist[X] = ∞ and it will never be updated because there is no path to X. This correctly represents that X is unreachable from S. In the final output, dist[X] = ∞ indicates no path exists. Students should recognize that this is the expected behavior and not an error in the algorithm.

## Exam Tips

1. REMEMBER THAT DIJKSTRA'S ONLY WORKS WITH NON-NEGATIVE WEIGHTS. If a graph has negative edge weights, you must use Bellman-Ford algorithm instead—this is a common trick question in exams.

2. THE ALGORITHM IS GREEDY BECAUSE IT ALWAYS SELECTS THE VERTEX WITH MINIMUM DISTANCE. This greedy choice is locally optimal but leads to globally optimal solution for shortest paths.

3. FOR TIME COMPLEXITY QUESTIONS, ALWAYS SPECIFY THE DATA STRUCTURE USED. The O(V²) complexity assumes an array or simple list implementation without a priority queue.

4. UNDERSTAND THE RELAXATION FORMULA THOROUGHLY. The condition "if dist[u] + weight < dist[v] then update" is frequently tested in both theory and practical exams.

5. KNOW THE DIFFERENCE BETWEEN DIJKSTRA AND BFS. BFS finds shortest path in unweighted graphs (or graphs with equal weights), while Dijkstra handles weighted graphs with non-negative weights.

6. BE ABLE TO TRACE THE ALGORITHM STEP BY STEP. Many exam questions ask you to show intermediate steps, the state of the priority queue, or the order in which vertices are selected.

7. REMEMBER THAT THE ALGORITHM MAY NOT TERMINATE EARLY IF A VERTEX IS UNREACHABLE. The distance remains infinity for such vertices, which is correct behavior.

8. UNDERSTAND WHY NEGATIVE WEIGHTS FAIL. The greedy choice assumes that once a vertex is selected (minimum distance), its distance is finalized. With negative weights, a later path might reduce the total distance, violating this assumption.