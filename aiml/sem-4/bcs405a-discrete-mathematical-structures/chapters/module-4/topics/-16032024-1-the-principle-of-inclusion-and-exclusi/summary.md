# Discrete Mathematical Structures

## The Principle of Inclusion and Exclusion

---

- The Principle of Inclusion and Exclusion (PIE) is a counting technique used to calculate the number of elements in the union of multiple sets.
- Definition: |A ∪ B| = |A| + |B| - |A ∩ B|
- Formula: |A1 ∪ A2 ∪ ... ∪ An| = ∑|Ai| - ∑|Ai ∩ Aj| + ... + (-1)^n-1 |Ai1 ∩ Ai2 ∩ ... ∩ An|

## Generalizations of the Principle

---

- Principle of Inclusion-Exclusion for more than two sets: generalized PIE
- Principle of Inclusion-Exclusion for finite sums: generalized PIE
- Principle of Inclusion-Exclusion for infinite sets: generalized PIE

## Derangements

---

- A derangement is a permutation of the elements of a set, such that no element is in its original position.
- Formula: D(n) = n! \* (1/0! - 1/1! + 1/2! - ... + (-1)^n/n!)
- Definition: A derangement of a set of n elements is a permutation of those elements such that no element is in its original position.

## Rook Polynomials

---

- A rook polynomial is a polynomial that encodes the number of ways to place a set of rooks (chess pieces) on a chessboard.
- Formula: R(n) = ∑(-1)^(n-k) \* C(n, k)
- Definition: A rook polynomial is a polynomial that counts the number of ways to place n rooks on an n x n chessboard, subject to certain constraints.
