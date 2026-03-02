# Module 4: Multi-armed Bandit Algorithms

## Introduction

In the realm of Statistical Machine Learning, we often face a fundamental trade-off: the tension between **exploration** (gathering new information) and **exploitation** (leveraging known information to maximize rewards). The Multi-armed Bandit (MAB) problem is a classic framework that elegantly formalizes this dilemma. Imagine a gambler facing a row of slot machines (often called "one-armed bandits"). Each machine has an unknown probability distribution of payouts. The gambler's goal is to devise a strategy to maximize their total reward over a series of plays. For data scientists and engineers, this is a powerful metaphor for scenarios like A/B testing website layouts, clinical trials, or online ad placement, where we must efficiently learn the best option while minimizing regret.

## Core Concepts

### 1. The Problem Setup

*   **Arms (k):** The set of available choices or actions. In our example, each slot machine is an "arm." In practice, an arm could be a recommendation algorithm, a drug dosage, or a website design.
*   **Reward (r_t):** The outcome received after pulling an arm at time `t`. Rewards are typically stochastic, drawn from an unknown probability distribution specific to each arm.
*   **Goal:** Maximize the cumulative sum of rewards over a finite time horizon `T`.
*   **Regret:** The primary metric for evaluating a bandit algorithm. It measures the difference between the reward you could have achieved if you always chose the best arm (the "oracle" strategy) and the reward you actually achieved.
    `Total Regret = Σ (Optimal Reward - Reward Received at each step t)`
    A good algorithm seeks to **minimize cumulative regret**.

### 2. Exploration vs. Exploitation

This is the heart of the problem:
*   **Exploitation:** Pulling the arm that has historically given the highest average reward. This maximizes immediate gain based on current knowledge but may miss a better arm.
*   **Exploration:** Pulling a different arm to gather more information about its reward distribution. This is costly in the short term but is necessary for long-term optimal performance.

### 3. The ε-Greedy Algorithm

This is one of the simplest and most intuitive strategies to balance exploration and exploitation.

*   **Parameter:** A small value ε (e.g., 0.1), which is the probability of exploration.
*   **Algorithm:**
    1.  With probability **(1 - ε)**, **exploit:** choose the arm with the highest current estimated average reward.
    2.  With probability **ε**, **explore:** choose any arm uniformly at random (including the currently best one).

**Example:** You are A/B testing two website headlines (Arm A and Arm B). After 100 visits, Arm A has a 5% click-through rate (CTR), Arm B has a 3% CTR.
*   With ε=0.1, 90% of the time you will show the better headline (Arm A).
*   10% of the time, you will randomly show either headline. This allows you to discover if Arm B's performance has improved over time.

**Drawback:** Exploration is done completely randomly, without considering the potential of the non-optimal arms.

### 4. Upper Confidence Bound (UCB) Algorithm

The UCB algorithm is a more sophisticated and theoretically grounded approach. It is "optimistic in the face of uncertainty." The core idea is to estimate an upper bound for the true expected reward of each arm and select the arm with the highest bound.

*   It calculates a value for each arm `i` at time `t`:
    `UCB(i) = Estimated Mean Reward(i) + Confidence Bound(i)`
*   A common UCB1 formula is:
    `UCB(i) = μ_i + √( (2 * ln(t)) / n_i )`
    where:
    *   `μ_i` is the current average reward for arm `i`.
    *   `n_i` is the number of times arm `i` has been pulled.
    *   `t` is the total number of pulls so far.

*   **Interpretation:**
    *   `μ_i` represents the **exploitation** component (what we know).
    *   `√( (2 * ln(t)) / n_i )` represents the **exploration bonus**. It is large if an arm has been pulled很少 times (`n_i` is small) relative to the total time passed. This encourages trying under-explored arms.

**Algorithm:** At each step, pull the arm `argmax( UCB(i) )`.

**Example:** A new ad (Arm C) is added to your campaign. It has only been shown 10 times (`n_c` is small), so its confidence interval term is large. Even if its current average reward (`μ_c`) is low, its UCB score might be higher than that of a well-explored arm, causing the algorithm to intelligently explore it.

## Key Points & Summary

*   **Core Dilemma:** Multi-armed bandit problems formally model the **exploration-exploitation trade-off**, a central challenge in sequential decision-making under uncertainty.
*   **Objective:** The goal is to **maximize cumulative reward** or, equivalently, **minimize cumulative regret**.
*   **ε-Greedy:** A simple and popular strategy that explores randomly with probability ε. It is easy to implement but explores inefficiently.
*   **UCB:** A more efficient, optimistic algorithm that assigns an optimistic value (upper confidence bound) to under-explored arms, leading to more targeted and intelligent exploration.
*   **Why it matters for Data Science:** MAB algorithms provide a statistically efficient framework for **online learning and decision-making**. They are vastly more efficient than traditional A/B testing (which is pure exploration followed by pure exploitation) for applications like:
    *   Dynamic ad placement
    *   Recommendation systems
    *   Hyperparameter tuning
    *   Clinical trial designs

Understanding bandit algorithms equips you with powerful tools to build systems that learn and adapt optimally from user feedback in real-time.