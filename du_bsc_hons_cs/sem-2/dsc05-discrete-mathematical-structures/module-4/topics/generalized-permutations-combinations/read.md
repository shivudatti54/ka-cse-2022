# Generalized Permutations and Combinations

## Introduction

Generalized permutations and combinations extend the fundamental counting principles to more complex scenarios where repetition of objects is allowed or where the arrangement of objects follows specific constraints. While basic permutations and combinations assume distinct objects without repetition, real-world problems often require us to count arrangements involving repeated elements, arrangements in circles, or selections from multi-sets (collections where elements may repeat).

This topic is crucial for computer science students as it forms the foundation for algorithm analysis, particularly in understanding the time complexity of algorithms that involve generating all possible arrangements. Additionally, these counting techniques are extensively used in probability theory, combinatorial optimization, and cryptography. In the context of DU's BSc (H) Computer Science program, this topic typically appears in the DSC05 paper and carries significant weight in both internal assessments and end-semester examinations.

The generalized counting methods discussed in this chapter—including permutations with repetition, combinations with repetition, circular permutations, and the stars and bars technique—provide powerful tools for solving problems that appear in competitive coding competitions and technical interviews conducted by top IT companies.

## Key Concepts

### 1. Permutations with Repetition (Permutations of Multisets)

When we have a multi-set containing n objects where some objects are identical, the number of distinct permutations is given by:

If the multi-set contains n objects with r₁ identical objects of type 1, r₂ identical objects of type 2, ..., rₖ identical objects of type k, where r₁ + r₂ + ... + rₖ = n, then:

**Number of distinct permutations = n! / (r₁! × r₂! × ... × rₖ!)**

This formula accounts for the fact that interchanging identical objects does not create a new arrangement.

### 2. Combinations with Repetition ( selections from Multi-sets)

When selecting r objects from a set of n distinct objects where repetition is allowed (each object can be selected multiple times), the number of distinct selections is given by the formula:

**C(n + r - 1, r) = (n + r - 1)! / [r!(n - 1)!]**

This is also known as "combinations with replacement" and can be visualized using the stars and bars method.

### 3. The Stars and Bars Method

The stars and bars technique provides a visual representation for solving distribution problems. For distributing r identical objects into n distinct boxes (where boxes can be empty), we use:

**Number of ways = C(n + r - 1, r)**

The method involves representing the r identical objects as stars (*) and using (n - 1) bars (|) to separate the stars into n groups, each group representing the contents of one box.

### 4. Circular Permutations

When arranging n distinct objects around a circle, the number of distinct arrangements is:

**(n - 1)!**

This is because in circular arrangements, rotations are considered equivalent. If clockwise and counter-clockwise arrangements are considered the same (i.e., reflection is not distinct), then the number is (n - 1)!/2 for n ≥ 3.

For arranging n beads of different colors in a necklace (where flipping is allowed), the formula becomes (n - 1)!/2 for n > 2.

### 5. Distribution of Distinct Objects

- **Distribution of n distinct objects into r distinct boxes (boxes can be empty):** rⁿ ways
- **Distribution of n distinct objects into r distinct boxes (no box empty):** r! × S(n, r), where S(n, r) are Stirling numbers of the second kind
- **Distribution of n distinct objects into r identical boxes (no box empty):** S(n, r) ways
- **Distribution of n identical objects into r distinct boxes (no box empty):** C(n - 1, r - 1) ways

### 6. Principle of Inclusion-Exclusion (Extension)

For counting arrangements with restrictions, the principle of inclusion-exclusion can be extended. For example, to count permutations of n elements where specific elements must not be in specific positions, we use derangements (subfactorials):

**Number of derangements D(n) = n! × Σ(k=0 to n) [(-1)ᵏ / k!]**

This can be approximated as D(n) ≈ n!/e.

## Examples

### Example 1: Permutations of a Multiset

**Problem:** How many distinct arrangements can be formed using the letters of the word "STATISTICS"?

**Solution:**

The word "STATISTICS" has 10 letters with the following frequencies:
- S appears 3 times
- T appears 3 times
- A appears 1 time
- I appears 2 times
- C appears 1 time

Using the formula for permutations of a multi-set:
Number of arrangements = 10! / (3! × 3! × 1! × 2! × 1!)

Calculating:
10! = 3,628,800
3! = 6, so 3! × 3! × 2! = 6 × 6 × 2 = 72

Number of arrangements = 3,628,800 / 72 = 50,400

Therefore, there are 50,400 distinct arrangements of the letters in "STATISTICS".

### Example 2: Combinations with Repetition

**Problem:** A shop sells 5 different varieties of ice cream. In how many ways can a customer buy 8 ice creams (where order doesn't matter but repetition is allowed)?

**Solution:**

This is a classic combinations with repetition problem where we select 8 items from 5 distinct types with repetition allowed.

Using the formula: C(n + r - 1, r) = C(5 + 8 - 1, 8) = C(12, 8)

C(12, 8) = C(12, 4) = (12 × 11 × 10 × 9) / (4 × 3 × 2 × 1) = 11,880 / 4 = 495

Alternatively, using stars and bars: We need to distribute 8 identical ice creams among 5 distinct varieties. Represent this as 8 stars and 4 bars:

Number of solutions = C(8 + 5 - 1, 5 - 1) = C(12, 4) = 495

**Answer:** 495 ways

### Example 3: Circular Arrangements

**Problem:** In how many ways can 7 different friends be seated around a circular table such that two particular friends always sit together?

**Solution:**

**Step 1:** Treat the two particular friends as a single entity.
Now we have 6 entities (the pair + 5 other friends) to arrange around the circle.

**Step 2:** Number of circular arrangements of 6 entities = (6 - 1)! = 5! = 120

**Step 3:** Within the pair, the two friends can be arranged in 2! = 2 ways.

**Step 4:** Total arrangements = 120 × 2 = 240

Therefore, there are 240 ways to seat the 7 friends such that the two particular friends sit together.

### Example 4: Distribution Problems

**Problem:** In how many ways can 4 distinct balls be distributed into 3 distinct boxes if boxes can remain empty?

**Solution:**

Each of the 4 distinct balls has 3 choices (any of the 3 boxes).

Total ways = 3⁴ = 81

**Answer:** 81 ways

**Follow-up:** If no box can remain empty, we need to subtract cases where at least one box is empty.

Using inclusion-exclusion:
- Total distributions: 3⁴ = 81
- Subtract distributions where box 1 is empty: 2⁴ = 16
- Similarly for boxes 2 and 3: 3 × 16 = 48
- Add back distributions where boxes 1 and 2 are empty: 1⁴ = 1
- Similarly for other pairs: 3 × 1 = 3
- Subtract distributions where all boxes are empty: 0 (impossible)

Using inclusion-exclusion: 81 - 48 + 3 = 36

Or using the formula: 3! × S(4, 3) = 6 × 6 = 36

## Exam Tips

1. **Identify the problem type correctly:** Always determine whether you're dealing with permutations (arrangements where order matters) or combinations (selections where order doesn't matter), and whether repetition is allowed.

2. **Master the stars and bars technique:** This is frequently tested in DU exams. Remember: distributing r identical objects into n distinct boxes gives C(n + r - 1, r).

3. **Circular permutations formula:** For n distinct objects around a circle, use (n - 1)!. For necklaces where flipping is allowed, use (n - 1)!/2 for n > 2.

4. **Multi-set permutations:** When objects repeat, divide by the factorials of the counts of each repeated object. This is crucial for anagram problems.

5. **Box distribution problems:** Distinguish between distinct and identical boxes/objects, and whether boxes can be empty. Use the appropriate formula (rⁿ for distinct boxes with distinct objects, or combinations with repetition for identical objects).

6. **Derangements:** Remember the formula D(n) = n! × Σ(-1)ᵏ/k! for counting arrangements where no element is in its original position.

7. **Practice inclusion-exclusion:** For problems with restrictions, systematically apply the inclusion-exclusion principle to count valid arrangements.

8. **Check boundary conditions:** Always consider edge cases like n = 1, 2 for circular arrangements, and verify if reflection symmetry applies.