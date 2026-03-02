# Resolution in Logic - Summary

## Key Definitions and Concepts

- **Resolution**: A complete inference rule for propositional and first-order logic that derives new clauses from two clauses containing complementary literals
- **Clause**: A disjunction of literals in Conjunctive Normal Form (CNF)
- **Unification**: The process of finding a substitution that makes two literals identical
- **Most General Unifier (MGU)**: The least restrictive substitution that makes literals equal
- **Refutation**: Proof by contradiction - derive empty clause to prove the original statement
- **Horn Clause**: A clause with at most one positive literal; basis of logic programming
- **Skolemization**: Process of removing existential quantifiers by introducing Skolem constants/functions

## Important Formulas and Theorems

- **Resolution Rule (Propositional)**: From (C₁ ∨ P) and (C₂ ∨ ¬P), derive (C₁ ∨ C₂)
- **Resolution Rule (Predicate)**: Using MGU θ, resolvent = (C₁θ - L₁θ) ∨ (C₂θ - L₂θ)
- **Implication Elimination**: (P → Q) ≡ (¬P ∨ Q)
- **Clause Form Conversion**: Formula → Eliminate implications → Move negations → Standardize → Skolemize → Drop universals → CNF → Clauses

## Key Points

1. Resolution is complete for first-order logic - if a conclusion logically follows, resolution can derive it
2. The empty clause (□) represents a contradiction and indicates successful proof
3. Unification must check the occurs condition to avoid infinite structures
4. Horn clauses enable efficient forward and backward chaining
5. Resolution strategies are essential to manage computational complexity
6. Prolog uses resolution with linear input resolution as its execution mechanism
7. Subsumption eliminates redundant clauses and reduces search space
8. Skolemization preserves satisfiability but not the original formula's truth

## Common Mistakes to Avoid

1. Forgetting the occurs check during unification, leading to incorrect substitutions
2. Not properly negating the goal statement when using refutation proof
3. Skolemizing incorrectly by using the same Skolem constant for different existential quantifiers
4. Forgetting that resolution requires complementary literals (P and ¬P)
5. Applying resolution to non-CNF formulas without proper conversion

## Revision Tips

1. Practice converting 5-6 different logical formulas to clause form
2. Solve at least 3 unification problems to master MGU computation
3. Remember the step-by-step procedure for refutation proofs
4. Focus on understanding Horn clauses as they connect to Prolog
5. Review resolution strategies and know which are complete
6. Practice with predicate logic examples involving functions and multiple variables
