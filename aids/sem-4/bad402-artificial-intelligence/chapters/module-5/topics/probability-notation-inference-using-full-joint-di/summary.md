### Probability Notation, Inference, and Bayes' Rule

#### Revision Notes for Artificial Intelligence - Uncertain Knowledge and Reasoning

- **Probability Notation:**
  - Random variable: X = {X(x): x ∈ Ω}
  - Probability distribution: P(X=x)
  - Probability mass function (PMF): P(X=x)
  - Probability density function (PDF): f(x)
- **Inference using Full Joint Distributions:**
  - Joint probability distribution: P(X=x, Y=y)
  - Conditional probability: P(X=x|Y=y)
  - Marginal probability: P(X=x)
- **Independence:**
  - Definition: P(X=x, Y=y) = P(X=x)P(Y=y)
  - Theorem: If X and Y are independent, then P(X=x|Y=y) = P(X=x)
- **Bayes' Rule:**
  - Bayes' Theorem: P(X=x|Y=y) = P(Y=y|X=x)P(X=x) / P(Y=y)
  - Definition: Conditional probability of X given Y
- **Formulas:**
  - Law of Total Probability: P(X=x) = ∑ P(X=x, Y=y)P(Y=y)
  - Bayes' Theorem: P(X=x|Y=y) = P(Y=y|X=x)P(X=x) / P(Y=y)
- **Important Theorems:**
  - De Morgan's Law: P(X∪Y) = P(X) + P(Y) - P(X∩Y)
  - Addition Rule: P(X∪Y) = P(X) + P(Y) - P(X∩Y)
