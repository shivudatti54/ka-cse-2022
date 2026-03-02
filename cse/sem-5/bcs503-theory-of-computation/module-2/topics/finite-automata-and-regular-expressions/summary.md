# Finite Automata and Regular Expressions - Summary

## Key Definitions and Concepts

- **Finite Automaton (FA)**: A 5-tuple (Q, Σ, δ, q₀, F) where Q is states, Σ is alphabet, δ is transition function, q₀ is start state, and F is accepting states.

- **DFA (Deterministic FA)**: δ: Q × Σ → Q (exactly one transition per state-symbol pair)

- **NFA (Non-Deterministic FA)**: δ: Q × Σ → P(Q) (zero, one, or multiple transitions possible)

- **Regular Expression**: Algebraic notation using union (|), concatenation (·), and Kleene star (\*) to describe languages.

## Important Formulas and Theorems

- **Kleene's Theorem**: Regular expressions and finite automata are equivalent in expressive power.

- **Pumping Lemma**: For any regular language L, there exists pumping length P such that for any w ∈ L with |w| ≥ P, w = xyz with y ≠ ε, |xy| ≤ P, and xyⁱz ∈ L for all i ≥ 0.

- **Subset Construction**: Converts NFA to DFA by creating states representing subsets of NFA states.

- **Thompson's Construction**: Systematically converts RE to NFA using specific patterns for basic operations.

- **State Elimination**: Converts DFA to RE by systematically removing states.

## Key Points

- DFA and NFA accept exactly the same class of languages (regular languages).

- ε-closure of a state S is the set of states reachable from S using zero or more ε-transitions.

- Regular expressions have algebraic properties: commutativity, associativity, distributivity, identity (ε), and annihilator (∅).

- Finite automata are used in lexical analyzers, text pattern matching, and network protocols.

- The complement of a DFA is obtained by making non-final states final and vice versa.

- A language is regular if and only if its Myhill-Neroje equivalence classes are finite.

## Common Mistakes to Avoid

- Forgetting that DFA transitions must be total (defined for all state-symbol pairs).

- Not computing ε-closures when converting NFA to DFA.

- Confusing Kleene star (R\*) with positive closure (R+).

- Not verifying RE-to-NFA conversions follow proper connection of states.

- Applying pumping lemma incorrectly (the lemma gives necessary but not sufficient conditions).

## Revision Tips

- Practice drawing DFAs for simple language patterns: strings ending in 'ab', strings with odd number of '1's, strings with at least one '0'.

- Memorize the steps for NFA-to-DFA conversion: compute ε-closures, create transition table for subsets.

- Remember RE operator precedence: \* > concatenation > |.

- Review at least 3 problems each on: DFA design, NFA to DFA conversion, RE to NFA conversion.
