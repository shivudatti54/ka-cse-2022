# Introduction to Machine Learning

## 1. What is Machine Learning?

Machine Learning (ML) is a subfield of artificial intelligence that enables computational systems to improve their performance on specific tasks through experience, without being explicitly programmed for every contingency. Rather than executing rigid, predetermined instructions, ML algorithms construct mathematical models from training data to perform predictions or decisions under uncertainty. Fundamentally, machine learning constitutes the automated detection of statistically significant patterns within datasets, subsequently employing these patterns to generalize to unseen data.

### 1.1 Formal Mathematical Definitions

Let us formalize the learning problem as follows: Given a training dataset $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^{n}$ where $\mathbf{x}_i \in \mathcal{X} \subseteq \mathbb{R}^d$ represents the feature vector and $y_i \in \mathcal{Y}$ represents the corresponding label, the objective is to learn a hypothesis $h: \mathcal{X} \to \mathcal{Y}$ from a hypothesis space $\mathcal{H}$ that minimizes the expected risk (or loss):

$$R(h) = \mathbb{E}_{(\mathbf{x}, y) \sim P}[\ell(h(\mathbf{x}), y)]$$

where $\ell: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_+$ denotes a loss function measuring the discrepancy between predicted and actual values. Since the underlying distribution $P$ is typically unknown, we minimize the empirical risk:

$$\hat{R}(h) = \frac{1}{n} \sum_{i=1}^{n} \ell(h(\mathbf{x}_i), y_i)$$

**Arthur Samuel (1959):** "Field of study that gives computers the ability to learn without being explicitly programmed."

**Tom Mitchell (1997):** "A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$."

The learning process can be conceptualized as:
$$\text{Training Data } \mathcal{D} \xrightarrow{\text{Learning Algorithm}} \text{Model } h \in \mathcal{H} \xrightarrow{\text{Inference}} \text{Predictions}$$

### 1.2 Hypothesis Space and Inductive Bias

The hypothesis space $\mathcal{H}$ represents the set of all possible functions the learning algorithm can consider. The choice of $\mathcal{H}$ encodes the inductive bias—assumptions that enable generalization from finite training data. Without inductive bias, no learning is theoretically possible (the "no free lunch" theorem states that no algorithm can generalize well across all possible problems).

**Theorem (No Free Lunch):** For any two learning algorithms $A$ and $B$, there exists a distribution $P$ for which $A$ performs no better than $B$, and vice versa. This necessitates careful hypothesis space selection based on domain knowledge.

## 2. Types of Machine Learning

Machine learning paradigms are categorized according to the nature of supervision available during training:

### 2.1 Supervised Learning

In supervised learning, the training dataset comprises labeled examples $(\mathbf{x}_i, y_i) \in \mathcal{X} \times \mathcal{Y}$. The objective is to learn a mapping $f: \mathcal{X} \to \mathcal{Y}$ that generalizes to unseen data.

**Mathematical Formulation:** Given $\mathcal{D}_{train} = \{(\mathbf{x}_i, y_i)\}_{i=1}^{n}$, find $h^* \in \mathcal{H}$ minimizing:

$$h^* = \arg\min_{h \in \mathcal{H}} \frac{1}{n} \sum_{i=1}^{n} \ell(h(\mathbf{x}_i), y_i) + \lambda \cdot \Omega(h)$$

where $\Omega(h)$ is a regularization term controlling model complexity and $\lambda$ is the regularization parameter.

**Classification vs. Regression:**

- **Classification:** $\mathcal{Y}$ is discrete (e.g., $\{0, 1\}$ for binary classification). The 0-1 loss is commonly used: $\ell(h(\mathbf{x}), y) = \mathbb{I}\{h(\mathbf{x}) \neq y\}$
- **Regression:** $\mathcal{Y}$ is continuous (e.g., $\mathbb{R}$). The squared loss is standard: $\ell(h(\mathbf{x}), y) = (h(\mathbf{x}) - y)^2$

**Common Algorithms with Mathematical Foundations:**

- **Linear Regression:** $h(\mathbf{x}) = \mathbf{w}^T \mathbf{x} + b$, optimized via ordinary least squares: $\min_{\mathbf{w}, b} \sum_{i=1}^{n} (y_i - \mathbf{w}^T \mathbf{x}_i - b)^2$
- **Logistic Regression:** $h(\mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b)$ where $\sigma(z) = \frac{1}{1 + e^{-z}}$, optimized via maximum likelihood estimation
- **Support Vector Machines (SVM):** Find maximum margin hyperplane: $\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2$ subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \geq 1$
- **Decision Trees:** Greedy splitting based on information gain or Gini impurity
- **Neural Networks:** Universal function approximators using gradient-based optimization

### 2.2 Unsupervised Learning

Unsupervised learning operates on unlabeled data $\mathcal{D} = \{\mathbf{x}_i\}_{i=1}^{n}$, seeking to discover latent structure, patterns, or representations without explicit guidance.

**Mathematical Formulation:** Given $\mathcal{D} = \{\mathbf{x}_i\}_{i=1}^{n}$, learn parameters $\theta$ of a model $p(\mathbf{x}; \theta)$ or discover clusters $\{C_k\}$ partitioning the data.

**Common Algorithms:**

- **K-Means Clustering:** $\min_{\{\mu_k\}, \{r_{ik}\}} \sum_{k=1}^{K} \sum_{i=1}^{n} r_{ik} \|\mathbf{x}_i - \mu_k\|^2$ subject to $r_{ik} \in \{0, 1\}$ and $\sum_k r_{ik} = 1$
- **Principal Component Analysis (PCA):** Find orthogonal directions of maximum variance. The $k$-th principal component $\mathbf{u}_k$ maximizes $\mathbf{u}_k^T \mathbf{S} \mathbf{u}_k$ subject to $\|\mathbf{u}_k\| = 1$ and orthogonality to previous components, where $\mathbf{S}$ is the sample covariance matrix
- **Gaussian Mixture Models (GMM):** Probabilistic clustering using expectation-maximization
- **Autoencoders:** Neural network learning identity mapping through bottleneck representation

### 2.3 Reinforcement Learning

Reinforcement learning (RL) involves an agent interacting with an environment, learning a policy $\pi: \mathcal{S} \to \mathcal{A}$ that maximizes cumulative reward.

**Mathematical Formulation:** The agent-environment interaction follows a Markov Decision Process (MDP) defined by tuple $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$ where:

- $\mathcal{S}$: State space
- $\mathcal{A}$: Action space
- $P(s'|s, a)$: Transition probability
- $R(s, a)$: Reward function
- $\gamma \in [0, 1)$: Discount factor

The objective is to find optimal policy $\pi^*$ maximizing:

$$V^{\pi}(s) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s, \pi\right]$$

**Common Algorithms:**

- **Q-Learning:** Temporal difference method learning action-value function $Q(s, a)$
- **Deep Q Networks (DQN):** Deep neural network approximating Q-function with experience replay
- **Policy Gradient Methods:** Directly optimize policy parameters $\theta$ via gradient ascent on expected return
- **Actor-Critic Algorithms:** Combine value function approximation with policy optimization

## 3. The Machine Learning Process

A rigorous ML project follows a systematic pipeline:

### 3.1 Problem Definition and Hypothesis Testing

Clearly articulate the task $T$, performance metric $P$, and establish baseline performance. Define whether the problem is classification, regression, clustering, or sequence modeling.

### 3.2 Data Collection and Curation

Gather data $\mathcal{D}$ from relevant sources. Assess data quality, quantity, and representativeness. The sample complexity—the number of training examples required to achieve desired generalization—is governed by:

$$n \geq \frac{1}{\epsilon^2}\left(\log|\mathcal{H}| + \log\frac{1}{\delta}\right)$$

for $\epsilon$-accuracy with probability $1-\delta$ (based on PAC learning theory).

### 3.3 Exploratory Data Analysis (EDA)

Perform descriptive statistical analysis:

- **Univariate:** Mean, median, mode, variance, skewness, kurtosis
- **Bivariate:** Correlation coefficients, scatter plots
- **Multivariate:** Covariance matrices, dimensionality assessment

### 3.4 Data Preprocessing and Feature Engineering

Critical preprocessing steps include:

- **Missing Value Imputation:** Mean/median imputation, KNN imputation, or modeling missingness
- **Normalization/Standardization:** $z = (x - \mu)/\sigma$ for standardization; min-max scaling for bounded ranges
- **Encoding Categorical Variables:** One-hot encoding, label encoding, target encoding
- **Feature Selection:** Filter methods (correlation), wrapper methods (RFE), embedded methods (Lasso)
- **Dimensionality Reduction:** PCA, t-SNE, UMAP for visualization

### 3.5 Model Selection

Select hypothesis space $\mathcal{H}$ based on:

- **Bias-Variance Tradeoff:** Model complexity vs. generalization error
- **Interpretability Requirements:** Linear models vs. black-box approaches
- **Computational Constraints:** Training and inference time

**Theorem (Bias-Variance Decomposition):** For squared loss, the expected prediction error decomposes as:

$$\mathbb{E}[(y - \hat{f}(\mathbf{x}))^2] = \text{Bias}^2(\hat{f}) + \text{Var}(\hat{f}) + \sigma^2$$

where $\sigma^2$ is irreducible error. High-bias models (underfitting) have large $\text{Bias}^2$; high-variance models (overfitting) have large $\text{Var}$.

### 3.6 Model Training and Regularization

Optimize model parameters using:

- **Gradient Descent:** $\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}(\theta)$
- **Stochastic Gradient Descent (SGD):** Gradient computed on mini-batches
- **Regularization:** L1 (Lasso), L2 (Ridge), Elastic Net to prevent overfitting

**Cross-Validation:** Use $k$-fold CV to estimate generalization error:

$$\hat{R}_{CV} = \frac{1}{k} \sum_{i=1}^{k} \hat{R}_i$$

### 3.7 Model Evaluation

Select appropriate metrics:

| Problem Type   | Metrics                                                         |
| -------------- | --------------------------------------------------------------- |
| Classification | Accuracy, Precision, Recall, F1-Score, AUC-ROC, Log Loss        |
| Regression     | MSE, RMSE, MAE, R², Adjusted R²                                 |
| Clustering     | Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index |

### 3.8 Deployment and Monitoring

Deploy model in production, monitor for:

- **Concept Drift:** $P(y|\mathbf{x})$ changes over time
- **Data Drift:** $P(\mathbf{x})$ changes
- **Model Decay:** Degradation in performance metrics

Implement continuous monitoring, A/B testing, and periodic retraining pipelines.

## 4. Key Theoretical Concepts

### 4.1 Overfitting and Underfitting

- **Underfitting:** High bias, model too simple for data complexity. Solution: Increase model complexity, add features, reduce regularization.
- **Overfitting:** High variance, model memorizes training data. Solution: Regularization, cross-validation, early stopping, dropout (neural networks), increase training data.

### 4.2 VC Dimension and PAC Learning

The Vapnik-Chervonenkis (VC) dimension measures the capacity of a hypothesis class $\mathcal{H}$—the maximum cardinality of a set that can be shattered (perfectly classified) by $\mathcal{H}$.

**Theorem (VC Generalization Bound):** With probability at least $1-\delta$:

$$R(h) \leq \hat{R}(h) + \sqrt{\frac{h(\log\frac{2n}{h} + 1) - \log\frac{\delta}{4}}{n}}$$

where $h$ is the VC dimension. This bound formalizes the tradeoff between empirical risk and model complexity.

### 4.3 Regularization and Capacity Control

Regularization explicitly controls hypothesis space complexity:

- **Ridge Regression (L2):** $\min_{\mathbf{w}} \sum_{i=1}^{n} (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \lambda \|\mathbf{w}\|_2^2$
- **Lasso (L1):** $\min_{\mathbf{w}} \sum_{i=1}^{n} (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \lambda \|\mathbf{w}\|_1$

Lasso performs feature selection by driving irrelevant coefficients to exactly zero.

## 5. Review Questions

### Question 1 (Application - Numerical)

Consider a binary classification problem with 1000 training examples and 10 features. You train a decision tree with maximum depth 1 (stump) and obtain training accuracy of 70%. When you increase the depth to 10, training accuracy becomes 98%. Evaluate which model is likely to generalize better and compute the apparent overfitting ratio.

### Question 2 (Analysis - Conceptual)

Given the bias-variance decomposition $E[(y - \hat{f}(x))^2] = \text{Bias}^2 + \text{Var} + \sigma^2$, analyze how each component changes as you: (a) increase polynomial degree from 1 to 10, (b) increase training sample size from 100 to 10000, (c) add L2 regularization with increasing $\lambda$.

### Question 3 (Proof-Based)

Prove that for the 0-1 loss function, the Bayes optimal classifier is the function that assigns each $\mathbf{x}$ to the class with highest conditional probability $P(y|\mathbf{x})$. This is known as the Bayes classifier.

### Question 4 (Application - Algorithm Comparison)

Suppose you have a dataset with 10,000 features but only 500 samples. (a) Which learning paradigm and specific algorithm would you recommend and why? (b) Derive or state the sample complexity bound. (c) Explain how you would use regularization to address the high-dimensionality problem.
