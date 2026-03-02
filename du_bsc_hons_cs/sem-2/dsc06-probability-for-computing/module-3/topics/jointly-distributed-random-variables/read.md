# Jointly Distributed Random Variables

## Introduction

In many real-world computing scenarios, we deal not with a single random variable in isolation but with multiple random variables simultaneously. Consider a web server where you want to analyze both the request arrival rate and the response time, or a machine learning model where features are correlated. **Jointly distributed random variables** provide the mathematical framework for studying two or more random variables defined on the same probability space, capturing their individual behaviors as well as their interdependencies.

The study of joint distributions is foundational to modern computing. From Bayesian inference in AI systems to performance modeling of distributed systems, from analyzing correlated failures in fault-tolerant computing to understanding feature dependencies in data science pipelines — joint distributions appear everywhere. Without this framework, we cannot reason about correlation, conditional behavior, or independence of multiple quantities, all of which are essential in algorithm design, probabilistic analysis, and statistical learning.

This topic builds upon your understanding of single random variables (discrete and continuous) and extends the machinery of probability mass functions, density functions, cumulative distribution functions, and expectation to the multivariate setting. We will cover joint PMFs and PDFs, marginal and conditional distributions, independence, covariance, and correlation — tools that form the backbone of probabilistic reasoning in computer science.

## Key Concepts

### 1. Joint Cumulative Distribution Function (Joint CDF)

For two random variables X and Y defined on the same sample space, the **joint CDF** is defined as:

$$F_{X,Y}(x, y) = P(X \leq x, Y \leq y)$$

**Properties of Joint CDF:**
- $F_{X,Y}(-\infty, y) = 0$, $F_{X,Y}(x, -\infty) = 0$
- $F_{X,Y}(\infty, \infty) = 1$
- $F_{X,Y}$ is non-decreasing in both arguments
- $F_{X,Y}$ is right-continuous in both arguments
- $P(a < X \leq b, c < Y \leq d) = F(b,d) - F(a,d) - F(b,c) + F(a,c)$

The marginal CDFs can be recovered as:
$$F_X(x) = F_{X,Y}(x, \infty), \quad F_Y(y) = F_{X,Y}(\infty, y)$$

### 2. Joint Probability Mass Function (Discrete Case)

When X and Y are both discrete random variables, their **joint PMF** is:

$$p_{X,Y}(x, y) = P(X = x, Y = y)$$

**Properties:**
- $p_{X,Y}(x, y) \geq 0$ for all $(x, y)$
- $\sum_{x} \sum_{y} p_{X,Y}(x, y) = 1$

The joint PMF is often displayed as a **probability table** where rows represent values of X, columns represent values of Y, and each cell contains $P(X = x, Y = y)$.

**Marginal PMFs** are obtained by summing over the other variable:
$$p_X(x) = \sum_{y} p_{X,Y}(x, y), \quad p_Y(y) = \sum_{x} p_{X,Y}(x, y)$$

### 3. Joint Probability Density Function (Continuous Case)

When X and Y are jointly continuous, their **joint PDF** $f_{X,Y}(x, y)$ satisfies:

$$P((X, Y) \in A) = \iint_A f_{X,Y}(x, y) \, dx \, dy$$

**Properties:**
- $f_{X,Y}(x, y) \geq 0$ for all $(x, y)$
- $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx \, dy = 1$

**Marginal PDFs:**
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy, \quad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx$$

**Computing probabilities over regions:**
$$P(X + Y \leq 1) = \iint_{x+y \leq 1} f_{X,Y}(x, y) \, dx \, dy$$

### 4. Conditional Distributions

**Discrete case:** The conditional PMF of Y given X = x is:
$$p_{Y|X}(y|x) = \frac{p_{X,Y}(x, y)}{p_X(x)}, \quad \text{provided } p_X(x) > 0$$

**Continuous case:** The conditional PDF of Y given X = x is:
$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)}, \quad \text{provided } f_X(x) > 0$$

Conditional distributions are crucial in computing, particularly in:
- **Bayesian classifiers:** Computing $P(\text{class} | \text{features})$
- **Markov chains:** Transition probabilities are conditional distributions
- **Conditional expectation:** $E[Y|X = x] = \sum_y y \cdot p_{Y|X}(y|x)$ or $\int y \cdot f_{Y|X}(y|x) \, dy$

### 5. Independence of Random Variables

Random variables X and Y are **independent** if and only if:

$$F_{X,Y}(x, y) = F_X(x) \cdot F_Y(y) \quad \text{for all } x, y$$

Equivalently:
- **Discrete:** $p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y)$ for all $x, y$
- **Continuous:** $f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y)$ for all $x, y$

**Quick test for independence:** If the joint PDF/PMF can be factored as $f_{X,Y}(x,y) = g(x) \cdot h(y)$ over a **rectangular region**, then X and Y are independent (and the marginals are proportional to $g$ and $h$). If the support region is non-rectangular (e.g., a triangle), the variables **cannot** be independent.

### 6. Covariance

The **covariance** of X and Y measures their linear association:

$$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$$

**Properties:**
- $\text{Cov}(X, X) = \text{Var}(X)$
- $\text{Cov}(X, Y) = \text{Cov}(Y, X)$
- $\text{Cov}(aX + b, cY + d) = ac \cdot \text{Cov}(X, Y)$
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$
- If X and Y are independent, then $\text{Cov}(X, Y) = 0$ (converse is **not** true in general)

**For joint expectation:**
$$E[XY] = \sum_x \sum_y xy \cdot p_{X,Y}(x,y) \quad \text{or} \quad \int \int xy \cdot f_{X,Y}(x,y) \, dx \, dy$$

### 7. Correlation Coefficient

The **Pearson correlation coefficient** normalizes covariance:

$$\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$$

**Properties:**
- $-1 \leq \rho_{X,Y} \leq 1$
- $|\rho| = 1$ if and only if $Y = aX + b$ for some constants (perfect linear relationship)
- $\rho = 0$ means X and Y are **uncorrelated** (not necessarily independent)

### 8. Functions of Jointly Distributed Random Variables

If $Z = g(X, Y)$, then:
$$E[Z] = E[g(X,Y)] = \sum_x \sum_y g(x,y) \cdot p_{X,Y}(x,y)$$

Important special cases:
- $E[X + Y] = E[X] + E[Y]$ (always, regardless of independence)
- $E[XY] = E[X] \cdot E[Y]$ only if X and Y are **uncorrelated**
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ only if X and Y are **uncorrelated**

## Examples

### Example 1: Discrete Joint Distribution — Network Packet Analysis

Two servers process requests. Let X be the number of packets dropped by Server A and Y be the number dropped by Server B. Their joint PMF is:

| | Y=0 | Y=1 | Y=2 |
|---|-----|-----|-----|
| **X=0** | 0.10 | 0.15 | 0.05 |
| **X=1** | 0.20 | 0.25 | 0.10 |
| **X=2** | 0.05 | 0.05 | 0.05 |

**(a) Find marginal PMFs.**

$p_X(0) = 0.10 + 0.15 + 0.05 = 0.30$
$p_X(1) = 0.20 + 0.25 + 0.10 = 0.55$
$p_X(2) = 0.05 + 0.05 + 0.05 = 0.15$

$p_Y(0) = 0.10 + 0.20 + 0.05 = 0.35$
$p_Y(1) = 0.15 + 0.25 + 0.05 = 0.45$
$p_Y(2) = 0.05 + 0.10 + 0.05 = 0.20$

**(b) Are X and Y independent?**

Check: $p_{X,Y}(0,0) = 0.10$ but $p_X(0) \cdot p_Y(0) = 0.30 \times 0.35 = 0.105 \neq 0.10$

**X and Y are NOT independent.** (One counterexample suffices.)

**(c) Find $P(Y = 1 | X = 1)$.**

$$p_{Y|X}(1|1) = \frac{p_{X,Y}(1, 1)}{p_X(1)} = \frac{0.25}{0.55} = \frac{5}{11} \approx 0.4545$$

**(d) Find $E[X]$, $E[Y]$, $E[XY]$, and $\text{Cov}(X,Y)$.**

$E[X] = 0(0.30) + 1(0.55) + 2(0.15) = 0.85$
$E[Y] = 0(0.35) + 1(0.45) + 2(0.20) = 0.85$

$E[XY] = \sum_x \sum_y xy \cdot p(x,y)$
$= 0 + 0 + 0 + 0 + 1(1)(0.25) + 1(2)(0.10) + 0 + 2(1)(0.05) + 2(2)(0.05)$
$= 0.25 + 0.20 + 0.10 + 0.20 = 0.75$

$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0.75 - (0.85)(0.85) = 0.75 - 0.7225 = 0.0275$

The positive covariance suggests that when Server A drops more packets, Server B tends to as well (possibly due to shared network congestion).

### Example 2: Continuous Joint Distribution

Let X and Y have joint PDF:

$$f_{X,Y}(x, y) = \begin{cases} 6(1-y) & 0 \leq x \leq y \leq 1 \\ 0 & \text{otherwise} \end{cases}$$

**(a) Verify this is a valid PDF.**

$$\int_0^1 \int_0^y 6(1-y) \, dx \, dy = \int_0^1 6(1-y) \cdot y \, dy = 6\int_0^1 (y - y^2) \, dy$$
$$= 6\left[\frac{y^2}{2} - \frac{y^3}{3}\right]_0^1 = 6\left(\frac{1}{2} - \frac{1}{3}\right) = 6 \cdot \frac{1}{6} = 1 \quad \checkmark$$

**(b) Find marginal PDFs.**

$$f_X(x) = \int_x^1 6(1-y) \, dy = 6\left[y - \frac{y^2}{2}\right]_x^1 \cdot (-1) \text{ ... let's compute carefully}$$
$$= 6\left[(1 - \frac{1}{2}) - (x - \frac{x^2}{2})\right] \cdot (-1)$$

Wait, let me recompute:
$$f_X(x) = \int_x^1 6(1-y) \, dy = 6\left[y - \frac{y^2}{2}\right]_x^1 = 6\left[\left(1 - \frac{1}{2}\right) - \left(x - \frac{x^2}{2}\right)\right] = 6\left[\frac{1}{2} - x + \frac{x^2}{2}\right]$$
$$= 3(1 - 2x + x^2) = 3(1-x)^2, \quad 0 \leq x \leq 1$$

$$f_Y(y) = \int_0^y 6(1-y) \, dx = 6(1-y) \cdot y = 6y(1-y), \quad 0 \leq y \leq 1$$

Note: $f_Y(y)$ is a Beta(2,2) distribution (up to constants).

**(c) Are X and Y independent?**

The support is the triangular region $\{0 \leq x \leq y \leq 1\}$, which is **not rectangular**. Therefore, **X and Y are NOT independent**.

Verification: $f_{X,Y}(x,y) = 6(1-y) \neq 3(1-x)^2 \cdot 6y(1-y) = f_X(x) \cdot f_Y(y)$.

**(d) Find $E[Y | X = 0.5]$.**

$$f_{Y|X}(y|0.5) = \frac{f_{X,Y}(0.5, y)}{f_X(0.5)} = \frac{6(1-y)}{3(1-0.5)^2} = \frac{6(1-y)}{3/4} = 8(1-y), \quad 0.5 \leq y \leq 1$$

$$E[Y|X=0.5] = \int_{0.5}^{1} y \cdot 8(1-y) \, dy = 8\int_{0.5}^{1} (y - y^2) \, dy$$
$$= 8\left[\frac{y^2}{2} - \frac{y^3}{3}\right]_{0.5}^{1} = 8\left[\left(\frac{1}{2} - \frac{1}{3}\right) - \left(\frac{1}{8} - \frac{1}{24}\right)\right] = 8\left[\frac{1}{6} - \frac{1}{12}\right] = 8 \cdot \frac{1}{12} = \frac{2}{3}$$

### Example 3: Computing Covariance and Correlation

Let X ~ Uniform(0,1) and $Y = X^2$. Find $\text{Cov}(X, Y)$ and $\rho_{X,Y}$.

**Step 1:** Compute required expectations.
- $E[X] = 1/2$
- $E[X^2] = 1/3$ → $\text{Var}(X) = 1/3 - 1/4 = 1/12$
- $E[Y] = E[X^2] = 1/3$
- $E[Y^2] = E[X^4] = \int_0^1 x^4 dx = 1/5$ → $\text{Var}(Y) = 1/5 - 1/9 = 4/45$
- $E[XY] = E[X \cdot X^2] = E[X^3] = \int_0^1 x^3 dx = 1/4$

**Step 2:** Covariance.
$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = \frac{1}{4} - \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{4} - \frac{1}{6} = \frac{1}{12}$$

**Step 3:** Correlation.
$$\rho_{X,Y} = \frac{1/12}{\sqrt{1/12} \cdot \sqrt{4/45}} = \frac{1/12}{\sqrt{4/540}} = \frac{1/12}{\sqrt{1/135}} = \frac{1/12}{1/\sqrt{135}}= \frac{\sqrt{135}}{12} = \frac{3\sqrt{15}}{12} = \frac{\sqrt{15}}{4} \approx 0.9682$$

**Key insight:** X and Y are clearly **not independent** (Y is a deterministic function of X), and $\rho \approx 0.968$ is high but not 1 because the relationship is **nonlinear**. Correlation only measures *linear* association.

## Exam Tips

1. **Always verify validity first:** When given a joint PDF/PMF, check that it integrates/sums to 1. This is a common first sub-question and easy marks.

2. **Non-rectangular support implies dependence:** If the region where $f_{X,Y}(x,y) > 0$ is triangular, circular, or any non-rectangular shape, X and Y **cannot** be independent. State this clearly in exams.

3. **Factorization shortcut for independence:** For rectangular support, if $f_{X,Y}(x,y) = g(x) \cdot h(y)$, then X and Y are independent. You don't even need to find the marginals explicitly.

4. **Remember the covariance shortcut:** $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$ is almost always easier to compute than the definition $E[(X-\mu_X)(Y-\mu_Y)]$.

5. **Uncorrelated ≠ Independent:** This is a favourite exam question. Zero covariance does NOT imply independence. Classic counterexample: X ~ Uniform(-1,1), Y = X². Then Cov(X,Y) = 0 but Y is completely determined by X.

6. **Limits of integration matter enormously:** In continuous joint distributions, carefully identify the region of support and set up integration limits correctly. Draw the region — this avoids most errors.

7. **Linearity of expectation always holds:** $E[X+Y] = E[X] + E[Y]$ regardless of dependence. But $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$ only when X and Y are uncorrelated. Don't confuse these.