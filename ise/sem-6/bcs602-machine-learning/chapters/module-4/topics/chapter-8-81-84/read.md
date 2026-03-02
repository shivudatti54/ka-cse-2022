# **Chapter-8 (8.1-8.4): Bayesian Learning**

### 8.1 Introduction to Bayesian Learning

Bayesian learning is a type of machine learning that uses Bayes' theorem to update the probability of a hypothesis based on new data. This approach is based on the idea of conditional probability, where the probability of a hypothesis given new data is calculated by multiplying the prior probability of the hypothesis by the likelihood of the data given the hypothesis.

**Definition:** Bayesian learning is a probabilistic approach to machine learning that uses Bayes' theorem to update the probability of a hypothesis based on new data.

**Key Concepts:**

- **Prior probability:** The probability of a hypothesis before new data is observed.
- **Likelihood:** The probability of new data given a hypothesis.
- **Posterior probability:** The probability of a hypothesis after new data is observed.

### 8.2 Fundamentals of Bayes Theorem

Bayes' theorem is a mathematical formula that calculates the posterior probability of a hypothesis given new data. The formula is as follows:

P(H|D) = P(D|H) \* P(H) / P(D)

where:

- P(H|D) is the posterior probability of the hypothesis given the data.
- P(D|H) is the likelihood of the data given the hypothesis.
- P(H) is the prior probability of the hypothesis.
- P(D) is the probability of the data.

**Explanation:** Bayes' theorem updates the prior probability of a hypothesis based on the likelihood of the data given the hypothesis.

**Example:** Suppose we want to determine whether a person is likely to have a disease based on their symptoms. We have a prior probability of 0.1 that the person has the disease, and a likelihood of 0.8 that the symptoms are present given that the person has the disease. Using Bayes' theorem, we can calculate the posterior probability of the person having the disease as follows:

P(Disease|Symptoms) = P(Symptoms|Disease) \* P(Disease) / P(Symptoms)
= 0.8 \* 0.1 / (0.8 \* 0.1 + 0.2 \* 0.9)
= 0.36 / (0.08 + 0.18)
= 0.36 / 0.26
= 0.138

In this example, the posterior probability of the person having the disease is 13.8%.

### 8.3 Bayesian Networks

A Bayesian network is a probabilistic graphical model that represents the relationships between variables. Each node in the network represents a variable, and each edge represents the conditional dependency between the variables.

**Definition:** A Bayesian network is a probabilistic graphical model that represents the relationships between variables.

**Key Concepts:**

- **Nodes:** Variables in the network.
- **Edges:** Conditional dependencies between nodes.

### 8.4 Applications of Bayesian Learning

Bayesian learning has many applications in machine learning, including:

- **Classification:** Bayesian classification is a type of supervised learning where the goal is to predict a class label based on a set of features.
- **Regression:** Bayesian regression is a type of supervised learning where the goal is to predict a continuous value based on a set of features.
- **Clustering:** Bayesian clustering is a type of unsupervised learning where the goal is to group similar data points into clusters.

**Example:** Suppose we want to perform classification on a set of images. We can use Bayesian learning to train a classifier that assigns a class label to each image based on its features. The classifier would use Bayes' theorem to update the probability of each class label based on the features of each image.
