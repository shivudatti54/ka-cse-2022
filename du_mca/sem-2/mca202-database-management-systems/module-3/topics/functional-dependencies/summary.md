# Functional Dependencies - Summary

## Key Definitions and Concepts
- **FD**: X → Y means Y is uniquely determined by X
- **Trivial FD**: Y ⊆ X in X → Y
- **Superkey**: Set of attributes that determines all others
- **Canonical Cover**: Minimal equivalent FD set without redundancy

## Important Formulas and Theorems
- **Attribute Closure Algorithm**:
  ```
  Initialize result = X
  While changes occur:
    If Y → Z and Y ⊆ result:
      result += Z
  ```
- **Union Rule**: If X → Y and X → Z, then X → YZ
- **Decomposition Rule**: If X → YZ, then X → Y and X → Z

## Key Points
- FDs represent inherent semantic constraints in data
- Armstrong's axioms are sound and complete
- BCNF requires all non-trivial FDs to have superkeys as determinants
- 3NF allows transitive dependencies if RHS is prime attribute
- Minimal covers eliminate redundant and implied dependencies
- Attribute closure is fundamental for key identification
- FD analysis precedes normalization decisions

## Common Mistakes to Avoid
- Confusing candidate keys with superkeys
- Missing transitive dependencies in closure computations
- Forgetting to check all minimality conditions for candidate keys
- Applying decomposition rules incorrectly during normalization

## Revision Tips
1. Practice closure computations with time limits (5 mins per problem)
2. Create FD diagrams for sample databases (e.g., library, university)
3. Solve previous years' DU questions on 3NF/BCNF conversion
4. Use mnemonics: "AAT" for Armstrong's Axioms (Augmentation, Armstrong's, Transitivity)

Length: 650 words