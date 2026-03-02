# Conditional Probability and Independent Events - Summary

## Key Definitions and Concepts

- **Conditional Probability**: P(A|B) = P(A ∩ B) / P(B), representing the probability of A given that B has occurred
- **Independent Events**: Events A and B are independent if P(A ∩ B) = P(A) × P(B), equivalently P(A|B) = P(A)
- **Mutual Independence**: Events are mutually independent if all combinations satisfy the product rule
- **Prior Probability**: Initial probability before evidence is observed (P(Bᵢ))
- **Posterior Probability**: Updated probability after observing evidence (P(Bᵢ|A))
- **Partition**: A set of mutually exclusive, exhaustive events

## Important Formulas and Theorems

- **Conditional Probability**: P(A|B) = P(A ∩ B) / P(B)
- **Multiplication Rule**: P(A ∩ B) = P(A) × P(B|A) = P(B) × P(A|B)
- **Law of Total Probability**: P(A) = Σ P(A|Bᵢ) × P(Bᵢ) for partition {Bᵢ}
- **Bayes' Theorem**: P(Bᵢ|A) = P(A|Bᵢ) × P(Bᵢ) / Σ P(A|Bⱼ) × P(Bⱼ)

## Key Points

- Conditional probability restricts the sample space to the conditioning event
- Independence means knowing one event doesn't change probability of the other
- Pairwise independence does not imply mutual independence
- Bayes' theorem is fundamental to inverse probability problems
- Base rate matters: high accuracy tests can still produce low predictive value
- The multiplication rule extends to multiple events: P(A₁ ∩ A₂ ∩ A₃) = P(A₁) × P(A₂|A₁) × P(A₃|A₁ ∩ A₂)
- Complement is useful for "at least one" problems: P(at least one) = 1 - P(none)

## Common Mistakes to Avoid

- Using P(A|B) = P(B|A) for independence (this is NOT the criterion)
- Forgetting to check P(B) > 0 before computing P(A|B)
- Confusing pairwise independence with mutual independence
- Applying Bayes' theorem without properly identifying hypotheses and evidence
- Ignoring the base rate in real-world probability problems
- Mixing up "or" (union) with "and" (intersection) in probability calculations

## Revision Tips

1. Practice at least 5 problems each on conditional probability, independence testing, and Bayes' theorem

2. Create a visual summary card with all formulas for quick reference during exam preparation

3. Work through past DU question papers to understand the exam pattern and difficulty level

4. Solve the "disease testing" problem type until it becomes intuitive—this is a guaranteed exam question

5. Remember: whenever you see "given that" or "if," think conditional probability; whenever you see "and," think intersection