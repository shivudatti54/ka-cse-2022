# Chromatic Polynomial - Summary

## Key Definitions and Concepts

- **Chromatic Polynomial P(G, k):** A polynomial function that counts the number of proper k-colorings of a graph G. It is a polynomial in k of degree n (number of vertices).

- **Proper Coloring:** Assignment of colors to vertices where no adjacent vertices share the same color.

- **Chromatic Number χ(G):** The minimum number of colors needed to properly color G, equal to the smallest positive integer root of P(G, k).

## Important Formulas and Theorems

- **Deletion-Contraction Recurrence:** P(G, k) = P(G-e, k) - P(G/e, k)

- **Complete Graph K_n:** P(K_n, k) = k(k-1)(k-2)...(k-n+1)

- **Path Graph P_n:** P(P_n, k) = k(k-1)^(n-1)

- **Cycle Graph C_n:** P(C_n, k) = (k-1)^n + (-1)^n(k-1)

- **Tree with n vertices:** P(T_n, k) = k(k-1)^(n-1)

- **Whitney's Theorem:** For connected graphs, coefficient of k^(n-1) equals -(n-1).

## Key Points

1. Chromatic polynomial has integer coefficients and degree equal to the number of vertices.

2. The leading coefficient is always 1, and constant term is 0 for graphs with edges.

3. P(G, 2) > 0 if and only if G is bipartite (2-colorable).

4. For odd cycles, P(C_n, 2) = 0; for even cycles, P(C_n, 2) = 2.

5. All trees with n vertices have identical chromatic polynomials: k(k-1)^(n-1).

6. Deletion-contraction is the fundamental algorithm for computing chromatic polynomials.

7. Chromatic polynomials satisfy the inequality: P(G, k) ≥ k! for k ≥ χ(G).

## Common Mistakes to Avoid

1. Forgetting that P(G, 0) = 0 and P(G, 1) = 0 for any graph with at least one edge.

2. Applying the wrong sign in the deletion-contraction formula (remember: subtract, not add).

3. Confusing chromatic polynomial with characteristic polynomial - these are different graph invariants.

4. Forgetting to account for edge contractions when the graph has multiple edges or loops after contraction.

## Revision Tips

1. Memorize the formulas for K_n, P_n, C_n, and trees as they appear frequently in exams.

2. Practice the deletion-contraction method on various graphs until comfortable.

3. Remember: if P(G, k) = 0 for some k, then χ(G) > k; if P(G, k) > 0, then χ(G) ≤ k.

4. Use the coefficient property (leading coefficient = 1, coefficient of k^(n-1) = -(n-1) for connected graphs) to verify your answers quickly.
