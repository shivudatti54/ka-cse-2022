**Subject: Mathematics for Computer Science**
**Module 3: Statistical Inference 1**
**Topic: Levels of Significance**

### Introduction

In statistical hypothesis testing, we use sample data to make inferences about a population parameter. A crucial part of this process is determining whether the observed sample data is significantly different from what we would expect under the null hypothesis (H₀). The **level of significance** is the threshold we set to decide what constitutes "significant" evidence. It is the probability of rejecting the null hypothesis when it is actually true—a false positive, known as a **Type I error**. For engineering students, especially in computer science, understanding this concept is vital for fields like A/B testing, machine learning model evaluation, and data-driven decision making.

### Core Concepts

#### 1. What is the Level of Significance?

Denoted by the Greek letter alpha (α), the level of significance is the maximum probability of committing a Type I error that a researcher is willing to accept. In simpler terms, it's the risk you are willing to take of being wrong when you reject the null hypothesis.

*   **Commonly used values:** α = 0.05 (5%), α = 0.01 (1%), and α = 0.10 (10%).
*   **Interpretation:** An α of 0.05 means you are willing to accept a 5% chance that you will incorrectly reject the null hypothesis. It defines the "unlikely" outcomes if the null hypothesis is true.

#### 2. The Relationship with the p-value

The decision to reject or not reject H₀ is made by comparing the **p-value** to the chosen α.

*   **p-value:** The probability of observing a test statistic as extreme as, or more extreme than, the one computed from your sample data, assuming the null hypothesis is true.
*   **Decision Rule:**
    *   If **p-value ≤ α**: The result is **statistically significant**. You reject the null hypothesis. The observed effect is unlikely to have occurred by random chance alone.
    *   If **p-value > α**: You **fail to reject the null hypothesis**. You do not have sufficient evidence to say the observed effect is real.

Think of α as the pre-set standard for how much evidence you need, and the p-value as the strength of the evidence you actually found.

#### 3. Critical Value and Rejection Region

The level of significance α directly defines the **critical value(s)** and the **rejection region** on a probability distribution (e.g., the standard normal Z-distribution or t-distribution).

*   **Critical Value:** The value of the test statistic that creates a boundary for the rejection region. The area under the curve beyond the critical value equals α.
*   **Rejection Region:** The set of all values of the test statistic for which the null hypothesis will be rejected.

For a two-tailed test with α = 0.05, the rejection region is in both tails, with 0.025 in each tail. The critical values might be Z = ±1.96.

### Example: Website A/B Testing

Imagine you are a data scientist testing if a new website design (Design B) leads to a higher click-through rate than the old design (Design A).

*   **Null Hypothesis (H₀):** The click-through rate of Design B is **equal to or less than** Design A.
*   **Alternative Hypothesis (H₁):** The click-through rate of Design B is **greater than** Design A.
*   **Choose a significance level:** You set **α = 0.05**. You are willing to take a 5% risk of wrongly concluding Design B is better.

You run the test and collect sample data. You calculate a test statistic and find the **p-value = 0.03**.

*   **Make a decision:** Since p-value (0.03) ≤ α (0.05), you reject the null hypothesis.
*   **Conclusion:** You have statistically significant evidence at the 5% level to conclude that Design B has a higher click-through rate than Design A.

**What if α was 0.01?** With the same p-value of 0.03, you would have p-value (0.03) > α (0.01). You would **fail to reject H₀**. The evidence is not strong enough to meet the stricter 1% significance standard. This highlights how the choice of α directly influences the conclusion.

### Choosing the Right Alpha (α)

The choice of α is not arbitrary and depends on the context and the consequences of error.
*   **α = 0.05:** A standard balance between risk and detection, used in most scientific and engineering fields.
*   **α = 0.01:** Used when the cost of a Type I error (a false positive) is very high. For example, in medical trials for a new drug with severe potential side effects, you want to be extremely confident before rejecting the null hypothesis of "no effect."
*   **α = 0.10:** Used in exploratory research or pilot studies where you are willing to take a higher risk of a false positive to identify potential effects for further study.

### Key Points & Summary

*   The **level of significance (α)** is the probability of making a **Type I error** (rejecting a true null hypothesis).
*   It is a **pre-defined threshold** set by the researcher *before* conducting a statistical test.
*   The calculated **p-value** is compared to α to make a decision: **Reject H₀ if p-value ≤ α**.
*   Alpha defines the **critical value(s)** and the **rejection region** on a statistical distribution.
*   Common values are 0.05, 0.01, and 0.10. The choice depends on the field and the consequences of drawing an incorrect conclusion.
*   A lower α (e.g., 0.01) makes it **harder to reject H₀**, reducing the chance of a false positive but increasing the chance of a **Type II error** (false negative). There is always a trade-off.

Understanding and correctly applying the level of significance is fundamental to drawing valid, reliable conclusions from data, a core skill for any computer scientist or engineer.