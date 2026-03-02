# Quantifiers and Rules of Inference - Summary

## Key Definitions and Concepts

- **Predicate/Propositional Function:** A statement containing variables that becomes a proposition when values are substituted; e.g., P(x): "x is prime"
- **Universal Quantifier (∀):** Expresses that a property holds for all elements in the domain; ∀x P(x) means "for all x, P(x) is true"
- **Existential Quantifier (∃):** Expresses that at least one element satisfies the property; ∃x P(x) means "there exists an x such that P(x) is true"
- **Argument Validity:** An argument is valid if the conclusion follows necessarily from the premises—true premises guarantee a true conclusion

## Important Formulas and Theorems

- **De Morgan's Laws for Quantifiers:**
  - ¬∀x P(x) ≡ ∃x ¬P(x)
  - ¬∃x P(x) ≡ ∀x ¬P(x)

- **Rules of Inference:**
  - Modus Ponens: (P → Q, P) ⊢ Q
  - Modus Tollens: (P → Q, ¬Q) ⊢ ¬P
  - Hypothetical Syllogism: (P → Q, Q → R) ⊢ (P → R)
  - Disjunctive Syllogism: (P ∨ Q, ¬P) ⊢ Q
  - Addition: P ⊢ (P ∨ Q)
  - Simplification: (P ∧ Q) ⊢ P

- **Quantifier Inference Rules:**
  - Universal Instantiation: ∀x P(x) ⊢ P(c)
  - Universal Generalization: P(c) ⊢ ∀x P(x) (c arbitrary)
  - Existential Instantiation: ∃x P(x) ⊢ P(c) (c new constant)
  - Existential Generalization: P(c) ⊢ ∃x P(x)

## Key Points

- Quantifiers extend propositional logic to handle "all" and "some" statements
- The negation of quantifiers swaps between universal and existential
- Validity depends on logical form, not the truth of specific propositions
- Modus Ponens and Modus Tollens are the most frequently used rules in proofs
- Universal Instantiation allows deriving specific instances from general statements
- Existential Instantiation introduces a new constant for some element satisfying the predicate
- A valid argument with false premises can have a false conclusion

## Common Mistakes to Avoid

1. Confusing universal and existential quantifiers—changing ∀ to ∃ without proper negation
2. Applying existential generalization to variables that are not arbitrary
3. Confusing argument validity with true conclusions—an argument can be valid with false premises
4. Forgetting to specify the domain when working with quantifiers
5. Applying Modus Tollens incorrectly by denying the antecedent instead of the consequent

## Revision Tips

1. Practice converting 5-10 English statements to symbolic form daily
2. Write out the proof for Modus Ponens and Modus Tollens from truth tables
3. Create a table summarizing all rules of inference with one example each
4. Work through at least 3 proof problems involving quantified statements
5. Remember: always negate quantifiers by switching the quantifier type and negating the predicate