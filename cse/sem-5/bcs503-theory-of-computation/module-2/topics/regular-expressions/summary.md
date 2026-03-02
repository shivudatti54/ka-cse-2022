# Regular Expressions - Summary

## Key Definitions and Concepts

- **Regular Expression**: A notation to describe a regular language, defined recursively using union (+), concatenation (implicit), and Kleene star (\*) operations over an alphabet Σ.

- **Kleene Star (r\*)**: Represents zero or more concatenations of r, including the empty string ε.

- **Language of RE**: L(r) is the set of all strings matched by the regular expression r.

- **Regular Language**: A language that can be described by some regular expression; equivalently, accepted by some finite automaton.

## Important Formulas and Theorems

- **Basic REs**: ε matches {ε}, a matches {a} for a ∈ Σ
- **Operations**:
  - Union: L(r₁ + r₂) = L(r₁) ∪ L(r₂)
  - Concatenation: L(r₁r₂) = L(r₁)L(r₂)
  - Kleene Star: L(r\*) = {ε} ∪ L(r) ∪ L(r)L(r) ∪ ...

- **Equivalence Theorem**: A language is regular if and only if there exists a regular expression describing it.

- **Kleene's Theorem**: Regular expressions and finite automata are equivalent in descriptive power.

## Key Points

- Every regular expression denotes a regular language, and every regular language can be expressed by a regular expression.

- Thompson's construction converts any regular expression to an NFA with at most 2n states (n = number of symbols/operators).

- State elimination method converts NFA/DFA to regular expression by systematically removing intermediate states.

- Operator precedence: Kleene star (\*) > Concatenation > Union (+)

- Common algebraic laws: Commutative (r₁ + r₂ = r₂ + r₁), Associative, Distributive, Identity (εr = r), Annihilator (φr = φ).

- Extended notations: r+ = rr\* (one or more), [abc] (character class), \d, \w, \s (shorthands).

## Common Mistakes to Avoid

- Confusing ε (empty string, length 0) with φ (empty set/language, matches nothing).

- Forgetting that Kleene star includes ε (zero or more), so r\* always matches the empty string.

- Ignoring operator precedence when writing or simplifying expressions.

- Assuming concatenation is explicitly written; in most notations, it is implicit (ab means a followed by b).

- Making the regex too complex when a simpler equivalent expression exists.

## Revision Tips

- Practice converting between RE ↔ NFA ↔ DFA until comfortable with both directions.

- Memorize the algebraic laws—they help simplify expressions in exam questions.

- For language description problems, first think about the pattern structure (prefix, core, suffix) before writing the RE.

- Use parentheses generously to ensure correct precedence, especially when combining multiple operations.

- Review previous exam questions on this topic for pattern and difficulty level.
