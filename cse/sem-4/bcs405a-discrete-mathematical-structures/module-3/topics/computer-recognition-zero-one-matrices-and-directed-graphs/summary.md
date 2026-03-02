# Computer Recognition, Zero-One Matrices, and Directed Graphs - Summary

## Key Definitions and Concepts

- **Directed Graph (Digraph)**: G = (V, E) where V is vertices and E is ordered pairs (u, v) representing directed edges
- **Adjacency Matrix**: A = [aᵢⱼ] where aᵢⱼ = 1 if edge (vᵢ, vⱼ) exists, else 0
- **Reachability Matrix**: R = [rᵢⱼ] where rᵢⱼ = 1 if a path exists from vᵢ to vⱼ
- **Transitive Closure**: A\* = A + A² + A³ + ... + Aⁿ using Boolean operations
- **Strongly Connected Digraph**: Every vertex reachable from every other vertex

## Important Formulas and Theorems

- **Adjacency Definition**: aᵢⱼ = 1 iff (vᵢ, vⱼ) ∈ E
- **Path Count**: (Aᵏ)ᵢⱼ = number of paths of length k from vᵢ to vⱼ
- **Warshall's Algorithm**: Wᵢⱼ^(k) = Wᵢⱼ^(k-1) OR (Wᵢₖ^(k-1) AND Wₖⱼ^(k-1))
- **Strong Connectivity**: A digraph is strongly connected iff transitive closure has all 1s
- **Boolean Matrix Multiplication**: (AB)[i][j] = OR over k of (A[i][k] AND B[k][j])

## Key Points

- Zero-one matrices provide efficient computer representation of finite digraphs
- Adjacency matrix enables O(1) edge lookup but requires O(n²) space
- Warshall's algorithm computes transitive closure in O(n³) time
- Boolean operations (OR, AND) replace arithmetic operations in path computations
- A digraph is strongly connected when its reachability matrix contains no zeros
- The transitive closure relates to all possible path lengths, not just direct edges
- Computer recognition uses matrix properties to identify graph structure efficiently

## Common Mistakes to Avoid

1. Using regular arithmetic instead of Boolean operations (OR for addition, AND for multiplication) when computing transitive closure
2. Confusing adjacency matrix (direct edges only) with reachability matrix (all paths)
3. Forgetting that directed edges are ordered pairs—the direction matters
4. Not initializing the matrix correctly before applying Warshall's algorithm
5. Missing the self-loop consideration when checking path from vertex to itself

## Revision Tips

1. Practice constructing adjacency matrices from edge lists at least 5 times
2. Trace through Warshall's algorithm completely on a 3×3 matrix to understand each iteration
3. Remember: Boolean AND corresponds to "both conditions must be true" for path continuation
4. Boolean OR corresponds to "either condition is true" for path existence
5. For exam questions, always verify your final transitive closure matrix has 1s on diagonal if the graph has cycles
