# Introduction to Artificial Intelligence: Text Book 1, Chapter 1

=====================================================

## What is Artificial Intelligence?

---

Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence, such as:

- Learning
- Problem-solving
- Reasoning
- Perception
- Language understanding

The term "Artificial Intelligence" was coined in 1956 by John McCarthy, who organized the first AI conference at the Dartmouth Summer Research Project on Artificial Intelligence.

### Key Characteristics of AI:

- **Intelligence**: AI systems are designed to perform tasks that require human intelligence, such as learning, problem-solving, and reasoning.
- **Autonomy**: AI systems can operate independently and make decisions without human intervention.
- **Improvisation**: AI systems can adapt to new situations and learn from experience.

## Problems and Problem Spaces

---

A problem is a situation that requires a goal-oriented solution. Problem spaces are the set of possible solutions to a problem.

### Types of Problems:

- **Well-defined problems**: These are problems that have a clear and well-defined solution, such as finding a specific object in a room.
- **Ill-defined problems**: These are problems that do not have a clear or well-defined solution, such as determining the meaning of a piece of text.

### Problem Spaces:

- **Finite problem spaces**: These are problem spaces that have a finite number of possible solutions, such as a puzzle with a fixed number of pieces.
- **Infinite problem spaces**: These are problem spaces that have an infinite number of possible solutions, such as a decision-making problem with multiple possible outcomes.

## Search Methods

---

Search methods are algorithms used to find a solution to a problem by exploring the problem space.

### Types of Search Methods:

- **Breadth-First Search (BFS)**: This method explores all the possible solutions at a given depth before moving on to the next depth level.
- **Depth-First Search (DFS)**: This method explores as far as possible along each branch before backtracking.
- **Dijkstra's Algorithm**: This method is used to find the shortest path between two nodes in a graph.
- **Greedy Search**: This method makes the locally optimal choice at each step with the hope that it will lead to a global optimum solution.

### Key Concepts:

- **State**: A state is a description of the current situation or problem.
- **Actions**: Actions are the possible steps that can be taken to change the state.
- **Transitions**: Transitions are the possible outcomes of taking an action.
- **Reward**: A reward is a measure of the desirability of a particular state or transition.

Example:

Suppose we want to find a path from a starting node to a goal node in a graph. We can use Dijkstra's algorithm to find the shortest path.

### Code Example:

```python
import heapq

def dijkstra(graph, start, goal):
    # Create a priority queue to hold the nodes to be processed
    queue = []
    heapq.heappush(queue, (0, start))

    # Create a dictionary to hold the distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a dictionary to hold the previous node in the shortest path
    previous = {node: None for node in graph}

    while queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(queue)

        # If we have reached the goal, we are done
        if current_node == goal:
            break

        # Process each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If we have not processed this neighbor before, or if the new distance is smaller
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Build the shortest path
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]

    # Return the shortest path in the correct order
    return path[::-1]

# Define the graph
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 2, 'E': 1},
    'E': {'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

# Find the shortest path from A to F
path = dijkstra(graph, 'A', 'F')
print(path)
```

This code uses Dijkstra's algorithm to find the shortest path from node A to node F in the graph. The shortest path is `[A, D, E, F]`.
