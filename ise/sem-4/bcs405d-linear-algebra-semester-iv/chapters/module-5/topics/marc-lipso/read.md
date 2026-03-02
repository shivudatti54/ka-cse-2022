Of course. Here is a comprehensive educational note on the topic, tailored for  Engineering students.

### **Module 5: Optimization Techniques in Linear Algebra - Markowitz Portfolio Optimization (MVO)**

**Subject:** Linear Algebra | **Semester:** IV

---

#### **1. Introduction**

In the world of finance and investment, a fundamental challenge is to maximize returns while minimizing risk. This is an optimization problem at its core. Harry Markowitz, in the 1950s, pioneered a mathematical framework for this called **Modern Portfolio Theory (MPT)**, for which he won the Nobel Prize. At the heart of MPT lies a powerful application of linear algebra: using vectors and matrices to model a portfolio and optimize its risk-return profile. This technique is a cornerstone of quantitative finance and a brilliant example of applying linear algebra to solve real-world engineering problems in economics.

#### **2. Core Concepts Explained**

The Markowitz model makes a few key assumptions:

1.  Investors are rational and risk-averse.
2.  Returns on assets are normally distributed.
3.  An investment's risk is quantified by the variance (or standard deviation) of its returns.

The goal is to construct an **"efficient portfolio"** – one that offers the highest expected return for a given level of risk, or the lowest risk for a given expected return.

**The Mathematical Setup (Using Linear Algebra):**

Let’s assume we have `n` different assets to invest in.

1.  **Portfolio Weights Vector (`w`):**
    This is a column vector that defines the fraction of our total capital invested in each asset.
    `w = [w₁, w₂, ..., wₙ]ᵀ`
    The weights must sum to 1: `w₁ + w₂ + ... + wₙ = 1` (This can be written as **uᵀw = 1**, where **u** is a unit vector of all 1s).

2.  **Expected Returns Vector (`R`):**
    This is a column vector containing the historical average (or expected future) return for each asset.
    `R = [R₁, R₂, ..., Rₙ]ᵀ`

3.  **Covariance Matrix (`Σ`):**
    This is the most crucial linear algebra component. It's an `n x n` symmetric matrix where:
    - The diagonal element `Σᵢᵢ` is the **variance** of the returns for asset `i`. Variance measures an asset's own risk.
    - The off-diagonal element `Σᵢⱼ` is the **covariance** between the returns of asset `i` and asset `j`. Covariance measures how two assets move together. A positive covariance means they tend to move in the same direction, while a negative covariance means they tend to move in opposite directions (which is good for diversification).

**The Optimization Problem:**

We now define our two key objectives in terms of these vectors and matrices:

- **Portfolio Expected Return (`μₚ`):**
  This is a simple linear combination (dot product) of the weights and returns.
  `μₚ = w₁R₁ + w₂R₂ + ... + wₙRₙ = wᵀR`

- **Portfolio Variance (`σₚ²`) - The Risk:**
  This is a quadratic form involving the weights and the covariance matrix.
  `σₚ² = wᵀΣw`
  Expanding this shows how it accounts for the variance of each asset and the covariance between every pair of assets.

The optimization problem can be formulated in two ways:

1.  **Minimize Risk for a Target Return (`Rₜ`):**
    Minimize `σₚ² = wᵀΣw`
    Subject to: `wᵀR = Rₜ` and `uᵀw = 1`

2.  **Maximize Return for a Given Risk Level:**
    Maximize `μₚ = wᵀR`
    Subject to: `wᵀΣw = σₜ²` and `uᵀw = 1`

These are **quadratic optimization problems** with linear constraints, perfectly suited for solving using Lagrange multipliers, which ultimately leads to solving a system of linear equations.

#### **3. A Simplified Example**

Imagine a portfolio with just two assets (Apple and Tesla).

- **Expected Returns Vector:** `R = [0.10, 0.15]ᵀ` (Apple: 10%, Tesla: 15%)
- **Covariance Matrix:** `Σ = [[0.04, 0.02], [0.02, 0.09]]`
  (Apple variance: 0.04, Tesla variance: 0.09, Covariance: 0.02)
- **Portfolio Weights:** `w = [w₁, w₂]ᵀ` where `w₂ = 1 - w₁`

Let's calculate the portfolio risk and return if we invest 60% in Apple and 40% in Tesla (`w = [0.6, 0.4]ᵀ`).

1.  **Expected Return (`μₚ`):**
    `μₚ = wᵀR = [0.6 0.4] * [0.10, 0.15]ᵀ = (0.6)(0.10) + (0.4)(0.15) = 0.06 + 0.06 = 0.12` or **12%**

2.  **Portfolio Variance (`σₚ²`):**
    `σₚ² = wᵀΣw = [0.6 0.4] * [[0.04, 0.02], [0.02, 0.09]] * [0.6, 0.4]ᵀ`
    First, compute `Σw`:
    `[[0.04, 0.02], * [0.6, = [(0.04)(0.6) + (0.02)(0.4), = [0.024 + 0.008, = [0.032,
 [0.02, 0.09]]   0.4]ᵀ    (0.02)(0.6) + (0.09)(0.4)]    0.012 + 0.036]    0.048]`
    Now, compute `wᵀ(Σw)`:
    `[0.6 0.4] * [0.032, 0.048]ᵀ = (0.6)(0.032) + (0.4)(0.048) = 0.0192 + 0.0192 = 0.0384`
    The portfolio variance is `0.0384`, so the standard deviation (risk) is `√0.0384 ≈ 0.196` or **19.6%**.

The Markowitz model would allow us to find the precise weights (e.g., 70%/30%) that would give a lower risk for the same 12% return, or a higher return for the same 19.6% risk.

#### **4. Key Points & Summary**

- **Foundation:** Markowitz Portfolio Optimization uses linear algebra to mathematically formalize the trade-off between risk and return.
- **Key Components:** The model uses a **weight vector (w)**, an **expected return vector (R)**, and a **covariance matrix (Σ)**.
- **Portfolio Return:** Is a linear function (`μₚ = wᵀR`).
- **Portfolio Risk:** Is a quadratic function (`σₚ² = wᵀΣw`), making the overall problem a quadratic optimization.
- **Diversification:** The power of the model comes from the covariance terms. Assets with low or negative covariance can be combined to reduce overall portfolio risk below the risk of any single asset—this is the "free lunch" of diversification.
- **Output:** Solving the optimization problem for all possible target returns generates the **"Efficient Frontier,"** a curve representing the set of optimal portfolios.
- **Limitations:** The model relies on historical estimates for `R` and `Σ`, which are not always accurate predictors of the future. It also assumes normal distribution of returns, which isn't always true.
