# Permutations - Summary

## Key Definitions and Concepts

- **Permutation**: An ordered arrangement of distinct objects taken from a set. The order of elements matters in permutations.
- **n! (n factorial)**: The product of all positive integers from n to 1, defined as n! = n × (n-1) × ... × 2 × 1, with 0! = 1
- **nPr**: The number of permutations of n objects taken r at a time
- **Circular Permutation**: An arrangement of objects around a circle where only relative order matters

## Important Formulas and Theorems

- **Permutation of n objects (all at once)**: nPn = n!
- **Permutation of n objects taken r at a time**: nPr = n!/(n-r)!
- **Circular permutation**: (n-1)! for n distinct objects
- **Permutation with repetition**: n!/(a!b!c!...) where a, b, c are the frequencies of repeated objects

## Key Points

1. Permutations consider ORDER while combinations do not—always check if order matters in the problem
2. The factorial notation n! represents the number of ways to arrange n distinct objects in a line
3. For circular arrangements, fix one position to account for rotational symmetry, giving (n-1)! arrangements
4. When objects repeat, divide the total arrangements by the factorials of each repeated object's frequency
5. 0! = 1 by definition, which is essential for formulas when r = n
6. The product method: nPr = n × (n-1) × (n-2) × ... × (n-r+1) is often easier for computation
7. For circular permutations with distinguishable seats, treat as linear arrangements (n!)

## Common Mistakes to Avoid

1. Treating all problems as linear permutations when circular arrangements require (n-1)!
2. Forgetting to account for repeated elements when arranging letters in words
3. Using combinations instead of permutations when order matters
4. Not checking whether repetition is allowed in the problem
5. Including rotational symmetries in circular arrangements when they should be excluded

## Revision Tips

1. Practice identifying keywords in problems that indicate permutations vs combinations
2. Work through at least 5 problems each of linear, circular, and repeated-element permutations
3. Remember the derivation of formulas—understanding why the formula works helps with memory
4. Create a decision tree: Is order important? → Yes → Is it circular? → Yes/No → Are there repeats? → Build the answer step by step
5. Practice simplifying factorials without fully calculating large numbers