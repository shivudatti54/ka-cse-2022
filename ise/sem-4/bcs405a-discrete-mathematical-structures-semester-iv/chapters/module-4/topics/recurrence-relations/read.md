# Recurrence Relations and Master Theorem

## Introduction to Recurrence Relations

In the analysis of algorithms, particularly those following the **Divide and Conquer** paradigm, we often encounter functions that are defined in terms of themselves. These are called **recurrence relations**. A recurrence relation expresses the value of a function in terms of its values for smaller inputs.

For example, the recurrence relation for Merge Sort is:

```
T(n) = 2T(n/2) + Θ(n)
```

This represents that the time to sort an array of size n is equal to the time to sort two halves (each of size n/2) plus the time to merge them (which is linear in n).

## Solving Recurrence Relations

There are several methods to solve recurrence relations:

### 1. Substitution Method

The substitution method involves:

1. Guess the form of the solution
2. Use mathematical induction to prove the guess is correct

**Example**: Solve T(n) = 2T(n/2) + n
Guess: T(n) = O(n log n)
Assume: T(n/2) ≤ c(n/2)log(n/2)
Then: T(n) ≤ 2[c(n/2)log(n/2)] + n = cn log(n/2) + n = cn log n - cn + n ≤ cn log n (for c ≥ 1)

### 2. Recursion Tree Method

This method involves drawing a tree that represents the recursive calls and summing the costs at each level.

```
         Level 0:         cn
                        /    \
        Level 1:   c(n/2)    c(n/2)
                    /  \      /  \
        Level 2: c(n/4) c(n/4) c(n/4) c(n/4)
        ...
        Level log n: T(1) T(1) ... T(1) [n leaves]
```

The total cost is the sum of all levels:
T(n) = cn + cn + cn + ... + cn (log n times) = cn log n = O(n log n)

### 3. Master Theorem

The Master Theorem provides a "cookbook" solution for recurrences of the form:

```
T(n) = aT(n/b) + f(n)
```

where:

- a ≥ 1 (number of subproblems)
- b > 1 (factor by which problem size reduces)
- f(n) is asymptotically positive

## The Master Theorem

The Master Theorem states that for a recurrence of the form T(n) = aT(n/b) + f(n):

### Case 1: If f(n) = O(n^(log_b a - ε)) for some ε > 0

Then: T(n) = Θ(n^(log_b a))

### Case 2: If f(n) = Θ(n^(log_b a) \* log^k n) for some k ≥ 0

Then: T(n) = Θ(n^(log_b a) \* log^(k+1) n)

### Case 3: If f(n) = Ω(n^(log_b a + ε)) for some ε > 0

And if af(n/b) ≤ cf(n) for some c < 1 and all sufficiently large n
Then: T(n) = Θ(f(n))

## Master Theorem Examples

**Example 1**: T(n) = 9T(n/3) + n

- a = 9, b = 3, f(n) = n
- n^(log_b a) = n^(log_3 9) = n²
- Compare f(n) = n with n²: n = O(n^(2-ε)) for ε = 1
- Case 1 applies: T(n) = Θ(n²)

**Example 2**: T(n) = T(2n/3) + 1

- a = 1, b = 3/2, f(n) = 1
- n^(log*b a) = n^(log*(3/2) 1) = n⁰ = 1
- f(n) = Θ(1) = Θ(n^(log_b a))
- Case 2 applies: T(n) = Θ(log n)

**Example 3**: T(n) = 3T(n/4) + n log n

- a = 3, b = 4, f(n) = n log n
- n^(log_b a) = n^(log_4 3) ≈ n^0.793
- Compare f(n) = n log n with n^0.793: n log n = Ω(n^(0.793+ε)) for ε ≈ 0.2
- Check regularity condition: 3f(n/4) = 3(n/4)log(n/4) ≤ (3/4)n log n = cf(n) for c = 3/4 < 1
- Case 3 applies: T(n) = Θ(n log n)

## Special Cases and Limitations

The Master Theorem doesn't cover all recurrences. Some important limitations:

1. Doesn't apply when f(n) is not polynomial
2. Doesn't work when a is not constant
3. Doesn't handle cases where the subproblems are not of equal size

For recurrences that don't fit the Master Theorem form, other methods like the Akra-Bazzi method or generating functions may be used.

## Comparison of Solving Methods

| Method         | When to Use                             | Advantages     | Disadvantages                  |
| -------------- | --------------------------------------- | -------------- | ------------------------------ |
| Substitution   | When you can guess the form             | Rigorous proof | Requires good guess            |
| Recursion Tree | Visualizing the recurrence              | Intuitive      | Can be messy for complex cases |
| Master Theorem | Standard divide-and-conquer recurrences | Quick solution | Limited applicability          |

## Applications in Divide and Conquer Algorithms

**Merge Sort**: T(n) = 2T(n/2) + Θ(n)

- a = 2, b = 2, f(n) = Θ(n)
- n^(log_b a) = n^(log_2 2) = n¹ = n
- f(n) = Θ(n) = Θ(n^(log_b a))
- Case 2 applies: T(n) = Θ(n log n)

**Binary Search**: T(n) = T(n/2) + Θ(1)

- a = 1, b = 2, f(n) = Θ(1)
- n^(log_b a) = n^(log_2 1) = n⁰ = 1
- f(n) = Θ(1) = Θ(n^(log_b a))
- Case 2 applies: T(n) = Θ(log n)

**Strassen's Matrix Multiplication**: T(n) = 7T(n/2) + Θ(n²)

- a = 7, b = 2, f(n) = Θ(n²)
- n^(log_b a) = n^(log_2 7) ≈ n^2.81
- f(n) = Θ(n²) = O(n^(2.81-ε)) for ε ≈ 0.81
- Case 1 applies: T(n) = Θ(n^(log_2 7)) ≈ Θ(n^2.81)

## Exam Tips

1. **Identify the form**: Always check if the recurrence fits T(n) = aT(n/b) + f(n)
2. **Calculate log_b a**: This is the critical exponent for comparison
3. **Check cases in order**: Always check Case 2 first, as it's the most common
4. **Verify regularity for Case 3**: Don't forget to check af(n/b) ≤ cf(n) for some c < 1
5. **Practice common recurrences**: Memorize the solutions for standard algorithms
6. **When Master Theorem doesn't apply**: Be prepared to use substitution or recursion tree methods
7. **Watch for special cases**: Some recurrences might need algebraic manipulation before applying the theorem

Remember that the Master Theorem is a powerful tool but has limitations. Understanding the proof and intuition behind it will help you apply it correctly and recognize when other methods are needed.
