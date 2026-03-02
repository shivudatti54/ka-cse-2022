Of course. Here is a comprehensive educational module on Greedy Best-First Search, tailored for  Engineering students.

### **Module 3: Greedy Best-First Search (GBFS)**

#### **1. Introduction**

In the domain of Artificial Intelligence, **informed search** algorithms use problem-specific knowledge beyond the graph structure to find solutions more efficiently than uninformed searches like BFS or DFS. **Greedy Best-First Search (GBFS)** is a classic informed search strategy that employs a **heuristic function** to guide its exploration toward the goal. It is called "greedy" because it always chooses the path that *appears* to be the shortest or most promising at that very moment, without considering the overall cost incurred so far or the potential cost of the remaining path.

---

#### **2. Core Concepts & How It Works**

GBFS operates by expanding the node that is deemed to be closest to the goal, based solely on a heuristic estimate.

**a) The Heuristic Function (`h(n)`)**
The heart of GBFS is the heuristic function, denoted as `h(n)`. This function estimates the **cost of the cheapest path from node `n` to the goal**. It is problem-specific and provides an educated guess. For example:
*   In a route-finding problem (like finding the shortest path between cities), `h(n)` could be the straight-line Euclidean distance from a city to the destination.
*   In a puzzle like the 8-Puzzle, `h(n)` could be the number of misplaced tiles.

A good heuristic is **admissible** (never overestimates the true cost to the goal), though GBFS does not require this property to function.

**b) The Evaluation Function (`f(n)`)**
Unlike algorithms such as A* that combine the cost-so-far (`g(n)`) and the cost-to-go (`h(n)`), GBFS uses a simple evaluation function:
**`f(n) = h(n)`**
This means its decision is based purely on the estimated cost to the goal from the current node, ignoring the path cost taken to get there.

**c) Algorithm Steps**
GBFS typically uses a **priority queue** (often implemented with a min-heap) for its `Open` list to always select the node with the smallest `h(n)` value.

1.  **Start:** Place the starting node on the `Open` list. This list is prioritized by `h(n)`.
2.  **Loop:**
    *   If the `Open` list is empty, the search fails.
    *   Else, pop the node with the lowest `h(n)` value from the `Open` list. This is the current node.
    *   Check if this current node is the goal. If yes, return the solution.
    *   Else, expand this current node (i.e., generate all its successors).
    *   For each successor:
        *   Calculate its heuristic value `h(n)`.
        *   If it hasn't been visited, add it to the `Open` list.
3.  **Terminate:** The process repeats until the goal is found or all possibilities are exhausted.

---

#### **3. Example: Pathfinding**

Consider finding a path from **Arad (A)** to **Bucharest (B)** on a map of Romania. We use the straight-line distance (heuristic) to Bucharest.

| Node | h(n) | Node | h(n) |
| :--- | :---: | :--- | :---: |
| Arad | 366 | Sibiu | 253 |
| Zerind | 374 | Fagaras | 176 |
| Timisoara | 329 | Rimnicu Vilcea | 193 |
| ... | ... | **Bucharest** | **0** |

**Search Steps:**
1.  Start at **Arad** (`h=366`). Expand it to get successors: **Zerind** (`374`), **Sibiu** (`253`), **Timisoara** (`329`).
2.  The node with the smallest `h(n)` is **Sibiu** (`253`). Go to Sibiu.
3.  Expand **Sibiu**. Successors: **Arad** (visited), **Fagaras** (`176`), **Oradea**, **Rimnicu Vilcea** (`193`).
4.  The smallest `h(n)` in the `Open` list is now **Fagaras** (`176`). Go to Fagaras.
5.  Expand **Fagaras**. Its successor is **Bucharest** (`0`).
6.  Pop **Bucharest** from the `Open` list. Goal is found!

The path is: Arad -> Sibiu -> Fagaras -> Bucharest.

> **Note:** While this found a path, it's not the *shortest* path (which is Arad->Sibiu->Rimnicu Vilcea->Pitesti->Bucharest). This highlights a key limitation of GBFS.

---

#### **4. Characteristics, Advantages, and Disadvantages**

| Aspect | Description |
| :--- | :--- |
| **Completeness** | ❌ No. It can get stuck in infinite loops or dead-ends (e.g., on infinite graphs or graphs with cycles), as it does not consider the path cost taken. It can be made complete with a closed list to avoid revisiting states. |
| **Optimality** | ❌ No. As shown in the example, the first solution found may not be the optimal (least-cost) one because it ignores the `g(n)` cost. |
| **Time Complexity** | `O(b^m)` in the worst case, but a good heuristic can lead to a solution much faster than uninformed searches. `b` is the branching factor, `m` is the maximum depth. |
| **Space Complexity** | `O(b^m)`, as it must keep all generated nodes in memory in the worst case. |

**Advantages:**
*   **Extremely Fast:** Often finds a solution very quickly because it is aggressively guided by the heuristic.
*   **Efficient:** Much more efficient than uninformed searches in well-designed problems.

**Disadvantages:**
*   **Not Optimal:** Can easily miss the best solution.
*   **Not Complete:** Can be misled by a bad heuristic into infinite paths.
*   **Myopic:** Its greedy nature means it only sees the immediate next step, not the bigger picture.

---

#### **5. Key Points & Summary**

*   GBFS is an **informed search** algorithm that uses a heuristic function `h(n)` to guide its search.
*   Its evaluation function is **`f(n) = h(n)`**.
*   It is **greedy** by nature, always selecting the node that *seems* closest to the goal.
*   **Advantage:** It is often very fast and memory-efficient compared to brute-force methods.
*   **Major Drawbacks:** It is **neither complete nor optimal**. It can get stuck in loops and may not find the best solution.
*   It is often used as a component in more advanced algorithms (like A*) or in scenarios where finding *any* solution quickly is more important than finding the *perfect* one.