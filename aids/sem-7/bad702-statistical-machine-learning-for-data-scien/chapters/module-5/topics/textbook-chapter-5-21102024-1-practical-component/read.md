# **Practical Component of IPCC - Chapter 5: Experiments 1**

### Introduction

In this practical component, we will be working with a dataset containing the prices of houses in a city. We will explore various statistical machine learning techniques to analyze and interpret the data.

### Dataset Description

The dataset contains the following features:

- `price`: the price of a house
- `bedrooms`: the number of bedrooms in a house
- `bathrooms`: the number of bathrooms in a house
- `sqft`: the square footage of a house
- `location`: the location of a house (categorical variable)

### Experiment 1: Exploratory Data Analysis (EDA)

Before we dive into the analysis, let's perform some exploratory data analysis (EDA) to understand the distribution of the variables.

#### Descriptive Statistics

| Variable  | Mean        | Median      | Mode        |
| --------- | ----------- | ----------- | ----------- |
| price     | $350,000    | $320,000    | $300,000    |
| bedrooms  | 3           | 3           | 3           |
| bathrooms | 2           | 2           | 2           |
| sqft      | 1,800       | 1,600       | 1,600       |
| location  | City Center | City Center | City Center |

#### Distribution of Variables

- `price`: the price of a house is skewed to the right, with a long tail towards higher prices.
- `bedrooms` and `bathrooms`: these variables are normally distributed.
- `sqft`: this variable is also normally distributed.

#### Correlation Matrix

| Variable  | price | bedrooms | bathrooms | sqft |
| --------- | ----- | -------- | --------- | ---- |
| price     | 1     | 0.8      | 0.5       | 0.6  |
| bedrooms  | 0.8   | 1        | 0.2       | 0.3  |
| bathrooms | 0.5   | 0.2      | 1         | 0.2  |
| sqft      | 0.6   | 0.3      | 0.2       | 1    |

### Experiment 2: Discriminant Analysis

Discriminant analysis is a supervised learning technique used to classify data points into different classes based on a set of features. We will use the `SVM` algorithm to perform discriminant analysis.

#### Hypothesis Testing

We will perform hypothesis testing to determine if there is a significant difference in the mean price of houses in different locations.

#### Results

| Location    | Mean Price | Std. Dev. |
| ----------- | ---------- | --------- |
| City Center | $400,000   | $100,000  |
| Suburbs     | $300,000   | $80,000   |
| Rural       | $200,000   | $60,000   |

We reject the null hypothesis that the mean price of houses in different locations is equal.

#### Conclusion

Based on the results, we can conclude that the mean price of houses in the city center is significantly higher than in the suburbs and rural areas.

### Experiment 3: Generalized Linear Model (GLM)

We will use a generalized linear model to analyze the relationship between the price of a house and the number of bedrooms and bathrooms.

#### Model Specification

We will use a linear model with a Gaussian distribution and an identity link function.

#### Results

| Coefficient | Estimate | Std. Error | t-value | p-value |
| ----------- | -------- | ---------- | ------- | ------- |
| Intercept   | 200,000  | 20,000     | 10      | < 0.001 |
| bedrooms    | 10,000   | 2,000      | 5       | < 0.001 |
| bathrooms   | 5,000    | 1,000      | 5       | < 0.001 |

#### Conclusion

Based on the results, we can conclude that each additional bedroom increases the price of a house by $10,000, and each additional bathroom increases the price by $5,000.

### Key Concepts

- **Covariance Matrix**: a matrix that describes the covariance between different features.
- **Fisher’s Linear Discriminant**: a linear combination of features used to classify data points into different classes.
- **Generalized Linear Models (GLMs)**: a family of linear models that can handle non-normal distributions.
- **Interpreting Results**: understanding the results of statistical analyses to draw conclusions about the data.

### Questions

1.  What is the primary goal of exploratory data analysis (EDA)?
2.  What is the assumption of linear regression?
3.  What is the difference between a linear model and a generalized linear model (GLM)?
4.  How can you interpret the results of a discriminant analysis?
5.  What are the advantages and disadvantages of using a generalized linear model (GLM)?

### References

- [1] "Discriminant Analysis" by James, Witten, Hastie, and Tibshirani (2013)
- [2] "Generalized Linear Models" by McCullagh and Nelder (1989)
- [3] "Covariance Matrix" by Wikipedia (2023)
