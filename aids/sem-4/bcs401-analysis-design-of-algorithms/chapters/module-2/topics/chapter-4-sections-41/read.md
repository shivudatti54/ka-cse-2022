# **Chapter 4: Analysis & Design of Algorithms**

## **BRUTE FORCE APPROACHES (continued): Exhaustive Search**

### 4.1 Exhaustive Search

**Definition:** Exhaustive search is a method of finding the optimal solution by checking every possible solution. It involves systematically exploring all possible combinations of input values to find the correct output.

**Characteristics:**

- Time complexity: O(n!), where n is the number of elements in the input.
- Space complexity: O(1), as only a constant amount of space is required.
- Relatively simple to implement.

### 4.1.1 Travelling Salesman Problem (TSP)

**Definition:** TSP is a classic problem in combinatorial optimization and computer science. Given a set of cities and their pairwise distances, the goal is to find the shortest possible tour that visits each city exactly once and returns to the starting city.

**Example:**

Suppose we have five cities: A, B, C, D, and E, with the following distances between them:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| A   | 0   | 10  | 15  | 20  | 25  |
| B   | 10  | 0   | 35  | 25  | 30  |
| C   | 15  | 35  | 0   | 20  | 15  |
| D   | 20  | 25  | 20  | 0   | 35  |
| E   | 25  | 30  | 15  | 35  | 0   |

The goal is to find the shortest possible tour that visits each city exactly once and returns to the starting city A.

**Solution:**

Using exhaustive search, we can calculate the total distance for each possible tour and find the shortest one:

1.  A -> B -> C -> D -> E -> A: 10 + 35 + 20 + 35 + 25 = 105
2.  A -> B -> C -> E -> D -> A: 10 + 35 + 30 + 35 + 20 = 110
3.  A -> B -> D -> C -> E -> A: 10 + 25 + 20 + 15 + 15 = 85
4.  A -> B -> D -> E -> C -> A: 10 + 25 + 35 + 15 + 15 = 100
5.  A -> C -> B -> D -> E -> A: 15 + 35 + 25 + 35 + 25 = 125
6.  A -> C -> B -> E -> D -> A: 15 + 35 + 30 + 35 + 20 = 135
7.  A -> C -> D -> B -> E -> A: 15 + 20 + 25 + 30 + 25 = 115
8.  A -> C -> D -> E -> B -> A: 15 + 20 + 35 + 30 + 10 = 110
9.  A -> C -> E -> B -> D -> A: 15 + 30 + 35 + 25 + 20 = 125
10. A -> C -> E -> D -> B -> A: 15 + 30 + 35 + 25 + 10 = 115
11. A -> C -> E -> B -> A -> D: 15 + 30 + 35 + 10 + 20 = 110
12. A -> C -> E -> D -> A -> B: 15 + 30 + 35 + 20 + 10 = 110
13. A -> C -> E -> D -> B -> A: 15 + 30 + 35 + 25 + 10 = 115
14. A -> C -> D -> E -> B -> A: 15 + 35 + 35 + 25 + 10 = 120
15. A -> D -> C -> B -> E -> A: 20 + 20 + 35 + 30 + 25 = 130
16. A -> D -> C -> E -> B -> A: 20 + 20 + 35 + 30 + 10 = 115
17. A -> D -> C -> E -> B -> A: 20 + 20 + 35 + 30 + 10 = 115
18. A -> D -> B -> C -> E -> A: 20 + 25 + 20 + 15 + 25 = 105
19. A -> D -> B -> E -> C -> A: 20 + 25 + 35 + 15 + 15 = 110
20. A -> D -> B -> E -> C -> A: 20 + 25 + 35 + 15 + 15 = 110

The shortest possible tour is A -> D -> B -> E -> C -> A, with a total distance of 105.

### 4.1.2 Example Use Cases

- Traveling Salesman Problem: TSP is widely used in logistics, transportation, and telecommunication industries to find the shortest possible route for delivery trucks, taxis, and other vehicles.
- Resource Allocation: Exhaustive search can be used to find the optimal resource allocation for tasks, jobs, or projects, by checking every possible combination of resources.
- Scheduling: TSP can be used to find the optimal scheduling for tasks, jobs, or projects, by checking every possible schedule.

### 4.1.3 Advantages and Disadvantages

**Advantages:**

- Relatively simple to implement.
- Can be used for small to medium-sized instances.
- Provides an optimal solution.

**Disadvantages:**

- Has a high time complexity (O(n!)), making it impractical for large instances.
- Requires a large amount of memory to store all possible solutions.
- Can be computationally expensive.

### 4.1.4 Conclusion

Exhaustive search is a simple and effective method for finding the optimal solution, but it is not suitable for large instances due to its high time and space complexity. Other methods, such as greedy algorithms, dynamic programming, and heuristics, are more efficient and practical for solving TSP and other problems.
