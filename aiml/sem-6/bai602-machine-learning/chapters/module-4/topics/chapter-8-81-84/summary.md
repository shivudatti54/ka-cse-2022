# **Revision Notes: Chapter 8 (8.1-8.4) - Decision Tree Learning**

## **Introduction**

- Decision Tree Learning is a supervised learning algorithm used for classification and regression tasks.
- It's based on the concept of a tree-like model of decisions.

## **Decision Tree Induction**

- Decision Tree Induction is a methodology for building decision trees.
- The process involves:
  - Data Preprocessing
  - Root Node Selection
  - Splitting
  - Pruning

## **Key Concepts**

- **Node**: A node in the decision tree represents a feature or attribute.
- **Leaf Node**: A leaf node represents the predicted class label or target value.
- **Branching**: Branching represents the decision-making process in the decision tree.

## **Formulas and Theorems**

- **Information Gain**: A measure of the reduction in entropy (uncertainty) after splitting a node.
  - Formula: IG(D) = H(D) - ∑ (p(x) \* H(D|x))
- **Entropy**: A measure of uncertainty in a distribution.
  - Formula: H(D) = - ∑ (p(x) \* log2(p(x)))

## **Important Definitions**

- **Decision Tree Induction Algorithm**: An algorithm for building decision trees.
- **Tree Pruning**: The process of removing unnecessary nodes from the decision tree.

## **Key Terms**

- **Root Node**: The topmost node in the decision tree.
- **Splitting Criterion**: A criterion used to decide which attribute to split on.
- **Overfitting**: When the decision tree is too complex and fits the noise in the training data.
