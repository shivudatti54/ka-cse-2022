# Chapter 4: Analysis & Design of Algorithms

### Section 4.1: Brute Force Approaches: Exhaustive Search

## **Introduction**

Exhaustive search, also known as brute force search, is a simple yet powerful algorithmic technique used to solve optimization problems. In this section, we will delve into the world of exhaustive search, explore its applications, and discuss its limitations.

## **What is Exhaustive Search?**

Exhaustive search is a trial-and-error approach that involves systematically exploring all possible solutions to a problem. It is based on the idea of trying every possible combination of inputs to find the optimal solution.

## **Historical Context**

Exhaustive search has been used for centuries in various forms. In ancient Greece, the mathematician Eratosthenes used exhaustive search to calculate the circumference of the Earth. In the 19th century, mathematicians used exhaustive search to prove Fermat's Last Theorem.

## **Modern Developments**

In the 20th century, exhaustive search was used extensively in computer science to solve optimization problems. Some notable examples include:

- **Traveling Salesman Problem (TSP)**: In 1932, the German mathematician Karl Menger used exhaustive search to solve the TSP.
- **Knapsack Problem**: In 1973, the American computer scientist Richard Bellman used exhaustive search to solve the knapsack problem.

## **Applications of Exhaustive Search**

Exhaustive search has numerous applications in various fields, including:

- **Optimization**: Exhaustive search is used to find the optimal solution to optimization problems, such as the traveling salesman problem, knapsack problem, and quadratic assignment problem.
- **Machine Learning**: Exhaustive search is used in machine learning to find the optimal solution to classification problems, such as support vector machines (SVMs).
- **Cryptography**: Exhaustive search is used in cryptography to find the prime factors of large numbers.

## **Types of Exhaustive Search**

There are two types of exhaustive search:

- **Brute Force Search**: Brute force search involves trying every possible combination of inputs to find the optimal solution.
- **Greedy Search**: Greedy search involves making the locally optimal choice at each step, hoping that it will lead to a global optimum.

## **Time and Space Complexity**

The time complexity of exhaustive search is O(n!), where n is the number of inputs. This makes it impractical for large inputs. The space complexity is also O(n!), as we need to store all possible combinations of inputs.

## **Example: Traveling Salesman Problem**

The traveling salesman problem is a classic example of an exhaustive search problem. Given a set of cities and their pairwise distances, the goal is to find the shortest possible tour that visits each city exactly once and returns to the starting city.

## **Algorithm**

Here is a simple algorithm for solving the traveling salesman problem using exhaustive search:

1.  Generate all possible permutations of the cities.
2.  Calculate the total distance of each permutation.
3.  Keep track of the permutation with the minimum distance.

## **Code**

```python
import itertools

def traveling_salesman_cities(cities):
    # Generate all possible permutations of the cities
    permutations = list(itertools.permutations(cities))

    # Initialize the minimum distance
    min_distance = float('inf')

    # Iterate over each permutation
    for permutation in permutations:
        # Calculate the total distance of the permutation
        distance = 0
        for i in range(len(permutation) - 1):
            distance += distance_matrix[permutation[i]][permutation[i + 1]]

        # Update the minimum distance
        min_distance = min(min_distance, distance)

    # Return the permutation with the minimum distance
    return permutation

# Define the distance matrix
distance_matrix = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('A', 'D'): 20,
    ('B', 'C'): 35,
    ('B', 'D'): 25,
    ('C', 'D'): 30
}

# Define the cities
cities = ['A', 'B', 'C', 'D']

# Solve the traveling salesman problem
solution = traveling_salesman_cities(cities)

print("The shortest tour is:", solution)
```

## **Conclusion**

In this section, we explored the world of exhaustive search, including its historical context, modern developments, and applications. We also discussed the time and space complexity of exhaustive search and provided an example of how to solve the traveling salesman problem using exhaustive search.

## **Further Reading**

- **"Introduction to Algorithms"** by Thomas H. Cormen: This book provides a comprehensive introduction to algorithms, including exhaustive search.
- **"The Traveling Salesman Problem"** by Lawrence W. Snyder: This book provides an in-depth analysis of the traveling salesman problem, including exhaustive search.
- **"Exhaustive Search"** by Wikipedia: This article provides a brief overview of exhaustive search, including its history, applications, and limitations.
