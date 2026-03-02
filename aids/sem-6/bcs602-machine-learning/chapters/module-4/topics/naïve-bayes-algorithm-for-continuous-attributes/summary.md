# **Naïve Bayes Algorithm for Continuous Attributes**

## **Key Concepts**

- **Naïve Bayes Algorithm**: A probabilistic classifier based on Bayes' theorem
- **Continuous Attributes**: Features with uncountable outcomes (e.g., temperatures, ages)
- **Bayes' Theorem**: P(A|B) = P(B|A) \* P(A) / P(B)

## **Definitions**

- **Conditional Probability**: P(A|B) = P(A and B) / P(B)
- **Prior Probability**: P(A) = P(A and B) + P(A and B')
- **Likelihood**: P(A|B) = f(x|B) \* P(B)

## **Theorems**

- **Bayes' Theorem**: P(A|B) = P(B|A) \* P(A) / P(B)
- **Independence**: If A and B are independent, then P(A|B) = P(A)

## **Naïve Bayes Algorithm**

- **Assumes Independence**: Attributes are independent of each other
- **Calculates Posteriors**: P(C|X) = ∑ P(C) \* P(X|C)
- **Uses Gaussian Mixture Models**: Assumes continuous attributes are Gaussian distributions

## **Formulas**

- **Gaussian Mixture Model**: P(X|C) = ∑ ω_c \* N(x;μ_c,σ_c^2)
- **Naïve Bayes Classifier**: P(C|X) = ∑ P(C) \* P(X|C)

## **Revision Tips**

- Understand the assumptions of the Naïve Bayes Algorithm
- Recognize the importance of independence between attributes
- Familiarize yourself with Gaussian Mixture Models and their application in Naïve Bayes
