Of course. Here is comprehensive educational content on Cournot’s Duopoly Game with Imperfect Information, tailored for  Engineering students.

# **Cournot’s Duopoly Game with Imperfect Information**

## **1. Introduction**

In Module 3, you studied Cournot's model under the assumption of **complete information**—where both firms know each other's cost functions, the market demand, and are fully rational. However, in real-world markets, this is often an idealized scenario. A firm might not know its competitor's production costs with certainty. This scenario, where players lack full knowledge of the characteristics or "types" of other players, is called a game of **imperfect information**.

This module extends the classic Cournot model to a more realistic setting where firms must make output decisions without knowing their rival's cost structure, turning it into a Bayesian game.

## **2. Core Concepts Explained**

### **The Bayesian Game Framework**

In a Bayesian game, we model the uncertainty about a player's characteristics. Here, a firm's "type" is defined by its cost function. For simplicity, we often consider two types: a **Low-Cost** firm and a **High-Cost** firm.

**Key Elements of the Model:**

1.  **Players:** Two firms, Firm 1 and Firm 2.
2.  **Actions:** The quantity each firm chooses to produce ($q_1$ and $q_2$).
3.  **Types:** Each firm has a private cost type. For instance:
    *   Firm 1's cost is known and common knowledge (e.g., $c_1$).
    *   Firm 2's cost is private. It can be either **High** ($c_H$) with probability $p$, or **Low** ($c_L$) with probability $(1-p)$, where $0 < p < 1$. Firm 2 knows its own type, but Firm 1 only knows the probability distribution.
4.  **Payoffs:** The profit for each firm remains a function of the total quantity supplied and its own cost:
    $$ \pi_i(q_i, q_j) = q_i \cdot (P(Q) - c_i) $$
    where $P(Q) = a - Q$ is the inverse market demand ($Q = q_1 + q_2$), and $a > c_i$.

### **Solving the Game: Bayes-Nash Equilibrium (BNE)**

The solution concept for a Bayesian game is the **Bayes-Nash Equilibrium (BNE)**. A BNE is a strategy profile where each player's strategy is optimal given their beliefs about the other players' types *and* the strategies those other types are expected to play.

**Solving Process (for the described scenario):**

1.  **Formulate Strategies:** Firm 1 chooses a single quantity $q_1^*$.
    Firm 2, knowing its own type, chooses a quantity for each possible type: $q_2^*(c_H)$ if its cost is high, and $q_2^*(c_L)$ if its cost is low.

2.  **Firm 1's Optimization:** Firm 1 does not know Firm 2's true cost. Therefore, it must maximize its **expected profit**, averaging over the possible types of Firm 2:
    $$ \max_{q_1} \mathbb{E}[\pi_1] = p \cdot \pi_1(q_1, q_2^*(c_H)) + (1-p) \cdot \pi_1(q_1, q_2^*(c_L)) $$
    Firm 1's best response depends on what it *believes* Firm 2 will produce, which depends on Firm 2's type.

3.  **Firm 2's Optimization (for each type):** Firm 2, knowing its own type (e.g., Low Cost), treats Firm 1's quantity $q_1^*$ as given and maximizes its own profit:
    $$ \max_{q_2} \pi_2(q_1^*, q_2; c_L) = q_2 \cdot (a - q_1^* - q_2 - c_L) $$
    This is identical to the standard Cournot best response function, but now specific to its cost type. The same is done for the high-cost type.

4.  **Find the Equilibrium:** The BNE is found by solving the system of equations simultaneously:
    *   Firm 1's reaction function (from its expected profit maximization).
    *   Firm 2's reaction function for its high-cost type.
    *   Firm 2's reaction function for its low-cost type.

This typically results in three equations that are solved for the three equilibrium quantities: $q_1^*$, $q_2^*(c_H)$, and $q_2^*(c_L)$.

### **Example Scenario**

Assume market demand: $P = 100 - (q_1 + q_2)$.
*   Firm 1's cost: $c_1 = 10$ (common knowledge).
*   Firm 2's cost: $c_2 = c_H = 20$ with probability $p=0.5$, or $c_2 = c_L = 5$ with probability $(1-p)=0.5$.

**In BNE:**
*   **Firm 2 (High-Cost):** Will produce less, as if in a standard Cournot duopoly against $q_1$ with $c_2=20$.
    Its best response: $q_2^{H} = \frac{100 - q_1 - 20}{2} = \frac{80 - q_1}{2}$.
*   **Firm 2 (Low-Cost):** Will produce more, as if with $c_2=5$.
    Its best response: $q_2^{L} = \frac{100 - q_1 - 5}{2} = \frac{95 - q_1}{2}$.
*   **Firm 1:** Maximizes its *expected* profit:
    $\mathbb{E}[\pi_1] = 0.5 \cdot [q_1(100 - q_1 - q_2^{H} - 10)] + 0.5 \cdot [q_1(100 - q_1 - q_2^{L} - 10)]$

Substituting the best responses of Firm 2 into this equation and solving for the profit-maximizing $q_1^*$ will yield the equilibrium quantity for Firm 1. Plugging $q_1^*$ back into Firm 2's best response functions gives the equilibrium outputs for both of Firm 2's types.

## **3. Key Points & Summary**

*   **Imperfect Information:** Models realistic markets where firms lack complete knowledge of their competitors' key characteristics, like production costs.
*   **Bayesian Game:** The appropriate framework for analyzing such games. Players have "types" (e.g., cost levels), and there is a common prior probability distribution over these types.
*   **Bayes-Nash Equilibrium (BNE):** The solution concept. Each player's strategy is optimal given their beliefs about others' types and the strategies those types are expected to use.
*   **Key Insight:** A firm must consider all possible types of its rival and weight its decisions based on the probability of each type. In our example:
    *   Firm 2 produces a different quantity depending on its actual cost.
    *   Firm 1 chooses a single quantity that is a best response to the *expected* output of Firm 2, which is an average of the high and low outputs.
*   **Comparison to Complete Information:** The outcome differs from a world where costs are known. Firm 1's output is generally between what it would produce if it knew Firm 2 was high-cost and what it would produce if it knew Firm 2 was low-cost.