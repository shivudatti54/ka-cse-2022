# **Forests**

### Definition

- A type of ensemble learning algorithm that combines multiple decision trees to improve the accuracy of predictions.
- Also known as Random Forests.

### Key Points

- **Definition**: Forest = collection of multiple decision trees trained on different subsets of features and/or instances.
- **Advantages**:
  - Reduces overfitting and improves generalization.
  - Handles high-dimensional data and missing values.
  - Robust to outliers and noise.
- **Steps**:
  1.  Training: multiple decision trees are trained on different subsets of data.
  2.  Stumping: each decision tree is a stump, a single decision tree with only one internal node.
  3.  Bagging: each decision tree is trained on a random subset of the data.
  4.  Subagging: each decision tree is trained on a random subset of features.
  5.  Random Subagging: each decision tree is trained on a random subset of features and a random subset of the data.
- **Types**:
  - **Random Forest**: uses bagging and random subagging.
  - **Subagging Forest**: uses subagging only.
  - **Random Subagging Forest**: uses random subagging only.

### Formulas and Definitions

- **Decision Tree**: a tree-like model that splits data into subsets based on features.
- **Stump**: a decision tree with only one internal node.
- **Bagging**: a technique that combines multiple decision trees trained on different subsets of data.
- **Bootstrapping**: a resampling technique used in bagging.

### Theorems and Properties

- **Vapnik-Chervonenkis (VC) Theorem**: provides a bound on the capacity of a set of decision trees.
- **Monotonicity**: a property of decision trees that states that the output of a tree is monotonically increasing or decreasing.

### Important Terms

- **Overfitting**: when a model is too complex and fits the training data too well, resulting in poor generalization.
- **Underfitting**: when a model is too simple and fails to capture the underlying patterns in the data.
- **Noise**: random variations in the data that can affect model performance.
