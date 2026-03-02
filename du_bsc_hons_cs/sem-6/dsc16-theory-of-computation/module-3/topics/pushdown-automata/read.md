# Pushdown Automata

## Introduction

In the study of formal languages and automata theory, we begin with finite automata, which serve as the simplest computational model. However, finite automata have a critical limitation: they can only recognize regular languages, which constitute a relatively small class of languages. To process more complex language patterns, such as matching parentheses, palindromes, and nested structures, we need additional memory. The pushdown automaton (PDA) addresses this limitation by augmenting a finite control unit with an unbounded stack memory.

Pushdown automata play a fundamental role in compiler design, particularly in parsing expressions and checking syntax. When you write code in any programming language, the compiler uses PDA-based parsing algorithms to verify that your code follows the language's grammatical rules. Every time you write nested parentheses or balanced curly braces, a pushdown automaton-like mechanism verifies the balance. This makes PDA not just a theoretical construct but a practical tool with real-world applications in language processing, syntax analysis, and pattern recognition.

The theory of pushdown automata bridges the gap between regular languages (recognized by finite automata) and context-free languages (recognized by pushdown automata). Understanding PDA is essential for any computer science student, as it forms the theoretical foundation for context-free grammars and parsing techniques used in compilers and interpreters.

## Key Concepts

### Formal Definition of Pushdown Automaton

A pushdown automaton is a 7-tuple M = (Q, Σ, Γ, δ, q₀, Z₀, F), where:

- Q is a finite set of states
- Σ is the input alphabet (finite set of input symbols)
- Γ is the stack alphabet (finite set of stack symbols)
- δ: Q × (Σ ∪ {ε}) × Γ → P(Q × Γ*) is the transition function
- q₀ ∈ Q is the initial state
- Z₀ ∈ Γ is the initial stack symbol (bottom-of-stack marker)
- F ⊆ Q is the set of accepting (final) states

The transition function δ maps a state, an input symbol (or ε for ε-transitions), and a stack symbol to a set of possible configurations. Each configuration consists of a new state and a string to replace the top stack symbol.

### Configuration and Instantaneous Description

A configuration or instantaneous description of a PDA is represented as a triple (q, w, γ), where:
- q ∈ Q is the current state
- w ∈ Σ* is the unread portion of the input
- γ ∈ Γ* is the current stack contents (top at the left)

For example, if the stack contains (from bottom to top) X, Y, Z, we represent it as ZYX (top symbol Z on the left).

### Types of Acceptance

A PDA can accept strings in two ways:

1. **Acceptance by Final State**: The PDA starts in initial state with initial stack symbol, processes the entire input, and reaches a final state. Formally, a string w is accepted if (q₀, w, Z₀) ⊢* (q, ε, γ) for some q ∈ F and any γ ∈ Γ*.

2. **Acceptance by Empty Stack**: The PDA processes the entire input and empties its stack (regardless of final state). Formally, a string w is accepted if (q₀, w, Z₀) ⊢* (q, ε, ε) for some q ∈ Q.

These two acceptance methods are equivalent in expressive power: for every PDA accepting by final state, there exists an equivalent PDA accepting by empty stack, and vice versa.

### Deterministic vs Non-Deterministic PDA

A **Deterministic Pushdown Automaton (DPDA)** has at most one choice for any given configuration:
- |δ(q, a, X)| ≤ 1 for every q ∈ Q, a ∈ Σ ∪ {ε}, X ∈ Γ

A **Non-Deterministic Pushdown Automaton (NPDA)** may have multiple possible transitions from a configuration.

Important distinctions:
- DPDAs accept exactly the **deterministic context-free languages**
- NPDAs accept all **context-free languages**
- Every regular language is accepted by some DPDA
- NPDAs are more powerful than DPDAs for language recognition

### Pushdown Store Operations

The stack in a PDA supports three fundamental operations:
1. **Push**: Add a symbol to the top of the stack
2. **Pop**: Remove the top symbol from the stack
3. **Replace**: Replace the top symbol with a string (can be ε for pop operation)

## Examples

### Example 1: PDA for Language L = {0ⁿ1ⁿ | n ≥ 1}

Design a PDA that accepts the language L = {0ⁿ1ⁿ | n ≥ 1} (strings with equal number of 0s followed by equal number of 1s, like 01, 0011, 000111).

**Solution:**

We use a PDA that pushes a symbol for each '0' read, then pops one symbol for each '1' read.

M = ({q₀, q₁, q₂}, {0, 1}, {Z₀, A}, δ, q₀, Z₀, {q₂})

Transitions:
1. δ(q₀, 0, Z₀) = {(q₀, AZ₀)} — Start by pushing A on seeing first 0
2. δ(q₀, 0, A) = {(q₀, AA)} — Push A for each additional 0
3. δ(q₀, 1, A) = {(q₁, ε)} — On seeing first 1, pop by replacing A with ε
4. δ(q₁, 1, A) = {(q₁, ε)} — Continue popping for each 1
5. δ(q₁, ε, Z₀) = {(q₂, Z₀)} — Accept when stack has only Z₀

**Trace for input "0011":**

Configuration: (q₀, 0011, Z₀)
⊢ (q₀, 011, AZ₀)      [push A for first 0]
⊢ (q₀, 11, AAZ₀)      [push A for second 0]
⊢ (q₁, 1, AZ₀)        [pop A for first 1]
⊢ (q₁, ε, Z₀)         [pop A for second 1]
⊢ (q₂, ε, Z₀)         [accept]

The string is accepted by final state q₂.

### Example 2: PDA for Palindromes

Design a PDA that accepts the language L = {w w^R | w ∈ {a, b}*} (all even-length palindromes).

**Solution:**

This PDA pushes each input symbol until it encounters a middle marker (or the end), then pops symbols to verify the second half is the reverse.

Transitions:
1. δ(q₀, a, Z₀) = {(q₀, aZ₀)} — Push a
2. δ(q₀, b, Z₀) = {(q₀, bZ₀)} — Push b
3. δ(q₀, a, a) = {(q₀, aa)} — Push a on a
4. δ(q₀, a, b) = {(q₀, ab)} — Push a on b
5. δ(q₀, b, a) = {(q₀, ba)} — Push b on a
6. δ(q₀, b, b) = {(q₀, bb)} — Push b on b
7. δ(q₀, ε, a) = {(q₁, a)} — Non-deterministically guess middle
8. δ(q₀, ε, b) = {(q₁, b)} — Non-deterministically guess middle
9. δ(q₁, a, a) = {(q₁, ε)} — Pop matching a
10. δ(q₁, b, b) = {(q₁, ε)} — Pop matching b
11. δ(q₁, ε, Z₀) = {(q₂, Z₀)} — Accept if stack empty

**Trace for input "aba":**

Configuration: (q₀, aba, Z₀)
⊢ (q₀, ba, aZ₀)  [push a]
⊢ (q₀, a, baZ₀) [push b]
⊢ (q₁, a, baZ₀) [guess middle]
⊢ (q₁, ε, bZ₀)  [pop a, doesn't match - this path fails]
Alternative path:
⊢ (q₀, ba, aZ₀) ⊢ (q₁, ba, aZ₀) [guess middle after first character]
⊢ (q₁, a, Z₀)   [pop b]
⊢ (q₂, ε, Z₀)   [accept]

The PDA accepts the string "aba" which is a palindrome.

## Exam Tips

1. **Remember both acceptance methods are equivalent**: If stuck on constructing a PDA, choose the easier method (empty stack or final state) and convert if needed.

2. **Always specify all seven components**: In exam questions asking to design a PDA, explicitly state Q, Σ, Γ, δ, q₀, Z₀, and F.

3. **Trace carefully step-by-step**: When asked to show acceptance, write each configuration change clearly with the transition used.

4. **NPDA ≠ DPDA**: Remember deterministic PDA cannot recognize all CFLs; only deterministic context-free languages. This is a common exam question.

5. **ε-transitions don't consume input**: When tracing, remember ε-moves only change state and stack, not the input string.

6. **Stack alphabet must include initial symbol**: The initial stack symbol Z₀ must be in Γ and is crucial for acceptance by empty stack.

7. **Non-determinism is essential for some languages**: Languages like ww^R require non-determinism to "guess" the middle point. DPDAs cannot recognize all CFLs.

8. **Relationship with Context-Free Grammars**: Every CFL is accepted by some PDA (via leftmost or rightmost derivation), and vice versa. This equivalence is frequently tested.