# Analysis & Design of Algorithms

## Module: BRUTE FORCE APPROACHES (continued)

### Exhaustive Search: Travelling Salesman Problem

#### @# 16032024 1 Annexure-II 2 Chapter 3(Section 3.4)

### 3.4 Exhaustive Search Algorithm

The Exhaustive Search algorithm is a simple, yet time-consuming approach to solve the Travelling Salesman Problem (TSP). This algorithm involves generating all possible permutations of the cities and calculating the total distance for each permutation.

### Key Concepts:

- **TSP:** A classic problem in combinatorial optimization and computer science, where the goal is to find the shortest possible route that visits a set of cities and returns to the starting city.
- **Exhaustive Search:** A brute-force approach that generates all possible solutions to a problem and evaluates them to find the optimal one.
- **Permutations:** A rearrangement of elements in a specific order.

### How the Algorithm Works:

1.  **Generate all permutations:** Create a list of all possible permutations of the cities. This can be done using backtracking or recursion.
2.  **Calculate the distance:** For each permutation, calculate the total distance traveled by summing up the distances between consecutive cities.
3.  **Find the shortest distance:** Compare the total distance of each permutation and find the one with the shortest distance.

### Example:

Suppose we have 4 cities: A, B, C, and D. We want to find the shortest route that visits each city and returns to the starting city.

| Permutation | Distance            |
| ----------- | ------------------- |
| ABCD        | 10 + 6 + 3 + 2 = 21 |
| ACBD        | 10 + 3 + 6 + 2 = 21 |
| ADBC        | 10 + 2 + 6 + 3 = 21 |
| ABDC        | 10 + 2 + 3 + 6 = 21 |
| BCAD        | 6 + 3 + 10 + 2 = 21 |
| BDAC        | 6 + 2 + 10 + 3 = 21 |
| CDAB        | 3 + 2 + 10 + 6 = 21 |
| CDBA        | 3 + 2 + 6 + 10 = 21 |

The shortest distance is 21, which is found in multiple permutations.

### Time Complexity:

The time complexity of the Exhaustive Search algorithm is O(n!), where n is the number of cities. This is because there are n! permutations of n cities, and we need to evaluate each permutation.

### Space Complexity:

The space complexity of the algorithm is O(n!), as we need to store all permutations in memory.

### Example Code (Python):

```python
import itertools

def distance(city1, city2):
    # Calculate distance between two cities (assuming Euclidean distance)
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def exhaustive_search(cities):
    # Generate all permutations of cities
    permutations = list(itertools.permutations(cities))

    # Initialize shortest distance and best permutation
    shortest_distance = float('inf')
    best_permutation = None

    for permutation in permutations:
        # Calculate total distance for each permutation
        total_distance = sum(distance(permutation[i], permutation[i + 1]) for i in range(len(permutation) - 1))

        # Update shortest distance and best permutation if necessary
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            best_permutation = permutation

    return best_permutation, shortest_distance

# Example usage:
cities = [(0, 0), (10, 0), (5, 3), (0, 5)]
best_permutation, shortest_distance = exhaustive_search(cities)
print("Best permutation:", best_permutation)
print("Shortest distance:", shortest_distance)
```

Note that the above code is a simplified example and may not be efficient for large inputs.
