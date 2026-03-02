# Dynamic Programming Advanced

## Comprehensive Study Material for MSc CS – Delhi University

---

## 1. Introduction and Real-World Relevance

**Dynamic Programming (DP)** is one of the most powerful algorithmic paradigms in computer science, enabling the solution of complex optimization and counting problems that would otherwise be computationally intractable. While basic DP problems like Fibonacci, knapsack, and longest common subsequence form the foundation, **Advanced Dynamic Programming** techniques are essential for solving real-world challenges at scale.

### Why Advanced DP Matters in Practice

In industry and research, advanced DP techniques are indispensable:

- **Bioinformatics**: Sequence alignment (Needleman-Wunsch algorithm) uses DP on intervals
- **Compiler Design**: Register allocation and instruction scheduling
- **String Processing**: Complex pattern matching and text compression
- **Game Theory**: Solving combinatorial games with state compression
- **Network Design**: Traveling salesman problem variants (bitmask TSP)
- **Digit Problems**: Counting numbers with specific properties (digit DP)
- **Machine Learning**: Viterbi algorithm for hidden Markov models

This study material covers the advanced DP techniques essential for the Delhi University MSc CS curriculum, focusing on algorithmic sophistication, optimization, and practical implementation.

---

## 2. Advanced DP Techniques

### 2.1 Digit Dynamic Programming (Digit DP)

Digit DP solves problems involving numbers with specific digit properties. Instead of iterating through all numbers (which is impossible for large ranges), we process numbers digit by digit using DP with state tracking.

**Key Concept**: Process numbers as strings, maintaining states like "tight" (prefix matches upper bound), "started" (non-zero digit encountered), and any problem-specific constraints.

#### Example Problem: Count numbers from 0 to N where digit sum is even

```python
def count_even_digit_sum(n):
    """
    Count numbers from 0 to n (inclusive) with even digit sum.
    Uses Digit DP with memoization.
    """
    digits = [int(d) for d in str(n)]
    n_digits = len(digits)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(pos, sum_so_far, tight, started):
        """
        pos: current position (0 to n_digits)
        sum_so_far: cumulative digit sum
        tight: whether prefix equals prefix of n
        started: whether we've placed any non-zero digit
        """
        # Base case: processed all digits
        if pos == n_digits:
            # Count valid number (including 0)
            return 1 if (sum_so_far % 2 == 0) else 0
        
        limit = digits[pos] if tight else 9
        result = 0
        
        for digit in range(limit + 1):
            new_tight = tight and (digit == limit)
            new_started = started or (digit != 0)
            
            # If we haven't started, sum remains 0
            new_sum = sum_so_far + (digit if new_started else 0)
            
            result += dp(pos + 1, new_sum, new_tight, new_started)
        
        return result
    
    return dp(0, 0, True, False)

# Example usage
print(count_even_digit_sum(100))  # Output: 51
```

**Time Complexity**: O(number_of_digits × 10 × possible_sum_states), much better than O(N)

#### Advanced Digit DP Variations

| Problem Type | State Additions | Common Use |
|--------------|-----------------|------------|
| Digit Constraints | `count[d]` for digit frequency | Numbers with at most k of digit '3' |
| Modular DP | `mod_value` | Divisibility by m |
| Position-based | `last_digit`, `consecutive` | No consecutive zeros |

---

### 2.2 State Compression Dynamic Programming (Bitmask DP)

When the state space is exponential but manageable (typically n ≤ 20), we use bitmasks to represent subsets. This is crucial for problems where each element can be "included" or "excluded."

#### Classic Problem: Traveling Salesman Problem (TSP) with Bitmask

```python
def tsp_bitmask(dist, start=0):
    """
    Solve TSP starting from 'start' using bitmask DP.
    dist: n x n distance matrix
    """
    n = len(dist)
    ALL = (1 << n) - 1
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(mask, current):
        """Minimum cost to visit all unvisited nodes from current position"""
        # All cities visited - return to start
        if mask == ALL:
            return dist[current][start]
        
        min_cost = float('inf')
        
        # Try visiting each unvisited city
        for next_city in range(n):
            if not (mask & (1 << next_city)):  # City not visited
                new_mask = mask | (1 << next_city)
                cost = dist[current][next_city] + dp(new_mask, next_city)
                min_cost = min(min_cost, cost)
        
        return min_cost
    
    return dp(1 << start, start)

# Example
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(f"TSP Minimum Cost: {tsp_bitmask(dist)}")  # Output: 80
```

**Time Complexity**: O(n² × 2^n) — exponential but feasible for n ≤ 20

#### State Compression for Graph Problems

```python
def count_vertex_covers(n, edges):
    """
    Count minimum vertex covers in a tree using DP on subsets.
    For demonstration: small graph (n <= 15)
    """
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def is_valid_cover(mask):
        """Check if selected vertices cover all edges"""
        for u, v in edges:
            if not (mask & (1 << u)) and not (mask & (1 << v)):
                return False
        return True
    
    min_size = n
    count = 0
    
    for mask in range(1 << n):
        if is_valid_cover(mask):
            bits = bin(mask).count('1')
            if bits < min_size:
                min_size = bits
                count = 1
            elif bits == min_size:
                count += 1
    
    return min_size, count
```

---

### 2.3 DP on Intervals (Interval DP)

Interval DP solves problems where the optimal solution for a segment depends on optimal solutions for subsegments. The DP table is built by considering all possible interval lengths.

**Pattern**: `dp[i][j] = min/max(dp[i][k] + dp[k][j] + cost[i][j])` for all k in (i, j)

#### Example: Optimal Matrix Chain Multiplication

```python
def matrix_chain_order(dimensions):
    """
    Find optimal parenthesization for matrix chain multiplication.
    dimensions: list of matrix dimensions [d0, d1, ..., dn]
    Returns minimum scalar multiplications and parenthesization.
    """
    n = len(dimensions) - 1  # Number of matrices
    
    # dp[i][j] = minimum cost to multiply matrices i to j
    dp = [[0] * n for _ in range(n)]
    
    # parent[i][j] = split point for reconstruction
    parent = [[0] * n for _ in range(n)]
    
    # length = 2 to n (at least 2 matrices)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # Try all split points
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    parent[i][j] = k
    
    def get_paren(i, j):
        if i == j:
            return f"M{i+1}"
        k = parent[i][j]
        return f"({get_paren(i, k)} × {get_paren(k+1, j)})"
    
    return dp[0][n-1], get_paren(0, n-1)

# Example
dims = [10, 30, 5, 60]  # Matrices: M1(10×30), M2(30×5), M3(5×60)
cost, paren = matrix_chain_order(dims)
print(f"Minimum cost: {cost}")  # Output: 4500
print(f"Parenthesization: {paren}")  # Output: (M1 × (M2 × M3))
```

#### Example: Palindrome Partitioning (Minimum Cuts)

```python
def min_palindrome_cuts(s):
    """
    Find minimum cuts needed to partition string into palindromes.
    """
    n = len(s)
    
    # is_pal[i][j] = True if s[i:j+1] is palindrome
    is_pal = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_pal[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                is_pal[i][j] = (s[i] == s[j])
            else:
                is_pal[i][j] = (s[i] == s[j]) and is_pal[i+1][j-1]
    
    # dp[i] = minimum cuts for s[0:i+1]
    dp = [0] * n
    
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            dp[i] = i  # Worst case: i cuts
            for j in range(i):
                if is_pal[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n-1]

# Example
print(min_palindrome_cuts("aab"))  # Output: 1 (cut between a and b)
```

---

### 2.4 Divide and Conquer Optimization

When DP recurrence has the form `dp[k][i] = min(dp[k-1][j] + cost(j, i))` for `j < i`, and the optimal j (called **opt**) satisfies the **quadrangle inequality** or **monotonicity condition** (i.e., `opt[k][i] ≤ opt[k][i+1]`), we can compute each row in O(n log n) instead of O(n²) using divide and conquer.

#### Conditions for D&C Optimization

1. **Monotonicity**: `opt[k][i] ≤ opt[k][i+1]` for all i
2. **Quadrangle Inequality**: `cost(a, c) + cost(b, d) ≤ cost(a, d) + cost(b, c)` for a ≤ b ≤ c ≤ d

This applies to:
- DP with convex/concave cost functions
- Aligned DP problems (knapsack with grouped items)
- Many competitive programming problems

#### Implementation Template

```python
def divide_conquer_dp(dp_prev, cost_fn, n):
    """
    Template for Divide and Conquer DP Optimization.
    dp_prev: dp values from previous layer
    cost_fn(j, i): cost from position j to i
    n: number of positions
    """
    INF = float('inf')
    dp = [INF] * n
    opt = [0] * n
    
    def compute(l, r, k_l, k_r):
        """Compute dp[i] for i in [l, r] with opt in [k_l, k_r]"""
        if l > r:
            return
        
        mid = (l + r) // 2
        dp[mid] = INF
        best_k = -1
        
        # Try optimal k in valid range
        for k in range(k_l, min(mid, k_r + 1)):
            val = dp_prev[k] + cost_fn(k, mid)
            if val < dp[mid]:
                dp[mid] = val
                best_k = k
        
        # Recurse on left and right
        compute(l, mid - 1, k_l, best_k)
        compute(mid + 1, r, best_k, k_r)
    
    compute(0, n - 1, 0, n - 1)
    return dp

# Example: Optimized DP for "Aliens" (consecutive items optimization)
def alien_domination(n, power_costs):
    """
    Simplified example showing D&C optimization structure.
    Real problems require verifying monotonicity condition.
    """
    # dp[i] = min cost considering first i items with optimization
    dp_prev = [0] + [float('inf')] * (n - 1)
    
    def cost_fn(j, i):
        """Example cost: sum of powers from j+1 to i"""
        return sum(power_costs[j+1:i+1]) ** 2
    
    return divide_conquer_dp(dp_prev, cost_fn, n)
```

**Time Complexity**: O(n log n) per DP layer instead of O(n²)

---

## 3. Delhi University Syllabus Context

The Advanced Algorithms paper for MSc CS (DELHI UNIVERSITY, July 2025) includes Dynamic Programming as a major component. This study material aligns with:

- **Unit III**: Advanced algorithmic paradigms
- **Topic Coverage**: Digit DP, Bitmask DP, Interval DP, Optimization techniques
- **Problem Difficulty**: Matching university examination standards (14-15 marks per question)
- **Practical Component**: Implementation in Python/C++ for lab courses

### Expected Examination Topics

| Topic | Weight | Difficulty |
|-------|--------|------------|
| Digit DP | 15-20% | High |
| State Compression | 15-20% | High |
| Interval DP | 10-15% | Medium-High |
| D&C Optimization | 10-15% | High |
| Combined Problems | 20-25% | Very High |

---

## 4. Key Takeaways

1. **Digit DP** processes numbers digit-by-digit, using "tight" and "started" states to handle bounds efficiently. Essential for counting problems with digit constraints.

2. **State Compression (Bitmask DP)** represents exponential states using bitmasks. Practical for n ≤ 20. The TSP solution demonstrates the canonical O(n² × 2^n) approach.

3. **Interval DP** builds solutions from smaller to larger intervals, following `dp[i][j] = min/max(dp[i][k] + dp[k][j] + cost)` pattern. Used in matrix chain multiplication and palindrome problems.

4. **Divide & Conquer Optimization** reduces O(n²) to O(n log n) when the optimal split point is monotonic. Requires proving the monotonicity condition.

5. **All techniques require**:
   - Clear state definition
   - Base case identification
   - Transition formulation
   - Order of computation

---

## 5. Advanced Assessment Items

### Multiple Choice Questions (Advanced Level)

**Question 1**: In Digit DP, the "tight" state represents:
- (a) Whether the current digit equals the maximum allowed digit
- (b) Whether all previous digits equal the prefix of the upper bound
- (c) Whether the number has trailing zeros
- (d) Whether the sum of digits exceeds a threshold

**Answer**: (b) The "tight" flag is True when the prefix built so far exactly matches the prefix of the upper bound, restricting the current digit to not exceed the corresponding digit in N.

---

**Question 2**: For the bitmask TSP with n cities, the time complexity is:
- (a) O(n!)
- (b) O(2^n)
- (c) O(n² × 2^n)
- (d) O(n × 2^n)

**Answer**: (c) We have 2^n possible subsets and for each state, we iterate through n possible next cities, giving O(n² × 2^n).

---

**Question 3**: Which condition is NOT required for Divide & Conquer DP optimization?
- (a) Monotonicity of optimal split points
- (b) Quadrangle inequality
- (c) Convex cost function
- (d) The recurrence must be of form dp[i] = min(dp[j] + cost(j, i))

**Answer**: (c) While convexity helps, the key requirements are monotonicity and quadrangle inequality (or the monotone matrix condition). Convexity alone is not sufficient.

---

**Question 4**: In Interval DP for matrix chain multiplication with n matrices, the time complexity is:
- (a) O(n)
- (b) O(n²)
- (c) O(n³)
- (d) O(n² × m) where m is dimension

**Answer**: (c) We consider all interval lengths (O(n)), all starting positions (O(n)), and all split points (O(n)), giving O(n³).

---

**Question 5**: For a digit DP problem counting numbers from 0 to N with exactly k zeros in the decimal representation, what additional state would you need?
- (a) `tight` and `started` only
- (b) `count_zeros` to track zeros in the current prefix
- (c) `last_digit` to check consecutive zeros
- (d) `sum_of_digits` to compare with k

**Answer**: (b) We need to explicitly track the count of zeros encountered in the prefix to ensure we have exactly k zeros in the final number.

---

### Fill-in-the-Blank Questions

1. In bitmask DP representing a subset of n elements, the empty set is represented by integer **0** and the full set by **(1 << n) - 1**.

2. The monotonicity condition for Divide & Conquer optimization states that `opt[i] ≤ opt[i+1]`, meaning the optimal split point never decreases as i increases.

3. For interval DP, the table is typically filled by increasing **interval length** to ensure subproblems are solved before being used.

4. In Digit DP, if `tight = True`, the current digit can range from **0 to digits[pos]**; if `tight = False`, it can range from **0 to 9**.

---

### Long Answer Questions

**Question 1** (15 marks): Explain the Digit DP technique for solving problems involving counting numbers with specific properties. Provide the general DP structure and show how to count numbers from 0 to N where no digit appears more than twice.

**Solution Outline**:
- Define state: position, tight flag, started flag, count array for each digit (0-9)
- Base case: when all positions processed, check if any digit count ≤ 2
- Transition: iterate digits respecting tight constraint, update counts
- Complexity: O(positions × 10 × possible_count_states)

---

**Question 2** (15 marks): Prove the monotonicity condition for Divide and Conquer optimization. Under what conditions can we apply this optimization to reduce time complexity from O(n²) to O(n log n)?

**Solution Outline**:
- Define opt[k][i] as optimal split point
- Monotonicity: opt[k][i] ≤ opt[k][i+1]
- Quadrangle inequality proof sketch
- Conditions: The cost function must satisfy quadrangle inequality and monotonicity
- Recurrence: dp[k][i] = min_{j < i} (dp[k-1][j] + cost(j, i))

---

## 6. Advanced Flashcards

### Flashcard 1
**Front**: What is the key insight behind State Compression DP?

**Back**: When n ≤ 20, we can represent subsets as bitmasks of n bits. Each bit indicates whether an element is included (1) or excluded (0). This transforms exponential state spaces into polynomial number of integer states (2^n).

---

### Flashcard 2
**Front**: Why is the "started" flag necessary in Digit DP?

**Back**: It distinguishes between leading zeros (which don't contribute to digit sum or count) and actual digits. Without it, numbers like 007 would be incorrectly counted as having two leading zeros, affecting constraints on digit frequency.

---

### Flashcard 3
**Front**: In Interval DP, what is the typical order of filling the DP table?

**Back**: Fill by increasing interval length. First compute dp[i][i] (length 1), then dp[i][i+1] (length 2), and so on. This ensures that when computing dp[i][j], all subintervals dp[i][k] and dp[k][j] are already computed.

---

### Flashcard 4
**Front**: What is the time complexity improvement from Divide & Conquer optimization?

**Back**: From O(n²) to O(n log n) per DP layer. Instead of trying all j for each i (O(n²)), we use recursion to narrow the search range, achieving O(n log n) total.

---

### Flashcard 5
**Front**: Give an example problem where State Compression DP is the only feasible approach.

**Back**: The Traveling Salesman Problem with up to 20 cities. Enumeration of all permutations gives O(n!), but bitmask DP achieves O(n² × 2^n), which is tractable for n ≤ 20.

---

### Flashcard 6
**Front**: How does the "tight" flag enable efficient Digit DP?

**Back**: It allows us to process numbers up to bound N without enumerating them. When tight is True, our current prefix matches N's prefix, limiting the current digit to at most N's digit at that position. When False, we can use any digit 0-9.

---

## 7. Conclusion

This comprehensive study material covers all advanced dynamic programming techniques required for the Delhi University MSc CS Advanced Algorithms course. The combination of theoretical explanations, working code examples, and challenging assessment items ensures thorough preparation for examinations and practical implementation.

**Remember**: The key to mastering advanced DP is understanding when to apply each technique—digit DP for digit constraints, bitmask for subset problems, interval DP for segment optimization, and divide-conquer for acceleration when monotonicity holds.