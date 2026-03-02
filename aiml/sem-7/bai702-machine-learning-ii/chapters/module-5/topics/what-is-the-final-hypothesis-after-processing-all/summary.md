# **Revision Notes: Final Hypothesis after Processing Positive Examples**

### Overview

After processing all positive examples using the same dataset, the final hypothesis in a Bayesian network is typically determined by the model with the highest posterior probability.

### Key Points

- **Definition:** The posterior probability of a hypothesis is the probability of the hypothesis given the observed data.
- **Formulas:**
  - Bayes' theorem: P(H|D) = P(D|H) \* P(H) / P(D)
  - Conditional probability: P(A|B) = P(A and B) / P(B)
- **Theorems:**
  - Bayes' theorem is a generalization of conditional probability.
  - The posterior probability is often used to update the prior probability based on new evidence.
- **Approximate Inference:**
  - The final hypothesis is often determined using approximate inference algorithms such as variational inference or Monte Carlo methods.
  - These methods approximate the posterior distribution and can be used to compute the posterior probability of the hypothesis.
- **Markov Property:**
  - The Markov property states that the conditional probability of a node given its parents is independent of the parents' states.
  - This property is often used to simplify inference in Bayesian networks.

### Markov Property and Approximate Inference

The Markov property allows us to factor the joint probability distribution of the nodes in the network into a product of conditional probabilities. This can be used to approximate the posterior distribution using variational inference or Monte Carlo methods.

### Important Formulas and Definitions

- **Conditional Probability:** P(A|B) = P(A and B) / P(B)
- **Bayes' Theorem:** P(H|D) = P(D|H) \* P(H) / P(D)
- **Posterior Probability:** P(H|D) = P(D|H) \* P(H) / P(D)

### Key Takeaways

- The final hypothesis is determined by the model with the highest posterior probability.
- Bayes' theorem and conditional probability are used to compute the posterior probability.
- Approximate inference algorithms such as variational inference or Monte Carlo methods can be used to approximate the posterior distribution.
- The Markov property is used to simplify inference in Bayesian networks.
