# **Which Variables Seem to Have the Strongest Relationships**

## **Introduction**

In discriminant analysis, we often want to determine which variables have the strongest relationships with the target variable. This is crucial in identifying the most informative features that can be used to make predictions or classify data. In this section, we will explore the concepts and techniques used to identify the strongest relationships between variables.

## **Covariance Matrix**

The covariance matrix is a square matrix that summarizes the covariance between each pair of variables in a dataset. It is a fundamental concept in statistics and is used to calculate the correlation coefficients.

### Definition

The covariance matrix is defined as:

Cov(X, Y) = E[(X - E(X))(Y - E(Y))]

where X and Y are random variables, E(X) and E(Y) are the means of X and Y respectively, and E[(X - E(X))(Y - E(Y))] is the covariance between X and Y.

### Example

Suppose we have two variables X and Y, and the following covariance matrix:

|     | X   | Y   |
| --- | --- | --- |
| X   | 2.5 | 1.2 |
| Y   | 1.2 | 3.8 |

The covariance between X and Y is 1.2.

## **Fisher’s Linear Discriminant**

Fisher’s linear discriminant is a linear combination of features that maximizes the between-class variance while minimizing the within-class variance. It is a widely used technique in discriminant analysis to identify the most informative features.

### Definition

Fisher’s linear discriminant is defined as:

W = x^T _ Σ^(-1) _ (μ1 - μ2)

where W is the discriminant vector, x is the feature vector, Σ is the covariance matrix, μ1 and μ2 are the mean vectors of the two classes, and ^(-1) denotes the inverse.

### Example

Suppose we have a dataset with two features X and Y, and the following mean vectors:

μ1 = [2, 3]
μ2 = [4, 5]

The covariance matrix is:

Σ = | 2.5 1.2 |
| 1.2 3.8 |

The discriminant vector is:

W = x^T _ Σ^(-1) _ (μ1 - μ2) = [2, 3]

## **Generalized Linear Models**

Generalized linear models are a type of linear model that can handle non-linear relationships between the independent variables and the target variable.

### Definition

A generalized linear model is defined as:

y = β0 + β1 _ x1 + β2 _ x2 + … + βn \* xn + ε

where y is the target variable, β0, β1, β2, …, βn are the coefficients, x1, x2, …, xn are the independent variables, and ε is the error term.

### Example

Suppose we have a dataset with two features X and Y, and the following generalized linear model:

y = 2 + 1.5 _ X1 + 0.8 _ X2 + ε

## **Interpreting Results**

When interpreting the results of discriminant analysis, we need to consider the following:

- **Covariance matrix:** Look for variables with high covariance values, as they may have strong relationships with the target variable.
- **Fisher’s linear discriminant:** The discriminant vector indicates the direction of the strongest relationship between variables.
- **Generalized linear models:** The coefficients of the model indicate the strength and direction of the relationships between variables.

## **Key Concepts:**

- Covariance matrix
- Fisher’s linear discriminant
- Generalized linear models
- Interpreting results

## **Tips and Tricks:**

- Use the covariance matrix to identify variables with high covariance values.
- Use Fisher’s linear discriminant to identify the most informative features.
- Use generalized linear models to handle non-linear relationships between variables.

By following these concepts and techniques, you can identify the strongest relationships between variables in your dataset and make informed decisions in your data science projects.
