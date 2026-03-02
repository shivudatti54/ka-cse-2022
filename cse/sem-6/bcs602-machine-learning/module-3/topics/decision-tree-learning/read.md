# Decision Trees

## 1. Introduction

Decision trees are supervised learning algorithms that construct tree-structured models through recursive partitioning of the feature space. Each internal node represents a test on a feature, each branch corresponds to an outcome of that test, and each leaf node provides a prediction. The resulting model encodes a set of decision rules that map input features to predicted outputs.

## 2. Mathematical Foundation

### 2.1 Impurity Measures

Let $D$ be a dataset with $k$ classes, where $p_i$ denotes the proportion of samples belonging to class $i$.

**Definition 2.1 (Gini Impurity)**
The Gini impurity of a node is defined as:
$$Gini(D) = 1 - \sum_{i=1}^{k} p_i^2$$

**Theorem 2.1 (Range of Gini Impurity)**
For binary classification ($k=2$), Gini impurity ranges from 0 to 0.5.

_Proof_: Let $p_1 = p$ and $p_2 = 1-p$, where $p \in [0,1]$.
$$Gini(D) = 1 - [p^2 + (1-p)^2] = 1 - [p^2 + 1 - 2p + p^2] = 2p - 2p^2 = 2p(1-p)$$

Since $p(1-p)$ is a parabola with maximum at $p = 0.5$, the maximum value is $2(0.5)(0.5) = 0.5$. At $p = 0$ or $p = 1$, $Gini(D) = 0$. ∎

**Definition 2.2 (Entropy)**
$$Entropy(D) = -\sum_{i=1}^{k} p_i \log_2(p_i)$$

With the convention that $0 \log_2(0) = 0$.

**Theorem 2.2 (Range of Entropy)**
For binary classification, entropy ranges from 0 to 1.

_Proof_: Using similar notation as Theorem 2.1, $Entropy(D) = -[p \log_2 p + (1-p) \log_2(1-p)]$. This function is maximized at $p = 0.5$ with value 1, and minimized at boundaries with value 0. ∎

**Theorem 2.3 (Information Gain)**
The information gain from splitting on feature $A$ is:
$$IG(D, A) = Impurity(D) - \sum_{v \in Values(A)} \frac{|D_v|}{|D|} \cdot Impurity(D_v)$$

_Proof_: The weighted sum of child node impurities represents the expected impurity after the split. The reduction in impurity (gain) measures the improvement from partitioning the data. Maximizing IG corresponds to minimizing weighted average child impurity, thus producing purer partitions. ∎

### 2.2 Relationship Between Entropy and Gini

**Theorem 2.4 (Approximation)**
For small differences between class probabilities, Gini impurity and entropy provide similar rankings of splits. Specifically:
$$Gini(D) \approx \frac{1}{2} Entropy(D)$$

_Proof_: Using Taylor series expansion of $\log_2 p$ around $p = 0.5$, one can show the approximation holds. Both measures are concave functions of class probabilities, attaining maximum at uniform distribution. ∎

## 3. Tree Construction Algorithm

### 3.1 ID3 Algorithm (Iterative Dichotomiser 3)

```
Algorithm ID3(D, Features, Target)
 if all samples in D belong to same class c:
 return leaf node with class c
 if Features is empty:
 return leaf node with majority class in D
 select feature A ∈ Features that maximizes Information Gain
 create root node with test on A
 for each value v of A:
 create child node D_v = {samples in D with A = v}
 if D_v is empty:
 attach leaf with majority class from D
 else:
 attach ID3(D_v, Features \ {A}, Target) to branch v
 return root
```

### 3.2 CART Algorithm with Cost-Complexity Pruning

CART (Classification and Regression Trees) uses binary splits and cost-complexity pruning:

```
Algorithm CART(D, Features, α)
 // Phase 1: Build full tree
 T_max = BuildFullTree(D, Features)

 // Phase 2: Prune using cost-complexity
 T = CostComplexityPrune(T_max, α)
 return T

Function CostComplexityPrune(T, α):
 while T is not root:
 for each internal node t in T:
 compute g(t) = [R(t) - R(T_t)] / (|T_t| - 1)
 prune subtree at node with minimum g(t)
 if α < min(g(t)): break
 return pruned tree
```

Where $R(t)$ is the misclassification rate at node $t$, and $T_t$ is the subtree rooted at $t$.

## 4. Numerical Example: Information Gain Calculation

Consider dataset $D$ with 14 samples:

| ID  | Outlook  | Temperature | Humidity | Wind   | Play |
| --- | -------- | ----------- | -------- | ------ | ---- |
| 1   | Sunny    | Hot         | High     | Weak   | No   |
| 2   | Sunny    | Hot         | High     | Strong | No   |
| 3   | Overcast | Hot         | High     | Weak   | Yes  |
| 4   | Rainy    | Mild        | High     | Weak   | Yes  |
| 5   | Rainy    | Cool        | Normal   | Weak   | Yes  |
| 6   | Rainy    | Cool        | Normal   | Strong | No   |
| 7   | Overcast | Cool        | Normal   | Strong | Yes  |
| 8   | Sunny    | Mild        | High     | Weak   | No   |
| 9   | Sunny    | Cool        | Normal   | Weak   | Yes  |
| 10  | Rainy    | Mild        | Normal   | Weak   | Yes  |
| 11  | Sunny    | Mild        | Normal   | Strong | Yes  |
| 12  | Overcast | Mild        | High     | Strong | Yes  |
| 13  | Overcast | Hot         | Normal   | Weak   | Yes  |
| 14  | Rainy    | Mild        | High     | Strong | No   |

**Step 1**: Calculate entropy of parent node:

- $P(Yes) = 9/14$, $P(No) = 5/14$
- $Entropy(Parent) = -(9/14)\log_2(9/14) - (5/14)\log_2(5/14) = 0.940$

**Step 2**: Calculate entropy after splitting on Outlook:

- Sunny (5 samples): 2 Yes, 3 No → $Entropy = -(\frac{2}{5})\log_2(\frac{2}{5}) - (\frac{3}{5})\log_2(\frac{3}{5}) = 0.971$
- Overcast (4 samples): 4 Yes, 0 No → $Entropy = 0$
- Rainy (5 samples): 3 Yes, 2 No → $Entropy = 0.971$

**Step 3**: Calculate Information Gain:
$$IG(Outlook) = 0.940 - \frac{5}{14}(0.971) - \frac{4}{14}(0) - \frac{5}{14}(0.971) = 0.246$$

Similarly, we compute IG for other features and select the one with maximum gain.

## 5. Complexity Analysis

| Operation  | Best Case (Balanced) | Worst Case (Unbalanced) |
| ---------- | -------------------- | ----------------------- |
| Training   | O(n·d·log n)         | O(n·d·n)                |
| Prediction | O(log n)             | O(n)                    |
| Space      | O(n)                 | O(n)                    |

Where $n$ = number of samples, $d$ = number of features.

## 6. Overfitting Prevention

### 6.1 Pre-pruning (Early Stopping)

- Maximum depth: $\lceil \log_2 n \rceil$ prevents excessive growth
- Minimum samples per split: $m_{min}$ ensures statistical validity
- Minimum impurity decrease: $\delta$ requires meaningful splits

### 6.2 Post-pruning (Cost-Complexity Pruning)

**Definition 6.1 (Cost-Complexity Criterion)**
For a subtree $T_t$ rooted at node $t$:
$$R_\alpha(T_t) = R(T_t) + \alpha |T_t|$$

where $R(T_t)$ is the empirical risk, $|T_t|$ is the number of leaves, and $\alpha \geq 0$ is the complexity parameter.

The optimal subtree $T_\alpha \subseteq T_{max}$ minimizes $R_\alpha$.

## 7. Advantages and Limitations

**Advantages**:

- High interpretability: decision rules can be extracted
- Handles non-linear relationships
- Minimal data preprocessing (no normalization required)
- Built-in feature importance measures

**Limitations**:

- Greedy algorithm: locally optimal splits may not yield global optimum
- High variance: small data changes produce different trees
- Bias toward features with many levels (mitigated by gain ratio)
- Cannot model complex interactions between features

## 8. Applications

Decision trees serve as base learners for ensemble methods including Random Forest (bagging) and Gradient Boosting (boosting), which address the high variance limitation through aggregation.
