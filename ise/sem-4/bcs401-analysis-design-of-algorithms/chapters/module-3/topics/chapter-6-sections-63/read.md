# **Chapter 6: Analysis and Design of Algorithms**

## **Module: TRANSFORM-AND-CONQUER: Balanced Search Trees, Heaps and Heapsort**

### 6.3 Analysis of Algorithms

#### Introduction

Analysis of algorithms is the process of measuring the complexity of an algorithm, which is a mathematical function that describes the amount of computational resources required to solve a problem. The complexity of an algorithm can be measured in terms of time, space, or both.

#### Time Complexity

Time complexity is a measure of the amount of time an algorithm takes to complete as a function of the input size. It is usually expressed as a function of the input size n.

- **Big O Notation**: Big O notation is used to describe the upper bound of an algorithm's time complexity. It gives an estimate of the worst-case scenario.
- **Upper Bound**: The upper bound is an estimate of the maximum amount of time an algorithm takes to complete.

#### Space Complexity

Space complexity is a measure of the amount of memory an algorithm requires as a function of the input size.

- **Big O Notation**: Big O notation is used to describe the upper bound of an algorithm's space complexity.

#### Measuring Time and Space Complexity

To measure time and space complexity, we use the following formulas:

- **Time Complexity**: T(n) = Upper bound of time taken by algorithm
- **Space Complexity**: S(n) = Upper bound of space required by algorithm

#### Example

Suppose we have an algorithm that sorts an array of n elements using bubble sort.

- **Time Complexity**: T(n) = O(n^2)
- **Space Complexity**: S(n) = O(1)

#### Key Concepts

- **Big O Notation**: Upper bound of time and space complexity
- **Upper Bound**: Estimate of the maximum amount of time or space required
- **Time Complexity**: Measure of time taken by algorithm as a function of input size
- **Space Complexity**: Measure of space required by algorithm as a function of input size

### 6.3.1 Divide and Conquer

Divide and Conquer is a method of solving problems by dividing them into smaller subproblems, solving each subproblem, and combining the solutions to solve the original problem.

- **Example**: Merge sort
- **Example**: Binary search

#### Key Concepts

- **Divide**: Divide the problem into smaller subproblems
- **Conquer**: Solve each subproblem recursively
- **Combine**: Combine the solutions to solve the original problem

### 6.3.2 Dynamic Programming

Dynamic programming is a method of solving problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation.

- **Example**: Fibonacci sequence
- **Example**: Longest common subsequence

#### Key Concepts

- **Memoization**: Store the solutions to subproblems to avoid redundant computation
- **Dynamic Programming**: Break down the problem into smaller subproblems, solve each subproblem only once, and store the solutions

### 6.3.3 Greedy Algorithms

Greedy algorithms are a type of algorithm that makes the locally optimal choice at each step with the hope of finding a global optimum.

- **Example**: Huffman coding
- **Example**: Activity selection problem

#### Key Concepts

- **Greedy**: Make the locally optimal choice at each step
- **Optimality**: The algorithm may not always find the global optimum

### 6.3.4 Backtracking

Backtracking is a method of solving problems by exploring all possible solutions and returning the first solution that satisfies the constraints.

- **Example**: N-Queens problem
- **Example**: Sudoku

#### Key Concepts

- **Backtracking**: Explore all possible solutions and return the first solution that satisfies the constraints
- **Constraint**: The algorithm must satisfy certain constraints to find a solution

### 6.3.5 Recursion

Recursion is a method of solving problems by breaking them down into smaller subproblems, solving each subproblem recursively, and combining the solutions to solve the original problem.

- **Example**: Factorial
- **Example**: Fibonacci sequence

#### Key Concepts

- **Recursion**: Break down the problem into smaller subproblems, solve each subproblem recursively, and combine the solutions
- **Base Case**: A stopping condition that stops the recursion

#### Study Questions

1.  What is the difference between time complexity and space complexity?
2.  What is big O notation, and how is it used to describe the upper bound of an algorithm's time complexity?
3.  What is divide and conquer, and how is it used to solve problems?
4.  What is dynamic programming, and how is it used to solve problems?
5.  What is greedy algorithms, and how is it used to solve problems?
