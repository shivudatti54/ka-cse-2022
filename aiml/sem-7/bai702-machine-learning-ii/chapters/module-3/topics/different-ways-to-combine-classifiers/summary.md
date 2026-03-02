# **Different Ways To Combine Classifiers**

## **Introduction**

In ensemble learning, multiple classifiers are combined to improve the overall performance of a machine learning model.

## **Methods**

- **Bagging (Bootstrap Aggregating)**
  - Create multiple training datasets by bootstrapping the original dataset
  - Train a separate classifier on each dataset
  - Average the predictions of the individual classifiers
- **Boosting**
  - Train multiple classifiers sequentially, with each subsequent classifier attempting to correct the errors of the previous classifier
  - Use a weighted voting system to combine the predictions
- **Adaboost**
  - Combines bagging and boosting
  - Uses weighted voting system with weights updated at each iteration
- **Subagging**
  - Randomly subsample the training dataset for each classifier
  - Combine the predictions using weighted voting
- **Random Forest**
  - Combines multiple decision trees
  - Uses bagging or subagging to create multiple trees
  - Combines the predictions of the individual trees using weighted voting

## **Formulas**

- Weighted voting system:
  - W = (1 - λ) + λ \* y
  - λ = 1 / (1 + e^(-y))
  - y = predicted output
- Adaboost formula:
  - w_t+1 = w_t \* e^(-h_t)
  - h_t = -log(W \* y_t / (1 - W))

## **Important Theorems**

- **Vapnik-Chervonenkis (VC) Dimension**: A measure of the capacity of a classifier
- **No Free Lunch Theorem**: A fundamental principle of machine learning, stating that no algorithm can be universally optimal

## **Key Concepts**

- **Ensemble learning**: Combining multiple classifiers to improve performance
- **Overfitting**: When a model is too complex and performs well on the training data but poorly on new data
- **Underfitting**: When a model is too simple and fails to capture the underlying patterns in the data
