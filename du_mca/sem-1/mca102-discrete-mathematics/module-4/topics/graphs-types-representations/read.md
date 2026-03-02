# Graph Theory: Types and Representations

## Introduction
Graph theory forms the backbone of modern computer science with applications ranging from social network analysis to routing algorithms. A graph is a mathematical structure consisting of vertices (nodes) connected by edges (links). Understanding different graph types and their representations is crucial for solving complex problems in areas like network design, database systems, and artificial intelligence.

Graph representations determine how efficiently we can perform operations like path finding or neighbor identification. With the NEP 2024 focus on industry-aligned learning, DU MCA students must master both theoretical foundations and practical implementations used in tech companies like Google (PageRank algorithm) and Uber (route optimization).

## Key Concepts

1. **Graph Types**:
   - **Directed vs. Undirected**: Directed graphs have edges with direction (e.g., web page links), while undirected edges have bidirectional relationships (e.g., Facebook friendships).
   - **Weighted vs. Unweighted**: Edges may carry weights (e.g., road distances in GPS systems).
   - **Cyclic vs. Acyclic**: Presence or absence of cycles (critical in dependency graphs).
   - **Special Types**: Trees (acyclic connected graphs), Bipartite graphs (two disjoint vertex sets), Complete graphs (all vertices interconnected).

2. **Representation Methods**:
   - **Adjacency Matrix**: A V×V matrix where entry (i,j) = 1 if edge exists between i and j. Space: O(V²). Ideal for dense graphs.
   - **Adjacency List**: Array of linked lists storing neighbors for each vertex. Space: O(V + E). Preferred for sparse graphs.
   - **Edge List**: Simple list of all edges. Space: O(E). Used in Kruskal's algorithm for MST.
   - **Incidence Matrix**: V×E matrix for directed graphs (entries: -1, 0, 1). Useful in network flow problems.

3. **Complexity Considerations**:
   - Adjacency matrices enable O(1) edge queries but require more memory.
   - Adjacency lists allow efficient traversal of neighbors in O(degree(v)) time.

## Examples

**Example 1: Adjacency Matrix Construction**  
Construct an adjacency matrix for the following undirected graph:  
Vertices: {A, B, C, D}  
Edges: A-B, B-C, C-D, D-A  

*Solution*:  
```
   A B C D  
A 0 1 0 1  
B 1 0 1 0  
C 0 1 0 1  
D 1 0 1 0  
```

**Example 2: BFS Using Adjacency List**  
Given adjacency list:  
A: [B, D]  
B: [A, C]  
C: [B, D]  
D: [A, C]  
Perform BFS starting from A.  

*Solution*:  
Level 0: A  
Level 1: B, D  
Level 2: C (via B) and C (via D) → Final order: A → B → D → C  

**Example 3: Edge List to Adjacency List Conversion**  
Edge list: [(1,2), (2,3), (3,4), (4,1)]  
Convert to adjacency list representation.  

*Solution*:  
1: [2, 4]  
2: [1, 3]  
3: [2, 4]  
4: [3, 1]  

## Exam Tips

1. Always mention time/space complexity when comparing representations.
2. For directed vs. undirected graphs: Adjacency matrices are symmetric only for undirected graphs.
3. Weighted graphs: Use matrix entries to store weights instead of 1/0.
4. In trees, the number of edges is always V-1 (theorem).
5. Practice converting between representations (common 8-mark question).
6. Remember complete graph edge count: n(n-1)/2 for undirected, n(n-1) for directed.
7. For bipartite graphs: No odd-length cycles (König's theorem).