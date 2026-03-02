Of course. Here is a comprehensive educational module on "Levels of Significance" tailored for  Engineering students.

---

# Module 3: Statistical Inference 1 - Levels of Significance

## 1. Introduction

In the previous modules, you learned about estimating population parameters. Now, we enter the realm of **hypothesis testing**, where we make decisions about a population based on sample data. A critical component of this process is the **Level of Significance**, denoted by the Greek letter **α (alpha)**. It is the probability threshold against which we measure the strength of our evidence. Understanding α is crucial for making statistically sound decisions in fields like data science, machine learning, and quality control, which are integral to computer science and engineering.

## 2. Core Concepts

### What is a Level of Significance (α)?

The **level of significance** is the maximum probability of rejecting the null hypothesis ($H_0$) when it is actually true. In simpler terms, it's the risk you are willing to take of making a **Type I Error**.

- **Type I Error:** Incorrectly rejecting a true null hypothesis (a "false positive").
  - _Example:_ Concluding that a new algorithm is faster when, in reality, it is not.
- **Type II Error ($\beta$):** Failing to reject a false null hypothesis (a "false negative").
  - _Example:_ Concluding that a new algorithm is not faster when, in reality, it is.

By choosing α, you directly control the probability of a Type I Error.
$$P(\text{Type I Error}) = \alpha$$

### Commonly Used Values of α

The choice of α is somewhat arbitrary but is guided by convention and the context of the problem.

- **α = 0.05 (5%):** This is the most common standard. It implies you are willing to accept a 5% chance of a false positive.
- **α = 0.01 (1%):** Used when you require a higher standard of evidence. Common in medical trials or any scenario where the cost of a Type I Error is very high.
- **α = 0.10 (10%):** Sometimes used in preliminary research where a higher risk of a false positive is acceptable to avoid missing a potential discovery.

### The p-value: The Evidence Against $H_0$

To use α, you need to compare it to the **p-value**.

- **p-value:** The probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true.
- **The Decision Rule:** After calculating your test statistic and its corresponding p-value from sample data:
  - If **p-value ≤ α**: The sample data provides sufficient evidence to **reject the null hypothesis ($H_0$)**. The result is deemed "statistically significant."
  - If **p-value > α**: The sample data does not provide sufficient evidence to reject the null hypothesis. The result is "not statistically significant."

### Visualizing the Rejection Region

The level of significance α defines the **critical region** or **rejection region** on the probability distribution of your test statistic (e.g., the Z or T-distribution). This is the extreme, low-probability area under the tails of the distribution. If your calculated test statistic falls into this region, it leads to the rejection of $H_0$.

## 3. Example: Algorithm Efficiency

**Scenario:** A computer scientist claims a new sorting algorithm reduces average execution time. The old algorithm's mean time ($\mu_0$) is 100 ms.

- **Null Hypothesis ($H_0$):** $\mu = 100$ ms (The new algorithm is no better)
- **Alternative Hypothesis ($H_1$):** $\mu < 100$ ms (The new algorithm is faster)

We choose **α = 0.05**. We run the new algorithm multiple times, collect a sample, and calculate a test statistic. Suppose the resulting **p-value is 0.03**.

**Decision:** Since p-value (0.03) ≤ α (0.05), we reject the null hypothesis. We have statistically significant evidence at the 5% level to conclude that the new algorithm is faster.

**Important Note:** There is still a 3% chance that this observed improvement is just due to random sampling variation and the algorithm is actually no better.

## 4. Key Points & Summary

| Concept                   | Description                                                                  | Symbol | Common Value               |
| :------------------------ | :--------------------------------------------------------------------------- | :----- | :------------------------- |
| **Level of Significance** | The probability of making a Type I Error. The threshold for rejecting $H_0$. | **α**  | 0.05                       |
| **Type I Error**          | Rejecting a true null hypothesis (False Positive).                           | -      | $P(\text{Error}) = \alpha$ |
| **Type II Error**         | Failing to reject a false null hypothesis (False Negative).                  | **β**  | -                          |
| **p-value**               | The probability of observing the sample result, assuming $H_0$ is true.      | _p_    | Calculated                 |

**Summary:**

1.  **α is a pre-defined threshold** set by the researcher _before_ conducting a test.
2.  It quantifies your **tolerance for a false positive** (Type I Error).
3.  The **p-value is calculated from the sample data** and is the evidence against $H_0$.
4.  The final decision is made by **comparing the p-value to α**:
    - **Reject $H_0$** if p-value ≤ α.
    - **Do not reject $H_0$** if p-value > α.
5.  A lower α (e.g., 0.01) makes it **harder to reject $H_0$** and requires stronger evidence. There is always a trade-off between Type I and Type II errors.
