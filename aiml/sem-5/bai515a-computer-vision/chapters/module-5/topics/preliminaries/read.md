# Network Basics and Preliminaries

## Introduction to Social Network Analysis (SNA)

Social Network Analysis (SNA) is the methodological approach that examines the structure of relationships between social entities. These entities can be individuals, groups, organizations, computers, URLs, or any other unit that can be connected through meaningful relationships. SNA provides both a visual and a mathematical analysis of human and digital connections.

**Core Principle:** The central theme in SNA is that the **pattern of connections** matters. An individual's position within a network, and the overall shape of the network itself, significantly influence outcomes like information flow, influence, innovation, and access to resources.

### Three Levels of Analysis

SNA operates at three distinct but interconnected levels:

1.  **Micro Level (The Node/Ego Level):** This level focuses on individual actors (nodes) and their immediate connections (their ego network). Analysis here concerns concepts like **centrality**, which measures a node's importance or influence based on its position.
    *   *Example:* Analyzing which employee in a company is the best-connected information broker.

2.  **Meso Level (The Group Level):** This level examines the substructures within a network, particularly the formation of **communities** or clusters where nodes are more densely connected to each other than to nodes outside the group.
    *   *Example:* Identifying cliques in a school or departments within an organization.

3.  **Macro Level (The Network Level):** This "bird's-eye view" analyzes the properties of the network as a whole. This includes metrics like **density**, **diameter**, and **assortativity**.
    *   *Example:* Measuring how quickly a rumor could spread through an entire online social network.

## Fundamental Network Concepts and Terminology

To analyze networks, we must first understand their basic building blocks and how to represent them mathematically.

### 1. What is a Network?

A network is a collection of points joined by lines. In formal terms:
*   **Nodes (or Vertices):** The fundamental units or entities in the network. Represented by the set `V`. A single node is denoted as `v_i`.
*   **Edges (or Links or Ties):** The connections or relationships between nodes. Represented by the set `E`. An edge between node `v_i` and `v_j` is denoted as `e_ij`.

A network is defined as a graph `G = (V, E)`.

### 2. Types of Networks

Networks can be classified based on their fundamental properties.

#### Directed vs. Undirected Networks

| Feature | Undirected Network | Directed Network (Digraph) |
| :--- | :--- | :--- |
| **Edges Represent** | Symmetric relationships (e.g., friendship, collaboration) | Asymmetric relationships (e.g., follows, owes money) |
| **Edge Notation** | `e_ij` is the same as `e_ji` | `e_ij` is distinct from `e_ji` |
| **Visual Cue** | Lines without arrows | Lines with arrows indicating direction |
| **Example** | Facebook friendship (mutual) | Twitter follow (one-way) |

**ASCII Diagram:**
```
Undirected:           Directed:
A -- B               A --> B
 \  /                 \    ^
   C                   v  /
                     C --> D
```

#### Weighted vs. Unweighted Networks

| Feature | Unweighted Network | Weighted Network |
| :--- | :--- | :--- |
| **Edges Represent** | Presence or absence of a connection | Strength, capacity, or intensity of a connection |
| **Edge Value** | Typically 1 (exists) or 0 (doesn't exist) | A numerical value (e.g., 5, 0.7, -2) |
| **Example** | "Are they friends? (Yes/No)" | "How many times did they communicate this month?" |

#### Other Important Types

*   **Signed Networks:** Edges have positive or negative weights, often representing friend/enemy or trust/distrust relationships.
*   **Multiplex Networks:** Multiple types of relationships exist between the same set of nodes (e.g., one network for friendships, another for advice-seeking).
*   **Bipartite Networks:** Networks with two distinct types of nodes, and edges only exist between nodes of different types (e.g., users and movies; actors and films).

### 3. Key Network Properties and Measures

#### Node-Level Properties

*   **Degree:** The number of connections a node has.
    *   In an **undirected network**, degree `k_i` of node `i` is simply the count of its edges.
    *   In a **directed network**, we have:
        *   **In-Degree (`k_i^in`)**: Number of edges pointing *towards* the node (popularity).
        *   **Out-Degree (`k_i^out`)**: Number of edges pointing *away from* the node (gregariousness).
    *   *Example:* In a Twitter network, a user's in-degree is their number of followers, and their out-degree is their number of follows.

*   **Neighborhood:** The set of nodes directly connected to a given node.

#### Network-Level Properties

*   **Network Size (N):** The total number of nodes in the network, `|V|`.

*   **Number of Edges (M):** The total number of edges in the network, `|E|`.

*   **Density:** The proportion of actual edges to the maximum possible number of edges. It measures how close the network is to being complete.
    *   **For Undirected Networks:** `Density = (2 * M) / (N * (N - 1))`
    *   **For Directed Networks:** `Density = M / (N * (N - 1))`
    *   *Interpretation:* Ranges from 0 (no connections) to 1 (everyone is connected to everyone). Real-world networks are often sparse (low density).

*   **Path:** A sequence of nodes where each consecutive pair is connected by an edge.
    *   **Shortest Path (Geodesic Path):** The path with the minimum number of edges between two nodes. The length of this path is the **distance** between the nodes.

*   **Diameter:** The longest shortest path in the entire network. It is the maximum distance between any two nodes. A small diameter is a hallmark of "small-world" networks.

*   **Components:** A connected subgraph where any two nodes are connected by a path, and no other nodes can be added while preserving this property.
    *   **Giant Component:** If a network has a component that contains a significant fraction (e.g., majority) of all nodes.

### 4. Representing Networks: The Adjacency Matrix

Networks can be represented mathematically using an **adjacency matrix**. This is a square `N x N` matrix `A`, where the element `A_ij` represents the connection from node `i` to node `j`.

**Rules for the adjacency matrix `A`:**
*   **For Unweighted, Undirected Networks:**
    *   `A_ij = 1` if an edge exists between `i` and `j`.
    *   `A_ij = 0` if no edge exists.
    *   The matrix is **symmetric** (`A_ij = A_ji`).
*   **For Unweighted, Directed Networks:**
    *   `A_ij = 1` if an edge exists *from* `i` *to* `j`.
    *   `A_ij = 0` if no edge exists.
    *   The matrix is **not necessarily symmetric**.
*   **For Weighted Networks:**
    *   `A_ij` takes the value of the weight of the edge from `i` to `j`.
    *   `A_ij = 0` implies no edge.

**Example:**
Consider an undirected network with nodes {A, B, C} and edges A-B and B-C.
The adjacency matrix (ordering A, B, C) is:
```
    A  B  C
A [ 0, 1, 0 ]
B [ 1, 0, 1 ]
C [ 0, 1, 0 ]
```

### 5. Practical Applications of SNA

The basics covered here form the foundation for countless applications:
*   **Epidemiology:** Modeling the spread of diseases through contact networks.
*   **Information Science:** Ranking web pages using algorithms like PageRank (based on the network of hyperlinks).
*   **Organizational Studies:** Mapping communication and advice networks to improve efficiency and identify key influencers.
*   **Counter-Terrorism:** Disrupting terrorist cells by understanding their network structure.
*   **Marketing:** Identifying influencers for viral marketing campaigns.

## Exam Tips

1.  **Visualize and Draw:** Always sketch a small network (5-6 nodes) when presented with a problem. It makes calculating degree, paths, and understanding concepts much easier.
2.  **Matrix Mastery:** Be comfortable creating an adjacency matrix from a network diagram and vice versa. This is a fundamental skill.
3.  **Know the Differences:** Be able to clearly articulate, with examples, the difference between directed/undirected and weighted/unweighted networks. This is a common question.
4.  **Calculate Density:** Remember the different formulas for density in directed vs. undirected networks. It's an easy calculation to perform if you know the formula.
5.  **Context is Key:** When asked to define a term like "degree" or "diameter," try to provide a real-world example to demonstrate your understanding. Don't just state the definition.
6.  **Levels of Analysis:** Be prepared to discuss a social phenomenon (like the spread of misinformation) from the micro, meso, and macro levels of analysis. This shows comprehensive understanding.