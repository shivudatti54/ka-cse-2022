# **Probability Notation, Inference using Full Joint Distributions, Independence, Baye’s Rule, and its Use**

## **Key Concepts**

### Probability Notation

- Random variable: X
- Probability Distribution: P(X = x)
- Probability Mass Function (PMF): P(X) = ∑ P(X = x)
- Probability Density Function (PDF): f(x)
- CDF: F(x) = P(X ≤ x)

### Inference using Full Joint Distributions

- Joint Probability Distribution: P(X, Y)
- Conditional Probability: P(X|Y) = P(X, Y) / P(Y)
- Bayes' Theorem: P(X|Y) = P(Y|X) \* P(X) / P(Y)

### Independence

- Definition: P(X, Y) = P(X) \* P(Y) if and only if X and Y are independent
- Mutual Independence: P(X, Y) = P(X) \* P(Y) = P(Y, X)

### Baye's Rule and its Use

- Definition: P(X|Y) = P(Y|X) \* P(X) / P(Y)
- Use in decision-making and updating probabilities

## **Theorems and Formulas**

- **De Morgan's Law**: ∼(X ∩ Y) = ∼X ∪ ∼Y
- **Addition Rule**: P(X ∪ Y) = P(X) + P(Y) - P(X ∩ Y)
- **Independence Theorem**: If X and Y are independent, then P(X ∩ Y) = P(X) \* P(Y)

## **Important Results**

- **Naive Bayes**: Conditional probability of X given Y is proportional to the conditional probability of Y given X times the probability of X
- **Normal Distribution**: PDF: f(x) = (1/σ√(2π)) \* e^(-((x-μ)^2)/(2σ^2))
