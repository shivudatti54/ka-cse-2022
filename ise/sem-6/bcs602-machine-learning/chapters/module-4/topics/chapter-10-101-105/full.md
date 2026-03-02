# **Chapter-10: Bayesian Learning**

## **10.1: Introduction to Bayesian Learning**

Bayesian learning is a type of machine learning that uses Bayes' theorem to update the probability of a hypothesis as more evidence or data becomes available. Bayes' theorem is a mathematical formula that describes the probability of a hypothesis given some evidence. It is a powerful tool for making predictions and decisions in a wide range of fields, including medicine, finance, and computer science.

### Historical Context

Bayes' theorem was first introduced by Thomas Bayes in 1763. However, it wasn't until the 20th century that the theorem gained widespread use in machine learning. The development of Bayesian learning is attributed to several researchers, including Richard McElree, Geoffrey Hinton, and Yann LeCun. They recognized the power of Bayes' theorem for making predictions and decisions in machine learning.

### Fundamentals of Bayes Theorem

Bayes' theorem is a mathematical formula that describes the probability of a hypothesis given some evidence. It is defined as follows:

P(H|E) = P(E|H) \* P(H) / P(E)

Where:

- P(H|E) is the probability of the hypothesis given the evidence
- P(E|H) is the probability of the evidence given the hypothesis
- P(H) is the prior probability of the hypothesis
- P(E) is the probability of the evidence

### Intuition

Bayes' theorem can be thought of as a way of updating the probability of a hypothesis as more evidence becomes available. The theorem states that the probability of a hypothesis given some evidence is equal to the probability of the evidence given the hypothesis, times the prior probability of the hypothesis, divided by the probability of the evidence.

### Example

Suppose we want to determine whether a person is likely to have a certain disease given some test results. We have a prior probability of 0.1 that the person has the disease, and a probability of 0.9 that the person does not have the disease. We also have a probability of 0.8 that the test results will be positive given that the person has the disease, and a probability of 0.2 that the test results will be positive given that the person does not have the disease.

Using Bayes' theorem, we can update the probability of the person having the disease given the test results as follows:

P(Disease|Test Results) = P(Test Results|Disease) \* P(Disease) / P(Test Results)
= 0.8 \* 0.1 / (0.8 \* 0.1 + 0.2 \* 0.9)
= 0.36

This means that the probability of the person having the disease given the test results is 0.36, or 36%.

### Application

Bayesian learning has many practical applications in machine learning, including:

- **Classification**: Bayesian learning can be used for classification tasks, such as spam vs. non-spam emails, or cancer vs. non-cancerous cells.
- **Regression**: Bayesian learning can be used for regression tasks, such as predicting house prices or predicting stock prices.
- **Clustering**: Bayesian learning can be used for clustering tasks, such as grouping customers by their demographic characteristics.

## **10.2: Bayesian Networks**

A Bayesian network is a type of probabilistic graphical model that represents the relationships between variables. It is a directed acyclic graph (DAG) that consists of nodes and edges.

### Nodes

A node in a Bayesian network represents a variable. Each node can have a probability distribution associated with it.

### Edges

An edge in a Bayesian network represents a conditional probability relationship between two variables. The edge from node A to node B represents the probability of B given A.

### Example

Suppose we want to model the relationship between a person's age, income, and likelihood of owning a house. We can create a Bayesian network with three nodes: Age, Income, and Owns House.

The edges in the network can be defined as follows:

- Age -> Income: The probability of a person having a higher income given that they are older.
- Income -> Owns House: The probability of a person owning a house given that they have a higher income.
- Age -> Owns House: The probability of a person owning a house given that they are older.

The probability distributions for each node can be defined as follows:

- Age: Uniform distribution from 20 to 80 years old.
- Income: Normal distribution with mean 50,000 and standard deviation 10,000.
- Owns House: Bernoulli distribution with parameter 0.5.

## **10.3: Conditional Probability**

Conditional probability is the probability of an event given that another event has occurred. It is a fundamental concept in Bayesian learning.

### Formula

The formula for conditional probability is:

P(A|B) = P(A and B) / P(B)

Where:

- P(A|B) is the probability of A given B
- P(A and B) is the probability of A and B
- P(B) is the probability of B

### Example

Suppose we want to determine the probability of a person having a certain disease given that they have been tested positive for the disease. We have a probability of 0.9 that the person has the disease given that they have been tested positive, and a probability of 0.1 that the person has the disease given that they have not been tested positive.

Using the formula for conditional probability, we can calculate the probability of the person having the disease given that they have been tested positive as follows:

P(Disease|Test Results Positive) = P(Disease and Test Results Positive) / P(Test Results Positive)
= 0.9 / (0.9 \* 0.9 + 0.1 \* 0.1)
= 0.9

This means that the probability of the person having the disease given that they have been tested positive is 0.9, or 90%.

## **10.4: Bayes' Theorem for Discrete Variables**

Bayes' theorem can be applied to discrete variables using the following formula:

P(H|E) = P(E|H) \* P(H) / P(E)

Where:

- P(H|E) is the probability of the hypothesis given the evidence
- P(E|H) is the probability of the evidence given the hypothesis
- P(H) is the prior probability of the hypothesis
- P(E) is the probability of the evidence

### Example

Suppose we want to determine whether a person is likely to have a certain disease given some test results. We have a prior probability of 0.1 that the person has the disease, and a probability of 0.8 that the person does not have the disease. We also have a probability of 0.9 that the test results will be positive given that the person has the disease, and a probability of 0.1 that the test results will be positive given that the person does not have the disease.

Using Bayes' theorem, we can update the probability of the person having the disease given the test results as follows:

P(Disease|Test Results) = P(Test Results|Disease) \* P(Disease) / P(Test Results)
= 0.9 \* 0.1 / (0.9 \* 0.1 + 0.1 \* 0.9)
= 0.1

This means that the probability of the person having the disease given the test results is 0.1, or 10%.

## **10.5: Bayesian Learning in Practice**

Bayesian learning has many practical applications in machine learning, including:

- **Image classification**: Bayesian learning can be used for image classification tasks, such as recognizing objects in images.
- **Speech recognition**: Bayesian learning can be used for speech recognition tasks, such as recognizing spoken words.
- **Natural language processing**: Bayesian learning can be used for natural language processing tasks, such as sentiment analysis.

## **Further Reading**

- **Bayes' theorem**: Thomas Bayes, "An Essay Towards Solving a Problem in the Doctrine of Chances", 1763.
- **Bayesian networks**: Judea Pearl, "Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference", 1988.
- **Bayesian learning**: David M. Blei, "Probabilistic Models of Text and Image"
