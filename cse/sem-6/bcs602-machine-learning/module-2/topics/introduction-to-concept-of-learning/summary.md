# Introduction to Concept of Learning

## Overview

Learning in machine learning refers to the process by which computer systems improve performance on specific tasks through experience. Unlike traditional programming with explicit instructions, ML systems learn patterns from data using Tom Mitchell's definition involving experience E, tasks T, and performance P.

## Key Points

- **Traditional vs ML**: Traditional (Rules + Data → Output) vs ML (Data + Output → Rules/Model)
- **Three Learning Paradigms**: Supervised (labeled data for predictions), Unsupervised (unlabeled data for patterns), Reinforcement (environment interaction for rewards)
- **Supervised Learning Types**: Classification (discrete categories: spam detection, image classification) and Regression (continuous values: price prediction, temperature)
- **Unsupervised Learning Types**: Clustering (customer segmentation), Dimensionality Reduction (PCA), Association Rules (market basket analysis)
- **Reinforcement Learning Components**: Agent, Environment, State, Action, Reward - learns optimal behavior through trial and error
- **Overfitting vs Underfitting**: Overfitting memorizes noise (high variance), Underfitting fails to capture patterns (high bias)

## Important Concepts

- ML needed for problems too complex for explicit programming, changing rules, personalization, and pattern discovery
- Bias-Variance Tradeoff: Total Error = Bias² + Variance + Irreducible Error; goal is balanced bias and variance
- Hypothesis space is the set of all possible functions the model can learn
- Inductive bias: assumptions made by algorithms to generalize (KNN assumes locality, linear models assume linearity)
- ML workflow: Data Collection → Preparation → Model Selection → Training → Evaluation → Deployment

## Notes

- Memorize Tom Mitchell's definition - frequently appears in exams
- Know the difference between classification and regression with examples
- Understand learning paradigms: supervised vs unsupervised vs reinforcement vs semi-supervised
- Be able to explain overfitting/underfitting with visual diagrams
- Know evaluation metrics: Accuracy/Precision/Recall for classification; MSE/RMSE/MAE/R² for regression
