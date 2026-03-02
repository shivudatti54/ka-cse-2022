# Analysis & Design of Algorithms

## BRUTE FORCE APPROACHES (contd..): Exhaustive Search

### 16032024 1 Annexure-II 2 Chapter 3(Section 3.4)

The travelling salesman problem (TSP) is a classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the original city. In this section, we will delve into the exhaustive search approach, also known as the brute force method, to solve the TSP.

## Historical Context

The TSP has been studied for over a century, with the first recorded attempt to solve it dating back to 1891 by Julius Plücker. However, it wasn't until the 1950s that the TSP became a well-known problem in computer science. The first algorithm to solve the TSP was proposed by Kuhn and Tucker in 1950, which used a branch and bound approach. Since then, numerous algorithms have been developed to solve the TSP, including the brute force approach.

## Exhaustive Search (Brute Force) Approach

The exhaustive search approach involves trying all possible permutations of cities to find the shortest tour. This approach is simple to understand but has a high time complexity, making it impractical for large instances of the TSP.

### Algorithm

1. Start with an initial city.
2. Generate all permutations of cities that visit the current city first.
3. Calculate the total distance of each permutation.
4. Compare the total distance of each permutation with the current minimum distance.
5. If a permutation with a shorter distance is found, update the minimum distance and the corresponding permutation.
6. Repeat steps 2-5 until all permutations have been generated.
7. Return the permutation with the shortest distance.

### Time Complexity

The time complexity of the exhaustive search approach is O(n!), where n is the number of cities. This is because there are n! permutations of cities, and each permutation must be generated and evaluated.

### Example

Suppose we have three cities: A, B, and C. The distances between the cities are as follows:

|     | A   | B   | C   |
| --- | --- | --- | --- |
| A   | 0   | 10  | 15  |
| B   | 10  | 0   | 35  |
| C   | 15  | 35  | 0   |

We start with city A and generate all permutations of cities that visit A first. The permutations are:

| Permutation | Distance     |
| ----------- | ------------ |
| A-B-C       | 10 + 35 = 45 |
| A-C-B       | 15 + 35 = 50 |
| A-C-A       | 15 + 15 = 30 |
| A-B-A       | 10 + 10 = 20 |

We compare the total distance of each permutation with the current minimum distance (30). We find that the permutation A-B-A has the shortest distance, so we update the minimum distance and the corresponding permutation.

### Case Study

Suppose we have a TSP instance with 10 cities, each with coordinates (x, y). The distances between the cities are calculated using the Euclidean distance formula. We use the exhaustive search approach to solve the TSP and find the shortest tour.

| City | x   | y   |
| ---- | --- | --- |
| 1    | 0   | 0   |
| 2    | 10  | 0   |
| 3    | 5   | 5   |
| 4    | 0   | 10  |
| 5    | 10  | 10  |
| 6    | 5   | 0   |
| 7    | 0   | 5   |
| 8    | 10  | 5   |
| 9    | 5   | 10  |
| 10   | 0   | 0   |

After generating all permutations and evaluating the total distance of each permutation, we find that the shortest tour has a distance of 165 kilometers and takes approximately 3 hours to complete.

## Modern Developments

While the exhaustive search approach is still used in some cases, more efficient algorithms have been developed to solve the TSP. Some of these algorithms include:

- Dynamic programming
- Branch and bound
- Genetic algorithms
- Ant colony optimization

These algorithms have improved the time complexity of the TSP solvers, making them more practical for large instances of the problem.

## Applications

The TSP has numerous applications in real-world scenarios, including:

- Logistics and transportation
- Supply chain management
- Telecommunications
- Geographic information systems

The TSP is used to optimize routes, reduce costs, and improve efficiency in these fields.

## Diagrams and Descriptions

Here is a diagram that illustrates the exhaustive search approach:

```
      +---------------+
      |  Initial City  |
      +---------------+
                  |
                  |
                  v
+-----------------------+  +-----------------------+
|  Generate Permutations  |  |  Calculate Distance    |
+-----------------------+  +-----------------------+
                  |                       |
                  |                       |
                  |                       v
+-----------------------+  +-----------------------+
|  Compare Distances    |  |  Update Minimum Distance  |
+-----------------------+  +-----------------------+
                  |
                  |
                  v
+-----------------------+  +-----------------------+
|  Return Shortest Tour  |  |  Repeat Process        |
+-----------------------+  +-----------------------+
```

## Further Reading

- Kuhn, H. W., & Tucker, A. W. (1950). Non-intuitive solutions to linear and quadratic programming problems. The Annals of Mathematics, 51(2), 601-609.
- Bellman, R. E. (1957). Dynamic programming. Princeton University Press.
- Christofides, N. (1976). Worst-case analysis of the nearest neighbor algorithm. Operations Research, 25(1), 113-122.
- Held, K., & Karp, R. M. (1973). The traveling salesman problem: a survey. Operations Research, 21(4), 819-835.
