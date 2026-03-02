# **Chi-Square Distribution as a Test of Goodness of Fit**

## **Key Concepts**

- **Goodness of Fit**: A statistical test used to determine how well observed data fits expected distributions.
- **Chi-Square Distribution**: A discrete probability distribution that arises from the sum of squares of independent standard normal variables.

## **Formulas and Definitions**

- **Chi-Square Statistic** (χ²): Σ [(observed frequency - expected frequency)^2 / expected frequency]
- **Degrees of Freedom** (k): Number of categories minus 1
- **Expected Frequency** (Ei): (Total observations \* row total) / Total observations
- **Chi-Square Distribution Table**: A table of critical values for χ² with different degrees of freedom

## **Theorems and Assumptions**

- **Central Limit Theorem**: The distribution of χ² is approximately normal with mean k and variance 2k if the observations are independent and identically distributed.
- **Independence Assumption**: The observations must be independent and identically distributed.
- **Homogeneity Assumption**: The expected frequencies must be approximately equal across all categories.

## **Key Points**

- The chi-square distribution is used to test the goodness of fit of a distribution.
- The test statistic is calculated as the sum of squared differences between observed and expected frequencies.
- The degrees of freedom are determined by the number of categories.
- The critical region is typically in the right tail of the chi-square distribution.
- The test is sensitive to non-normality of the data and non-independence of the observations.

## **Important Formulas and Results**

- χ² = Σ [(observed frequency - expected frequency)^2 / expected frequency] with degrees of freedom k
- p-value = P(χ² > calculated χ²) with degrees of freedom k
- Reject the null hypothesis if p-value < α
