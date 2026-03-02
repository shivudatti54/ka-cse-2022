# Probability Defined on Events - Summary

## Key Definitions and Concepts

- **Sample Space (S)**: The set of all possible outcomes of a random experiment
- **Event**: A subset of the sample space—an event "occurs" if the outcome belongs to this subset
- **Probability Space**: Triple (S, ℱ, P) where S = sample space, ℱ = event space (collection of subsets), P = probability function
- **Mutually Exclusive Events**: Events A and B with A ∩ B = ∅—they cannot occur simultaneously
- **Exhaustive Events**: Events whose union equals the sample space

## Important Formulas and Theorems

**Complement Rule**: P(A') = 1 - P(A)

**Addition Rule (General)**: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

**Inclusion-Exclusion (Three Events)**: P(A ∪ B ∪ C) = P(A) + P(B) + P(C) - P(A∩B) - P(A∩C) - P(B∩C) + P(A∩B∩C)

**Law of Total Probability**: P(A) = Σ P(A|Bᵢ)P(Bᵢ) for partition {B₁, B₂, ..., Bₙ} of S

**Classical Probability** (equiprobable outcomes): P(A) = |A|/|S| = favorable outcomes / total outcomes

## Key Points

- Probability functions must satisfy three axioms: non-negativity, normalization (P(S)=1), and countable additivity
- The complement of an event is its "not occurring" case—useful for "at least one" problems
- Mutually exclusive events do not require subtraction in union; non-mutually exclusive events do
- Independent events (P(A∩B) = P(A)×P(B)) are different from mutually exclusive events
- Venn diagrams are essential tools for visualizing event relationships
- All probability values must satisfy 0 ≤ P(A) ≤ 1

## Common Mistakes to Avoid

1. **Confusing independence with mutual exclusivity**: Independent events can occur together; mutually exclusive events cannot. P(A∩B) = 0 for mutually exclusive, but = P(A)×P(B) for independent events.

2. **Forgetting to subtract intersections**: Using P(A∪B) = P(A) + P(B) for non-mutually exclusive events is incorrect—you must subtract P(A∩B).

3. **Incorrect sample spaces**: An improperly defined sample space leads to wrong probability calculations. Always verify all outcomes are accounted for.

4. **Assuming equal probability without justification**: Not all outcomes are equally likely unless explicitly stated or derived from symmetry.

## Revision Tips

1. Practice drawing Venn diagrams for various two and three-event scenarios
2. Memorize the inclusion-exclusion formula and know when to apply each term
3. Solve at least 5 problems involving "at least one" using the complement method
4. Review the law of total probability with tree diagram representations
5. Create a quick reference card with all formulas for last-minute revision