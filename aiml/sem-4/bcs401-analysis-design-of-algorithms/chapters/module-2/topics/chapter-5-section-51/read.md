# **Chapter 5: Analysis & Design of Algorithms**

## **Module: BRUTE FORCE APPROACHES (continued)**

## **Exhaustive Search (Travelling Salesman Problem)**

### Introduction

The Travelling Salesman Problem (TSP) is a classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the original city. It is a classic example of an NP-hard problem, which means that the running time of traditional algorithms increases exponentially with the size of the input.

### Definition

The Travelling Salesman Problem (TSP) can be defined as follows:

- Given a set of cities, each represented by a pair of coordinates (x, y)
- The objective is to find the shortest possible tour that visits all cities and returns to the original city
- The tour is represented by a sequence of cities

### Examples

- Suppose we have a set of 5 cities with coordinates (0, 0), (10, 0), (10, 10), (0, 10), and (5, 5)
- The shortest possible tour would visit the cities in the order: (0, 0) -> (10, 0) -> (10, 10) -> (0, 10) -> (5, 5) -> (0, 0)

### Exhaustive Search Algorithm

The Exhaustive Search algorithm is a simple algorithm that solves TSP by generating all possible tours and selecting the shortest one. The algorithm works as follows:

1. Generate all possible tours of a given length
2. Calculate the total distance of each tour
3. Select the tour with the shortest total distance

### Pseudocode

```
function exhaustiveSearch(cities, length):
  // Generate all possible tours
  tours = generateTours(cities, length)

  // Initialize minimum distance
  minDistance = infinity

  // Iterate over each tour
  foreach tour in tours:
    // Calculate total distance of tour
    distance = calculateDistance(tour)

    // Update minimum distance if necessary
    if distance < minDistance:
      minDistance = distance
  return minDistance
```

### Time Complexity

The time complexity of the Exhaustive Search algorithm is O(n!), where n is the number of cities. This is because there are n! possible tours, and the algorithm generates and evaluates each one.

### Space Complexity

The space complexity of the Exhaustive Search algorithm is O(n!), as the algorithm needs to store all possible tours.

### Limitations

The Exhaustive Search algorithm is not practical for large inputs due to its high time and space complexity. It is mainly used for small inputs or for illustrative purposes.

### Conclusion

The Exhaustive Search algorithm is a simple algorithm for solving the Travelling Salesman Problem, but it is not practical for large inputs due to its high time and space complexity. Other algorithms, such as dynamic programming and approximation algorithms, are more efficient and effective for solving TSP.

### Key Concepts

- **Travelling Salesman Problem (TSP)**: a classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the original city.
- **Exhaustive Search Algorithm**: a simple algorithm that solves TSP by generating all possible tours and selecting the shortest one.
- **NP-hard problem**: a type of problem that is computationally intractable and requires an exponential amount of time to solve exactly.
- **Time complexity**: a measure of the amount of time an algorithm takes to complete, usually expressed in Big O notation.
- **Space complexity**: a measure of the amount of memory an algorithm uses, usually expressed in Big O notation.
