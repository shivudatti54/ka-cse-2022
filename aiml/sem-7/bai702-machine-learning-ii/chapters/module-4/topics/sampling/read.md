# Module 4: Sampling in Machine Learning

## Introduction

In the realm of machine learning, we often deal with massive datasets. However, building and training models on the entire population of data is frequently computationally expensive, time-consuming, and sometimes unnecessary. **Sampling** is a fundamental statistical technique that addresses this by selecting a subset of data points, known as a **sample**, from a larger population. The core assumption is that a properly chosen sample is representative of the entire population, allowing us to draw accurate inferences, build efficient models, and perform robust validation without the overhead of processing all the data.

## Core Concepts of Sampling

### 1. Population vs. Sample

*   **Population:** The complete set of all possible data points or observations of interest. (e.g., All engineering students in India).
*   **Sample:** A smaller, manageable subset selected from the population. (e.g., 10,000  students selected for a survey).

The goal is for the sample's properties (mean, variance, distribution) to closely mirror those of the population.

### 2. Why Sample in ML?

*   **Computational Efficiency:** Training on a sample is significantly faster and cheaper than on the entire dataset.
*   **Data Acquisition:** It's often impractical or impossible to collect data for an entire population.
*   **Model Validation:** Techniques like **train-test split** and **cross-validation** rely on sampling to create hold-out validation sets.
*   **Handling Imbalanced Data:** Sampling is key to techniques like **oversampling** the minority class or **undersampling** the majority class to create a balanced dataset.

### 3. Types of Sampling

Sampling methods are broadly classified into two categories:

#### A. Probability Sampling
Every data point in the population has a known, non-zero probability of being selected. This allows for unbiased inference about the population.

*   **Simple Random Sampling:** The gold standard. Every possible subset of `n` units has an equal chance of being selected. Like a random lottery. (e.g., Using `np.random.choice()` in Python to randomly pick data points).
*   **Systematic Sampling:** Selecting every `k-th` element from an ordered list. (k = N/n). It's simple but can introduce bias if the list has a hidden pattern.
*   **Stratified Sampling:** The population is divided into homogeneous subgroups called **strata** (e.g., strata based on class: 'Excellent', 'Good', 'Average'). Samples are then drawn randomly from each stratum. This ensures all key subgroups are represented.
*   **Cluster Sampling:** The population is divided into clusters (often geographically). A random sample of clusters is selected, and *all* data points within the chosen clusters are used. (e.g., selecting 5 city wards and surveying all students in those wards).

#### B. Non-Probability Sampling
The probability of selecting a particular data point is unknown. While faster and easier, the results are prone to selection bias and cannot be used for statistical inference.

*   **Convenience Sampling:** Selecting samples based on ease of access. (e.g., using the first 1000 rows of a dataset).
*   **Purposive Sampling:** The researcher uses their judgment to select samples that are most useful for the purpose.

### 4. Sampling Error and Bias

*   **Sampling Error:** The natural variation between the sample statistic and the population parameter that occurs because you are not surveying the entire population. It can be reduced by increasing the sample size.
*   **Sampling Bias:** A systematic error that makes the sample non-representative of the population. It invalidates your conclusions. Common causes include a flawed sampling frame (e.g., a voter list missing young voters) or non-random selection (e.g., convenience sampling).

## Example: Creating a Training Set

Imagine a dataset of 1,00,000 images for a cat vs. dog classifier.

1.  **Problem:** Training a complex CNN on all 100k images takes 10 hours per epoch.
2.  **Solution:** Apply **Stratified Sampling**.
    *   **Strata:** The two classes - 'cat' (40k images) and 'dog' (60k images).
    *   **Action:** Randomly select 10% from each stratum.
    *   **Result:** A balanced sample of 4,000 cats + 6,000 dogs = 10,000 images. This sample preserves the original class distribution and is far quicker to train on, likely leading to a model that generalizes well.

## Key Points & Summary

*   **Purpose:** Sampling allows for efficient, practical, and cost-effective model training and evaluation by working with a representative subset of data.
*   **Representativeness is Key:** A sample must accurately reflect the population's characteristics for any inference or model built on it to be valid.
*   **Probability vs. Non-Probability:** Prefer **probability sampling** (like random or stratified) for machine learning to avoid bias and enable statistical rigor. Non-probability methods are generally unsuitable for model training.
*   **Bias is a Critical Issue:** **Sampling bias** is a major pitfall that can lead to flawed models that fail in the real world. Always scrutinize how your data was collected.
*   **Foundational for Validation:** Core ML practices like **train-test splits**, **k-fold cross-validation**, and **bootstrapping** are all sophisticated applications of sampling techniques.
*   **Tool of Choice:** For handling imbalanced datasets, use sampling techniques like **SMOTE** (Synthetic Minority Oversampling Technique) or **RandomUnderSampler** to improve model performance on minority classes.