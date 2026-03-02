# First-Order Predicate Logic - Summary

## Key Definitions and Concepts

- **Predicate/Propositional Function**: A statement containing variables that becomes a proposition when values are substituted (e.g., P(x), Q(x,y))

- **Quantifiers**: ∀ (universal - "for all") and ∃ (existential - "there exists")

- **Well-Formed Formula (wff)**: Formula constructed using atomic formulas, logical connectives, and quantifiers following recursive rules

- **Free Variable**: Variable not bound by any quantifier; bound variables fall within quantifier scope

- **Sentence/Closed Formula**: A wff with no free variables; has a definite truth value

- **Interpretation**: Assignment of domain, constants to constant symbols, and relations to predicate symbols

## Important Formulas and Theorems

- **Quantifier Negation (De Morgan's Laws)**:
  - ¬∀x P(x) ≡ ∃x ¬P(x)
  - ¬∃x P(x) ≡ ∀x ¬P(x)

- **"All A are B"**: ∀x (A(x) → B(x))

- **"Some A are B"**: ∃x (A(x) ∧ B(x))

- **Quantifier Order Matters**: ∀x∃y P(x,y) ≠ ∃y∀x P(x,y) in general

## Key Points

- Predicate logic extends propositional logic by analyzing internal structure of statements

- Quantifiers specify the extent of predicates: universal (all) or existential (some)

- The scope of a quantifier is the part of the formula where it operates

- Order of different quantifiers (∀ then ∃ vs ∃ then ∀) changes meaning completely

- A formula is valid if true under all interpretations; satisfiable if true under at least one

- Translation to/from English requires careful identification of predicates, domain, and appropriate quantifiers

## Common Mistakes to Avoid

1. Using ∧ instead of → in universal statements ("All A are B" → ∀x(A(x) → B(x)), not ∀x(A(x) ∧ B(x)))

2. Forgetting that quantifier order matters: ∀x∃y ≠ ∃y∀x

3. Neglecting to specify the domain when defining interpretations

4. Confusing free and bound variables; only closed formulas have definite truth values

5. Incorrectly negating quantified statements without properly swapping quantifiers

## Revision Tips

1. Practice translating 5-10 English statements to predicate logic daily

2. Create a truth table for simple predicates over finite domains (like {1, 2, 3})

3. Memorize the standard translation patterns for "all," "some," "only," and "none"

4. Always check your negations by translating back to English to verify correctness

5. Solve previous year DU examination questions on predicate logic for pattern familiarity