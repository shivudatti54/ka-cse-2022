# Pigeonhole Principle - Summary

## Key Definitions and Concepts

- **Pigeonhole Principle:** If n items are placed into m containers where n > m, at least one container holds at least two items.
- **Generalized Pigeonhole Principle:** If n items are placed into m containers, at least one container holds at least ⌈n/m⌉ items.
- **Pigeons:** The items being distributed or placed
- **Pigeonholes:** The containers, categories, or sets into which items are placed
- **Ceiling Function ⌈x⌉:** Smallest integer greater than or equal to x
- **Floor Function ⌊x⌋:** Greatest integer less than or equal to x

## Important Formulas and Theorems

- **Basic Form:** If n > m, then some container has ≥ 2 items
- **Generalized Form:** If n items into m containers, then max ≥ ⌈n/m⌉
- **Converse:** If max ≤ k, then n ≤ mk
- **For guaranteeing at least k in one container:** Need n > m(k-1), i.e., n ≥ m(k-1) + 1
- **For birthday problem:** With n days and d people, probability of collision increases dramatically when d ≈ √n

## Key Points

- The principle guarantees existence, not construction
- Always identify what represents "items" and what represents "categories"
- Remainders modulo m create exactly m categories
- In graph theory, R(3,3) = 6 (Ramsey number)
- The principle is fundamental to hash table collision analysis
- Minimum guaranteed value is ⌈n/m⌉, not ⌊n/m⌋
- The principle extends to any function between finite sets

## Common Mistakes to Avoid

- Confusing ⌈n/m⌉ with ⌊n/m⌋ — remember ceiling gives minimum maximum
- Incorrectly identifying pigeons and pigeonholes in complex scenarios
- Forgetting that the principle gives a guaranteed minimum, not an exact count
- Applying the principle when n ≤ m (no guarantee in this case)
- Using "at most" statements when the problem asks for "at least"

## Revision Tips

1. Practice converting word problems into pigeonhole formulations
2. Memorize the formula ⌈n/m⌉ for the generalized principle
3. Work through at least 5-6 varied examples before the exam
4. Focus on remainder-based problems as they are most common in DU exams
5. Understand the connection to hash tables and the birthday paradox for CS applications