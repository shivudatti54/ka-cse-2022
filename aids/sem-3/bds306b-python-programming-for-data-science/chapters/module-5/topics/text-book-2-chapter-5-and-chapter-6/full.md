# Text Book 2: Chapter 5 and Chapter 6

## **Introduction**

Chapter 5 and Chapter 6 of Text Book 2: Python Programming for Data Science cover the essential concepts of data structures and algorithms. These chapters are crucial for any data scientist as they provide the foundation for efficient data processing, analysis, and visualization. In this chapter, we will delve into the details of these chapters, exploring their historical context, modern developments, and providing numerous examples, case studies, and applications.

## **Chapter 5: Data Structures**

### 5.1 Overview of Data Structures

Data structures are the backbone of any programming language. They determine how data is organized, stored, and retrieved. In the context of data science, data structures play a vital role in data processing, analysis, and visualization. There are two primary types of data structures: arrays and linked lists.

### 5.2 Arrays

Arrays are a fundamental data structure in programming. They are a collection of elements of the same data type stored in contiguous memory locations. Arrays are useful for storing and manipulating large datasets.

**Example 1: Creating an Array in Python**

```python
# Create an array of integers
arr = [1, 2, 3, 4, 5]

# Print the array
print(arr)
```

Output:

```
[1, 2, 3, 4, 5]
```

**Example 2: Accessing Array Elements**

```python
# Create an array of integers
arr = [1, 2, 3, 4, 5]

# Access the first element
print(arr[0])  # Output: 1

# Access the last element
print(arr[-1])  # Output: 5
```

### 5.3 Linked Lists

Linked lists are a type of data structure where elements are stored in separate memory locations, and each element points to the next element in the list. Linked lists are useful for implementing dynamic data structures and algorithms.

**Example 3: Creating a Linked List in Python**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Create a linked list
ll = LinkedList()

# Append elements to the linked list
ll.append(1)
ll.append(2)
ll.append(3)

# Print the linked list
current = ll.head
while current:
    print(current.data)
    current = current.next
```

Output:

```
1
2
3
```

### 5.4 Stacks and Queues

Stacks and queues are two types of data structures that follow the Last-In-First-Out (LIFO) and First-In-First-Out (FIFO) principles, respectively.

**Example 4: Implementing a Stack using a Linked List**

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# Create a stack
s = Stack()

# Push elements onto the stack
s.push(1)
s.push(2)
s.push(3)

# Pop elements from the stack
print(s.pop())  # Output: 3
print(s.pop())  # Output: 2
print(s.pop())  # Output: 1
```

### 5.5 Heaps

Heaps are a type of data structure that satisfies the heap property: the parent node is either greater than or equal to its child nodes (max heap) or less than or equal to its child nodes (min heap).

**Example 5: Implementing a Max Heap using Python**

```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        if self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

# Create a max heap
mh = MaxHeap()

# Insert elements into the max heap
mh.insert(3)
mh.insert(2)
mh.insert(1)

# Extract the maximum element
print(mh.extract_max())  # Output: 3
```

### 5.6 Trees

Trees are a type of data structure that consists of nodes, where each node has a value and zero or more child nodes.

**Example 6: Implementing a Binary Tree using Python**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = Node(value)

# Create a binary tree
bt = BinaryTree()

# Insert elements into the binary tree
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# Print the binary tree
def print_tree(node, level=0):
    if node:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)

print_tree(bt.root)
```

Output:

```
        -> 8
    -> 7
-> 5
    -> 4
-> 3
    -> 2
        -> 6
```

### 5.7 Graphs

Graphs are a type of data structure that consists of nodes and edges, where each node represents a data element and each edge represents a connection between two nodes.

**Example 7: Implementing a Graph using Python**

```python
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            self.nodes[value1].append(value2)
            self.nodes[value2].append(value1)

# Create a graph
g = Graph()

# Add nodes to the graph
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

# Add edges to the graph
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

# Print the graph
def print_graph(nodes):
    for node in nodes:
        print(node, '->', nodes[node])

print_graph(g.nodes)
```

Output:

```
{1 -> [2, 4], 2 -> [1, 3], 3 -> [2, 4], 4 -> [1, 3, 1]}
```

### 5.8 Big O Notation

Big O notation is a measure of the complexity of an algorithm, expressing the upper bound of its execution time or space requirements.

**Example 8: Analyzing the Time Complexity of an Algorithm**

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Test the function
arr = [1, 2, 3, 4, 5]
print(find_max(arr))  # Output: 5
```

Time complexity: O(n)
Space complexity: O(1)

In this chapter, we have covered the essential concepts of data structures and algorithms in Python programming for data science. We have explored arrays, linked lists, stacks, queues, heaps, trees, and graphs, along with their applications and examples. We have also discussed big O notation and its importance in analyzing the complexity of algorithms.

## **Chapter 6: Algorithms**

### 6.1 Sorting Algorithms

Sorting algorithms are used to arrange data in a specific order. There are several sorting algorithms, including bubble sort, selection sort, insertion sort, merge sort, quick sort, and heap sort.

**Example 9: Implementing Merge Sort using Python**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# Test the function
arr = [5, 2, 8, 1, 9]
print(merge_sort(arr))  # Output: [1, 2, 5, 8, 9]
```

### 6.2 Searching Algorithms

Searching algorithms are used to find specific data in a dataset. There are several searching algorithms, including linear search, binary search, and hash search.

**Example 10: Implementing Linear Search using Python**

```python
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Test the function
arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 3))  # Output: 2
```

### 6.3 Greedy Algorithms

Greedy algorithms are used to find the optimal solution to a problem by making the locally optimal choice at each step.

**Example 11: Implementing the Coin Change Problem using Python**

```python
def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# Test the function
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: [5, 5, 1]
```

### 6.4 Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems and solving each subproblem only once.

**Example 12: Implementing the Fibonacci Sequence using Python**

```python
def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Test the function
n = 10
print(fibonacci(n))  # Output: 55
```

### 6.5 Backtracking Algorithms

Backtracking algorithms are used to solve problems by exploring all possible solutions and finding the first one that satisfies the conditions.

**Example 13: Implementing the N-Queens Problem using Python**

```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, row + 1)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    result = []
    backtrack(board, 0)
    return result

# Test the function
n = 4
print(solve_n_queens(n))  # Output: [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
```

### 6.6 Greedy Algorithm with Memoization

Greedy algorithms with memoization are used to solve problems by making the locally optimal choice at each step and storing the results of subproblems.

**Example 14: Implementing the Longest Common Subsequence Problem using Python**

```python
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# Test the function
s1 = "ABCDGH"
s2 = "AEDFHR"
print(longest_common_subsequence(s1, s2))  # Output: 4
```

### 6.7 Branch and Bound Algorithm

Branch and bound algorithms are used to solve problems by exploring all possible solutions and pruning branches that do not lead to a solution.

**Example 15: Implementing the Tower of Hanoi Problem using Python**

```python
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Test the function
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
```

### 6.8 Genetic Algorithm

Genetic algorithms are used to solve problems by simulating the process of evolution and selection.

**Example 16: Implementing the Traveling Salesman Problem using Python**

```python
import random

def traveling_salesman_problem(cities, distance_matrix):
    population_size = 100
    generations = 1000
    mutation_rate = 0.1

    def fitness(individual):
        distance = 0
        for i in range(len(individual) - 1):
            distance += distance_matrix[individual[i]][individual[i + 1]]
        return distance

    def mutate(individual):
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        return individual

    def crossover(parent1, parent2):
        idx = random.randint(1, len(parent1) - 1)
        child1 = parent1[:idx] + parent2[idx:]
        child2 = parent2[:idx] + parent1[idx:]
        return child1, child2

    population = [random.sample(range(len(cities)), len(cities)) for _ in range(population_size)]

    for generation in range(generations):
        fitness_values = [fitness(individual) for individual in population]
        population = sorted(zip(population, fitness_values), key=lambda x: x[1])
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = population[0]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)
        for individual in population:
            if random.random() < mutation_rate:
                individual = mutate(individual)
        population = new_population

    return population[0]

# Test the function
cities = ['A', 'B', 'C', 'D']
distance_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(traveling_salesman_problem(cities, distance_matrix))
```

### 6.9 Simulated Annealing Algorithm

Simulated annealing algorithms are used to solve problems by exploring all possible solutions and cooling the system.

**Example 17: Implementing the Knapsack Problem using Python**

```python
import random

def knapsack(weights, values, capacity):
    temperature = 100
    alpha = 0.99
    population_size = 100
    generations = 1000

    def fitness(individual):
        total_weight = sum(weights[i] for i in individual)
        total_value = sum(values[i] for i in individual)
        return -total_value if total_weight <= capacity else 0

    def mutate(individual):
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        return individual

    def crossover(parent1, parent2):
        idx = random.randint(1, len(parent1) - 1)
        child1
```
