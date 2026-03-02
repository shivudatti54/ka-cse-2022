# Categorical Data

=====================

## Definitions and Formulas

---

- **Categorical variable**: A variable that takes on a limited number of distinct values, often represented as categories or labels.
- **Category**: A distinct value or label assigned to an observation.
- **One-hot encoding**: A technique for representing categorical variables as binary vectors.
  - Formula: `x^{(c)} = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}`, where `x^{(c)}` is the one-hot encoding of category `c`.

## Theorems

---

- **The Law of Total Probability**: A theorem that describes the relationship between the probability of a categorical variable and the probabilities of its individual categories.
  - Formula: `P(X) = \sum_{c} P(X=c)P(C=c)`, where `P(X)` is the probability of the categorical variable `X`, `P(X=c)` is the probability of category `c`, and `P(C=c)` is the probability of category `c` given the value of `X`.

## Important Concepts

---

- **Mode**: The most frequently occurring category in a categorical variable.
- **Median**: The middle value of a categorical variable when it is ordered from least to greatest.
- **Frequency distribution**: A table or graph that shows the number of observations that fall into each category.

## Important Formulas

---

- **Fisher's Exact Test**: A statistical test used to determine whether there is a significant association between two categorical variables.
  - Formula: `P(X) = \sum_{i=0}^{n} \binom{n}{i} \binom{m-i}{k-i} \binom{j-i}{k-i}`, where `n` is the total number of observations, `m` is the number of observations in one category, `j` is the number of observations in another category, and `k` is the number of observations in the intersection of the two categories.
