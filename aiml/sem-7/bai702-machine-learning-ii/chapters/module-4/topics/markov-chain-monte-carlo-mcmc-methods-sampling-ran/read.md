# **Markov Chain Monte Carlo (MCMC) Methods: Sampling**

## **Introduction**

Markov Chain Monte Carlo (MCMC) methods are a class of algorithms used for sampling from complex probability distributions. In this section, we will cover the basics of MCMC methods, including random numbers, Gaussian random numbers, Monte Carlo or Bust, the proposal distribution, and Markov chains.

## **Random Numbers**

A random number is a value chosen from a probability distribution. In MCMC methods, random numbers are used to sample from a target distribution.

- **Pseudorandom numbers**: These are generated using an algorithm, such as the linear congruential generator.
- **Quasi-Monte Carlo methods**: These use a sequence of points in a low-dimensional space to approximate the distribution.

## **Gaussian Random Numbers**

Gaussian random numbers are random numbers drawn from a normal distribution. They are commonly used in MCMC methods due to their ability to represent a wide range of probability distributions.

- **Mean and variance**: The mean and variance of a normal distribution determine its shape and spread.
- **Standard deviation**: The standard deviation is a measure of the spread of the distribution.

## **Monte Carlo or Bust**

The phrase "Monte Carlo or Bust" refers to the idea that Monte Carlo methods are only useful if they can generate samples from a target distribution.

- **Importance sampling**: This technique involves sampling from a proposal distribution to generate samples from the target distribution.
- **Control variates**: This technique involves using a secondary distribution to reduce the variance of the samples.

## **The Proposal Distribution**

The proposal distribution is a probability distribution used to generate samples from the target distribution. It is typically chosen to be easy to sample from and to have a similar shape to the target distribution.

- **Single-chain MCMC**: This involves using a single proposal distribution to generate samples from the target distribution.
- **Multi-chain MCMC**: This involves using multiple proposal distributions to generate samples from the target distribution.

## **Markov Chains**

A Markov chain is a sequence of random states, where each state is chosen based on the previous state.

- **Transition matrix**: This is a matrix that describes the probability of transitioning from one state to another.
- **Stationary distribution**: This is the long-term probability distribution of the Markov chain.

## **Example Use Case**

Suppose we want to sample from a complex probability distribution using an MCMC method. We can use a proposal distribution to generate samples from the target distribution, and then use a transition matrix to update the samples and generate a new set of samples.

### Algorithm

1.  Initialize the proposal distribution and the target distribution.
2.  Choose an initial state from the proposal distribution.
3.  Generate a new state by applying the transition matrix to the current state.
4.  Generate a new sample from the target distribution using the new state.
5.  Repeat steps 3-4 until a specified number of samples have been generated.

### Code

```python
import numpy as np

# Define the transition matrix
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])

# Define the proposal distribution
proposal_distribution = np.array([0.5, 0.5])

# Initialize the state
state = 0

# Initialize the samples
samples = []

# Generate samples
for i in range(1000):
    # Generate a new state
    new_state = np.random.choice([0, 1], p=transition_matrix[state, :])

    # Generate a new sample from the target distribution
    sample = np.random.normal(0, 1, size=1)

    # Update the samples
    samples.append(sample)

    # Update the state
    state = new_state

# Print the samples
print(samples)
```

This code generates 1000 samples from a complex probability distribution using an MCMC method. The transition matrix and proposal distribution are defined, and the samples are generated using a loop.
