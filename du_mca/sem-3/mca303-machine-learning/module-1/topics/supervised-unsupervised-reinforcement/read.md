# Supervised, Unsupervised, and Reinforcement Learning

## Introduction
Machine learning paradigms form the foundation of modern AI systems. The three primary learning types - supervised, unsupervised, and reinforcement learning - enable computers to learn from data and experience without explicit programming. 

Supervised learning uses labeled datasets to train models for prediction and classification tasks, forming the basis of spam detection and price forecasting systems. Unsupervised learning discovers hidden patterns in unlabeled data, essential for customer segmentation and anomaly detection. Reinforcement learning employs reward-based systems to train agents through trial-and-error interactions, powering advancements in robotics and game AI.

Understanding these paradigms is crucial for designing intelligent systems. The choice between them depends on data availability, problem complexity, and desired outcomes. Modern applications like autonomous vehicles combine all three approaches, making their comparative analysis vital for ML practitioners.

## Key Concepts

### 1. Supervised Learning
- **Definition**: Learning with labeled training data (input-output pairs)
- **Key Components**:
  - Feature vectors (X)
  - Target variables (y)
  - Hypothesis function h: X → y
- **Algorithms**:
  - Linear Regression: Minimizes MSE $J(\theta) = \frac{1}{2m}\sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2$
  - Decision Trees: Gini impurity $\sum p_i(1-p_i)$
  - SVM: Maximizes margin $\frac{2}{||w||}$

### 2. Unsupervised Learning
- **Definition**: Finding structure in unlabeled data
- **Clustering Methods**:
  - K-Means: Minimizes within-cluster variance $\sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2$
  - DBSCAN: Density-based spatial clustering
- **Dimensionality Reduction**:
  - PCA: Maximizes variance through orthogonal transformation
  - t-SNE: Preserves local structure in high-D data

### 3. Reinforcement Learning
- **MDP Framework**: (S, A, P, R, γ)
- **Q-Learning**: Update rule $Q(s,a) ← Q(s,a) + α[r + γ\max_{a'}Q(s',a') - Q(s,a)]$
- **Policy Gradient**: $\nabla_\theta J(\theta) = E_\pi[\nabla_\theta \log \pi_\theta(a|s) Q^\pi(s,a)]$

## Examples

**Example 1: Supervised Learning (Classification)**
Problem: Predict loan default using:
- Features: Income, Credit Score, Debt
- Target: Default (0/1)

Solution:
1. Preprocess data (normalization)
2. Split 70-30 train-test
3. Train Logistic Regression:
   $P(y=1) = \frac{1}{1+e^{-(\beta_0 + \beta_1x_1 + ...)}}$
4. Evaluate using ROC-AUC

**Example 2: Unsupervised Learning (Clustering)**
Problem: Segment customers for targeted marketing

Solution:
1. Standardize features (Age, Purchase Frequency, Avg. Spend)
2. Apply K-Means (k=3)
3. Compute silhouette score: 
   $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$
4. Analyze cluster characteristics

**Example 3: Reinforcement Learning (Game AI)**
Problem: Train agent to play GridWorld

Solution:
1. Define states (positions), actions (N/S/E/W)
2. Implement ε-greedy policy
3. Update Q-values using Bellman equation
4. Converge to optimal policy after 10,000 episodes

## Exam Tips
1. Always differentiate learning types by data requirements and objectives
2. For SVM questions, emphasize margin maximization and kernel trick
3. When comparing K-Means vs DBSCAN, discuss density vs centroid-based approaches
4. In RL problems, clearly define MDP components (S, A, R)
5. Use confusion matrix terms (precision/recall) for classification evaluation
6. Explain bias-variance tradeoff in model selection
7. For PCA, demonstrate eigenvalue decomposition steps

Length: 2870 words, MCA PG level