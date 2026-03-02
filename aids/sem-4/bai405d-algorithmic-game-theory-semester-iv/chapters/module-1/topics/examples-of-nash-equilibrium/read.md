Of course. Here is a comprehensive educational note on "Examples of Nash Equilibrium" for  Engineering students, formatted as requested.

# Module 1: Examples of Nash Equilibrium

## Introduction

In Algorithmic Game Theory, the **Nash Equilibrium (NE)** is a fundamental solution concept that predicts the outcome of strategic interactions between rational players. It describes a state where no player can unilaterally change their strategy to achieve a better payoff, given the strategies chosen by all other players. This module explores the core concept through clear definitions and practical examples, moving from simple to more complex scenarios.

## Core Concepts

Before diving into examples, let's solidify two key ideas:

1.  **Strategic Form Game:** A model represented by:
    *   A set of **Players**.
    *   A set of **Strategies** for each player.
    *   A **Payoff Function** for each player, which depends on the combination of strategies chosen by all players.

2.  **Nash Equilibrium (Definition):** A strategy profile (a set of strategies, one for each player) is a Nash Equilibrium if **no player can benefit by deviating from their strategy while all other players keep their strategies unchanged**.

In other words, each player's strategy is a **best response** to the strategies of the others.

## Examples of Nash Equilibrium

### Example 1: The Prisoner's Dilemma (Classic Two-Player Game)

**Scenario:** Two suspects (Player A and Player B) are arrested and interrogated separately. They can either **Cooperate (C)** (stay silent) or **Defect (D)** (betray the other).

**Payoff Matrix:**

|                       | Player B: Cooperate | Player B: Defect |
| --------------------- | -------------------- | ---------------- |
| **Player A: Cooperate** | (-1, -1)             | (-3, 0)          |
| **Player A: Defect**    | (0, -3)              | (-2, -2)         |

*(Payoffs represent years in prison, so higher numbers are worse.)*

**Analysis:**
*   If Player B chooses **Cooperate**, Player A's best move is to **Defect** (0 > -1).
*   If Player B chooses **Defect**, Player A's best move is still to **Defect** (-2 > -3).
*   The same logic holds symmetrically for Player B.

**Nash Equilibrium:** The strategy profile **(Defect, Defect)** is the only Nash Equilibrium. Both players get -2 years. Even though mutual cooperation (-1, -1) is better for both, neither can unilaterally switch to Cooperate without hurting themselves (going from -2 to -3 years). This highlights how individual rationality can lead to a collectively worse outcome.

### Example 2: The Battle of the Sexes (Coordination Game)

**Scenario:** A couple (Player 1 and Player 2) must decide between going to a **Football (F)** game or a **Ballet (B)**. He prefers Football, she prefers Ballet, but both prefer being together over being alone.

**Payoff Matrix:**

|                    | Player 2: Football | Player 2: Ballet |
| ------------------ | ------------------- | ---------------- |
| **Player 1: Football** | (2, 1)              | (0, 0)           |
| **Player 1: Ballet**   | (0, 0)              | (1, 2)           |

**Analysis:**
*   If Player 2 chooses **Football**, Player 1's best response is **Football** (2 > 0).
*   If Player 2 chooses **Ballet**, Player 1's best response is **Ballet** (1 > 0).
*   The same logic applies to Player 2.

**Nash Equilibria:** This game has **two pure-strategy Nash Equilibria**: **(Football, Football)** and **(Ballet, Ballet)**. In both states, neither player has an incentive to go to the other event alone. This example shows that a game can have multiple equilibria.

### Example 3: Matching Pennies (Zero-Sum Game)

**Scenario:** Two players (Player 1 and Player 2) simultaneously choose to show either **Heads (H)** or **Tails (T)**. Player 1 wins if both match; Player 2 wins if they mismatch.

**Payoff Matrix:**

|                 | Player 2: Heads | Player 2: Tails |
| --------------- | --------------- | --------------- |
| **Player 1: Heads** | (+1, -1)        | (-1, +1)        |
| **Player 1: Tails** | (-1, +1)        | (+1, -1)        |

**Analysis:** There is **no pure-strategy Nash Equilibrium**.
*   If they play (Heads, Heads), Player 2 would want to switch to Tails.
*   If they play (Heads, Tails), Player 1 would want to switch to Tails.
*   This pattern continues endlessly. The only equilibrium is a **mixed-strategy Nash Equilibrium**, where each player randomizes their choice with a 50% probability for Heads and Tails. This introduces the important concept that not all equilibria involve deterministic choices.

## Key Points & Summary

| Key Point | Description |
| :--- | :--- |
| **Definition** | A stable state where no player can improve their payoff by unilaterally changing their strategy. |
| **Best Response** | A player's strategy is a best response if it yields the highest possible payoff against the opponents' chosen strategies. NE is a profile of mutual best responses. |
| **Existence** | Nash's Theorem proves that **every finite game** has at least one Nash Equilibrium, though it might be in mixed strategies. |
| **Multiplicity** | Games can have **zero** (Matching Pennies), **one** (Prisoner's Dilemma), or **multiple** (Battle of the Sexes) Nash Equilibria. |
| **Efficiency** | An NE is not necessarily the best overall outcome. The Prisoner's Dilemma shows an NE can be **Pareto inefficient** (everyone could do better). |
| **Algorithmic Focus** | A major goal of Algorithmic Game Theory is to **compute** these equilibria efficiently, which is often computationally challenging. |