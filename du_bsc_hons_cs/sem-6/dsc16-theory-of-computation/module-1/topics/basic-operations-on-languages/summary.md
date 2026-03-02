# Basic Operations on Languages - Summary

## Key Definitions and Concepts

- **Language**: A set of strings over an alphabet Σ. Denoted as L ⊆ Σ*
- **Alphabet (Σ)**: Finite, non-empty set of symbols
- **Empty String (ε)**: String with zero length
- **Empty Language (∅)**: Language containing no strings

## Important Formulas and Theorems

| Operation | Notation | Definition |
|-----------|----------|------------|
| Union | L₁ ∪ L₂ | {w \| w ∈ L₁ or w ∈ L₂} |
| Concatenation | L₁L₂ | {xy \| x ∈ L₁, y ∈ L₂} |
| Kleene Star | L* | {ε} ∪ L ∪ LL ∪ LLL ∪ ... = ⋃ᵢ₌₀^∞ Lⁱ |
| Kleene Plus | L⁺ | L ∪ LL ∪ LLL ∪ ... = ⋃ᵢ₌₁^∞ Lⁱ |
| Intersection | L₁ ∩ L₂ | {w \| w ∈ L₁ and w ∈ L₂} |
| Complement | L̄ | Σ* - L = {w ∈ Σ* \| w ∉ L} |
| Reversal | Lᴿ | {wᴿ \| w ∈ L} |
| Homomorphism | h(L) | {h(w) \| w ∈ L} |
| Inverse Homomorphism | h⁻¹(L') | {w \| h(w) ∈ L'} |

## Key Points

- **Kleene Star Properties**: L* = L⁺ ∪ {ε}, L⁺ = LL*, ∅* = {ε}, {ε}* = {ε}
- **Empty String vs Empty Language**: {ε} ≠ ∅; {ε} contains one string (empty string), ∅ contains no strings
- **Concatenation with Empty**: L{ε} = L and L∅ = ∅
- **Homomorphism**: Maps each symbol to a string; preserves regularity
- **Reversal of Concatenation**: (L₁L₂)ᴿ = L₂ᴿL₁ᴿ
- **Regular Languages** are closed under: union, concatenation, Kleene star, intersection, complement, homomorphism, inverse homomorphism
- **De Morgan's Laws**: (L₁ ∪ L₂)̄ = L̄₁ ∩ L̄₂ and (L₁ ∩ L₂)̄ = L̄₁ ∪ L̄₂

## Common Mistakes to Avoid

1. **Confusing ∅ and {ε}**: The empty language ∅ has no strings, while {ε} contains exactly one string (the empty string). This affects operations: ∅* = {ε}, but {ε}* = {ε}.

2. **Forgetting ε in Kleene Star**: Many students forget that L* always contains ε, regardless of whether L contains ε.

3. **Reversal Order**: When reversing concatenated languages, remember the order reverses: (L₁L₂)ᴿ ≠ L₁ᴿL₂ᴿ (except in special cases).

4. **Homomorphism Length**: Remember that homomorphism can change string lengths. A string of length n may map to a string of length k×n (if each symbol maps to length k on average).

5. **Complement Requires Universal Language**: The complement L̄ is always relative to some universal language (typically Σ*). Always specify the alphabet when taking complements.

## Revision Tips

1. **Practice with Small Languages**: Work through examples with small finite languages to build intuition about how operations work.

2. **Use Venn Diagrams**: For union and intersection, visualize using Venn diagrams to better understand the operations.

3. **Remember Special Cases**: Memorize the behavior of operations with ∅ and {ε} as they frequently appear in exam questions.

4. **Construct Automata**: Practice constructing NFAs for operations like Kleene star to understand closure properties visually.

5. **Solve Previous Years' Questions**: DU exams often include questions on computing language operations and proving closure properties.