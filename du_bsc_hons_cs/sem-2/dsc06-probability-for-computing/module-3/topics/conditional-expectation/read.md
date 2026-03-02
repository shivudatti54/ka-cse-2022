# Conditional Expectation

## Introduction

Conditional expectation is one of the most powerful and elegant concepts in probability theory, serving as a cornerstone for advanced topics in statistics, machine learning, and stochastic processes. In the context of computing, conditional expectation plays a vital role in algorithm analysis, random algorithms, queuing theory, and Bayesian machine learning. 

When we compute the expected value of a random variable, we are essentially summarizing the entire distribution with a single number. However, in many real-world computing scenarios, we have partial information about the outcome of an experiment. For instance, when analyzing the running time of a randomized algorithm, we might want to know the expected running time given that a particular branch was taken, or when processing network traffic, we might need to estimate delay times given that the buffer is not empty. Conditional expectation provides the mathematical framework for computing expectations under such partial information.

The concept of conditional expectation extends the notion of conditional probability to expected values, allowing us to refine our predictions when we acquire new information. This topic builds directly on your understanding of conditional probability and expectation, which are fundamental to the probability curriculum at Delhi University. Mastery of conditional expectation is essential not only for solving examination problems but also for understanding more advanced topics like Markov chains, martingales, and Bayesian inference.

## Key Concepts

### Definition of Conditional Expectation

Given two discrete random variables X and Y, the conditional expectation of X given Y = y is defined as the expected value of X computed with respect to the conditional distribution of X given Y = y. Mathematically, for discrete random variables:

**E[X | Y = y] = Σₓ x · P(X = x | Y = y)**

For continuous random variables with joint density f(x, y):

**E[X | Y = y] = ∫₋∞^∞ x · f_X|Y(x|y) dx**

where f_X|Y(x|y) = f(x,y)/f_Y(y) is the conditional density of X given Y = y.

### The Law of Total Expectation

One of the most important theorems in probability, the Law of Total Expectation (also called the Tower Rule), states:

**E[E[X | Y]] = E[X]**

This theorem implies that if we take the expectation of the conditional expectation of X given Y, we recover the unconditional expectation of X. This is incredibly useful because it allows us to break down complex expectations into simpler conditional ones. In computing applications, this is often used to compute expected values by conditioning on different scenarios or states of a system.

### Properties of Conditional Expectation

1. **Linearity**: E[aX + bY | Z] = aE[X | Z] + bE[Y | Z] for constants a, b.

2. **Taking out what is known**: If g(Z) is a function of Z, then E[g(Z)X | Z] = g(Z) · E[X | Z].

3. **Independence**: If X is independent of Y, then E[X | Y] = E[X]. Knowing Y provides no additional information about X.

4. **Iterated Expectation**: E[E[X | Y, Z] | Y] = E[X | Y]. This is the "smoothing" property.

### Conditional Expectation as a Random Variable

An important perspective often overlooked in introductory courses is that E[X | Y] is itself a random variable. Since the conditional expectation depends on the value of Y, which is random, E[X | Y] is a function of Y. We can write:

**g(Y) = E[X | Y]**

This means the conditional expectation maps each possible outcome of Y to the corresponding conditional expectation of X. This perspective is crucial when working with stochastic processes and random algorithms.

### Variance and Conditional Expectation

The law of total variance decomposes the total variance of X into components attributable to different sources of randomness:

**Var(X) = E[Var(X | Y)] + Var(E[X | Y])**

This decomposition is particularly useful in algorithm analysis where we want to understand both the average performance and the variability around that average.

### Computing Conditional Expectation from Joint Distribution

To compute conditional expectations, we follow a systematic approach:

1. Find the conditional distribution P(X = x | Y = y) or f_X|Y(x|y)
2. Multiply each value of X by its conditional probability
3. Sum (or integrate) over all possible values

## Examples

### Example 1: Expected Search Time in a Hash Table

Consider a simple hash table with n keys and m slots using linear probing. Let X be the number of probes needed to find an empty slot, and suppose the hash function distributes keys uniformly. If we know that a particular slot k is already occupied, what is the expected number of additional probes needed?

**Solution:**
Let Y be the event that slot k is occupied. We want E[X | Y]. Under linear probing with uniform hashing, the probability that any specific slot is occupied is approximately n/m (load factor α = n/m).

Given that slot k is occupied, the expected number of probes to find the next empty slot follows a geometric distribution with success probability (1 - α). Therefore:

**E[X | slot k occupied] = 1/(1 - α) = m/(m - n)**

This example illustrates how conditional expectation helps analyze data structure performance under partial information about the state of the system.

### Example 2: Average Case Analysis of QuickSort

QuickSort's running time depends on the choice of pivot. Let T(n) be the expected running time on an array of size n. When we choose a random pivot, the partition splits the array into two subarrays of sizes k and n-k-1 with equal probability (1/n for each k).

Using the law of total expectation and linearity:

**T(n) = E[T(n) | pivot position] = (1/n) Σₖ₌₀ⁿ⁻¹ [T(k) + T(n-k-1)] + O(n)**

This recurrence can be solved to show that the average case running time of QuickSort is O(n log n). The conditional expectation here is taken over the random choice of pivot, which allows us to analyze the expected performance.

### Example 3: Network Packet Delay Estimation

In a communication network, let X be the total delay experienced by a packet, and let Y indicate whether the buffer was full (Y = 1) or not (Y = 0) when the packet arrived. Suppose:
- P(Y = 1) = 0.3 (30% chance buffer is full)
- E[X | Y = 0] = 5 ms (average delay when buffer not full)
- E[X | Y = 1] = 25 ms (average delay when buffer is full)

Using the law of total expectation:
**E[X] = E[X | Y = 0] · P(Y = 0) + E[X | Y = 1] · P(Y = 1)**
**E[X] = 5 × 0.7 + 25 × 0.3 = 3.5 + 7.5 = 11 ms**

This example demonstrates how network engineers estimate average packet delay by conditioning on system states.

## Exam Tips

1. **Understand the definition thoroughly**: Students often confuse conditional expectation with conditional probability. Remember that conditional expectation is an expected value computed with respect to a conditional distribution.

2. **Apply the Law of Total Expectation strategically**: When a problem asks for E[X] but gives conditional information, try conditioning on a suitable random variable Y to simplify the calculation.

3. **Recognize independence**: If X and Y are independent, then E[X | Y] = E[X]. This simplifies many problems significantly.

4. **Treat E[X | Y] as a function of Y**: Always remember that the conditional expectation is a random variable that depends on Y. When computing probabilities involving E[X | Y], treat it as g(Y).

5. **Practice the variance decomposition**: The formula Var(X) = E[Var(X | Y)] + Var(E[X | Y]) is frequently tested in DU examinations.

6. **Master the properties**: Linearity and the "taking out what is known" property are essential for solving complex problems efficiently.

7. **Check your answers**: Use the Law of Total Expectation as a verification tool. If you compute E[X | Y] for different values of y, taking their expectation should give you back E[X].