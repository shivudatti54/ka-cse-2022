# Supervised, Unsupervised, and Reinforcement Learning - Summary

## Key Definitions and Concepts
- **Supervised Learning**: Labeled data → predictive models
- **Unsupervised Learning**: Unlabeled data → hidden patterns
- **Reinforcement Learning**: Agent-environment interaction → reward maximization

## Important Formulas and Theorems
- **Linear Regression**: $J(\theta) = \frac{1}{2m}\sum(h_\theta(x^{(i)}) - y^{(i)})^2$
- **K-Means Objective**: $\min \sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2$
- **Bellman Equation**: $V(s) = \max_a [R(s,a) + γ\sum P(s'|s,a)V(s')]$

## Key Points
- Supervised requires labeled data; unsupervised works with unlabeled data
- RL focuses on sequential decision-making with delayed rewards
- Clustering validation requires internal (silhouette) and external metrics
- Exploration vs exploitation tradeoff is critical in RL
- Regularization (L1/L2) prevents overfitting in supervised models
- Dimensionality reduction improves model performance and interpretability
- Policy gradient methods directly optimize stochastic policies

## Common Mistakes to Avoid
- Confusing unsupervised learning with reinforcement learning
- Ignoring feature scaling in K-Means and SVM
- Forgetting discount factor (γ) in RL value iteration
- Using accuracy metric for imbalanced classification problems

## Revision Tips
1. Create comparison tables of all three learning paradigms
2. Practice gradient descent calculations manually
3. Implement Q-learning for simple grid environments
4. Use sklearn pipelines for supervised/unsupervised workflows

Length: 650 words