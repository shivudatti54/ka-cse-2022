# **Probability Mass and Density Functions**

## **Introduction**

Probability mass and density functions are mathematical tools used to model random variables and describe the probability distribution of a random experiment. Understanding these concepts is crucial in probability theory and has numerous applications in computer science, statistics, and engineering.

## **Probability Mass Functions**

A probability mass function (PMF) is a function that assigns a probability to each possible outcome of a discrete random variable. It is used to model the probability distribution of a random variable that can take on only a finite number of values.

**Definition:**

- A probability mass function (PMF) $P$ is defined as:

* $P(X = x) = p_x$ for all possible values $x$ in the sample space $X$
* $p_x \geq 0$ for all $x$ in $X$
* $\sum_{x \in X} p_x = 1$

**Examples:**

- The PMF of a fair six-sided coin toss is:

* $P(Head) = 1/2$
* $P(Tail) = 1/2$

- The PMF of a random variable that can take on values 1, 2, or 3 with probabilities 1/3, 1/3, and 1/3, respectively, is:

* $P(X = 1) = 1/3$
* $P(X = 2) = 1/3$
* $P(X = 3) = 1/3$

**Key Concepts:**

- The PMF is a function that assigns a probability to each possible outcome of a discrete random variable.
- The PMF must satisfy the following conditions:

* $p_x \geq 0$ for all $x$ in $X$
* $\sum_{x \in X} p_x = 1$

## **Probability Density Functions**

A probability density function (PDF) is a function that assigns a probability density to each possible value of a continuous random variable. It is used to model the probability distribution of a random variable that can take on any value within a continuous range.

**Definition:**

- A probability density function (PDF) $f$ is defined as:

* $f(x) = f_x$ for all $x$ in the sample space $X$
* $f_x \geq 0$ for all $x$ in $X$
* $\int_{-\infty}^{\infty} f(x) dx = 1$

**Examples:**

- The PDF of a normal distribution with mean $\mu$ and variance $\sigma^2$ is:

* $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

- The PDF of a uniform distribution on the interval $[a, b]$ is:

* $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$

**Key Concepts:**

- The PDF is a function that assigns a probability density to each possible value of a continuous random variable.
- The PDF must satisfy the following conditions:

* $f_x \geq 0$ for all $x$ in $X$
* $\int_{-\infty}^{\infty} f(x) dx = 1$

## **Relationship Between PMF and PDF**

While PMFs and PDFs are used to model different types of random variables, they are related in the sense that the probability mass function can be viewed as a discrete version of the probability density function.

- The PMF of a discrete random variable can be viewed as a PDF with a mass at each point.
- The PDF of a continuous random variable can be viewed as a PMF with a mass at each point.

## **Conclusion**

Probability mass and density functions are fundamental concepts in probability theory that are used to model random variables and describe their probability distributions. Understanding these concepts is crucial in probability theory and has numerous applications in computer science, statistics, and engineering.
