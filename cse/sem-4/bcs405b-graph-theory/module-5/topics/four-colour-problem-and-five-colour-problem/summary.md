# Four Colour Problem and Five Colour Problem - Summary

## Key Definitions and Concepts

- **Planar Graph**: A graph that can be drawn on a plane without any edges crossing. A connected planar graph satisfies Euler's formula: V - E + F = 2, where V is vertices, E is edges, and F is faces.

- **Graph Colouring**: Assigning colours to vertices such that no two adjacent vertices share the same colour. The minimum colours required is the chromatic number.

- **Dual Graph**: The dual of a planar graph has vertices representing faces of the original graph, with edges connecting faces that share a boundary.

- **Kempe Chain**: A maximal connected subgraph containing vertices of only two specified colours.

## Important Formulas and Theorems

- **Euler's Formula**: V - E + F = 2 (for connected planar graphs)

- **Edge Bound**: For simple planar graphs with V ≥ 3: E ≤ 3V - 6

- **Five Colour Theorem (Heawood, 1890)**: Every planar graph can be coloured with at most 5 colours.

- **Four Colour Theorem (Appel & Haken, 1976)**: Every planar graph can be coloured with at most 4 colours.

- **Vertex Degree Theorem**: Every planar graph contains at least one vertex of degree 5 or less.

## Key Points

- The Four Colour Problem was posed by Francis Guthrie in 1852 and solved by Appel and Haken in 1976 using computer verification.

- The Five Colour Theorem was proven by Percy Heawood in 1890, providing an upper bound of 5 colours for planar graphs.

- The proof that every planar graph has a vertex of degree at most 5 uses Euler's formula and leads to the inequality E ≤ 3V - 6.

- K₄ (complete graph on 4 vertices) is planar and requires exactly 4 colours, demonstrating that 4 is the tight bound.

- K₅ is non-planar and requires 5 colours, illustrating the connection between planarity and chromatic number.

- The Four Colour Theorem was the first major mathematical theorem proven with substantial computer assistance.

## Common Mistakes to Avoid

- Confusing the Four and Five Colour Theorems: Remember that Five was proven first (1890) analytically, while Four required computers (1976).

- Forgetting that Euler's formula applies only to connected planar graphs; disconnected graphs require separate consideration for each component.

- Assuming that non-planar graphs can be coloured with 4 colours; K₅ is non-planar and requires 5 colours.

## Revision Tips

- Memorize the key dates: 1852 (Guthrie's question), 1890 (Heawood's Five Colour proof), 1976 (Appel-Haken Four Colour proof).

- Practice deriving the edge bound E ≤ 3V - 6 from Euler's formula as this is frequently tested.

- Remember that K₅ and K₃,₃ are the fundamental non-planar graphs, and their subdivisions cannot appear in planar graphs.
