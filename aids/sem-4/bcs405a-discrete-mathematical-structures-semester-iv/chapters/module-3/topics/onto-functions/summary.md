# Onto Functions - Summary

## Key Definitions and Concepts

- ONTO (SURJECTIVE) FUNCTION: A function f: A → B is onto if for every element b in the codomain B, there exists at least one element a in the domain A such that f(a) = b. Formally: ∀b ∈ B, ∃a ∈ A: f(a) = b

- RANGE VS CODOMAIN: A function is onto precisely when its range (image) equals its codomain

- BIJECTIVE FUNCTION: A function that is both one-to-one (injective) and onto (surjective), establishing a perfect pairing between domain and codomain

## Important Formulas and Theorems

- Number of onto functions from set A (|A| = m) to set B (|B| = n), where m ≥ n:
  n^m - C(n,1)(n-1)^m + C(n,2)(n-2)^m - ... + (-1)^(n-1)C(n,n-1)(1)^m
  Or equivalently: Σ(k=0 to n) (-1)^k C(n,k)(n-k)^m

- For |A| = |B| = n, number of onto (bijective) functions = n! (permutations)

- PIGEONHOLE PRINCIPLE COROLLARY: If |A| < |B|, no function f: A → B can be onto

## Key Points

- To prove f is onto: take arbitrary y ∈ B, solve f(x) = y to find x ∈ A

- To prove f is NOT onto: find ONE element in B with no preimage

- Onto functions guarantee "coverage" of the entire codomain

- Every function is onto when restricted to its image as codomain

- The inverse of a function exists if and only if the function is bijective

- Onto functions have RIGHT INVERSES; one-to-one functions have LEFT INVERSES

## Common Mistakes to Avoid

- CONFUSING RANGE WITH CODOMAIN: The range is always a subset of the codomain. A function is onto only when they are equal

- INCORRECT PROOF APPROACH: Do not simply give examples—proofs require arbitrary elements and general solutions

- FORGETTING THE DOMAIN CONSTRAINT: When solving f(x) = y, ensure the solution x actually belongs to the domain

- IGNORING THE PIGEONHOLE PRINCIPLE: If domain has fewer elements than codomain, onto is impossible—this provides quick disproof

## Revision Tips

- Practice proving both onto and non-onto cases with various function types (linear, polynomial, constant)

- Memorize the inclusion-exclusion counting formula and practice with small values of m and n

- Draw mapping diagrams for visual understanding of the onto property

- Solve previous year DU question papers to understand the exam pattern and common question types