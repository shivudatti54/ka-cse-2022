# Fundamental Circuits - Summary

## Key Definitions and Concepts

- **Spanning Tree**: A connected subgraph containing all vertices of the original graph with exactly n-1 edges, containing no cycles.
- **Chord (Cotree Edge)**: An edge of graph G that is not part of a chosen spanning tree T.
- **Fundamental Circuit**: The unique cycle formed when adding a chord to a spanning tree; consists of the chord plus the unique path in T connecting its endpoints.
- **Cycle Space**: The vector space over GF(2) formed by all cycles of a graph, where addition is symmetric difference.
- **Cyclomatic Number (Cycle Rank)**: Given by m - n + 1, represents the number of independent cycles.

## Important Formulas and Theorems

- **Number of Fundamental Circuits**: m - n + 1 (where m = edges, n = vertices)
- **Spanning Tree Edges**: n - 1
- **Number of Chords**: m - (n - 1) = m - n + 1
- **Fundamental Circuit for edge e**: C(T,e) = e ∪ path_T(u,v), where u and v are endpoints of e

## Key Points

1. Fundamental circuits are defined with respect to a specific spanning tree; different trees yield different sets.

2. Each chord produces exactly one fundamental circuit with a given spanning tree.

3. The set of all fundamental circuits forms a basis for the cycle space of the graph.

4. For a tree (acyclic graph), there are no fundamental circuits since m = n - 1.

5. Fundamental circuits are independent cycles - no fundamental circuit can be expressed as a combination of others.

6. The dimension of cycle space equals m - n + 1, which is also the number of fundamental circuits.

7. Any arbitrary cycle in the graph can be expressed as the symmetric difference of some fundamental circuits.

## Common Mistakes to Avoid

1. Confusing tree edges with chords - tree edges are in T, chords are not in T.

2. Forgetting that the fundamental circuit includes both the chord and the path in the tree.

3. Using the wrong formula - some students confuse m - n + 1 with n - 1.

4. Assuming fundamental circuits are unique - they depend on the choice of spanning tree.

5. Not verifying that the spanning tree is indeed acyclic and connects all vertices.

## Revision Tips

1. Practice drawing different graphs and finding their spanning trees and fundamental circuits.

2. Memorize the relationship: number of fundamental circuits = m - n + 1.

3. Remember that fundamental circuits form a basis - this is crucial for understanding cycle space.

4. Solve previous year university questions on this topic to understand the exam pattern.

5. Focus on the procedure: Find spanning tree → Identify chords → Find paths in tree → Form circuits.
