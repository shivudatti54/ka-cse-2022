# Subset Sum Problem

## Introduction

The Subset Sum Problem is a fundamental NP-complete problem in computer science that appears extensively in cryptography, resource allocation, financial modeling, and combinatorial optimization. Given a set of integers and a target sum, the problem asks whether there exists a subset of the given integers that adds up exactly to the target sum.

This problem holds significant importance in the Design and Analysis of Algorithms course as it serves as a classic example of an NP-complete problem, helping students understand the boundaries of efficient computation. The Subset Sum Problem was one of Karp's original 21 NP-complete problems (1972), and its various approximations remain active areas of research.

In this module, we will explore both exponential-time brute force solutions and pseudo-polynomial dynamic programming approaches, understanding their complexity trade-offs and practical applications in real-world scenarios like knapsack problems, currency systems, and load balancing.

## Key Concepts

### Problem Definition

The Subset Sum Problem can be formally stated as:

**Input:** A set S = {s₁, s₂, ..., sₙ} of n positive integers and a target integer T.

**Output:** Determine whether there exists a subset S' ⊆ S such that the sum of all elements in S' equals exactly T.

### Variants

1. **Decision Problem:** Does a subset summing to T exist? (Yes/No)
2. **Optimization Problem:** Find the subset with sum closest to T without exceeding it
3. **Counting Problem:** Count the number of subsets that sum to T

### Approaches to Solve Subset Sum Problem

#### 1. Brute Force Approach (Exponential Time)

The naive approach generates all 2ⁿ possible subsets and checks each one's sum.

```
SUBSET-SUM(S, n, T):
    for i from 0 to 2ⁿ - 1:
        sum = 0
        for j from 0 to n - 1:
            if i-th bit of j is set:
                sum = sum + S[j]
        if sum == T:
            return true
    return false
```

**Time Complexity:** O(n × 2ⁿ)
**Space Complexity:** O(n) for recursion stack or O(1) for iterative

#### 2. Backtracking Approach

A more intelligent brute force that prunes branches when partial sum exceeds target:

```
SUBSET-SUM-BACKTRACK(S, n, T, current_sum, index):
    if current_sum == T:
        return true
    if index == n or current_sum > T:
        return false
    
    // Include current element
    if SUBSET-SUM-BACKTRACK(S, n, T, current_sum + S[index], index + 1):
        return true
    
    // Exclude current element
    return SUBSET-SUM-BACKTRACK(S, n, T, current_sum, index + 1)
```

**Time Complexity:** O(2ⁿ) in worst case, but much better in practice

#### 3. Dynamic Programming Approach (Pseudo-polynomial)

The DP solution creates a table where dp[i][j] represents whether a subset of the first i elements can sum to j.

```
SUBSET-SUM-DP(S, n, T):
    // Create DP table
    dp = 2D array of size (n+1) × (T+1)
    
    // Base case: sum 0 is always achievable
    for i from 0 to n:
        dp[i][0] = true
    
    // Base case: no elements, non-zero sum impossible
    for j from 1 to T:
        dp[0][j] = false
    
    // Fill the table
    for i from 1 to n:
        for j from 1 to T:
            if S[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] OR dp[i-1][j - S[i-1]]
    
    return dp[n][T]
```

**Time Complexity:** O(n × T)
**Space Complexity:** O(n × T), can be reduced to O(T) using 1D array

### Space Optimization

The 2D DP table can be reduced to 1D by iterating j from T down to S[i-1]:

```
SUBSET-SUM-DP-OPTIMIZED(S, n, T):
    dp = boolean array of size T+1, initialized to false
    dp[0] = true
    
    for i from 0 to n-1:
        for j from T down to S[i]:
            dp[j] = dp[j] OR dp[j - S[i]]
    
    return dp[T]
```

**Time Complexity:** O(n × T)
**Space Complexity:** O(T)

## Examples

### Example 1: Basic Subset Sum

**Problem:** Given set S = {3, 34, 4, 12, 5, 2} and target T = 9, determine if a subset sums to 9.

**Solution using DP:**

Step 1: Initialize dp[0] = true (sum of 0 is always possible)

Step 2: Process each element:

- Element 3: Update dp[3], dp[6], dp[9] = true
- Element 34: Too large, skip
- Element 4: Update dp[4], dp[7], dp[9] = true (already true)
- Element 12: Too large, skip
- Element 5: Update dp[5], dp[8], dp[9] = true (already true)
- Element 2: Update dp[2], dp[7], dp[9] = true (already true)

**Result:** dp[9] = true, so subset {4, 5} or {3, 4, 2} exists.

### Example 2: Subset Sum with No Solution

**Problem:** S = {2, 3, 7, 8}, T = 11

**DP Table Construction:**

| Elements | Sum=0 | Sum=1 | Sum=2 | ... | Sum=11 |
|----------|-------|-------|-------|-----|--------|
| ∅        | T     | F     | F     | ... | F      |
| {2}      | T     | F     | T     | ... | F      |
| {2,3}    | T     | F     | T     | ... | F      |
| {2,3,7}  | T     | F     | T     | ... | F      |
| {2,3,7,8}| T     | F     | T     | ... | F      |

**Result:** dp[11] = false, no subset sums to 11.

### Example 3: Space-Optimized Implementation

**Problem:** S = {1, 3, 4, 5}, T = 7

**Trace (1D DP):**

- Initial: dp = [T, F, F, F, F, F, F, F]
- After element 1: dp[1]=T
- After element 3: dp[4]=T (from dp[1]), dp[3]=T
- After element 4: dp[7]=T (from dp[3]), dp[5]=T, dp[4]=T
- After element 5: dp[7]=T (remains), dp[6]=T (from dp[1])

**Result:** dp[7] = true, subset {3, 4} or {1, 4, 5} exists.

## Exam Tips

1. **Remember the complexity trade-off:** The DP solution is pseudo-polynomial (O(n×T)), not truly polynomial. For large T, it becomes impractical.

2. **NP-Completeness context:** Understand that Subset Sum is NP-complete, meaning no polynomial-time algorithm is known (unless P = NP).

3. **Space optimization technique:** Always remember to iterate backward in 1D DP to avoid using the same element twice.

4. **Base cases are crucial:** In DP, always initialize dp[0] = true (empty subset achieves sum 0).

5. **Pseudo-polynomial definition:** Know that when T is polynomial in input size, the algorithm is polynomial; otherwise, it's exponential in input size.

6. **Connection to 0/1 Knapsack:** Subset Sum is a special case of 0/1 Knapsack where all values equal weights.

7. **Difference from Partition Problem:** While similar, Partition Problem asks if equal-sum partition exists (target = sum/2), a special case of Subset Sum.

8. **Approximation schemes:** For large instances, FPTAS (Fully Polynomial Time Approximation Scheme) exists for the optimization version.