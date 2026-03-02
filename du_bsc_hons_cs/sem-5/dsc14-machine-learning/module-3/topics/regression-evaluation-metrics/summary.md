# Regression Evaluation Metrics - Summary

## Key Definitions and Concepts

- **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual values. Robust to outliers. Formula: $\frac{1}{n} \sum |y_i - \hat{y}_i|$

- **Mean Squared Error (MSE)**: Average squared difference between predicted and actual values. Penalizes large errors heavily. Formula: $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$

- **Root Mean Squared Error (RMSE)**: Square root of MSE, in original units. More interpretable than MSE. Formula: $\sqrt{MSE}$

- **R-squared (R²)**: Proportion of variance explained by the model. Ranges from 0 to 1 (can be negative if model is worse than baseline). Formula: $1 - \frac{SS_{res}}{SS_{tot}}$

- **Adjusted R-squared**: R² adjusted for number of predictors. Decreases if irrelevant predictors are added. Formula: $1 - \frac{(1-R^2)(n-1)}{n-p-1}$

- **MAPE**: Errors expressed as percentage of actual values. Scale-independent but problematic with zero values. Formula: $\frac{100}{n} \sum |\frac{y_i - \hat{y}_i}{y_i}|$

## Important Formulas and Theorems

| Metric | Formula | Units |
|--------|---------|-------|
| MAE | $\frac{1}{n} \sum |y_i - \hat{y}_i|$ | Same as target |
| MSE | $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$ | Squared units |
| RMSE | $\sqrt{MSE}$ | Same as target |
| R² | $1 - \frac{SS_{res}}{SS_{tot}}$ | Dimensionless |
| Adjusted R² | $1 - \frac{(1-R^2)(n-1)}{n-p-1}$ | Dimensionless |

## Key Points

- RMSE ≥ MAE always; the gap indicates presence of large errors
- R² measures relative improvement over predicting the mean
- Use Adjusted R² when comparing models with different numbers of predictors
- MAE is preferred when outliers should not heavily influence the model
- RMSE is preferred when large errors are particularly costly
- MAPE is useful for business reporting but fails with zero actual values
- Always consider the context and units when interpreting metrics

## Common Mistakes to Avoid

1. **Confusing MSE with RMSE**: Remember to take the square root to get interpretable units
2. **Ignoring Adjusted R²**: Using regular R² for model comparison with different predictor counts
3. **Using MAPE blindly**: Not checking for zero or near-zero values in the dataset
4. **Interpreting R² as accuracy**: R² is not accuracy—it's variance explained (0-1 scale)
5. **Forgetting that R² can be negative**: This happens when the model performs worse than predicting the mean

## Revision Tips

1. Practice calculating all metrics from scratch using small datasets to understand the mechanics
2. Create a comparison table summarizing when each metric is appropriate
3. Remember: larger errors → higher MSE/RMSE; smaller errors → lower MAE/RMSE
4. For R²: higher is better (up to 1); for errors: lower is better
5. In exams, always check units and interpret what the number means in context