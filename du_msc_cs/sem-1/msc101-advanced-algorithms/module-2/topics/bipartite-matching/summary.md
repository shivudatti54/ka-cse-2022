# Bipartite Matching - Quick Revision Summary

## Introduction
Bipartite Matching is a fundamental combinatorial optimization problem in graph theory, forming a crucial part of the Delhi University MSc CS Advanced Algorithms syllabus. It deals with finding the maximum pairing between two disjoint sets where each element can be matched to at most one partner.

---

## Key Concepts

### 1. **Bipartite Graph**
- A graph G = (V, E) where vertex set V can be partitioned into two disjoint sets L and R
- Edges exist only between vertices in L and R (no edges within L or R)
- **Formal definition**: G is bipartite if and only if it contains no odd-length cycles

### 2. **Matching Definitions**
- **Matching**: A subset of edges where no two edges share a vertex
- **Maximum Matching**: Matching with maximum possible number of edges
- **Perfect Matching**: Every vertex in both partitions is matched (|L| = |R| = |M|)
- **Cardinality**: Number of edges in the matching

### 3. **Augmenting Paths**
- A path that alternates between unmatched and matched edges
- Starts and ends at unmatched vertices
- **Key Theorem**: A matching is maximum iff no augmenting path exists (Berge's Lemma)

---

## Algorithms (Delhi University Syllabus)

### 1. **Hungarian Algorithm (Kuhn's Algorithm)**
- O(VE) time complexity
- Iteratively finds augmenting paths using DFS
- For each unmatched vertex in L, attempt to find augmenting path to R
- Guaranteed to find maximum matching

### 2. **Hopcroft-Karp Algorithm**
- O(√V E) time complexity
- BFS to find shortest augmenting paths
- Multiple augmentations in one phase
- More efficient for dense graphs

---

## Applications
- Job assignment problem (workers to jobs)
- Maximum bipartite matching in scheduling
- Online advertising matching
- College admissions process
- Resource allocation in distributed systems

---

## Important Theorems (CU Syllabus)
- **König's Theorem**: In bipartite graphs, size of maximum matching equals size of minimum vertex cover
- **Hall's Marriage Theorem**: Condition for perfect matching (Hall's condition)
- **Kőnig-Egérváry Theorem**: Relationship between matching and vertex cover

---

## Complexity Summary
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Kuhn's | O(VE) | O(V + E) |
| Hopcroft-Karp | O(√V E) | O(V + E) |

---

## Conclusion
Bipartite matching is essential for solving assignment problems efficiently. Master the augmenting path concept and both algorithms (Kuhn and Hopcroft-Karp) as these are frequently tested in Delhi University exams. Understand the relationship between matching, vertex cover, and flow networks for comprehensive preparation.