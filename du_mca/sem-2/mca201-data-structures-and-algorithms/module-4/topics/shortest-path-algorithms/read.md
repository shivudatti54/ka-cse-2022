# Shortest Path Algorithms

## Introduction
Shortest path algorithms are fundamental tools in graph theory with wide-ranging applications in computer networks, transportation systems, and artificial intelligence. These algorithms find the minimum-cost path between nodes in a graph, where cost could represent distance, time, or other metrics. At DU's MCA level, understanding these algorithms requires analyzing their mathematical foundations, time complexities, and practical implementations.

The importance of shortest path algorithms extends to real-world systems:
1. GPS navigation (Dijkstra's algorithm)
2. Internet packet routing (Bellman-Ford algorithm)
3. Flight connection optimization (Floyd-Warshall algorithm)
4. Game AI pathfinding (A* algorithm)

With the rise of complex networks in Big Data applications, efficient shortest path computation has become critical for recommendation systems, logistics optimization, and social network analysis.

## Key Concepts
1. **Dijkstra's Algorithm**
   - Greedy approach for weighted graphs with non-negative edges
   - Uses priority queue for optimal node selection
   - Time complexity: O((V+E) log V) with Fibonacci heap

2. **Bellman-Ford Algorithm**
   - Handles negative weight edges
   - Detects negative weight cycles
   - Time complexity: O(VE)

3. **Floyd-Warshall Algorithm**
   - Dynamic programming approach for all-pairs shortest paths
   - Works with positive and negative weights (no negative cycles)
   - Time complexity: O(V³)

4. **A* Search Algorithm**
   - Best-first search using heuristics
   - Optimal with admissible heuristic functions
   - Widely used in robotics and game development

5. **Relaxation Technique**
   - Fundamental operation in most shortest path algorithms
   - Continuously updates the shortest distance estimate

## Examples

**Example 1: Dijkstra's Algorithm**
Find shortest paths from node A:
```
Graph:
A-B: 4
A-C: 2
B-C: 1
B-D: 5
C-D: 8
C-E: 10
D-E: 2
```

Solution:
1. Initialize distances: A=0, others=∞
2. Process C (smallest unvisited): Update B(3), D(10), E(12)
3. Process B: Update D(8)
4. Process D: Update E(10)
5. Final distances: A=0, B=3, C=2, D=8, E=10

**Example 2: Bellman-Ford with Negative Edge**
Check for shortest path from A in:
```
A-B: 4
B-C: -2
C-A: -1
```

Solution:
1. Initialize: A=0, others=∞
2. After 1st iteration: B=4, C=2
3. After 2nd iteration: A=1 (via C)
4. After 3rd iteration: B=5 (via A)
5. Detects no negative cycle since no further updates

**Example 3: Floyd-Warshall Matrix Update**
Compute all-pairs shortest paths for:
```
Adjacency matrix:
0 3 ∞
∞ 0 1
2 ∞ 0
```

Solution:
1. Initialize D⁰ matrix
2. k=1: No changes
3. k=2: D[3][1] becomes min(∞, 2+1) = 3
4. k=3: D[1][2] becomes min(3, ∞+0) = 3
5. Final matrix contains all shortest paths

## Exam Tips
1. Always check for negative weights before choosing Dijkstra's
2. Bellman-Ford can detect negative cycles through nth iteration
3. Floyd-Warshall's space complexity is O(V²) - important for coding
4. A* heuristic must be admissible (never overestimates)
5. Practice drawing relaxation steps for 3-4 node graphs
6. Remember time complexity tradeoffs:
   - Dijkstra: Fast for single-source
   - Floyd-Warshall: Efficient for dense graphs
7. Negative edges ≠ Negative cycles - clarify in answers

Length: 2500 words, MCA (Master of Computer Applications) PG level