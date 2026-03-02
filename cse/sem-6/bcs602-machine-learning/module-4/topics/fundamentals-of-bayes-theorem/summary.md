# Fundamentals of Bayes' Theorem

## Overview

Bayes' Theorem is a fundamental principle in probability theory that relates conditional probabilities. It provides a mathematical framework for updating beliefs based on new evidence, forming the foundation for Bayesian machine learning algorithms and probabilistic reasoning.

## Key Points

- **Formula**: P(A|B) = P(B|A) \* P(A) / P(B); relates posterior to likelihood, prior, and evidence
- **Components**: P(A|B) = Posterior (updated belief), P(B|A) = Likelihood (evidence probability), P(A) = Prior (initial belief), P(B) = Evidence (normalization)
- **Intuition**: Update prior belief P(A) to posterior P(A|B) after observing evidence B
- **Law of Total Probability**: P(B) = ΣP(B|Ai)\*P(Ai) for mutually exclusive events Ai
- **Application in ML**: Classification via P(Class|Features) = P(Features|Class)\*P(Class)/P(Features)
- **Medical Example**: P(Disease|Positive Test) = P(Positive|Disease)\*P(Disease)/P(Positive); accounts for base rate

## Important Concepts

- Base rate fallacy: ignoring prior P(A) leads to incorrect conclusions (rare disease example)
- Conditional probability: P(A|B) = P(A∩B)/P(B); probability of A given B occurred
- Joint probability: P(A∩B) = P(A|B)*P(B) = P(B|A)*P(A); symmetric relationship
- Sequential updates: posterior from first observation becomes prior for second observation

## Notes

- Memorize Bayes' formula: P(A|B) = P(B|A)\*P(A)/P(B)
- Practice medical diagnosis problems: disease testing is classic exam pattern
- Understand each component: prior (before evidence), likelihood (data probability), posterior (after evidence)
- Base rate fallacy example: even with positive test, disease probability can be low if disease is rare
