# Chapter 4: Analysis & Design of Algorithms

## Brute Force Approaches (continued): Exhaustive Search

### Section 4.1: The Travelling Salesman Problem

=====================================================

The Travelling Salesman Problem (TSP) is a classic problem in combinatorial optimization and operations research that has been extensively studied in computer science and mathematics. The problem is defined as follows:

**Problem Statement:**

Given a list of cities and their pairwise distances, find the shortest possible tour that visits each city exactly once and returns to the starting city.

**Example:**

Suppose we have five cities: A, B, C, D, and E, with the following pairwise distances:

| City | A   | B   | C   | D   | E   |
| ---- | --- | --- | --- | --- | --- |
| A    | 0   | 10  | 15  | 20  | 25  |
| B    | 10  | 0   | 35  | 25  | 30  |
| C    | 15  | 35  | 0   | 30  | 20  |
| D    | 20  | 25  | 30  | 0   | 15  |
| E    | 25  | 30  | 20  | 15  | 0   |

We want to find the shortest possible tour that visits each city exactly once and returns to the starting city.

### Algorithm Design: Exhaustive Search

---

The Exhaustive Search algorithm is a brute force approach that involves trying all possible permutations of cities and calculating the total distance for each permutation. The algorithm works as follows:

1. Generate all possible permutations of cities.
2. Calculate the total distance for each permutation.
3. Keep track of the permutation with the shortest total distance.

### Example Code (Python):

```python
import itertools

def calculate_distance(city_distances, permutation):
    distance = 0
    for i in range(len(permutation) - 1):
        distance += city_distances[permutation[i]][permutation[i + 1]]
    distance += city_distances[permutation[-1]][permutation[0]]
    return distance

def exhaustive_search(city_distances):
    min_distance = float('inf')
    shortest_permutation = None
    for permutation in itertools.permutations(range(len(city_distances))):
        distance = calculate_distance(city_distances, permutation)
        if distance < min_distance:
            min_distance = distance
            shortest_permutation = permutation
    return shortest_permutation, min_distance

# Example usage:
city_distances = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

shortest_permutation, min_distance = exhaustive_search(city_distances)
print("Shortest permutation:", shortest_permutation)
print("Minimum distance:", min_distance)
```

### Analysis and Design Considerations

---

1. **Time Complexity:** The time complexity of the Exhaustive Search algorithm is O(n!), where n is the number of cities. This is because there are n! possible permutations of cities.
2. **Space Complexity:** The space complexity of the algorithm is O(n), where n is the number of cities. This is because we need to store the city distances and the permutations.
3. **Scalability:** The Exhaustive Search algorithm is not scalable for large numbers of cities due to its high time complexity.

### Modern Developments and Variations

---

1. **Approximation Algorithms:** There are several approximation algorithms that can solve the TSP in polynomial time, such as the Christofides algorithm and the Held-Karp algorithm.
2. **Heuristics:** Heuristics such as the Nearest Neighbor algorithm and the Genetic Algorithm can be used to solve the TSP in a reasonable amount of time.
3. **Metaheuristics:** Metaheuristics such as Simulated Annealing and Tabu Search can be used to solve the TSP in a reasonable amount of time.

### Case Studies and Applications

---

1. **Route Planning:** The TSP has numerous applications in route planning, such as determining the shortest route for a delivery truck or a taxi.
2. **Logistics:** The TSP has numerous applications in logistics, such as determining the shortest route for a supply chain.
3. **Telecommunications:** The TSP has numerous applications in telecommunications, such as determining the shortest route for a fiber optic cable.

### Further Reading

---

- [1] "The Travelling Salesman Problem" by Richard K. Beasley, Donald J. Olsen, and Peter R. Russell
- [2] "Approximation Algorithms for the Travelling Salesman Problem" by David S. Johnson
- [3] "The Held-Karp Algorithm for the Travelling Salesman Problem" by M. Held and D. P. Karp

Note: The references provided are just a few examples of the many resources available on the topic of the Travelling Salesman Problem.
