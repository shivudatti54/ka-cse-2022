# Pure Equilibrium when Randomization is Allowed

### Introduction

In game theory, a pure equilibrium occurs when a player's strategy is a deterministic function of the other players' strategies. However, in many real-world situations, players are not always rational or have access to perfect information. This is where randomization comes in - a player may choose to randomize their strategy to make it harder for their opponents to predict their actions. But what happens when randomization is allowed in a strategic game? Does it still result in a pure equilibrium?

In this module, we will explore the concept of pure equilibrium when randomization is allowed. We will delve into the historical context, discuss the mathematical framework, and provide examples and case studies to illustrate the concept.

### Historical Context

The concept of randomization in game theory was first introduced by John Nash in the 1950s. Nash showed that even in deterministic games, players can randomize their strategies to achieve a Nash equilibrium. However, this was a one-time randomization, where the player would randomize their strategy only once.

In the 1960s and 1970s, game theorists like John Harsanyi and Reinhard Selten built upon Nash's work and introduced the concept of mixed-strategy Nash equilibria. A mixed-strategy Nash equilibrium is a stable state where no player can improve their expected payoff by unilaterally changing their strategy, assuming all other players keep their strategies unchanged. In this context, randomization plays a crucial role, as players can randomize their strategies to make it harder for their opponents to predict their actions.

### Mathematical Framework

Let's consider a simple game with two players, Player 1 and Player 2, and two possible actions for each player: Action 1 and Action 2. The game can be represented as follows:

|              | Action 2 | Action 1 |
| ------------ | -------- | -------- |
| **Action 1** | (1,1)    | (2,2)    |
| **Action 2** | (2,2)    | (1,1)    |

In this game, the payoff matrix is:

|                         | Player 2's Action | Player 2's Action |
| ----------------------- | ----------------- | ----------------- |
| **Player 1's Action 1** | 2                 | 1                 |
| **Player 1's Action 2** | 1                 | 2                 |

Player 1's expected payoff for Action 1 is 2*(1/2) + 1*(1/2) = 1.5, and Player 2's expected payoff for Action 1 is 2*(1/2) + 1*(1/2) = 1.5.

To find the pure equilibrium, we need to find the strategies that make Player 1's expected payoff equal to 1.

### Pure Equilibrium when Randomization is Allowed

When randomization is allowed, Player 1 can choose to randomize their strategy between Action 1 and Action 2. This changes the expected payoff for Player 1.

Let's say Player 1 randomizes their strategy with probability p (for Action 1) and (1-p) (for Action 2). The expected payoff for Player 1 is:

E(P1) = p*2 + (1-p)*1

To find the pure equilibrium, we need to find the probability p that makes Player 1's expected payoff equal to 1.

Solving for p, we get:

p = 1/3

Therefore, Player 1's optimal strategy is to randomize their action with probability 1/3 and action 1 with probability 2/3.

### Examples and Case Studies

1. **The Prisoner's Dilemma**: In this game, two prisoners have two possible actions: to confess or to remain silent. The payoff matrix is:

|                                         | Prisoner 2's Action | Prisoner 2's Action |
| --------------------------------------- | ------------------- | ------------------- |
| **Prisoner 1's Action - Confess**       | 0,0                 | 3,7                 |
| **Prisoner 1's Action - Remain Silent** | 3,7                 | 5,5                 |

When randomization is allowed, the prisoners can choose to randomize their actions. Let's say the first prisoner randomizes their action with probability p (for confessing) and (1-p) (for remaining silent). The expected payoff for the first prisoner is:

E(P1) = p*3 + (1-p)*5

To find the pure equilibrium, we need to find the probability p that makes the first prisoner's expected payoff equal to 0.

Solving for p, we get:

p = 1/2

Therefore, the first prisoner's optimal strategy is to randomize their action with probability 1/2 and confess with probability 1/2.

2. **The Ultimatum Game**: In this game, two players have two possible actions: to accept or to reject an offer. The payoff matrix is:

|                                | Player 2's Action | Player 2's Action |
| ------------------------------ | ----------------- | ----------------- |
| **Player 1's Action - Accept** | 0,0               | 5,0               |
| **Player 1's Action - Reject** | 0,0               | 0,0               |

When randomization is allowed, players can choose to randomize their actions. Let's say the first player randomizes their action with probability p (for accepting) and (1-p) (for rejecting). The expected payoff for the first player is:

E(P1) = p*5 + (1-p)*0

To find the pure equilibrium, we need to find the probability p that makes the first player's expected payoff equal to 1.

Solving for p, we get:

p = 1/2

Therefore, the first player's optimal strategy is to randomize their action with probability 1/2 and accept with probability 1/2.

### Applications

1. **Economics**: In economics, randomization can be used to model uncertainty in decision-making. For example, a firm may randomize its pricing strategy to account for uncertainty in demand.
2. **Biology**: In biology, randomization can be used to model the behavior of animals in a population. For example, a predator may randomize its hunting strategy to account for uncertainty in prey distribution.
3. **Finance**: In finance, randomization can be used to model risk in investment strategies. For example, a portfolio manager may randomize their investment allocation to account for uncertainty in market returns.

### Further Reading

- Nash, J. F. (1950). The problem of simultaneous action. Econometrica, 18(2), 155-162.
- Harsanyi, J. C. (1953). A concept of rational choice among many alternative behaviors. Econometrica, 21(2), 263-295.
- Selten, R. (1967). The strategy of anticipation. International Journal of Game Theory, 1(1), 81-117.
- Aumann, R. J. (1974). Subjective probability and expected utility. Econometrica, 42(1), 1-17.

In conclusion, the concept of pure equilibrium when randomization is allowed is a powerful tool in game theory. It allows players to model uncertainty in decision-making and can be used to analyze a wide range of strategic games. By considering the mathematical framework and providing examples and case studies, we have seen how randomization can be used to achieve a pure equilibrium in strategic games.
