**Chapter 5: Analysis & Design of Algorithms**
**Module: BRUTE FORCE APPROACHES (continued) - Exhaustive Search**
**Topic: Chapter 5 (Section 5.1) - Exhaustive Search**

# **Exhaustive Search: A Brute Force Approach**

Exhaustive search is a brute force approach that involves checking all possible solutions to a problem. This approach is often used when the number of possible solutions is relatively small and the problem can be easily evaluated.

## **Definition**

Exhaustive search is a search algorithm that checks all possible solutions to a problem. It is also known as a brute force algorithm, because it involves trying all possible solutions, without any optimization or pruning.

## **How Exhaustive Search Works**

The exhaustive search algorithm works as follows:

1.  **Define the search space**: Identify the possible solutions to the problem.
2.  **Evaluate each solution**: Check each possible solution to determine if it is a valid solution.
3.  **Compare solutions**: Compare each valid solution to determine which one is the optimal solution.

## **Example: Traveling Salesman Problem**

The traveling salesman problem is an example of a problem that can be solved using exhaustive search. The problem is defined as follows:

- Given a list of cities and their pairwise distances, find the shortest possible tour that visits each city exactly once and returns to the starting city.

## **Pseudocode for Exhaustive Search**

Here is a pseudocode for exhaustive search:

```
function exhaustiveSearch(cities, distances, startCity):
    bestTour = null
    bestDistance = Infinity

    for i from 0 to number of cities:
        currentTour = [startCity]
        currentDistance = 0

        for j from i+1 to number of cities:
            currentTour.add(cities[j])
            currentDistance += distances[currentTour[i]][currentTour[j]]

        currentDistance += distances[currentTour[-1]][currentTour[0]]
        currentDistance += cities[0][startCity]

        if currentDistance < bestDistance:
            bestTour = currentTour
            bestDistance = currentDistance

    return bestTour
```

## **Time Complexity**

The time complexity of exhaustive search is O(n!), where n is the number of cities. This is because there are n! possible tours, and each tour must be evaluated.

## **Space Complexity**

The space complexity of exhaustive search is O(n), where n is the number of cities. This is because we need to store the current tour and the distances between cities.

## **Advantages and Disadvantages**

**Advantages:**

- Exhaustive search is guaranteed to find the optimal solution, if one exists.
- Exhaustive search is simple to implement.

**Disadvantages:**

- Exhaustive search has a high time complexity, making it impractical for large problems.
- Exhaustive search requires a lot of memory to store all possible solutions.

## **When to Use Exhaustive Search**

Exhaustive search should be used when:

- The number of possible solutions is relatively small.
- The problem can be easily evaluated.
- The optimal solution is guaranteed to exist.

## **Conclusion**

Exhaustive search is a brute force approach that involves checking all possible solutions to a problem. While it is guaranteed to find the optimal solution, if one exists, it is impractical for large problems due to its high time complexity. Exhaustive search should be used when the number of possible solutions is relatively small and the problem can be easily evaluated.
