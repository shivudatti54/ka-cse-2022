# Classification Using Bayes Model

### Introduction

- Bayes Theorem is a mathematical tool used to update the probability of a hypothesis as more evidence or information becomes available.
- In classification problems, Bayes Theorem is used to determine the probability of an instance belonging to a particular class.

### Definitions

- **Bayes Theorem**: P(H|E) = P(E|H) \* P(H) / P(E)
- **Prior Distribution**: P(H) - the probability of the hypothesis before observing the evidence
- **Likelihood**: P(E|H) - the probability of the evidence given the hypothesis
- **Posterior Distribution**: P(H|E) - the updated probability of the hypothesis after observing the evidence

### Formulas

- **Bayes Theorem**: P(H|E) = P(E|H) \* P(H) / P(E)
- **Normalizing Constant**: P(H) = ∫P(E|H) \* P(H) / P(E) dH

### Theorems

- **Theorem of Total Probability**: P(E) = ∑P(E|H) \* P(H)

### Classification Using Bayes Model

- **Conditional Probability**: P(H|E) = P(E|H) \* P(H) / P(E)
- **Naive Bayes Classifier**: uses the conditional probability of each feature given the class
- **Multinomial Naive Bayes Classifier**: uses the conditional probability of each feature given the class and the number of instances in each class

### Important Formulas

- **Probability of a Class**: P(H) = P(E|H) \* P(H) / P(E)
- **Error Rate**: 1 - P(H|E)
