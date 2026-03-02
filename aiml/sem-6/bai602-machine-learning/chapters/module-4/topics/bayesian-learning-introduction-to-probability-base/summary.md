# **Bayesian Learning Revision Notes**

### Introduction to Probability-based Learning

- **Probability Theory**: Study of chance events and their likelihood
- **Random Variables**: Variables that can take on different values with varying probabilities
- **Probability Distribution**: Function that describes the probability of each possible value of a random variable

### Fundamentals of Bayes Theorem

- **Bayes' Theorem**: Formula for updating the probability of a hypothesis based on new evidence
- **Bayes' Theorem Formula**:
  \[ P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)} \]
- **Definition**: A measure of the probability of a hypothesis given some evidence

### Classification Using Bayes Model

- **Bayes Classifier**: A machine learning model that uses Bayes' Theorem to classify new instances
- **Assumptions**:
  - Instances are independent and identically distributed
  - Conditional independence between features given the class label

### Naïve Bayes Algorithm

- **Naïve Bayes Assumption**: Conditional independence between features given the class label
- **Naïve Bayes Formula**:
  \[ P(c|X) = \frac{P(X|c) \cdot P(c)}{\sum P(X|c') \cdot P(c')} \]
- **Definition**: A simplified version of Bayes' Theorem that assumes independence between features

**Important Formulas and Definitions**

- **Probability**: A measure of the likelihood of an event occurring
- **Conditional Probability**: The probability of an event occurring given that another event has occurred
- **Independence**: A property of random variables where the probability distribution of one variable does not depend on the value of another variable

**Theorems**

- **Bayes' Theorem**: A fundamental theorem in probability theory that updates the probability of a hypothesis based on new evidence
- **Naïve Bayes Assumption**: A simplifying assumption that allows for efficient computation of the Bayes classifier
