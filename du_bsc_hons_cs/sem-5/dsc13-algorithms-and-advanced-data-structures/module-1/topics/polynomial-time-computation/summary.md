# Polynomial Time Computation - Summary

## Key Definitions and Concepts

- **Polynomial Time**: An algorithm runs in polynomial time if its time complexity is O(n^k) for some constant k, where n is the input size. Examples include O(1), O(log n), O(n), O(n²), O(n³).

- **Tractable Problems**: Problems solvable in polynomial time; considered "efficiently solvable" in practice.

- **Intractable Problems**: Problems requiring super-polynomial time (exponential or factorial); impractical for large inputs.

- **Class P**: The set of all decision problems solvable by a deterministic Turing machine in polynomial time.

- **Polynomial Time Reduction**: Transforming an instance of problem A to problem B in polynomial time such that solving B solves A.

## Important Formulas and Theorems

- **Big O Notation**: f(n) = O(g(n)) if there exist constants c and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀

- **Complexity Classes**: P ⊆ NP, though whether P = NP remains an open question

- **Church-Turing Thesis**: Any reasonable computation model can be simulated by a Turing machine

- **Cook's Thesis**: Any realistic computation model can simulate a DTM with polynomial slowdown

## Key Points

- Polynomial time (O(n^k)) represents the practical boundary between solvable and unsolvable problems
- The difference between O(n²) and O(2^n) is dramatic: for n=20, n² = 400 while 2^n = 1,048,576
- Class P includes sorting, shortest path, minimum spanning tree, and many graph problems
- Exponential algorithms become impractical even for small n (typically n > 30)
- Polynomial time reduction preserves tractability: if A reduces to B and B is in P, then A is in P
- The P vs NP problem asks whether verification speed equals solution speed
- Practical efficiency depends on input sizes; theoretical polynomial bounds guide algorithm selection

## Common Mistakes to Avoid

- Confusing O(n²) with O(2^n)—the former is polynomial, the latter exponential
- Assuming polynomial time always means "fast in practice"—large exponents still cause problems
- Forgetting that constants matter in practice: O(n) with large constant may be slower than O(n²) for small inputs
- Misunderstanding reduction direction: if A reduces to B, solving B helps solve A, not vice versa

## Revision Tips

1. Memorize common time complexities and classify them as polynomial or exponential
2. Practice identifying whether given algorithms are polynomial-time by analyzing their loops and recursion
3. Remember key examples: sorting (n log n), matrix multiplication (n^2.373), Fibonacci (linear with memoization, exponential without)
4. Review the practical implications table showing growth rates for different complexities
5. Understand why the polynomial bound exists and what would happen without it