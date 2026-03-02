# Bayes' Theorem - Summary

## Key Definitions and Concepts

- **Conditional Probability:** P(A|B) = P(A ∩ B) / P(B), the probability of A given B has occurred
- **Joint Probability:** P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)
- **Prior Probability P(H):** Initial belief about a hypothesis before observing evidence
- **Posterior Probability P(H|E):** Updated belief about hypothesis after considering evidence
- **Likelihood P(E|H):** Probability of observing evidence given the hypothesis is true
- **Marginal Likelihood P(E):** Total probability of observing the evidence under all hypotheses
- **Law of Total Probability:** P(E) = Σ P(E|Hᵢ) × P(Hᵢ) for partitioned hypotheses

## Important Formulas and Theorems

- **Bayes' Theorem:** P(A|B) = [P(B|A) × P(A)] / P(B)
- **Extended Form:** P(H|E) = [P(E|H) × P(H)] / [P(E|H₁)P(H₁) + P(E|H₂)P(H₂) + ...]
- **Naive Bayes:** P(C|F₁,...,Fₙ) ∝ P(C) × Πᵢ P(Fᵢ|C)

## Key Points

1. Bayes' Theorem provides a mathematical framework for updating probabilities when new evidence is obtained.

2. The theorem solves "inverse probability" problems - finding P(cause|effect) from P(effect|cause).

3. Prior probability (base rate) critically affects the posterior probability, especially for rare events.

4. Even with a highly accurate test, false positives can dominate when the condition is rare (base rate neglect).

5. The denominator P(B) acts as a normalizing constant ensuring probabilities sum to 1.

6. Naive Bayes classifiers assume feature independence but perform well in practice.

7. Applications include spam filtering, medical diagnosis, search engines, and recommendation systems.

8. The "naive" assumption in Naive Bayes allows computationally efficient classification.

## Common Mistakes to Avoid

1. Confusing P(A|B) with P(B|A) - these are generally different values
2. Forgetting to calculate the marginal probability (denominator) correctly
3. Ignoring the prior probability and assuming P(H|E) ≈ P(E|H)
4. Using the wrong events as hypothesis and evidence
5. Not considering all possible hypotheses when calculating marginal likelihood

## Revision Tips

1. Practice converting word problems into probability notation before applying formulas
2. Memorize the Bayes' Theorem formula and understand what each term represents
3. Work through at least 5-6 diverse problems covering different application domains
4. Remember that "given" always goes after the vertical bar (|) in probability notation
5. For quick recall: Posterior ∝ Likelihood × Prior