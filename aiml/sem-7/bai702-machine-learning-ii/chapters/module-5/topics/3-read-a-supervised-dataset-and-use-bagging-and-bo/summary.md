# **Supervised Learning with Bagging and Boosting**

### Overview

- Read a supervised dataset for classification
- Use bagging and boosting techniques to improve model performance

### Key Concepts

- **Bagging (Bootstrap Aggregating)**:
  - Combine multiple models trained on different subsets of the dataset
  - Reduce overfitting and improve generalization
  - Formula: **Boosted Error** = **(1 - α) \* Boosted Error** + α \* (1 - **Boosted Accuracy**)
- **Boosting**:
  - Combine multiple weak models to create a strong predictive model
  - Weighted errors are used to update model parameters
  - Formula: **h(w) = f(w) + α \* w \* (y^{(i)} - f(w))**

### Definitions

- **Weak Model**: A simple model that makes accurate predictions on a small subset of the data
- **Strong Model**: A combined model that improves accuracy using multiple weak models

### Important Formulas

- **Boosting Error**: The error made by the boosting model on a new, unseen sample
- **Boosted Accuracy**: The accuracy achieved by the boosting model on the test dataset

### Theorems

- **Vapnik-Chervonenkis (VC) Dimension**: A measure of the model's capacity to fit a dataset
- **Shannon Entropy**: A measure of the uncertainty or randomness in a dataset

### Applications

- Improve the accuracy of a model by combining multiple weak models
- Reduce overfitting by combining multiple models trained on different subsets of the data

### Revision Notes

- Read a supervised dataset for classification
- Use bagging to combine multiple models trained on different subsets of the data
- Use boosting to combine multiple weak models and improve accuracy
- Evaluate the performance of the boosted model using metrics such as accuracy and mean squared error
