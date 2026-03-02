# Graph Traversals & Topological Sort

## Introduction
Graph traversals and topological sorting are fundamental algorithmic techniques for processing directed acyclic graphs (DAGs). According to the Delhi University B.Sc. (Physical Science – CS) NEP 2024 syllabus, these topics belong to the *Graph Algorithms* unit and are essential for solving problems such as task scheduling, course prerequisite ordering, and build systems.

## Key Concepts
- **Graph Representation**  
  - *Adjacency list* – efficient for sparse graphs (O(V+E) space).  
  - *Adjacency matrix* – O(V²) space, constant‑time edge lookup.

- **Breadth‑First Search (BFS)**  
  - Uses a queue; explores vertices level by level.  
  - Produces shortest‑path distances in unweighted graphs.  
  - **Time:** O(V+E), **Space:** O(V).

- **Depth‑First Search (DFS)**  
  - Uses recursion or an explicit stack; explores as far as possible along each branch.  
  - Generates vertex finish times; useful for cycle detection and topological ordering.  
  - **Time:** O(V+E), **Space:** O(V) (recursion stack).

- **Topological Sort**  
  - **Definition:** Linear ordering of vertices of a DAG such that for every directed edge *(u, v)*, *u* appears before *v*.  
  - **Properties:** Only possible if the graph is a DAG; multiple valid orders may exist.  
  - **Kahn’s Algorithm (BFS‑based)**  
    1. Compute in‑degree of each vertex.  
    2. Enqueue all zero‑in‑degree vertices.  
    3. Repeatedly dequeue a vertex, add to order, reduce in‑degrees of its neighbors; enqueue any neighbor whose in‑degree becomes zero.  
    4. If all vertices are processed → topological order; otherwise, a cycle exists.  
    - **Time:** O(V+E), **Space:** O(V).  
  - **DFS‑Based Method**  
    - Perform DFS; push vertices onto a stack when their recursion finishes.  
    - Pop the stack to obtain a topological order.  
    - Automatically detects cycles (if a back edge is found during DFS).  
    - **Time:** O(V+E), **Space:** O(V).

- **Complexity & Applications**  
  - Both methods run in linear time O(V+E), matching the traversal cost.  
  - Used in build systems (make), course timetabling, task scheduling, and resolving symbol dependencies in linkers.

## Conclusion
Mastering BFS/DFS traversals provides the backbone for exploring any graph structure, while topological sort leverages these traversals to order tasks in a DAG. Understanding their algorithms, complexities, and cycle‑detection capabilities equips students to tackle real‑world scheduling and ordering problems, as required by the Delhi University NEP 2024 examination.