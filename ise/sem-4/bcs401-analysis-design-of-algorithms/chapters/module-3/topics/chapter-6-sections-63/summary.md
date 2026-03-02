# **Chapter 6 (Sections 6.3) - Analysis & Design of Algorithms**

### 6.3 Analysis of Algorithms

- **Big O Notation**:
  - Definition: Upper bound on the time/space complexity of an algorithm
  - Examples: O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n)
- **Upper Bound**:
  - Definition: Tightest upper bound on the time/space complexity of an algorithm
  - Example: O(n) is an upper bound on the time complexity of a binary search
- **Lower Bound**:
  - Definition: Loosest lower bound on the time/space complexity of an algorithm
  - Example: Ω(n) is a lower bound on the time complexity of a binary search
- **Big Omega Notation**:
  - Definition: Tightest lower bound on the time/space complexity of an algorithm
  - Example: Ω(n) is a lower bound on the time complexity of a binary search
- **Big Theta Notation**:
  - Definition: Both upper and lower bounds on the time/space complexity of an algorithm
  - Example: Θ(n) is a tight bound on the time complexity of a binary search

### 6.3.1 Time Complexity Analysis

- **Constant Time Complexity**:
  - Definition: O(1) time complexity
  - Example: Accessing an element in an array by its index
- **Logarithmic Time Complexity**:
  - Definition: O(log n) time complexity
  - Example: Binary search in an array
- **Linear Time Complexity**:
  - Definition: O(n) time complexity
  - Example: Finding an element in an array using linear search
- **Quadratic Time Complexity**:
  - Definition: O(n^2) time complexity
  - Example: Bubble sort algorithm
- **Exponential Time Complexity**:
  - Definition: O(2^n) time complexity
  - Example: Recursive algorithms with no optimization

### 6.3.2 Space Complexity Analysis

- **Constant Space Complexity**:
  - Definition: O(1) space complexity
  - Example: Arrays and strings
- **Linear Space Complexity**:
  - Definition: O(n) space complexity
  - Example: Dynamic arrays and linked lists
- **Quadratic Space Complexity**:
  - Definition: O(n^2) space complexity
  - Example: Matrix multiplication algorithms

### 6.3.3 Comparison of Algorithms

- **Comparison of Time Complexities**:
  - Definition: Comparing the time complexities of two algorithms
  - Example: Comparing binary search and linear search
- **Comparison of Space Complexities**:
  - Definition: Comparing the space complexities of two algorithms
  - Example: Comparing binary search and linear search

### Important Formulas and Definitions

- **Average-Case Time Complexity**:
  - Definition: The average time complexity of an algorithm over all possible inputs
  - Formula: T(n) = ∑(P(n)/Q(n)) \* t(n)
- **Worst-Case Time Complexity**:
  - Definition: The maximum time complexity of an algorithm over all possible inputs
  - Formula: T(n) = max(T(n-1) + t(n))

### Theorems

- **Master Theorem**:
  - Definition: A theorem for solving recurrence relations
  - Formula: T(n) = aT(n/b) + f(n)
  - Example: Solving recurrence relations using the Master Theorem
- **Catalan's Conjecture**:
  - Definition: A conjecture about the number of binary trees with n nodes
  - Formula: T(n) = n! / (n/2)! \* (1/2)^(n/2)
