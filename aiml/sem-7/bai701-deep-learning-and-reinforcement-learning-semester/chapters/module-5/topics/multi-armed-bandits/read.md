# Module 5: Multi-Armed Bandits

## Introduction

In the broader landscape of Reinforcement Learning (RL), an agent learns to make optimal decisions by interacting with an environment. However, many complex RL problems can be distilled into a simpler, fundamental dilemma: the **exploration vs. exploitation trade-off**. The Multi-Armed Bandit (MAB) problem is the quintessential framework for studying this trade-off in a simplified, stateless setting. Imagine a gambler facing a row of slot machines (often called "one-armed bandits"), each with an unknown probability of providing a reward. The gambler must decide which machines to play, how many times to play each, and in which order to play them to maximize their total reward. This scenario perfectly encapsulates the core challenge: should you **exploit** the machine that has given the best rewards so far, or **explore** other machines that might have a higher payout?

## Core Concepts

### 1. The Formal Problem

A K-armed bandit problem is defined by:
*   **Arms (or Actions):** A set of `K` possible actions (`a₁, a₂, ..., aₖ`). In our example, each slot machine is an arm.
*   **Reward Distribution:** Each arm `a` has an associated probability distribution of rewards with an unknown mean (`μₐ`). This is the true, hidden average payout for that machine.
*   **Goal:** The agent's goal is to maximize the total reward (or equivalently, minimize **regret**) over a time horizon `T` (a fixed number of pulls).

### 2. Regret: The Measure of Performance

The performance of a bandit algorithm is measured not by total reward, but by **regret**. Regret quantifies the cost of not choosing the best action (the optimal arm `a*`).

*   **Instantaneous Regret** at time `t`: The difference between the reward of the optimal arm and the reward of the arm you chose.
    `regretₜ = μ* - μₐₜ`
*   **Total Regret:** The sum of all instantaneous regrets over `T` rounds.
    `R(T) = Σ [μ* - μₐₜ]` for `t=1` to `T`.

A good algorithm seeks to have its total regret grow *sub-linearly* with `T`. This means the average regret per step (`R(T)/T`) goes to zero over time, indicating the agent is learning the optimal action.

### 3. Exploration vs. Exploitation

This is the heart of the bandit problem:
*   **Exploitation:** Choosing the arm that has the highest *estimated* reward based on current knowledge. This maximizes immediate gain but may lead to missing a better arm.
*   **Exploration:** Choosing an arm that is not the current best-estimated to gather more information about its reward distribution. This sacrifices immediate gain for potentially higher long-term gains.

### 4. Simple Algorithms

#### Greedy Algorithm
This is a pure **exploitation** strategy.
*   **Method:** At every step, choose the arm with the highest estimated value (average reward received so far).
*   **Drawback:** It may lock onto a suboptimal arm early on and never explore a potentially better one.

#### ε-Greedy Algorithm
This is a simple but powerful strategy that balances exploration and exploitation with a parameter `ε` (epsilon).
*   **Method:** With probability `1 - ε`, choose the greedy arm (exploit). With probability `ε`, choose any arm uniformly at random (explore).
*   **Trade-off:** A large `ε` explores more, while a small `ε` exploits more. It often requires tuning for the specific problem.

#### Upper Confidence Bound (UCB) Algorithm
This is a more sophisticated and theoretically grounded approach that uses confidence bounds to guide exploration.
*   **Idea:** The algorithm maintains an estimate of each arm's value *and* the uncertainty (confidence interval) of that estimate. It is optimistic in the face of uncertainty.
*   **Method:** At each step, choose the arm `a` that maximizes:
    `Q(a) + c * √(log(t) / Nₜ(a))`
    where:
    *   `Q(a)` is the estimated value of arm `a`.
    *   `Nₜ(a)` is the number of times arm `a` has been chosen so far.
    *   `c` is a confidence parameter.
    *   `log(t)` ensures the term grows slowly over time `t`.
*   The `√(...)` term represents the uncertainty. An arm that has been pulled less often (`Nₜ(a)` is small) has a higher uncertainty, making it more likely to be chosen. This ensures systematic exploration of less-known arms.

## Example: Online Advertising

Imagine a website showing one of three ads (`K=3`) to each user.
*   **Arms:** Ad #1, Ad #2, Ad #3.
*   **Reward:** A click is a reward of `1`; no click is `0`.
*   **Goal:** Maximize the total number of clicks over 1 million visits.

Each ad has a true, unknown click-through rate (CTR: `μ₁, μ₂, μ₃`). A **Greedy** algorithm might show the first ad that got a click forever. An **ε-Greedy** would mostly show the best-performing ad but occasionally test the others. **UCB** would mathematically balance showing the ad with the highest upper confidence bound of its CTR, efficiently identifying the best ad.

## Key Points & Summary

*   **Core Problem:** Multi-Armed Bandits formalize the **exploration-exploitation dilemma** in a stateless environment.
*   **Objective:** Maximize cumulative reward or, equivalently, minimize **total regret** (`R(T)`).
*   **Regret** measures the cost of not choosing the optimal action at every step.
*   **Simple Strategies:**
    *   **Greedy:** Pure exploitation; prone to suboptimal performance.
    *   **ε-Greedy:** Simple forced exploration; effective but requires parameter tuning.
*   **Advanced Strategy:**
    *   **UCB:** Uses optimism (upper confidence bounds) to guide exploration intelligently, leading to better theoretical guarantees.
*   **Foundation:** The MAB problem is a foundational element of RL, introducing core concepts that scale to more complex problems with states (like MDPs).