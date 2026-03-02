Of course. Here is a comprehensive educational note on Cournot's duopoly game with imperfect information, tailored for  engineering students.

# Cournot's Duopoly Game with Imperfect Information

## Introduction

In **Algorithmic Game Theory**, we study how rational agents make strategic decisions. Cournot's duopoly model is a classic example of a non-cooperative game where two firms (duopolists) compete by simultaneously choosing their output quantities. The standard model assumes **perfect information**—each firm knows its own cost structure and its competitor's. However, in the real world, a firm's production costs are often private information. **Module 4** introduces us to this more realistic scenario: **Cournot competition with imperfect information**, where firms must form beliefs about their rival's costs.

## Core Concepts

### 1. Standard Cournot Model (A Quick Recap)
In the standard model with perfect information, two firms, Firm 1 and Firm 2, produce a homogeneous product. The market price `P` is determined by the inverse demand function `P(Q) = a - Q`, where `Q = q1 + q2` is the total quantity supplied. Each firm `i` has a constant marginal cost `ci`. The profit for Firm `i` is:
**π_i(qi, qj) = [P(Q) - ci] * qi = [a - (qi + qj) - ci] * qi**

Each firm chooses its quantity `qi` to maximize its own profit, given its belief about the other firm's quantity. The solution leads to a **Nash Equilibrium** where each firm's choice is a best response to the other's.

### 2. Introducing Imperfect Information
The key change in the imperfect information model is that a firm's cost is now **private knowledge**. Let's assume:
*   **Firm 1** has a known, common marginal cost `c1`.
*   **Firm 2**'s marginal cost is private. It can be either **high (`cH`)** with probability `θ` or **low (`cL`)** with probability `(1 - θ)`, where `cH > cL`.
*   Firm 1 knows the *possible* costs for Firm 2 and their probabilities but does not know which one is true when making its decision. Firm 2, of course, knows its own cost.

This asymmetry of information is the core of the game. Firm 1 must now optimize its output based on its *expectation* of Firm 2's behavior.

### 3. Solving the Game: Best Responses and Bayesian Nash Equilibrium (BNE)
We solve this using the concept of a **Bayesian Nash Equilibrium (BNE)**, which is the extension of Nash Equilibrium to games of imperfect information. In a BNE, the strategy of each player is a best response to the *expected* strategies of the other players, given their beliefs about the other players' types (here, cost types).

The solution involves the following steps:

1.  **Firm 2's Strategy (Informed Player):** Firm 2 knows its own cost. Therefore, it will have two different best-response functions, one for each possible cost type.
    *   If its cost is high (`cH`), it maximizes: **π₂ᴴ(q1, q2ᴴ) = [a - (q1 + q2ᴴ) - cH] * q2ᴴ**
    *   If its cost is low (`cL`), it maximizes: **π₂ᴸ(q1, q2ᴸ) = [a - (q1 + q2ᴸ) - cL] * q2ᴸ**
    We can derive these best-response functions by taking the derivative of the profit function with respect to `q2` and setting it to zero.

2.  **Firm 1's Strategy (Uninformed Player):** Firm 1 does not know Firm 2's cost. It must choose `q1` to maximize its *expected profit*. Its expected profit is the average of the profits it would get against a high-cost Firm 2 and a low-cost Firm 2, weighted by their probabilities (`θ` and `1-θ`).
    **E[π₁(q1, q2)] = θ * [a - (q1 + q2ᴴ) - c1] * q1 + (1-θ) * [a - (q1 + q2ᴸ) - c1] * q1**

3.  **Finding the Equilibrium:** A Bayesian Nash Equilibrium is a set of strategies `(q1*, q2ᴴ*, q2ᴸ*)` where:
    *   `q2ᴴ*` is a best response for the high-cost Firm 2 to `q1*`.
    *   `q2ᴸ*` is a best response for the low-cost Firm 2 to `q1*`.
    *   `q1*` is a best response to the *expected* quantity of Firm 2, i.e., `E[q2] = θ*q2ᴴ* + (1-θ)*q2ᴸ*`.

Solving these three equations simultaneously gives us the equilibrium quantities for all scenarios.

### Example (With Numbers)
Assume market demand: `P = 100 - (q1 + q2)`. Firm 1's cost is `c1 = 10`.
Firm 2's cost is `cH = 20` (with probability `θ = 0.5`) or `cL = 5` (with probability `1-θ = 0.5`).

**Firm 2's Best Responses (Standard Cournot formula: q_j = (a - c_j - q_i)/2 ):**
*   If high-cost: `q2ᴴ = (100 - 20 - q1)/2 = (80 - q1)/2`
*   If low-cost: `q2ᴸ = (100 - 5 - q1)/2 = (95 - q1)/2`

**Firm 1's Expected Profit Maximization:**
Firm 1's expected quantity from Firm 2 is `E[q2] = 0.5 * q2ᴴ + 0.5 * q2ᴸ`.
Firm 1 chooses `q1` to max: `[100 - (q1 + E[q2]) - 10] * q1`

Substituting and solving this system leads to specific numerical values for `q1*`, `q2ᴴ*`, and `q2ᴸ*`, which constitute the BNE. You will find that the low-cost Firm 2 produces more than the high-cost Firm 2, which is an intuitive result.

## Key Points & Summary

*   **Imperfect Information:** Firms lack complete knowledge about their rival's key parameters, such as production costs. This is a more realistic model of market competition.
*   **Bayesian Nash Equilibrium (BNE):** This is the solution concept. Strategies must be best responses to the *expected* strategies of others, given a probability distribution over their possible "types" (e.g., cost types).
*   **Firm 1's Decision:** The uninformed firm (Firm 1) bases its output on the **expected value** of its rival's quantity (`E[q2]`).
*   **Firm 2's Decision:** The informed firm (Firm 2) has a distinct strategy for each of its possible types. A lower-cost firm will optimally produce a higher quantity.
*   **Algorithmic Connection:** Understanding how to compute these equilibria is crucial for modeling automated agents in economic scenarios, such as e-commerce platforms where bots with different efficiencies might compete.