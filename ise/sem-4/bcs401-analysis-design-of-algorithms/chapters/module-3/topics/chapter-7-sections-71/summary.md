# **Chapter 7 (Sections 7.1) Revision Notes: Analysis & Design of Algorithms**

## **Key Concepts**

- **Analysis of Algorithms**
  - Definition: The process of measuring the performance or efficiency of an algorithm
  - Important formulas:
    - Big O notation (O(n)): Upper bound on the number of operations
    - Big Ω notation (Ω(n)): Lower bound on the number of operations
    - Big θ notation (θ(n)): Tighter bound on the number of operations
- **Design of Algorithms**
  - Definition: The process of creating an efficient algorithm
  - Important techniques:
    - Divide and Conquer
    - Dynamic Programming
    - Greedy Algorithm

## **The Big-Theta Notation**

- Definition: A tight bound on the number of operations
- Formula: θ(f(n)) = lim(n→∞) (g(n)/f(n)) = 0
- Example: θ(n log n) = θ(n^2)

## **Time Complexity**

- **Constants**: O(1), O(log n), O(n), O(n log n), O(n^2)
- **Logarithmic Time Complexity**:
  - O(log n) for binary search
  - O(log log n) for heap operations
- **Linear Time Complexity**:
  - O(n) for array operations
- **Quadratic Time Complexity**:
  - O(n^2) for bubble sort

## **Space Complexity**

- **Constants**: O(1), O(log n), O(n), O(n log n), O(n^2)
- **Logarithmic Space Complexity**:
  - O(log n) for recursive functions
- **Linear Space Complexity**:
  - O(n) for array operations

## **Important Theorems**

- **Master Theorem**: Solves recurrence relations of the form T(n) = aT(n/b) + f(n)
- **Recurrence Relation Solving**: Solves recurrence relations using iteration and recursion

## **Key Terms**

- **Divide and Conquer**: A problem-solving strategy that breaks down a problem into smaller sub-problems
- **Dynamic Programming**: A problem-solving strategy that stores the solutions to sub-problems to avoid redundant computation
- **Greedy Algorithm**: A problem-solving strategy that makes the locally optimal choice at each step, hoping to find a global optimum solution
