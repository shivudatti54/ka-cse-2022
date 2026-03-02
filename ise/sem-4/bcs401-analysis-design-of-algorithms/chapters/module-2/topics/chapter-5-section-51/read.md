**Chapter 5: Analysis & Design of Algorithms**
**Section 5.1: BRUTE FORCE APPROACHES (continued)**
**Exhaustive Search: Travelling Salesman Problem**

# **5.1.1 Introduction**

The Travelling Salesman Problem (TSP) is a classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the starting city. In this section, we will explore the Brute Force approach to solving TSP, which involves exhaustively searching all possible permutations of cities.

# **5.1.2 Definition**

The Travelling Salesman Problem is defined as follows:

- A set of `n` cities, each represented by a coordinate (x, y)
- Each city has a distance function `d(i, j)` that calculates the distance between cities `i` and `j`
- The goal is to find the shortest possible tour that visits each city exactly once and returns to the starting city

# **5.1.3 Brute Force Approach**

The Brute Force approach to solving TSP involves exhaustively searching all possible permutations of cities. Here is a high-level outline of the steps involved:

1. **Generate all permutations**: Generate all possible permutations of the `n` cities
2. **Calculate distance**: Calculate the total distance of each permutation
3. **Compare distances**: Compare the distances of each permutation and keep track of the shortest one

# **5.1.4 Example**

Suppose we have 4 cities: A(0, 0), B(3, 4), C(6, 8), and D(9, 12). We can generate all possible permutations of these cities and calculate the distance of each permutation:

| Permutation | Distance |
| ----------- | -------- |
| A-B-C-D     | 17       |
| A-B-D-C     | 20       |
| A-C-B-D     | 22       |
| A-C-D-B     | 25       |
| A-D-B-C     | 24       |
| A-D-C-B     | 28       |
| B-A-C-D     | 19       |
| B-A-D-C     | 22       |
| ...         | ...      |

As we can see, the Brute Force approach requires an exponential amount of computation, especially for larger values of `n`.

# **5.1.5 Time and Space Complexity**

The time complexity of the Brute Force approach is O(n!), where `n` is the number of cities. This is because we need to generate all possible permutations of `n` cities.

The space complexity is also O(n!), as we need to store all permutations in memory.

# **5.1.6 Trade-offs**

While the Brute Force approach is simple to understand and implement, it is not efficient for large values of `n`. More efficient algorithms, such as dynamic programming and approximation algorithms, are needed for larger instances of TSP.

# **5.1.7 Key Concepts**

- **Permutation**: An arrangement of objects in a specific order
- **Distance function**: A function that calculates the distance between two points
- **Brute Force approach**: A method that involves exhaustively searching all possible solutions
- **Time complexity**: A measure of the amount of time an algorithm takes to execute
- **Space complexity**: A measure of the amount of memory an algorithm uses

# **Conclusion**

In this section, we explored the Brute Force approach to solving the Travelling Salesman Problem, which involves exhaustively searching all possible permutations of cities. While this approach is simple to understand and implement, it is not efficient for large values of `n`. More efficient algorithms are needed for larger instances of TSP.
