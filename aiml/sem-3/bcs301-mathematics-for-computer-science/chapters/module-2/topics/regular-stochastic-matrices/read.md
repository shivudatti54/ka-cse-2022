Of course. Here is a comprehensive educational note on Regular Stochastic Matrices, tailored for  Engineering students.

---

# **Regular Stochastic Matrices: A Key to Predicting Long-Term Behavior**

**Subject:** Mathematics for Computer Science
**Module:** Module 2: Joint Probability Distribution & Markov Chain
**Topic:** Regular Stochastic Matrices

## **1. Introduction**

In the study of Markov Chains, we are often interested in their **long-term behavior**. Will the system eventually settle into a stable state, regardless of where it started? This is a crucial question for modeling real-world processes like network traffic, game theory, or population genetics. **Regular Stochastic Matrices** are a special class of transition matrices that guarantee this stable, predictable long-term outcome. Understanding them is key to harnessing the predictive power of Markov Chains.

## **2. Core Concepts**

### **What is a Stochastic Matrix?**

First, a quick recap. A **Stochastic Matrix** (or probability matrix) is a square matrix `P` where:
1. Every entry `p_ij` is a probability, i.e., `0 ≤ p_ij ≤ 1`.
2. The sum of the entries in each row is 1. (Each row is a probability distribution).

**Example:**
$$
P = \begin{bmatrix}
0.7 & 0.3 \\
0.4 & 0.6 \\
\end{bmatrix}
$$
Row 1: `0.7 + 0.3 = 1`. Row 2: `0.4 + 0.6 = 1`. This is a stochastic matrix.

### **Defining a Regular Stochastic Matrix**

A stochastic matrix `P` is called **regular** if some power of `P` (i.e., `P^k` for some integer `k > 0`) has **only positive entries**. That is, every entry in `P^k` is strictly greater than zero.

**Why is this important?** This condition of having all positive entries in `P^k` means that it is possible to get from any state `i` to any state `j` in exactly `k` steps. This "interconnectedness" of all states is what leads to a unique long-term equilibrium.

### **The Fundamental Theorem of Regular Markov Chains**

If `P` is a regular stochastic matrix, then:
1. **Unique Stationary Vector:** There exists a unique probability vector `v` such that `vP = v`. This vector `v` is called the **steady-state** or **equilibrium** vector.
2. **Convergence:** As the number of steps `n` increases, the powers of the transition matrix `P^n` approach a fixed matrix `L`. Each row of this limiting matrix `L` is identical and equal to the steady-state vector `v`.
   $$ \lim_{n \to \infty} P^n = L = \begin{bmatrix} v \\ v \\ \vdots \\ v \end{bmatrix} $$
3. **Initial State Irrelevance:** Regardless of the initial state probability vector `u_0`, the state vector after `n` steps, `u_n = u_0 P^n`, will converge to the steady-state vector `v` as `n` becomes large.
   $$ \lim_{n \to \infty} u_0 P^n = v $$

## **3. Example**

Let's determine if the following stochastic matrix is regular and find its steady-state vector.

$$
P = \begin{bmatrix}
0 & 1 \\
0.5 & 0.5 \\
\end{bmatrix}
$$

**Step 1: Check for Regularity**
`P` itself has a zero entry. Let's compute `P²`:
$$
P^2 = P \times P = \begin{bmatrix}
(0)(0) + (1)(0.5) & (0)(1) + (1)(0.5) \\
(0.5)(0) + (0.5)(0.5) & (0.5)(1) + (0.5)(0.5) \\
\end{bmatrix} = \begin{bmatrix}
0.5 & 0.5 \\
0.25 & 0.75 \\
\end{bmatrix}
$$
Since `P²` has all positive entries, `P` is regular.

**Step 2: Find the Steady-State Vector `v`**
Let `v = [v1, v2]`. We know `vP = v` and `v1 + v2 = 1`.

$$
[v_1, v_2] \begin{bmatrix}
0 & 1 \\
0.5 & 0.5 \\
\end{bmatrix} = [v_1, v_2]
$$
This gives us the system of equations:
1. `v1*(0) + v2*(0.5) = v1`  =>  `0.5v2 = v1`
2. `v1*(1) + v2*(0.5) = v2`  =>  `v1 + 0.5v2 = v2`
From equation 1, we substitute `v1 = 0.5v2` into `v1 + v2 = 1`:
`0.5v2 + v2 = 1`  =>  `1.5v2 = 1`  =>  `v2 = 2/3`
Then, `v1 = 0.5 * (2/3) = 1/3`

So, the steady-state vector is `v = [1/3, 2/3]`. This means that in the long run, the system will spend approximately 1/3 of its time in state 1 and 2/3 of its time in state 2, regardless of the initial state.

## **4. Key Points & Summary**

| Key Point | Description |
| :--- | :--- |
| **Definition** | A stochastic matrix `P` is **regular** if some power `P^k` has **all positive entries** (no zeros). |
| **Implication** | Regularity ensures every state is eventually reachable from every other state. |
| **Long-Term Behavior** | Regular chains always converge to a unique **steady-state vector** `v`. |
| **Calculation** | Find `v` by solving the system `vP = v` with the constraint that the sum of `v`'s components is 1. |
| **Application** | Used to predict the stable, long-term distribution of a Markov system, which is invaluable for modeling and forecasting in computer science (e.g., queueing systems, PageRank algorithm). |

**In summary:** Regular stochastic matrices are the workhorses for predicting long-term behavior in Markov Chains. Their defining property guarantees a stable equilibrium, providing a powerful tool for analysis in countless engineering and computer science applications.