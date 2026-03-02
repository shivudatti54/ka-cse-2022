**Chapter 4: Analysis & Design of Algorithms**
**Module: BRUTE FORCE APPROACHES (continued)**
**Topic: Exhaustive Search**

# **4.1 Introduction to Exhaustive Search**

Exhaustive search is a problem-solving strategy used in algorithm design where all possible solutions are considered and evaluated to find the optimal or correct one.

**Key Concepts:**

- Exhaustive search involves systematically checking all possible solutions.
- It is often used for problems with a small number of possible solutions.
- Exhaustive search can be time-consuming and inefficient for large problem sizes.

**Definition:**
Exhaustive search is a problem-solving strategy that involves checking all possible solutions to find the optimal or correct one.

## **Types of Exhaustive Search:**

### 1. Breadth-First Search (BFS)

Breadth-First Search is a type of exhaustive search that explores all the nodes at the current level before moving to the next level.

**Example:** Finding the shortest path between two nodes in an unweighted graph using BFS.

### 2. Depth-First Search (DFS)

Depth-First Search is a type of exhaustive search that explores as far as possible along each branch before backtracking.

**Example:** Finding a path between two nodes in a graph using DFS.

### 3. Exhaustive Search with Branch and Bound

Exhaustive search with branch and bound is a type of exhaustive search that uses bounds to prune branches that cannot lead to the optimal solution.

**Example:** Solving the traveling salesman problem using exhaustive search with branch and bound.

## **Example Problem: Traveling Salesman Problem**

The traveling salesman problem is a classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the starting city.

**Problem Statement:**

Given a set of cities and their pairwise distances, find the shortest possible tour that visits each city exactly once and returns to the starting city.

**Solution:**

1.  List all possible tours.
2.  Calculate the total distance of each tour.
3.  Return the tour with the shortest total distance.

**Time Complexity:** O(n!), where n is the number of cities.

**Space Complexity:** O(n), where n is the number of cities.

## **Analysis:**

Exhaustive search is a simple and intuitive problem-solving strategy, but it can be impractical for large problem sizes due to its high time complexity.

**Advantages:**

- Exhaustive search is easy to understand and implement.
- It can be used for problems with a small number of possible solutions.

**Disadvantages:**

- Exhaustive search can be time-consuming and inefficient for large problem sizes.
- It can be impractical for problems with a large number of possible solutions.

## **Conclusion:**

Exhaustive search is a problem-solving strategy that involves checking all possible solutions to find the optimal or correct one. While it can be effective for small problem sizes, it can be impractical for large problem sizes due to its high time complexity. In the next chapter, we will explore more efficient problem-solving strategies such as dynamic programming and greedy algorithms.
