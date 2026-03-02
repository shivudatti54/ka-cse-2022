# Isolated Vertex, Pendant Vertex, and Null Graph - Summary

## Key Definitions and Concepts

- **Isolated Vertex**: A vertex with degree 0 (no edges connected)
- **Pendant Vertex**: A vertex with degree 1 (connected to exactly one vertex); also called leaf vertex
- **Null Graph**: A graph with no edges; denoted as Nₙ for n vertices; also called edgeless or empty graph
- **Trivial Graph**: A null graph with a single vertex (sometimes considered separately)

## Important Formulas and Theorems

- **Degree of Isolated Vertex**: deg(v) = 0
- **Degree of Pendant Vertex**: deg(v) = 1
- **Handshaking Lemma**: Σ deg(v) = 2|E| (sum of all vertex degrees equals twice the number of edges)
- **Null Graph Complement**: Complement of Kₙ (complete graph) = Nₙ (null graph)

## Key Points

- Isolated vertices have no connections to any other vertex in the graph
- Pendant vertices have exactly one edge connecting them to the rest of the graph
- A null graph contains only isolated vertices (no edges between any vertices)
- In the adjacency matrix, isolated vertices correspond to zero rows and columns
- Trees have at least two pendant vertices (leaves) if they have more than one vertex
- A single vertex with no edges is both a trivial graph and a null graph
- The degree sequence helps identify special vertices quickly

## Common Mistakes to Avoid

- Confusing isolated vertices (degree 0) with pendant vertices (degree 1)
- Treating a single vertex graph as not being a null graph
- Forgetting that null graphs can have multiple isolated vertices
- Confusing complete graph complement with null graph complement

## Revision Tips

1. Practice identifying special vertices from degree sequences
2. Draw sample graphs with various combinations of isolated and pendant vertices
3. Verify answers using the Handshaking Lemma
4. Remember that in trees, pendant vertices are the "leaves"
5. Review adjacency matrix representation to quickly identify special vertices
