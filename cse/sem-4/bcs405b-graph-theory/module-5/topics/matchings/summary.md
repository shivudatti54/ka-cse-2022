# Matchings in Graph Theory - Summary

## Key Definitions and Concepts

- **Matching**: A set of edges where no two edges share a common vertex
- **Maximum Matching**: A matching of largest possible size in the graph
- **Perfect Matching**: A matching that covers every vertex in the graph (every vertex is incident to exactly one edge)
- **Augmenting Path**: A path that alternates between unmatched and matched edges, starting and ending at unmatched vertices
- **Bipartite Graph**: Graph G = (X, Y, E) where vertices are partitioned into two sets X and Y with edges only between X and Y

## Important Formulas and Theorems

- **Hall's Marriage Theorem**: A bipartite graph G = (X, Y, E) has an X-perfect matching if and only if for every subset S ⊆ X, |N(S)| ≥ |S|

- **König's Theorem**: In any bipartite graph, the size of a minimum vertex cover equals the size of a maximum matching: α'(G) = τ(G)

- **Berge's Theorem**: A matching M is maximum if and only if there is no augmenting path with respect to M

- **Tutte's Theorem**: A graph G has a perfect matching if and only if for every subset S ⊆ V(G), o(G - S) ≤ |S| (number of odd components does not exceed |S|)

## Key Points

1. A perfect matching exists only in graphs with an even number of vertices
2. Every perfect matching is a maximum matching, but the converse is not always true
3. Hall's Theorem provides necessary and sufficient conditions for X-perfect matching in bipartite graphs
4. Augmenting path algorithms can find maximum matchings by repeatedly improving the matching
5. König's Theorem connects matching theory with vertex cover problems in bipartite graphs
6. Tutte's Theorem generalizes Hall's Theorem to general (non-bipartite) graphs
7. If Hall's condition fails for some S, there is no X-perfect matching; constructive proof shows which vertices cause the failure
8. Maximum matching in bipartite graphs can be found in O(VE) time using augmenting path approaches

## Common Mistakes to Avoid

1. Confusing maximum matching with perfect matching—they are different concepts
2. Forgetting that Hall's Theorem requires checking ALL subsets S ⊆ X, not just singletons
3. Assuming Hall's Theorem applies to non-bipartite graphs—it only works for bipartite graphs
4. Incorrectly identifying augmenting paths—they must alternate between matched and unmatched edges
5. Forgetting that König's Theorem applies only to bipartite graphs, not general graphs

## Revision Tips

1. Practice checking Hall's condition on small bipartite graphs by enumerating all subsets
2. Draw augmenting paths clearly, marking matched vs. unmatched edges to avoid confusion
3. Remember: Hall's condition is necessary AND sufficient—this is powerful for problem solving
4. König's Theorem provides a quick way to find minimum vertex cover size once maximum matching size is known
5. When asked to find maximum matching, always look for augmenting paths starting from unmatched vertices
