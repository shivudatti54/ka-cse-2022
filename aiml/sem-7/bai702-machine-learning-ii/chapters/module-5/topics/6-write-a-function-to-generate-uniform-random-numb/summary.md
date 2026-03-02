# **Uniform Random Number Generation**

## **Key Points**

- A uniform random variable $X$ is said to be uniformly distributed on the interval $[a, b]$ if its probability density function (PDF) is given by:
  \[ f(x) = \begin{cases} \frac{1}{b-a} & \text{if } a \leq x \leq b \\ 0 & \text{otherwise} \end{cases} \]
- The cumulative distribution function (CDF) of $X$ is given by:
  \[ F(x) = \begin{cases} 0 & \text{if } x < a \\ \frac{x-a}{b-a} & \text{if } a \leq x \leq b \\ 1 & \text{if } x > b \end{cases} \]
- To generate a uniform random variable $X$ on the interval $[a, b]$, we can use the inverse transform sampling method:
  \[ X = F^{-1}(U) \]
  where $U$ is a uniform random variable on the interval $[0, 1]$.

## **Formulas and Definitions**

- Probability density function (PDF): $f(x)$
- Cumulative distribution function (CDF): $F(x)$
- Uniform random variable: $X$ with PDF $f(x)$
- Inverse transform sampling method: $X = F^{-1}(U)$

## **Theorem**

- The inverse transform sampling method is a valid method for generating uniform random variables.

## **Implementation**

- We can use the following Python function to generate a uniform random variable $X$ on the interval $[a, b]$:

```python
import numpy as np

def uniform_random_number(a, b):
    u = np.random.uniform(0, 1)
    x = a + (b-a) * u
    return x
```

This function uses the inverse transform sampling method to generate a uniform random variable $X$ on the interval $[a, b]$.
