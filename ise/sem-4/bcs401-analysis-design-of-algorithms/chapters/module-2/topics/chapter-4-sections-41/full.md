# **Chapter 4: Analysis & Design of Algorithms**

## **Section 4.1: BRUTE FORCE APPROACHES (contd..)**

## **Exhaustive Search: A Brute Force Approach**

Exhaustive search is a brute force approach to solving a problem by trying all possible solutions. This method is often used when the problem has a small number of possible solutions, and the cost of evaluating each solution is low.

## **History of Exhaustive Search**

The concept of exhaustive search dates back to ancient Greece, where mathematicians such as Euclid and Archimedes used it to solve problems. However, the term "exhaustive search" was first coined by the computer scientist Alan Turing in the 1930s.

## **Theoretical Background**

Exhaustive search is based on the concept of a search tree, which is a tree-like data structure that represents all possible solutions to a problem. Each node in the tree represents a solution, and each edge represents a possible next step.

The search tree can be traversed using a depth-first search (DFS) or breadth-first search (BFS) algorithm. DFS is used when the search tree is too large to fit in memory, while BFS is used when the search tree is too large to fit in memory.

## **Example: Travelling Salesman Problem**

The Travelling Salesman Problem (TSP) is a classic example of an exhaustive search problem. Given a set of cities and their pairwise distances, the goal is to find the shortest possible tour that visits each city exactly once and returns to the starting city.

Here is an example of how the TSP can be solved using exhaustive search:

```markdown
|        | City A | City B | City C |
| ------ | ------ | ------ | ------ |
| City A | 0      | 10     | 15     |
| City B | 10     | 0      | 35     |
| City C | 15     | 35     | 0      |
```

In this example, there are 3 cities, and the pairwise distances are given. The exhaustive search algorithm tries all possible tours, starting from each city, and evaluates the total distance of each tour.

## **Algorithm**

Here is a step-by-step algorithm for solving the TSP using exhaustive search:

1. Start at a random city.
2. Evaluate all possible tours starting from the current city.
3. For each tour, calculate the total distance.
4. Keep track of the shortest tour found so far.
5. Repeat steps 2-4 until all possible tours have been evaluated.
6. Return the shortest tour found.

## **Code Example**

Here is a Python code example that solves the TSP using exhaustive search:

```python
import itertools

def tsp_exhaustive_search(distances):
    # Define the number of cities
    num_cities = len(distances)

    # Initialize the shortest tour
    shortest_tour = None
    shortest_distance = float('inf')

    # Evaluate all possible tours
    for tour in itertools.permutations(range(num_cities)):
        # Calculate the total distance
        distance = sum(distances[tour[i]][tour[(i+1) % num_cities]] for i in range(num_cities))

        # Update the shortest tour if necessary
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_tour = tour

    return shortest_tour, shortest_distance

# Example usage
distances = [[0, 10, 15], [10, 0, 35], [15, 35, 0]]
tour, distance = tsp_exhaustive_search(distances)
print("Shortest tour:", tour)
print("Shortest distance:", distance)
```

## **Case Study: The Traveling Salesman Problem**

The Traveling Salesman Problem is a classic example of an exhaustive search problem. The problem has been extensively studied in computer science and operations research, and several algorithms have been developed to solve it.

One of the most well-known algorithms for solving the TSP is the Held-Karp algorithm, which is a dynamic programming algorithm that solves the problem in O(n^2 \* 2^n) time.

Another algorithm for solving the TSP is the branch and bound algorithm, which is a heuristic algorithm that uses bounds to prune the search tree.

## **Applications**

Exhaustive search has several applications in computer science and operations research, including:

- The Traveling Salesman Problem
- The Knapsack Problem
- The Scheduling Problem
- The Resource Allocation Problem

## **Modern Developments**

While exhaustive search is still used in some applications, it is no longer the preferred method due to its high computational complexity. Modern algorithms such as branch and bound, genetic algorithms, and metaheuristics have been developed to solve TSP and other exhaustive search problems.

## **Further Reading**

- "The Traveling Salesman Problem" by David S. Johnson
- "Exhaustive Search" by Alan Turing
- "The Held-Karp Algorithm" by Richard M. Karp
- "Branch and Bound" by David B. Johnson
- "Genetic Algorithms" by John H. Holland

I hope this detailed content on exhaustive search provides a comprehensive understanding of the topic.
