# Quantifiers: Definitions and Proofs of Theorems - Summary

## Key Definitions and Concepts

- **Predicate (Propositional Function):** A statement with variables that becomes a proposition when values are substituted
- **Universal Quantifier (∀x P(x)):** True when P(x) holds for every element in the domain
- **Existential Quantifier (∃x P(x)):** True when P(x) holds for at least one element in the domain
- **Bound Variable:** A variable within the scope of a quantifier
- **Free Variable:** A variable not bound by any quantifier

## Important Formulas and Theorems

- **Negation of Universal:** ¬∀x P(x) ≡ ∃x ¬P(x)
- **Negation of Existential:** ¬∃x P(x) ≡ ∀x ¬P(x)
- **Order matters:** ∀x ∃y P(x,y) ≠ ∃y ∀x P(x,y) in general

## Key Points

1. Quantifiers express properties about collections of objects, not individuals
2. The domain of discourse must be clearly specified for quantifiers to have meaning
3. Negating quantifiers flips them: ∀ becomes ∃ and vice versa, with predicate negation
4. Multiple quantifiers require careful attention to order; swapping them often changes truth value
5. To disprove ∀x P(x), find a single counterexample
6. To disprove ∃x P(x), show P(x) is false for all elements
7. "None," "no," "never" are negations of existential statements
8. "All," "every," "always" are universal statements

## Common Mistakes to Avoid

- Forgetting to specify or consider the domain when evaluating quantified statements
- Negating the predicate instead of the quantifier (common error)
- Assuming ∀x ∃y is equivalent to ∃y ∀x (they are different)
- Treating free variables as having definite truth values

## Revision Tips

1. Practice converting English statements to symbolic form and back
2. Work through negation examples repeatedly until automatic
3. Remember: "for all" → ∀, "there exists" → ∃
4. When proving ∀x ∃y, your proof strategy should construct y in terms of x
5. When proving ∃x ∀y, you need to find a specific x that works for all y
