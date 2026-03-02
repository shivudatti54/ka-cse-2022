# Dynamic Programming Advanced - Summary

**Introduction**
Dynamic Programming (DP) is a cornerstone technique in the Advanced Algorithms syllabus for MSc CS at Delhi University (July 2025). It solves complex problems by breaking them into overlapping subproblems and combining optimal solutions. DP is crucial for optimization, counting, and decision problems, making it a high-yield topic for exams.

**Key Concepts**
- **Optimal Substructure**: A problem exhibits optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems.
- **Overlapping Subproblems**: Subproblems are reused multiple times, necessitating efficient computation via caching.
- **Memoization vs Tabulation**: Top-down approach (recursive with memoization) vs bottom-up approach (iterative table-building). Choose based on problem structure.
- **State Transition Equations**: Define recurrence relations to compute DP states (e.g., `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])` for knapsack).
- **Space Optimization**: Reduce space complexity from O(n²) to O(n) or O(1) by storing only necessary previous states (e.g., rolling arrays).
- **Types of DP Problems**:
  - *Optimization*: Maximize or minimize a value (e.g., 0/1 knapsack, longest common subsequence).
  - *Counting*: Count the number of ways (e.g., climbing stairs, coin change).
  - *Decision*: Determine feasibility (e.g., subset sum, palindrome partitioning).
- **Common DP Patterns**:
  - *Linear DP*: Single dimension (e.g., fibonacci, longest increasing subsequence).
  - *Multi-dimensional DP*: Two or more dimensions (e.g., matrix chain multiplication, edit distance).
  - *Partition DP*: Divide into subsets (e.g., partition equal subset sum).
  - *Tree DP*: On tree structures (e.g., binary tree max path sum).
  - *Bitmask DP*: Using bitmasks for state representation (e.g., traveling salesman problem).
- **Advanced Optimization Techniques**:
  - *Divide and Conquer Optimization*: For DP with convexity (e.g., Knuth optimization in optimal binary search tree).
  - *Monotonic Queue Optimization*: For sliding window minimum/maximum in DP (e.g., maximum sum subarray of size k).
  - *Convex Hull Optimization*: For linear recurrences with divide and conquer (e.g., DP with slopes).
- **Syllabus-Centric Examples** (per Delhi University MSc CS Advanced Algorithms):
  - 0/1 Knapsack (weight-value optimization)
  - Longest Common Subsequence (LCS)
  - Matrix Chain Multiplication (parenthesis optimization)
  - Edit Distance (string alignment)
  - Optimal Binary Search Tree
  - All-Pairs Shortest Path (Floyd-Warshall algorithm)
  - Single-Source Shortest Path with Negative Weights (Bellman-Ford)
- **Complexity Analysis**: Typical time complexity O(n²) to O(n³); space O(n) to O(n²). Optimizations like space reduction and advanced techniques improve efficiency.

**Conclusion**
Dynamic Programming is vital for solving real-world optimization problems. Mastery of state design, recurrence relations, and advanced optimizations (like monotonic queues) is essential for exam success and algorithmic problem-solving in professional settings.