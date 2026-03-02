# Eulerian and Hamiltonian Paths

## Introduction to Paths

In graph theory, a **path** is a sequence of vertices where each consecutive pair is connected by an edge, and no vertex is repeated (unless it's a closed path starting and ending at the same vertex). Understanding paths is fundamental to analyzing graph connectivity and traversal possibilities.

## Eulerian Paths and Circuits

### Historical Context

The concept of Eulerian paths originates from Leonhard Euler's solution to the famous **Königsberg Bridge Problem** in 1736. The problem asked whether it was possible to walk through the city crossing each of its seven bridges exactly once.

### Definitions

- **Eulerian Path**: A path that traverses every edge exactly once. Vertices may be repeated.
- **Eulerian Circuit**: A closed Eulerian path that starts and ends at the same vertex.

### Necessary and Sufficient Conditions

For a connected graph G:

| Graph Type | Eulerian Circuit Exists If                   | Eulerian Path Exists If                                                                                                                    |
| ---------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Undirected | Every vertex has even degree                 | Exactly zero or two vertices have odd degree                                                                                               |
| Directed   | For each vertex, in-degree equals out-degree | At most one vertex has (out-degree - in-degree) = 1, at most one has (in-degree - out-degree) = 1, and all others have equal in/out-degree |

### Examples

**Example 1: Eulerian Circuit**

```
Graph:
A -- B
|    |
C -- D

Vertices: A, B, C, D
Degrees: A=2, B=2, C=2, D=2 (all even)
Eulerian Circuit: A-B-D-C-A
```

**Example 2: Eulerian Path**

```
Graph:
A -- B -- C
|    |
D -- E

Vertices: A, B, C, D, E
Degrees: A=2, B=3, C=1, D=2, E=2
Odd degree vertices: B and C (exactly two)
Eulerian Path: C-B-A-D-E-B
```

### Finding Eulerian Paths/Circuits

Fleury's Algorithm and Hierholzer's Algorithm are commonly used to find Eulerian paths and circuits.

## Hamiltonian Paths and Cycles

### Definitions

- **Hamiltonian Path**: A path that visits each vertex exactly once.
- **Hamiltonian Cycle**: A Hamiltonian path that forms a cycle by connecting the last vertex to the first.

### Comparison with Eulerian Paths

| Aspect     | Eulerian                                         | Hamiltonian                                         |
| ---------- | ------------------------------------------------ | --------------------------------------------------- |
| Focus      | Edges                                            | Vertices                                            |
| Condition  | All edges used exactly once                      | All vertices visited exactly once                   |
| Complexity | Polynomial time (O(E))                           | NP-complete                                         |
| Existence  | Well-defined necessary and sufficient conditions | No known simple necessary and sufficient conditions |

### Necessary Conditions

- The graph must be connected
- No articulation points that would make traversal impossible
- Sufficient degree conditions (Dirac's Theorem: If each vertex has degree ≥ n/2, Hamiltonian cycle exists)
- Ore's Theorem: If deg(u) + deg(v) ≥ n for every pair of non-adjacent vertices, then Hamiltonian cycle exists

### Examples

**Example 1: Hamiltonian Path**

```
Graph:
A -- B -- C
|         |
D -- E -- F

Hamiltonian Path: A-D-E-F-C-B
```

**Example 2: Hamiltonian Cycle**

```
Complete Graph K₄:
A -- B
| \/ |
| /\ |
C -- D

Hamiltonian Cycle: A-B-D-C-A
```

## Applications

### Eulerian Applications

- Garbage collection routes
- Network packet routing
- DNA fragment assembly
- Postal route planning

### Hamiltonian Applications

- Traveling salesman problem
- Circuit board drilling
- Genome sequencing
- Social network analysis

## Algorithmic Approaches

### For Eulerian Paths/Circuits

```python
# Hierholzer's Algorithm for Eulerian Circuit
def hierholzer(graph):
    # Implementation details
    pass
```

### For Hamiltonian Paths/Cycles

```python
# Backtracking approach for Hamiltonian Path
def hamiltonian_backtracking(graph):
    # NP-hard problem - exponential time
    pass
```

## Exam Tips

1. **Remember the degree conditions** for Eulerian paths/circuits - this is frequently tested
2. **For Hamiltonian problems**, look for obvious obstructions like degree-1 vertices that must be endpoints
3. **Practice drawing examples** of both types of paths
4. **Understand the complexity difference**: Eulerian = polynomial, Hamiltonian = NP-complete
5. **Be able to convert between directed and undirected graph conditions**
6. **Memorize key theorems**: Dirac's and Ore's theorems for Hamiltonian cycles
