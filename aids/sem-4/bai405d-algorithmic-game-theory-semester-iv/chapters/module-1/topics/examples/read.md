# Examples in Strategic Games

## Introduction

Game theory provides a mathematical framework for analyzing strategic interactions among rational decision-makers. In this topic, we examine concrete examples that illustrate how players choose strategies, how equilibria emerge, and how the theory of rational choice applies to real-world scenarios. These examples range from simple textbook games like Matching Pennies to more complex economic and social interactions. Understanding these examples is crucial because they form the foundation for analyzing sophisticated games in economics, political science, biology, and computer science.

The examples we study demonstrate fundamental concepts: dominant strategies, dominated strategies, Nash equilibrium, best responses, and the tension between individual rationality and collective welfare. By working through these examples systematically, students develop intuition for game-theoretic reasoning and learn to identify equilibrium outcomes in various strategic settings.

## Key Concepts

### The Battle of the Sexes

The Battle of the Sexes is a classic coordination game that illustrates how players with conflicting preferences can still achieve equilibrium. A couple must decide whether to attend a boxing match or a ballet. The husband prefers boxing, the wife prefers ballet, but both prefer going to the same event over going alone.

The payoff matrix shows: if both attend boxing, husband gets 3 and wife gets 1. If both attend ballet, husband gets 1 and wife gets 3. If they attend different events, both get 0. This game has two pure strategy Nash equilibria: (Boxing, Boxing) and (Ballet, Ballet). Additionally, there exists a mixed strategy Nash equilibrium where each player randomizes between their preferred and less-preferred option.

This example demonstrates that multiple equilibria can exist in a game, and coordination problems arise when players must select among several equilibrium outcomes.

### The Stag Hunt

The Stag Hunt, attributed to Jean-Jacques Rousseau, represents a risk-dominant versus payoff-dominant equilibrium conflict. Two hunters can either hunt a stag (which requires cooperation) or hunt a hare (which can be done individually). A stag provides greater reward but requires both hunters to cooperate. A hare provides smaller but guaranteed payoff.

The payoffs are: Stag-Stag yields (3, 3), Hare-Hare yields (2, 2), and asymmetric outcomes yield (0, 3) or (3, 0) depending on who gets the hare. Both (Stag, Stag) and (Hare, Hare) are Nash equilibria. This game illustrates how societies sometimes get trapped in inefficient equilibria (Hare-Hare) despite better options being available, a concept fundamental to understanding institutional design and social contracts.

### Chicken (Hawks and Doves)

The game of Chicken models aggressive confrontation where two players drive toward each other, and the first to swerve loses face. If both swerve, they share a small payoff. If one swerves and the other doesn't, the non-swerving player gets maximum payoff while the swerver gets nothing. If both refuse to swerve, the outcome is disastrous for both.

This zero-sum style game has two pure strategy equilibria: (Swerve, Don't Swerve) and (Don't Swerve, Swerve). The mixed strategy equilibrium involves each player randomly choosing to swerve with specific probabilities. Chicken games appear in arms races, traffic conflicts, and bargaining situations where commitment to aggressive behavior can be advantageous.

### Cournot Duopoly

The Cournot model analyzes strategic interaction between two firms producing homogeneous goods. Each firm simultaneously chooses output quantity, and market price depends on total supply. Given linear demand and constant marginal cost, each firm's best response is a linear function of the competitor's output.

In equilibrium, both firms produce half the monopoly output, resulting in higher prices than perfect competition but lower than monopoly. This example demonstrates how oligopolistic markets operate and provides insights into strategic decision-making in economic contexts.

### Bertrand Competition

In contrast to Cournot, Bertrand competition involves firms setting prices rather than quantities. With homogeneous products, consumers purchase from the cheapest seller. If prices differ, the lower-priced firm captures the entire market. If prices are equal, consumers are indifferent.

The unique Nash equilibrium is both firms setting price equal to marginal cost—the competitive outcome—despite only two firms existing. This surprising result highlights how strategic variable choice (prices versus quantities) dramatically affects equilibrium outcomes.

## Examples

### Example 1: Finding Nash Equilibrium in Battle of the Sexes

Consider the payoff matrix where row player (Husband) chooses between Boxing (B) and Ballet (A), column player (Wife) makes the same choice. Payoffs are (Husband, Wife):

- (B, B): (3, 1)
- (A, A): (1, 3)
- (B, A): (0, 0)
- (A, B): (0, 0)

Step 1: Identify each player's best response to opponent's strategies.
- If Wife chooses B, Husband's best response is B (3 > 0)
- If Wife chooses A, Husband's best response is A (1 > 0)
- If Husband chooses B, Wife's best response is B (1 > 0)
- If Husband chooses A, Wife's best response is A (3 > 0)

Step 2: Find strategy profiles where both players are playing best responses.
- (B, B): Husband's best response to B, Wife's best response to B ✓
- (A, A): Husband's best response to A, Wife's best response to A ✓

Step 3: Conclusion. Nash equilibria are (B, B) and (A, A).

### Example 2: Mixed Strategy Equilibrium in Matching Pennies

Row player wins if coins match (both heads or both tails); Column player wins if they differ.

Payoff matrix: Row wins (+1) or loses (-1)

- (H, H): (1, -1)
- (H, T): (-1, 1)
- (T, H): (-1, 1)
- (T, T): (1, -1)

Step 1: Check for pure strategy equilibria. No pure strategy profile is a mutual best response.

Step 2: Find mixed strategy equilibrium. Let Row play H with probability p and T with probability (1-p).

Row's expected payoff from Column playing H: p(1) + (1-p)(-1) = 2p - 1
Row's expected payoff from Column playing T: p(-1) + (1-p)(1) = 1 - 2p

For Column to be indifferent: 2p - 1 = 1 - 2p → 4p = 2 → p = 0.5

Similarly, let Column play H with probability q. Column's indifference condition yields q = 0.5.

Step 3: Conclusion. Both players randomize 50-50 between heads and tails.

### Example 3: Best Response Functions in Cournot Duopoly

Consider two firms with identical costs. Market demand: P = 30 - Q, where Q = q1 + q2. Both firms have zero marginal cost.

Step 1: Derive revenue and profit functions.
Firm 1's revenue: R1 = q1(30 - q1 - q2) = 30q1 - q1² - q1q2
Firm 1's profit: π1 = R1 (since cost = 0)

Step 2: Find best response function.
∂π1/∂q1 = 30 - 2q1 - q2 = 0 → q1* = 15 - q2/2

Step 3: By symmetry, Firm 2's best response: q2* = 15 - q1/2

Step 4: Solve for equilibrium.
Substitute: q1 = 15 - (15 - q1/2)/2 = 15 - 7.5 + q1/4 = 7.5 + q1/4
q1 - q1/4 = 7.5 → (3/4)q1 = 7.5 → q1 = 10
By symmetry, q2 = 10

Step 5: Verify equilibrium. Total output Q = 20, Price P = 10, Each firm earns profit π = 100.

## Exam Tips

1. Always check for dominated strategies first—if a strategy is always worse regardless of opponent's choice, eliminate it to simplify the game.

2. When finding Nash equilibrium, underline best responses in the payoff matrix to visually identify mutual best responses.

3. For mixed strategy equilibrium, use the indifference principle—opponents must be indifferent between their pure strategy options.

4. Remember that Nash equilibrium requires each player's strategy to be a best response to others' strategies, not to all possible strategies.

5. In symmetric games, look for symmetric equilibria where both players use identical strategies.

6. Distinguish between weak and strict Nash equilibria—weak equilibria involve indifference between strategies and may be less stable.

7. Practice converting payoff matrices into best response functions, as this skill is essential for continuous strategy games.

8. Understand that multiple equilibria require additional selection criteria (payoff dominance, risk dominance, focal points) beyond pure game theory.