# Analysis of Completely Randomized Design

**Definition**

- A completely randomized design (CRD) is a type of experimental design where all treatments are randomly assigned to all possible combinations of experimental units

**Key Points**

- **Randomization**: Each experimental unit is assigned a treatment randomly, with no prior knowledge of the treatment's effect
- **Independence**: Each experimental unit is independent of others, with no correlation between units
- **Replication**: Each treatment is replicated a fixed number of times (n)
- **Confounding Variables**: None, as all treatments are randomized

**Important Formulas**

- **Mean Squared Error (MSE)**: Measures the average variation within the data
  - MSE = Σ[(observed - expected)^2] / (n - k - 1)
- **Degrees of Freedom (df)**: Measures the number of independent pieces of information
  - df = n - 1
- **Sum of Squares (SS)**: Measures the total variation in the data
  - SS = Σ(observed^2) + Σ(expected^2)

**Theorems**

- **Central Limit Theorem (CLT)**: States that the distribution of the sample mean will be approximately normal, even if the population distribution is not normal
- **F-distribution**: Used to test the significance of the treatment mean difference

**Analysis Steps**

1. Calculate the overall mean
2. Calculate the treatment mean
3. Calculate the MSE
4. Calculate the SS
5. Calculate the df
6. Use the F-distribution to test the significance of the treatment mean difference

**Critical Values**

- **F-critical value**: The value of F from the F-distribution with df1 and df2 degrees of freedom, which separates the rejection region from the non-rejection region

**Assumptions**

- Normality of residuals
- Homoscedasticity (constant variance)
- Independence of observations
