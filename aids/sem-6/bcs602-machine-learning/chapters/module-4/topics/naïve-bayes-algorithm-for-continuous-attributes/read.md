# **Naïve Bayes Algorithm for Continuous Attributes**

## **Introduction**

The Naïve Bayes algorithm is a popular supervised learning algorithm used for classification and regression tasks. In this study material, we will focus on the Naïve Bayes algorithm for continuous attributes, which deals with continuous-valued features.

## **What is Naïve Bayes?**

Naïve Bayes is a family of probabilistic classifiers based on Bayes' theorem, which is a mathematical formula for determining the probability of an event based on the probabilities of its constituent parts. The algorithm is called "naïve" because it assumes that the features are independent, meaning that the value of one feature does not affect the value of another feature.

## **Key Concepts**

- **Conditional Probability**: The probability of an event occurring given that another event has occurred.
- **Bayes' Theorem**: The probability of an event happening given some prior knowledge of conditions that might be related to the event.
- **Naïve Assumption**: The assumption that each feature is independent of every other feature.

### Naïve Bayes Classifier

The Naïve Bayes classifier uses the following steps to classify new data points:

1.  **Calculate Prior Probabilities**: Calculate the prior probability of each class.
2.  **Calculate Likelihoods**: Calculate the likelihood of each feature given each class.
3.  **Calculate Posterior Probabilities**: Calculate the posterior probability of each class given each feature.
4.  **Classify**: Choose the class with the highest posterior probability.

### Naïve Bayes for Continuous Attributes

To implement Naïve Bayes for continuous attributes, we need to calculate the likelihood of each feature given each class. We can do this by using the following formula:

P(X=x|y=c) = (1/σ(y))^n \* f(x) \* P(y=c)

where:

- P(X=x|y=c) is the probability of feature x given class c
- σ(y) is the standard deviation of class y
- n is the number of features
- f(x) is the probability density function of feature x
- P(y=c) is the prior probability of class c

### Example

Suppose we have a dataset with two continuous features: age and income. We want to classify people into two classes: high-income and low-income. We can use Naïve Bayes to calculate the likelihood of each feature given each class.

| Age | Income | High-Income | Low-Income |
| --- | ------ | ----------- | ---------- |
| 25  | 50000  | 0.7         | 0.3        |
| 30  | 60000  | 0.8         | 0.2        |
| 35  | 70000  | 0.9         | 0.1        |

In this example, we can calculate the likelihood of age given each class as follows:

- P(Age=25|High-Income) = 0.7
- P(Age=25|Low-Income) = 0.3
- P(Age=30|High-Income) = 0.8
- P(Age=30|Low-Income) = 0.2
- P(Age=35|High-Income) = 0.9
- P(Age=35|Low-Income) = 0.1

We can then use these likelihoods to calculate the posterior probabilities of each class given each feature.

### Code Implementation

Here is a simple implementation of the Naïve Bayes algorithm for continuous attributes in Python:

```python
import numpy as np
from scipy.stats import norm

class NaiveBayes:
    def __init__(self):
        self.classes = []
        self.means = []
        self.stds = []

    def fit(self, X, y):
        self.classes = np.unique(y)
        self.means = []
        self.stds = []

        for c in self.classes:
            X_c = X[y == c]
            self.means.append(X_c.mean())
            self.stds.append(X_c.std())

    def predict(self, X):
        predictions = []
        for x in X:
            posterior_probabilities = []
            for c in self.classes:
                likelihood = np.prod(norm.pdf(x, loc=self.means[c], scale=self.stds[c]))
                posterior_probability = likelihood * (len(self.classes) / len(y)) * (1 / np.sqrt(2 * np.pi * self.stds[c]**2))
                posterior_probabilities.append(posterior_probability)
            predictions.append(np.argmax(posterior_probabilities))
        return predictions

# Example usage
np.random.seed(0)
X = np.random.normal(0, 1, size=(100, 2))
y = np.random.choice([0, 1], size=100)

nb = NaiveBayes()
nb.fit(X, y)
predictions = nb.predict(X)

print("Predictions:", predictions)
```

This code implements a simple Naïve Bayes classifier for continuous attributes. It uses the mean and standard deviation of each feature given each class to calculate the likelihood of each feature. The classifier then uses these likelihoods to calculate the posterior probabilities of each class given each feature and chooses the class with the highest posterior probability.
