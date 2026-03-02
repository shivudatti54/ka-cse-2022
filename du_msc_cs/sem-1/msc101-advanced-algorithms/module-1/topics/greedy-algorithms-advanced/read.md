# Advanced Greedy Algorithms

## Introduction
Greedy algorithms represent a fundamental paradigm in algorithm design, making locally optimal choices at each stage to find global optima. While basic greedy techniques are covered in undergraduate courses, advanced applications require deeper analysis of optimality conditions and approximation guarantees. These methods are particularly valuable in NP-hard optimization problems where exact solutions are impractical.

In modern computing, advanced greedy algorithms power critical systems including real-time scheduling, network routing, and machine learning feature selection. Their efficiency makes them indispensable for big data applications. Recent research has extended greedy approaches to submodular optimization, online algorithms, and quantum computing hybrids, demonstrating their enduring relevance in theoretical CS.

This unit focuses on proving greedy optimality through matroid theory, handling constraints via exchange arguments, and analyzing approximation factors. We bridge classical theory with cutting-edge applications in AI and distributed systems, preparing students for research in algorithmic optimization.

## Key Concepts
1. **Matroid Theory**: 
   - Algebraic structure (E, I) where E is finite set and I is collection of independent subsets
   - Basis axioms: Hereditary, Augmentation properties
   - Key theorem: All maximal independent sets in matroid have same size

2. **Submodular Optimization**:
   - Set functions with diminishing returns: f(A∪{x}) - f(A) ≥ f(B∪{x}) - f(B) for A ⊆ B
   - Greedy guarantees: (1-1/e) approximation for monotone submodular maximization

3. **Online Greedy Algorithms**:
   - Decisions made without future input knowledge
   - Competitive ratio analysis (e.g., ski rental problem)

4. **Exchange Arguments**:
   - Technique to prove optimality by swapping elements between solutions
   - Used in scheduling proofs (e.g., minimizing weighted completion time)

5. **Approximation Mechanisms**:
   - Set Cover: ln(n)-approximation via greedy selection
   - Knapsack: FPTAS using greedy + dynamic programming hybrid

## Examples

**Example 1: Interval Partitioning with Multiple Resources**
_Problem_: Schedule n intervals using minimum classrooms where each room has k capacity.

_Solution_:
1. Sort intervals by start time
2. Use min-heap tracking room end times + current occupancy
3. For each interval:
   - If existing room has end ≤ start and occupancy < k: assign
   - Else: create new room
_Analysis_: Achieves optimal room count via greedy assignment. Time: O(n log n)

**Example 2: Adaptive Huffman Coding**
_Problem_: Compress data stream with dynamically changing frequencies.

_Algorithm_:
1. Initialize Huffman tree with 0-weight NYT node
2. For each symbol:
   - Update frequency and rebuild tree using splay-like rotations
   - Maintain sibling property through greedy local adjustments
_Proof_: Maintains optimal prefix code through weight ordering invariants.

**Example 3: Submodular Maximization with Knapsack Constraints**
_Problem_: max f(S) s.t. Σ_{i∈S} c_i ≤ B, f is submodular.

_Greedy+ Algorithm_:
1. Sort elements by f(i)/c_i descending
2. Build solution S maintaining Σc_i ≤ B
3. Compare with best single element
_Approximation_: (1-1/√e) guarantee via multilinear extensions analysis

## Exam Tips
1. Always verify matroid properties before applying greedy algorithms
2. For approximation proofs: Track residual gains in submodular functions
3. Memorize key ratios: 1/2 for knapsack, 1-1/e for submodular, ln n for set cover
4. Practice exchange arguments using "greedy stays ahead" technique
5. Understand difference between offline and online competitive analysis
6. For scheduling: Convert precedence constraints to matroid independence
7. Remember greedy can be worst-case optimal for some online problems (e.g., paging)