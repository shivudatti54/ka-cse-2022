# Poisson and Normal (Problems & Derivations)

## Table of Contents

- [Poisson and Normal (Problems & Derivations)](#poisson-and-normal-problems--derivations)
- [Core Concepts and Derivations](#core-concepts-and-derivations)
  - [1. Poisson Distribution](#1-poisson-distribution)
  - [2. Normal (Gaussian) Distribution](#2-normal-gaussian-distribution)
- [Example Problem (Poisson)](#example-problem-poisson)
- [Key Points & Summary](#key-points--summary)

## Core Concepts and Derivations

### 1. Poisson Distribution

The Poisson distribution models the probability of a given number of events occurring in a fixed interval of time or space, provided these events happen with a known constant mean rate ($\lambda$) and independently of the time since the last event.

Its Probability Mass Function (PMF) is:
$$P(X = k) = \frac{e^{-\lambda} \lambda^{k}}{k!}$$
where $k = 0, 1, 2, 3, ...$ is the number of occurrences, and $\lambda$ is the average rate (mean).

#### Derivation of the Mean (E[X])

The mean, or expected value, for a discrete distribution is defined as:
$$E[X] = \sum_{k=0}^{\infty} k \cdot P(X=k)$$

Substituting the Poisson PMF:

$$
E[X] = \sum_{k=0}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^{k}}{k!}
$$

Notice that for $k=0$, the term $k \cdot P(X=0)$ is $0$. So, we can start the sum from $k=1$:

$$
E[X] = \sum_{k=1}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^{k}}{k!} = \sum_{k=1}^{\infty} \frac{e^{-\lambda} \lambda^{k}}{(k-1)!}
$$

Factor out $\lambda$ and $e^{-\lambda}$:

$$
E[X] = e^{-\lambda} \lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}
$$

Let $j = k - 1$. As $k$ goes from $1$ to $\infty$, $j$ goes from $0$ to $\infty$:

$$
E[X] = e^{-\lambda} \lambda \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!}
$$

The summation $\sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!}$ is the Taylor series expansion of $e^{\lambda}$. Therefore:

$$
E[X] = e^{-\lambda} \lambda \cdot e^{\lambda} = \lambda
$$

**Result:** The mean of a Poisson distribution is $E[X] = \lambda$.

### 2. Normal (Gaussian) Distribution

The Normal distribution is a continuous distribution that is symmetric about its mean, describing many natural phenomena and measurement errors. Its Probability Density Function (PDF) is:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
where $\mu$ is the mean and $\sigma$ is the standard deviation.

#### Derivation of the Mean (E[X])

The expected value for a continuous distribution is:
$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx$$

Substitute the normal PDF:

$$
E[X] = \int_{-\infty}^{\infty} x \cdot \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} dx
$$

Use the substitution $z = \frac{x - \mu}{\sigma}$. Then, $x = \mu + \sigma z$ and $dx = \sigma dz$.

$$
E[X] = \frac{1}{\sigma\sqrt{2\pi}} \int_{-\infty}^{\infty} (\mu + \sigma z) e^{-\frac{1}{2}z^2} \sigma dz
$$

Simplify:

$$
E[X] = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} (\mu + \sigma z) e^{-\frac{1}{2}z^2} dz
$$

Break this into two integrals:

$$
E[X] = \frac{1}{\sqrt{2\pi}} \left[ \mu \int_{-\infty}^{\infty} e^{-\frac{1}{2}z^2} dz + \sigma \int_{-\infty}^{\infty} z e^{-\frac{1}{2}z^2} dz \right]
$$

1. The first integral, $\int_{-\infty}^{\infty} e^{-\frac{1}{2}z^2} dz$, is $\sqrt{2\pi}$ (the total area under a standard normal PDF).
2. The second integral, $\int_{-\infty}^{\infty} z e^{-\frac{1}{2}z^2} dz$, is an odd function evaluated over symmetric limits, so its value is **0**.

Therefore:

$$
E[X] = \frac{1}{\sqrt{2\pi}} \left[ \mu \cdot \sqrt{2\pi} + \sigma \cdot 0 \right] = \frac{1}{\sqrt{2\pi}} \cdot \mu \sqrt{2\pi} = \mu
$$

**Result:** The mean of a Normal distribution is $E[X] = \mu$.

---

## Example Problem (Poisson)

**Problem:** A web server receives an average of 4 requests per second ($\lambda = 4$). What is the probability that it receives exactly 6 requests in a given second?

**Solution:**
Using the Poisson PMF with $k=6$ and $\lambda=4$:

$$
P(X=6) = \frac{e^{-4} \cdot 4^6}{6!} = \frac{0.0183 \cdot 4096}{720} \approx \frac{75.0}{720} \approx 0.1042
$$

There is approximately a 10.42% chance of exactly 6 requests in a second.

---

## Key Points & Summary

| Distribution | Type       | Parameter(s)                       | Mean ($E[X]$) | Key Application                                                            |
| :----------- | :--------- | :--------------------------------- | :------------ | :------------------------------------------------------------------------- |
| **Poisson**  | Discrete   | $\lambda$ (mean rate)              | $\lambda$     | Modeling rare, independent events over time/space (e.g., packets, errors). |
| **Normal**   | Continuous | $\mu$ (mean), $\sigma$ (std. dev.) | $\mu$         | Modeling measurements, natural phenomena, noise (e.g., sensor data).       |

- **Poisson Derivation:** The mean is derived by manipulating an infinite series, leveraging the Taylor series for $e^{\lambda}$.
- **Normal Derivation:** The mean is derived using a change of variable (z-score) and leveraging the properties of odd/even functions over symmetric intervals.
- ** Focus:** Mastering these derivations is essential. You must be able to replicate these steps and apply the distributions to solve engineering problems, such as calculating probabilities and expected values in real-world scenarios like queuing theory or signal processing.
