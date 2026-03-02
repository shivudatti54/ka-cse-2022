# Chapter 8: Dynamic Programming - Analysis and Design of Algorithms

### 8.1: Introduction to Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing the results to avoid redundant computation. This technique is particularly useful for problems that have overlapping subproblems or that can be decomposed into smaller subproblems.

#### History

The concept of dynamic programming was first introduced by the American mathematician Richard Bellman in the 1950s. Bellman was working at the RAND Corporation, a nonprofit research organization, where he was trying to develop a method for solving complex problems. He realized that many problems could be solved by breaking them down into smaller subproblems and solving each subproblem only once. This approach was later formalized and popularized by other mathematicians and computer scientists.

#### Key Concepts

Before we dive into the details of dynamic programming, let's define some key concepts:

- **Optimal Substructure**: A problem has optimal substructure if the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
- **Overlapping Subproblems**: A problem has overlapping subproblems if the subproblems are not independent of each other, i.e., solving one subproblem can provide information that can be used to solve other subproblems.

#### Types of Dynamic Programming Problems

Dynamic programming problems can be classified into three main types:

1.  **Zero-One Knapsack Problem**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
2.  **Longest Common Subsequence Problem**: Given two sequences, find the length of their longest common subsequence.
3.  **Fibonacci Series**: Given a positive integer n, compute the nth Fibonacci number, where each Fibonacci number is the sum of the two preceding ones.

### 8.2: The Knapsack Problem

The 0/1 Knapsack Problem is a classic example of a dynamic programming problem. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

#### Formulation

Let `n` be the number of items, `W` be the maximum weight capacity of the knapsack, and `v_i` and `w_i` be the value and weight of item `i`, respectively. We need to find the optimal solution to the following problem:

`maximize` `Z = v_1 * x_1 + v_2 * x_2 + ... + v_n * x_n`

subject to:

`x_i * w_i <= W`

`x_i >= 0`

`i = 1, 2, ..., n`

#### Dynamic Programming Solution

We can solve the 0/1 Knapsack Problem using dynamic programming by breaking it down into smaller subproblems. We create a 2D table `dp` of size `(n+1) x (W+1)`, where `dp[i][j]` represents the maximum value that can be obtained using the first `i` items and a weight capacity of `j`.

```markdown
|     | 0                                  | 1                                           | 2                                                     | ... | W                                                          |
| --- | ---------------------------------- | ------------------------------------------- | ----------------------------------------------------- | --- | ---------------------------------------------------------- |
| 0   | dp[0][0] = 0                       | dp[0][1] = 0                                | dp[0][2] = 0                                          | ... | dp[0][W] = 0                                               |
| 1   | dp[1][0] = v_1                     | dp[1][1] = v_1 + v_2                        | dp[1][2] = max(v_1, v_2)                              | ... | dp[1][W] = max(v_1, v_2, ..., v_W)                         |
| 2   | dp[2][0] = max(v_1, v_2)           | dp[2][1] = max(v_1, v_2, v_3)               | dp[2][2] = v_3                                        | ... | dp[2][W] = max(v_1, v_2, ..., v_W)                         |
| ... | ...                                | ...                                         | ...                                                   | ... | ...                                                        |
| n   | dp[n][0] = max(v_1, v_2, ..., v_n) | dp[n][1] = max(v*1, v_2, ..., v_n, v*{n+1}) | dp[n][2] = max(v*1, v_2, ..., v_n, v*{n+1}, v\_{n+2}) | ... | dp[n][W] = max(v*1, v_2, ..., v_n, v*{n+1}, ..., v\_{n+W}) |
```

We fill up the table `dp` using the following recurrence relation:

`dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i] + v_i)`

The final answer is stored in `dp[n][W]`.

#### Example

Suppose we have three items with values and weights as follows:

| Item | Value | Weight |
| ---- | ----- | ------ |
| 1    | 60    | 10     |
| 2    | 100   | 20     |
| 3    | 120   | 30     |

We need to find the maximum value that can be obtained using these items and a weight capacity of 50.

```markdown
|     | 0              | 10              | 20              | 30              | 40              | 50              |
| --- | -------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| 0   | dp[0][0] = 0   | dp[0][10] = 0   | dp[0][20] = 0   | dp[0][30] = 0   | dp[0][40] = 0   | dp[0][50] = 0   |
| 1   | dp[1][0] = 60  | dp[1][10] = 60  | dp[1][20] = 60  | dp[1][30] = 60  | dp[1][40] = 80  | dp[1][50] = 80  |
| 2   | dp[2][0] = 120 | dp[2][10] = 120 | dp[2][20] = 120 | dp[2][30] = 180 | dp[2][40] = 180 | dp[2][50] = 180 |
| 3   | dp[3][0] = 180 | dp[3][10] = 180 | dp[3][20] = 180 | dp[3][30] = 240 | dp[3][40] = 240 | dp[3][50] = 240 |
```

The maximum value that can be obtained is 240.

### 8.3: Longest Common Subsequence Problem

The Longest Common Subsequence (LCS) Problem is a dynamic programming problem that involves finding the longest common subsequence between two sequences.

#### Formulation

Given two sequences `X = x_1, x_2, ..., x_m` and `Y = y_1, y_2, ..., y_n`, find the longest common subsequence `LCS = l_1, l_2, ..., l_k`.

#### Dynamic Programming Solution

We can solve the LCS Problem using dynamic programming by creating a 2D table `dp` of size `(m+1) x (n+1)`, where `dp[i][j]` represents the length of the LCS between the first `i` characters of `X` and the first `j` characters of `Y`.

```markdown
|     | 0            | 1            | 2            | ... | n            |
| --- | ------------ | ------------ | ------------ | --- | ------------ |
| 0   | dp[0][0] = 0 | dp[0][1] = 0 | dp[0][2] = 0 | ... | dp[0][n] = 0 |
| 1   | dp[1][0] = 0 | dp[1][1] = 1 | dp[1][2] = 0 | ... | dp[1][n] = 0 |
| 2   | dp[2][0] = 0 | dp[2][1] = 0 | dp[2][2] = 2 | ... | dp[2][n] = 0 |
| ... | ...          | ...          | ...          | ... | ...          |
| m   | dp[m][0] = 0 | dp[m][1] = 0 | dp[m][2] = 0 | ... | dp[m][n] = 0 |
```

We fill up the table `dp` using the following recurrence relation:

`dp[i][j] = max(dp[i-1][j-1] + (x_i == y_j), dp[i-1][j])`

The final answer is stored in `dp[m][n]`.

#### Example

Suppose we have two sequences `X = "AGGTAB"` and `Y = "GXTXAYB"`.

```markdown
|     | 0            | 1            | 2            | ...          | 7            |
| --- | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 0   | dp[0][0] = 0 | dp[0][1] = 0 | dp[0][2] = 0 | ...          | dp[0][7] = 0 |
| 1   | dp[1][0] = 0 | dp[1][1] = 1 | dp[1][2] = 0 | ...          | dp[1][7] = 0 |
| 2   | dp[2][0] = 0 | dp[2][1] = 0 | dp[2][2] = 2 | ...          | dp[2][7] = 0 |
| 3   | dp[3][0] = 0 | dp[3][1] = 0 | dp[3][2] = 0 | ...          | dp[3][7] = 0 |
| 4   | dp[4][0] = 0 | dp[4][1] = 0 | dp[4][2] = 0 | dp[4][3] = 3 | ...          | dp[4][7] = 3 |
| 5   | dp[5][0] = 0 | dp[5][1] = 0 | dp[5][2] = 0 | dp[5][3] = 0 | dp[5][4] = 4 | ...          | dp[5][7] = 4 |
| 6   | dp[6][0] = 0 | dp[6][1] = 0 | dp[6][2] = 0 | dp[6][3] = 0 | dp[6][4] = 0 | dp[6][5] = 5 | ...          | dp[6][7] = 5 |
| 7   | dp[7][0] = 0 | dp[7][1] = 0 | dp[7][2] = 0 | dp[7][3] = 0 | dp[7][4] = 0 | dp[7][5] = 0 | dp[7][6] = 6 | ...          | dp[7][7] = 6 |
```

The longest common subsequence is "GTAB".

### 8.4: Fibonacci Series

The Fibonacci Series is a classic example of a dynamic programming problem. Given a positive integer `n`, compute the `n`th Fibonacci number, where each Fibonacci number is the sum of the two preceding ones.

#### Formulation

The Fibonacci Series can be defined recursively as:

`fib(n) = fib(n-1) + fib(n-2)`

The base cases are:

`fib(0) = 0`

`fib(1) = 1`

#### Dynamic Programming Solution

We can solve the Fibonacci Series using dynamic programming by creating a 1D table `dp` of size `n+1`, where `dp[i]` represents the `i`th Fibonacci number.

```markdown
|     | 0         | 1         | 2         | ... | n              |
| --- | --------- | --------- | --------- | --- | -------------- |
| 0   | dp[0] = 0 |           |           | ... |                |
| 1   | dp[1] = 1 |           |           | ... |                |
| 2   | dp[2] = 1 | dp[2] = 1 |           | ... |                |
| ... | ...       | ...       | ...       | ... | ...            |
| n   | dp[n] = ? | dp[n] = ? | dp[n] = ? | ... | dp[n] = fib(n) |
```

We fill up the table `dp` using the following recurrence relation:

`dp[i] = dp[i-1] + dp[i-2]`

The final answer is stored in `dp[n]`.

#### Example

Suppose we need to compute the 5th Fibonacci number.

```markdown
|     | 0         | 1         | 2         | 3         | 4         | 5   |
| --- | --------- | --------- | --------- | --------- | --------- | --- |
| 0   | dp[0] = 0 |           |           |           |           |     |
| 1   | dp[1] = 1 |           |           |           |           |     |
| 2   | dp[2] = 1 | dp[2] = 1 |           |           |           |     |
| 3   | dp[3] = 2 | dp[3] = 1 | dp[3] = 2 |           |           |     |
| 4   | dp[4] = 3 | dp[4] = 2 | dp[4] = 1 | dp[4] = 3 |           |     |
| 5   | dp[5] = 5 | dp[5] = 3 | dp[5] = 2 | dp[5] = 1 | dp[5] = 5 |     |
```

The 5th Fibonacci number is 5.

### 8.5: Case Studies and Applications

Dynamic programming has numerous applications in various fields, including:

- **Computer Networks**: Dynamic programming is used to solve problems related to network flows, routing, and scheduling.
- **Cryptography**: Dynamic programming is used to solve problems related to encryption and decryption.
- **Optimization**: Dynamic programming is used to solve problems related to optimization, such as finding the shortest path in a graph.
- **Machine Learning**: Dynamic programming is used to solve problems related to machine learning, such as finding the optimal parameters for a model.

Some notable case studies include:

- **Google's PageRank Algorithm**: Google's PageRank algorithm uses dynamic programming to calculate the importance of web pages.
- **Facebook's News Feed Algorithm**: Facebook's news feed algorithm uses dynamic programming to rank news articles.
- **Amazon's Recommendation System**: Amazon's recommendation system uses dynamic programming to recommend products to customers.

### 8.6: Conclusion

Dynamic programming is a powerful technique for solving complex problems by breaking them down into smaller subproblems and solving each subproblem only once. It has numerous applications in various fields and is a fundamental tool for any problem solver.

### Further Reading

- "Dynamic Programming" by Richard E. Bellman
- "The Elements of Computing Systems" by Noam Nisan and Shimon Schocken
- "Introduction to Algorithms" by Thomas H. Cormen
- "Dynamic Programming" by Thomas H. Cormen
- "Algorithms" by Robert Sedgewick and Kevin Wayne
