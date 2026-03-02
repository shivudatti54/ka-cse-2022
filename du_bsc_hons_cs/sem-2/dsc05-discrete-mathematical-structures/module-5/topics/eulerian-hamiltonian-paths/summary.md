# Eulerian and Hamiltonian Paths - Summary

## Key Definitions and Concepts

- **Eulerian Path**: A path that traverses each edge of a graph exactly once
- **Eulerian Circuit**: An Eulerian path that starts and ends at the same vertex
- **Eulerian Graph**: A graph containing an Eulerian circuit
- **Semi-Eulerian Graph**: A graph with an Eulerian path but no circuit
- **Hamiltonian Path**: A path that visits each vertex exactly once
- **Hamiltonian Cycle**: A Hamiltonian path that returns to its starting vertex
- **Hamiltonian Graph**: A graph containing a Hamiltonian cycle

## Important Formulas and Theorems

- **Euler's Theorem**: A connected graph has an Eulerian circuit iff all vertices have even degree. It has an Eulerian path (not circuit) iff exactly two vertices have odd degree.

- **Dirac's Theorem**: If δ(G) ≥ n/2 for a graph with n ≥ 3 vertices, then G is Hamiltonian.

- **Ore's Theorem**: If deg(u) + deg(v) ≥ n for every pair of non-adjacent vertices u and v (n ≥ 3), then G is Hamiltonian.

## Key Points

- Eulerian problems involve traversing edges exactly once; Hamiltonian problems involve visiting vertices exactly once.

- Finding Eulerian paths has polynomial-time algorithms (O(V + E)); determining Hamiltonian paths is NP-complete.

- Fleury's algorithm: Avoid bridges unless no alternative exists.

- All vertices must have even degree for an Eulerian circuit; exactly two odd-degree vertices allow an Eulerian path (not circuit).

- Dirac's and Ore's theorems provide sufficient conditions for Hamiltonicity but are not necessary.

- The minimum degree conditions in Dirac's theorem (δ ≥ n/2) and Ore's theorem (sum of degrees ≥ n) are sufficient but not necessary.

- Real-world applications: Route planning (Eulerian for streets, Hamiltonian for visiting cities).

## Common Mistakes to Check

- Forgetting to verify graph connectivity before applying Euler's theorem
- Confusing Eulerian (edges) with Hamiltonian (vertices) problems
- Applying Dirac's/Ore's theorems as necessary conditions (they are only sufficient)
- Incorrectly identifying bridges in Fleury's algorithm

## Revision Tips

1. Always check connectivity first: disconnected graphs cannot have Eulerian paths.

2. Count degrees carefully: use the handshaking lemma (sum of degrees = 2|E|) to verify.

3. For Eulerian paths, remember "even circuit, odd path"—all even for circuit, exactly two odd for path.

4. Practice both Fleury's and Hierholzer's algorithms with small graphs until comfortable.

5. Know the P vs NP distinction: Eulerian is polynomial-time solvable; Hamiltonian is NP-complete—this is frequently tested.