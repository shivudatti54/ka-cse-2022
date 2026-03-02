# Regular Expressions - Summary

## Key Definitions and Concepts
- **Regex**: Algebraic notation describing regular languages over Σ
- **Atomic operations**: ∅ (empty set), ε (empty string), symbol a ∈ Σ
- **Operators**: Union (|), Concatenation (·), Kleene star (*)

## Important Formulas and Theorems
- **Kleene's Theorem**: L is regular ⇨ ∃ regex E with L(E) = L
- **Arden's Lemma**: For equations X = AX + B, solution X = A*B
- **Closure Properties**: Regular languages closed under union, concat, star, complement

## Key Points
- Regex ≡ NFA ≡ DFA in expressive power
- Extended regex (+, ?, ranges) are syntactic sugar, not more powerful
- Pumping lemma proves non-regular languages (e.g., 0^n1^n)
- State elimination method converts FA to regex
- Regex engines use backtracking (NFA simulation)
- Lookaheads/lookbehinds make regex irregular in practice

## Common Mistakes to Avoid
- Forgetting ε in union operations (e.g., a|ε instead of a?)
- Incorrect operator precedence: ab* ≠ (ab)*
- Trying to match non-regular patterns (e.g., HTML tags)
- Overusing complex regex when simple string operations suffice

## Revision Tips
1. Practice conversions: regex ↔ NFA ↔ DFA using Thompson/Subset methods
2. Memorize regex laws: (R*)* = R*, R(S+T) = RS + RT
3. Use online testers (regex101.com) to validate patterns
4. Solve previous DU papers on regex-FA conversions

Length: 650 words