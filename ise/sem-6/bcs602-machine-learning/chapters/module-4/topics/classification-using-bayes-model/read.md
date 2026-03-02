# Classification Using Bayes Model

### Introduction

Bayes' theorem is a mathematical formula used to update the probability of a hypothesis as more evidence or information becomes available. In the context of machine learning, Bayes' theorem can be applied to classify data into different classes based on the probability of each class given the observed features. This topic will delve into the concepts of Bayes' theorem, its application in classification, and the underlying mathematics.

### Bayes' Theorem

Bayes' theorem is a probabilistic formula that describes the probability of an event occurring given some new evidence. The formula is as follows:

P(H|E) = P(E|H) \* P(H) / P(E)

Where:

- P(H|E) is the probability of the hypothesis (class) H given the evidence E
- P(E|H) is the probability of the evidence E given the hypothesis H
- P(H) is the prior probability of the hypothesis H
- P(E) is the probability of the evidence E

### Classification Using Bayes Model

In classification using Bayes model, the goal is to assign a new data point to one of the predefined classes based on the probability of each class given the observed features. The Bayes decision rule is as follows:

- For each class H, calculate the posterior probability P(H|E) using Bayes' theorem
- Assign the new data point to the class with the highest posterior probability P(H|E)

### Key Concepts

- **Prior Probability**: The probability of a class before observing any evidence
- **Likelihood**: The probability of observing the evidence given a class
- **Posterior Probability**: The probability of a class given the observed evidence
- **Bayes' Theorem**: A mathematical formula to update the probability of a hypothesis as more evidence becomes available

### Bayes' Theorem for Classification

Here is an example of how Bayes' theorem can be applied to classify a new data point into one of the two classes:

Suppose we have a dataset with two classes: spam and non-spam emails. We want to classify a new email as either spam or non-spam based on its features such as subject, body, and sender.

Let's denote the prior probabilities of each class as follows:

- P(spam) = 0.7 (prior probability of a spam email)
- P(non-spam) = 0.3 (prior probability of a non-spam email)

We also have the following likelihoods:

- P(subject=funny|spam) = 0.8 (probability of a funny subject given a spam email)
- P(subject=funny|non-spam) = 0.2 (probability of a funny subject given a non-spam email)
- P(sender=new|spam) = 0.9 (probability of a new sender given a spam email)
- P(sender=new|non-spam) = 0.1 (probability of a new sender given a non-spam email)

We want to classify a new email with the following features:

- Subject: funny
- Sender: new

Using Bayes' theorem, we can calculate the posterior probabilities as follows:

- P(spam|email) = P(subject=funny|spam) \* P(sender=new|spam) \* P(spam) / (P(subject=funny|spam) \* P(sender=new|spam) \* P(spam) + P(subject=funny|non-spam) \* P(sender=new|non-spam) \* P(non-spam))
- P(non-spam|email) = P(subject=funny|non-spam) \* P(sender=new|non-spam) \* P(non-spam) / (P(subject=funny|spam) \* P(sender=new|spam) \* P(spam) + P(subject=funny|non-spam) \* P(sender=new|non-spam) \* P(non-spam))

Based on the posterior probabilities, we can assign the new email to either the spam or non-spam class.

### Conclusion

Bayes' theorem is a powerful tool in machine learning for classification. By applying Bayes' theorem, we can update the probability of a hypothesis as more evidence becomes available, leading to more accurate classification results. The key concepts of prior probability, likelihood, posterior probability, and Bayes' theorem are essential to understanding how Bayes model works.

### Code Implementation

Here is an example code implementation in Python to classify a new email into either spam or non-spam:

```python
import numpy as np

# Define the prior probabilities
prior_spam = 0.7
prior_non_spam = 0.3

# Define the likelihoods
def likelihood_spam(subject, sender):
    return 0.8 if subject == 'funny' else 0.2
def likelihood_non_spam(subject, sender):
    return 0.2 if subject == 'funny' else 0.1

# Define the Bayes' theorem function
def bayes_theorem(email, spam=True):
    subject = email['subject']
    sender = email['sender']
    likelihood = likelihood_spam(subject, sender)
    prior = prior_spam if spam else prior_non_spam
    posterior = likelihood * prior / (likelihood * prior + (1-likelihood) * (1-prior))
    return posterior

# Define the email features
email = {'subject': 'funny', 'sender': 'new'}

# Calculate the posterior probabilities
posterior_spam = bayes_theorem(email, spam=True)
posterior_non_spam = bayes_theorem(email, spam=False)

# Assign the email to either spam or non-spam class
if posterior_spam > posterior_non_spam:
    print('Email is spam')
else:
    print('Email is non-spam')
```

Note: This is a simplified example and may not be representative of real-world spam classification scenarios.
