# Bayesian Learning: Introduction to Probability-based Learning

===========================================================

## 10.9-10.11: Bayesian Inference and Decision Theory

### Introduction

Bayesian learning is a probability-based approach to machine learning that involves updating probabilities based on new data. In this section, we will cover the basics of Bayesian inference and decision theory, including Bayes' theorem and decision theory.

### Bayes' Theorem

Bayes' theorem is a mathematical formula that describes the probability of a hypothesis given new data. It is a fundamental concept in Bayesian learning and is used to update probabilities based on new information.

**Bayes' Theorem Formula**

P(H|D) = P(D|H) \* P(H) / P(D)

Where:

- P(H|D) is the probability of hypothesis H given data D
- P(D|H) is the probability of data D given hypothesis H
- P(H) is the prior probability of hypothesis H
- P(D) is the likelihood of data D

**Example**

Suppose we want to determine whether a person has a disease based on a test result. The prior probability of the person having the disease is 0.1, the probability of a positive test result given the disease is 0.9, and the probability of a positive test result given no disease is 0.05.

Using Bayes' theorem, we can calculate the probability of the person having the disease given the test result as follows:

P(Disease|Test Result) = P(Test Result|Disease) \* P(Disease) / P(Test Result)
= 0.9 \* 0.1 / 0.55
= 0.1636

### Decision Theory

Decision theory is a branch of mathematics that deals with making decisions based on uncertainty. In the context of Bayesian learning, decision theory is used to determine the best course of action based on the probability of different outcomes.

**Expected Utility**

The expected utility of an action is calculated by multiplying the probability of each outcome by its utility and summing the results.

E(U) = ∑[P(i) \* U(i)]

Where:

- E(U) is the expected utility
- P(i) is the probability of outcome i
- U(i) is the utility of outcome i

**Example**

Suppose we want to determine whether to invest in a stock based on its expected return and risk. The expected return of the stock is 0.1, and the expected return of a risk-free investment is 0.05. The probability of the stock returning more than its expected return is 0.2, and the probability of the stock returning less than its expected return is 0.8.

Using decision theory, we can calculate the expected utility of investing in the stock as follows:

E(U) = P(Return > 0.1) \* U(Return > 0.1) + P(Return < 0.1) \* U(Return < 0.1)
= 0.2 \* 0.1 + 0.8 \* -0.05
= -0.045

Since the expected utility of investing in the stock is less than the expected utility of the risk-free investment, we should choose the risk-free investment.

### Key Concepts

- Bayes' theorem: a mathematical formula for updating probabilities based on new data
- Decision theory: a branch of mathematics that deals with making decisions based on uncertainty
- Expected utility: the calculation of the expected outcome of an action based on its probabilities and utilities
- Prior probability: the probability of a hypothesis before new data is considered
- Likelihood: the probability of data given a hypothesis
- Posterior probability: the probability of a hypothesis after new data is considered
