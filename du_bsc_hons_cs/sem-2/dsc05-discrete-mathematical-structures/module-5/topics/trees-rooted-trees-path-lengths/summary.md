# Trees, Rooted Trees, and Path Lengths  

**Introduction**  
Trees are fundamental non‑linear data structures in discrete mathematics.  As prescribed in the Delhi University B.Sc. (H) Computer Science (NEP 2024) syllabus, this unit covers the definition of a tree, rooted variants, and the notion of path length, together with key theorems that are essential for quick revision.

**Key Concepts**

- **Tree (undirected)**  
  - A connected acyclic graph.  
  - *Properties*: If a tree has *n* vertices, it contains exactly *n − 1* edges.

- **Rooted Tree**  
  - A tree in which one vertex is designated as the **root**.  
  - Every other vertex has a unique **parent** (the vertex adjacent on the path to the root) and zero or more **children**.  
  - **Leaf** (external node): a vertex with no children.  
  - **Internal node**: a vertex with at least one child.

- **Depth, Height, and Level**  
  - **Depth of a vertex** = number of edges on the unique path from the root to that vertex.  
  - **Height of a vertex** = length of the longest downward path from the vertex to a leaf.  
  - **Height of a tree** = height of its root (maximum depth).  
  - All vertices at the same depth belong to the same **level**.

- **Path Lengths**  
  - **Root‑to‑node path length** = depth of the node.  
  - **Internal path length (IPL)** = sum of depths of all internal (non‑leaf) vertices.  
  - **External path length (EPL)** = sum of depths of all leaf vertices.  
  - **Average depth** = IPL / (number of internal nodes) or EPL / (number of leaves), depending on context.

- **Important Theorems**  
  - *Edge count*: Any tree with *n* vertices has *n − 1* edges.  
  - *Full binary tree*: In a full binary tree (every internal node has exactly two children), **L = I + 1**, where *L* = leaves and *I* = internal nodes.  
  - *Internal‑external path length relationship*: For a full binary tree, **EPL = IPL + 2I** (or equivalently, EPL = IPL + 2(L − 1)).  

- **Special Binary Trees (quick recall)**  
  - **Perfect (complete) binary tree**: All levels are fully filled; height *h* has 2^(h+1) − 1 vertices.  
  - **Complete binary tree**: All levels except possibly the last are filled, and the last level is left‑justified.  
  - **Full binary tree**: Every node has either 0 or 2 children.

- **Representation & Traversal (optional for path‑length problems)**  
  - **Parent‑pointer array** or **adjacency list** used to compute depths in O(n).  
  - Pre‑order, in‑order, post‑order traversals give different root‑to‑node orderings, useful for verifying depth calculations.

**Conclusion**  
Mastering the definitions of trees and rooted trees, the concepts of depth/height, and the formulae for internal and external path lengths equips you to solve most exam problems on this topic.  Remember the core relationships: *n − 1* edges, *L = I + 1* for full binary trees, and the path‑length formulas—these are the key take‑aways for the Delhi University discrete structures paper.