# Joint Probability Distribution for Two Discrete Random Variables

### Key Points

- A joint probability distribution for two discrete random variables $X$ and $Y$ is a function that assigns a probability to each possible ordered pair $(x, y)$.
- The probability distribution of $X$ and $Y$ is a 2-dimensional table or a set of equations that describe the probabilities of all possible outcomes.
- We can define a joint probability distribution using the following formula:
  - $P(X = x, Y = y) = P(X = x) \cdot P(Y = y)$

### Important Formulas

- The probability of a single event $X = x$ is given by:
  - $P(X = x) = \sum_{y} P(X = x, Y = y)$
- The marginal probability of $X$ is given by:
  - $P(X = x) = \sum_{y} P(X = x, Y = y)$
- The marginal probability of $Y$ is given by:
  - $P(Y = y) = \sum_{x} P(X = x, Y = y)$
- The joint probability distribution can be represented using a 2-dimensional table:
  - | $X = x_1$ | $X = x_2$ | ... | $X = x_n$ |
  - | $P(X = x_1, Y = y_1)$ | $P(X = x_1, Y = y_2)$ | ... | $P(X = x_1, Y = y_m)$ |
  - | $P(X = x_2, Y = y_1)$ | $P(X = x_2, Y = y_2)$ | ... | $P(X = x_2, Y = y_m)$ |
  - | $...$ | $...$ | ... | $...$ |
  - | $P(X = x_n, Y = y_1)$ | $P(X = x_n, Y = y_2)$ | ... | $P(X = x_n, Y = y_m)$ |

### Important Definitions

- **Conditional probability**: The probability of an event $A$ given that event $B$ has occurred. It is denoted by $P(A|B)$.
- **Independence**: Two events $A$ and $B$ are independent if the occurrence of one does not affect the probability of the other.

### Important Theorems

- **Theorem of Total Probability**: For two discrete random variables $X$ and $Y$, the probability of an event $A$ can be expressed as:
  - $P(A) = \sum_{x} \sum_{y} P(X = x, Y = y) \cdot I_{(x, y) \in A}$
  - where $I_{(x, y) \in A}$ is the indicator function that equals 1 if $(x, y) \in A$ and 0 otherwise.
