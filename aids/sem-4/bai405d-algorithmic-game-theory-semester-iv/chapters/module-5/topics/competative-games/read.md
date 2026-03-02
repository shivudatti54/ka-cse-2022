Of course. Here is a comprehensive educational note on Competitive Games for  Engineering students, tailored to the specified curriculum.

# Module 5: Competitive Games

## 1. Introduction

Algorithmic Game Theory (AGT) sits at the intersection of computer science, economics, and mathematics. It studies the behavior of strategic agents in *algorithmic settings*. While cooperative game theory focuses on coalition formation, **Competitive Games** (often synonymous with non-cooperative games) analyze scenarios where rational, self-interested players make decisions to maximize their own utility, often in direct conflict with others. These games form the bedrock of modeling interactions in networked systems, online markets, and routing problems.

## 2. Core Concepts

### 2.1 Strategic-Form Games

The most fundamental model for competitive games is the **Strategic-Form** (or Normal-Form) game. It is defined by three components:
*   **Players:** A finite set of participants (e.g., `Player 1`, `Player 2`, ..., `Player n`).
*   **Strategies:** For each player, a set of possible actions or plans. The strategy set for player `i` is denoted `S_i`.
*   **Payoffs:** A function for each player that assigns a numerical utility (or payoff) for every possible combination of strategies chosen by all players. The payoff for player `i` is a function `u_i(s_1, s_2, ..., s_n)`.

### 2.2 The Nash Equilibrium (NE)

The central solution concept in competitive games is the **Nash Equilibrium (NE)**, named after mathematician John Nash. It describes a stable state where no player can unilaterally deviate to achieve a better payoff, given the strategies of all other players.

**Formal Definition:** A strategy profile `s* = (s*_1, s*_2, ..., s*_n)` is a Nash Equilibrium if for every player `i` and every alternative strategy `s_i ∈ S_i`:
`u_i(s*_i, s*_{-i}) ≥ u_i(s_i, s*_{-i})`
Here, `s*_{-i}` represents the strategies of all players *except* player `i`.

In simpler terms, in a NE, each player's strategy is a **best response** to the strategies of the others.

### 2.3 Example: The Prisoner's Dilemma

This classic example perfectly illustrates the tension between individual rationality and collective good.

*   **Players:** Two suspects arrested for a crime (Player A and Player B).
*   **Strategies:** Each player's strategy set is {**Cooperate** (Stay Silent), **Defect** (Betray the other)}.
*   **Payoffs:** The outcomes (often expressed as years reduced from a sentence) are represented in a payoff matrix:

|                       | Player B: Cooperate | Player B: Defect |
| --------------------- | -------------------- | ---------------- |
| **Player A: Cooperate** | (-1, -1)             | (-3, 0)          |
| **Player A: Defect**    | (0, -3)              | (-2, -2)         |

*(Note: Negative payoffs are common; a higher number is better, e.g., 0 > -1)*

**Analysis:**
*   If both cooperate (silent), they both get a light sentence (`-1`).
*   However, each player has an incentive to defect:
    *   If A thinks B will cooperate, A can get a great deal (`0`) by defecting.
    *   If A thinks B will defect, A must defect to avoid the worst outcome (`-3` vs `-2`).

Defecting is a **dominant strategy** for both—it yields a better payoff regardless of the other's choice. Therefore, the only Nash Equilibrium is (**Defect, Defect**), resulting in the worse collective outcome (`-2, -2`). This highlights how rational individual decisions can lead to a socially suboptimal result.

### 2.4 Variations and Important Types

*   **Zero-Sum Games:** A special class where one player's gain is exactly equal to the other players' loss. The total utility sum is always zero. Examples include poker, rock-paper-scissors, and many classic two-player games. The **Minimax Theorem** by von Neumann states that in such games, a solution (a pair of strategies) always exists.
*   **Mixed Strategies:** So far, we've considered **pure strategies** (choosing one action definitively). A **mixed strategy** is a probability distribution over a player's pure strategies. This is crucial for games like Rock-Paper-Scissors, where the only Nash Equilibrium is for each player to randomly choose each action with a probability of 1/3. Nash proved that **every finite strategic-form game has a Nash Equilibrium, possibly in mixed strategies.**

## 3. Key Points & Summary

*   **Competitive Games** model interactions between rational, self-interested agents.
*   They are formally described by their **players, strategies, and payoffs** (Strategic-Form).
*   The **Nash Equilibrium (NE)** is the core solution concept. It is a state where no player can benefit by unilaterally changing their strategy.
*   The **Prisoner's Dilemma** is a canonical example showing how individual rationality can lead to poor collective outcomes. The NE is not always the best overall result.
*   **Zero-Sum Games** are a specific, purely competitive class with well-defined solutions.
*   **Mixed Strategies** (randomizing over actions) are often necessary to find a Nash Equilibrium, guaranteeing its existence in finite games.
*   In AGT, we are concerned with the **computational complexity** of finding these equilibria, which is often challenging (PPAD-hard for general games).