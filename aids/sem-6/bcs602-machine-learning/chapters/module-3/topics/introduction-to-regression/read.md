# Introduction to Regression

## Introduction

Regression analysis stands as one of the most fundamental and widely used statistical techniques in the field of machine learning and data science. It serves as the cornerstone for predictive modeling, allowing us to understand and quantify the relationship between variables. In the context of computer science and machine learning, regression enables computers to learn patterns from historical data and make predictions about continuous numerical outcomes.

The origin of regression dates back to the late 19th century when Sir Francis Galton introduced the concept while studying the relationship between the heights of parents and their children. Since then, regression has evolved into a sophisticated tool that forms the backbone of numerous applications we encounter daily. From predicting house prices based on square footage and location to forecasting stock market trends, from estimating crop yields based on weather conditions to predicting patient recovery times, regression techniques are everywhere.

Understanding regression is essential for any computer science student because it bridges the gap between pure algorithmic thinking and statistical reasoning. It provides a mathematical framework for making data-driven decisions without explicit programming. In the era of big data and machine learning, the ability to build and interpret regression models has become a critical skill. This chapter introduces the fundamental concepts of regression, preparing you for more advanced topics like linear regression, polynomial regression, and logistic regression that follow in subsequent chapters.

## Key Concepts

### Understanding Regression

Regression is a supervised learning technique used to predict continuous numerical values. Unlike classification, which assigns data points to discrete categories, regression predicts actual numerical outcomes. The fundamental idea is to establish a mathematical relationship between a dependent variable (also called the target or response variable) and one or more independent variables (also called predictors or features).

For example, if you want to predict the price of a house, the price is the dependent variable, while factors like area, number of rooms, location, and age are independent variables. The regression model learns the relationship between these variables from historical data and then applies this learned relationship to make predictions on new data.

### Types of Regression

Regression can be categorized in several ways based on the number of predictors and the nature of the relationship between variables.

Simple linear regression involves only one independent variable and assumes a linear relationship between the predictor and the target. The relationship is expressed as a straight line: Y = β₀ + β₁X + ε, where Y is the dependent variable, X is the independent variable, β₀ is the y-intercept, β₁ is the slope coefficient, and ε represents the error term.

Multiple linear regression extends this concept to include multiple independent variables. The equation becomes: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε, where X₁, X₂, ..., Xₙ represent different predictor variables. This allows for more complex and realistic models that consider multiple factors simultaneously.

Polynomial regression handles non-linear relationships by including polynomial terms of the independent variable. For instance, Y = β₀ + β₁X + β₂X² + β₃X³ allows the model to capture curved relationships between variables.

### The Line of Best Fit

The core of simple linear regression is finding the line that best represents the relationship between two variables. This line is called the line of best fit or the regression line. The "best fit" is determined by minimizing the sum of squared residuals, where a residual is the difference between the actual observed value and the predicted value.

The method used to find this optimal line is called Ordinary Least Squares (OLS). It calculates the coefficients that minimize the sum of squared differences between the observed and predicted values. Mathematically, if we have n data points (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ), we want to find β₀ and β₁ such that the sum of (yᵢ - (β₀ + β₁xᵢ))² is minimized for all i from 1 to n.

### Coefficient of Determination (R²)

R², also known as the coefficient of determination, measures the proportion of variance in the dependent variable that is explained by the independent variable(s). It ranges from 0 to 1, where 0 indicates that the model explains none of the variability, and 1 indicates perfect explanation. An R² of 0.75 means that 75% of the variation in the dependent variable can be explained by the regression model.

However, R² should be interpreted carefully. A high R² does not necessarily mean the model is good, as it can be artificially inflated by overfitting. Adjusted R² penalizes the model for adding unnecessary predictors, providing a more realistic measure in multiple regression scenarios.

### Assumptions of Linear Regression

Linear regression relies on several key assumptions that must be satisfied for valid results:

Linearity assumes that the relationship between independent and dependent variables is linear. Homoscedasticity assumes that the variance of residuals is constant across all levels of independent variables. Independence assumes that observations are independent of each other. Normality assumes that residuals follow a normal distribution, particularly important for small sample sizes.

Violation of these assumptions can lead to unreliable predictions and incorrect conclusions. Diagnostic plots and statistical tests help verify whether these assumptions are met in practice.

### Training and Testing

In machine learning applications, the dataset is typically split into training and testing sets. The training set is used to build the regression model by finding the optimal coefficients. The testing set, which the model has not seen during training, is used to evaluate how well the model generalizes to new data.

This separation prevents overfitting, where the model performs excellently on training data but poorly on unseen data. The model's performance on the test set provides an estimate of how it will perform in real-world applications.

## Examples

### Example 1: Simple Linear Regression

Suppose we have data about the number of hours studied (X) and exam scores (Y) for 5 students:

| Hours Studied (X) | Exam Score (Y) |
|-------------------|----------------|
| 2                 | 65             |
| 4                 | 75             |
| 6                 | 82             |
| 8                 | 90             |
| 10                | 95             |

Step 1: Calculate means
Mean of X = (2+4+6+8+10)/5 = 6
Mean of Y = (65+75+82+90+95)/5 = 81.4

Step 2: Calculate slope (β₁)
β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
Numerator = (2-6)(65-81.4) + (4-6)(75-81.4) + (6-6)(82-81.4) + (8-6)(90-81.4) + (10-6)(95-81.4)
= (-4)(-16.4) + (-2)(-6.4) + (0)(0.6) + (2)(8.6) + (4)(13.6)
= 65.6 + 12.8 + 0 + 17.2 + 54.4 = 150

Denominator = (2-6)² + (4-6)² + (6-6)² + (8-6)² + (10-6)² = 16 + 4 + 0 + 16 + 40 = 76

β₁ = 150/76 ≈ 1.97

Step 3: Calculate intercept (β₀)
β₀ = ȳ - β₁x̄ = 81.4 - 1.97(6) = 81.4 - 11.82 = 69.58

Step 4: Regression equation
Y = 69.58 + 1.97X

Interpretation: For each additional hour studied, the exam score increases by approximately 1.97 points. A student who studies for 7 hours would be predicted to score: Y = 69.58 + 1.97(7) = 69.58 + 13.79 = 83.37

### Example 2: Multiple Linear Regression

Consider predicting house prices using two features: area in square feet (X₁) and number of bedrooms (X₂). Suppose we have this training data:

| Area (X₁) | Bedrooms (X₂) | Price (Y in lakhs) |
|-----------|---------------|--------------------|
| 1000      | 2             | 25                 |
| 1500      | 3             | 40                 |
| 2000      | 3             | 55                 |
| 2500      | 4             | 70                 |
| 3000      | 4             | 85                 |

Using multiple linear regression, we might derive an equation like:
Price = 5 + 0.02(Area) + 5(Bedrooms)

For a house with 1800 square feet and 3 bedrooms:
Price = 5 + 0.02(1800) + 5(3) = 5 + 36 + 15 = 56 lakhs

This shows how multiple linear regression combines the effects of several variables to make predictions.

### Example 3: Residual Analysis

Given the regression model Y = 50 + 2X and the following actual data points:

| X | Actual Y | Predicted Y | Residual |
|---|----------|-------------|----------|
| 5 | 60       | 60          | 0        |
| 10| 75       | 70          | 5        |
| 15| 85       | 80          | 5        |
| 20| 95       | 90          | 5        |
| 25| 100      | 100         | 0        |

The sum of residuals is 15, but the sum of squared residuals is 75. The OLS method finds coefficients that minimize this sum of squared residuals. Small residuals indicate good model fit, while large residuals suggest the model is missing important patterns or relationships.

## Exam Tips

For DU semester examinations, keep the following points in mind when studying regression:

Understand the difference between regression and classification clearly. Regression predicts continuous values while classification predicts discrete categories. This distinction frequently appears in exam questions.

Memorize the simple linear regression equation Y = β₀ + β₁X + ε and understand what each term represents. Be able to identify dependent and independent variables in given scenarios.

The Ordinary Least Squares method minimizes the sum of squared residuals. Know how to interpret this concept and understand why squaring rather than taking absolute values is preferred.

R² measures the goodness of fit but has limitations. Remember that a high R² does not guarantee a good model, and correlation does not imply causation.

Know the four key assumptions of linear regression: linearity, homoscedasticity, independence, and normality. Be able to recognize when these assumptions are violated.

In multiple regression, understand that adding more predictors will always increase R², which is why Adjusted R² is preferred for model comparison.

Be prepared to calculate regression coefficients using the formula for β₁ and β₀. Practice with numerical problems as they commonly appear in exams.

Interpret regression coefficients correctly. A positive coefficient indicates a direct relationship, while a negative coefficient indicates an inverse relationship between variables.