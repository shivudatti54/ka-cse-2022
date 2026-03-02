# Nash Equilibrium Payoffs of an Infinitely Repeated Prisoner's Dilemma

## Definitions and Formulas

- **Infinitely Repeated Prisoner's Dilemma (IRPD):** A game-theoretic model where two players, A and B, make repeated decisions regarding cooperation or defection.
- **Nash Equilibrium:** A state where no player can improve their payoff by unilaterally changing their strategy, assuming the other player's strategy remains the same.
- **Payoff Matrix:**

```markdown
|                   | Cooperate (C) | Defect (D) |
| ----------------- | ------------- | ---------- |
| **Cooperate (C)** | (R, R)        | (T, P)     |
| **Defect (D)**    | (T, P)        | (S, S)     |
```

- Where:
  - R: Reward for cooperative player (e.g., 3 points)
  - T: Penalty for defector (e.g., 0 points)
  - P: Punishment for defector (e.g., 1 point)
  - S: Satisfaction for cooperative player (e.g., 2 points)

## Key Points

- **Perfect Bayesian Equilibrium:** A Nash equilibrium where players use Bayesian updating to learn the type of the other player.
- **Regret Minimization:** A strategy that minimizes the regret (difference between the ideal and actual payoffs).
- **Tit-for-Tat (TFT):** A strategy that imitates the other player's previous action, with randomization to avoid predictability.
- **Folk Theorem:** A theorem that states that a Nash equilibrium can be achieved in a repeated game, assuming rational behavior and infinite time.

## Important Theorems

- **Folk Theorem:** Establishes the existence of a Nash equilibrium in a repeated game.
- **Re iterations Theorem:** Shows that the Nash equilibrium of a repeated game can be iterated to achieve a stable equilibrium.

## Notes

- The infinitely repeated Prisoner's dilemma is a classic example of a repeated game, where players make repeated decisions to maximize their payoffs.
- The Nash equilibrium in this game is (D, D), where both players defect, resulting in a payoff of (T, P).
- The perfect Bayesian equilibrium and regret minimization strategies can lead to a more cooperative outcome, where both players cooperate.
- The Tit-for-Tat strategy is a popular approach in repeated games, as it balances cooperation and punishment.
