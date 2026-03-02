# Adjacency Matrix - Summary

## Key Definitions and Concepts

- **Adjacency Matrix:** An n × n matrix A where A[i][j] = 1 if edge exists between vertices i and j, else 0
- **Undirected Graph:** Matrix is symmetric (A[i][j] = A[j][i]), diagonal is always zero for simple graphs
- **Directed Graph:** Matrix need not be symmetric; row sum = out-degree, column sum = in-degree
- **Weighted Graph:** Matrix entry A[i][j] stores edge weight; non-existent edges typically marked as 0 or ∞

## Important Formulas and Theorems

- **Degree of vertex i (undirected):** deg(i) = Σⱼ A[i][j] = Σⱼ A[j][i]
- **Out-degree (directed):** outdeg(i) = Σⱼ A[i][j]
- **In-degree (directed):** indeg(i) = Σⱼ A[j][i]
- **Handshaking Lemma:** Σ deg(i) = 2|E| (for undirected graphs)
- **Path counting:** (Aᵏ)[i][j] = number of walks of length k from i to j
- **Space complexity:** O(V²) where V = number of vertices

## Key Points

- Adjacency matrix provides O(1) edge existence check
- For undirected graphs, the matrix is always symmetric
- Row/column sums directly give vertex degrees
- Matrix powers reveal path information between vertices
- Suitable for dense graphs; inefficient for sparse graphs (O(V²) space regardless of edges)
- Complete graph Kn has adjacency matrix with 0s on diagonal and 1s elsewhere
- Self-loops appear on the diagonal (A[i][i] = 1)
- In weighted graphs, convention matters: check whether 0 or ∞ represents "no edge"
- Adjacency matrix can represent multigraphs by storing edge counts instead of 1/0

## Common Mistakes to Avoid

1. **Forgetting symmetry in undirected graphs** - Always verify A[i][j] = A[j][i]
2. **Confusing row and column sums** - Row = out-degree, Column = in-degree for directed graphs
3. **Ignoring diagonal entries** - They represent self-loops, often mistakenly assumed to be 0
4. **Wrong convention for weighted graphs** - Some texts use 0, others use ∞ for non-edges
5. **Space complexity confusion** - Remember it's always O(V²), not O(E)

## Revision Tips

1. Practice drawing graphs from adjacency matrices and vice versa - this is the most common exam question
2. Memorize the degree formulas: row sum for undirected, row/column sums for directed
3. Remember that A² entry (i,j) counts paths of length 2 - practice computing small matrix multiplications
4. Know when to use adjacency matrix vs adjacency list: matrix for dense graphs, frequent edge checks; list for sparse graphs, memory efficiency
5. Quick verification: For undirected graphs, sum of all row sums should equal 2 × number of edges
