# Greedy Algorithm Design

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction to Greedy Algorithms

### 1.1 What is a Greedy Algorithm?

A **greedy algorithm** is a fundamental algorithmic paradigm that builds a solution incrementally by making the **locally optimal choice** at each step, with the hope that these local optimal decisions will lead to a **globally optimal solution**. Unlike dynamic programming, which explores all possible solutions and stores intermediate results, greedy algorithms make irreversible decisions based on the current state without reconsidering previous choices.

The greedy approach is characterized by:

- **Greedy Choice Property**: A global optimal solution can be reached by making a series of locally optimal choices.
- **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems.
- **Irreversibility**: Once a choice is made, it is never reconsidered.

### 1.2 Real-World Analogy

Consider the problem of finding the shortest path while driving through a city with multiple routes. A greedy driver might always choose the road that appears shortest at the current intersection, without considering the overall route. While this doesn't always yield the globally shortest path (due to traffic, one-way streets, or road conditions), it demonstrates the greedy principle: make the best immediate choice and hope it leads to an optimal overall outcome.

In computer science, greedy algorithms are used in:

- **Network Routing**: Finding shortest paths in networks
- **Compression**: Huffman coding for data compression
- **Scheduling**: Allocating resources efficiently
- **Graph Algorithms**: Minimum spanning trees, activity selection

### 1.3 Why Greedy Algorithms Matter (Delhi University Context)

In the **Design and Analysis of Algorithms** course under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science at Delhi University, greedy algorithms form a critical pillar alongside divide-and-conquer and dynamic programming. Understanding when greedy works—and more importantly, when it fails—is essential for developing efficient algorithmic solutions in placements, competitive programming, and real-world software development.

---

## 2. Key Concepts and Design Principles

### 2.1 Greedy Choice Property

The **greedy choice property** states that a globally optimal solution can be constructed by repeatedly selecting what appears to be the best option at the moment. This property distinguishes greedy algorithms from exhaustive search approaches.

**Example**: In the Activity Selection Problem, selecting the activity that finishes earliest (and is compatible with previously selected activities) leads to an optimal solution.

### 2.2 Optimal Substructure

A problem exhibits **optimal substructure** if an optimal solution to the problem contains optimal solutions to its subproblems. This property is essential for both greedy algorithms and dynamic programming, though they exploit it differently:

- **Greedy**: Solves subproblems after making the greedy choice
- **Dynamic Programming**: Solves subproblems first, then makes the greedy choice

### 2.3 Greedy vs. Dynamic Programming

| Aspect | Greedy Algorithm | Dynamic Programming |
|--------|------------------|---------------------|
| **Approach** | Makes best choice immediately | Explores all possibilities |
| **Time Complexity** | Usually polynomial | Often exponential without memoization |
| **Optimality** | Not always optimal | Always optimal (if applicable) |
| **Subproblems** | May not overlap | Overlapping subproblems |
| **Memory** | Usually less memory | Requires DP table |

### 2.4 Steps to Design a Greedy Algorithm

1. **Characterize the optimal structure** of the problem
2. **Develop a recursive formulation** for the optimal solution
3. **Prove that at each step**, the greedy choice is safe (leads to optimal solution)
4. **Construct an iterative algorithm** based on the greedy choice
5. **Analyze the algorithm** for time and space complexity

---

## 3. Classical Greedy Algorithm Examples with Code

### 3.1 Activity Selection Problem

**Problem Statement**: Given a set of activities with start and finish times, select the maximum number of non-overlapping activities.

**Algorithm**:
1. Sort activities by their finish times
2. Select the first activity
3. For each remaining activity, select it if its start time is ≥ last selected activity's finish time

```python
def activity_selection(activities):
    """
    Activity Selection Problem using Greedy Approach
    activities: List of tuples (start, finish)
    Returns: Maximum number of non-overlapping activities
    """
    # Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Select first activity
    selected = [sorted_activities[0]]
    last_finish = sorted_activities[0][1]
    
    # Greedy selection: choose next activity that starts after last finishes
    for start, finish in sorted_activities[1:]:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    
    return selected, len(selected)


# Example usage
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
selected, count = activity_selection(activities)
print(f"Maximum activities: {count}")
print(f"Selected activities: {selected}")
```

**Time Complexity**: O(n log n) due to sorting
**Space Complexity**: O(n) for storing results

### 3.2 Fractional Knapsack Problem

**Problem Statement**: Given weights and values of items and a knapsack with capacity W, maximize the total value in the knapsack. Items can be divided (fractional).

**Algorithm**:
1. Calculate value-to-weight ratio for each item
2. Sort items by ratio in descending order
3. Fill knapsack: take full items while possible, take fraction of last item if needed

```python
def fractional_knapsack(items, capacity):
    """
    Fractional Knapsack Problem using Greedy Approach
    items: List of tuples (value, weight)
    capacity: Maximum weight capacity
    Returns: Maximum value and items selected
    """
    # Calculate value/weight ratio and sort descending
    ratios = [(value/weight, weight, value) for value, weight in items]
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    remaining_capacity = capacity
    selected = []
    
    for ratio, weight, value in ratios:
        if remaining_capacity == 0:
            break
            
        if weight <= remaining_capacity:
            # Take entire item
            total_value += value
            remaining_capacity -= weight
            selected.append((weight, value, 1.0))  # 1.0 = full item
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            selected.append((weight, value, fraction))
    
    return total_value, selected


# Example usage
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
max_value, selected_items = fractional_knapsack(items, capacity)
print(f"Maximum value: {max_value:.2f}")
print("Items selected (weight, value, fraction):")
for item in selected_items:
    print(f"  Weight: {item[0]}, Value: {item[1]}, Fraction: {item[2]:.2f}")
```

**Time Complexity**: O(n log n) due to sorting
**Space Complexity**: O(n)

### 3.3 Huffman Coding (Data Compression)

**Problem Statement**: Create an optimal prefix-free binary code for characters based on their frequencies.

**Algorithm**:
1. Build a min-heap with all characters and their frequencies
2. Extract two nodes with minimum frequency
3. Create a new internal node with frequency = sum of two nodes
4. Insert the new node back into the heap
5. Repeat until one node remains

```python
import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    """
    Huffman Coding using Greedy Approach
    Returns: Huffman codes for each character
    """
    if not text:
        return {}, {}
    
    # Step 1: Calculate frequency of each character
    frequency = Counter(text)
    
    # Step 2: Build min-heap
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Step 3: Build Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    # Step 4: Generate codes using DFS
    codes = {}
    
    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    
    root = heap[0]
    generate_codes(root, "")
    
    return codes


# Example usage
text = "this is an example for huffman encoding"
codes = huffman_coding(text)
print("Huffman Codes:")
for char, code in sorted(codes.items()):
    print(f"  '{char}': {code}")

# Encode the text
encoded = ''.join(codes[char] for char in text)
print(f"\nOriginal text: {text}")
print(f"Encoded text: {encoded}")
print(f"Original length: {len(text) * 8} bits")
print(f"Encoded length: {len(encoded)} bits")
```

**Time Complexity**: O(n log n) where n is the number of unique characters
**Space Complexity**: O(n)

### 3.4 Dijkstra's Shortest Path Algorithm

**Problem Statement**: Find the shortest path from a source vertex to all other vertices in a weighted graph with non-negative weights.

```python
import heapq

def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Greedy Approach
    graph: Adjacency list representation {vertex: [(neighbor, weight), ...]}
    source: Source vertex
    Returns: Dictionary of shortest distances
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    pq = [(0, source)]  # (distance, vertex)
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


# Example usage
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2), ('F', 6)],
    'E': [('F', 3)],
    'F': []
}

distances = dijkstra(graph, 'A')
print("Shortest distances from A:")
for vertex, dist in distances.items():
    print(f"  To {vertex}: {dist}")
```

**Time Complexity**: O((V + E) log V) using binary heap
**Space Complexity**: O(V)

---

## 4. Counterexamples: When Greedy Fails

Understanding when greedy algorithms fail is as important as knowing when they work. Here are critical examples:

### 4.1 0/1 Knapsack Problem

The 0/1 knapsack problem differs from fractional knapsack in that items cannot be divided. Greedy approach (by value/weight ratio) fails here.

**Counterexample**:
- Capacity = 50
- Items: (60, 10), (100, 20), (120, 30) — (value, weight)
- Greedy (by ratio): Select items with ratio 6, 5, 4 → Takes items 1 and 2 (weight 30, value 160)
- **Optimal**: Items 2 and 3 (weight 50, value 220)

```python
def knapsack_01_greedy(items, capacity):
    """Greedy approach - FAILS for 0/1 Knapsack"""
    ratios = [(value/weight, weight, value) for value, weight in items]
    ratios.sort(reverse=True)
    
    total_value = 0
    remaining = capacity
    
    for ratio, weight, value in ratios:
        if weight <= remaining:
            total_value += value
            remaining -= weight
    
    return total_value


def knapsack_01_dp(items, capacity):
    """Dynamic Programming - CORRECT approach"""
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight = items[i-1][1]
        value = items[i-1][0]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]


items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50

greedy_result = knapsack_01_greedy(items, capacity)
dp_result = knapsack_01_dp(items, capacity)

print(f"Greedy result: {greedy_result}")
print(f"DP result (optimal): {dp_result}")
print(f"Greedy is WRONG here!")
```

### 4.2 Coin Change Problem

For some coin denominations, greedy fails to find the minimum number of coins.

**Counterexample**:
- Coins: [1, 3, 4]
- Target: 6
- Greedy: 4 + 1 + 1 = 3 coins
- **Optimal**: 3 + 3 = 2 coins

```python
def coin_change_greedy(coins, amount):
    """Greedy approach - can fail"""
    coins_sorted = sorted(coins, reverse=True)
    count = 0
    result = []
    
    for coin in coins_sorted:
        while amount >= coin:
            amount -= coin
            count += 1
            result.append(coin)
    
    if amount == 0:
        return count, result
    return -1, []


def coin_change_dp(coins, amount):
    """Dynamic Programming - always correct"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 3, 4]
amount = 6

greedy_count, greedy_coins = coin_change_greedy(coins, amount)
dp_count = coin_change_dp(coins, amount)

print(f"Greedy: {greedy_count} coins {greedy_coins}")
print(f"DP (optimal): {dp_count} coins")
```

### 4.3 Traveling Salesman Problem (TSP)

Greedy (nearest neighbor) does not guarantee an optimal solution.

**Counterexample**:
- Four cities in a square pattern with specific distances
- Greedy may visit: A → B → C → D → A (cost 100)
- Optimal: A → B → D → C → A (cost 80)

---

## 5. Analysis of Greedy Algorithms

### 5.1 Time Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|-------------------|
| Activity Selection | O(n log n) | O(n) |
| Fractional Knapsack | O(n log n) | O(n) |
| Huffman Coding | O(n log n) | O(n) |
| Dijkstra's | O((V+E) log V) | O(V) |
| Kruskal's MST | O(E log E) | O(V) |
| Prim's MST | O(E log V) | O(V) |

### 5.2 Proving Correctness of Greedy Algorithms

To prove a greedy algorithm is correct, we typically use:

1. **Greedy Choice Property**: Show that there exists an optimal solution that makes the greedy choice first.
2. **Inductive Proof**: Show that if the greedy choice is made at each step, the remaining subproblem is of the same type and can be solved optimally.

---

## 6. Delhi University Syllabus Alignment

This study material covers the following topics from the **Design and Analysis of Algorithms** syllabus under NEP 2024 UGCF:

- ✅ Introduction to Greedy Algorithm paradigm
- ✅ Greedy Choice Property and Optimal Substructure
- ✅ Classical Greedy algorithms (Activity Selection, Knapsack, Huffman Coding, Dijkstra's)
- ✅ Analysis of time and space complexity
- ✅ Counterexamples where greedy fails
- ✅ Comparison with Dynamic Programming approach
- ✅ Practical implementations in Python

---

## 7. Multiple Choice Questions

### Section A: Theory

1. **Which of the following is NOT a property required for a greedy algorithm to find the optimal solution?**
   - (a) Greedy Choice Property
   - (b) Optimal Substructure
   - (c) Overlapping Subproblems
   - (d) None of the above

2. **The time complexity of Dijkstra's algorithm using a binary heap is:**
   - (a) O(V²)
   - (b) O(E log V)
   - (c) O((V+E) log V)
   - (d) O(V log E)

3. **In the Activity Selection Problem, activities are sorted by:**
   - (a) Start time
   - (b) Finish time
   - (c) Duration
   - (d) Value

4. **Huffman coding uses which data structure?**
   - (a) Stack
   - (b) Queue
   - (c) Min-Heap
   - (d) Binary Search Tree

5. **Which of the following problems can be solved optimally using a greedy approach?**
   - (a) 0/1 Knapsack
   - (b) Fractional Knapsack
   - (c) Traveling Salesman
   - (d) Subset Sum

### Section B: Analysis

6. **What is the time complexity of sorting n activities by finish time?**
   - (a) O(n)
   - (b) O(n log n)
   - (c) O(log n)
   - (d) O(n²)

7. **In Fractional Knapsack, after sorting by value/weight ratio, what is the approach?**
   - (a) Select items with lowest ratio first
   - (b) Select items with highest ratio first
   - (c) Select items randomly
   - (d) Select items by weight

8. **Kruskal's algorithm for MST uses:**
   - (a) BFS
   - (b) DFS
   - (c) Union-Find
   - (d) Priority Queue

9. **Greedy algorithm for coin change works correctly for which coin system?**
   - (a) {1, 3, 4}
   - (b) {1, 3, 7}
   - (c) {1, 5, 10, 25}
   - (d) All of the above

10. **Which property states that an optimal solution contains optimal solutions to subproblems?**
    - (a) Greedy Choice Property
    - (b) Optimal Substructure
    - (c) Optimal Overlap
    - (d) None

### Section C: Code & Application

11. **In Huffman coding, when two nodes are combined, the new node's frequency is:**
    - (a) Maximum of two frequencies
    - (b) Minimum of two frequencies
    - (c) Sum of two frequencies
    - (d) Average of two frequencies

12. **Dijkstra's algorithm fails when:**
    - (a) Graph is connected
    - (b) Weights are negative
    - (c) Graph is directed
    - (d) Graph has cycles

13. **The main difference between Prim's and Kruskal's MST algorithms is:**
    - (a) Time complexity
    - (b) Approach (vertex-based vs edge-based)
    - (c) Both (a) and (b)
    - (d) None

14. **In the Activity Selection Problem, after selecting an activity, the next activity must have:**
    - (a) Start time ≥ last finish time
    - (b) Finish time ≤ last start time
    - (c) Any start time
    - (d) Start time = last finish time

15. **Which algorithm is used for finding shortest path with non-negative weights?**
    - (a) Bellman-Ford
    - (b) Floyd-Warshall
    - (c) Dijkstra's
    - (d) BFS (unweighted)

### Section D: Advanced

16. **Prim's algorithm resembles which data structure's traversal?**
    - (a) DFS
    - (b) BFS
    - (c) Level-order
    - (d) Inorder

17. **The space complexity of storing Huffman tree is:**
    - (a) O(1)
    - (b) O(log n)
    - (c) O(n)
    - (d) O(n log n)

18. **For which case does the greedy algorithm always work for coin change?**
    - (a) Any coin system
    - (b) Canonical coin systems
    - (c) No coin system
    - (d) Only US coins

19. **Greedy algorithms are examples of:**
    - (a) Divide and Conquer
    - (b) Dynamic Programming
    - (c) Both
    - (d) Neither

20. **The fractional knapsack problem has time complexity:**
    - (a) O(nW)
    - (b) O(n log n)
    - (c) O(n²)
    - (d) O(2ⁿ)

---

## 8. Flashcards for Quick Review

### Flashcard Set 1: Key Concepts

| # | Term/Concept | Answer |
|---|--------------|--------|
| 1 | Greedy Algorithm | Algorithm that makes locally optimal choices hoping for global optimum |
| 2 | Greedy Choice Property | Property that global optimal solution can be reached by making locally optimal choices |
| 3 | Optimal Substructure | When optimal solution contains optimal solutions to subproblems |
| 4 | Greedy vs DP | Greedy makes choice first; DP solves subproblems first |
| 5 | Activity Selection | Select maximum non-overlapping activities sorted by finish time |

### Flashcard Set 2: Algorithms

| # | Algorithm | Key Point |
|---|-----------|-----------|
| 6 | Dijkstra's | Finds shortest path, fails with negative weights |
| 7 | Huffman Coding | Data compression using min-heap, prefix-free codes |
| 8 | Kruskal's MST | Edge-based, uses Union-Find, sorts edges |
| 9 | Prim's MST | Vertex-based, grows one tree, uses priority queue |
| 10 | Fractional Knapsack | Greedy by value/weight ratio works optimally |

### Flashcard Set 3: Failure Cases

| # | Problem | Why Greedy Fails |
|---|---------|------------------|
| 11 | 0/1 Knapsack | Cannot take fractions; greedy by ratio not optimal |
| 12 | Coin Change {1,3,4} | Greedy gives 3 coins (4+1+1), optimal is 2 (3+3) |
| 13 | TSP | Nearest neighbor doesn't guarantee optimal tour |
| 14 | Vertex Cover | Greedy may not find minimum vertex cover |
| 15 | Scheduling with Deadlines | Simple greedy may miss optimal schedule |

### Flashcard Set 4: Complexity

| # | Algorithm | Time | Space |
|---|-----------|------|-------|
| 16 | Activity Selection | O(n log n) | O(n) |
| 17 | Fractional Knapsack | O(n log n) | O(n) |
| 18 | Huffman Coding | O(n log n) | O(n) |
| 19 | Dijkstra (Binary Heap) | O((V+E) log V) | O(V) |
| 20 | Kruskal's MST | O(E log E) | O(V) |

### Flashcard Set 5: Real-World Applications

| # | Application | Greedy Algorithm Used |
|---|-------------|----------------------|
| 21 | GPS Navigation | Dijkstra's / A* |
| 22 | File Compression | Huffman Coding |
| 23 | Network Broadcasting | Prim's / Kruskal's |
| 24 | Event Scheduling | Activity Selection |
| 25 | Resource Allocation | Fractional Knapsack |

---

## 9. Long Answer Questions (University Level)

### Question 1 (10 Marks)

**Define the greedy algorithm paradigm. Explain the two key properties required for a problem to be solved using the greedy approach. Also, distinguish between the greedy approach and dynamic programming with respect to how they handle subproblems.**

### Question 2 (15 Marks)

**Explain the Activity Selection Problem. Write a Python algorithm to solve it using the greedy approach. Prove that your greedy algorithm always produces an optimal solution. Analyze its time and space complexity.**

### Question 3 (15 Marks)

**Discuss the Fractional Knapsack problem in detail. Explain why the greedy approach works for Fractional Knapsack but fails for 0/1 Knapsack. Provide counterexamples to justify your answer.**

### Question 4 (10 Marks)

**What is Huffman Coding? Explain the greedy algorithm used in Huffman coding. Discuss how it achieves data compression and analyze its complexity.**

### Question 5 (15 Marks)

**Write a detailed note on counterexamples where greedy algorithms fail. Discuss at least three problems where greedy approach does not yield optimal solution and explain the reasons for failure.**

### Question 6 (10 Marks)

**Compare and contrast Prim's and Kruskal's algorithms for finding Minimum Spanning Tree. Under what circumstances would you prefer one over the other?**

### Question 7 (15 Marks)

**Explain Dijkstra's algorithm for single-source shortest path problem. Why does Dijkstra's algorithm fail when negative edge weights are present? Write the algorithm and analyze its complexity when implemented using a binary heap.**

---

## 10. Key Takeaways

### Core Concepts
- ✅ **Greedy algorithms** make locally optimal choices at each step, hoping for global optimality
- ✅ Two essential properties: **Greedy Choice Property** and **Optimal Substructure**
- ✅ Unlike DP, greedy doesn't reconsider previous decisions

### Where Greedy Works
- ✅ **Activity Selection**: Sort by finish time, pick compatible activities
- ✅ **Fractional Knapsack**: Sort by value/weight ratio, take items greedily
- ✅ **Huffman Coding**: Build tree by repeatedly combining minimum frequency nodes
- ✅ **Dijkstra's Algorithm**: Use priority queue to always expand closest vertex
- ✅ **MST (Kruskal's & Prim's)**: Greedily add minimum weight edges

### Where Greedy Fails
- ❌ **0/1 Knapsack**: Requires DP due to indivisibility
- ❌ **Coin Change**: Greedy fails for non-canonical systems
- ❌ **Traveling Salesman**: NP-hard problem, no known polynomial greedy solution
- ❌ **Vertex Cover**: Requires more sophisticated approaches
- ❌ **Negative Weights**: Dijkstra fails; use Bellman-Ford instead

### Complexity Summary
- Most greedy algorithms have **O(n log n)** time complexity
- Sorting is often the dominant operation
- Space complexity typically **O(n)** for most algorithms

### Practical Applications
- Network routing protocols
- Data compression (Huffman, JPEG)
- Resource allocation and scheduling
- Graph algorithms (MST, shortest path)
- Cryptocurrency (transaction fees)

---

*This comprehensive study material covers all essential concepts of Greedy Algorithm Design for BSc (Hons) Computer Science students at Delhi University, aligned with the NEP 2024 UGCF curriculum.*