# Naive Bayes Classifier

## Introduction
Naive Bayes is a probabilistic machine learning algorithm widely used for classification tasks. It is based on **Bayes' Theorem** with a "naive" assumption of conditional independence between features. Despite its simplicity, it performs remarkably well in many real-world applications, particularly in text classification.

---

## Key Concepts

### 1. Bayes' Theorem
The foundation of Naive Bayes:
- **P(A|B) = [P(B|A) × P(A)] / P(B)**
- **P(A|B)** = Posterior probability (probability of class A given feature B)
- **P(A)** = Prior probability of class A
- **P(B|A)** = Likelihood (probability of feature B given class A)
- **P(B)** = Evidence (probability of feature B)

### 2. Naive Assumption
- Assumes all features are **conditionally independent** given the class
- This simplifies calculation: P(X₁, X₂, ..., Xₙ|C) = P(X₁|C) × P(X₂|C) × ... × P(Xₙ|C)

### 3. Types of Naive Bayes Classifiers

| Type | Use Case |
|------|----------|
| **Gaussian** | Continuous features (e.g., iris dataset) |
| **Multinomial** | Text classification, word counts |
| **Bernoulli** | Binary/boolean features |

### 4. Working Steps
1. Calculate prior probability for each class
2. Compute likelihood for each feature given each class
3. Apply Bayes theorem to find posterior probability
4. Select class with highest posterior probability

### 5. Laplace Smoothing (Additive Smoothing)
- Used to handle zero probabilities for unseen features
- Formula: **P(xᵢ|c) = (count(xᵢ, c) + α) / (count(c) + α|V|)**
- α = smoothing parameter (usually 1)

---

## Advantages
- Simple to implement and fast to train/predict
- Works well with high-dimensional data
- Handles missing values gracefully
- Performs well with small training data

## Limitations
- Strong independence assumption often violated in reality
- Cannot learn relationships between features
- Zero probability problem for unseen feature combinations

---

## Applications (As per DU Syllabus)
- **Spam email detection**
- **Sentiment analysis**
- **Document classification**
- **Medical diagnosis**
- **Credit risk assessment**

---

## Conclusion
Naive Bayes is a fundamental probabilistic classifier in Machine Learning. Its simplicity, efficiency, and effectiveness make it ideal for quick baseline models and text-related classification tasks. Despite its "naive" assumption, it remains a popular choice for exam preparation and practical applications.

> **Exam Tip:** Remember the Bayes theorem formula and understand when to use each type (Gaussian, Multinomial, Bernoulli).