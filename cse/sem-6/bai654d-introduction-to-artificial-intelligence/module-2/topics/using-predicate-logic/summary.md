# Using Predicate Logic

## Overview

Predicate Logic (First-Order Logic) extends propositional logic by introducing predicates, quantifiers, and variables, enabling representation of object properties and relationships. It provides a formal, precise system for knowledge representation with well-defined syntax, semantics, and inference mechanisms.

## Key Points

- **Constants**: Represent specific objects (John, Paris, 5)
- **Variables**: Represent unspecified objects (x, y, z)
- **Predicates**: Express properties or relations (Human(John), Likes(John, Mary))
- **Universal Quantifier (∀)**: Asserts property holds for all objects in domain
- **Existential Quantifier (∃)**: Asserts property holds for at least one object
- **Unification**: Process of finding substitutions that make two expressions identical, crucial for inference
- **Modus Ponens**: From P→Q and P, infer Q
- **Resolution Principle**: Extended to predicate logic using unification for automated theorem proving

## Important Concepts

- Conversion to clause form enables resolution-based inference through seven systematic steps
- Nested quantifiers express complex relationships (∀x∃y Loves(x,y) means "everyone loves someone")
- Predicate logic offers high expressiveness but semi-decidable inference complexity
- Universal instantiation allows inferring P(c) from ∀x P(x) for any constant c

## Notes

- Pay careful attention to quantifier scope and which variables are bound
- Practice conversion to clause form as it's frequently required for resolution proofs
- Master unification by finding the most general unifier for expression pairs
- Distinguish between syntax (well-formed formulas) and semantics (interpretations)
- Understand limitations: cannot handle uncertainty directly, inference can be computationally complex
- Compare with propositional logic to explain how predicate logic extends expressive power
