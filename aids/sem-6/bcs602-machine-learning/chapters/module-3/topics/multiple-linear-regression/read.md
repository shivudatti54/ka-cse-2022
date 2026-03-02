# Multiple Linear Regression

## Introduction

Multiple Linear Regression (MLR) is a fundamental statistical technique in machine learning and predictive analytics that extends the concept of simple linear regression to accommodate multiple independent variables. While simple linear regression examines the relationship between one predictor variable and one response variable, multiple linear regression analyzes how several predictor variables jointly influence a continuous outcome variable. This extension makes MLR significantly more powerful and applicable to real-world scenarios where phenomena are rarely influenced by a single factor alone.

In the context of data science and machine learning, multiple linear regression serves as a cornerstone algorithm for predictive modeling. It enables analysts and researchers to understand how multiple factors simultaneously affect an outcome, which is essential for decision-making in business, economics, social sciences, and engineering. For instance, predicting house prices requires considering not just square footage but also location, number of bedrooms, age of the property, and neighborhood characteristics. Similarly, predicting student performance might involve analyzing study hours, attendance, previous grades, and socioeconomic factors collectively.

The mathematical foundation of multiple linear regression builds upon the principles of simple linear regression while introducing additional complexity in matrix operations and interpretation. Understanding MLR is crucial for students pursuing computer science as it forms the basis for more advanced regression techniques including polynomial regression, ridge regression, and lasso regression. The ability to implement and interpret multiple linear regression models is a fundamental skill that data scientists and machine learning practitioners must possess.

## Key Concepts

### The Multiple Linear Regression Model

The multiple linear regression model with k predictor variables can be expressed mathematically as:

Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

Where:
- Y is the dependent variable (response/dependent variable)
- X₁, X₂, ..., Xₖ are the independent variables (predictors/features)
- β₀ is the intercept (constant term)
- β₁, β₂, ..., βₖ are the regression coefficients
- ε is the error term (residual), assumed to be normally distributed with mean zero and constant variance

The coefficient βⱼ represents the change in Y for a one-unit change in Xⱼ, while holding all other predictor variables constant. This is known as the CETERIS PARIBUS assumption and is fundamental to interpreting multiple regression results.

### Assumptions of Multiple Linear Regression

Multiple linear regression relies on several key assumptions that must be satisfied for valid inference:

LINEARITY: The relationship between each predictor and the dependent variable must be linear. This assumption can be checked through scatter plots of residuals versus predicted values.

INDEPENDENCE: The observations must be independent of each other. This is particularly important for time series data where autocorrelation may violate this assumption.

HOMOSCEDASTICITY: The variance of residuals should be constant across all levels of the predictor variables. When this assumption is violated, we encounter heteroscedasticity, which affects the efficiency of coefficient estimates.

NORMALITY: The residuals should be approximately normally distributed. This assumption is crucial for hypothesis testing and constructing confidence intervals.

NO MULTICOLLINEARITY: The predictor variables should not be highly correlated with each other. High multicollinearity makes it difficult to isolate the individual effect of each predictor and inflates the variance of coefficient estimates.

### Estimating Regression Coefficients

The most common method for estimating regression coefficients is Ordinary Least Squares (OLS). The OLS method minimizes the sum of squared residuals:

SSE = Σ(yᵢ - ŷᵢ)²

Where ŷᵢ is the predicted value. The solution to this minimization problem can be expressed using matrix notation:

β = (X'X)⁻¹X'Y

Where X is the matrix of predictor variables (including a column of ones for the intercept), Y is the vector of observed values, and (X'X)⁻¹ is the inverse of the matrix X'X.

### Coefficient of Determination (R²)

The coefficient of determination, denoted R², measures the proportion of variance in the dependent variable that is explained by the independent variables:

R² = 1 - (SS_res / SS_tot)

Where SS_res is the sum of squared residuals and SS_tot is the total sum of squares. R² ranges from 0 to 1, with higher values indicating better model fit. However, adding more predictors always increases R², even if they are not truly related to the dependent variable. This limitation is addressed by the adjusted R²:

R²_adj = 1 - [(1 - R²)(n - 1) / (n - k - 1)]

Where n is the sample size and k is the number of predictors.

### Multicollinearity and Variance Inflation Factor

Multicollinearity occurs when predictor variables are highly correlated, making it problematic to determine the individual contribution of each variable. The Variance Inflation Factor (VIF) quantifies the severity of multicollinearity:

VIFᵢ = 1 / (1 - R²ᵢ)

Where R²ᵢ is the R-squared value when predictor Xᵢ is regressed on all other predictors. A VIF value greater than 10 is typically considered indicative of problematic multicollinearity, though some practitioners use a threshold of 5.

### Hypothesis Testing in Multiple Regression

Statistical significance of regression coefficients is tested using the t-test:

t = βᵢ / SE(βᵢ)

Where SE(βᵢ) is the standard error of the coefficient estimate. The null hypothesis H₀: βᵢ = 0 is tested against the alternative H₁: βᵢ ≠ 0. Additionally, the F-test evaluates whether the overall regression model is significant:

F = (MSR / MSE)

Where MSR is the mean square due to regression and MSE is the mean square error.

## Examples

### Example 1: Predicting House Prices

Consider a real estate analyst wants to predict house prices based on three variables: area (square feet), number of bedrooms, and age of house (years). The data for 10 houses is given below:

| Area (X₁) | Bedrooms (X₂) | Age (X₃) | Price (Y in Lakhs) |
|-----------|---------------|----------|---------------------|
| 1500      | 3             | 5        | 45                  |
| 1800      | 3             | 10       | 52                  |
| 1200      | 2             | 2        | 38                  |
| 2100      | 4             | 8        | 65                  |
| 1600      | 3             | 15       | 48                  |
| 1900      | 4             | 3        | 58                  |
| 1400      | 2             | 20       | 42                  |
| 2200      | 4             | 12       | 70                  |
| 1700      | 3             | 7        | 55                  |
| 1300      | 2             | 1        | 35                  |

Step 1: Set up the design matrix X with columns for intercept (1s), X₁, X₂, and X₃.

Step 2: Compute β = (X'X)⁻¹X'Y using matrix operations.

Step 3: After calculation, suppose we obtain:
- β₀ = 12.5 (intercept)
- β₁ = 0.025 (area coefficient)
- β₂ = 3.2 (bedrooms coefficient)
- β₃ = -0.4 (age coefficient)

Step 4: The regression equation becomes:
Price = 12.5 + 0.025 × Area + 3.2 × Bedrooms - 0.4 × Age

Step 5: Interpretation:
- For each additional square foot, the price increases by 0.025 lakhs (₹25,000), holding bedrooms and age constant.
- Each additional bedroom adds 3.2 lakhs to the price, holding area and age constant.
- Each additional year of age decreases the price by 0.4 lakhs, holding area and bedrooms constant.

### Example 2: Employee Performance Prediction

An HR department wants to predict employee performance scores based on years of experience, training hours, and education level. Using OLS estimation on data from 50 employees, the following model is obtained:

Performance = 40 + 2.5 × Experience + 1.8 × Training + 5 × Education_Level

Where Education_Level is coded as 1 for graduate, 2 for postgraduate.

R² = 0.78, Adjusted R² = 0.76

The model explains 78% of the variance in performance scores. The F-test shows the model is statistically significant (p < 0.001). Individual t-tests reveal all coefficients are significant at the 5% level (p < 0.05), indicating each predictor significantly contributes to predicting performance.

### Example 3: Checking Multicollinearity

In a study predicting student GPA, three predictors are used: SAT scores, high school GPA, and class rank. The VIF values are calculated:

- VIF for SAT = 2.8
- VIF for High School GPA = 4.5
- VIF for Class Rank = 3.2

All VIF values are below 5, indicating no serious multicollinearity problem. The model can proceed with reliable coefficient estimates. If VIF for high school GPA had been 12.5, we would need to address multicollinearity by either removing one correlated variable, combining variables, or using regularization techniques like ridge regression.

## Exam Tips

1. UNDERSTAND THE MATHEMATICAL FORMULATION: Be able to write the multiple linear regression equation with k predictors and explain each component. Know the matrix representation of the OLS solution.

2. MEMORIZE ALL ASSUMPTIONS: The five classical assumptions (linearity, independence, homoscedasticity, normality, no multicollinearity) are frequently tested in exams. Be prepared to explain how to check each assumption.

3. KNOW THE DIFFERENCE BETWEEN R² AND ADJUSTED R²: Remember that R² always increases with added predictors, while adjusted R² can decrease if the new predictor does not contribute meaningfully. This is a common exam question.

4. INTERPRET COEFFICIENTS CORRECTLY: When interpreting βᵢ, always mention "holding all other variables constant" or "ceteris paribus." This nuance is crucial for full marks.

5. UNDERSTAND HYPOTHESIS TESTING: Know how to conduct t-tests for individual coefficients and F-test for overall model significance. Be able to state null and alternative hypotheses.

6. VIF CALCULATION AND INTERPRETATION: Know the formula for VIF and understand what VIF values indicate about multicollinearity. Remember threshold values (5 or 10).

7. PRACTICE NUMERICAL PROBLEMS: DU exams often include numerical problems requiring calculation of regression coefficients, R², or interpretation of output. Work through multiple examples.

8. KNOW WHEN TO USE MULTIPLE VS. SIMPLE REGRESSION: Understand that multiple regression is appropriate when multiple factors jointly influence the outcome and we want to isolate individual effects.

9. BE AWARE OF LIMITATIONS: Understand the limitations of MLR including sensitivity to outliers, inability to capture non-linear relationships without transformation, and the ceteris paribus interpretation challenges.

10. CONNECT TO OTHER TOPICS: Understand how MLR relates to other topics in the module such as polynomial regression (which adds transformed predictors) and logistic regression (which handles categorical dependent variables).