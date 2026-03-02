Of course. Here is comprehensive educational content on the Chi-square test, tailored for  Engineering students in the "Statistical Machine Learning for Data Science" course.

# Module 2: Chi-square Test for Feature Selection

## 1. Introduction

In data science and machine learning, datasets often contain a mix of numerical and categorical features. A critical step in building an effective model is **feature selection**—identifying and retaining the most relevant features that have a strong relationship with the target variable. The **Chi-square (χ²) test** is a fundamental statistical hypothesis test used specifically for this purpose when dealing with categorical variables. It helps us determine if there is a significant association between a categorical feature and the target class, allowing us to filter out irrelevant features and improve model performance.

## 2. Core Concepts

### What is the Chi-square Test?

The Chi-square test is a non-parametric statistical test used to examine the relationship between two categorical variables. It assesses whether the distribution of sample categorical data is consistent with an expected distribution (Goodness-of-Fit) or, more commonly in feature selection, whether two variables are independent of each other (Test of Independence).

The core idea is simple: **it compares the observed frequencies in the data with the frequencies we would expect to see if the two variables were completely independent.**

### The Chi-square Statistic Formula

The value that quantifies this difference is the Chi-square statistic, calculated as:

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Where:
*   $O_i$ = Observed frequency in each category/cell
*   $E_i$ = Expected frequency if the variables were independent
*   The summation $\sum$ is over all categories or cells in the contingency table.

A higher χ² value indicates a greater difference between observed and expected values, suggesting a stronger evidence **against** the null hypothesis (which states that the variables are independent).

### How is the Expected Frequency Calculated?

For a contingency table, the expected frequency for a cell (row $i$, column $j$) is calculated as:
$$E_{ij} = \frac{( \text{Row Total}_i ) \times ( \text{Column Total}_j )}{\text{Grand Total}}$$

This formula comes directly from the definition of statistical independence: P(A and B) = P(A) * P(B).

### The Feature Selection Process using χ²

In machine learning, we use the Chi-square test to rank features. The process is as follows:
1.  **Form Hypotheses:**
    *   **Null Hypothesis (H₀):** The two categorical variables are independent.
    *   **Alternative Hypothesis (H₁):** The two variables are dependent (associated).

2.  **Construct a Contingency Table:** For each feature and the target, create a table showing the frequency distribution of their categories.

3.  **Calculate the χ² statistic:** Use the formula above for the contingency table.

4.  **Determine Significance:**
    *   The calculated χ² value is compared against a **critical value** from the Chi-square distribution table. This critical value depends on the **degrees of freedom (df)** and the chosen **significance level (α)**, typically 0.05 or 0.01.
    *   **Degrees of Freedom (df)** for a contingency table is: $df = (number\ of\ rows - 1) * (number\ of\ columns - 1)$

5.  **Make a Decision:**
    *   If $\chi^2_{calculated} > \chi^2_{critical}$ (or if the corresponding **p-value < α**), we **reject the null hypothesis (H₀)**. This means the feature is likely dependent on the target and is relevant for prediction.
    *   If $\chi^2_{calculated} <= \chi^2_{critical}$ (or p-value >= α), we **fail to reject H₀**. The feature is independent of the target and is a candidate for removal.

## 3. Example: Selecting a Feature for a Marketing Campaign

Imagine you are building a model to predict whether a customer will click on a marketing email (`Clicked`: Yes/No). You have a categorical feature `Age_Group` (Young, Middle-aged, Senior).

**Step 1: Contingency Table (Observed Frequencies)**

| Age Group     | Clicked = No | Clicked = Yes | Row Total |
| :------------ | :----------: | :-----------: | :-------: |
| Young         | 45           | 55            | 100       |
| Middle-aged   | 70           | 30            | 100       |
| Senior        | 80           | 20            | 100       |
| **Column Total** | **195**      | **105**       | **300**   |

**Step 2: Calculate Expected Frequencies (E)**
For the "Young & Clicked=No" cell:
$E = (100 * 195) / 300 = 65$
For the "Young & Clicked=Yes" cell:
$E = (100 * 105) / 300 = 35$

Repeat this for all cells.

**Step 3: Calculate χ² statistic**
For each cell, compute $\frac{(O-E)^2}{E}$ and sum them up.
$\chi^2 = \frac{(45-65)^2}{65} + \frac{(55-35)^2}{35} + \frac{(70-65)^2}{65} + ...$
This calculation yields a single χ² value (let's assume it's **32.5**).

**Step 4: Determine Significance**
*   Degrees of Freedom: $df = (3-1)*(2-1) = 2$
*   For α=0.05, the critical value from the χ² table is **5.991**.

**Step 5: Decision**
Since $32.5 > 5.991$, we reject the null hypothesis. We conclude that `Age_Group` and `Clicked` are **not independent**. Therefore, `Age_Group` is a relevant feature for our model and should be retained.

## 4. Key Points & Summary

*   **Purpose:** The Chi-square test is used for feature selection with categorical variables by testing the independence between a feature and the target label.
*   **Core Idea:** It compares observed frequencies in the data to the expected frequencies if the variables were independent. A large discrepancy leads to a high χ² value.
*   **Hypothesis Testing:** Rejecting the null hypothesis (H₀) implies a significant association, making the feature relevant.
*   **Assumptions:** The test requires the data to be frequencies (not percentages), categories must be mutually exclusive, and expected frequencies in each cell should ideally be greater than 5 for reliability.
*   **ML Usage:** In `scikit-learn`, the `chi2` function from `sklearn.feature_selection` is used to calculate χ² statistics and p-values, which are then used with `SelectKBest` or `SelectPercentile` to choose the top-k features.
*   **Limitation:** It only captures linear associations between categorical variables. It cannot evaluate the strength of the relationship, only its existence.