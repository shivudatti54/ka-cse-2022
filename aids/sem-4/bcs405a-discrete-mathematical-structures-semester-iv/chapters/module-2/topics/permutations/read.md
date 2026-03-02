# Permutations

## Introduction

Permutations form one of the fundamental concepts in combinatorics, which is the branch of mathematics dealing with counting, arranging, and selecting objects. In the context of Computer Science and discrete mathematics, permutations are essential for understanding how to count arrangements of objects in different scenarios. The word "permutation" itself means arrangement—the order in which objects are placed becomes crucial, distinguishing permutations from combinations where order does not matter.

The study of permutations has significant applications in computer science, particularly in algorithm analysis, cryptography, and data structures. When we arrange elements in different orders, we are dealing with permutations. For example, generating all possible orders in which tasks can be performed, arranging files in memory, or even understanding how different sorting algorithms work all rely on the principles of permutations. In this chapter, we will explore the definition of permutations, formulas for calculating them, various types of permutations, and their applications through detailed examples.

Understanding permutations is crucial for the Fundamental Principles of Counting that form the backbone of combinatorial mathematics. Together with combinations, these concepts help us solve complex counting problems that appear frequently in competitive programming, database management, and network communications. The distinction between permutations and combinations—where one considers order and the other does not—is a fundamental concept that students must master to succeed in advanced topics.

## Key Concepts

### Definition of Permutations

A permutation is an ordered arrangement of distinct objects taken from a set. The key characteristic that differentiates permutations from combinations is that in permutations, the order of arrangement matters. For instance, the arrangements ABC and BCA are considered different permutations because the elements appear in different orders. If we were merely selecting elements (combinations), these would be considered the same set.

Formally, a permutation of n distinct objects taken r at a time (where 0 ≤ r ≤ n) is an arrangement of r objects selected from n distinct objects in a specific order. We denote this as nPr or P(n, r), which represents the number of ways to arrange r objects chosen from n distinct objects.

### Permutations of n Objects (All at Once)

When we wish to arrange all n distinct objects in a row, the number of permutations is given by n!, read as "n factorial." This is because we have n choices for the first position, (n-1) choices for the second position, (n-2) choices for the third, and so on, until we have only one choice for the last position.

The factorial notation is defined as:
- n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1
- 0! = 1 (by definition)

For example, if we have 4 distinct books and wish to arrange them on a shelf, the number of possible arrangements is 4! = 4 × 3 × 2 × 1 = 24.

### Permutations of n Objects Taken r at a Time

When we want to arrange only r objects selected from n distinct objects (where r < n), the formula becomes:

nPr = n! / (n-r)!

This formula can be derived from the factorial definition. We have n choices for the first position, (n-1) for the second, (n-2) for the third, continuing until we have (n-r+1) choices for the r-th position. Multiplying these choices gives us n × (n-1) × (n-2) × ... × (n-r+1), which simplifies to n! / (n-r)!.

### Circular Permutations

When objects are arranged in a circle, the concept of position changes. In circular permutations, only the relative order matters, not the absolute position. This is because rotating a circular arrangement does not create a new permutation. For n distinct objects arranged in a circle, the number of permutations is (n-1)!.

This can be understood by fixing one object's position (to account for rotational symmetry) and then arranging the remaining (n-1) objects in (n-1)! ways. For example, if 5 people are to be seated around a circular table, the number of different seating arrangements is (5-1)! = 4! = 24.

However, if the circle has a distinguished starting point (like a head table position), then we treat it as a linear arrangement, and the count becomes n!.

### Permutations with Repetition

Sometimes we need to arrange objects where some objects are identical. When we have n objects with some repetitions—say a objects of type 1, b objects of type 2, c objects of type 3, and so on, where a + b + c + ... = n—the number of distinct permutations is:

n! / (a! × b! × c! × ...)

For example, arranging the letters in the word "STATISTICS" involves 10 letters where S appears 3 times, T appears 3 times, A appears 1 time, I appears 2 times, and C appears 1 time. The number of distinct arrangements is 10! / (3! × 3! × 1! × 2! × 1!).

### Permutations of Multi-sets

A multi-set is a generalization of a set where elements can appear multiple times. The permutation formula for multi-sets follows the same principle as permutations with repetition. If we have a multi-set with k distinct elements where element i appears ni times, the number of distinct permutations is:

n! / (n1! × n2! × ... × nk!)

## Examples

### Example 1: Counting Linear Arrangements

**Problem:** In how many ways can 7 different books be arranged on a shelf?

**Solution:**
Since we are arranging all 7 distinct books, we use the formula for permutations of n objects taken all at once.

Number of arrangements = 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040

**Answer:** There are 5,040 different ways to arrange the 7 books.

### Example 2: Permutations Taken r at a Time

**Problem:** How many 3-digit numbers can be formed using the digits 1, 2, 3, 4, 5 if digits cannot be repeated?

**Solution:**
Here we need to arrange 3 digits chosen from 5 distinct digits, with no repetition allowed. This is a permutation of 5 objects taken 3 at a time.

Using the formula: 5P3 = 5! / (5-3)! = 5! / 2! = (5 × 4 × 3 × 2 × 1) / 2 = 60

Alternatively, we can think step-by-step:
- First digit: 5 choices (1, 2, 3, 4, 5)
- Second digit: 4 choices (remaining 4 digits)
- Third digit: 3 choices (remaining 3 digits)
- Total = 5 × 4 × 3 = 60

**Answer:** 60 different 3-digit numbers can be formed.

### Example 3: Circular Permutations

**Problem:** In how many ways can 6 friends be seated around a circular dinner table?

**Solution:**
For circular permutations, we fix one person's position to account for rotational symmetry and arrange the remaining (n-1) people linearly.

Number of arrangements = (6-1)! = 5! = 5 × 4 × 3 × 2 × 1 = 120

**Answer:** The 6 friends can be seated in 120 different ways around the table.

### Example 4: Permutations with Repeated Elements

**Problem:** How many distinct arrangements can be made from the letters of the word "COMPUTER"?

**Solution:**
The word "COMPUTER" has 8 distinct letters, with no repetitions. Therefore, the number of arrangements is simply 8! = 40,320.

**Answer:** There are 40,320 distinct arrangements.

### Example 5: Permutations with Some Repeated Elements

**Problem:** Find the number of distinct arrangements of the letters in the word "BANANA".

**Solution:**
The word "BANANA" has 6 letters where:
- A appears 3 times
- B appears 1 time
- N appears 2 times

Using the formula for permutations with repetition:
Number of arrangements = 6! / (3! × 1! × 2!) = 720 / (6 × 1 × 2) = 720 / 12 = 60

**Answer:** There are 60 distinct arrangements of the letters in "BANANA".

## Exam Tips

1. **Understand the fundamental difference**: Remember that permutations consider ORDER while combinations do not. When solving problems, first determine whether order matters in the context.

2. **Identify when to use each formula**: For arranging all n objects, use n!. For arranging r objects from n, use n!/(n-r)!. For circular arrangements, use (n-1)!. For repeated objects, use n!/(a!b!c!...).

3. **Check for repetition constraints**: Always determine if the problem states "digits cannot be repeated" or allows repetition. This changes the approach entirely.

4. **For circular permutations, remember to fix one position**: When dealing with arrangements around a circle, fix one object to eliminate rotational duplicates, then arrange the remaining.

5. **Simplify factorials when possible**: Instead of calculating large factorials completely, cancel terms. For example, 10P3 = 10!/(10-3)! = 10!/7! = 10 × 9 × 8 = 720.

6. **Distinguish between linear and circular contexts**: A line of people and people around a circular table yield different counts even with the same number of people.

7. **Watch for key words**: Words like "arrange," "order," "sequence," "seated," or "positioned" typically indicate permutations. Words like "select," "choose," "form a committee," or "combination" typically indicate combinations.

8. **Practice both direct counting and formula approaches**: Understanding both methods helps verify answers and builds conceptual clarity, which is essential for solving complex problems.