# Decision Trees
## Introduction

Decision Trees are a fundamental concept in Machine Learning, used for both classification and regression tasks. They are a type of supervised learning algorithm that can be used to predict the value of a target variable based on several input features. Decision Trees are popular due to their simplicity, interpretability, and ability to handle categorical and numerical data.

In a Decision Tree, the data is recursively partitioned into smaller subsets based on the values of the input features. The partitioning process continues until a stopping criterion is met, such as when all instances in a node belong to the same class. The resulting tree structure consists of internal nodes that represent features or attributes, and leaf nodes that represent class labels or predicted values.

Decision Trees have many applications in real-world problems, such as credit risk assessment, medical diagnosis, and customer segmentation. They are also used as a building block for more complex algorithms, such as Random Forests and Gradient Boosting.

## Key Concepts

### 1. Decision Tree Structure

A Decision Tree consists of the following components:

* **Root Node**: The topmost node in the tree, which represents the entire dataset.
* **Internal Nodes**: These nodes represent features or attributes and are used to split the data into smaller subsets.
* **Leaf Nodes**: These nodes represent class labels or predicted values and are the terminal nodes in the tree.
* **Edges**: These represent the relationships between nodes and are used to traverse the tree.

### 2. Decision Tree Construction

The construction of a Decision Tree involves the following steps:

1. **Choose a Feature**: Select a feature to split the data based on a splitting criterion, such as Gini Impurity or Entropy.
2. **Split the Data**: Partition the data into smaller subsets based on the chosen feature.
3. **Recursion**: Recursively apply the splitting process to each subset until a stopping criterion is met.
4. **Pruning**: Remove branches that do not contribute to the accuracy of the tree.

### 3. Splitting Criteria

Common splitting criteria used in Decision Trees include:

* **Gini Impurity**: Measures the probability of misclassifying a new instance.
* **Entropy**: Measures the amount of uncertainty in the data.
* **Variance**: Measures the spread of the data.

### 4. Pruning Techniques

Pruning techniques are used to reduce the complexity of the Decision Tree and prevent overfitting. Common pruning techniques include:

* **Pre-Pruning**: Prune branches during the construction of the tree.
* **Post-Pruning**: Prune branches after the construction of the tree.

## Examples

### Example 1: Classification

Suppose we want to build a Decision Tree to classify customers as either "Creditworthy" or "Not Creditworthy" based on their age and income.

| Age | Income | Creditworthy |
| --- | --- | --- |
| 25  | 50000 | Yes          |
| 30  | 60000 | Yes          |
| 35  | 70000 | No           |
| 40  | 80000 | Yes          |

Using the Gini Impurity criterion, we can construct the following Decision Tree:

* Root Node: Age
* Internal Node: Income
* Leaf Node: Creditworthy

### Example 2: Regression

Suppose we want to build a Decision Tree to predict the price of a house based on its features.

| Feature | Price |
| --- | --- |
| 2 bedrooms | 200000 |
| 3 bedrooms | 300000 |
| 4 bedrooms | 400000 |

Using the Variance criterion, we can construct the following Decision Tree:

* Root Node: Number of Bedrooms
* Internal Node: Square Footage
* Leaf Node: Price

## Exam Tips

1. Understand the different types of Decision Trees, including classification and regression trees.
2. Know how to construct a Decision Tree using a splitting criterion.
3. Be able to identify the components of a Decision Tree, including root nodes, internal nodes, and leaf nodes.
4. Understand the importance of pruning in Decision Trees.
5. Be able to apply Decision Trees to real-world problems.
6. Know how to evaluate the performance of a Decision Tree using metrics such as accuracy and mean squared error.
7. Understand the limitations of Decision Trees, including overfitting and underfitting.