# THE GREEDY METHOD: Prim’s Algorithm, Kruskal’s Algorithm, Dijkstra’s Algorithm, Huffman Trees and Codes

=====================================================

## Introduction

---

The greedy method is a popular approach in algorithms and computer science. It involves making the locally optimal choice at each stage, with the hope that these local choices will lead to a globally optimal solution. In this section, we will explore five classic examples of the greedy method: Prim's Algorithm, Kruskal's Algorithm, Dijkstra's Algorithm, Huffman Trees and Codes.

## Historical Context

---

The concept of the greedy method has been around for centuries. The ancient Greeks and Romans used a similar approach to solve problems. However, the modern version of the greedy method was first introduced by Edsger W. Dijkstra in the 1950s. Dijkstra's Algorithm, which is one of the most famous examples of the greedy method, was first published in 1959.

## Prim’s Algorithm

---

Prim's Algorithm is a greedy method used to find the minimum spanning tree of a graph. It works by selecting the minimum-weight edge that connects a new node to the existing tree.

### How it Works

1.  Start with an empty tree and a set of unvisited nodes.
2.  Select the minimum-weight edge that connects a new node to the existing tree.
3.  Add the new node and edge to the tree.
4.  Repeat steps 2-3 until all nodes are visited.

### Example

Suppose we have a graph with five nodes (A, B, C, D, E) and six edges:

- AB (weight 2)
- BC (weight 3)
- CD (weight 1)
- DE (weight 4)
- AC (weight 2)
- CE (weight 5)

We start with an empty tree and select the minimum-weight edge AB (weight 2). We add node A to the tree and select the minimum-weight edge CD (weight 1). We add node C to the tree and select the minimum-weight edge BC (weight 3). We add node B to the tree and select the minimum-weight edge AC (weight 2). We add node A to the tree again and select the minimum-weight edge DE (weight 4). We add node E to the tree.

The resulting minimum spanning tree is:

- AB (weight 2)
- CD (weight 1)
- BC (weight 3)
- AC (weight 2)
- DE (weight 4)

### Code

```python
import sys

def prim(graph):
    # Initialize the tree and visited nodes
    tree = []
    visited = set()

    # Select the minimum-weight edge
    min_weight = sys.maxsize
    min_edge = None

    while len(visited) < len(graph):
        # Find the minimum-weight edge
        for edge in graph:
            if edge[0] not in visited and edge[1] not in visited and edge[2] < min_weight:
                min_weight = edge[2]
                min_edge = edge

        # Add the new node and edge to the tree
        tree.append(min_edge)
        visited.add(min_edge[0])
        visited.add(min_edge[1])

    return tree

# Example graph
graph = [
    ('A', 'B', 2),
    ('B', 'C', 3),
    ('C', 'D', 1),
    ('D', 'E', 4),
    ('A', 'C', 2),
    ('C', 'E', 5)
]

# Run Prim's Algorithm
tree = prim(graph)
print(tree)
```

## Kruskal’s Algorithm

---

Kruskal's Algorithm is another greedy method used to find the minimum spanning tree of a graph. It works by selecting the minimum-weight edge that connects two nodes that are not yet connected.

### How it Works

1.  Start with an empty tree and a set of unvisited nodes.
2.  Select the minimum-weight edge that connects two nodes that are not yet connected.
3.  Add the new edge to the tree.
4.  Repeat steps 2-3 until all nodes are visited.

### Example

Suppose we have a graph with five nodes (A, B, C, D, E) and six edges:

- AB (weight 2)
- BC (weight 3)
- CD (weight 1)
- DE (weight 4)
- AC (weight 2)
- CE (weight 5)

We start with an empty tree and select the minimum-weight edge CD (weight 1). We add node C to the tree and select the minimum-weight edge BC (weight 3). We add node B to the tree and select the minimum-weight edge AB (weight 2). We add node A to the tree and select the minimum-weight edge AC (weight 2). We add node A to the tree again and select the minimum-weight edge DE (weight 4). We add node E to the tree.

The resulting minimum spanning tree is:

- CD (weight 1)
- BC (weight 3)
- AB (weight 2)
- AC (weight 2)
- DE (weight 4)

### Code

```python
import sys

def kruskal(graph):
    # Initialize the tree and visited nodes
    tree = []
    visited = set()

    # Sort the edges by weight
    graph.sort(key=lambda x: x[2])

    # Select the minimum-weight edge
    min_weight = sys.maxsize
    min_edge = None

    while len(visited) < len(graph):
        # Find the minimum-weight edge
        for edge in graph:
            if edge[0] not in visited and edge[1] not in visited and edge[2] < min_weight:
                min_weight = edge[2]
                min_edge = edge

        # Add the new node and edge to the tree
        tree.append(min_edge)
        visited.add(min_edge[0])
        visited.add(min_edge[1])

    return tree

# Example graph
graph = [
    ('A', 'B', 2),
    ('B', 'C', 3),
    ('C', 'D', 1),
    ('D', 'E', 4),
    ('A', 'C', 2),
    ('C', 'E', 5)
]

# Run Kruskal's Algorithm
tree = kruskal(graph)
print(tree)
```

## Dijkstra’s Algorithm

---

Dijkstra's Algorithm is a greedy method used to find the shortest path between two nodes in a graph. It works by selecting the minimum-weight edge that leads to an unvisited node.

### How it Works

1.  Start with the source node and a set of unvisited nodes.
2.  Select the minimum-weight edge that leads to an unvisited node.
3.  Update the distance of the new node.
4.  Mark the new node as visited.
5.  Repeat steps 2-4 until all nodes are visited.

### Example

Suppose we have a graph with five nodes (A, B, C, D, E) and six edges:

- AB (weight 2)
- BC (weight 3)
- CD (weight 1)
- DE (weight 4)
- AC (weight 2)
- CE (weight 5)

We start with node A and select the minimum-weight edge AB (weight 2). We update the distance of node B to 2. We mark node B as visited and select the minimum-weight edge BC (weight 3). We update the distance of node C to 5. We mark node C as visited and select the minimum-weight edge CD (weight 1). We update the distance of node D to 6. We mark node D as visited and select the minimum-weight edge AC (weight 2). We update the distance of node A to 2 and node C to 5. We mark node C as visited and select the minimum-weight edge CE (weight 5). We update the distance of node E to 7.

The resulting shortest path from node A to node E is:

- A -> B (weight 2)
- B -> C (weight 3)
- C -> D (weight 1)
- D -> E (weight 4)

### Code

```python
import sys

def dijkstra(graph, source):
    # Initialize the distance and previous node
    distance = {node: sys.maxsize for node in graph}
    previous = {node: None for node in graph}

    # Set the distance of the source node to 0
    distance[source] = 0

    # Select the minimum-weight edge
    min_weight = sys.maxsize
    min_edge = None

    while min_weight > 0:
        # Find the minimum-weight edge
        for edge in graph:
            if edge[0] == source and distance[edge[0]] + edge[2] < distance[edge[1]]:
                min_weight = distance[edge[0]] + edge[2]
                min_edge = edge

        # Update the distance and previous node
        distance[min_edge[1]] = min_weight
        previous[min_edge[1]] = min_edge[0]

        # Mark the new node as visited
        source = min_edge[1]

    return distance, previous

# Example graph
graph = [
    ('A', 'B', 2),
    ('B', 'C', 3),
    ('C', 'D', 1),
    ('D', 'E', 4),
    ('A', 'C', 2),
    ('C', 'E', 5)
]

# Run Dijkstra's Algorithm
distance, previous = dijkstra(graph, 'A')
print("Distance:", distance)
print("Previous:", previous)
```

## Huffman Trees and Codes

---

Huffman Trees and Codes are a type of Huffman Coding, which is a method of compressing binary data using variable-length codes. The goal of Huffman Coding is to assign shorter codes to more frequently occurring symbols.

### How it Works

1.  Create a priority queue to store the symbols and their frequencies.
2.  Merge the two symbols with the lowest frequencies and create a new node with the combined frequency.
3.  Remove the new node from the priority queue and add it to the Huffman Tree.
4.  Repeat steps 2-3 until all symbols are added to the Huffman Tree.
5.  Traverse the Huffman Tree and assign variable-length codes to each symbol based on its position in the tree.

### Example

Suppose we have a set of binary symbols with their frequencies:

- 0 (weight 2)
- 1 (weight 3)
- 00 (weight 4)
- 11 (weight 5)
- 10 (weight 1)
- 01 (weight 2)

We start by creating a priority queue with the symbols and their frequencies:

| Symbol | Frequency |
| ------ | --------- |
| 0      | 2         |
| 1      | 3         |
| 00     | 4         |
| 11     | 5         |
| 10     | 1         |
| 01     | 2         |

We merge the symbols with the lowest frequencies, 10 and 01, and create a new node with a combined frequency of 3.

| Symbol | Frequency |
| ------ | --------- |
| 0      | 2         |
| 1      | 3         |
| 00     | 4         |
| 11     | 5         |
| 10     | 3         |
| 01     | 3         |

We add the new node to the Huffman Tree and remove it from the priority queue.

| Symbol | Frequency |
| ------ | --------- |
| 0      | 2         |
| 1      | 3         |
| 00     | 4         |
| 11     | 5         |
| 10     | 3         |
| 01     | 3         |

We repeat the process until all symbols are added to the Huffman Tree:

| Symbol | Frequency |
| ------ | --------- |
| 0      | 3         |
| 1      | 4         |
| 00     | 5         |
| 11     | 6         |
| 10     | 3         |
| 01     | 3         |

We traverse the Huffman Tree and assign variable-length codes to each symbol based on its position in the tree.

| Symbol | Code |
| ------ | ---- |
| 0      | 00   |
| 1      | 01   |
| 00     | 100  |
| 11     | 110  |
| 10     | 10   |
| 01     | 11   |

The resulting Huffman Codes are:

- 0: 00 (weight 2)
- 1: 01 (weight 3)
- 00: 100 (weight 4)
- 11: 110 (weight 5)
- 10: 10 (weight 1)
- 01: 11 (weight 2)

### Code

```python
import heapq

class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

class HuffmanCoder:
    def __init__(self, symbols):
        self.symbols = symbols

    def build_tree(self):
        # Create a priority queue to store the symbols and their frequencies
        priority_queue = []
        for symbol in self.symbols:
            node = Node(symbol, self.symbols[symbol])
            heapq.heappush(priority_queue, (node.frequency, node))

        # Merge the two symbols with the lowest frequencies
        while len(priority_queue) > 1:
            frequency1 = heapq.heappop(priority_queue)[0]
            frequency2 = heapq.heappop(priority_queue)[0]
            node = Node(None, frequency1 + frequency2)
            node.left = priority_queue[0]
            node.right = priority_queue[1]
            heapq.heappush(priority_queue, (node.frequency, node))

        return priority_queue[0]

    def traverse_tree(self, node, code):
        # Traverse the Huffman Tree and assign variable-length codes to each symbol
        if node.symbol is not None:
            self.symbols[node.symbol] = code
        else:
            self.traverse_tree(node.left, code + '0')
            self.traverse_tree(node.right, code + '1')

# Example symbols
symbols = {
    '0': 2,
    '1': 3,
    '00': 4,
    '11': 5,
    '10': 1,
    '01': 2
}

# Run Huffman Coding
coder = HuffmanCoder(symbols)
tree = coder.build_tree()
coder.traverse_tree(tree, '')
print("Huffman Codes:", symbols)
```

## Further Reading

---

- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms) by Thomas H. Cormen
- [Algorithms](https://www.geeksforgeeks.org/algorithms/) by GeeksforGeeks
- [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding) by Wikipedia
- [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) by Wikipedia
- [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) by Wikipedia
- [Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) by Wikipedia
