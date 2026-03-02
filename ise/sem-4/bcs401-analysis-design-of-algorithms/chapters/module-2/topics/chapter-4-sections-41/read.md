# Chapter 4: Brute Force Approaches (Exhaustive Search)

=============================================

# 4.1: Traveling Salesman Problem (TSP)

---

The Traveling Salesman Problem (TSP) is a classic problem in combinatorial optimization and computer science. It involves finding the shortest possible tour that visits a set of cities and returns to the starting city.

## Definition:

Given a set of cities (or nodes) and their pairwise distances, the TSP is to find the shortest possible tour that visits each city exactly once and returns to the starting city.

## Examples:

- A salesman who needs to visit a set of customers, return to the salesperson's office, and minimize the total distance traveled.
- A delivery truck that needs to visit a set of warehouses, return to the depot, and minimize the total distance traveled.

## Key Concepts:

- **Distance Matrix**: A matrix that represents the pairwise distances between each pair of cities.
- **TSP Instance**: A specific instance of the TSP problem, represented by a group of cities and their pairwise distances.
- **Tour**: A sequence of cities visited in a particular order, representing a possible solution to the TSP.

## Brute Force Approach:

The brute force approach to solving TSP involves generating all possible tours of the given cities and selecting the shortest one. This is often referred to as the **exhaustive search** method.

### Algorithm:

1. Generate all possible permutations of the cities (i.e., all possible tours).
2. Calculate the total distance of each tour using the distance matrix.
3. Compare the distances of each tour and select the shortest one.
4. Return the shortest tour as the solution to the TSP.

### Time Complexity:

The time complexity of the brute force approach is O(n!), where n is the number of cities. This is because there are n! possible permutations of the cities, and generating each permutation requires O(n) time.

## Limitations:

The brute force approach is impractical for large TSP instances due to its high time complexity. It is also not a efficient method for solving TSP, as it involves generating and evaluating all possible tours.

## Real-World Applications:

- Route planning for delivery trucks and taxis.
- Scheduling for tour operators.
- Optimization of supply chain routes.

## Code Example:

Here is a simple Python code that demonstrates the brute force approach to solving TSP using a distance matrix:

```python
import itertools
import math

def distance_matrix(cities):
    # Initialize distance matrix with zeros
    dist_matrix = [[0 for _ in range(len(cities))] for _ in range(len(cities))]

    # Calculate pairwise distances
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

    return dist_matrix

def brute_force_tsp(cities, dist_matrix):
    # Generate all possible permutations of cities
    permutations = list(itertools.permutations(cities))

    # Initialize minimum distance
    min_dist = float('inf')

    # Find shortest tour
    for tour in permutations:
        tour_dist = 0
        for i in range(len(tour)-1):
            tour_dist += dist_matrix[tour[i]][tour[i+1]]
        tour_dist += dist_matrix[tour[-1]][tour[0]]  # Add distance from last city to first city
        if tour_dist < min_dist:
            min_dist = tour_dist

    return min_dist

# Example usage
cities = [(0, 0), (10, 0), (5, 3), (0, 5)]
dist_matrix = distance_matrix(cities)
min_dist = brute_force_tsp(cities, dist_matrix)
print("Minimum distance:", min_dist)
```

Note that this is a highly optimized example and does not account for many real-world complexities, such as handling degenerate cases and using more efficient data structures.
