Of course. Here is a comprehensive educational module on Competitive Games, tailored for  Engineering students.

# Module 5: Competitive Games

**Course:** Algorithmic Game Theory
**Semester:** IV

---

### 1. Introduction to Competitive Games

In the previous modules, we explored how rational agents interact in scenarios with potential for cooperation. However, many real-world strategic interactions are purely **competitive** or **strictly adversarial**. In these situations, one agent's gain is directly and immediately another agent's loss. Algorithmic Game Theory provides a powerful, formal framework to model, analyze, and compute optimal strategies for such conflicts. These are known as **Competitive Games** or, more formally, **Two-Player Zero-Sum Games**.

This module will delve into the core concepts of these games, understand how to represent them, and learn the fundamental principle for determining optimal play: the **Minimax Theorem**.

### 2. Core Concepts Explained

#### 2.1. What is a Zero-Sum Game?

A zero-sum game is a type of strategic interaction between two players where the total payoff (or utility) is constant. Any gain for Player 1 must be matched by an equal loss for Player 2, and vice versa. The "sum" of the outcomes for both players is always **zero**.

*   **Formal Definition:** A two-player game is zero-sum if for every strategy profile (s₁, s₂), the utilities satisfy: **u₁(s₁, s₂) + u₂(s₁, s₂) = 0**.
*   **Implication:** The players' interests are diametrically opposed. There is no incentive for cooperation or coordination.

#### 2.2. The Normal Form (Matrix) Representation

The most intuitive way to represent a two-player zero-sum game is using a **payoff matrix**.

*   **Rows** represent the possible pure strategies of Player 1 (the row player).
*   **Columns** represent the possible pure strategies of Player 2 (the column player).
*   **Matrix Entry aᵢⱼ** represents the payoff that Player 1 receives if they choose strategy *i* and Player 2 chooses strategy *j*. Since the game is zero-sum, Player 2's payoff is simply **-aᵢⱼ**.

**Example: The Penalty Kick Game (Simplified)**
Consider a penalty kick in football. The kicker (Player 1) can shoot left or right. The goalkeeper (Player 2) can dive left or right. If the goalkeeper dives correctly, they save the shot (a win for the goalie, loss for the kicker). If they dive incorrectly, the kicker scores (a win for the kicker, loss for the goalie). We can assign a payoff of +1 to a score and -1 to a save. The matrix from the Kicker's perspective is:

| | **Goalie Dives Left** | **Goalie Dives Right** |
| :--- | :---: | :---: |
| **Kicker Shoots Left** | +1 | -1 |
| **Kicker Shoots Right** | -1 | +1 |

This is a classic zero-sum game.

#### 2.3. Strategies and Security Levels

In a adversarial environment, a rational player must consider the worst-case scenario. They assume their opponent is perfectly rational and will always choose the strategy that minimizes the player's payoff.

*   **Security Level (Value):** The maximum payoff a player can **guarantee** for themselves, regardless of the opponent's actions. It's the "best of the worst-case scenarios."
*   **For Player 1 (Maximizing Player):** They want to **maximize** their minimum payoff. They compute: **v₁ = max_{i} min_{j} aᵢⱼ**
*   **For Player 2 (Minimizing Player):** They want to **minimize** Player 1's maximum payoff. They compute: **v₂ = min_{j} max_{i} aᵢⱼ**

In the penalty kick example:
*   Player 1's security level: max( min(+1, -1), min(-1, +1) ) = max(-1, -1) = **-1**
*   Player 2's security level: min( max(+1, -1), max(-1, +1) ) = min(+1, +1) = **+1**

Notice that v₁ ≠ v₂. This leads to a fundamental question: can a player always guarantee a certain value?

#### 2.4. The Minimax Theorem and Mixed Strategies

The discrepancy above arises because we only considered **pure strategies** (deterministic choices). The cornerstone of competitive game theory is John von Neumann's **Minimax Theorem**.

*   **The Minimax Theorem:** *In any finite two-player zero-sum game, there exists a value V and **mixed strategies** for both players (probability distributions over pure strategies) such that:*
    *   *Player 1 can guarantee an expected payoff of **at least V** by using their optimal mixed strategy.*
    *   *Player 2 can guarantee that Player 1's expected payoff is **at most V** by using their optimal mixed strategy.*

This common value **V** is called the **value of the game**.

*   **Mixed Strategy:** A strategy where a player randomizes over their available pure actions according to a specific probability distribution. This introduces uncertainty, making it impossible for the opponent to predict and exploit a pattern.

**Revisiting the Penalty Kick with Mixed Strategies:**
If the Kicker shoots left with probability *p* and right with probability *(1-p)*, and the Goalie dives left with probability *q* and right with probability *(1-q)*, we can solve for the Nash Equilibrium (which, in zero-sum games, is the pair of minimax strategies).

The optimal strategy for both players, it turns out, is to choose left or right **completely randomly with 50% probability each**. The **value of the game V is 0**. The Kicker can expect to score 50% of the time, and the Goalie can expect to save 50% of the time. Neither can unilaterally deviate and get a better outcome.

### 3. Key Points & Summary

*   **Competitive (Zero-Sum) Games** model strictly adversarial interactions where one player's gain is the other's loss.
*   They are effectively represented using a **payoff matrix** from one player's perspective.
*   Using only pure strategies, players can often only guarantee a low security level due to the opponent's ability to counter.
*   The **Minimax Theorem** states that by using **mixed strategies** (randomization), there always exists an optimal way to play that allows each player to secure an **expected value V**.
*   Finding this optimal mixed strategy for each player is a solved problem (using Linear Programming) and is a fundamental problem in algorithms and AI for games like Poker, StarCraft, and other adversarial environments.