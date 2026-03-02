Of course. Here is a comprehensive educational note on finding subgame perfect equilibria in finite horizon games, tailored for  Engineering students.

# Module 3: Finding Subgame Perfect Equilibria in Finite Horizon Games

## 1. Introduction

In game theory, a **Nash Equilibrium (NE)** is a set of strategies where no player can benefit by unilaterally changing their strategy, given what the others are doing. However, in sequential games (represented by game trees), a standard NE can include **non-credible threats**—promises to act irrationally in the future to influence an opponent's behavior today. **Subgame Perfect Equilibrium (SPE)**, a refinement concept introduced by Reinhard Selten, eliminates these incredible threats by requiring that players' strategies form a Nash Equilibrium in *every* subgame of the original game, not just the overall game. For finite horizon games, the primary tool for finding all SPE is **Backward Induction**.

## 2. Core Concepts

### Subgame
A **subgame** is any part of a sequential game that:
1.  **Starts at a single decision node.**
2.  **Contains all subsequent nodes** following that starting point.
3.  **Does not break information sets** (i.e., if an information set is entered, all nodes within that set must be included). This is crucial for games with imperfect information.

### Subgame Perfect Equilibrium (SPE)
A strategy profile (a complete plan of action for each player) is a **Subgame Perfect Equilibrium** if it constitutes a Nash Equilibrium in every subgame of the original game. This ensures that every player's strategy is optimal not only for the start of the game but for any point at which they might find themselves.

### Backward Induction
**Backward Induction** is the algorithm used to solve for SPE in finite sequential games of perfect information. The process is intuitive and mechanical:
1.  **Start at the end:** Identify the final decision nodes in the game (the "leaves" of the game tree).
2.  **Determine the optimal move:** At each of these final nodes, determine what action the player whose turn it is would choose. Essentially, you are solving the smallest possible subgames first.
3.  **Move backward:** Replace these final decision nodes with the payoffs that would result from the optimal play you just found. This effectively "prunes" the tree.
4.  **Repeat:** Continue this process, moving backward step-by-step to the root of the game tree. The path that remains after this pruning is the SPE.

## 3. Example: A Simple Two-Stage Game

Consider a game between two firms, A and B, deciding whether to enter a market.
*   **Stage 1:** Firm A chooses to `Enter` the market or `Stay Out`.
*   **Stage 2:** If Firm A enters, Firm B then chooses to `Fight` (e.g., start a price war) or `Acquiesce` (e.g., share the market).

The payoff tree is as follows (values represent profit in millions):
*   If A stays out: A gets `1`, B gets `5`.
*   If A enters and B fights: A gets `-1`, B gets `2`.
*   If A enters and B acquiesces: A gets `3`, B gets `3`.

Let's find the SPE using Backward Induction.

**Step 1: Start at the final decision node.**
This is Firm B's node after A has entered. B has a choice: `Fight` for a payoff of `2` or `Acquiesce` for a payoff of `3`. Since `3 > 2`, B's rational choice is to `Acquiesce`.

**Step 2: Move backward and prune the tree.**
We now replace the entire subgame starting from B's decision node with the payoff that results from B's optimal action: `(3, 3)`.

**Step 3: Solve the previous stage.**
Firm A now faces a choice at the initial node:
*   Choose `Stay Out` and get a payoff of `1`.
*   Choose `Enter`, which we now know leads to the pruned payoff of `3`.

Since `3 > 1`, A's rational choice is to `Enter`.

**The Subgame Perfect Equilibrium:**
*   **Firm A's Strategy:** `Enter`.
*   **Firm B's Strategy:** `Acquiesce if A enters`. (Note: The "if A enters" part is critical; it specifies the action for that specific subgame).

The SPE outcome is `(Enter, Acquiesce)` with payoffs `(3, 3)`. A standard NE might also include the non-credible threat where B promises to `Fight`, scaring A into `Staying Out` for a payoff of `(1, 5)`. However, this is not subgame perfect because in the subgame after A enters, fighting (`2`) is not optimal for B compared to acquiescing (`3`). Backward Induction eliminates this irrational threat.

## 4. Key Points & Summary

*   **Purpose:** Subgame Perfect Equilibrium (SPE) refines Nash Equilibrium by eliminating strategies that rely on non-credible threats, demanding rationality at every point in the game.
*   **Tool:** For finite games of perfect information, **Backward Induction** is the definitive method for finding all SPE.
*   **Process:** The algorithm works from the end of the game backwards to the beginning, solving each subgame optimally and using that solution to simplify the previous decision.
*   **Strategy Profile:** An SPE is a complete plan of action. It must specify what a player will do in every subgame where it is their turn to move, even if those subgames are not reached in the final equilibrium path.
*   **Credibility:** SPE ensures that all threats and promises within the equilibrium strategy are credible because they are optimal responses when the time comes.

**In essence, backward induction formalizes the idea of thinking ahead and reasoning backward, providing a powerful solution concept for sequential decision-making.**