Of course. Here is a comprehensive educational explanation of Greedy Best-First Search for  Engineering students, formatted in Markdown.

# **Greedy Best-First Search (GBFS)**

**Subject:** Artificial Intelligence
**Semester:** IV
**Module:** Module 3 - Informed (Heuristic) Search Strategies

---

## **1. Introduction**

Informed search strategies use problem-specific knowledge beyond the problem definition itself to find solutions more efficiently than uninformed searches like BFS or DFS. **Greedy Best-First Search (GBFS)** is a fundamental informed search algorithm. It is called "greedy" because it always chooses the path that *appears* to be the best at that very moment, based on a heuristic estimate. It expands the node that seems closest to the goal, hoping this choice will lead to a solution quickly and with minimal cost.

## **2. Core Concepts**

### **The Heuristic Function (`h(n)`)**
The heart of GBFS is the **heuristic function**, denoted as `h(n)`. This function estimates the cost of the cheapest path from node `n` to the goal. It uses domain-specific knowledge to make an educated guess.
*   It is **admissible** if it never overestimates the true cost to the goal (a crucial property for another algorithm, A*, but not strictly required for GBFS).
*   For example, in a pathfinding problem on a map, `h(n)` is often the straight-line (Euclidean) distance from a city to the destination city.

### **How Greedy Best-First Search Works**
GBFS uses only the heuristic function `h(n)` to decide which node to expand next. It completely ignores the cost it took to reach the current node (`g(n)`). The algorithm can be summarized in these steps:

1.  **Start:** Place the start node in a priority queue (often called `OPEN`). The priority is determined by `h(n)` (lower heuristic value = higher priority).
2.  **Loop:**
    a. If the queue is empty, return failure.
    b. Pop the node with the **lowest** `h(n)` value from the queue. This is the current node.
    c. If this node is the goal, return the solution by backtracking the path.
    d. Else, expand this node (generate all its successors) and add them to the queue. Their priority is calculated based on their own `h(n)` value.
3.  **Repeat:** Continue the loop until the goal is found or all possibilities are exhausted.

### **Characteristics**
*   **Completeness:** GBFS is **not complete**. It can get stuck in infinite loops, especially if it starts going down a path that has a steadily decreasing heuristic value but no actual goal (e.g., dead ends). It can miss the optimal solution if the heuristic leads it astray.
*   **Optimality:** GBFS is **not optimal**. The greedy choice might lead to a quick solution, but it is often not the least-cost path. It sacrifices optimality for speed.
*   **Time and Space Complexity:** In the worst case, its time and space complexity is **O(b^m)**, where `b` is the branching factor and `m` is the maximum depth of the search space. However, with a good heuristic, it can be significantly faster than uninformed searches.

## **3. Example: Finding a Path on a Map**

Imagine we want to find a path from **Arad (A)** to **Bucharest (B)**. We will use the **straight-line distance** (SLD) to Bucharest as our heuristic function `h(n)`.

**Heuristic Table (h(n)):**
| Node         | h(n) |
| :----------- | :--- |
| Arad (A)     | 366  |
| Sibiu (S)    | 253  |
| Zerind (Z)   | 374  |
| Timisoara (T)| 329  |
| Fagaras (F)  | 176  |
| Rimnicu Vilcea (R) | 193 |
| Bucharest (B)| 0    |

**Search Steps:**

1.  Start at **Arad** (h=366). Expand it to get successors: **Sibiu** (h=253), **Timisoara** (h=329), **Zerind** (h=374).
2.  The node with the *lowest h(n)* is **Sibiu** (253). Pop it and expand.
3.  From Sibiu, we get **Arad** (h=366), **Fagaras** (h=176), **Oradea** (h=380), **Rimnicu Vilcea** (h=193).
4.  The node with the *lowest h(n)* in the entire queue is now **Fagaras** (176). Pop and expand it.
5.  From Fagaras, we get **Sibiu** (h=253) and **Bucharest** (h=0).
6.  The node with the *lowest h(n)* is **Bucharest** (0). We pop it, find it's the goal, and the search is successful.

**The path found is: Arad → Sibiu → Fagaras → Bucharest.**
Note: This is **not** the shortest path (which is Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest). GBFS took a "greedy" but more expensive route because Fagaras had a lower `h(n)` than Rimnicu Vilcea (176 vs. 193), leading to a suboptimal solution.

## **4. Key Points & Summary**

| **Aspect**         | **Description**                                                                                              |
| :----------------- | :----------------------------------------------------------------------------------------------------------- |
| **Principle**      | Always selects the node that appears closest to the goal based on a heuristic function `h(n)`.               |
| **Strategy**       | Uses a priority queue where nodes are ordered by increasing `h(n)`.                                          |
| **Heuristic**      | `h(n)`: Estimated cost from node `n` to the goal. Drives the entire search.                                  |
| **Completeness**   | **No**. Can get trapped in infinite loops and fail to find a solution that exists.                           |
| **Optimality**     | **No**. Often finds a solution quickly, but it is not guaranteed to be the best or cheapest one.            |
| **Complexity**     | Time and Space: O(b^m) in the worst case, but often very efficient with a good heuristic.                    |
| **Advantages**      | Often very fast and efficient in terms of the number of nodes expanded, especially with a good heuristic.     |
| **Disadvantages**   | Can make poor initial choices, is neither complete nor optimal, and is highly dependent on the heuristic quality. |

In summary, Greedy Best-First Search is a simple yet powerful strategy for informed search. Its performance is critically dependent on the choice of the heuristic function. While it is not complete or optimal, its speed and simplicity make it a useful algorithm in many scenarios, often serving as a foundation for more advanced algorithms like **A\* Search**, which combines the greedy approach with the cost-so-far to ensure optimality.