# Decision Tree Induction Algorithms

## Introduction

A Decision Tree constitutes a fundamental supervised learning paradigm employed extensively for both classification and regression tasks. Unlike parametric models that estimate a fixed set of parameters, decision trees adopt a non-parametric approach, constructing predictive models by learning decision rules inferred from the underlying data features. The resulting model architecture assumes a hierarchical tree structure, wherein each internal node represents a test condition on a specific feature, each branch embodies the outcome of said test, and each leaf node signifies a final prediction—either a class label for classification problems or a continuous value for regression tasks.

The theoretical appeal of decision trees stems from several advantageous properties: interpretability (the decision process can be visualized and understood intuitively), handling of both categorical and numerical features without extensive preprocessing, and computational efficiency during prediction phase. These characteristics render decision trees particularly suitable for applications requiring model transparency, such as medical diagnosis and credit risk assessment.

## Structural Components

The decision tree architecture comprises four essential structural elements:

- **Root Node**: The premier node of the tree, representing the complete training dataset. This node undergoes the first partitioning operation based on the most informative attribute.
- **Internal Nodes (Decision Nodes)**: Nodes possessing at least one incoming edge and two or more outgoing edges. Each internal node evaluates a specific condition pertaining to a feature, thereby effectuating a partition of the data subset it represents.
- **Leaf Nodes (Terminal Nodes)**: Nodes possessing exactly one incoming edge and no outgoing edges. In classification contexts, leaf nodes represent class labels; in regression contexts, they represent predicted numerical values.
- **Edges/Branches**: The connective elements linking parent nodes to child nodes, representing the outcomes of conditional tests.

## Theoretical Foundations of Splitting Criteria

The efficacy of a decision tree algorithm fundamentally depends upon the attribute selection measure employed to determine optimal splitting points. The underlying principle seeks to maximize homogeneity within resulting subsets while maintaining heterogeneity between subsets.

### Entropy and Information Gain

**Entropy** originates from information theory and provides a mathematical measure of uncertainty or impurity within a dataset. Formally, for a dataset $S$ containing $c$ classes with proportions $p_i$:

$$H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

**Theorem (Properties of Entropy)**: Entropy achieves its minimum value of 0 when all instances belong to a single class (pure subset), and attains its maximum value of $\log_2(c)$ when instances are uniformly distributed across all classes.

_Proof_: Consider the function $f(p) = -p \log_2(p)$ for $p \in (0,1]$. Using Lagrange multipliers to maximize $H(S) = \sum_{i} f(p_i)$ subject to $\sum_i p_i = 1$, we find that the maximum occurs when all $p_i = 1/c$, yielding $H_{max} = \log_2(c)$. The minimum occurs when some $p_i = 1$ and others approach 0, approaching $H_{min} = 0$. ∎

**Information Gain** quantifies the reduction in entropy achieved by partitioning the dataset according to a particular attribute $A$:

$$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$

Where $Values(A)$ denotes the set of possible values for attribute $A$, and $S_v$ represents the subset of $S$ for which attribute $A$ takes value $v$.

The attribute exhibiting maximum Information Gain is selected for splitting at each node. This selection mechanism is theoretically justified by the principle that optimal splits should maximally reduce uncertainty regarding class membership.

### Gini Impurity

**Gini Impurity** provides an alternative measure of node impurity, calculating the probability of misclassification if labels were assigned according to class distribution:

$$Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$$

**Theorem (Relationship between Entropy and Gini)**: For binary classification, Gini impurity and entropy produce virtually identical splitting decisions. For multi-class problems, Gini tends to isolate the most frequent class more aggressively, while entropy produces more balanced partitions.

_Proof_: Using Taylor expansion around $p = 0.5$, we observe that $Gini(p) = 4p(1-p)$ and $H(p) = -p \log_2(p) - (1-p)\log_2(1-p)$ exhibit similar monotonic behavior in the impurity region. Both functions are concave and achieve maximum at $p = 0.5$. ∎

The Gini gain is computed analogously to Information Gain:
$$GiniGain(S, A) = Gini(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Gini(S_v)$$

### Variance Reduction for Regression Trees

For continuous target variables, splitting criteria aim to minimize variance within subsets:

$$Variance(S) = \frac{1}{|S|} \sum_{i \in S} (y_i - \bar{y})^2$$

Where $\bar{y}$ denotes the mean of target values in $S$. The variance reduction criterion selects the attribute and split point maximizing:

$$VR(S, A) = Variance(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Variance(S_v)$$

## Algorithmic Frameworks

### ID3 Algorithm (Iterative Dichotomiser 3)

The ID3 algorithm, developed by Ross Quinlan in 1986, represents the foundational decision tree induction algorithm.

**Algorithm ID3**:

```
Input: Training set S, Feature set F
Output: Decision tree T

1. If all instances in S belong to same class C:
 Return leaf node with label C

2. If F is empty:
 Return leaf node with majority class in S

3. Select feature A ∈ F with highest Information Gain
4. Create decision node with feature A
5. For each value v ∈ Values(A):
 - Let S_v = {x ∈ S | A(x) = v}
 - If S_v is empty:
 Add leaf node with majority class in S
 - Else:
 Add subtree ID3(S_v, F - {A})

6. Return decision node
```

**Time Complexity**: $O(|F| \cdot |S| \log |S|)$ for building a tree of size $O(|S|)$.

**Limitations**: ID3 exclusively handles categorical attributes and exhibits bias toward attributes possessing numerous values, as these attributes tend to produce artificially high Information Gain by creating small, pure partitions.

### C4.5 Algorithm

C4.5 addresses several limitations of ID3 through following enhancements:

**Gain Ratio Normalization**: To mitigate bias toward multi-valued attributes, C4.5 introduces the Gain Ratio:

$$GainRatio(S, A) = \frac{IG(S, A)}{SplitInformation(S, A)}$$

Where:
$$SplitInformation(S, A) = -\sum_{v \in Values(A)} \frac{|S_v|}{|S|} \log_2\left(\frac{|S_v|}{|S|}\right)$$

This normalization penalizes attributes producing numerous small partitions.

**Continuous Attribute Handling**: C4.5 identifies optimal split points for numerical attributes by evaluating all candidate thresholds between consecutive sorted values and selecting the threshold maximizing Information Gain.

**Missing Value Handling**: Instances with missing attribute values are distributed probabilistically across branches according to known class distributions.

**Algorithm C4.5**:

```
Input: Training set S, Feature set F
Output: Decision tree T

1-3. Identical to ID3, substituting Gain Ratio for Information Gain

4. For continuous attributes:
 - Sort values
 - Evaluate split at each midpoint
 - Select optimal threshold

5. Handle missing values:
 - Distribute instances probabilistically
 - Weight contributions to entropy calculation

6. Return decision node with pruning (see Section 5)
```

### CART (Classification and Regression Trees)

CART, developed by Breiman et al. (1984), employs Gini impurity for classification and variance for regression. CART constructs binary trees exclusively—each internal node produces exactly two child nodes.

**Binary Split Selection**: For continuous attributes, CART selects threshold $t$ maximizing:
$$GiniGain(S, A, t) = Gini(S) - \frac{|S_L|}{|S|} Gini(S_L) - \frac{|S_R|}{|S|} Gini(S_R)$$

Where $S_L = \{x \in S | A(x) \leq t\}$ and $S_R = S - S_L$.

**Regression Split Selection**: For continuous targets:
$$VarianceReduction(S, A, t) = Variance(S) - \frac{|S_L|}{|S|} Variance(S_L) - \frac{|S_R|}{|S|} Variance(S_R)$$

## Stopping Criteria and Pruning Strategies

### Pre-pruning (Early Stopping)

Pre-pruning terminates tree construction prematurely based on predefined conditions:

- **Maximum Depth**: $depth(T) \leq d_{max}$
- **Minimum Samples per Split**: $|S| \geq n_{min}$ required for node splitting
- **Minimum Impurity Decrease**: $Gain(S, A) \geq \delta_{min}$
- **Maximum Features**: Consider only random subset of features at each node

While computationally efficient, pre-pruning risks premature termination, potentially sacrificing predictive accuracy.

### Post-pruning (Cost-Complexity Pruning)

Post-pruning constructs the complete tree subsequently removing subtrees exhibiting insufficient statistical significance. **Cost-Complexity Pruning** minimizes:

$$R_\alpha(T) = R(T) + \alpha|T|$$

Where $R(T)$ denotes the misclassification rate (or mean squared error for regression), $|T|$ represents the number of leaf nodes, and $\alpha$ is the complexity parameter.

**Theoretical Justification**: The complexity parameter $\alpha$ governs the bias-variance tradeoff. Smaller $\alpha$ values permit complex trees (lower bias, higher variance), while larger $\alpha$ values enforce simpler trees (higher bias, lower variance). Cross-validation typically determines optimal $\alpha$.

**Algorithm for Finding Optimal Pruned Trees**:

```
1. Build complete tree T_max
2. For α from 0 to ∞:
 - Find weakest link: internal node where subtree error equals node error
 - Collapse weakest link to create T_α
 - Stop when single-node tree remains
3. Select T_α minimizing validation error
```

## Practical Considerations and Complexity Analysis

### Computational Complexity

Building decision trees requires evaluating all features and all possible split points:

- **Time Complexity**: $O(m \cdot n \log n)$ where $m$ denotes number of features and $n$ denotes number of training instances.
- **Space Complexity**: $O(n)$ for storing the tree structure and training data.

### Handling Continuous vs. Categorical Attributes

Continuous attributes necessitate evaluating $O(n \log n)$ potential split points (sorted values), whereas categorical attributes with $k$ distinct values require evaluating $O(2^{k-1} - 1)$ possible partitions for binary trees.

### Overfitting and Underfitting

Decision trees exhibit high variance, readily adapting to training data noise. Strategies for mitigation include:

1. Ensemble methods (Random Forests, Gradient Boosted Trees)
2. Regularization through tree constraints
3. Pruning strategies discussed previously

---

## Assessment Questions

### Hard Level Questions

**Question 1**: Consider a dataset $S$ with 100 instances belonging to two classes: 60 positive and 40 negative.

a) Calculate the entropy of $S$.
b) Suppose attribute $A$ splits $S$ into $S_1$ (40 instances: 30 positive, 10 negative) and $S_2$ (60 instances: 30 positive, 30 negative). Calculate Information Gain for attribute $A$.
c) If Gini impurity were used instead, which attribute would be preferred?

**Answer**:
a) $H(S) = -\frac{60}{100}\log_2(0.6) - \frac{40}{100}\log_2(0.4) = 0.971$ bits
b) $H(S_1) = -\frac{30}{40}\log_2(0.75) - \frac{10}{40}\log_2(0.25) = 0.811$ bits
$H(S_2) = -\frac{30}{60}\log_2(0.5) - \frac{30}{60}\log_2(0.5) = 1.0$ bits
$IG(S, A) = 0.971 - (0.4 \times 0.811 + 0.6 \times 1.0) = 0.175$ bits
c) Gini calculations yield identical preference since both $S_1$ and $S_2$ are non-pure subsets.

**Question 2**: Explain why Information Gain may exhibit bias toward attributes with numerous distinct values, and describe how C4.5 mitigates this limitation.

**Answer**: Attributes producing many distinct values create numerous small partitions, each potentially pure or near-pure, yielding artificially elevated Information Gain. For instance, a unique identifier attribute (e.g., transaction ID) yields maximum Information Gain ($IG = H(S)$) but possesses no generalization capability. C4.5 addresses this through Gain Ratio normalization, dividing Information Gain by the split information (entropy of the partition distribution). This penalty increases with the number of splits, counteracting the bias toward multi-valued attributes.

**Question 3**: Derive the relationship between Gini impurity and entropy, demonstrating their equivalence for binary classification.

**Answer**: For binary classification with proportions $(p, 1-p)$:

- Gini: $G(p) = 1 - (p^2 + (1-p)^2) = 2p(1-p)$
- Entropy: $H(p) = -p\log_2(p) - (1-p)\log_2(1-p)$

Using the approximation $\log_2(x) \approx \frac{x-1}{x\ln 2}$ near $x=1$:
$H(p) \approx \frac{1}{\ln 2} [p(1-p) + (1-p)(p)] = \frac{2p(1-p)}{\ln 2} \approx 1.44 \cdot G(p)$

Since $H(p)$ is a linear scaling of $G(p)$ for binary classification, maximizing either criterion produces identical splitting decisions.
