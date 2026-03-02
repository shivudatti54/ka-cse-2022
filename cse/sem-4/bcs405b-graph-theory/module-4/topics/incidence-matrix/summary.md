# Incidence Matrix - Summary

## Key Definitions and Concepts

- **Incidence Matrix**: An n × m matrix representing the relationship between n vertices and m edges in a graph G = (V, E).

- **Undirected Graph Incidence Matrix**: Entry M_ij = 1 if vertex i is incident to edge j; otherwise 0.

- **Directed Graph Incidence Matrix**: Entry M_ij = +1 if edge j leaves vertex i (outgoing), -1 if edge j enters vertex i (incoming), 0 otherwise.

## Important Formulas and Theorems

- **Column Sum (Undirected)**: Each column has exactly two 1's for simple graphs
- **Column Sum (Directed)**: Each column has one +1 and one -1 (sum = 0)
- **Row Sum (Undirected)**: Equals the degree of the vertex
- **Row Sum (Directed)**: Equals (outdegree - indegree)
- **Rank Property**: For connected graph with n vertices, rank(M) = n-1; for k components, rank = n-k

## Key Points

- Incidence matrix is n × m (vertices × edges), while adjacency matrix is n × n
- Each edge in undirected graph corresponds to a column with exactly two 1's
- Each directed edge has +1 at tail vertex and -1 at head vertex
- Loops are represented with single 1 (±2 in directed) at the corresponding vertex
- Row sums directly give vertex degrees in undirected graphs
- The rank of incidence matrix indicates graph connectivity
- M × M^T gives degree information: diagonal = degrees, off-diagonal = common edges

## Common Mistakes to Avoid

- Confusing incidence matrix with adjacency matrix (common exam error)
- Forgetting that directed incidence matrix uses +1 and -1, not just 1's
- Not verifying column properties (should have two 1's for undirected simple graphs)
- Incorrectly identifying the tail and head when constructing directed incidence matrix

## Revision Tips

1. Practice drawing small graphs and writing their incidence matrices until the process becomes automatic.

2. Memorize the key properties: row sums = degrees, rank = n-1 for connected graphs.

3. Always verify your constructed matrix by checking that each column correctly represents its edge.

4. Solve at least 3-4 problems from previous university question papers on this topic.
