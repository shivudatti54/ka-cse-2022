# Classification Using Bayes Model

### Overview

- Bayes' theorem is a mathematical formula for updating the probability of a hypothesis as more evidence or information becomes available.
- Classification using Bayes model is a type of supervised learning where the goal is to predict a class label for a new instance based on its features.

### Key Concepts

- **Bayes' Theorem**:
  ```r
  P(H|E) = P(E|H) \* P(H) / P(E)
  ```

````
  Where:
  - `P(H|E)` is the posterior probability of the hypothesis given the evidence
  - `P(E|H)` is the likelihood of the evidence given the hypothesis
  - `P(H)` is the prior probability of the hypothesis
  - `P(E)` is the prior probability of the evidence

* **Conditional Probability**:
  ```r
P(A|B) = P(A \* B) / P(B)
````

Where:

- `P(A|B)` is the conditional probability of event A given event B
- `P(A \* B)` is the joint probability of events A and B
- `P(B)` is the probability of event B

* **Naive Bayes**:
  A simplified version of Bayes' theorem that assumes independence between features.
  ```r
  P(c|x) = P(x|c) \* P(c) / P(x)
  ```

```
  Where:
  - `P(c|x)` is the posterior probability of class c given feature x
  - `P(x|c)` is the likelihood of feature x given class c
  - `P(c)` is the prior probability of class c
  - `P(x)` is the prior probability of feature x

### Important Formulas and Theorems

* **Bayes' Theorem**: `P(H|E) = P(E|H) \* P(H) / P(E)`
* **Conditional Probability**: `P(A|B) = P(A \* B) / P(B)`
* **Naive Bayes**: `P(c|x) = P(x|c) \* P(c) / P(x)`

### Definitions

* **Hypothesis**: A variable representing a possible explanation for a phenomenon
* **Evidence**: A variable representing the data used to test the hypothesis
* **Prior Probability**: The probability of an event before new evidence is available
* **Posterior Probability**: The probability of an event after new evidence is available
```
