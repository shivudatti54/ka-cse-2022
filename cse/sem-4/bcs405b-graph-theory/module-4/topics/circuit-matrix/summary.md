# Circuit Matrix - Summary

## Key Definitions and Concepts

- **Circuit (Cycle):** A closed walk in a graph that starts and ends at the same vertex, with all edges and vertices appearing exactly once (except start/end vertex).

- **Fundamental Circuit:** A unique circuit formed by combining a chord (non-tree edge) with the tree edges on the unique path between its endpoints in a spanning tree.

- **Circuit Matrix (F-matrix):** An (m-n+1) × m matrix where rows represent fundamental circuits and columns represent edges. Entry is 1 if edge is in the circuit, 0 otherwise.

- **Chord (Non-tree edge):** An edge in the graph that is not part of the selected spanning tree.

## Important Formulas and Theorems

- **Cyclomatic Number (Number of independent circuits):** c = m - n + 1
- **Number of tree edges in spanning tree:** n - 1
- **Number of chords:** m - (n - 1) = m - n + 1
- **Rank of circuit matrix:** c = m - n + 1
- **Orthogonality Property:** F × A^T = 0 (mod 2), where A is the incidence matrix

## Key Points

- The circuit matrix depends on the choice of spanning tree; different spanning trees yield different but equivalent F-matrices.

- Each fundamental circuit contains exactly one chord and one or more tree edges.

- The rows of the F-matrix form a basis for the cycle space of the graph.

- For a connected graph with n vertices and m edges, there are exactly (m-n+1) fundamental circuits.

- The circuit matrix extends the capability to analyze cyclic structures in networks beyond what the incidence matrix provides.

- The F-matrix has dimensions (m-n+1) × m, where rows represent independent circuits.

## Common Mistakes to Avoid

1. Confusing the dimensions of the circuit matrix - it is (m-n+1) rows by m columns, not the reverse.

2. Forgetting that the number of fundamental circuits equals the number of chords, not the total number of edges.

3. Incorrectly identifying which edges are chords versus tree edges when constructing the F-matrix.

4. Not understanding that the fundamental circuit for a chord includes tree edges on the path between the chord's endpoints.

## Revision Tips

1. Practice constructing F-matrices for different graphs with various spanning trees to understand the relationship.

2. Memorize the formula c = m - n + 1 and be able to apply it quickly in exam questions.

3. Review the relationship between circuit matrix, incidence matrix, and cut-set matrix to understand their complementary roles.

4. Solve previous year university questions on circuit matrix to familiarize with exam patterns and common question types.
