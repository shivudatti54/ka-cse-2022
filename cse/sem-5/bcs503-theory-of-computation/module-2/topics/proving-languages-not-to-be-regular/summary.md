# Proving Languages Not to Be Regular - Summary

## Key Definitions and Concepts

- **Pumping Lemma**: A necessary condition for regularity. If L is regular, there exists pumping length p such that every string s ∈ L with |s| ≥ p can be written as xyz where |y| > 0, |xy| ≤ p, and xyⁱz ∈ L for all i ≥ 0.

- **Myhill-Nerode Theorem**: A language L is regular iff the equivalence relation R_L has finitely many equivalence classes (or equivalently, there are finitely many pairwise distinguishable strings).

- **Distinguishable Strings**: Two strings x and y are distinguishable with respect to L if there exists a string z such that exactly one of xz and yz belongs to L.

- **Pumping Length (p)**: A constant guaranteed to exist for any regular language, used as the threshold for the pumping lemma.

## Important Formulas and Theorems

- **Pumping Lemma Condition**: xyⁱz ∈ L for all i ≥ 0
- **Constraints**: |y| > 0 and |xy| ≤ p
- **Myhill-Nerode**: L is regular ⇔ |R_L| is finite
- **Closure Operations**: Union, intersection, complement, homomorphism, and inverse homomorphism preserve regularity

## Key Points

- Pumping Lemma provides a necessary but not sufficient condition for regularity
- To prove non-regularity using Pumping Lemma: assume regular → choose string → show contradiction
- The string chosen must have length at least p (the pumping length)
- All possible decompositions of the string must lead to contradiction
- Myhill-Nerode is both necessary and sufficient for regularity
- An infinite set of pairwise distinguishable strings proves non-regularity
- Classic non-regular languages: {aⁿbⁿ}, {ww}, {ww^R}, {aᵖ | p is prime}

## Common Mistakes to Avoid

1. Choosing a string that is too short (length < p)
2. Not considering all possible decompositions of the string into xyz
3. Failing to satisfy the constraint |xy| ≤ p
4. Confusing necessary vs. sufficient conditions
5. Incorrectly applying closure properties (some operations don't preserve regularity)

## Revision Tips

1. Memorize the statement of Pumping Lemma exactly
2. Practice at least 5 classic proofs: aⁿbⁿ, ww, ww^R, aᵖ (prime), equal number of a's and b's
3. Understand the intuition: finite automata have limited memory, cannot count arbitrarily high
4. Keep both methods (Pumping Lemma and Myhill-Nerode) in your toolkit
5. In exams, always state what you're assuming before deriving contradiction
