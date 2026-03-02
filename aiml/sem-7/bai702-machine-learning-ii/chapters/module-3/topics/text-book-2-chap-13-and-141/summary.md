# **Revision Notes: Text Book 2, Chap 13 and 14.1**

### Introduction

---

- **Decision by Committee**: A machine learning approach where multiple models make predictions collectively.
- **Ensemble Learning**: Combining multiple models to improve performance.

### Adaboost

---

- **Definition**: Boosting algorithm that combines multiple weak models to create a strong predictive model.
- **Key steps**:
  - **Training**: Train a weak model on the entire dataset.
  - **Weighting**: Assign weights to misclassified instances based on the model's performance.
  - **Prediction**: Use the weighted model to make predictions on the entire dataset.
  - **Update**: Update the model by adding a new weak model that corrects the errors of the previous model.
- **Importance Score**: Assign a score to each instance based on its contribution to the model's accuracy.
- **Adaboost Equation**:
  - $y' = \Sigma w_i K(x_i, y_i)$, where $K(x_i, y_i)$ is the loss function and $w_i$ is the weight.

### Stumping

---

- **Definition**: A weak model consisting of a single decision tree.
- **Key characteristics**:
  - **Splitting**: The model splits the dataset into subsets based on a feature.
  - **Leaf Node**: The model assigns a class label to each subset.
- **Stumping Equation**:
  - $y = \text{Majority Vote of Leaf Nodes}$

### Bagging

---

- **Definition**: A technique that combines multiple models trained on different subsets of the dataset.
- **Key steps**:
  - **Bootstrapping**: Create multiple subsets of the dataset with replacement.
  - **Model Training**: Train a model on each subset.
  - **Vote**: Use the models to make predictions on the entire dataset.
- **Subagging**: A variation of bagging that uses a weighted voting scheme.

### Subagging

---

- **Definition**: A variation of bagging that uses a weighted voting scheme.
- **Key characteristics**:
  - **Weighting**: Assign weights to each model based on its performance.
  - **Voting**: Use the weighted models to make predictions.
- **Subagging Equation**:
  - $y = \text{Weighted Majority Vote}$

### Theorems

---

- **Vapnik-Chervonenkis (VC) Theorem**: A theoretical framework for understanding the capacity of ensemble methods.
- **Weak Law of Large Numbers (WLLN)**: A theorem that shows the ensemble method converges to the true model as the number of models increases.
