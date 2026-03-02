# Random Fields, Hidden Markov Models, and Approximate Inference

===========================================================

## Overview

---

- Random Fields: statistical models for spatially correlated data
- Hidden Markov Models (HMMs): models for temporal sequences with unobserved states
- Approximate inference methods: Forward Algorithm, Viterbi Algorithm, Baum-Welch Algorithm, Forward-Backward Algorithm

## Key Points

---

### Random Fields

- **Definition**: Statistical model for spatially correlated data, where each observation is a function of neighboring observations
- **Notation**:
  - $X_i$ and $Y_i$: observed and hidden variables
  - $W_{ij}$: pairwise interaction weights
  - $a_i$: unary potentials for hidden variables
  - $b_i$: unary potentials for observed variables
- **Inference**:
  - **Forward Algorithm**: computes marginal probabilities of hidden variables
  - **Viterbi Algorithm**: computes most likely state sequence

### Hidden Markov Models (HMMs)

- **Definition**: Statistical model for temporal sequences with unobserved states
- **Notation**:
  - $Q_i$: hidden state variables
  - $O_i$: observed state variables
  - $A_{ij}$: transition probabilities between hidden states
  - $B_{ji}$: emission probabilities from hidden to observed states
  - $π_j$: initial state probabilities
  - $μ_j$: duration probabilities for hidden states
- **Inference**:
  - **Viterbi Algorithm**: computes most likely state sequence
  - **Baum-Welch Algorithm**: computes maximum likelihood parameters

### Approximate Inference Methods

- **Forward Algorithm**: computes marginal probabilities of hidden variables
  - $f_i(x) = \sum_{y} \pi(y|x) b(y) \prod_{j=1}^{T-1} a(x_j|x,y_{j-1}) (1 - W_{xy_{j-1}})$
- **Viterbi Algorithm**: computes most likely state sequence
  - $\delta_i(x) = \max_{y} \{ f_i(x) + a(x_i|x,y) \}$, $\psi_i(x) = \arg\max_{y} \{ f_i(x) + a(x_i|x,y) \}$
- **Baum-Welch Algorithm**: computes maximum likelihood parameters
  - $\pi_j = \frac{1}{Z} \sum_{x} \prod_{i=1}^{T} a(x_i|x) b(x_i)$
  - $A_{ij} = \frac{1}{Z} \sum_{x} \prod_{i=1}^{T} a(x_i|x) b(x_i) \delta_i(x) \psi_i(x)$
- **Forward-Backward Algorithm**: computes marginal probabilities of hidden variables
  - $\alpha_i(x) = \sum_{y} \pi(y|x) b(y) \prod_{j=1}^{T-1} a(x_j|x,y_{j-1}) (1 - W_{xy_{j-1}})$
  - $\beta_i(x) = \sum_{y} \pi(y|x) b(y) \prod_{j=1}^{T-1} a(x_j|x,y_{j-1}) (1 - W_{xy_{j-1}})$

## Important Formulas and Theorems

---

- **Bayes' Rule**: $P(x|y) = \frac{P(y|x)P(x)}{P(y)}$
- **Normalizing Constant**: $Z = \sum_{x} P(x)$
- **Markov Property**: $P(x,y) = P(x|y)P(y)$
