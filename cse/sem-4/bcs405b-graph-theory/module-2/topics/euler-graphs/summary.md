# Euler Graphs - Summary

## Key Definitions and Concepts

- **Eulerian Circuit**: A closed trail that traverses every edge of a graph exactly once; starts and ends at the same vertex.
- **Eulerian Path**: An open trail that traverses every edge exactly once; starts and ends at different vertices.
- **Euler Graph**: A connected graph containing an Eulerian circuit (all vertices have even degree).
- **Semi-Eulerian Graph**: A connected graph containing an Eulerian path but not circuit (exactly two vertices have odd degree).

## Important Formulas and Theorems

- **Euler's Circuit Theorem**: A connected graph is Eulerian if and only if every vertex has even degree.
- **Euler's Path Theorem**: A connected graph has an Eulerian path (but not circuit) if and only if it has exactly two vertices of odd degree.
- **Handshaking Lemma**: Sum of all vertex degrees = 2 × number of edges.

## Key Points

- A graph must be connected (ignoring isolated vertices) to be Eulerian or semi-Eulerian.
- If 0 vertices have odd degree → Eulerian circuit exists.
- If exactly 2 vertices have odd degree → Eulerian path exists (but no circuit).
- If more than 2 vertices have odd degree → Neither Eulerian path nor circuit exists.
- Fleury's Algorithm: At each step, avoid bridges unless no alternative exists.
- Hierholzer's Algorithm: Build circuits and splice them together; more efficient than Fleury's.
- Eulerian problems can be solved in polynomial time (O(E)), unlike Hamiltonian problems which are NP-complete.

## Common Mistakes to Ignore

- Forgetting to check connectivity before applying Euler's theorems.
- Choosing bridge edges prematurely in Fleury's algorithm.
- Not identifying the correct starting vertex for semi-Eulerian graphs (must start at odd-degree vertex).
- Confusing Eulerian (edges) with Hamiltonian (vertices) concepts.

## Revision Tips

- Always count vertex degrees first when analyzing any graph for Eulerian properties.
- Practice with simple graphs first before attempting complex ones.
- Remember: Even degree = circuit possible; Two odd degrees = path possible.
- For Fleury's algorithm, remember the phrase "never cross a bridge unless forced."
