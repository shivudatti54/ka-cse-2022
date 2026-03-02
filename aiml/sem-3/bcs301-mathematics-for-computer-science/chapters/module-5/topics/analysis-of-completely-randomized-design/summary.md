# **Analysis of Completely Randomized Design**

### Definitions

- **Completely Randomized Design (CRD):** An experimental design where all treatments are applied to all combinations of experimental units.
- **Experimental Unit:** The individual units being tested, such as plants, animals, or machines.
- **Treatment:** The different variables being tested, such as different levels of fertilizer.

### Key Concepts

- **Replication:** The number of times each treatment is repeated in the experiment.
- **Block:** A group of experimental units that are similar in some way, such as different soil types.
- **Error:** The variation in the response variable that is not due to the treatment.

### Formulas and Theorems

- **Degrees of Freedom (df):** Calculated as df = (replications - 1) + (treatments - 1) + (block - 1)
- **Mean Square Error (MSE):** Calculated as MSE = (sum of squared errors) / (df - treatments + 1)
- **F-statistic:** Calculated as F = MSE / (MST - MSE), where MST is the Mean Square Treatment.
- **ANOVA Table:**

| Source    | df    | SS   | MS    | F   |
| --------- | ----- | ---- | ----- | --- |
| Treatment | `t-1` | `ST` | `MST` | `F` |
| Error     | `e-1` | `SE` | `MSE` |     |
| Total     | `n-1` | `TS` |       |     |

### Important Theorems

- **Central Limit Theorem:** The sampling distribution of the treatment mean is approximately normal with a mean of μ and a standard error of σ / sqrt(n), where n is the number of replications.
- **F-distribution:** The F-statistic follows an F-distribution with `t-1` and `e-1` degrees of freedom.

### Key Points for Revision

- Understand the definitions of CRD, experimental unit, and treatment.
- Know the formulas and theorems for calculating df, MSE, F-statistic, and ANOVA table.
- Recognize the importance of replication, blocking, and error in CRD.
- Recall the Central Limit Theorem and F-distribution theorems.
