# Types of Machine Learning

## Introduction

Machine learning algorithms can be categorized based on the nature of feedback signals available during training. Understanding this classification is fundamental to problem formulation, algorithm selection, and performance evaluation. The three primary paradigms—**supervised learning**, **unsupervised learning**, and **reinforcement learning**—differ fundamentally in their objectives, mathematical formulations, and computational requirements. Additionally, hybrid paradigms such as semi-supervised and self-supervised learning have emerged to address practical limitations in data annotation and to leverage abundant unlabeled data.

## 1. Supervised Learning

### 1.1 Formal Definition

Supervised learning involves learning a mapping function $f: \mathcal{X} \rightarrow \mathcal{Y}$ from a labeled dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{n}$, where $x_i \in \mathcal{X} \subseteq \mathbb{R}^d$ and $y_i \in \mathcal{Y}$. The goal is to minimize the **expected loss** (risk):

$$R(f) = \mathbb{E}_{(x,y) \sim P}[L(f(x), y)]$$

where $L: \mathcal{Y} \times \mathcal{Y} \rightarrow \mathbb{R}^+$ is a loss function (e.g., 0-1 loss, squared loss, cross-entropy). Since the true distribution $P$ is unknown, we minimize the **empirical risk**:

$$\hat{R}(f) = \frac{1}{n} \sum_{i=1}^{n} L(f(x_i), y_i)$$

The **bias-variance decomposition** provides theoretical insight into generalization:

$$\mathbb{E}[(y - \hat{f}(x))^2] = \text{Bias}^2(\hat{f}) + \text{Var}(\hat{f}) + \sigma^2$$

### 1.2 Classification vs. Regression

| Aspect        | Classification                            | Regression                                    |
| ------------- | ----------------------------------------- | --------------------------------------------- |
| Output Space  | Discrete $\mathcal{Y} = \{1, 2, ..., k\}$ | Continuous $\mathcal{Y} \subseteq \mathbb{R}$ |
| Loss Function | Cross-entropy, hinge loss                 | Mean squared error (MSE), MAE                 |
| Evaluation    | Accuracy, Precision, Recall, F1, AUC-ROC  | $R^2$, RMSE, MAE                              |
| Examples      | Logistic Regression, SVM, Neural Networks | Linear Regression, Decision Trees             |

### 1.3 Algorithm Complexity Analysis

| Algorithm         | Training Time                                  | Space Complexity   | Inference Time                      |
| ----------------- | ---------------------------------------------- | ------------------ | ----------------------------------- |
| Linear Regression | $O(nd^2 + d^3)$                                | $O(d)$             | $O(d)$                              |
| k-NN              | $O(1)$                                         | $O(nd)$            | $O(nd)$                             |
| Decision Tree     | $O(nd \log n)$                                 | $O(\text{nodes})$  | $O(\text{depth})$                   |
| SVM (Kernel)      | $O(n^2 \text{ to } n^3)$                       | $O(n)$             | $O(\text{support vectors} \cdot d)$ |
| Neural Network    | $O(\text{epochs} \cdot n \cdot \text{params})$ | $O(\text{params})$ | $O(\text{params})$                  |

### 1.4 Practical Considerations

- **Labeling Cost**: Human annotation is expensive; active learning can reduce labeled data requirements
- **Overfitting**: Regularization (L1/L2, dropout) mitigates high variance
- **Underfitting**: Increase model capacity or engineer better features

## 2. Unsupervised Learning

### 2.1 Formal Definition

Unsupervised learning discovers structure in data without labeled responses. Given $\mathcal{D} = \{x_i\}_{i=1}^{n}$ drawn from unknown distribution $P$, the objective is to learn underlying patterns, typically via **density estimation** or **latent variable models**.

For **parametric density estimation** (e.g., Gaussian mixture models), we maximize the log-likelihood:

$$\theta^* = \arg\max_\theta \sum_{i=1}^{n} \log p(x_i | \theta)$$

The **EM algorithm** provides iterative optimization for latent variable models:

1. **E-step**: Compute expected latent variables $Q_i(z) = p(z | x_i, \theta^{old})$
2. **M-step**: Maximize expected complete-data log-likelihood

### 2.2 Clustering

**k-Means Algorithm**:

- Objective: $\min \sum_{j=1}^{k} \sum_{x_i \in C_j} \|x_i - \mu_j\|^2$
- Complexity: $O(nkdI)$ where $I$ = iterations
- Convergence: Guaranteed to local optimum

**Gaussian Mixture Models (GMM)**:

- Probabilistic extension allowing soft clustering
- Uses EM algorithm for parameter estimation
- Provides posterior probabilities $p(z_j | x_i)$

### 2.3 Dimensionality Reduction

| Method       | Objective                                        | Complexity                                     | Applications               |
| ------------ | ------------------------------------------------ | ---------------------------------------------- | -------------------------- |
| PCA          | Maximize variance, minimize reconstruction error | $O(\min(nd^2, dn^2))$                          | Compression, visualization |
| t-SNE        | Preserve neighborhood structure                  | $O(n^2)$                                       | Visualization              |
| Autoencoders | Minimize reconstruction loss                     | $O(\text{epochs} \cdot n \cdot \text{params})$ | Deep compression           |

### 2.4 Association Rule Mining

- **Support**: $P(A \cup B)$
- **Confidence**: $P(B|A) = P(A \cup B) / P(A)$
- **Lift**: $\frac{P(A \cup B)}{P(A) \cdot P(B)}$

Apriori algorithm: $O(m \cdot n)$ per pass where $m$ = number of itemsets.

## 3. Reinforcement Learning

### 3.1 Markov Decision Process (MDP) Formalism

An RL problem is formally defined as an MDP tuple $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$:

- $\mathcal{S}$: State space
- $\mathcal{A}$: Action space
- $P(s'|s, a)$: Transition probability function
- $R(s, a, s')$: Reward function
- $\gamma \in [0, 1)$: Discount factor

The **return** at time $t$ is $G_t = \sum_{i=0}^{\infty} \gamma^i r_{t+i}$.

### 3.2 Bellman Equations

The **state-value function** $V^\pi(s)$ under policy $\pi$ satisfies:

$$V^\pi(s) = \sum_{a} \pi(a|s) \sum_{s'} P(s'|s, a)[R(s, a, s') + \gamma V^\pi(s')]$$

The **optimal value function** satisfies the **Bellman optimality equation**:

$$V^*(s) = \max_a \sum_{s'} P(s'|s, a)[R(s, a, s') + \gamma V^*(s')]$$

### 3.3 RL Algorithm Classification

| Category     | Examples                | Characteristics                |
| ------------ | ----------------------- | ------------------------------ |
| Value-Based  | Q-Learning, DQN         | Learn $Q(s,a)$, extract policy |
| Policy-Based | REINFORCE, Actor-Critic | Directly optimize $\pi$        |
| Model-Based  | Dyna, MCTS              | Learn transition model         |

**Exploration-Exploitation Trade-off**:

- $\epsilon$-greedy: With probability $\epsilon$, explore random action
- UCB (Upper Confidence Bound): $a_t = \arg\max_a \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]$
- Thompson Sampling: Bayesian approach using posterior sampling

### 3.4 Complexity Considerations

| Algorithm       | Sample Complexity                                   | Function Approximation             |
| --------------- | --------------------------------------------------- | ---------------------------------- | --- | ----------- | --------------------------- | ---------------------------------------------- |
| Q-Learning      | $O(\frac{                                           | \mathcal{S}                        |     | \mathcal{A} | }{(1-\gamma)^2\epsilon^2})$ | May diverge without function class constraints |
| Policy Gradient | $O(\frac{\text{Var}(\nabla J)}{\text{batch size}})$ | Converges to local optimum         |
| DQN             | Deep network training complexity                    | Target network stabilizes learning |

## 4. Hybrid and Advanced Paradigms

### 4.1 Semi-Supervised Learning

Leverages both labeled and unlabeled data:

- **Self-training**: Train on labeled data, pseudo-label unlabeled data, retrain
- **Co-training**: Multiple views of data, each classifier labels for others
- **Graph-based**: Propagate labels through similarity graph

Theoretical guarantee: If $P(Y|X)$ is low-dimensional or clusters exist in $\mathcal{X}$, unlabeled data improves bounds.

### 4.2 Self-Supervised Learning

Creates supervisory signals from data itself:

- **Contrastive learning**: Maximize similarity between augmented views
- **Predictive tasks**: Predict masked portions (e.g., BERT, MAE)
- **Pretext tasks**: Rotation prediction, jigsaw puzzles

### 4.3 Multi-Arm Bandits

Simplified RL with single state:

- **Regret**: $\text{Regret}(T) = \sum_{t=1}^{T} [r_{a^*} - r_{a_t}]$
- **UCB1**: $O(\log T)$ regret in stochastic bandits
- **Exp3**: $O(\sqrt{KT})$ for adversarial bandits

## 5. Comparative Analysis

| Criterion        | Supervised                         | Unsupervised            | Reinforcement                                          |
| ---------------- | ---------------------------------- | ----------------------- | ------------------------------------------------------ |
| Feedback         | Labels                             | No feedback             | Rewards                                                |
| Objective        | Minimize prediction loss           | Discover structure      | Maximize cumulative reward                             |
| Data Requirement | $(\mathcal{X}, \mathcal{Y})$ pairs | $\mathcal{X}$ only      | $(\mathcal{S}, \mathcal{A}, \mathcal{R})$ trajectories |
| Convergence      | Empirical risk $\rightarrow$ 0     | Likelihood maximization | Policy evaluation $\rightarrow$ optimal                |
| Interpretability | Generally high (linear models)     | Moderate                | Low                                                    |

## 6. Hard MCQs

### Question 1

A researcher has 10,000 unlabeled images and 500 labeled images of cats and dogs. Which approach would yield the best classification performance?

A) Train only on 500 labeled images using SVM
B) Use k-means clustering on all images and assign cluster labels
C) Train on labeled images, then use the model to pseudo-label unlabeled images (self-training)
D) Use random guessing

**Answer**: C. Self-training leverages unlabeled data distribution while bootstrapstrapping from limited labels.

### Question 2

Given an MDP with $\gamma = 0.9$, state values $V(s_1) = 10$, $V(s_2) = 5$, and transition $P(s_2|s_1, a_1) = 0.8$ with reward $R(s_1, a_1, s_2) = 2$, compute the Q-value $Q(s_1, a_1)$:

A) 2.0
B) 6.2
C) 10.2
D) 14.0

**Answer**: B. $Q(s_1, a_1) = \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma V(s')] = 0.8 \times [2 + 0.9 \times 5] = 0.8 \times 6.5 = 5.2$ (assuming deterministic transition to $s_2$ with probability 0.2 going elsewhere with 0 reward). If $P(s_2|s_1,a_1)=1$: $Q = 2 + 0.9 \times 5 = 6.5$.

### Question 3

For k-means clustering with $k=3$ on a dataset of $n=1000$ points in $d=10$ dimensions, assuming convergence in 20 iterations, the computational complexity is:

A) $O(1000 \times 10 \times 3 \times 20)$
B) $O(1000^2)$
C) $O(10^3)$
D) $O(1000 \times 3)$

**Answer**: A. $O(nkdI)$ where $n$=1000, $k$=3, $d$=10, $I$=20.

### Question 4

In a reinforcement learning scenario, an autonomous vehicle receives a reward of +100 for reaching the destination, -1 per timestep, and -50 for collisions. This reward function exhibits:

A) Sparse rewards only
B) Shaped rewards only
C) Both sparse and shaped rewards
D) No exploration requirement

**Answer**: C. The step penalty (-1) shapes the learning, while the terminal rewards (collision/arrival) are sparse.

### Question 5

Which unsupervised technique would be most appropriate for reducing 1000-dimensional gene expression data to 2 dimensions for cancer subtype visualization?

A) Linear Discriminant Analysis (LDA)
B) t-SNE
C) Principal Component Analysis (PCA)
D) K-means clustering

**Answer**: B. t-SNE excels at preserving local neighborhood structure for visualization, unlike PCA (global structure) or LDA (supervised).
