# Mathematics for Computer Science - Module 1: Probability Distributions

## Topic: Review of Basic Probability Theory & Random Variables

### Introduction

Probability theory is the mathematical framework for analyzing uncertainty, a concept inherent in countless computer science applications. From designing randomized algorithms and machine learning models to network traffic analysis and cryptography, a solid grasp of probability is indispensable. This review session will re-establish the core principles of probability and introduce the fundamental concept of a **random variable**, which allows us to move from abstract events to quantifiable numerical outcomes.

### Core Concepts

#### 1. Basic Probability Theory

At its heart, probability measures the likelihood of an event occurring.

*   **Sample Space (S):** The set of all possible outcomes of a random experiment. For example, the sample space for a single coin toss is `S = {Heads, Tails}`.
*   **Event (E):** Any subset of the sample space. For example, the event "getting a head" is `E = {Heads}`.
*   **Probability of an Event (P(E)):** A number between 0 and 1 (inclusive) assigned to an event. `P(E) = 0` means the event is impossible, while `P(E) = 1` means it is certain.
*   **Axioms of Probability:**
    1.  **Non-Negativity:** `P(E) >= 0` for any event E.
    2.  **Normalization:** `P(S) = 1`. The probability of some outcome occurring is 1.
    3.  **Additivity:** For any sequence of mutually exclusive events (events that cannot happen simultaneously, e.g., getting a 1 *or* a 2 on a die roll), the probability of their union is the sum of their probabilities: `P(E1 ∪ E2 ∪ ...) = P(E1) + P(E2) + ...`

From these axioms, other crucial rules follow, such as `P(not E) = 1 - P(E)` and the formula `P(A ∪ B) = P(A) + P(B) - P(A ∩ B)` for events that are not mutually exclusive.

#### 2. Random Variables

A **Random Variable (RV)** is a powerful function that assigns a real number to each outcome in the sample space. It bridges the gap between non-numerical outcomes and quantitative analysis.

*   **Formal Definition:** Let `S` be a sample space. A random variable `X` is a function `X: S -> R`, mapping outcomes to real numbers.

There are two primary types of random variables:

**a) Discrete Random Variables**
An RV is discrete if it can take on a finite or countably infinite number of distinct values (e.g., integers).

*   **Probability Mass Function (PMF):** Denoted as `p(x)`, the PMF gives the probability that a discrete random variable `X` takes exactly the value `x`.
    `p(x) = P(X = x)`
    The PMF must satisfy: (i) `0 <= p(x) <= 1` for all `x`, and (ii) `Σ p(x) = 1` (sum over all possible values of `x`).

*   **Example:** Consider the random variable `X` defined as the number of heads in two coin tosses.
    *   Possible values of `X`: {0, 1, 2}
    *   Sample Space: {TT, TH, HT, HH}
    *   PMF:
        `P(X=0) = P(TT) = 1/4`
        `P(X=1) = P(TH ∪ HT) = P(TH) + P(HT) = 1/4 + 1/4 = 1/2`
        `P(X=2) = P(HH) = 1/4`

**b) Continuous Random Variables**
An RV is continuous if it can take on an uncountably infinite number of values (e.g., any value in an interval, like time, height, or temperature).

*   **Probability Density Function (PDF):** Denoted as `f(x)`, the PDF describes the relative likelihood for a continuous random variable to take on a given value. **Crucially, `f(x)` is *not* a probability.** For a continuous RV, `P(X = x) = 0` for any specific point `x`.
*   **Probability as an Area:** Probability is defined as the area under the PDF curve for an interval.
    `P(a < X < b) = ∫(from a to b) f(x) dx`
    The PDF must satisfy: (i) `f(x) >= 0` for all `x`, and (ii) `∫(over all x) f(x) dx = 1`.

*   **Example:** The time (in seconds) a server takes to respond to a query, `T`, is a continuous RV. The probability that the response time is between 1.0 and 1.5 seconds is found by integrating its PDF `f(t)` from 1.0 to 1.5.

### Key Points & Summary

| Concept | Description | Key Function | Applies to |
| :--- | :--- | :--- | :--- |
| **Sample Space (S)** | Set of all possible outcomes of an experiment. | - | - |
| **Event (E)** | A subset of the sample space. | - | - |
| **Probability P(E)** | Likelihood of an event `E`, `0 <= P(E) <= 1`. | - | - |
| **Random Variable (X)** | A function that maps outcomes to real numbers. | `X: S -> R` | Both |
| **Discrete RV** | Takes finite/countable distinct values. | - | - |
| **Probability Mass Function (PMF)** | Gives `P(X = x)` for a specific value `x`. | `p(x) = P(X=x)` | Discrete |
| **Continuous RV** | Takes uncountable values in an interval. | - | - |
| **Probability Density Function (PDF)** | Describes relative likelihood; probability is area under the curve. | `P(a<X<b)=∫f(x)dx` | Continuous |

**Why is this important for Computer Science?** Discrete random variables model things like the number of bits in error in a data packet, the number of searches on a server, or the roll of a die in a game. Continuous random variables model metrics like algorithm execution time, network latency, and sensor readings. Mastering these concepts is the first step toward understanding more complex probability distributions that model real-world phenomena in computing.