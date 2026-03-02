# Design of Experiments & ANOVA

## Introduction

Design of Experiments (DoE) and Analysis of Variance (ANOVA) are fundamental statistical methodologies used extensively in Computer Science and Engineering. They provide a structured, efficient approach to analyzing complex systems where multiple factors can influence an outcome. Whether you are optimizing a machine learning algorithm's hyperparameters, testing software performance under different configurations, or analyzing network traffic patterns, DoE and ANOVA are powerful tools for drawing meaningful, data-driven conclusions.

## Core Concepts

### 1. Design of Experiments (DoE)

DoE is a systematic method for planning, conducting, analyzing, and interpreting controlled tests. Its primary goal is to evaluate the factors that influence a particular response variable.

*   **Key Principle:** Instead of changing one factor at a time (OFAT), which is inefficient and can miss interaction effects, DoE varies all relevant factors simultaneously in a controlled pattern.
*   **Basic Terminology:**
    *   **Factors (or Independent Variables):** The input variables or parameters you control in an experiment (e.g., cache size, number of threads, learning rate).
    *   **Levels:** The specific values or settings chosen for a factor (e.g., cache size: 2MB, 4MB, 8MB).
    *   **Response (or Dependent Variable):** The output or performance metric you measure (e.g., execution time, accuracy, throughput).
    *   **Treatment:** A specific combination of factor levels used in an experimental run.
    *   **Replication:** Repeating the same treatment multiple times to estimate experimental error.

*   **Common Designs:**
    *   **Full Factorial Design:** Tests all possible combinations of all levels of all factors. It's comprehensive but can become computationally expensive as the number of factors grows (`n^k` runs).
    *   **Fractional Factorial Design:** A carefully chosen subset of a full factorial design. It's used to screen many factors efficiently, assuming higher-order interactions are negligible.

### 2. Analysis of Variance (ANOVA)

ANOVA is the statistical technique used to analyze the data collected from a designed experiment. It partitions the total variation in the response data into components attributable to different sources of variation (factors and error).

*   **Null Hypothesis (H₀):** The means of the response variable across different groups (or factor levels) are all equal.
*   **Alternative Hypothesis (H₁):** At least one group mean is different.
*   **The ANOVA Table:** The result of an ANOVA is typically summarized in a table:
| Source of Variation | Sum of Squares (SS) | Degrees of Freedom (df) | Mean Square (MS) | F-value |
| :--- | :--- | :--- | :--- | :--- |
| Between Groups (Factor) | SS<sub>Factor</sub> | k - 1 | MS<sub>Factor</sub> = SS<sub>Factor</sub> / df<sub>Factor</sub> | F = MS<sub>Factor</sub> / MS<sub>Error</sub> |
| Within Groups (Error) | SS<sub>Error</sub> | N - k | MS<sub>Error</sub> = SS<sub>Error</sub> / df<sub>Error</sub> | |
| **Total** | **SS<sub>Total</sub>** | **N - 1** | | |

*   **The F-test:** The calculated F-value is compared to a critical F-value from statistical tables (based on the degrees of freedom and a chosen significance level, α, often 0.05).
    *   If F > F<sub>critical</sub>, we **reject the null hypothesis (H₀)**. This indicates that the variation due to the factor is significantly larger than the random variation (error), meaning the factor has a statistically significant effect on the response.
    *   If F ≤ F<sub>critical</sub>, we **fail to reject H₀**.

## Example: Testing Sorting Algorithms

Imagine an experiment to compare the execution time of three different sorting algorithms (Bubble Sort, Merge Sort, Quick Sort) – this is the single **factor** "Algorithm" with three **levels**.

1.  **Design:** You would run each algorithm on the same set of multiple randomized input arrays (**replication**).
2.  **Data Collection:** Measure the execution time for each run (**response**).
3.  **ANOVA:** Perform a one-way ANOVA (one factor) to test:
    *   H₀: µ<sub>Bubble</sub> = µ<sub>Merge</sub> = µ<sub>Quick</sub>
    *   H₁: At least one mean execution time is different.
4.  **Conclusion:** If ANOVA gives a significant F-value (e.g., p-value < 0.05), you conclude that the choice of algorithm *does* significantly affect execution time. You would then use post-hoc tests (like Tukey's HSD) to determine *which specific algorithms* differ from each other.

## Key Points & Summary

*   **DoE** is about **efficiently structuring** how data is collected.
*   **ANOVA** is the **statistical tool** used to analyze that collected data.
*   The core idea is to **compare the variance between groups** (caused by the factor) to the **variance within groups** (natural random error).
*   A significant **F-test** indicates that the factor being studied has a real, measurable effect on the system's output.
*   These techniques are crucial for **A/B testing**, **algorithm optimization**, **performance analysis**, and any scenario requiring rigorous comparison of multiple systems or configurations.