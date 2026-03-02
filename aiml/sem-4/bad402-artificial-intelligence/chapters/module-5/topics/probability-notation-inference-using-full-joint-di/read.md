# **Probability Notation, Inference using Full Joint Distributions, Independence, Baye’s Rule and its use**

## **Probability Notation**

Probability notation is used to express the probability of an event occurring. It is denoted by the symbol P(A) and represents the probability of event A.

- **Event**: A set of outcomes that can occur.
- **Random Variable**: A variable that can take on different values based on the occurrence of an event.
- **Sample Space**: The set of all possible outcomes of an experiment.
- **Event Space**: A set of events that can occur.

## **Inference using Full Joint Distributions**

A joint distribution is a probability distribution that describes the probability of events A and B occurring together. It is denoted by the symbol P(A, B) or P(A ∩ B).

- **Conditional Probability**: The probability of event A occurring given that event B has occurred. It is denoted by the symbol P(A|B) or P(A ∩ B)/P(B).
- **Independent Events**: Events A and B are independent if the occurrence of one event does not affect the probability of the other event. It is denoted by the symbol P(A ∩ B) = P(A)P(B).

## **Independence**

Two events A and B are independent if the occurrence of one event does not affect the probability of the other event. This can be checked using the following conditions:

- **Mutual Independence**: P(A ∩ B) = P(A)P(B) for all possible values of A and B.
- **Mutual Exclusive**: P(A ∩ B) = 0 for all possible values of A and B.

## **Baye’s Rule**

Baye’s rule is a mathematical formula used to update the probability of an event A given new evidence B. It is denoted by the symbol P(A|B) and is calculated as:

- **P(A|B) = P(B|A) \* P(A) / P(B)**

where:

- **P(B|A)**: The probability of event B given event A.
- **P(A)**: The prior probability of event A.
- **P(B)**: The likelihood of event B.

## **Example**

Suppose we have a coin toss experiment where the heads and tails are equally likely to occur.

- **Event A**: Getting heads.
- **Event B**: Getting tails.
- **P(A)**: 0.5
- **P(B)**: 0.5

We want to update the probability of event A given that event B has occurred.

- **P(B|A)**: 1 (since getting tails given heads is certain)
- **P(A|B)** = P(B|A) \* P(A) / P(B) = 1 \* 0.5 / 0.5 = 0.5

Therefore, the probability of event A given that event B has occurred is 0.5.

## **Conclusion**

Probability notation, inference using full joint distributions, independence, Baye’s rule, and its use are essential concepts in artificial intelligence. By understanding these concepts, we can quantify uncertainty and make informed decisions under uncertainty.
