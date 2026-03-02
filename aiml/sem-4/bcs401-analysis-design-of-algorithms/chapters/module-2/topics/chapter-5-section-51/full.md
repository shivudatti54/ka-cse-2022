# Chapter 5: Analysis & Design of Algorithms

### Section 5.1: Exhaustive Search (Brute Force Approaches)

Exhaustive search, also known as brute force search, is a straightforward approach to solving optimization problems. It involves systematically checking all possible solutions to find the optimal one. In this section, we will delve into the analysis and design of exhaustive search algorithms, with a focus on the Travelling Salesman Problem (TSP).

### Historical Context

The concept of exhaustive search dates back to the early days of computer science. In the 1950s, computers were not as powerful as they are today, and algorithms were designed with the assumption that the problem size was small. Exhaustive search was a viable approach for solving small problems, such as the Traveling Salesman Problem.

However, with the advent of modern computers and the increasing size of problems, exhaustive search became impractical. The number of possible solutions grows exponentially with the problem size, making it impossible to solve large problems using exhaustive search alone.

### Analysis of Exhaustive Search

Exhaustive search is a simple and intuitive approach to solving optimization problems. It involves the following steps:

1. **Problem Definition**: Define the problem clearly, including the objective function and constraints.
2. **Solution Space**: Determine the solution space, which is the set of all possible solutions.
3. **Evaluation Function**: Define an evaluation function that assigns a score to each solution based on the objective function.
4. **Search**: Systematically check all possible solutions in the solution space, evaluating each one using the evaluation function.
5. **Optimal Solution**: Identify the optimal solution, which is the solution with the highest score.

### Strengths of Exhaustive Search

1. **Guaranteed Optimal**: Exhaustive search guarantees the optimal solution, as it checks all possible solutions.
2. **Simple Implementation**: Exhaustive search is a simple approach to implement, as it involves a straightforward loop through all possible solutions.

### Weaknesses of Exhaustive Search

1. **High Computational Complexity**: Exhaustive search has high computational complexity, as it requires checking all possible solutions.
2. **Infeasible for Large Problems**: Exhaustive search is infeasible for large problems, as the number of possible solutions grows exponentially with the problem size.

### Application of Exhaustive Search

Exhaustive search is commonly used in optimization problems that have a small solution space. Some examples include:

1. **Traveling Salesman Problem (TSP)**: Exhaustive search is used to find the shortest possible tour that visits all cities and returns to the starting point.
2. **Scheduling Problems**: Exhaustive search is used to schedule tasks and resources to minimize delays and maximize efficiency.
3. **Resource Allocation**: Exhaustive search is used to allocate resources to maximize efficiency and minimize waste.

### Case Study: Traveling Salesman Problem (TSP)

The Traveling Salesman Problem (TSP) is a classic optimization problem that involves finding the shortest possible tour that visits all cities and returns to the starting point. The TSP is a great example of an exhaustive search problem, as it involves checking all possible tours to find the optimal one.

**Problem Definition**:

- Define the cities and their coordinates.
- Define the distance matrix, which represents the distance between each pair of cities.
- Define the objective function, which is the total distance of the tour.

**Solution Space**:

- The solution space consists of all possible tours that visit all cities and return to the starting point.
- The number of possible tours is equal to the number of permutations of the cities.

**Evaluation Function**:

- The evaluation function assigns a score to each tour based on the total distance.
- The score is calculated by summing up the distances between each pair of cities in the tour.

**Search**:

- The exhaustive search algorithm checks all possible tours in the solution space, evaluating each one using the evaluation function.
- The algorithm uses a brute force approach, checking all possible permutations of the cities.

**Optimal Solution**:

- The algorithm identifies the optimal solution, which is the tour with the shortest total distance.
- The optimal solution is the shortest possible tour that visits all cities and returns to the starting point.

### Diagram: Exhaustive Search Algorithm

```markdown
+---------------+
| Problem Definition |
+---------------+
|
|
v
+---------------+
| Solution Space |
+---------------+
|
|
v
+---------------+
| Evaluation Function |
+---------------+
|
|
v
+---------------+
| Search (Brute Force) |
+---------------+
|
|
v
+---------------+
| Optimal Solution |
+---------------+
```

### Modern Developments

While exhaustive search is still used in some optimization problems, modern algorithms have largely replaced it due to their improved efficiency and scalability. Some examples include:

1. **Greedy Algorithms**: Greedy algorithms use a heuristic approach to find a suboptimal solution that is near optimal.
2. **Local Search Algorithms**: Local search algorithms use a iterative approach to find a local optimum solution.
3. **Metaheuristics**: Metaheuristics use a combination of heuristics and search techniques to find a good solution.

### Conclusion

Exhaustive search is a simple and intuitive approach to solving optimization problems. While it is guaranteed to find the optimal solution, it has high computational complexity and is infeasible for large problems. Modern algorithms have largely replaced exhaustive search due to their improved efficiency and scalability.

### Further Reading

1. "Introduction to Algorithms" by Thomas H. Cormen
2. "Algorithms" by Robert Sedgewick and Kevin Wayne
3. "Optimization Algorithms" by Steven C. Chapra and Raymond P. Canale
4. "Traveling Salesman Problem" by David S. Johnson
5. "Greedy Algorithms" by Robert Sedgewick and Kevin Wayne

Note: The references provided are a selection of popular and well-regarded resources on the topic of algorithms and optimization. They are intended to provide a starting point for further exploration and learning.
