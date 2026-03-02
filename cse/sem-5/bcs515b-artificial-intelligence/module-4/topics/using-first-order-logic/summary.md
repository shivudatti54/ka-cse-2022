# Using First-Order Logic - Summary

## Key Definitions and Concepts

- **First-Order Logic (FOL)**: An extension of propositional logic that uses variables, predicates, and quantifiers to represent statements about objects and their relationships.

- **Terms**: Constants, variables, or function applications (e.g., John, x, FatherOf(John))

- **Atoms (Atomic Formulas)**: Predicates applied to terms (e.g., Mortal(x), Likes(x,y))

- **Quantifiers**: Universal (∀) - "for all" and Existential (∃) - "there exists"

- **Interpretation**: Assignment of meanings to symbols including domain, constants, predicates, and functions

- **Unification**: The process of finding a substitution that makes two expressions identical

- **Resolution**: An inference rule used for automated reasoning in FOL

## Important Formulas and Theorems

- **Quantifier Negation**:
  - ¬∀x P(x) ≡ ∃x ¬P(x)
  - ¬∃x P(x) ≡ ∀x ¬P(x)

- **Universal Instantiation**: From ∀x P(x), derive P(c) for any constant c

- **Generalized Modus Ponens**: From P(c) and ∀x (P(x) → Q(x)), infer Q(c)

- **Resolution Principle**: Given clauses, resolve to derive new clauses; empty clause indicates contradiction

## Key Points

1. FOL is more expressive than propositional logic - can represent general rules rather than just specific facts

2. Constants represent specific objects; variables represent unspecified objects

3. Predicates represent properties (unary) or relations (n-ary)

4. The order of quantifiers matters: ∀x ∃y P(x,y) ≠ ∃y ∀x P(x,y)

5. Unification requires the occurs check to prevent circular substitutions

6. Skolemization removes existential quantifiers before resolution

7. FOL is decidable for some restricted cases but unidable in the general case

8. Resolution is refutation-complete for first-order logic

## Common Mistakes to Avoid

1. Confusing the scope of nested quantifiers - ∀x ∃y is different from ∃y ∀x

2. Forgetting to apply the occurs check during unification

3. Incorrectly distributing quantifiers: ∀x (P(x) ∧ Q(x)) ≠ (∀x P(x)) ∧ (∀x Q(x))

4. Treating free variables as bound - they have different semantics

5. Not negating the conclusion properly when using resolution for proof by contradiction

## Revision Tips

1. Practice converting English statements to FOL formulas - this is the most important skill

2. Work through unification examples until the process becomes automatic

3. Remember that resolution requires clause form - practice the conversion steps

4. Understand the relationship between ∀ and ∃ through negation equivalence

5. Focus on understanding why certain unifications fail rather than just memorizing rules
