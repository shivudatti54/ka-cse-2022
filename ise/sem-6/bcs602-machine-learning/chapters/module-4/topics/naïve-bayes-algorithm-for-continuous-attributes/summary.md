# Naïve Bayes Algorithm for Continuous Attributes

### Overview

- Naïve Bayes algorithm is a probabilistic classifier based on Bayes' theorem.
- It is suitable for continuous attributes and multi-class classification problems.

### Key Formulas and Definitions

- **Bayes' Theorem**:
  ```math
  P(C|X) = \frac{P(X|C) \cdot P(C)}{P(X)}
  ```

```
  where `P(C|X)` is the posterior probability of class `C` given feature `X`, `P(X|C)` is the likelihood of feature `X` given class `C`, and `P(X)` is the marginal probability of feature `X`.

* **Naïve Bayes Assumption**:
  Assume independence between features, i.e., `P(X|C) = P(X_1|C) \cdot P(X_2|C) \cdot ... \cdot P(X_n|C)`, where `X_i` is the `i-th` feature.

* **Conditional Probability Distribution**:
  `P(X_i|C) = \frac{f_{i}(x_i)}{\sum_{x_i} f_{i}(x_i)}`, where `f_i(x_i)` is the probability density function of feature `X_i`.

* **Prior Probability**:
  `P(C) = \frac{N_C}{N}`, where `N_C` is the number of samples in class `C` and `N` is the total number of samples.

### Theorem

* **Naïve Bayes Classifier**:
  `P(C|X) = \frac{\prod_{i=1}^{n} P(X_i|C)}{\sum_{C'} \prod_{i=1}^{n} P(X_i|C')}`, where `n` is the number of features.

### Revision Notes

* Use the Naïve Bayes assumption to simplify the calculation of conditional probabilities.
* Calculate the probability of each feature given the class using the conditional probability distribution.
* Normalize the probabilities using the prior probability and the marginal probability of the feature.
* Compare the posterior probabilities of each class to make predictions.

### Important Terms

* **Continuous attributes**: Features with a continuous range of values.
* **Multi-class classification**: Classification problems with more than two classes.
* **Naïve Bayes algorithm**: A probabilistic classifier based on Bayes' theorem, suitable for continuous attributes and multi-class classification problems.
```
