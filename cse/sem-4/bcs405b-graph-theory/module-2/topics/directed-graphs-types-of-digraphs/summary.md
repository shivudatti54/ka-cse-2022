# Directed Graphs - Types of Digraphs - Summary

## Key Definitions and Concepts

- **Directed Graph (Digraph)**: A graph G = (V, E) where each edge is an ordered pair (u, v) indicating direction from tail u to head v.
- **Simple Digraph**: A digraph with no loops and at most one directed edge between any two vertices.
- **Complete Digraph**: A digraph where every pair of distinct vertices has edges in both directions; has n(n-1) edges.
- **Strongly Connected Digraph**: For any two vertices u and v, directed paths exist from u to v and v to u.
- **Weakly Connected Digraph**: The underlying undirected graph is connected.
- **DAG (Directed Acyclic Graph)**: A digraph with no directed cycles; has at least one source (indegree 0) and one sink (outdegree 0).
- **Tournament**: A complete oriented graph where exactly one edge exists between each pair of vertices.
- **k-Regular Digraph**: Each vertex has exactly k incoming and k outgoing edges.

## Important Formulas and Theorems

- Number of edges in complete digraph with n vertices: **n(n-1)**
- Maximum edges in a DAG with n vertices: **n(n-1)/2**
- In any digraph: **Σ od(v) = Σ id(v) = |E|**
- **Handshaking Lemma for Digraphs**: Sum of outdegrees equals sum of indegrees.
- **Theorem**: Every tournament has a Hamiltonian path.
- **Theorem**: A digraph is a DAG if and only if topological sorting is possible.

## Key Points

- Directed graphs model asymmetric relationships where direction matters.
- Strong connectivity is stronger than weak connectivity (strongly connected ⇒ weakly connected, but not vice versa).
- DAGs are essential for task scheduling, build systems, and dependency resolution.
- Tournaments represent complete competitions where every pair has exactly one match.
- The reverse of a digraph swaps the direction of all edges.
- Transitive digraphs satisfy: if (u,v) and (v,w) exist, then (u,w) must exist.
- Topological sort produces a linear ordering where all edges point from earlier to later vertices.
- Complete digraph has edges in both directions between every pair; tournament has exactly one.

## Common Mistakes to Avoid

1. Confusing strongly connected with weakly connected—always check if directed paths exist in both directions.
2. Forgetting that DAGs cannot have any directed cycles—even self-loops disqualify a graph from being a DAG.
3. Incorrectly counting edges in complete digraphs (n(n-1) vs n(n-1)/2).
4. Assuming topological sort exists for all digraphs—it only works for DAGs.
5. Overlooking that a single vertex with no edges is both a source and sink simultaneously.

## Revision Tips

1. Practice drawing different types of digraphs with 3-4 vertices to visualize properties.
2. Memorize the key differences between types of connectivity and digraph classifications.
3. Remember: source vertices have indegree 0; sink vertices have outdegree 0.
4. Review the proof of Hamiltonian path in tournaments—it frequently appears in exams.
5. Solve previous university questions on digraph types to understand the examination pattern.
