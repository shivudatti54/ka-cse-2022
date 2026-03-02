# Decision Tree Learning

## Introduction

Decision Tree Learning represents one of the most fundamental and widely-used supervised learning techniques in machine learning. It is a method for approximating discrete-valued target functions by learning decision rules inferred from data features. Unlike other machine learning algorithms that function as "black boxes," decision trees provide interpretable models where the learned knowledge can be visualized as a tree structure, making it particularly valuable for understanding how predictions are made.

In the context of the University of Delhi's Computer Science curriculum, decision tree learning holds significant importance because it forms the foundation for understanding more advanced ensemble methods like Random Forests and Gradient Boosting. The algorithm's ability to handle both categorical and numerical data, its natural handling of missing values, and its interpretability make it a preferred choice for many real-world applications including medical diagnosis, credit risk assessment, customer churn prediction, and fraud detection.

This chapter explores the theoretical foundations of decision tree learning, including the underlying principles of information theory that drive the tree-building process. We will examine the ID3 and C4.5 algorithms in detail, understand the concepts of entropy and information gain, and learn how to construct decision trees from training data. Additionally, we will discuss practical considerations including overfitting, pruning strategies, and techniques for handling continuous attributes.

## Key Concepts

### 1. Decision Tree Representation

A decision tree is a hierarchical structure consisting of nodes and directed edges. The tree has three types of nodes:

- **Root Node**: The topmost node that represents the entire dataset. It has no incoming edges but may have two or more outgoing edges.

- **Internal Nodes (Decision Nodes)**: These nodes represent tests on specific attributes. Each internal node has exactly one incoming edge and two or more outgoing edges.

- **Leaf Nodes (Terminal Nodes)**: These nodes represent class labels or constant values. They have exactly one incoming edge and no outgoing edges.

The path from the root to any leaf node represents a classification rule or a regression prediction. Each internal node tests the value of a particular attribute, and each branch corresponds to one of the possible values (or ranges) of that attribute.

### 2. Top-Down Induction of Decision Trees (TDIDT)

The most common algorithm for constructing decision trees follows a greedy top-down approach. The process begins at the root with the entire training set and recursively partitions the data based on attribute values. At each step, the algorithm selects the "best" attribute to split the data, creating child nodes for each possible value of that attribute. This process continues until stopping criteria are met, such as all instances in a node belonging to the same class or no remaining attributes to split.

### 3. Entropy - The Foundation of Information Theory

Entropy is a fundamental concept from information theory that measures the impurity or randomness in a dataset. In the context of decision tree learning, entropy quantifies the uncertainty associated with the class distribution in a set of examples.

For a binary classification problem where examples can belong to either class YES or class NO, the entropy is calculated as:

**Entropy(S) = -p_yes × log₂(p_yes) - p_no × log₂(p_no)**

Where:
- p_yes = |YES| / |S| (proportion of positive examples)
- p_no = |NO| / |S| (proportion of negative examples)

The entropy value ranges from 0 to 1:
- Entropy = 0: The set is perfectly pure (all examples belong to one class)
- Entropy = 1: The set is maximally impure (examples are equally divided)
- Entropy = 0.5: Maximum uncertainty in binary classification

For multi-class problems with k classes, the general formula is:

**Entropy(S) = Σᵢ pᵢ × log₂(pᵢ) for i = 1 to k**

### 4. Information Gain

Information Gain measures the reduction in entropy achieved by partitioning the examples according to a particular attribute. The attribute that provides the highest information gain is selected as the splitting attribute at each node.

The Information Gain of attribute A on set S is calculated as:

**Gain(S, A) = Entropy(S) - Σᵥ (|Sᵥ| / |S|) × Entropy(Sᵥ)**

Where:
- Sᵥ is the subset of S for which attribute A has value v
- |Sᵥ| is the size of the subset
- |S| is the total size of the set

The algorithm selects the attribute with the highest information gain because it provides the greatest reduction in uncertainty about the class labels.

### 5. ID3 Algorithm

The ID3 (Iterative Dichotomiser 3) algorithm, developed by Ross Quinlan in 1986, is the classic algorithm for constructing decision trees. The algorithm follows these steps:

1. Start with the training set S at the root node
2. If all examples in S belong to the same class C, create a leaf node labeled C
3. If no attributes remain, create a leaf node labeled with the majority class in S
4. Otherwise:
   - For each attribute A, calculate Gain(S, A)
   - Select the attribute A* with highest information gain
   - Create a decision node for A*
   - For each possible value v of A*:
     - Create a child node with subset Sᵥ = {examples in S where A* = v}
     - Recursively apply the algorithm to Sᵥ

### 6. C4.5 Algorithm

C4.5 is an improved version of ID3 developed by Quinlan in 1993. It addresses several limitations of ID3:

- **Split Information**: C4.5 uses Gain Ratio instead of Information Gain to handle attributes with many values
- **Continuous Attributes**: C4.5 can handle continuous attributes by finding optimal split points
- **Missing Values**: C4.5 has built-in handling for missing attribute values
- **Pruning**: C4.5 includes post-pruning mechanisms

The Gain Ratio is calculated as:

**GainRatio(S, A) = Gain(S, A) / SplitInformation(S, A)**

Where SplitInformation(S, A) = -Σᵥ (|Sᵥ|/|S|) × log₂(|Sᵥ|/|S|)

### 7. CART (Classification and Regression Trees)

CART is another popular decision tree algorithm that can be used for both classification and regression. Unlike ID3/C4.5 which use information gain, CART uses the Gini Index as the splitting criterion:

**Gini(S) = 1 - Σᵢ pᵢ²**

For a binary classification:
**Gini(S) = 2 × p × (1 - p)**

The Gini index measures the probability of misclassification if an example is randomly assigned according to the class distribution in S.

### 8. Overfitting in Decision Trees

Overfitting occurs when the decision tree becomes overly complex and captures noise in the training data rather than the underlying patterns. An overfit tree has high accuracy on training data but poor generalization to unseen data.

Two main strategies to address overfitting:

- **Pre-pruning (Early Stopping)**: Stop tree construction early by imposing conditions like:
  - Maximum tree depth
  - Minimum examples per node
  - Minimum information gain threshold

- **Post-pruning (Reduced Error Pruning)**: Build the complete tree first, then remove subtrees that do not contribute to accuracy on validation data.

### 9. Handling Continuous Attributes

Continuous (numerical) attributes require special handling in decision trees. The algorithm finds the best split point that divides the continuous range into two intervals:

1. Sort all values of the continuous attribute
2. Consider split points between consecutive distinct values
3. Evaluate each potential split using information gain or Gini index
4. Select the split point that maximizes the criterion

### 10. Practical Considerations

- **Attribute Selection**: While information gain tends to favor attributes with many values, gain ratio or Gini index provide alternatives
- **Handling Missing Values**: Strategies include assigning the most common value, distributing instances proportionally, or creating separate branches for "unknown"
- **Multi-class Problems**: Decision trees naturally handle multiple classes without any modification
- **Interpretability**: Decision trees provide white-box models that can be easily visualized and explained

## Examples

### Example 1: Calculating Entropy

Consider a training set S with 14 examples, where 9 examples belong to class YES and 5 examples belong to class NO.

Calculate the entropy of S:

**Step 1: Calculate proportions**
- p_yes = 9/14 = 0.6429
- p_no = 5/14 = 0.3571

**Step 2: Apply entropy formula**
Entropy(S) = -(0.6429 × log₂(0.6429)) - (0.3571 × log₂(0.3571))

Calculating logarithms:
- log₂(0.6429) ≈ -0.6366
- log₂(0.3571) ≈ -1.4852

Entropy(S) = -(0.6429 × -0.6366) - (0.3571 × -1.4852)
Entropy(S) = 0.4093 + 0.5304
Entropy(S) ≈ 0.940

This high entropy indicates significant impurity in the dataset.

### Example 2: Calculating Information Gain

Using the same dataset with entropy 0.940, consider splitting on attribute "Weather" which has three values: Sunny, Overcast, and Rainy.

- Sunny: 5 examples (2 YES, 3 NO)
- Overcast: 4 examples (4 YES, 0 NO)
- Rainy: 5 examples (3 YES, 2 NO)

**Step 1: Calculate entropy for each subset**

For Sunny:
p_yes = 2/5 = 0.4, p_no = 3/5 = 0.6
Entropy(Sunny) = -(0.4 × log₂(0.4)) - (0.6 × log₂(0.6))
= -(0.4 × -1.3219) - (0.6 × -0.7369)
= 0.5288 + 0.4421 = 0.9709

For Overcast:
p_yes = 4/4 = 1.0, p_no = 0/4 = 0
Entropy(Overcast) = -(1 × log₂(1)) - (0 × log₂(0)) = 0

For Rainy:
p_yes = 3/5 = 0.6, p_no = 2/5 = 0.4
Entropy(Rainy) = -(0.6 × log₂(0.6)) - (0.4 × log₂(0.4))
= -(0.6 × -0.7369) - (0.4 × -1.3219)
= 0.4421 + 0.5288 = 0.9709

**Step 2: Calculate weighted average entropy**

Weighted_Entropy = (5/14) × 0.9709 + (4/14) × 0 + (5/14) × 0.9709
= 0.3571 × 0.9709 + 0.2857 × 0 + 0.3571 × 0.9709
= 0.3467 + 0 + 0.3467 = 0.6934

**Step 3: Calculate Information Gain**

Gain(S, Weather) = Entropy(S) - Weighted_Entropy
= 0.940 - 0.6934 = 0.2466

The information gain of 0.2466 tells us how much uncertainty is reduced by splitting on the Weather attribute.

### Example 3: Building a Decision Tree

Given a training set for "Play Tennis" decision:

| Day | Outlook  | Humidity | Wind    | Play |
|-----|----------|----------|---------|------|
| D1  | Sunny    | High     | Strong  | No   |
| D2  | Sunny    | High     | Weak    | No   |
| D3  | Overcast | High     | Strong  | Yes  |
| D4  | Rainy    | High     | Strong  | Yes  |
| D5  | Rainy    | Low      | Strong  | No   |
| D6  | Rainy    | Low      | Weak    | Yes  |
| D7  | Overcast | Low      | Weak    | Yes  |
| D8  | Sunny    | High     | Strong  | No   |
| D9  | Sunny    | Low      | Weak    | Yes  |
| D10 | Rainy    | Low      | Strong  | Yes  |
| D11 | Sunny    | Low      | Strong  | Yes  |
| D12 | Overcast | High     | Strong  | Yes  |
| D13 | Overcast | Low      | Weak    | Yes  |
| D14 | Rainy    | High     | Weak    | No   |

**Step 1: Calculate initial entropy**
- Yes: 9 examples
- No: 5 examples
- Entropy(S) = -(9/14) × log₂(9/14) - (5/14) × log₂(5/14) = 0.940

**Step 2: Calculate information gain for each attribute**

For Outlook (Sunny: 5, Overcast: 4, Rainy: 5):
- Sunny: 2 Yes, 3 No → Entropy = 0.971
- Overcast: 4 Yes, 0 No → Entropy = 0
- Rainy: 3 Yes, 2 No → Entropy = 0.971

Gain = 0.940 - [(5/14) × 0.971 + (4/14) × 0 + (5/14) × 0.971] = 0.247

For Humidity (High: 7, Low: 7):
- High: 3 Yes, 4 No → Entropy = 0.985
- Low: 6 Yes, 1 No → Entropy = 0.592

Gain = 0.940 - [(7/14) × 0.985 + (7/14) × 0.592] = 0.151

For Wind (Strong: 8, Weak: 6):
- Strong: 6 Yes, 2 No → Entropy = 0.811
- Weak: 3 Yes, 3 No → Entropy = 1.0

Gain = 0.940 - [(8/14) × 0.811 + (6/14) × 1.0] = 0.048

**Step 3: Select root node**
Outlook has the highest information gain (0.247), so it becomes the root node.

**Step 4: Recursively build subtrees**
Continue this process for each branch until all leaves are pure or no attributes remain.

## Exam Tips

1. **Memorize Key Formulas**: Ensure you can calculate entropy, information gain, and Gini index from given data. These are frequently tested in DU examinations.

2. **Understand Attribute Selection**: The algorithm always selects the attribute with HIGHEST information gain. Practice calculating these values for different attributes to identify the best split.

3. **Interpret Entropy Values**: Remember that Entropy = 0 means pure (all same class), while Entropy = 1 means maximally impure for binary classification.

4. **Handle Binary vs Multi-class**: For binary classification, entropy ranges from 0 to 1. For multi-class with k classes, entropy can go up to log₂(k).

5. **Know the Difference Between ID3 and C4.5**: ID3 uses information gain and cannot handle continuous attributes, while C4.5 uses gain ratio and handles continuous attributes.

6. **Pruning is Essential**: Understand the difference between pre-pruning and post-pruning. Pre-pruning stops early, post-pruning prunes after full tree construction.

7. **Step-by-Step Problem Solving**: In exams, show all calculation steps. Even if final answer is wrong, partial marks are awarded for correct methodology.

8. **Time Management**: Practice these calculations multiple times to improve speed. Typical exam questions require calculating information gain for 2-3 attributes.

9. **Real-world Interpretation**: Be prepared to explain what the constructed decision tree means in practical terms - each path represents a classification rule.

10. **Common Pitfall**: Remember to use log base 2 for entropy calculations, not natural logarithm or base 10.