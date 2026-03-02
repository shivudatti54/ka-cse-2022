# Decision Tree Induction Algorithms

## Introduction to Decision Trees

A Decision Tree is a supervised learning algorithm used for both classification and regression tasks. It models decisions and their possible consequences as a tree-like structure, comprising nodes, branches, and leaves. The model learns simple decision rules inferred from the data features to predict the value of a target variable.

**Key Components of a Decision Tree:**

- **Root Node:** Represents the entire dataset, which is then split.
- **Internal/Decision Nodes:** A sub-node that splits into further sub-nodes based on a condition.
- **Leaf/Terminal Node:** The final node that represents a class label (in classification) or a continuous value (in regression).
- **Branches/Edges:** The outcome of a split, connecting one node to another.

```
Example Structure:
         [Root Node: Entire Dataset]
                 |
         / (Condition A) \
   [Internal Node]    [Leaf Node: Class X]
         |
   / (Condition B) \
[Leaf: Class Y]  [Leaf: Class Z]
```

## The Need for Tree Induction Algorithms

Building a decision tree manually for a dataset with many features and instances is infeasible. An algorithm is needed to automatically:

1.  Select which feature to split on at each node.
2.  Determine the optimal split point/value for that feature.
3.  Decide when to stop splitting and create a leaf node.

These algorithms systematically navigate the vast space of possible trees to find a model that is both accurate and generalizable.

## Core Concepts in Tree Induction

### 1. Splitting Criteria (Attribute Selection Measures)

The algorithm needs a metric to evaluate and compare the "goodness" of potential splits. The goal is to select the split that creates the purest subsets (for classification) or the most homogeneous subsets (for regression).

#### For Classification Trees:

**a) Information Gain (IG)**
Based on Claude Shannon's information theory and the concept of entropy. Entropy measures the impurity or uncertainty in a set of data.

- **Entropy:** $Entropy(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$
  Where $S$ is the dataset, $c$ is the number of classes, and $p_i$ is the proportion of instances belonging to class $i$.
- **Information Gain:** Measures the reduction in entropy after splitting on an attribute $A$.
  $IG(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Entropy(S_v)$
  Where $Values(A)$ are the possible values of attribute $A$, and $S_v$ is the subset of $S$ where $A = v$.
  _The algorithm chooses the attribute with the highest Information Gain._

**b) Gini Impurity**
Measures the probability of incorrectly classifying a randomly chosen element if it were labeled according to the class distribution in the subset.

- **Gini Index:** $Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$
- The decrease in Gini Impurity after a split is calculated similarly to Information Gain. The attribute with the largest decrease (Gini Gain) is preferred.

**Comparison: Entropy vs. Gini**
| Metric | Calculation | Range | Behavior |
| :--- | :--- | :--- | :--- |
| **Entropy** | Logarithmic | 0 (pure) to 1 (max impurity) | Tends to create slightly more balanced trees |
| **Gini** | Quadratic | 0 (pure) to 0.5 (max impurity) | Slightly faster to compute, often results in similar trees |

#### For Regression Trees:

The goal is to minimize variance in the resulting subsets.

- **Variance:** Measures how far data points are from the mean.
  $Variance(S) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \bar{y})^2$
- The splitting criterion is the **weighted variance reduction**.
  $VarianceReduction(S, A) = Variance(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Variance(S_v)$
  The split that results in the maximum variance reduction is chosen.

### 2. Stopping Criteria

To prevent a tree from growing infinitely and overfitting the training data, stopping conditions are applied:

- **Maximum Depth:** Tree growth stops once a specified depth is reached.
- **Minimum Samples Split:** A node must have at least this many samples to be split.
- **Minimum Samples Leaf:** A leaf node must have at least this many samples.
- **Minimum Impurity Decrease:** A split will only be performed if it reduces impurity by at least this value.
- **No Improvement:** Stop if no split leads to a significant improvement (e.g., in variance reduction).

### 3. Tree Pruning

Building a tree until all leaves are pure often leads to overfitting. Pruning is a technique to reduce the size of a tree by removing sections that provide little predictive power.

- **Pre-pruning (Early Stopping):** Stopping the tree-building process early using the criteria above.
- **Post-pruning:** Building the full tree first and then removing branches that do not provide a significant gain in performance on a validation dataset. A common method is **Cost-Complexity Pruning** (also known as weakest link pruning), which minimizes a function $R_\alpha(T) = R(T) + \alpha|T|$, where $R(T)$ is the error rate of the tree, $|T|$ is the number of leaf nodes, and $\alpha$ is a complexity parameter.

## Popular Induction Algorithms

### 1. ID3 (Iterative Dichotomiser 3)

- **Key Features:** Uses Information Gain for splitting. Designed for categorical data only. Does not handle missing values or numerical features directly (they must be discretized first). Prone to overfitting as it grows trees until purity.
- **Process:**
  1.  Start at the root node with the entire dataset.
  2.  Calculate IG for all features.
  3.  Split the dataset on the feature with the highest IG.
  4.  Recursively repeat the process for each child node.

### 2. C4.5 (Successor to ID3)

- **Key Improvements over ID3:**
  - Handles both categorical and continuous features (by finding the optimal split point for continuous values).
  - Handles missing values by distributing instances probabilistically.
  - Uses **Gain Ratio** to correct Information Gain's bias towards features with many unique values.
    $GainRatio(S, A) = \frac{IG(S, A)}{SplitInfo(S, A)}$
    $SplitInfo(S, A) = -\sum_{v \in Values(A)} \frac{|S_v|}{|S|} \log_2(\frac{|S_v|}{|S|})$
  - Includes post-pruning.

### 3. CART (Classification and Regression Trees)

- **Key Features:** Can build both classification and regression trees.
  - For **classification,** uses Gini Impurity.
  - For **regression,** uses variance reduction.
- Creates **binary trees** (each split has exactly two branches). This simplifies the model structure.
- Uses cost-complexity pruning.
- The algorithm is the basis for powerful ensemble methods like Random Forest and Gradient Boosting.

**Comparison of Algorithms**
| Algorithm | Splitting Criterion | Tree Type | Handles Numeric Features? | Pruning |
| :--- | :--- | :--- | :--- | :--- |
| **ID3** | Information Gain | Multi-way | No (requires discretization) | No |
| **C4.5** | Gain Ratio | Multi-way | Yes | Post-pruning |
| **CART** | Gini / Variance | Binary | Yes | Cost-complexity pruning |

## Worked Example: ID3 for a Simple Dataset

Let's predict if someone will go to a concert based on Weather, Company, and Budget.

**Training Data:**
| Weather | Company | Budget | Go? |
| :--- | :--- | :--- | :--- |
| Sunny | Friends | High | Yes |
| Sunny | Alone | High | No |
| Overcast| Friends | High | Yes |
| Rainy | Friends | Low | No |
| Rainy | Alone | Low | No |

**Step 1: Calculate Initial Entropy**
Total instances: 5. Class distribution: Yes=2, No=3.
$Entropy(S) = -(\frac{2}{5}\log_2(\frac{2}{5}) + \frac{3}{5}\log_2(\frac{3}{5})) \approx -(-0.5288 -0.4422) \approx 0.971$

**Step 2: Calculate IG for each feature**

- **IG(Weather):**
  - Values: Sunny (2 instances: 1Y,1N), Overcast (1Y), Rainy (2N)
  - $Entropy(Sunny) = -(\frac{1}{2}\log_2(\frac{1}{2}) + \frac{1}{2}\log_2(\frac{1}{2})) = 1.0$
  - $Entropy(Overcast) = 0$ (pure)
  - $Entropy(Rainy) = 0$ (pure)
  - Weighted Avg: $(\frac{2}{5} * 1.0) + (\frac{1}{5} * 0) + (\frac{2}{5} * 0) = 0.4$
  - $IG(S, Weather) = 0.971 - 0.4 = 0.571$
- **IG(Company):** (Calculate similarly, will be lower)
- **IG(Budget):** (Calculate similarly, will be lower)

**Step 3: Split on Best Feature**
Weather has the highest IG (0.571), so it becomes the root node.

```
         [Weather?]
         /    |    \
 Sunny / Overcast| Rainy \
     [ ]        [Yes]    [No]
(Impure node)
```

We now recursively apply the same process to the "Sunny" branch, but only using the 2 instances where Weather=Sunny. The algorithm would next split this node on the feature with the highest IG from the remaining features (Company, Budget).

## Advantages and Disadvantages

| Advantages                                                               | Disadvantages                                                                                   |
| :----------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **Easy to Understand:** The model is white-box and highly interpretable. | **Overfitting:** Can easily create overly complex trees that memorize noise. Requires pruning.  |
| **Little Data Prep:** No need for feature scaling or normalization.      | **Instability:** Small changes in data can lead to a completely different tree (high variance). |
| **Handles Mixed Data:** Works with both numerical and categorical data.  | **Biased to Dominant Features:** Trees can be biased towards features with more levels.         |
| **Non-linear:** Can model non-linear decision boundaries.                | **Not Great for Extrapolation:** Poor at predicting outside the range of training data.         |

## Exam Tips

1.  **Calculation Questions:** Be prepared to calculate Entropy, Gini, Information Gain, and Gain Ratio for a small dataset. Practice is key.
2.  **Algorithm Differences:** Clearly explain the differences between ID3, C4.5, and CART. A comparison table in your answer is very effective.
3.  **Overfitting:** Always mention the problem of overfitting in the context of decision trees and explain the solutions: pruning (both pre and post) and setting hyperparameters (max depth, min samples leaf).
4.  **Terminology:** Define key terms like root node, leaf node, splitting criterion, and pruning accurately.
5.  **Interpret a Tree:** You may be given a diagram of a decision tree and asked to classify a sample or explain its logic.
6.  **Advantages/Disadvantages:** Be ready to list and briefly explain the pros and cons of using decision trees.
