# Equivalence and Minimization of Automata

## Introduction

Equivalence and Minimization of Automata constitute fundamental concepts in the Theory of Computation that address the optimization of finite automata while preserving their computational behavior. When we design a finite automaton to recognize a particular regular language, the initial construction may contain redundant states that do not contribute meaningfully to language recognition. The minimization process systematically eliminates these redundant states, resulting in a more efficient automaton with the minimum number of states possible.

The concept of **equivalence** refers to the property wherein two automata accept identical languages. Understanding equivalence is crucial for multiple reasons: it enables comparison between different automata recognizing the same language, it provides the theoretical foundation for minimization, and it facilitates optimization in practical applications such as compiler design, pattern matching, digital circuit design, and text processing applications.

This chapter presents a rigorous treatment of state equivalence and distinguishability, the Myhill-Nerode theorem with formal proof, the complete minimization algorithm using partition refinement, and methodologies for checking equivalence between automata. The minimized automaton, also known as the reduced or canonical DFA, exhibits a remarkable property: it is unique for a given regular language up to isomorphism.

## Equivalence of States

### Formal Definition

Let M = (Q, Σ, δ, q₀, F) be a deterministic finite automaton. Two states p and q in Q are said to be **equivalent** (or **indistinguishable**) if for every input string w ∈ Σ\*, the states reached from p and q on processing w are either both accepting or both non-accepting.

Mathematically, states p and q are equivalent if:

∀w ∈ Σ\*: [δ(p, w) ∈ F] ↔ [δ(q, w) ∈ F]

This equivalence relation partitions the state set Q into disjoint equivalence classes. States within the same equivalence class cannot be distinguished by any input string, while states in different classes are distinguishable.

### Theorem: Properties of State Equivalence

**Theorem 1:** State equivalence is an equivalence relation on Q, meaning it is reflexive, symmetric, and transitive.

_Proof:_

- **Reflexive:** For any state p ∈ Q, consider any string w. Since δ(p, w) = δ(p, w), both are either in F or not in F. Hence p ≡ p.
- **Symmetric:** If p ≡ q, then for every w, δ(p, w) ∈ F iff δ(q, w) ∈ F. This condition is symmetric, hence q ≡ p.
- **Transitive:** If p ≡ q and q ≡ r, then for every w, δ(p, w) ∈ F iff δ(q, w) ∈ F, and δ(q, w) ∈ F iff δ(r, w) ∈ F. Therefore, δ(p, w) ∈ F iff δ(r, w) ∈ F, proving p ≡ r.

## Distinguishable States

### Formal Definition

Two states p and q are **distinguishable** if there exists at least one input string w ∈ Σ\* such that one of δ(p, w) or δ(q, w) is a final state while the other is a non-final state. The string w is called a **distinguishing string** for states p and q.

Formally, p and q are distinguishable if:
∃w ∈ Σ\*: [δ(p, w) ∈ F] ⊕ [δ(q, w) ∈ F]

where ⊕ denotes exclusive-or.

### The Distinguishability Table Method

The **table-filling algorithm** (also called the partition refinement method) provides a systematic procedure for identifying distinguishable states:

**Algorithm:**

1. Initialize a table with all state pairs (p, q) where p ≠ q
2. Mark a pair {p, q} if exactly one of p or q is in F (final states)
3. For each unmarked pair {p, q}, examine all input symbols a ∈ Σ
4. If {δ(p, a), δ(q, a)} is a marked pair, then mark {p, q}
5. Repeat steps 3-4 until no new pairs are marked
6. Unmarked pairs represent equivalent states

**Theorem 2 (Fundamental Theorem of Minimization):** After the table-filling algorithm terminates, two states are equivalent if and only if their pair remains unmarked.

_Proof Sketch:_ The algorithm iteratively marks pairs that are "k-distinguishable" (distinguishable by strings of length ≤ k). After iteration k, all pairs distinguishable by strings of length ≤ k are marked. If the algorithm terminates with a pair unmarked, no string of any length can distinguish them, hence they are equivalent.

## Myhill-Nerode Theorem

The Myhill-Nerode theorem provides the theoretical foundation for DFA minimization and characterizes regular languages through equivalence classes.

### Theorem (Myhill-Nerode)

Let L ⊆ Σ* be a language. Define the relation R_L on Σ* as:
x R_L y ⇔ ∀z ∈ Σ\*: (xz ∈ L) ↔ (yz ∈ L)

Then the following three statements are equivalent:

1. L is a regular language
2. The relation R_L has finitely many equivalence classes
3. There exists a DFA M such that L(M) = L with exactly one state for each equivalence class of R_L

_Proof:_

(1) ⇒ (2): If L is regular, there exists a DFA M = (Q, Σ, δ, q₀, F) recognizing L. Define f: Σ* → Q as f(w) = δ(q₀, w). For any x, y ∈ Σ*, if f(x) = f(y) = q, then for any z ∈ Σ\*, δ(q, z) = δ(f(x), z) = f(xz) and similarly for yz. Thus xz ∈ L iff f(xz) ∈ F iff f(yz) ∈ F iff yz ∈ L. Hence x R_L y. Each state q ∈ Q corresponds to at least one string (its preimage under f), so the number of equivalence classes is at most |Q|, which is finite.

(2) ⇒ (3): Suppose R_L has finitely many equivalence classes. Let these classes be [x₁], [x₂], ..., [xₙ]. Construct DFA M = (Q, Σ, δ, q₀, F) where:

- Q = {[x₁], [x₂], ..., [xₙ]}
- q₀ = [ε] (the class of the empty string)
- F = {[x] : x ∈ L}
- δ([x], a) = [xa] for each a ∈ Σ

This construction is well-defined because if x R_L y, then for any a, xa R_L ya. The DFA accepts exactly L, and has one state per equivalence class.

(3) ⇒ (1): If such a DFA exists, it obviously recognizes L, hence L is regular.

**Corollary:** The minimal DFA for a regular language L has exactly |Q| states, where Q is the set of equivalence classes of R_L. This number is called the **index** of L.

## Minimization Algorithm: Partition Refinement

The standard minimization algorithm uses iterative partition refinement to compute the equivalence classes of states.

### Algorithm (Partition Refinement Method)

**Input:** DFA M = (Q, Σ, δ, q₀, F)

**Output:** Minimal DFA M' = (Q', Σ, δ', q₀', F')

**Step 1: Initial Partition**
Create the coarsest partition P₀:

- Block 1: All accepting states F
- Block 2: All non-accepting states Q \ F

**Step 2: Iterative Refinement**
For each block B in current partition P, examine states within B:

- For each pair of states p, q ∈ B and each input symbol a ∈ Σ:
  - If δ(p, a) and δ(q, a) belong to different blocks in P, then p and q must be in different blocks
  - Split B into subgroups where all states have transitions to the same block for each input symbol

**Step 3: Repeat** Step 2 until no further splitting occurs (P stabilizes)

**Step 4: Construct Minimal DFA**

- Each block in final partition P becomes a state in Q'
- Start state: block containing q₀
- Accepting states: blocks that contain any state from F
- Transition function δ': For each block B and symbol a, let δ'(B, a) = the block containing δ(p, a) for any p ∈ B

**Theorem 3 (Correctness):** The algorithm produces the unique minimal DFA equivalent to the input DFA.

_Proof Sketch:_ The algorithm preserves the invariant that states in the same block are indistinguishable. When no more splits occur, states in different blocks are distinguishable. Thus the final partition represents exactly the equivalence classes of the indistinguishability relation. The constructed DFA has one state per equivalence class and accepts the same language.

### Complexity Analysis

The naive partition refinement algorithm runs in O(n²m) time, where n = |Q| and m = |Σ|. Hopcroft's algorithm achieves O(n log n) time complexity using a divide-and-conquer approach with sophisticated data structures.

## Worked Example: Complete DFA Minimization

Consider a DFA that accepts strings ending in 'ab' over alphabet Σ = {a, b}:

**Given DFA:**

- States: {A, B, C, D}
- Start state: A
- Final states: {D}

**Transition Table:**
| State | a | b |
|-------|---|---|
| A | B | A |
| B | B | C |
| C | B | D |
| D | B | A |

**Solution:**

**Step 1: Initial Partition P₀**

- P₀ = { {D}, {A, B, C} }

**Step 2: First Refinement**
Examine block {A, B, C}:

- On input 'a': δ(A,a)=B, δ(B,a)=B, δ(C,a)=B → all go to {A,B,C}
- On input 'b': δ(A,b)=A, δ(B,b)=C, δ(C,b)=D

Since C goes to {D} and A goes to {A,B,C} on 'b', split {A,B,C}:

- P₁ = { {D}, {C}, {A, B} }

**Step 3: Second Refinement**
Examine block {A, B}:

- On input 'a': δ(A,a)=B, δ(B,a)=B → both to {A,B}
- On input 'b': δ(A,b)=A, δ(B,b)=C → A goes to {A,B}, B goes to {C}

Since they go to different blocks on 'b', split {A,B}:

- P₂ = { {D}, {C}, {A}, {B} }

**Step 4: Final Partition**
No further splitting possible. Final blocks: {A}, {B}, {C}, {D}

**Constructing Minimal DFA:**
Each block becomes a state:

- q₀' = {A} (start)
- F' = {D}
- Transitions: δ'({X}, a) = the block containing δ(X, a)

The minimized DFA has 4 states (no reduction possible for this example).

## Equivalence of DFAs

### Definition and Product Construction

Two DFAs D₁ = (Q₁, Σ, δ₁, s₁, F₁) and D₂ = (Q₂, Σ, δ₂, s₂, F₂) are **equivalent** if they accept the same language, i.e., L(D₁) = L(D₂).

### Algorithm Using Product Automaton

**Step 1:** Construct the product DFA P = (Q₁ × Q₂, Σ, δ_P, (s₁, s₂), F_P) where:

- δ_P((p, q), a) = (δ₁(p, a), δ₂(q, a))
- F_P = (F₁ × (Q₂ - F₂)) ∪ ((Q₁ - F₁) × F₂)

**Step 2:** Perform BFS/DFS from the start state (s₁, s₂) in the product automaton

**Step 3:** If any accepting state in F_P is reachable, the DFAs are distinguishable; otherwise they are equivalent

**Theorem 4:** DFAs D₁ and D₂ are equivalent if and only if no state in the product automaton is reachable from (s₁, s₂) where one component is accepting and the other is not.

## Equivalence of NFAs

Two NFAs are equivalent if they accept the same language. The procedure:

1. Convert both NFAs to equivalent DFAs using subset construction
2. Minimize both DFAs using the partition refinement algorithm
3. Check equivalence of the minimized DFAs using product construction

Since minimal DFAs for regular languages are unique up to isomorphism, equivalence checking can also be done by comparing canonical forms.

## Summary

This chapter established the theoretical and algorithmic foundations for DFA minimization:

- **State equivalence** partitions the state set into indistinguishable states
- **Distinguishability** identifies states that must be separated
- **Myhill-Nerode theorem** proves that minimal DFA states correspond to equivalence classes of the indistinguishability relation
- **Partition refinement** provides an efficient algorithm to compute equivalence classes
- **Product construction** enables checking equivalence between automata

The minimized DFA is unique and has the minimum possible number of states among all DFAs recognizing the same language.
