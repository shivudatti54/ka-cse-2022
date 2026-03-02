# Text Search Using Finite Automata

## Introduction

Text search, also known as pattern matching, is a fundamental problem in computer science where we find occurrences of a pattern string within a larger text string. In the Theory of Computation, this problem is approached from an automata-theoretic perspective, where pattern matching is viewed as a language recognition problem. Given a pattern P of length m and a text T of length n, we seek all positions i such that T[i..i+m-1] = P.

The automata-theoretic approach to text search exploits the mathematical foundations of finite automata to solve pattern matching problems. This perspective provides rigorous methods for constructing pattern matchers and proving their correctness. The key insight is that a pattern can be viewed as describing a regular language, and a finite automaton can be constructed to recognize this language as it processes the input text character by character. This approach is particularly powerful because it extends naturally to complex patterns expressible as regular expressions, providing a unified framework for various text search problems.

## Key Concepts

### Pattern Matching as Language Recognition

Consider a pattern P = "ab". The set of all strings that contain "ab" as a substring forms a regular language. We can define this formally as L = {w ∈ Σ* : w contains "ab" as a substring}. This language is regular because it can be expressed by the regular expression (a|b)*ab(a|b)\*. The finite automaton recognizing this language will have states representing how much of the pattern has been matched so far.

### Deterministic Finite Automaton (DFA) for Single Pattern

For a pattern P = p₁p₂...pₘ, we construct a DFA with m+1 states. State qᵢ (where 0 ≤ i ≤ m) represents that we have successfully matched the first i characters of the pattern. State m is the single accepting state. The transition function δ(qᵢ, c) = j means that after matching i characters of P, if we read character c, we transition to state j representing the longest prefix of P that is a suffix of (p₁...pᵢc).

**Formal Definition:** For pattern P of length m over alphabet Σ, we define a DFA M = (Q, Σ, δ, q₀, F) where:

- Q = {q₀, q₁, ..., qₘ} (q₀ is start state, qₘ ∈ F is accepting state)
- δ(qᵢ, c) = k where k is the largest value such that p₁...pₖ is a suffix of p₁...pᵢc

### Construction Example: Pattern "ababa"

Let P = "ababa" (m = 5). We construct a DFA with states q₀ through q₅. For alphabet Σ = {a, b}:

- δ(q₀, 'a') = q₁ (matched 'a')
- δ(q₀, 'b') = q₀ (no prefix of pattern starts with 'b')
- δ(q₁, 'a') = q₁ (since "aa" has no prefix of "ababa")
- δ(q₁, 'b') = q₂ (matched "ab")
- δ(q₂, 'a') = q₃ (matched "aba")
- δ(q₂, 'b') = q₀ (since "bab" has no prefix of "ababa")
- δ(q₃, 'a') = q₄ (matched "abaa" → longest suffix that's prefix is "a")
- δ(q₃, 'b') = q₅ (matched "abab" → accepts "ababa" partially)
- And so on for all states.

### NFA Construction Using Thompson's Construction

For complex patterns expressed as regular expressions, we use Thompson's construction algorithm. This algorithm systematically converts a regular expression into an equivalent NFA with ε-transitions. The NFA can then be simulated deterministically or converted to a DFA using the subset construction.

Given a pattern P, we can express it directly as a regular expression. For example, pattern "010" corresponds to the regex 010. Thompson's construction creates:

1. For atomic symbols: NFA with two states and one transition
2. For concatenation: Connect ε-transition from accept state of first NFA to start state of second
3. For alternation (|): Create new start and accept states with ε-transitions to both sub-NFAs
4. For Kleene star (\*): Create loop with ε-transitions

### Automaton-Based Search Algorithm

The search algorithm proceeds as follows:

```
Algorithm: Automaton-Matcher(T, P)
Input: Text T[1..n], Pattern P[1..m]
Output: All positions where P occurs in T

1. Construct DFA M for pattern P
2. state ← q₀ (start state)
3. for i ← 1 to n do
4.     state ← δ(state, T[i])
5.     if state = qₘ then
6.         report match ending at position i
```

**Proof of Correctness:** We prove by induction on position i in the text that after processing T[1..i], the automaton is in state qⱼ where j is the length of the longest suffix of T[1..i] that is a prefix of P. When j = m, we have found a match. This invariant holds initially (j = 0 at start), and the transition function ensures it is maintained.

### Time Complexity Analysis

For a DFA with m states over alphabet Σ, preprocessing takes O(m|Σ|) time to construct transitions. The search phase processes each character of the text exactly once, taking O(n) time. The total time is O(n + m|Σ|), and space complexity is O(m|Σ|). Unlike naive algorithms, this provides linear-time guarantees independent of input.

## Examples

### Example 1: Constructing DFA for Pattern "aa"

Pattern: P = "aa", m = 2, Σ = {a, b}

States: Q = {q₀, q₁, q₂} where q₂ is accepting

Transitions:

- δ(q₀, a) = q₁, δ(q₀, b) = q₀
- δ(q₁, a) = q₂, δ(q₁, b) = q₀
- δ(q₂, a) = q₂ (stays in accepting state), δ(q₂, b) = q₀

For text T = "baaab":

- Process 'b': q₀ → q₀
- Process 'a': q₀ → q₁
- Process 'a': q₁ → q₂ (match at position 2)
- Process 'a': q₂ → q₂ (match at position 3)
- Process 'b': q₂ → q₀

Matches found at positions 2 and 3.

### Example 2: NFA for Regex "a(b|c)\*"

Construct NFA for pattern that matches 'a' followed by zero or more 'b' or 'c'.

Using Thompson's construction:

1. Create NFA for 'a': s₀ --a--> s₁
2. Create NFA for (b|c): s₂ --b--> s₃, s₄ --c--> s₃
3. Create NFA for (b|c)\*: Add ε-transitions forming a loop
4. Concatenate: Connect final state of 'a' NFA to start of (b|c)\* NFA

The resulting NFA has approximately 8-10 states with ε-transitions.

### Example 3: Multi-Pattern Search Using Aho-Corasick

For multiple patterns, we build a finite state machine combining all patterns. The Aho-Corasick automaton builds a trie of all patterns and computes failure links similar to the KMP prefix function. This allows scanning text once to find all occurrences of all patterns simultaneously in O(n + m + z) time where z is the number of matches.

## Exam Tips

1. **Pattern to DFA**: When asked to construct a DFA for a pattern, always identify states representing the length of matched prefix (0 through m).

2. **Transition Function**: Remember that δ(qᵢ, c) must give the longest prefix of the pattern that is a suffix of (current_matched_text + c).

3. **Accepting States**: For single pattern matching, there is exactly one accepting state (state m). For "contains pattern" questions, state m is accepting; for "begins with pattern" questions, only state m is accepting.

4. **Regular Expression Connection**: Always express your pattern as a regular expression first—it guides the automaton construction.

5. **Time Complexity**: Automaton-based search guarantees O(n) search time after O(m|Σ|) preprocessing, unlike naive O(mn).

6. **Proof Techniques**: Know the induction proof that the automaton state correctly tracks the longest suffix that is a prefix of the pattern.

7. **ε-NFA Construction**: Remember Thompson's construction rules—concatenation connects accept to start, alternation creates a new start and accept with ε-transitions to both branches.
