# **Decision Tree Learning: Introduction**

### 8.1 Introduction to Decision Trees

A decision tree is a type of supervised learning algorithm used for classification and regression tasks. It is a tree-like model that splits the data into smaller subsets based on the features of the data.

### 8.2 Decision Tree Induction

Decision tree induction is the process of training a decision tree model on a dataset. The goal is to create a tree that can correctly classify new, unseen data.

#### Step 1: Root Node

The root node is the topmost node in the decision tree. It is the entry point for the algorithm and is chosen based on the feature with the highest variance in the training data.

#### Step 2: Splitting

The algorithm splits the data into two subsets based on the feature at the root node. The split is chosen such that the two subsets have approximately equal number of samples.

#### Step 3: Recursion

The algorithm repeats the process of splitting and recursion until a stopping criterion is met.

#### Example

Suppose we have a dataset of students with attributes `Age` and `GPA`, and we want to predict whether they will `Graduate` or not. We can create a decision tree that splits the data based on the `Age` attribute.

```
      +---------------+
      |  Age >= 25   |
      +---------------+
            |
            |
            v
      +---------------+
      |  GPA >= 3.0  |
      +---------------+
            |
            |
            v
      +---------------+
      |  Graduate    |
      +---------------+
```

### 8.3 Types of Decision Trees

There are several types of decision trees, including:

- **Classification Trees**: Used for binary classification tasks.
- **Regression Trees**: Used for regression tasks.
- **Random Forests**: An ensemble of decision trees used for both classification and regression tasks.
- **Gradient Boosting Trees**: An ensemble of decision trees used for regression tasks.

### 8.4 Advantages and Disadvantages of Decision Trees

#### Advantages

- **Interpretability**: Decision trees are easy to understand and interpret.
- **Simple to Implement**: Decision trees are relatively simple to implement.
- **Handling Missing Values**: Decision trees can handle missing values.

#### Disadvantages

- **Overfitting**: Decision trees can suffer from overfitting, especially when the trees are deep.
- **Not Suitable for High-Dimensional Data**: Decision trees can be slow and inefficient when dealing with high-dimensional data.
- **Not Suitable for Non-Linear Relationships**: Decision trees are not suitable for modeling non-linear relationships between variables.

### Key Concepts

- **Node**: A node in the decision tree represents a feature and a value.
- **Edge**: An edge represents the split between two nodes.
- **Split**: A split is the process of dividing the data into two subsets based on a feature.
- **Variance**: Variance measures the amount of variation in the data.
- **Splitting Criterion**: The splitting criterion is the rule used to choose the feature to split the data.
- **Stopping Criterion**: The stopping criterion is the rule used to determine when to stop splitting the data.
