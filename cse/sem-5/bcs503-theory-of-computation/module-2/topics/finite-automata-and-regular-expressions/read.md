# Finite Automata and Regular Expressions

## Introduction

Finite Automata and Regular Expressions constitute foundational concepts in the Theory of Computation, representing mathematically rigorous frameworks for describing regular languages. These equivalent formalisms provide the theoretical underpinnings for pattern matching applications ranging from lexical analyzers in compilers to text processing tools and network protocol verification.

A **Finite Automaton (FA)** is a mathematical abstraction representing a computational device with a finite memory capacity. It processes input strings sequentially, transitioning between discrete states based on the current input symbol. The automaton accepts a string if, after consuming the entire input, it resides in a designated accepting state; otherwise, the string is rejected.

**Regular Expressions (RE)** offer an algebraic formalism for specifying language patterns through union, concatenation, and Kleene star operations. The equivalence between these representations, established by Stephen Kleene in 1956, provides theoretical foundation for lexical analysis and pattern recognition systems.

## Formal Definitions and Components

### 1. Deterministic Finite Automaton (DFA)

A Deterministic Finite Automaton is formally defined as a 5-tuple M = (Q, Σ, δ, q₀, F) where:

- **Q**: Finite non-empty set of states
- **Σ**: Finite non-empty input alphabet
- **δ**: Transition function δ: Q × Σ → Q (total function)
- **q₀**: Initial state (q₀ ∈ Q)
- **F**: Set of accepting/final states (F ⊆ Q)

**Computation**: For an input string w = a₁a₂...aₙ, the DFA computes the state sequence q₀, q₁, q₂, ..., qₙ where qᵢ₊₁ = δ(qᵢ, aᵢ₊₁). The string w is accepted if qₙ ∈ F.

**Example 1 (Design)**: Construct a DFA for L = {w ∈ {a,b}\* | w ends with 'abb'}

Solution:

- Q = {q₀, q₁, q₂, q₃}
- Σ = {a, b}
- F = {q₃}
- Transitions:
  - δ(q₀, a) = q₁, δ(q₀, b) = q₀
  - δ(q₁, a) = q₁, δ(q₁, b) = q₂
  - δ(q₂, a) = q₁, δ(q₂, b) = q₃
  - δ(q₃, a) = q₁, δ(q₃, b) = q₀

### 2. Non-Deterministic Finite Automaton (NFA)

An NFA permits multiple possible transitions for a given state-symbol pair and may include ε-transitions (empty string moves).

Formal Definition: M = (Q, Σ, δ, q₀, F) where:

- **δ**: Q × Σ → P(Q) (transition to subsets of states)
- **ε-transitions**: δ may include transitions labeled ε

**Acceptance Criterion**: A string w is accepted if there exists at least one computation path leading from q₀ to a state in F after consuming w. This non-determinism "guesses" the correct path.

**Example 2 (NFA)**: NFA accepting (a|b)\*abb:

- Q = {q₀, q₁, q₂, q₃}
- Σ = {a, b}
- δ:
  - δ(q₀, a) = {q₀, q₁}, δ(q₀, b) = {q₀}
  - δ(q₁, a) = ∅, δ(q₁, b) = {q₂}
  - δ(q₂, b) = {q₃}
- F = {q₃}

### 3. Extended Transition Function

For both DFA and NFA, we define the extended transition function to process entire strings:

**DFA**: δ*: Q × Σ* → Q

- Base: δ\*(q, ε) = q
- Inductive: δ*(q, wa) = δ(δ*(q, w), a)

**NFA**: δ*: Q × Σ* → P(Q)

- Base: δ\*(q, ε) = ε-closure({q})
- Inductive: δ*(q, wa) = ε-closure(∪{δ(p, a) | p ∈ δ*(q, w)})

## The Subset Construction: NFA to DFA Conversion

### 4. ε-Closure Computation

The ε-closure of a set of states S, denoted ε-closure(S), is the set of all states reachable from states in S through zero or more ε-transitions.

**Algorithm**:

```
ε-closure(S):
    push all states in S onto stack
    add all states in S to result
    while stack not empty:
        pop state t
        for each state u in ε-moves(t):
            if u not in result:
                add u to result
                push u onto stack
    return result
```

**Example**: Given NFA with ε-transitions:

- ε-closure({q₀}) = {q₀, q₁} (assuming ε-move from q₀ to q₁)

### 5. Subset Construction Algorithm

**Theorem**: For every NFA N, there exists a DFA D such that L(D) = L(N).

**Proof Sketch**: The construction defines DFA states as subsets of NFA states. The DFA state [S] (where S ⊆ Q_N) represents "being in all states reachable via some path." Formally, δ_D([S], a) = ε-closure(∪{δ_N(p, a) | p ∈ S}).

**Algorithm**:

```
1. Let ε-closure({q₀}) be the initial DFA state
2. For each DFA state [S] and symbol a ∈ Σ:
   Compute T = ε-closure(∪{δ(p, a) | p ∈ S})
   If T is not in D's states, add as new state
   Add transition δ_D([S], a) = [T]
3. A DFA state [S] is accepting if S ∩ F ≠ ∅
4. Repeat until no new states
```

**Complete Example**: Convert the NFA from Example 2 to DFA:

NFA: Q = {q₀, q₁, q₂, q₃}, Σ = {a, b}, F = {q₃}
Transitions:

- δ(q₀, a) = {q₀, q₁}, δ(q₀, b) = {q₀}
- δ(q₁, b) = {q₂}, δ(q₂, b) = {q₃}

Step 1: Compute ε-closures (assuming no ε-transitions):

- ε-closure({q₀}) = {q₀}
- ε-closure({q₁}) = {q₁}
- ε-closure({q₂}) = {q₂}
- ε-closure({q₃}) = {q₃}

Step 2: Initial DFA state: ε-closure({q₀}) = {q₀} = R₁

Step 3: Compute transitions from R₁ = {q₀}:

- On 'a': δ_N({q₀}, a) = {q₀, q₁} → ε-closure = {q₀, q₁} = R₂
- On 'b': δ_N({q₀}, b) = {q₀} → ε-closure = {q₀} = R₁

Step 4: Process R₂ = {q₀, q₁}:

- On 'a': δ_N({q₀, q₁}, a) = {q₀, q₁} → R₂
- On 'b': δ_N({q₀, q₁}, b) = {q₀, q₂} → ε-closure({q₀, q₂}) = {q₀, q₂} = R₃

Step 5: Process R₃ = {q₀, q₂}:

- On 'a': δ_N({q₀, q₂}, a) = {q₀, q₁} → R₂
- On 'b': δ_N({q₀, q₂}, b) = {q₀, q₃} → ε-closure = {q₀, q₃} = R₄ (accepting)

Step 6: Process R₄ = {q₀, q₃}:

- On 'a': δ_N({q₀, q₃}, a) = {q₀, q₁} → R₂
- On 'b': δ_N({q₀, q₃}, b) = {q₀, q₃} → R₄

Final DFA: States = {R₁, R₂, R₃, R₄}, Accepting = {R₄}

## Regular Expressions

### 6. Syntax and Semantics

A Regular Expression over alphabet Σ is defined recursively:

**Base Cases**:

- ∅ (empty set): Language with no strings
- ε (empty string): Language {ε}
- a (for a ∈ Σ): Language {a}

**Inductive Cases**: If r and s are regular expressions:

- Union: (r | s) → L(r) ∪ L(s)
- Concatenation: (rs) → L(r)L(s) = {xy | x ∈ L(r), y ∈ L(s)}
- Kleene Star: (r)_ → L(r)_ = {ε} ∪ L(r) ∪ L(r)L(r) ∪ ...

**Operator Precedence**: \* highest, then concatenation, then |

### 7. Algebraic Laws

Let r, s, t be regular expressions:

- Commutativity: r | s = s | r
- Associativity: (r | s) | t = r | (s | t), (rs)t = r(st)
- Left Distributivity: r(s | t) = rs | rt
- Right Distributivity: (s | t)r = sr | tr
- Identity: εr = rε = r
- Annihilator: ∅r = r∅ = ∅
- Idempotence: r | r = r
- Star Properties: r* = r*r* = (r | ε)*

## Conversion Methods

### 8. Thompson's Construction: RE → NFA

This algorithm constructs an NFA from any regular expression in O(n) states.

**Construction Rules**:

1. **Base**: Create isolated NFA fragments for ∅, ε, and a
2. **Union**: Connect new start to both sub-NFAs' starts via ε; connect both accepting states to new accepting via ε
3. **Concatenation**: Connect first NFA's accepting to second's start
4. **Kleene Star**: Add ε-transitions from accepting back to start and from start to accepting

**Example**: Construct NFA for (a|b)\*abb using Thompson's Construction:

Step 1: Build NFA for 'a' and 'b' (separate)
Step 2: Union 'a' and 'b' → NFA for (a|b)
Step 3: Apply Kleene star → NFA for (a|b)\*
Step 4: Concatenate with 'a', 'b', 'b' sequentially

Resulting NFA has 14 states (optimal for this expression).

### 9. State Elimination: DFA/NFA → RE

**Algorithm**:

1. Create new initial state q_s and final state q_f
2. Add ε-transitions: q_s → q₀ and each state in F → q_f
3. Eliminate intermediate states one by one, updating edge labels with REs
4. Final RE connects q_s to q_f

**Example**: Convert DFA for (a|b)\*abb to RE:

After elimination, the regular expression is (a|b)\*abb.

## Kleene's Theorem

### Theorem Statement

A language L is regular if and only if there exists a regular expression r such that L = L(r).

### Proof Outline

**Part 1 (RE → FA)**: Thompson's Construction provides constructive proof that every RE generates an NFA recognizing its language.

**Part 2 (FA → RE)**: State Elimination Method demonstrates that every DFA/NFA can be converted to an equivalent regular expression. By the NFA→DFA equivalence, this establishes the theorem.

## State Minimization (Myhill-Nerode)

### Equivalence Relation

Two states p and q are distinguishable if there exists a string w such that exactly one of δ(p, w) and δ(q, w) is accepting.

### Minimization Algorithm

```
1. Remove all unreachable states
2. Partition states into F and Q-F (initially)
3. For each symbol, check if states in same block go to different blocks
4. Refine partition until stable
5. Each block becomes one state in minimized DFA
```

**Example**: Minimize the 4-state DFA for (a|b)\*abb:
Resulting minimized DFA has 4 states (this particular example is already minimal).

## Summary

The theory of finite automata and regular expressions provides fundamental tools for language recognition. Key relationships include:

1. **DFA ↔ NFA**: Equivalent computational power via subset construction
2. **RE ↔ FA**: Kleene's theorem establishes equivalence
3. **Minimization**: Myhill-Nerode theorem provides canonical minimized DFA

These concepts enable systematic design of lexical analyzers and pattern matching systems in compiler construction and text processing applications.
