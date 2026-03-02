# Directed Acyclic Graphs (DAGs) and Topological Ordering

## Introduction

A **Directed Acyclic Graph (DAG)** is a fundamental data structure in computer science that models relationships where dependencies flow in a specific direction without creating cycles. In simpler terms, a DAG is a directed graph that contains no directed cycles—meaning you cannot start at a vertex and follow the directed edges to return to the same vertex.

The concept of topological ordering is crucial in computer science because it provides a linear ordering of vertices in a DAG such that for every directed edge (u, v), vertex u comes before vertex v in the ordering. This property makes DAGs invaluable for solving real-world problems like course prerequisite planning, build systems (like makefiles), task scheduling, and resolving symbol dependencies in linkers.

Understanding DAGs and topological sorting is essential for the University of Delhi's Computer Science curriculum, as these concepts frequently appear in algorithmic interviews, competitive programming, and practical software development. This topic forms the foundation for more advanced graph algorithms and is a common component in DU semester examinations.

## Key Concepts

### 1. Directed Acyclic Graph (DAG) Definition

A **Directed Acyclic Graph (DAG)** is a directed graph G = (V, E) where V is a set of vertices and E is a set of directed edges, such that there exists no directed cycle in the graph. In other words, there is no path that starts and ends at the same vertex following the direction of edges.

**Properties of DAGs:**
- Every DAG has at least one vertex with in-degree 0 (no incoming edges)
- Every DAG has at least one vertex with out-degree 0 (no outgoing edges)
- A DAG can be used to represent partial orders mathematically
- DAGs are also known as "posets" (partially ordered sets) in discrete mathematics

### 2. Topological Sort Definition

A **topological ordering** or **topological sort** of a DAG is a linear ordering of all its vertices such that for every directed edge (u, v), u appears before v in the ordering. This ordering respects all the dependencies in the graph.

**Important Properties:**
- Topological ordering exists only for DAGs (if a graph has a cycle, topological sort is impossible)
- A DAG may have multiple valid topological orderings
- The number of possible topological orderings can be exponential in some cases

### 3. Kahn's Algorithm (BFS-Based Topological Sort)

Kahn's algorithm is the most commonly taught method for topological sorting and works using the concept of in-degree.

**Algorithm Steps:**
1. Calculate in-degree for all vertices (number of incoming edges)
2. Initialize a queue with all vertices having in-degree 0
3. While the queue is not empty:
   - Dequeue a vertex u
   - Add u to the topological order
   - For each neighbor v of u:
     - Decrease v's in-degree by 1
     - If v's in-degree becomes 0, add v to the queue
4. If the topological order contains all vertices, we have a valid ordering; otherwise, the graph contains a cycle

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

### 4. DFS-Based Topological Sort

This approach uses Depth-First Search with a modification—vertices are added to the result list after all their descendants have been processed.

**Algorithm Steps:**
1. Perform DFS on the graph
2. When finishing a vertex (after exploring all its neighbors), add it to the front of a result list
3. The final result list (reversed) gives the topological ordering

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

### 5. Detecting Cycles Using Topological Sort

A key application of topological sorting is cycle detection:
- If Kahn's algorithm processes all vertices, the graph is acyclic
- If some vertices remain unprocessed, the graph contains a cycle
- This is because vertices in cycles have non-zero in-degrees throughout the algorithm

## Examples

### Example 1: Course Prerequisites Problem

Consider a university computer science curriculum with the following courses and prerequisites:
- CS101: Introduction to Programming (no prerequisites)
- CS102: Data Structures (prerequisite: CS101)
- CS201: Algorithms (prerequisites: CS102)
- CS202: Database Systems (prerequisites: CS102)
- CS301: Machine Learning (prerequisites: CS201, CS202)

**Graph Representation:**
```
Vertices: {CS101, CS102, CS201, CS202, CS301}
Edges: {(CS101, CS102), (CS102, CS201), (CS102, CS202), (CS201, CS301), (CS202, CS301)}
```

**Applying Kahn's Algorithm:**

Step 1: Calculate in-degrees
- CS101: 0
- CS102: 1
- CS201: 1
- CS202: 1
- CS301: 2

Step 2: Queue initially contains: CS101 (in-degree 0)

Step 3: Process CS101:
- Output: CS101
- Reduce CS102 in-degree: 1 → 0
- Queue: CS102

Step 4: Process CS102:
- Output: CS101, CS102
- Reduce CS201 in-degree: 1 → 0
- Reduce CS202 in-degree: 1 → 0
- Queue: CS201, CS202

Step 5: Process CS201:
- Output: CS101, CS102, CS201
- Reduce CS301 in-degree: 2 → 1
- Queue: CS202

Step 6: Process CS202:
- Output: CS101, CS102, CS201, CS202
- Reduce CS301 in-degree: 1 → 0
- Queue: CS301

Step 7: Process CS301:
- Output: CS101, CS102, CS201, CS202, CS301

**Final Topological Order:** CS101 → CS102 → CS201 → CS202 → CS301

This ordering tells students the correct sequence to take courses.

### Example 2: Build System Dependency Resolution

Consider a software project with the following files and dependencies:
- main.c depends on: utils.h, math.h
- utils.c depends on: utils.h
- math.c depends on: math.h
- utils.h: no dependencies
- math.h: no dependencies

**Graph:**
```
Vertices: {main.c, utils.c, math.c, utils.h, math.h}
Edges: {(utils.h, utils.c), (math.h, math.c), (utils.h, main.c), (math.h, main.c)}
```

**Topological Order (one valid solution):** utils.h → math.h → utils.c → math.c → main.c

This order ensures all dependencies are compiled before the files that need them.

### Example 3: DFS-Based Topological Sort

Using the course prerequisite graph from Example 1:

**DFS Traversal:**
- Start at CS101, explore to CS102, then to CS201, then to CS301
- CS301 has no unvisited neighbors, add to result: [CS301]
- Backtrack to CS201, add to result: [CS301, CS201]
- Backtrack to CS102, explore CS202, then to CS301 (already visited)
- Add CS202 to result: [CS301, CS201, CS202]
- Backtrack to CS102, add to result: [CS301, CS201, CS202, CS102]
- Backtrack to CS101, add to result: [CS301, CS201, CS202, CS102, CS101]

**Reverse the result:** CS101 → CS102 → CS202 → CS201 → CS301

(Note: This differs from Kahn's result but is equally valid)

## Exam Tips

1. **Remember the fundamental property:** Topological sort is only possible for DAGs. Always check for cycles first in exam questions.

2. **Kahn's Algorithm is exam-favorite:** Most DU exam questions ask you to perform Kahn's algorithm step-by-step. Practice calculating in-degrees and maintaining the queue.

3. **Multiple valid answers exist:** If a question asks for "a" topological ordering, any valid ordering earns full marks. Don't panic if your answer differs from the solution key.

4. **Cycle detection trick:** In Kahn's algorithm, if the number of processed vertices equals the total vertices, the graph is acyclic. If not, a cycle exists.

5. **Time and Space Complexity:** Memorize O(V + E) for both Kahn's and DFS-based approaches. This is frequently asked in short answer questions.

6. **Relationship with DFS:** Remember that DFS-based topological sort uses "finish time"—vertices are added to the result when their DFS call completes.

7. **Application-based questions:** Be prepared to identify DAGs in real-world scenarios like task scheduling, prerequisite courses, and build systems.

8. **In-degree always starts with zero:** Only vertices with in-degree 0 can be the starting point in Kahn's algorithm.

9. **Practice graph drawing:** Many exam questions present a graph pictorially and ask for the topological order. Practice drawing and analyzing directed graphs.

10. **Verify your answer:** For any topological order, check that for every edge (u, v), u appears before v. This is your verification method.