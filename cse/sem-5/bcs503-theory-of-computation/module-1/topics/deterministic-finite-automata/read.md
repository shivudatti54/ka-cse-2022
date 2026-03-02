# Deterministic Finite Automata

## 1. Introduction

Deterministic Finite Automata (DFA) constitutes a fundamental computational model in the Theory of Computation and serves as the theoretical foundation for understanding regular languages, lexical analysis, and pattern matching. A DFA is a theoretical machine that processes an input string character by character and determines whether the string belongs to a particular language. The term "deterministic" implies that for each state and input symbol, there exists exactly one transition to the next state—no ambiguity exists in the machine's behavior.

In the context of Computer Science and Engineering curriculum, understanding DFA is crucial because it serves as the basis for lexical analyzer design in compiler construction. Modern compilers employ finite automata to tokenize source code, identifying keywords, identifiers, operators, and other lexical elements. Additionally, DFAs are extensively used in text processing applications, network protocols, pattern matching algorithms (such as regular expression engines), and digital circuit design. The study of DFAs introduces students to the fundamental concept of computational models, which is essential for understanding the limits of computation and the Chomsky hierarchy.

This topic connects directly to other fundamental concepts in automata theory, including Non-Deterministic Finite Automata (NFA), regular expressions, regular languages, and the Myhill-Nerode theorem. The equivalence between DFA and NFA represents a significant theoretical result that provides flexibility in designing finite automata for specific languages.

## 2. Formal Definition of DFA

A Deterministic Finite Automaton is formally defined as a 5-tuple M = (Q, Σ, δ, q₀, F), where:

- **Q**: A finite, non-empty set of states representing the possible configurations of the automaton
- **Σ**: A finite set of input symbols called the alphabet
- **δ**: The transition function, defined as δ: Q × Σ → Q, which maps each state-symbol pair to exactly one state
- **q₀**: The initial/start state, where q₀ ∈ Q
- **F**: The set of accepting/final states, where F ⊆ Q

The transition function δ(q, a) = p signifies that when the automaton is in state q and reads input symbol a, it deterministically moves to state p. For a complete DFA, this function must be defined for every combination of state and input symbol—a total function with no undefined transitions.

**Example of Complete DFA:**

Let M = (Q, Σ, δ, q₀, F) where:

- Q = {q₀, q₁}
- Σ = {0, 1}
- δ(q₀, 0) = q₀, δ(q₀, 1) = q₁
- δ(q₁, 0) = q₀, δ(q₁, 1) = q₁
- F = {q₁}

This DFA accepts all strings over {0,1} that end with '1'.

## 3. Language of a DFA

The language accepted by a DFA M, denoted L(M), is the set of all strings that cause the automaton to finish in an accepting state after reading the entire input. Formally:

**Definition:** L(M) = {w ∈ Σ\* | δ(q₀, w) ∈ F}

where δ(q₀, w) represents the state reached after processing the entire string w starting from q₀. Strings that end in a non-accepting state are rejected. The empty string ε is accepted if and only if the start state is an accepting state (q₀ ∈ F).

### 3.1 Extended Transition Function

The basic transition function δ operates on a single input symbol. To determine the state reached after processing an entire string, we define the extended transition function δ̂: Q × Σ\* → Q through structural induction:

**Theorem:** For any state q ∈ Q and string w ∈ Σ\*, the extended transition function δ̂(q, w) is well-defined and can be computed recursively.

**Proof by Structural Induction:**

_Base Case:_ For the empty string ε, we define δ̂(q, ε) = q. Reading no input leaves the automaton in its current state.

_Inductive Step:_ Assume δ̂(q, w) is defined for string w of length |w| = n. For string wa (where a ∈ Σ), we define:
δ̂(q, wa) = δ(δ̂(q, w), a)

This recursive definition processes the string symbol by symbol, applying the transition function at each step. By induction on the length of w, δ̂(q, w) is defined for all w ∈ Σ\*.

**Example:** For the DFA in Section 2, compute δ̂(q₀, "101"):

- δ̂(q₀, ε) = q₀
- δ̂(q₀, "1") = δ(q₀, "1") = δ(q₀, 1) = q₁
- δ̂(q₀, "10") = δ(q₁, 0) = q₀
- δ̂(q₀, "101") = δ(q₀, 1) = q₁

Since q₁ ∈ F, the string "101" is accepted.

## 4. Representation of DFA

DFAs can be represented in two common formal ways:

### 4.1 Transition Table

A tabular representation where rows represent states and columns represent input symbols. The cell (q, a) contains the state δ(q, a). For the DFA accepting strings ending in '1':

| State | 0   | 1   |
| ----- | --- | --- |
| q₀    | q₀  | q₁  |
| q₁    | q₀  | q₁  |

### 4.2 Transition Diagram (State Diagram)

A directed graph where:

- States are represented by circles (nodes)
- Start state is indicated by an arrow pointing from nowhere (labeled "Start")
- Accepting states are marked with double circles
- Transitions are represented by directed edges labeled with input symbols
- Multiple edges between same states can be combined (e.g., 0,1)

## 5. Complete vs Incomplete DFA

A **complete DFA** has a defined transition for every state and every input symbol in the alphabet. An **incomplete DFA** (also called partial DFA) may have undefined transitions for some state-symbol combinations, causing the machine to reject any string that triggers such a transition. Incomplete DFAs are useful for modeling certain scenarios but can be converted to complete DFAs by adding a dead trap state (rejecting state) with self-loops for all input symbols.

## 6. Worked Examples

### Example 1: DFA Accepting Strings Ending with '1'

**Problem:** Design a DFA that accepts all strings over Σ = {0, 1} that end with the symbol '1'.

**Solution:**
We need to track whether the last symbol read is '1' or '0'. The DFA has two states:

- q₀: Start state (last symbol was '0' or no symbol read yet)
- q₁: Accepting state (last symbol was '1')

**Formal Definition:**

- Q = {q₀, q₁}
- Σ = {0, 1}
- q₀ = q₀
- F = {q₁}
- δ: as defined in the transition table above

**Verification:**

- Input "101": q₀ →(1)→ q₁ →(0)→ q₀ →(1)→ q₁. Final state q₁ ∈ F → ACCEPTED
- Input "100": q₀ →(1)→ q₁ →(0)→ q₀ →(0)→ q₀. Final state q₀ ∉ F → REJECTED
- Input "ε": q₀ (start). Since q₀ ∉ F → REJECTED

### Example 2: DFA Accepting Binary Strings Divisible by 2

**Problem:** Design a DFA that accepts all binary strings (representing numbers in MSB-first notation) that are divisible by 2.

**Solution:**
A binary number is divisible by 2 if and only if its last digit is 0.

- q₀: Start and accepting state (remainder 0, divisible by 2)
- q₁: Non-accepting state (remainder 1, not divisible by 2)

**Transition Function:**

- δ(q₀, 0) = q₀ (adding 0 maintains divisibility by 2)
- δ(q₀, 1) = q₁ (adding 1 produces remainder 1)
- δ(q₁, 0) = q₀ (adding 0 to odd number makes it even)
- δ(q₁, 1) = q₁ (adding 1 maintains oddness)

**Acceptance Verification:**

- "1100": Last digit 0 → final state q₀ ∈ F → ACCEPTED
- "1101": Last digit 1 → final state q₁ ∉ F → REJECTED
- "ε": Start at q₀ (accepting) → ACCEPTED

### Example 3: DFA for Language L = {0*1(0+1)*}

**Problem:** Design a DFA accepting strings containing at least one '1'.

**Solution:**
We need at least one '1' somewhere in the string.

- q₀: Start state, no '1' seen yet (non-accepting)
- q₁: '1' has been seen (accepting)

**Transitions:**

- δ(q₀, 0) = q₀ (still no '1')
- δ(q₀, 1) = q₁ (first '1' encountered)
- δ(q₁, 0) = q₁ (stay in accepting)
- δ(q₁, 1) = q₁ (stay in accepting)

## 7. DFA Operations and Closure Properties

### 7.1 Closure under Union

**Theorem:** If L₁ and L₂ are regular languages, then L₁ ∪ L₂ is also regular.

**Proof Sketch:** Let M₁ = (Q₁, Σ, δ₁, q₁₀, F₁) and M₂ = (Q₂, Σ, δ₂, q₂₀, F₂) be DFAs accepting L₁ and L₂ respectively. Construct the product automaton M = (Q₁ × Q₂, Σ, δ, (q₁₀, q₂₀), F) where:

- δ((p, q), a) = (δ₁(p, a), δ₂(q, a))
- F = {(p, q) | p ∈ F₁ or q ∈ F₂}

This DFA accepts a string w if and only if δ((q₁₀, q₂₀), w) ∈ F, meaning either M₁ accepts w or M₂ accepts w (or both). Thus L(M) = L₁ ∪ L₂.

### 7.2 Closure under Intersection

**Theorem:** If L₁ and L₂ are regular languages, then L₁ ∩ L₂ is also regular.

**Proof:** Using the same product construction, define:

- F = {(p, q) | p ∈ F₁ and q ∈ F₂}

The resulting DFA accepts w if and only if both M₁ and M₂ accept w, so L(M) = L₁ ∩ L₂.

### 7.3 Closure under Complement

**Theorem:** If L is a regular language, then Σ\* - L (the complement of L) is also regular.

**Proof:** Let M = (Q, Σ, δ, q₀, F) be a DFA accepting L. Construct M' = (Q, Σ, δ, q₀, Q - F). This DFA accepts exactly those strings that lead to non-accepting states in M, hence accepts Σ\* - L.

## 8. DFA Minimization

The minimization algorithm reduces a DFA to its canonical (unique) minimum form by merging equivalent (indistinguishable) states.

### 8.1 Myhill-Nerode Equivalence

Two states p and q are equivalent (indistinguishable) if for all strings w ∈ Σ\*, δ(p, w) ∈ F if and only if δ(q, w) ∈ F. If there exists some w that distinguishes p and q, they are distinguishable.

### 8.2 Minimization Algorithm (Hopcroft's Algorithm)

**Step 1:** Partition states into two blocks: F (accepting) and Q - F (non-accepting).

**Step 2:** For each block, identify distinguishable state pairs by examining transitions on each input symbol. If states in different blocks are reached, the original states are distinguishable.

**Step 3:** Refine the partition until no new distinctions are found.

**Step 4:** Merge equivalent states into single states.

**Example:** Minimize the DFA with:

- Q = {q₀, q₁, q₂, q₃}
- Σ = {0, 1}
- F = {q₀}
- δ: δ(q₀, 0)=q₁, δ(q₀, 1)=q₂; δ(q₁, 0)=q₃, δ(q₁, 1)=q₂; δ(q₂, 0)=q₁, δ(q₂, 1)=q₃; δ(q₃, 0)=q₃, δ(q₃, 1)=q₃

**Solution:**

- Initial partition: {q₀}, {q₁, q₂, q₃}
- q₁ and q₂: On input 0, go to q₃ and q₁ (different blocks) → distinguishable
- Final partition: {q₀}, {q₁}, {q₂}, {q₃}
- Already minimal (4 states, no equivalent pairs)

## 9. DFA-NFA Equivalence

**Theorem:** Every Non-Deterministic Finite Automaton has an equivalent Deterministic Finite Automaton accepting the same language.

**Proof Sketch:** Given an NFA M = (Q, Σ, δ, q₀, F), construct the equivalent DFA M' using the powerset construction:

- States of M': subsets of Q (all possible sets of NFA states)
- Start state: ε-closure({q₀}) including all states reachable via ε-transitions
- Transition: δ'({q₁, q₂, ..., qₖ}, a) = ε-closure(∪ δ(qᵢ, a))
- Accepting states: any subset containing at least one accepting state of M

This construction yields a DFA accepting exactly L(M). The converse (NFA from DFA) is trivial since every DFA is also an NFA.

## 10. Practice Questions

### Multiple Choice Questions

**Q1.** Consider a DFA with n states. What is the maximum number of states in the equivalent DFA constructed from an NFA with n states using powerset construction?

- (a) n
- (b) n²
- (c) 2ⁿ
- (d) n!

**Answer:** (c) 2ⁿ

**Q2.** Which of the following is TRUE about the language L = {w ∈ {0,1}\* | w ends with 00}?

- (a) Not regular
- (b) Regular, requires exactly 3 states
- (c) Regular, requires exactly 2 states
- (d) Regular, requires exactly 4 states

**Answer:** (b)

**Q3.** In DFA minimization, two states are equivalent if:

- (a) Both are accepting states
- (b) Both are non-accepting states
- (c) For all input strings, they lead to same acceptance result
- (d) They have same number of outgoing transitions

**Answer:** (c)

**Q4.** The complement of a regular language is:

- (a) Always regular
- (b) Never regular
- (c) Regular only if language is infinite
- (d) Context-free but not regular

**Answer:** (a)

### Short Answer Questions

**Q5.** Design a DFA that accepts all strings over {0,1} containing "101" as a substring. (State diagram and formal definition required)

**Q6.** Prove or disprove: The language L = {0ⁿ1ⁿ | n ≥ 0} is regular.

**Q7.** Minimize the following DFA:

| State | 0   | 1   |
| ----- | --- | --- |
| A     | B   | C   |
| B     | A   | D   |
| C     | B   | C   |
| D     | D   | D   |

Initial state: A, Accepting states: {D}
