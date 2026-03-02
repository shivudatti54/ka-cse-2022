# Permutations and Combinations

## Introduction

Permutations and combinations form the cornerstone of combinatorial mathematics, a branch of discrete mathematics that deals with counting, arranging, and selecting objects. These concepts are fundamental to computer science, particularly in algorithm analysis, probability theory, cryptography, and data structures. For students at the University of Delhi studying Discrete Mathematical Structures, mastering permutations and combinations is essential as they provide the mathematical foundation for understanding how to count possibilities efficiently without enumerating each case individually.

The distinction between permutations and combinations lies in whether the order of selection matters. When arranging objects where the sequence is important (such as ranking contestants or forming passwords), we use permutations. When selecting objects where only the composition matters (such as forming committees or choosing items from a menu), we use combinations. This seemingly simple distinction leads to different formulas and applications, making it crucial for students to understand when to apply each concept.

In the context of real-world computing applications, permutations are used in password cracking algorithms, sorting algorithms, and generating all possible orderings. Combinations appear in database query optimization, network routing, and combinatorial game theory. Understanding these concepts deeply will help you appreciate their applications in algorithm design and computational complexity.

## Key Concepts

### Fundamental Principle of Counting (Multiplication Rule)

The fundamental principle of counting states: If a task can be performed in m ways and after performing it in any of these ways, a second task can be performed in n ways, then both tasks can be performed in m × n ways. This principle extends to any number of tasks. For example, if you have 3 shirts, 4 pants, and 2 shoes, the number of different outfits you can wear is 3 × 4 × 2 = 24.

### Permutations

A permutation is an arrangement of objects in a specific order where the order matters. The number of permutations of n distinct objects taken r at a time is denoted as P(n,r), nPr, or nPk, and is calculated using the formula:

**P(n,r) = n! / (n-r)!**

Where n! (n factorial) = n × (n-1) × (n-2) × ... × 2 × 1, and by convention, 0! = 1.

**Special Cases:**
- Permutations of all n objects: P(n,n) = n!
- Permutations with repetition: If there are n objects where some are identical, the formula adjusts accordingly.

**Permutations with Repeated Elements:**
If we have n objects with n₁ identical of type 1, n₂ identical of type 2, ..., nk identical of type k, where n₁ + n₂ + ... + nk = n, then the number of distinct permutations is:
**n! / (n₁! × n₂! × ... × nk!)**

### Combinations

A combination is a selection of objects where the order does not matter. The number of combinations of n distinct objects taken r at a time is denoted as C(n,r), nCr, or (n choose r), and is calculated using the formula:

**C(n,r) = n! / [r! × (n-r)!]**

This formula can also be written as: C(n,r) = nCr = n! / (r!(n-r)!)

**Key Properties of Combinations:**
1. C(n,0) = C(n,n) = 1
2. C(n,r) = C(n,n-r) (Symmetry property)
3. C(n,r) + C(n,r-1) = C(n+1,r) (Pascal's Identity)
4. C(n,0) + C(n,1) + ... + C(n,n) = 2^n

### Circular Permutations

When arranging objects in a circle, the concept of circular permutations applies. The number of distinct arrangements of n distinct objects around a circle is (n-1)!. This is because in circular arrangements, only the relative order matters, not the absolute position. For example, arranging 5 people around a round table yields (5-1)! = 24 different seatings.

If clockwise and counter-clockwise arrangements are considered the same (i.e., the table is not oriented), we divide by 2, giving (n-1)!/2 arrangements.

### Binomial Theorem and Combinations

The binomial theorem expresses the expansion of (a + b)^n as:
**(a + b)^n = Σ C(n,r) × a^(n-r) × b^r** (where r ranges from 0 to n)

The coefficients C(n,0), C(n,1), ..., C(n,n) are called binomial coefficients.

## Examples

### Example 1: Permutations Problem

**Problem:** In how many ways can 7 different books be arranged on a shelf if 3 particular books must always be together?

**Solution:**
Step 1: Treat the 3 particular books as a single unit. This gives us 5 units to arrange (the 3-book block + the other 4 individual books).

Step 2: Arrange these 5 units: P(5,5) = 5! = 120 ways.

Step 3: Arrange the 3 particular books within their block: 3! = 6 ways.

Step 4: Multiply by the fundamental principle of counting: 120 × 6 = 720 ways.

**Answer:** 720 ways

### Example 2: Combinations Problem

**Problem:** A committee of 5 is to be formed from 6 men and 4 women. In how many ways can this be done if the committee must contain exactly 2 women?

**Solution:**
Step 1: Select 2 women from 4 women: C(4,2) = 4!/(2!×2!) = 6 ways.

Step 2: Select the remaining 3 men from 6 men: C(6,3) = 6!/(3!×3!) = 20 ways.

Step 3: Apply multiplication rule: 6 × 20 = 120 ways.

**Answer:** 120 ways

### Example 3: Mixed Permutations and Combinations

**Problem:** From a standard deck of 52 cards, how many ways can we select 5 cards containing exactly 3 red cards and 2 black cards?

**Solution:**
Step 1: There are 26 red cards and 26 black cards in a deck.

Step 2: Select 3 red cards from 26: C(26,3) = 2600 ways.

Step 3: Select 2 black cards from 26: C(26,2) = 325 ways.

Step 4: Total ways = C(26,3) × C(26,2) = 2600 × 325 = 845,000 ways.

**Answer:** 845,000 ways

## Exam Tips

1. **Identify the Type First:** Always determine whether the problem involves permutation (order matters) or combination (order doesn't matter) before applying formulas. A common trick is to ask: "Does rearranging the selected objects create a new situation?"

2. **Use the Selection-Arrangement Test:** If you're selecting a subset and then arranging it, you may need both combinations and permutations. First select, then arrange if needed.

3. **Apply Complementary Counting:** Sometimes it's easier to count what you don't want and subtract from the total. For example, "at least one" problems often use complementary counting.

4. **Remember Special Cases:** Know when to apply circular permutation formula (n-1)! and when objects are identical, use the repetition formula.

5. **Use Pascal's Triangle:** For quick binomial coefficient calculations in exams, Pascal's triangle provides a visual method to compute C(n,r) without calculator.

6. **Check for Restrictions:** Always identify and handle restrictions first. For "must be together" problems, treat the restricted items as a single unit, then multiply by internal arrangements.

7. **Practice Binomial Expansion:** The binomial theorem frequently appears in exams. Remember that the coefficient of a^kb^(n-k) in (a+b)^n is C(n,k).