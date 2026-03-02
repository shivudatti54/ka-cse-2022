# Introduction to Probability-Based Learning

## Overview

Probability-based learning uses probability theory to model uncertainty in predictions. These methods estimate probability distributions from data and use them for classification and regression, providing not just predictions but confidence levels, making them valuable for decision-making under uncertainty.

## Key Points

- **Core Idea**: Learn probability P(Y|X) from training data; predict class with highest probability
- **Bayesian Framework**: Apply Bayes' theorem P(Y|X) = P(X|Y)\*P(Y)/P(X) to update beliefs with evidence
- **Advantages**: Outputs probabilities (not just labels), handles missing data naturally, incorporates prior knowledge, robust to noise
- **Applications**: Spam filtering, medical diagnosis, document classification, risk assessment, anomaly detection
- **Key Algorithms**: Naive Bayes, Bayesian Networks, Gaussian Processes, Hidden Markov Models
- **Probabilistic vs Deterministic**: Probabilistic outputs uncertainty estimates; deterministic gives point predictions

## Important Concepts

- Prior P(Y): initial belief before seeing data; Likelihood P(X|Y): probability of observing data given class; Posterior P(Y|X): updated belief after data
- Maximum A Posteriori (MAP): choose class with highest posterior probability
- Generative vs Discriminative: generative models P(X,Y), discriminative models P(Y|X) directly
- Conditional independence assumptions simplify computation (e.g., Naive Bayes)

## Notes

- Understand Bayes' theorem components: Prior, Likelihood, Posterior, Evidence
- Know advantage: outputs calibrated probabilities useful for decision-making
- Difference from deterministic models: uncertainty quantification vs point predictions
- Naive Bayes is simplest probability-based classifier - frequently tested
