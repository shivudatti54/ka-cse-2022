# Chapter-8 (8.1-8.4)

## Bayesian Learning: Introduction to Probability-based Learning

### 8.1 Introduction to Probability-based Learning

Probability-based learning is a type of machine learning that uses probability theory to make predictions or decisions. It is based on the idea that the likelihood of an event occurring is proportional to the number of favorable outcomes divided by the total number of possible outcomes.

**Key Concepts:**

- **Probability**: A measure of the likelihood of an event occurring.
- **Random Variable**: A variable whose value is determined by chance.
- **Sample Space**: The set of all possible outcomes of a random experiment.

### 8.2 Fundamentals of Bayes Theorem

Bayes Theorem is a mathematical formula that describes the probability of an event occurring given some prior knowledge. It is a fundamental concept in probability-based learning and is used in many machine learning algorithms.

**Bayes Theorem Formula:**

P(A|B) = P(B|A) \* P(A) / P(B)

Where:

- P(A|B) is the probability of event A occurring given event B
- P(B|A) is the probability of event B occurring given event A
- P(A) is the prior probability of event A
- P(B) is the prior probability of event B

**Example:**

Suppose we want to determine the probability that a person has a disease given that they have symptoms. We know that the prior probability of having the disease is 0.01, and the probability of having symptoms given that we have the disease is 0.8. We also know that the probability of having symptoms given that we do not have the disease is 0.2.

Using Bayes Theorem, we can calculate the probability of having the disease given that we have symptoms:

P(Disease|Symptoms) = P(Symptoms|Disease) \* P(Disease) / P(Symptoms)
= 0.8 \* 0.01 / (0.8 \* 0.01 + 0.2 \* 0.99)
= 0.4 / (0.08 + 0.198)
= 0.4 / 0.298
= 0.135

Therefore, the probability of having the disease given that we have symptoms is approximately 13.5%.

### 8.3 Conditional Probability

Conditional probability is the probability of an event occurring given that another event has occurred. It is a key concept in probability-based learning and is used in many machine learning algorithms.

**Definition:**

P(A|B) = P(A and B) / P(B)

**Example:**

Suppose we want to determine the probability that it will rain given that the weather forecast predicts a 30% chance of rain. Using conditional probability, we can calculate the probability of rain as follows:

P(Rain|Forecast) = P(Rain and Forecast) / P(Forecast)
= 0.3 / 0.3
= 0.3

Therefore, the probability of rain given that the forecast predicts a 30% chance of rain is 30%.

### 8.4 Independence of Events

Two events are independent if the occurrence of one event does not affect the probability of the other event. Independence is an important concept in probability-based learning and is used in many machine learning algorithms.

**Definition:**

Two events A and B are independent if P(A and B) = P(A) \* P(B)

**Example:**

Suppose we want to determine the probability that it will rain and that the temperature will be warm. If the occurrence of rain does not affect the probability of the temperature being warm, then the two events are independent. Using independence, we can calculate the probability of rain and warm temperature as follows:

P(Rain and Warm Temperature) = P(Rain) \* P(Warm Temperature)
= 0.3 \* 0.4
= 0.12

Therefore, the probability of rain and warm temperature is 12%.
