# Exhaustive Search: A Brute Force Approach to the Travelling Salesman Problem

===========================================================

## Introduction

---

Exhaustive search is a brute force approach used to solve the Travelling Salesman Problem (TSP). TSP is an NP-hard problem that involves finding the shortest possible tour that visits a set of cities and returns to the original city. Exhaustive search involves generating all possible permutations of cities and selecting the one with the shortest total distance.

## Definition

---

Exhaustive search is a search algorithm that generates all possible solutions to a problem and evaluates each solution. In the context of TSP, it involves generating all possible permutations of cities and calculating the total distance of each permutation.

## How it Works

---

Here are the steps involved in implementing exhaustive search for TSP:

1. **Generate all permutations**: Generate all possible permutations of cities.
2. **Calculate total distance**: Calculate the total distance of each permutation.
3. **Evaluate permutations**: Evaluate each permutation based on its total distance.
4. **Select the shortest permutation**: Select the permutation with the shortest total distance.

## Algorithm

---

Here is a step-by-step algorithm for implementing exhaustive search for TSP:

### Step 1: Generate All Permutations

- Start with the first city.
- For each subsequent city, choose one of the two options: include it in the current permutation or exclude it.
- Generate all possible permutations using this process.

### Step 2: Calculate Total Distance

- For each permutation, calculate the total distance by summing up the distances between consecutive cities in the permutation.

### Step 3: Evaluate Permutations

- For each permutation, evaluate its total distance.

### Step 4: Select the Shortest Permutation

- Compare the total distances of all permutations and select the one with the shortest total distance.

## Example

---

Suppose we have five cities: A, B, C, D, and E. We want to find the shortest possible tour that visits all five cities and returns to the original city.

Here are the distances between consecutive cities:

| City | A   | B   | C   | D   | E   |
| ---- | --- | --- | --- | --- | --- |
| A    | 0   | 10  | 15  | 20  | 25  |
| B    | 10  | 0   | 35  | 30  | 20  |
| C    | 15  | 35  | 0   | 25  | 18  |
| D    | 20  | 30  | 25  | 0   | 22  |
| E    | 25  | 20  | 18  | 22  | 0   |

We can generate all possible permutations of cities and calculate the total distance of each permutation. Here are the permutations and their total distances:

| Permutation | Total Distance |
| ----------- | -------------- |
| A-B-C-D-E   | 90             |
| A-B-C-E-D   | 95             |
| A-B-D-C-E   | 100            |
| A-B-D-E-C   | 105            |
| A-C-B-D-E   | 90             |
| ...         | ...            |

After evaluating all permutations, we select the permutation with the shortest total distance, which is A-B-C-D-E with a total distance of 90.

## Code Example

---

Here is a Python code example that implements exhaustive search for TSP:

```python
import itertools

def distance(city1, city2):
    # Define the distances between consecutive cities
    distances = {
        ('A', 'B'): 10,
        ('A', 'C'): 15,
        ('A', 'D'): 20,
        ('A', 'E'): 25,
        ('B', 'A'): 10,
        ('B', 'C'): 35,
        ('B', 'D'): 30,
        ('B', 'E'): 20,
        ('C', 'A'): 15,
        ('C', 'B'): 35,
        ('C', 'D'): 25,
        ('C', 'E'): 18,
        ('D', 'A'): 20,
        ('D', 'B'): 30,
        ('D', 'C'): 25,
        ('D', 'E'): 22,
        ('E', 'A'): 25,
        ('E', 'B'): 20,
        ('E', 'C'): 18,
        ('E', 'D'): 22
    }
    return distances[(city1, city2)]

def exhaustive_search(cities):
    # Generate all permutations of cities
    permutations = list(itertools.permutations(cities))

    # Calculate the total distance of each permutation
    distances = [sum(distance(permutation[i], permutation[i+1]) for i in range(len(permutation)-1)) + distance(permutation[-1], permutation[0]) for permutation in permutations]

    # Find the permutation with the shortest total distance
    min_distance = min(distances)
    min_permutation = permutations[distances.index(min_distance)]
    return min_permutation, min_distance

# Example usage
cities = ['A', 'B', 'C', 'D', 'E']
min_permutation, min_distance = exhaustive_search(cities)
print(f"Shortest permutation: {min_permutation}")
print(f"Minimum distance: {min_distance}")
```

This code defines a `distance` function that calculates the distance between two cities, and an `exhaustive_search` function that generates all permutations of cities, calculates the total distance of each permutation, and finds the permutation with the shortest total distance.
