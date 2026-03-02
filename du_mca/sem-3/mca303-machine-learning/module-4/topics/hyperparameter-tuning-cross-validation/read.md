# Hyperparameter Tuning & Cross-Validation

## Introduction
Hyperparameter tuning is the process of optimizing the configuration settings that govern machine learning models' learning processes. Unlike model parameters learned during training, hyperparameters (like learning rate, k in k-NN, or tree depth) are set before training. Effective tuning can mean the difference between state-of-the-art performance and failed models.

Cross-validation is a statistical technique to assess model generalizability. It addresses overfitting by rotating data subsets for validation, particularly crucial when tuning hyperparameters to prevent information leakage. Together, these techniques form the backbone of robust ML pipelines in industry applications like recommendation systems and fraud detection.

In real-world ML projects (e.g., AWS SageMaker pipelines or Kaggle competitions), hyperparameter optimization accounts for 30-50% of development effort. The Delhi Metro's predictive maintenance system uses Bayesian hyperparameter optimization with time-series cross-validation to predict equipment failures with 92% accuracy.

## Key Concepts
1. **Hyperparameters vs Parameters**: 
   - Parameters: Learned from data (e.g., neural network weights)
   - Hyperparameters: Set pre-training (e.g., SVM's C, random forest's n_estimators)

2. **Cross-Validation Types**:
   - k-Fold: Divide data into k equal partitions
   - Stratified k-Fold: Preserves class distribution
   - Time Series Split: Maintains temporal order
   - Leave-One-Out: k=n samples

3. **Tuning Methods**:
   - Grid Search: Exhaustive combinatorial search
   - Random Search: Randomized parameter sampling
   - Bayesian Optimization: Gaussian processes for efficient search
   - Evolutionary Algorithms: Genetic programming approaches

4. **Nested Cross-Validation**:
   Outer loop estimates generalization error, inner loop performs tuning. Prevents optimistic bias in performance estimates.

5. **Performance Metrics**:
   - Classification: F1-score, AUC-ROC
   - Regression: MAE, RMSE
   - Custom metrics: Business-specific loss functions

## Examples

**Example 1: Grid Search for SVM on Iris Dataset**
```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {'C': [0.1, 1, 10], 
              'kernel': ['linear', 'rbf']}
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Test accuracy: {grid_search.score(X_test, y_test):.2f}")
```
*Solution*: The grid evaluates 3×2=6 combinations. 5-fold CV means 6×5=30 model fits. Best parameters are selected based on average validation performance.

**Example 2: Bayesian Optimization for Neural Network**
Using Optuna library:
```python
import optuna

def objective(trial):
    n_layers = trial.suggest_int('n_layers', 1, 3)
    lr = trial.suggest_loguniform('lr', 1e-5, 1e-2)
    
    model = build_nn(n_layers, lr)
    return cross_val_score(model, X, cv=5).mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

**Example 3: Nested CV for Model Selection**
```python
outer_cv = StratifiedKFold(n_splits=5)
inner_cv = KFold(n_splits=3)

for train_idx, test_idx in outer_cv.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    
    # Inner loop for tuning
    grid_search = GridSearchCV(estimator, param_grid, cv=inner_cv)
    grid_search.fit(X_train, y_train)
    
    # Evaluate on held-out fold
    score = grid_search.best_estimator_.score(X_test, y_test)
```

## Exam Tips
1. Always distinguish between model parameters (learned) vs hyperparameters (set)
2. Cross-validation's primary purpose: estimate generalization error without separate test set
3. Grid Search vs Random Search: Grid is exhaustive but expensive for high dimensions
4. Stratified k-fold is mandatory for imbalanced datasets
5. Never tune hyperparameters on test data - use validation sets
6. Nested CV gives unbiased performance estimates but is computationally heavy
7. Bayesian optimization typically requires fewer iterations than random search