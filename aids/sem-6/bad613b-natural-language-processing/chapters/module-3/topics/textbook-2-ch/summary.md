# **Textbook 2: Ch - Natural Language Processing**

## **Naive Bayes Classifiers**

### Definitions

- **Naive Bayes**: A family of probabilistic classifiers based on Bayes' theorem, assuming conditional independence between features.
- **Conditional Independence**: The probability of a feature conditional on other features is independent of those features.

### Formulas

- **Naive Bayes Classifier**: P(class|features) = ∑(P(class) \* P(features|class)) / P(features)
- **Conditional Probability**: P(A|B) = P(A \* B) / P(B)
- **Joint Probability**: P(A \* B) = P(A) \* P(B|A)

### Key Points

- **Multinomial Naive Bayes**: For categorical features.
- **Bernoulli Naive Bayes**: For binary features.
- **Multinomial Naive Bayes for Categorical Features**:
  - P(class|features) = ∑(P(class) \* (P(feature1|class) \* P(feature2|class) \* ... \* P(featureN|class))) / P(features)
- **Bernoulli Naive Bayes for Binary Features**:
  - P(class|features) = ∑(P(class) \* P(feature|class)) / P(features)

### Theorems

- **Bayes' Theorem**: P(A|B) = P(A \* B) / P(B)
- **Conditional Probability Rule**: P(A|B) = P(A \* B) / P(B)

### Important Concepts

- **Conditional Probability**: The probability of an event conditional on another event.
- **Joint Probability**: The probability of two or more events occurring together.
- **Independence**: The probability of two or more events is independent if the occurrence of one event does not affect the probability of the other event.
