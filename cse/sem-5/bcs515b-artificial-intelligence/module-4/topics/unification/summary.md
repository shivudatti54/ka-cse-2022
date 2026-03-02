# Unification - Summary

## Key Definitions and Concepts

- **Unification**: The process of finding a substitution θ such that two terms t₁ and t₂ become identical when θ is applied (t₁θ = t₂θ)
- **Substitution**: A mapping from variables to terms, represented as {X₁/t₁, X₂/t₂, ..., Xₙ/tₙ}
- **Unifier**: A substitution that makes two terms identical
- **Most General Unifier (MGU)**: The unifier that makes the least restrictive commitments; unique up to variable renaming
- **Occurs Check**: Verifies that a variable does not occur in the term it is being bound to, preventing infinite structures

## Important Formulas and Theorems

- **Unification condition**: t₁ and t₂ unify iff there exists θ such that t₁θ = t₂θ
- **MGU property**: If θ is MGU of t₁,t₂, then any other unifier θ' = θλ for some λ
- **Algorithm recursive case**: To unify f(s₁,...,sₙ) and f(t₁,...,tₙ), unify all pairs (sᵢ, tᵢ) recursively

## Key Points

1. Variables can be unified with constants, other variables, or compound terms
2. Two terms with different functors or arity cannot be unified
3. The occurs check prevents infinite terms like X = f(X)
4. Unification is the core mechanism in Prolog for pattern matching and variable binding
5. The MGU is unique up to variable renaming
6. Unification proceeds recursively on the structure of terms
7. Failed unification occurs due to functor mismatch, arity mismatch, or occurs check failure

## Common Mistakes to Avoid

1. Forgetting the occurs check when binding variables to compound terms
2. Not checking if functors match before attempting argument unification
3. Confusing the order of substitution composition (right-to-left)
4. Assuming any two terms can be unified when structural compatibility is required

## Revision Tips

1. Practice unification with 3-4 examples of varying complexity daily
2. Always start by comparing functors and arity before recursive argument unification
3. When computing MGU, show each step clearly in the exam
4. Remember that constants and identical variables unify with identity substitution
5. Understand that variable-to-variable binding creates aliasing relationships
