# Counting Principles, Permutations, and Combinations

## Introduction

Counting principles form the bedrock of discrete mathematics and computer science. These fundamental techniques allow us to systematically determine the number of ways objects can be arranged, selected, or combined without listing each possibility—a task that would be impossible for large numbers. Whether you're analyzing algorithm complexity, computing probabilities, or solving real-world selection problems, counting techniques provide the mathematical framework essential for efficient problem-solving.

In computer science, these principles underpin critical applications: database query optimization uses combinations to evaluate join orders; network protocols analyze message sequences through permutations; probability calculations in machine learning rely on combinations for feature selection; and cryptographic algorithms depend on counting arguments for security analysis. For DU MCA students, mastering these techniques is not merely an academic exercise but a practical necessity for advanced courses in algorithms, data structures, and theoretical computer science.

This module covers the fundamental counting principles—the product rule and addition rule—followed by permutations and combinations, which represent the two primary ways of arranging or selecting objects from a set. We also explore the pigeonhole principle and inclusion-exclusion principle, which provide powerful tools for proving existence and counting complex scenarios.

## Key Concepts

### 1. Fundamental Counting Principle (Product Rule)

The **Product Rule** states: If a first task can be performed in m ways and a second task can be performed in n ways (after the first task is completed), then the total number of ways to perform both tasks is m × n ways.

More generally, if k tasks can be performed in n₁, n₂, ..., nₖ ways respectively, then the total number of ways to perform all k tasks in sequence is n₁ × n₂ × ... × nₖ.

**Key condition**: Each task must be performed, and the choices for each task must be independent (the number of choices for one task does not affect the others).

### 2. Addition Rule (Sum Rule)

The **Addition Rule** states: If a task can be performed in m ways or a second task can be performed in n ways (but not both simultaneously), then the total number of ways to perform either task is m + n ways.

**Important distinction**: This rule applies when tasks are **mutually exclusive**—they cannot happen together. If there is overlap, we must use the inclusion-exclusion principle.

### 3. Permutations

A **permutation** is an ordered arrangement of distinct objects where the order matters.

**Permutation without repetition**: The number of ways to arrange n distinct objects taken r at a time is:

$$P(n,r) = \frac{n!}{(n-r)!} = n \times (n-1) \times (n-2) \times \ldots \times (n-r+1)$$

Where n! (n factorial) = n × (n-1) × (n-2) × ... × 2 × 1, and 0! = 1.

**Special case**: When r = n, we have P(n,n) = n! — the number of ways to arrange all n distinct objects.

**Permutation with repetition**: When we have n objects where some are identical, the number of distinct arrangements is:

$$\frac{n!}{n_1! \times n_2! \times \ldots \times n_k!}$$

where n₁, n₂, ..., nₖ are the counts of each type of identical object, and n₁ + n₂ + ... + nₖ = n.

### 4. Combinations

A **combination** is a selection of objects where order does NOT matter.

**Combination without repetition**: The number of ways to choose r objects from n distinct objects is:

$$C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

This is read as "n choose r" and is called a **binomial coefficient**.

**Key relationship**: Since permutations count ordered arrangements and combinations count unordered selections, we have:
$$P(n,r) = C(n,r) \times r!$$

**Combination with repetition**: When selecting r objects from n types (with unlimited supply of each type), the number of ways is:

$$C(n+r-1, r) = \binom{n+r-1}{r}$$

This is also written as C(n+r-1, n-1).

### 5. Pigeonhole Principle

The **Basic Pigeonhole Principle** states: If n items are placed into m containers and n > m, then at least one container contains more than one item.

The **Generalized Pigeonhole Principle**: If n items are placed into m containers, then at least one container contains at least ⌈n/m⌉ items.

This simple yet powerful principle is used to prove existence results without constructing explicit examples.

### 6. Inclusion-Exclusion Principle

For two sets A and B:
$$|A \cup B| = |A| + |B| - |A \cap B|$$

For three sets A, B, and C:
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

This principle is essential for counting problems where direct counting is complicated by overlapping cases.

## Examples

### Example 1: Counting Passwords

**Problem**: How many different passwords can be created if each password consists of 2 letters followed by 2 digits, assuming:
(a) Letters can be any of 26 and digits can be any of 10 (repetition allowed)
(b) Letters can be any of 26 and digits can be any of 10 (no repetition allowed)

**Solution**:

(a) With repetition allowed:
- First letter: 26 choices
- Second letter: 26 choices (repetition allowed)
- First digit: 10 choices
- Second digit: 10 choices (repetition allowed)

Total = 26 × 26 × 10 × 10 = **67,600 passwords**

(b) Without repetition:
- First letter: 26 choices
- Second letter: 25 choices (cannot repeat first letter)
- First digit: 10 choices
- Second digit: 9 choices (cannot repeat first digit)

Total = 26 × 25 × 10 × 9 = **58,500 passwords**

### Example 2: Committee Selection

**Problem**: From a department of 8 men and 6 women, how many ways can we form a committee of 4 people that contains:
(a) Exactly 2 men
(b) At least 2 men
(c) Exactly 1 woman and the remaining men must include the department head

**Solution**:

(a) Exactly 2 men:
- Choose 2 men from 8: C(8,2) = 28
- Choose 2 women from 6: C(6,2) = 15
- Total = 28 × 15 = **420 committees**

(b) At least 2 men:
- Case 2 men: C(8,2) × C(6,2) = 28 × 15 = 420
- Case 3 men: C(8,3) × C(6,1) = 56 × 6 = 336
- Case 4 men: C(8,4) × C(6,0) = 70 × 1 = 70
- Total = 420 + 336 + 70 = **826 committees**

(c) Exactly 1 woman, committee must include department head (assume head is a man):
- The committee head is fixed (1 man)
- We need 2 more men from remaining 7: C(7,2) = 21
- Choose 1 woman from 6: C(6,1) = 6
- Total = 1 × 21 × 6 = **126 committees**

### Example 3: Pigeonhole Principle Application

**Problem**: Show that in any group of 10 people, at least 2 were born in the same month.

**Solution**: There are 12 months (containers) and 10 people (items). Since 10 < 12, the basic pigeonhole principle doesn't directly apply. However, consider this: We want to prove at least 2 share a month. Let's use the contrapositive: Assume all 10 were born in different months. Then we'd need 10 distinct months. Since there are only 12 months, this is possible—but we need to show a contradiction.

Actually, for 10 people and 12 months, it's possible to have all in different months (10 ≤ 12). So the statement is **false**—we cannot guarantee 2 in the same month.

For 13 people: With 13 people and 12 months, by pigeonhole principle, at least ⌈13/12⌉ = 2 people share a month. **Proof complete.**

### Example 4: Circular Arrangements

**Problem**: In how many ways can 5 men and 5 women be seated around a circular table such that:
(a) No restrictions
(b) Men and women alternate
(c) All men sit together

**Solution**:

(a) No restrictions: For circular arrangements, fix one person's position to account for rotation symmetry.
- Total = (10-1)! = 9! = **362,880 ways**

(b) Men and women alternate: 
- First, arrange the 5 men in a circle: (5-1)! = 4! = 24 ways
- Then place 5 women in the 5 gaps between men: 5! = 120 ways
- Total = 24 × 120 = **2,880 ways**

(c) All men sit together:
- Treat the 5 men as a single block: 5 women + 1 block = 6 entities
- Arrange these 6 around circle: (6-1)! = 5! = 120 ways
- Men can be arranged within their block: 5! = 120 ways
- Total = 120 × 120 = **14,400 ways**

## Exam Tips

1. **Read the problem carefully**: Identify whether order matters (permutations) or doesn't matter (combinations). The words "arrange," "order," "sequence" suggest permutations; "select," "choose," "committee" suggest combinations.

2. **Check for repetition**: Determine whether elements can be repeated. Phrases like "repetition allowed," "any number of times," or "unlimited" indicate repetition; "different," "distinct," "no repetition" means no repetition.

3. **Break complex problems into cases**: For "at least" or "at most" problems, sum the cases. For "exactly" problems, multiply the independent choices for each category.

4. **Apply the product rule for sequential decisions**: When making multiple independent choices, multiply the number of options. When choosing between mutually exclusive options, add.

5. **Remember the circular arrangement formula**: For n distinct objects around a circle, it's (n-1)!, not n!. This accounts for rotational symmetry.

6. **Use complementary counting when direct counting is complex**: Sometimes it's easier to count the total and subtract the cases you don't want: "at least one" = total - "none".

7. **The binomial coefficient identity**: Remember that C(n,r) = C(n,n-r). This symmetry can simplify calculations, especially when r > n/2.

8. **Pigeonhole principle problems**: Identify what are the "pigeons" (items) and what are the "holes" (categories/containers). Then apply the formula ⌈n/m⌉.