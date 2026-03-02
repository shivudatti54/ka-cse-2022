# Hyperparameters and Model Validation Chapter 37 Summary

=============================================

### Key Concepts

- **Hyperparameters**: Parameters set before training a model, as opposed to model parameters which are learned during training.
- **Model Validation**: The process of evaluating a model's performance on unseen data to estimate its generalization ability.
- **Cross-Validation**: A technique for model validation that involves splitting data into training and validation sets.
- **Grid Search**: A technique for hyperparameter tuning that involves searching over a grid of possible hyperparameters.
- **Random Search**: A technique for hyperparameter tuning that involves randomly sampling over possible hyperparameters.

### Important Formulas and Definitions

- **Mean Squared Error (MSE)**: A measure of the average squared difference between predicted and actual values.
  - $MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
- **Mean Absolute Error (MAE)**: A measure of the average absolute difference between predicted and actual values.
  - $MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$
- **R-Squared (R²)**: A measure of the proportion of variance in the dependent variable that is predictable from the independent variable(s).
  - $R² = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$

### Theorems and Important Results

- **Central Limit Theorem (CLT)**: States that the distribution of sample means will be approximately normal with large sample sizes.
- **Law of Large Numbers (LLN)**: States that the average of sample values will converge to the population mean as the sample size increases.

### Key Techniques

- **Grid Search**: A brute-force approach for hyperparameter tuning.
- **Random Search**: A probabilistic approach for hyperparameter tuning.
- **Cross-Validation**: A technique for model validation that involves splitting data into training and validation sets.
- **K-Fold Cross-Validation**: A variation of cross-validation that involves splitting data into k folds and evaluating model performance on each fold.
- **Bootstrap Cross-Validation**: A variation of cross-validation that involves resampling data with replacement.
