# **Probability Notation, Inference using Full Joint Distributions, Independence, Baye’s Rule and its use**

## **1. Introduction to Probability**

Probability is a branch of mathematics that deals with the study of chance events and their likelihood of occurrence. In the context of artificial intelligence, probability is used to quantify uncertainty and make predictions about future events.

## **Probability Notation**

Probability notation is used to express the likelihood of an event. It is typically expressed as a value between 0 and 1, where:

- 0 represents an impossible event (0% chance of occurrence)
- 1 represents a certain event (100% chance of occurrence)
- A value between 0 and 1 represents a possible event (chance of occurrence between 0% and 100%)

Common probability notation includes:

- P(A): The probability of event A occurring
- P(A|B): The probability of event A occurring given that event B has occurred
- P(A, B): The joint probability of events A and B occurring

Example:

```markdown
P(Rain) = 0.5 (50% chance of rain)
P(Sunshine|No Rain) = 0.8 (80% chance of sunshine given no rain)
P(Rain, Sunshine) = 0.2 (20% chance of both rain and sunshine occurring)
```

## **2. Inference using Full Joint Distributions**

A full joint distribution is a probability distribution that describes the joint probability of multiple events. It is typically expressed as a table or a mathematical formula that describes the probability of each possible combination of events.

Example:

```markdown
|         | Sunny | Cloudy |
| ------- | ----- | ------ |
| Rain    | 0.2   | 0.3    |
| No Rain | 0.7   | 0.4    |
```

In this example, the joint probability of rain and sunshine is 0.2, while the joint probability of no rain and sunshine is 0.7.

## **3. Independence**

Two events are considered independent if the occurrence of one event does not affect the probability of the other event. Mathematically, independence can be expressed as:

P(A|B) = P(A)

In other words, if event A is independent of event B, then the probability of A occurring given that B has occurred is equal to the probability of A occurring in general.

Example:

```markdown
P(Rain|Sunny) = P(Rain) = 0.2 (independent events)
```

## **4. Baye’s Rule**

Baye's rule is a mathematical formula that describes the probability of an event A occurring given evidence B. It is expressed as:

P(A|B) = P(B|A) \* P(A) / P(B)

where:

- P(B|A) is the probability of B occurring given that A has occurred
- P(A) is the probability of A occurring in general
- P(B) is the probability of B occurring in general

Example:

```markdown
P(Rain|Sunny) = P(Sunny|Rain) \* P(Rain) / P(Sunny)
P(Sunny) = 0.6 (probability of sunshine)
P(Rain) = 0.4 (probability of rain)
P(Sunny|Rain) = 0.8 (probability of sunshine given rain)
```

Using Baye's rule, we can calculate the probability of rain given sunshine:

P(Rain|Sunny) = 0.8 \* 0.4 / 0.6 = 0.5333

This means that the probability of rain given sunshine is approximately 53.33%.

## **5. Use of Baye’s Rule**

Baye's rule is commonly used in decision-making and inference problems in artificial intelligence. It allows us to update our beliefs about an event based on new evidence.

Example:

```markdown
Suppose we have a system that can detect rain or shine using weather sensors. We want to update our belief about the probability of rain given that the system detects sunshine.

Initial Belief:
P(Rain) = 0.4

New Evidence:
P(Sunshine) = 0.6

Updated Belief:
P(Rain|Sunshine) = P(Sunshine|Rain) \* P(Rain) / P(Sunshine)
P(Sunshine|Rain) = 0.8
P(Sunshine) = 0.6

P(Rain|Sunshine) = 0.8 \* 0.4 / 0.6 = 0.5333
```

Using Baye's rule, we have updated our belief about the probability of rain given sunshine.
