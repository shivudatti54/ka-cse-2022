# Understanding Data - 2: Bivariate Data and Multivariate Data

## Introduction

The progression from univariate analysis—examining variables in isolation—to multivariate analysis represents a fundamental paradigm shift in statistical methodology. **Bivariate analysis** investigates the relationship between exactly two variables, establishing the foundational framework for understanding pairwise associations. **Multivariate analysis** extends this framework to three or more variables simultaneously, acknowledging that most real-world phenomena are governed by complex interdependencies among multiple factors. In the context of machine learning, this multivariate perspective is indispensable: feature selection algorithms rely on correlation structures, regularized regression models address multicollinearity through variance decomposition, and dimensionality reduction techniques leverage covariance eigenstructure to project high-dimensional data onto informative subspaces.

This module provides a rigorous treatment of bivariate and multivariate statistical concepts, including formal derivations of key results, numerical illustrations, and practical applications relevant to machine learning pipelines.

---

## 1. Bivariate Data Analysis

### 1.1 Definition and Classification

**Definition 1.1 (Bivariate Data).** Bivariate data consists of paired observations $(X_i, Y_i)$ for $i = 1, 2, \ldots, n$, where each observation unit yields simultaneously measured values on two variables. The data may be classified according to the measurement scales of the constituent variables:

| Variable X  | Variable Y  | Relationship Type       | Example                        |
| ----------- | ----------- | ----------------------- | ------------------------------ |
| Continuous  | Continuous  | Numerical-Numerical     | Height vs. Weight              |
| Categorical | Categorical | Categorical-Categorical | Gender vs. Purchase Preference |
| Continuous  | Categorical | Numerical-Categorical   | Income vs. Employment Status   |
| Categorical | Numerical   | Categorical-Numerical   | Department vs. Salary          |

The distinction between these types determines the appropriate statistical measures and visualization techniques for analysis.

### 1.2 Scatter Plots for Numerical-Numerical Relationships

The **scatter plot** constitutes the primary graphical tool for visualizing bivariate relationships between two continuous variables. Each ordered pair $(X_i, Y_i)$ is represented as a point in the Cartesian plane, with $X$ plotted on the horizontal axis and $Y$ on the vertical axis.

```
 Scatter Plot Patterns

 Positive Correlation No Correlation Negative Correlation
 Y ^ Y ^ Y ^
 | . . | . . . | . .
 | . . | . . . | . .
 | . . | . . . | . .
 | . . | . . | . .
 | . . | . . . | . .
 +----------> X +----------> X +----------> X
```

From scatter plots, analysts extract information regarding:

1. **Direction**: Whether the relationship is positive (points trend upward from left to right) or negative (points trend downward)
2. **Strength**: The degree of clustering around a central tendency—tight clustering indicates strong association
3. **Form**: Whether the relationship follows a linear pattern or exhibits curvature (polynomial, exponential, etc.)
4. **Outliers**: Points substantially distant from the general pattern, warranting investigation for measurement error or genuine extreme values

---

## 2. Covariance and Its Properties

### 2.1 Definition

**Definition 2.1 (Sample Covariance).** Given bivariate data $(X_i, Y_i)$ for $i = 1, \ldots, n$, with sample means $\bar{X}$ and $\bar{Y}$, the **sample covariance** is defined as:

$$\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})$$

The divisor $n-1$ (rather than $n$) provides an unbiased estimator of the population covariance, consistent with the univariate sample variance formula.

### 2.2 Interpretation

The covariance sign indicates the **direction** of linear relationship:

- **Cov(X, Y) > 0**: $X$ and $Y$ tend to deviate from their means in the same direction—a positive association
- **Cov(X, Y) < 0**: $X$ and $Y$ tend to deviate in opposite directions—a negative association
- **Cov(X, Y) = 0**: No linear relationship exists (though non-linear relationships may persist)

### 2.3 Critical Limitation

Covariance is **scale-dependent**. If the variables $X$ and $Y$ are measured in different units, the magnitude of covariance is not comparable across different variable pairs. This limitation motivates the construction of scale-free standardized measures.

---

## 3. Pearson Correlation Coefficient

### 3.1 Definition and Derivation

**Definition 3.1 (Pearson Correlation Coefficient).** The Pearson product-moment correlation coefficient is defined as:

$$r = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2} \cdot \sqrt{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}}$$

where $\sigma_X$ and $\sigma_Y$ denote the sample standard deviations.

The division by the product of standard deviations normalizes the covariance to a **dimensionless quantity** independent of scale.

### 3.2 Proof: Correlation Coefficient Lies Between -1 and +1

**Theorem 3.1.** For any two variables $X$ and $Y$, $-1 \leq r \leq 1$.

_Proof._ Consider the expression:

$$r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2} \cdot \sqrt{\sum (Y_i - \bar{Y})^2}}$$

Define the **correlation coefficient** as the cosine of the angle between the centered vectors. Consider the **Cauchy-Schwarz Inequality**: For any real vectors $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$:

$$|\mathbf{a} \cdot \mathbf{b}| \leq \|\mathbf{a}\| \cdot \|\mathbf{b}\|$$

Let $\mathbf{a} = (X_1 - \bar{X}, \ldots, X_n - \bar{X})$ and $\mathbf{b} = (Y_1 - \bar{Y}, \ldots, Y_n - \bar{Y})$. Then:

$$|\sum (X_i - \bar{X})(Y_i - \bar{Y})| \leq \sqrt{\sum (X_i - \bar{X})^2} \cdot \sqrt{\sum (Y_i - \bar{Y})^2}$$

Dividing both sides by the denominator yields:

$$-1 \leq r \leq 1$$

Equality holds when $Y_i = aX_i + b$ for some constants $a$ and $b$ (perfect linear relationship). $\square$

### 3.3 Interpretation Guidelines

| Correlation Range    | Interpretation                       |
| -------------------- | ------------------------------------ |
| $r = +1$             | Perfect positive linear relationship |
| $0.7 \leq r < 1.0$   | Strong positive correlation          |
| $0.3 \leq r < 0.7$   | Moderate positive correlation        |
| $0 < r < 0.3$        | Weak positive correlation            |
| $r = 0$              | No linear correlation                |
| $-0.3 < r < 0$       | Weak negative correlation            |
| $-0.7 < r \leq -0.3$ | Moderate negative correlation        |
| $-1.0 < r \leq -0.7$ | Strong negative correlation          |
| $r = -1$             | Perfect negative linear relationship |

### 3.4 Assumptions

Pearson's $r$ is appropriate when:

1. Both variables are **continuous** (interval or ratio scale)
2. The relationship between variables is **linear**
3. The joint distribution is **bivariate normal** (for inferential tests)
4. Observations are **independent**

### 3.5 Worked Numerical Example

**Problem:** Given the dataset $X = [1, 2, 3, 4, 5]$ and $Y = [2, 4, 5, 4, 5]$, compute the Pearson correlation coefficient.

**Solution:**

_Step 1: Compute means_

$$\bar{X} = \frac{1+2+3+4+5}{5} = 3, \quad \bar{Y} = \frac{2+4+5+4+5}{5} = 4$$

_Step 2: Compute deviations and products_

| $X_i$ | $Y_i$ | $X_i - \bar{X}$ | $Y_i - \bar{Y}$ | Product |
| ----- | ----- | --------------- | --------------- | ------- |
| 1     | 2     | -2              | -2              | 4       |
| 2     | 4     | -1              | 0               | 0       |
| 3     | 5     | 0               | 1               | 0       |
| 4     | 4     | 1               | 0               | 0       |
| 5     | 5     | 2               | 1               | 2       |

_Step 3: Compute covariance_

$$\text{Cov}(X,Y) = \frac{4 + 0 + 0 + 0 + 2}{4} = \frac{6}{4} = 1.5$$

_Step 4: Compute standard deviations_

$$\sigma_X = \sqrt{\frac{(-2)^2 + (-1)^2 + 0^2 + 1^2 + 2^2}{4}} = \sqrt{\frac{10}{4}} = \sqrt{2.5} \approx 1.58$$

$$\sigma_Y = \sqrt{\frac{(-2)^2 + 0^2 + 1^2 + 0^2 + 1^2}{4}} = \sqrt{\frac{6}{4}} = \sqrt{1.5} \approx 1.22$$

_Step 5: Compute correlation_

$$r = \frac{1.5}{1.58 \times 1.22} = \frac{1.5}{1.93} \approx 0.78$$

**Interpretation:** The correlation coefficient of $r \approx 0.78$ indicates a **strong positive linear relationship** between $X$ and $Y$.

---

## 4. Spearman Rank Correlation

### 4.1 Definition

When the assumptions of Pearson's correlation are violated—particularly when data is ordinal, contains substantial outliers, or exhibits monotonic but non-linear relationships—the **Spearman rank correlation** provides a robust alternative.

**Definition 4.1 (Spearman Rank Correlation).** Given paired observations $(X_i, Y_i)$, let $R(X_i)$ and $R(Y_i)$ denote the ranks of $X_i$ and $Y_i$ respectively. The Spearman correlation is:

$$\rho_s = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}$\_i = R(X_i) - R(Y_i)$ is the difference$

where $d between ranks.

### 4.2 When to Use Spearman Over Pearson

| Condition                                          | Recommended Method |
| -------------------------------------------------- | ------------------ |
| Variables are ordinal                              | Spearman           |
| Data contains significant outliers                 | Spearman           |
| Relationship is monotonic but non-linear           | Spearman           |
| Both variables continuous and normally distributed | Pearson            |
| Linear relationship expected                       | Pearson            |

---

## 5. Analysis of Categorical-Categorical Bivariate Data

### 5.1 Cross-Tabulation (Contingency Tables)

When both variables are categorical, the **contingency table** provides a systematic summary of joint frequencies.

**Example:** Survey data on shopping preference by gender:

|                | Male | Female | Total |
| -------------- | ---- | ------ | ----- |
| Prefer Online  | 30   | 45     | 75    |
| Prefer Offline | 20   | 5      | 25    |
| **Total**      | 50   | 50     | 100   |

### 5.2 Chi-Square Test of Independence

The **Chi-square ($\chi^2$) test** determines whether two categorical variables are statistically independent.

**Test Statistic:**

$$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

where $O_{ij}$ is the observed frequency and $E_{ij} = \frac{(\text{row total}) \times (\text{column total})}{\text{grand total}}$ is the expected frequency under the null hypothesis of independence.

**Degrees of freedom:** $df = (r-1)(c-1)$

---

## 6. Correlation Versus Causation

### 6.1 Conceptual Distinction

A fundamental principle in statistical analysis is the distinction between **correlation** (statistical association) and **causation** (direct influence):

- **Correlation**: $A \xleftarrow{\text{?}} B$ — variables move together but may share a common cause
- **Causation**: $A \rightarrow B$ — changes in $A$ directly produce changes in $B$

```
Correlation: Hot Weather ----> Ice Cream Sales
 | |
 v v
 Drowning Incidents <------+

Causation Model: Smoking ----> Lung Cancer
```

### 6.2 The Spurious Correlation Problem

**Classic Example:** Ice cream sales and drowning incidents exhibit positive correlation. However, ice cream consumption does not cause drowning. The **confounding variable**—hot weather—causes both: people buy more ice cream and swim more frequently during hot weather, increasing drowning risk.

### 6.3 Implications for Machine Learning

In feature selection, relying exclusively on correlation-based criteria may introduce **spurious features** that predict outcomes through confounding mechanisms. This poses particular challenges in:

1. **Multicollinearity**: Highly correlated predictors in linear regression inflate variance of coefficient estimates
2. **Feature Leakage**: Proxy variables that encode the target directly lead to overfitting
3. **Interpretability**: Correlated features obscure the true causal drivers of the outcome

---

## 7. Multivariate Data Analysis

### 7.1 Introduction to Multivariate Data

**Definition 7.1 (Multivariate Data).** Multivariate data consists of observations on $p \geq 3$ variables for each unit of observation: $(X_{i1}, X_{i2}, \ldots, X_{ip})$ for $i = 1, \ldots, n$.

In machine learning contexts, multivariate data structures arise frequently:

- **Feature vectors** in classification/regression problems
- **Time series** with multiple lags
- **Text data** represented as term frequency vectors

### 7.2 The Covariance Matrix

The univariate concepts of variance and covariance generalize naturally to the multivariate setting through the **covariance matrix**.

**Definition 7.2 (Sample Covariance Matrix).** For $p$ variables observed on $n$ units, the $p \times p$ sample covariance matrix is:

$$\mathbf{S} = \begin{bmatrix} s_1^2 & s_{12} & \cdots & s_{1p} \\ s_{21} & s_2^2 & \cdots & s_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ s_{p1} & s_{p2} & \cdots & s_p^2 \end{bmatrix}$$

where $s_j^2$ is the sample variance of the $j$-th variable and $s_{jk} = \text{Cov}(X_j, X_k)$.

**Properties of the Covariance Matrix:**

1. **Symmetry**: $\mathbf{S} = \mathbf{S}^T$
2. **Positive Semi-definiteness**: All eigenvalues $\lambda_i \geq 0$
3. **Interpretation**: Diagonal elements capture marginal variability; off-diagonal elements capture pairwise associations

### 7.3 The Correlation Matrix

The **correlation matrix** $\mathbf{R}$ standardizes the covariance matrix by the product of standard deviations:

$$\mathbf{R}_{jk} = \frac{s_{jk}}{s_j \cdot s_k}$$

The correlation matrix is also symmetric and positive semi-definite, with unit diagonal elements.

### 7.4 Multivariate Visualization Techniques

| Technique                       | Variables           | Purpose                                             |
| ------------------------------- | ------------------- | --------------------------------------------------- |
| Scatter Plot Matrix (Pair Plot) | All numerical pairs | Visualize pairwise relationships in grid format     |
| Correlation Heatmap             | All pairs           | Color-coded visualization of correlation magnitudes |
| 3D Scatter Plot                 | 3 numerical         | Visualize trivariate relationships                  |
| Parallel Coordinates            | Multiple numerical  | Compare variable profiles across observations       |

### 7.5 Connection to Machine Learning

The covariance matrix plays a central role in several machine learning algorithms:

1. **Principal Component Analysis (PCA)**: Eigenvalue decomposition of the covariance matrix yields orthogonal directions of maximum variance
2. **Linear Discriminant Analysis (LDA)**: Within-class and between-class covariance matrices determine the projection maximizing class separability
3. **Mahalanobis Distance**: Multivariate distance measure incorporating covariance structure
4. **Regularized Regression (Ridge/LASSO)**: Penalty terms address instability arising from high covariance among predictors

---

## 8. Summary

This module has examined statistical methods for analyzing relationships between variables:

1. **Bivariate Analysis** establishes foundational concepts of association between two variables, including covariance as a measure of joint variability and Pearson correlation as its standardized counterpart bounded between -1 and +1.

2. **Spearman Rank Correlation** provides a robust alternative when linearity assumptions are violated or ordinal data is encountered.

3. **Categorical Bivariate Analysis** utilizes contingency tables and the chi-square test for assessing independence between categorical variables.

4. **The Critical Distinction** between correlation and causation underscores the importance of causal reasoning in feature selection and model building.

5. **Multivariate Analysis** generalizes bivariate concepts to $p > 2$ variables through the covariance matrix, enabling dimensionality reduction, feature engineering, and advanced modeling techniques essential for modern machine learning applications.

These foundations prepare students for subsequent topics including multivariate statistical inference, dimensionality reduction, and advanced regression methodologies.

---

## 9. Assessment

### Multiple Choice Questions

**Question 1:** Which of the following statements about the Pearson correlation coefficient $r$ is correct?

(A) $r$ can be greater than 1 if the relationship is strongly non-linear
(B) $r$ is unitless and therefore does not depend on the scales of $X$ and $Y$
(C) $r = 0$ implies that $X$ and $Y$ are independent
(D) A negative correlation indicates that $X$ causes $Y$ to decrease

**Answer:** (B)

---

**Question 2:** Given the following bivariate data, compute the correlation coefficient:

$X$: [10, 20, 30, 40, 50]
$Y$: [15, 25, 35, 45, 55]

(A) $r = 0.5$
(B) $r = 1.0$
(C) $r = 0$
(D) $r = -1.0$

**Answer:** (B) — The data perfectly follows $Y = X + 5$, hence $r = 1.0$

---

**Question 3:** Under what condition does the Spearman rank correlation equal the Pearson correlation?

(A) When both variables are normally distributed
(B) When the relationship between variables is perfectly linear
(C) When the relationship is monotonic but not necessarily linear
(D) When sample size is large ($n > 30$)

**Answer:** (C)

---

**Question 4:** In a covariance matrix $\mathbf{S}$ of dimension $p \times p$, how many unique elements must be estimated from data?

(A) $p$
(B) $p^2$
(C) $p(p+1)/2$
(D) $2p$

**Answer:** (C) — Due to symmetry, only $\frac{p(p+1)}{2}$ elements (diagonal variances and unique covariances) require estimation

---

**Question 5:** Two variables $X$ and $Y$ have covariance $\text{Cov}(X, Y) = 0$. Which statement is necessarily true?

(A) $X$ and $Y$ are independent
(B) $r = 0$
(C) There is no relationship between $X$ and $Y$
(D) The scatter plot shows a horizontal line

**Answer:** (B) — Zero covariance implies zero Pearson correlation, but independence cannot be concluded without additional information

---

### Flashcard

| Term                     | Definition                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Covariance**           | A measure of joint variability between two variables, indicating the direction of linear relationship        |
| **Pearson Correlation**  | Standardized covariance measure bounded between -1 and +1, independent of variable scales                    |
| **Confounding Variable** | A variable that influences both the dependent and independent variable, creating a spurious association      |
| **Multicollinearity**    | High correlation among predictor variables in regression, causing inflated variance in coefficient estimates |
