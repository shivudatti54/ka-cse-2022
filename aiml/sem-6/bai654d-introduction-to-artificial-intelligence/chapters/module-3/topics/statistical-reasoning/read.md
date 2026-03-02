# Module 3: Statistical Reasoning in AI

## Introduction

Welcome to Module 3 of Introduction to Artificial Intelligence. While logic-based reasoning (covered in previous modules) is powerful for deterministic problems, the real world is fraught with uncertainty. Statistical reasoning provides a mathematical framework for making rational decisions and inferences under this uncertainty. It is the backbone of modern AI, enabling systems to learn from data, predict outcomes, and handle incomplete information. This module explores how probability theory forms the basis for intelligent behaviour in uncertain environments.

## Core Concepts

### 1. Probability and Bayes' Theorem

At its core, probability quantifies uncertainty. It is a measure between 0 and 1, representing the likelihood of an event occurring, where 0 is impossibility and 1 is certainty.

The most crucial rule in statistical reasoning is **Bayes' Theorem** (or Bayes' Rule). It describes the probability of an event based on prior knowledge of conditions that might be related to the event. Its formula is:

`P(H|E) = [P(E|H) * P(H)] / P(E)`

Where:
*   `P(H|E)` is the **posterior probability**. This is the probability of hypothesis `H` *after* observing evidence `E`. This is what we want to compute.
*   `P(H)` is the **prior probability**. This is the initial probability of `H` *before* seeing any evidence.
*   `P(E|H)` is the **likelihood**. This is the probability of observing evidence `E` *given* that hypothesis `H` is true.
*   `P(E)` is the **marginal likelihood** (or evidence). This is the total probability of observing evidence `E` under all possible hypotheses.

**Example: Medical Diagnosis**
Suppose a disease `D` appears in 1% of the population (`P(D) = 0.01`). A test for this disease is 99% accurate: it gives a positive result for 99% of infected people (`P(+|D) = 0.99`) and a negative result for 99% of healthy people (`P(-|¬D) = 0.99`).

If a patient tests positive (`E = +`), what is the probability they actually have the disease (`P(D|+)`)?

Using Bayes' Theorem:
1.  Prior, `P(D) = 0.01`
2.  Likelihood, `P(+|D) = 0.99`
3.  Marginal Likelihood, `P(+) = P(+|D)*P(D) + P(+|¬D)*P(¬D) = (0.99)(0.01) + (0.01)(0.99) = 0.0198`
4.  Posterior, `P(D|+) = (0.99 * 0.01) / 0.0198 ≈ 0.5`

Despite the "99% accurate" test, the probability of having the disease after a positive result is only about 50%. This counter-intuitive result highlights the importance of considering prior probabilities.

### 2. Bayesian Networks

For complex problems with many variables, applying Bayes' Theorem directly becomes computationally infeasible. **Bayesian Networks** (or Belief Networks) solve this. They are a type of **Probabilistic Graphical Model** that represents a set of variables and their conditional dependencies via a Directed Acyclic Graph (DAG).

*   **Nodes** represent random variables (e.g., `Rain`, `Sprinkler`, `GrassWet`).
*   **Edges** represent conditional dependencies.
*   Each node has a **Conditional Probability Table (CPT)** that quantifies the effect of its parents.

This structure allows for efficient computation of joint probabilities for a large number of variables. The network encodes the assumption: *a node is conditionally independent of its non-descendants given its parents*. This dramatically simplifies reasoning.

**Example: A Simple Bayesian Network**
Imagine a network with three variables:
1.  `Rain` (R): Yes/No
2.  `Sprinkler` (S): On/Off (which depends on `Rain`)
3.  `Grass Wet` (W): Yes/No (which depends on both `Rain` and `Sprinkler`)

The graph would be R → S → W and R → W. The CPT for `Grass Wet` would list `P(W | R, S)` for all combinations of R and S. This network can be used to answer queries like "What is the probability that it rained, given that the grass is wet?" (`P(R|W)`).

### 3. Uncertainty and Rational Decisions

Statistical reasoning ultimately aims to support decision-making. The concept of **utility** is introduced to represent the value or desirability of an outcome. A rational agent chooses the action that maximizes its **expected utility**.

`EU(A) = Σ_{i} P(Result_i | A) * U(Result_i)`

Where `Result_i` are the possible outcomes of action `A`. This framework of probability and utility is the foundation of **decision theory**.

## Key Points & Summary

*   **Handling Uncertainty:** Statistical reasoning is essential for AI to operate effectively in the real, uncertain world.
*   **Bayes' Theorem:** The fundamental rule for updating beliefs (`posterior`) based on new evidence (`likelihood`), while incorporating existing knowledge (`prior`).
*   **Bayesian Networks:** A powerful graphical tool to represent complex probabilistic relationships between many variables efficiently. They use conditional independence assumptions to simplify computations.
*   **Decision Theory:** The combination of probability (what we believe) and utility (what we want) to define rational, optimal behaviour for an intelligent agent.
*   **Applications:** These concepts are not just theoretical; they are the bedrock of modern machine learning, spam filtering, medical diagnostic systems, robotics, and any AI system that must reason with incomplete or noisy data.