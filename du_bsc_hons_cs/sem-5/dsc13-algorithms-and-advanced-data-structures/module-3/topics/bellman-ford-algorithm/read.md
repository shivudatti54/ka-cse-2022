# Bellman-Ford Algorithm

## Introduction

The Bellman-Ford algorithm is a fundamental graph algorithm used to find the shortest paths from a single source vertex to all other vertices in a weighted graph. Unlike Dijkstra's algorithm, which works only with non-negative edge weights, Bellman-Ford algorithm can handle graphs with negative weight edges, making it more versatile for real-world scenarios. This algorithm was independently discovered by several researchers, with Richard Bellman and Lester Ford Jr. being the most prominent names associated with it.

In the context of the University of Delhi's Computer Science curriculum, the Bellman-Ford algorithm represents a crucial extension of shortest path algorithms. It introduces students to handling negative edge weights and detecting negative weight cycles, which are essential concepts for advanced graph problem-solving. The algorithm's ability to work with negative weights makes it applicable in various scenarios such as currency arbitrage detection, network routing protocols, and optimizing certain types of computational problems where edge weights can represent costs or losses.

Understanding the Bellman-Ford algorithm requires a solid foundation in graph theory and algorithmic thinking. This algorithm serves as a bridge between basic shortest path algorithms and more complex dynamic programming approaches, demonstrating how iterative refinement can solve optimization problems efficiently.

## Key Concepts

### Single-Source Shortest Path Problem

The single-source shortest path problem asks for the shortest paths from a designated source vertex to all other vertices in the graph. For a graph G = (V, E) with weight function w: E → R, we aim to find the shortest path distance from source vertex s to every vertex v ∈ V.

### Negative Weight Edges

In real-world applications, edge weights can sometimes be negative. For instance, in a financial network, an edge weight might represent a transaction cost (positive) or a discount (negative). The Bellman-Ford algorithm correctly handles such scenarios, whereas Dijkstra's algorithm would fail because it assumes non-negative weights.

### Negative Weight Cycles

A negative weight cycle is a cycle whose total edge weight is negative. When such a cycle exists and is reachable from the source, the shortest path is undefined because one could traverse the cycle arbitrarily many times to get arbitrarily small path costs. The Bellman-Ford algorithm can detect the presence of negative weight cycles.

### Relaxation Operation

The core operation in Bellman-Ford algorithm is relaxation. For each edge (u, v) with weight w, if the current known distance to v can be improved by going through u, we update the distance. Formally:

```
if dist[u] + w(u, v) < dist[v]:
    dist[v] = dist[u] + w(u, v)
```

This operation is performed repeatedly to progressively improve the distance estimates.

### Algorithm Description

The Bellman-Ford algorithm works as follows:

1. **Initialization**: Set dist[s] = 0 for the source vertex s, and dist[v] = ∞ for all other vertices.

2. **Iteration**: Repeat |V| - 1 times:
   - For each edge (u, v) in the graph, perform relaxation

3. **Negative Cycle Detection**: After the |V| - 1 iterations, check if any edge can still be relaxed. If yes, a negative weight cycle exists.

### Time and Space Complexity

- **Time Complexity**: O(|V| × |E|), where V is the number of vertices and E is the number of edges
- **Space Complexity**: O(|V|), for storing distance values and predecessor information

### Comparison with Dijkstra's Algorithm

| Aspect | Bellman-Ford | Dijkstra's |
|--------|--------------|------------|
| Time Complexity | O(VE) | O((V + E) log V) |
| Negative Weights | Supported | Not supported |
| Negative Cycle Detection | Yes | No |
| Approach | Dynamic Programming | Greedy |

## Examples

### Example 1: Basic Bellman-Ford Execution

Consider the following graph with vertices {A, B, C, D, E} and edges with weights:

```
A → B: 4, A → E: 2
B → C: 3, B → E: 3
C → D: -2 (negative weight!)
D → B: 1, D → E: -1 (negative weight!)
E → C: 5
```

Source: A

**Solution:**

**Step 1: Initialization**
dist[A] = 0, dist[B] = dist[C] = dist[D] = dist[E] = ∞

**Step 2: Iteration 1** (First pass through all edges)
- Edge A→B: dist[A] + 4 = 0 + 4 < ∞ → dist[B] = 4
- Edge A→E: 0 + 2 < ∞ → dist[E] = 2
- Edge B→C: 4 + 3 = 7 < ∞ → dist[C] = 7
- Edge B→E: 4 + 3 = 7 > 2 (no update)
- Edge C→D: 7 + (-2) = 5 < ∞ → dist[D] = 5
- Edge D→B: 5 + 1 = 6 > 4 (no update)
- Edge D→E: 5 + (-1) = 4 > 2 (no update)
- Edge E→C: 2 + 5 = 7 = 7 (no update)

**Step 3: Iteration 2**
- Edge A→B: 0 + 4 = 4 (no update)
- Edge A→E: 0 + 2 = 2 (no update)
- Edge B→C: 4 + 3 = 7 (no update)
- Edge B→E: 4 + 3 = 7 (no update)
- Edge C→D: 7 + (-2) = 5 (no update)
- Edge D→B: 5 + 1 = 6 > 4 (no update)
- Edge D→E: 5 + (-1) = 4 > 2 (no update)
- Edge E→C: 2 + 5 = 7 (no update)

**Step 4: Iteration 3** (same as above, no changes)
**Step 5: Iteration 4** (same as above, no changes)

**Step 6: Negative Cycle Check**
All edges fail to relax. No negative weight cycle exists.

**Final Distances:**
dist[A] = 0, dist[B] = 4, dist[C] = 7, dist[D] = 5, dist[E] = 2

### Example 2: Negative Weight Cycle Detection

Consider graph with vertices {S, A, B} and edges:
S→A: 4, S→B: 5, A→B: -8, B→A: 2

Source: S

**Solution:**

**Initialization:** dist[S] = 0, dist[A] = dist[B] = ∞

**Iteration 1:**
- S→A: dist[A] = 4
- S→B: dist[B] = 5
- A→B: 4 + (-8) = -4 < 5 → dist[B] = -4
- B→A: -4 + 2 = -2 < 4 → dist[A] = -2

**Iteration 2:**
- S→A: 0 + 4 = 4 > -2 (no update)
- S→B: 0 + 5 = 5 > -4 (no update)
- A→B: -2 + (-8) = -10 < -4 → dist[B] = -10
- B→A: -10 + 2 = -8 < -2 → dist[A] = -8

**After |V|-1 = 2 iterations, we continue checking:**

**Negative Cycle Check:**
- A→B: -8 + (-8) = -16 < -10 → **CYCLE DETECTED!**

The algorithm correctly identifies a negative weight cycle (S→A→B→A→B... keeps decreasing).

## Exam Tips

1. **Understand when to use Bellman-Ford**: Always choose Bellman-Ford when the graph contains negative edge weights or when negative cycle detection is required.

2. **Remember the iteration count**: The algorithm performs exactly |V| - 1 iterations because the shortest path in a graph without cycles can have at most |V| - 1 edges.

3. **Master the relaxation operation**: The if condition `dist[u] + w < dist[v]` is the core of the algorithm—practice writing this correctly.

4. **Negative cycle detection is key**: After |V| - 1 iterations, one more pass to detect if any edge can still be relaxed confirms a negative cycle.

5. **Space optimization**: For exam questions, remember you only need an array of size |V| for distances plus optional predecessor array.

6. **Edge cases to remember**: Single vertex (no edges), disconnected graphs (infinite distances remain), and self-loops.

7. **Comparison questions**: Be prepared to compare Bellman-Ford with Dijkstra regarding time complexity, negative weights, and algorithmic approach.

8. **Practice tracing algorithm**: Exam questions often ask you to trace through the algorithm step by step—practice with various graph configurations.