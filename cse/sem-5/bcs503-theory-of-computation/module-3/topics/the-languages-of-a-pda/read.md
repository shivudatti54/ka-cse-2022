# The Languages of a Pushdown Automaton

## Introduction

A Pushdown Automaton (PDA) is a theoretical computational model that extends the capabilities of a finite automaton by incorporating a stack memory. While finite automata can only recognize regular languages, pushdown automata can recognize a much broader class of languages called context-free languages. The stack allows the PDA to store and retrieve information in a Last-In-First-Out (LIFO) manner, enabling it to match nested structures such as balanced parentheses, matching quotes, and properly nested if-else statements.

The languages accepted by a PDA are precisely the context-free languages, which play a fundamental role in compiler design, programming language parsing, and various other applications in computer science. Understanding how PDAs accept languages is crucial for comprehending the relationship between different classes of automata and the Chomsky hierarchy. This module explores the two primary acceptance mechanisms for PDAs—acceptance by final state and acceptance by empty stack—and demonstrates their equivalence through constructive proofs.

## Key Concepts

### Definition of Pushdown Automaton

A Pushdown Automaton is defined as a 7-tuple M = (Q, Σ, Γ, δ, q₀, Z₀, F) where:

- **Q** is a finite, non-empty set of states
- **Σ** is the input alphabet (finite, non-empty)
- **Γ** is the stack alphabet (finite, non-empty)
- **δ: Q × (Σ ∪ {ε}) × Γ → 𝒫(Q × Γ\*)** is the transition function
- **q₀ ∈ Q** is the initial (start) state
- **Z₀ ∈ Γ** is the initial stack symbol (bottom-of-stack marker)
- **F ⊆ Q** is the set of final (accepting) states

The transition function δ(q, a, X) = {(p₁, γ₁), (p₂, γ₂), ...} means that when the PDA is in state q, reads input symbol a (or ε for ε-moves/Nothing), and sees X on top of the stack, it can non-deterministically choose to move to state pᵢ and replace X with the string γᵢ on the stack. If γᵢ = ε, the top symbol is simply popped. If γᵢ = XY, X is pushed (X becomes new top).

**Configuration:** A PDA configuration is a triple (q, w, γ) where q ∈ Q is the current state, w ∈ Σ* is the unread input, and γ ∈ Γ* is the current stack content (leftmost symbol is top of stack).

**Yield Relation (⊢):** (q, aw, Xβ) ⊢ (p, w, γβ) if δ(q, a, X) contains (p, γ), where a ∈ Σ ∪ {ε}, w ∈ Σ*, X ∈ Γ, β, γ ∈ Γ*.

### Acceptance by Final State

A PDA accepts a string w by final state if, starting from the initial configuration (q₀, w, Z₀), the PDA can make a sequence of moves to reach a configuration (p, ε, γ) where p ∈ F (a final state) and γ is any stack content (including possibly non-empty).

**Definition:** The language accepted by final state is denoted L(M) = {w ∈ Σ* | (q₀, w, Z₀) ⊢* (p, ε, γ) for some p ∈ F, γ ∈ Γ\*}.

**Theorem:** L(M) ⊆ Σ\* for some PDA M if and only if L is a context-free language.

### Acceptance by Empty Stack

A PDA accepts a string w by empty stack if, starting from the initial configuration (q₀, w, Z₀), the PDA can make a sequence of moves to reach a configuration (q, ε, ε) where the stack becomes completely empty. The initial stack symbol Z₀ must be popped for acceptance.

**Definition:** The language accepted by empty stack is denoted N(M) = {w ∈ Σ* | (q₀, w, Z₀) ⊢* (q, ε, ε) for some q ∈ Q}.

### Equivalence of Acceptance Methods

A fundamental theorem in automata theory states that the families of languages accepted by final state and empty stack are identical. This equivalence is proven through two constructive transformations.

**Theorem:** For every PDA M₁ accepting language L by final state, there exists a PDA M₂ accepting L by empty stack. Conversely, for every PDA M₁ accepting language L by empty stack, there exists a PDA M₂ accepting L by final state.

#### Proof: Converting from Final State to Empty Stack

Given PDA M₁ = (Q, Σ, Γ, δ, q₀, Z₀, F) accepting L by final state, construct PDA M₂ = (Q ∪ {q_accept, q_reject}, Σ, Γ ∪ {X₀}, δ', q₀, X₀, ∅) accepting L by empty stack as follows:

1. Add new bottom marker X₀ to prevent stack underflow.
2. Add new states q_accept and q_reject.
3. For every transition δ(q, a, X) = {(p, γ)} in M₁, add δ'(q, a, X) = {(p, γ)} in M₂ (with X₀ treated like other stack symbols).
4. Add ε-transitions from each final state f ∈ F to q_accept: for all X ∈ Γ ∪ {X₀}, add δ'(f, ε, X) = {(q_accept, X)}.
5. In state q_accept, pop all symbols until empty: for all X ∈ Γ, add δ'(q_accept, ε, X) = {(q_reject, ε)} and δ'(q_reject, ε, X) = {(q_reject, ε)}. Finally, δ'(q_accept, ε, X₀) = {(q_reject, ε)}.
6. From q_reject, have ε-loop to clear any remaining input: δ'(q_reject, ε, X) = {(q_reject, ε)} for all X ∈ Γ ∪ {X₀}.

**Correctness:** Any accepting computation in M₁ ends in a final state f with some stack γ. M₂ simulates this computation, then uses ε-moves to pop all stack symbols, reaching (q_reject, ε, ε). Thus L(M₂) = L(M₁).

#### Proof: Converting from Empty Stack to Final State

Given PDA M₁ = (Q, Σ, Γ, δ, q₀, Z₀, ∅) accepting L by empty stack, construct PDA M₂ = (Q ∪ {q_f}, Σ, Γ ∪ {X₀}, δ', q₀, X₀, {q_f}) accepting L by final state as follows:

1. Add new bottom marker X₀ to the stack initially.
2. Add new final state q_f.
3. For every transition δ(q, a, X) = {(p, γ)} in M₁, add δ'(q, a, X) = {(p, γX₀)} in M₂. This ensures X₀ remains at bottom throughout computation.
4. When M₁ would empty the stack, M₂ enters final state: for all q ∈ Q, add δ'(q, ε, X₀) = {(q_f, X₀)}.
5. In final state q_f, allow stack to remain or be popped but stay in q_f: δ'(q_f, ε, X₀) = {(q_f, X₀)}.

**Correctness:** Any string w accepted by M₁ leads to configuration (q, ε, ε). In M₂, the computation ends with (q, ε, X₀). Since δ'(q, ε, X₀) contains (q_f, X₀), we reach final state q_f with non-empty stack. Thus N(M₁) = L(M₂).

### Deterministic vs Non-Deterministic PDA

A PDA is deterministic (DPDA) if for each state q, input symbol a, and stack symbol X, there is at most one move. Formally, |δ(q, a, X)| ≤ 1 for all q ∈ Q, a ∈ Σ ∪ {ε}, X ∈ Γ.

**Key Properties:**

- Deterministic PDAs can only accept a proper subset of context-free languages called deterministic context-free languages (DCFL)
- DCFLs are closed under complementation, LR(k) grammars generate exactly DCFLs
- Every regular language is a deterministic context-free language
- Not all CFLs are deterministic: L = {ww^R | w ∈ {a, b}\*} is not deterministic

**Theorem:** The family of deterministic context-free languages is a proper subset of context-free languages.

## Worked Examples

### Example 1: Language L = {aⁿbⁿ | n ≥ 0} (Acceptance by Empty Stack)

Design a PDA that accepts L = {aⁿbⁿ | n ≥ 0} by empty stack.

**Solution:**

Let M = ({q₀}, {a, b}, {A, Z₀}, δ, q₀, Z₀, ∅)

**Transitions:**

1. δ(q₀, a, Z₀) = {(q₀, AZ₀)} — On reading 'a' with Z₀ on stack, push A
2. δ(q₀, a, A) = {(q₀, AA)} — On reading 'a' with A on stack, push another A
3. δ(q₀, b, A) = {(q₀, ε)} — On reading 'b', pop A from stack
4. δ(q₀, ε, Z₀) = {(q₀, ε)} — Accept empty string (ε ∈ L)

**State Diagram:**

```
         a, Z₀/AZ₀           b, A/ε
    ┌──────────────────────────────────────┐
    │                                      │
    ▼                                      │
(q₀)──────a, A/AA─────────────────►(q₀)   │
    ▲                                      │
    │          b, A/ε                      │
    └──────────────────────────────────────┘
         ε, Z₀/ε (accept ε)
```

**Trace for string "aabb":**

| Step     | Configuration (q, input, stack)         |
| -------- | --------------------------------------- |
| Start    | (q₀, aabb, Z₀)                          |
| Read 'a' | (q₀, abb, AZ₀)                          |
| Read 'a' | (q₀, bb, AAZ₀)                          |
| Read 'b' | (q₀, b, AZ₀)                            |
| Read 'b' | (q₀, ε, Z₀)                             |
| ε-move   | (q₀, ε, ε) — **ACCEPTED (empty stack)** |

### Example 2: Language L = {ww^R | w ∈ {a, b}\*} (Acceptance by Final State)

Design a PDA that accepts L = {ww^R | w^R is the reverse of w} by final state.

**Solution:**

Let M = ({q₀, q₁, q₂}, {a, b}, {a, b, Z₀}, δ, q₀, Z₀, {q₂})

**Transitions:**

_Push phase (before center):_

- δ(q₀, a, Z₀) = {(q₀, aZ₀)}
- δ(q₀, b, Z₀) = {(q₀, bZ₀)}
- δ(q₀, a, a) = {(q₀, aa)}
- δ(q₀, a, b) = {(q₀, ab)}
- δ(q₀, b, a) = {(q₀, ba)}
- δ(q₀, b, b) = {(q₀, bb)}

_Guess the middle (ε-transition):_

- δ(q₀, ε, Z₀) = {(q₁, Z₀)}
- δ(q₀, ε, a) = {(q₁, a)}
- δ(q₀, ε, b) = {(q₁, b)}

_Pop phase (matching and popping):_

- δ(q₁, a, a) = {(q₁, ε)}
- δ(q₁, b, b) = {(q₁, ε)}

_Accept (enter final state):_

- δ(q₁, ε, Z₀) = {(q₂, Z₀)}

**State Diagram:**

```
         a,b: push                    ε: guess middle
    ┌────────────────►(q₀)◄─────────────────────┐
    │                   │                       │
    │                   │ a,b: push             ▼
    │                   ▼                 (q₁)
    │              (push onto stack)       │   │
    │                                     │   │
    │                   ε: Z₀/Z₀           │   │ a/a→ε, b/b→ε
    └─────────────────────────────────────►│   │
                                 ε: Z₀/Z₀  ▼   │
                                           (q₂) [FINAL]
```

**Trace for string "aba":**

| Step          | Configuration (q, input, stack)          |
| ------------- | ---------------------------------------- |
| Start         | (q₀, aba, Z₀)                            |
| Read 'a'      | (q₀, ba, aZ₀)                            |
| Read 'b'      | (q₀, a, baZ₀)                            |
| ε-move to q₁  | (q₁, a, baZ₀)                            |
| Read 'a', pop | (q₁, ε, bZ₀)                             |
| Read 'b', pop | (q₁, ε, Z₀)                              |
| ε-move to q₂  | (q₂, ε, Z₀) — **ACCEPTED (final state)** |

### Example 3: Language L = {w c w^R | w ∈ {a, b}\*} (Center-Marked Palindromes)

Design a PDA that accepts by empty stack. This language has a center marker 'c', making it deterministic.

**Solution:**

Let M = ({q₀, q₁}, {a, b, c}, {a, b, Z₀}, δ, q₀, Z₀, ∅)

**Transitions:**

_Push phase (before c):_

- δ(q₀, a, X) = {(q₀, aX)} for X ∈ {a, b, Z₀}
- δ(q₀, b, X) = {(q₀, bX)} for X ∈ {a, b, Z₀}

_Transition on center marker:_

- δ(q₀, c, X) = {(q₁, X)} for X ∈ {a, b, Z₀}

_Pop phase (after c):_

- δ(q₁, a, a) = {(q₁, ε)}
- δ(q₁, b, b) = {(q₁, ε)}
- δ(q₁, ε, Z₀) = {(q₁, ε)} — Accept by empty stack

**Trace for string "ab c ba":**

| Step                | Configuration (q, input, stack) |
| ------------------- | ------------------------------- |
| Start               | (q₀, abcba, Z₀)                 |
| Read 'a', push      | (q₀, bcba, aZ₀)                 |
| Read 'b', push      | (q₀, cba, baZ₀)                 |
| Read 'c', no change | (q₁, ba, baZ₀)                  |
| Read 'b', pop       | (q₁, a, aZ₀)                    |
| Read 'a', pop       | (q₁, ε, Z₀)                     |
| ε-move              | (q₁, ε, ε) — **ACCEPTED**       |

## Key Theorems Summary

1. **CFL = N(PDA) = L(PDA)**: The family of context-free languages equals both the family of languages accepted by empty stack and the family accepted by final state.

2. **DPDA ⊂ CFL**: Deterministic context-free languages form a proper subset of context-free languages.

3. **DCFL = LR(k)**: Deterministic context-free languages are exactly those generated by LR(k) grammars.

4. **DCFL Closure**: DCFLs are closed under complementation and inverse homomorphisms, but not under union, intersection, or Kleene star.
