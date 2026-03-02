# Structural Representations of Finite Automata

## Introduction

The theory of finite automata provides a mathematical model for understanding computation with bounded memory. To effectively analyze and work with finite automata, we require precise structural representations that capture both the logical structure and operational behavior of these computational models. The three principal representations used in automata theory are: the state diagram (graphical representation), the transition table (tabular representation), and the formal mathematical definition (5-tuple specification). Each representation offers distinct advantages—the state diagram provides intuitive visual comprehension, the transition table facilitates algorithmic processing, and the formal definition enables rigorous mathematical reasoning about automata properties.

Understanding these structural representations is fundamental to the study of computational theory, as they form the foundation for more complex topics such as nondeterministic finite automata, epsilon transitions, and the equivalence between different automaton classes. The ability to convert between these representations is a core competency that students must develop to proceed successfully in this course.

## Key Concepts

### State Diagram Representation

A state diagram is a directed graph that provides a visual representation of a finite automaton. The diagram consists of nodes (representing states) and labeled edges (representing transitions). The graphical conventions for constructing state diagrams are as follows: states are represented as circles, with the initial state indicated by an incoming arrow from nowhere, and accepting states (final states) marked by a double circle. Each transition is depicted as a directed edge labeled with the input symbol that triggers that transition. When multiple input symbols cause transitions from one state to another, the edges may be labeled with a comma-separated list of symbols, or multiple parallel edges may be drawn.

**Formal Definition**: A state diagram is a directed graph G = (V, E, L) where V is the set of vertices (states), E ⊆ V × Σ × V is the set of labeled edges (transitions), and L: E → Σ assigns labels to edges from the input alphabet.

### Transition Table Representation

A transition table is a tabular array that provides a compact representation of the transition function. The table has rows corresponding to states and columns corresponding to input symbols. Each cell contains the next state(s) reached when the automaton is in the given state and reads the given input symbol. For deterministic finite automata (DFA), each cell contains exactly one state; for nondeterministic finite automata (NFA), a cell may contain zero, one, or multiple states. The initial state is typically marked with an arrow (→) and accepting states are marked with an asterisk (\*).

The transition table representation is particularly useful for algorithmic implementation and for demonstrating the equivalence between different automata. It provides a direct mapping that can be easily converted into data structures for computer implementation.

### Formal Mathematical Definition (5-Tuple)

The most rigorous representation of a finite automaton is the formal 5-tuple definition: M = (Q, Σ, δ, q₀, F), where Q is the finite non-empty set of states, Σ is the finite non-empty input alphabet, δ: Q × Σ → P(Q) is the transition function (mapping state-symbol pairs to sets of states), q₀ ∈ Q is the initial state, and F ⊆ Q is the set of accepting (final) states. For deterministic automata, the codomain is Q rather than P(Q), indicating single-valued transitions.

**Theorem (Representation Equivalence)**: For every finite automaton, the state diagram, transition table, and 5-tuple definition are informationally equivalent; that is, they describe the same automaton and accept exactly the same language.

_Proof Sketch_: We establish equivalence by showing bi-directional conversion. Given a 5-tuple (Q, Σ, δ, q₀, F), we construct a state diagram with vertices Q, directed edges (p, a, q) whenever q ∈ δ(p, a), and apply the initial/final marking conventions. Conversely, from a state diagram we extract Q as the vertex set, Σ as the set of edge labels, δ from labeled edges, q₀ as the uniquely marked initial vertex, and F as the set of final vertices. The transition table is obtained directly from δ by arranging Q and Σ as rows and columns. All conversions preserve the language accepted by the automaton.

## Examples

**Example 1**: Construct all three representations for a DFA that accepts all binary strings ending with 'abb'.

The language L = {w ∈ {0,1}\* : w ends with 'abb'}

**5-Tuple Definition**:
M = (Q, Σ, δ, q₀, F) where:

- Q = {q₀, q₁, q₂, q₃}
- Σ = {0, 1}
- δ: Q × Σ → Q as defined below
- q₀ is initial
- F = {q₃}

**Transition Table**:

| State | 0   | 1   |
| ----- | --- | --- |
| →q₀   | q₀  | q₁  |
| q₁    | q₀  | q₂  |
| q₂    | q₀  | q₃  |
| \*q₃  | q₀  | q₁  |

**State Diagram**: [Vertices: q₀, q₁, q₂, q₃; Initial: q₀; Final: q₃; Edges: q₀--0-->q₀, q₀--1-->q₁, q₁--0-->q₀, q₁--1-->q₂, q₂--0-->q₀, q₂--1-->q₃, q₃--0-->q₀, q₃--1-->q₁]

**Example 2**: Convert the following transition table to a 5-tuple and state diagram.

| State | a   | b   |
| ----- | --- | --- |
| →p    | q   | p   |
| \*q   | q   | r   |
| r     | p   | r   |

**Solution**: The 5-tuple is M = ({p, q, r}, {a, b}, δ, p, {q}) where δ(p,a)=q, δ(p,b)=p, δ(q,a)=q, δ(q,b)=r, δ(r,a)=p, δ(r,b)=r. The state diagram has three states p, q, r with p as initial (arrow), q as final (double circle), and transitions as specified in the table.

## Exam Tips

1. **Representation Conversion**: Practice converting between all three representations (5-tuple, transition table, state diagram) as this is a frequently tested skill in examinations.

2. **Determinism Verification**: Always verify that a given representation describes a deterministic automaton by checking that the transition function yields exactly one state for each (state, input) pair in the DFA case.

3. **Language Identification**: Given a state diagram or table, be able to derive the language accepted by constructing the set of all strings that lead to accepting states.

4. **Formal Notation**: Memorize the precise 5-tuple definition M = (Q, Σ, δ, q₀, F) and understand the difference between δ for DFA (Q × Σ → Q) and NFA (Q × Σ → P(Q)).

5. **Traps and Dead States**: Identify trap states (non-accepting states with self-loops for all inputs) in state diagrams, as these are crucial for determining language rejection.

6. **Empty Transitions**: When ε-transitions are present (in ε-NFA), remember that the state diagram includes edges labeled with ε, and the transition table requires columns for ε-closure computation.

7. **Equivalence Proofs**: Be prepared to prove that two different representations accept the same language by demonstrating their structural correspondence.
