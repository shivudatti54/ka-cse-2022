Of course. Here is an educational content piece on the "Likelihood Function Based on the State-Space Model" tailored for  engineering students.

***

### **Module 3: Likelihood Function Based on the State-Space Model**

#### **1. Introduction**
In the previous modules, you learned how State-Space Models (SSMs) provide a powerful framework for representing dynamic systems, where an unobserved **state vector** evolves over time and generates observable **measurements**. A critical challenge is estimating the unknown parameters (e.g., matrices **A**, **C**, **Q**, **R**) of this model from the observed data. The **Likelihood Function** is the cornerstone of this estimation process. It measures the probability of having observed our actual data, given a specific set of model parameters. Maximizing this likelihood leads to the most probable parameter estimates.

#### **2. Core Concepts Explained**

**a) The State-Space Model (Recap)**
Recall the standard linear Gaussian SSM:
*   **State Equation:** $\mathbf{x}_t = \mathbf{A}\mathbf{x}_{t-1} + \mathbf{w}_t$, where $\mathbf{w}_t \sim N(0, \mathbf{Q})$
*   **Measurement Equation:** $\mathbf{y}_t = \mathbf{C}\mathbf{x}_t + \mathbf{v}_t$, where $\mathbf{v}_t \sim N(0, \mathbf{R})$
Here, $\mathbf{x}_t$ is the hidden state, and $\mathbf{y}_t$ is the observation at time $t$.

**b) What is the Likelihood Function?**
For a set of observations $\mathbf{Y}_T = \\{\mathbf{y}_1, \mathbf{y}_2, ..., \mathbf{y}_T\\}$ and a parameter set $\mathbf{\theta}$ (which contains the elements of **A**, **C**, **Q**, **R**), the likelihood is the joint probability density of all observations:
$$ L(\mathbf{\theta} | \mathbf{Y}_T) = p(\mathbf{y}_1, \mathbf{y}_2, ..., \mathbf{y}_T; \mathbf{\theta}) $$

**c) The Challenge and the Solution: Prediction Error Decomposition**
Directly calculating this joint density is complex because observations are not independent; they are linked through the hidden state. The elegant solution is the **prediction error decomposition**.

The joint density can be factored into a product of conditional densities:
$$ p(\mathbf{y}_1, ..., \mathbf{y}_T; \mathbf{\theta}) = p(\mathbf{y}_1; \mathbf{\theta}) \prod_{t=2}^T p(\mathbf{y}_t | \mathbf{Y}_{t-1}; \mathbf{\theta}) $$
where $p(\mathbf{y}_t | \mathbf{Y}_{t-1}; \mathbf{\theta})$ is the density of $\mathbf{y}_t$ given all previous observations. This is where the Kalman Filter becomes essential.

**d) The Role of the Kalman Filter**
The Kalman Filter calculates the optimal one-step-ahead prediction of the state and, consequently, the observation.
1.  It provides the **predicted observation**: $\hat{\mathbf{y}}_{t|t-1} = \mathbf{C} \hat{\mathbf{x}}_{t|t-1}$.
2.  It provides the **prediction error** or **innovation**: $\boldsymbol{\nu}_t = \mathbf{y}_t - \hat{\mathbf{y}}_{t|t-1}$.
3.  Crucially, it provides the **covariance of this innovation**, $\mathbf{F}_t$**, which measures the uncertainty in the prediction.

**e) Constructing the Likelihood Function**
Under the Gaussian assumption, the conditional distribution $p(\mathbf{y}_t | \mathbf{Y}_{t-1}; \mathbf{\theta})$ is Gaussian with mean $\hat{\mathbf{y}}_{t|t-1}$ and covariance $\mathbf{F}_t$. Therefore, its density is:
$$ p(\mathbf{y}_t | \mathbf{Y}_{t-1}; \mathbf{\theta}) = \frac{1}{\sqrt{(2\pi)^m |\mathbf{F}_t|}} \exp\left(-\frac{1}{2} \boldsymbol{\nu}_t^\top \mathbf{F}_t^{-1} \boldsymbol{\nu}_t\right) $$
where $m$ is the dimension of $\mathbf{y}_t$.

The log-likelihood function (easier to maximize than the product form) becomes:
$$ \log L(\mathbf{\theta} | \mathbf{Y}_T) = -\frac{Tm}{2} \log(2\pi) - \frac{1}{2} \sum_{t=1}^T \left( \log |\mathbf{F}_t| + \boldsymbol{\nu}_t^\top \mathbf{F}_t^{-1} \boldsymbol{\nu}_t \right) $$

**The Kalman Filter is run for a given $\mathbf{\theta}$ to generate the sequence of innovations $\boldsymbol{\nu}_t$ and covariance matrices $\mathbf{F}_t$, which are then plugged into this formula to compute the log-likelihood value.**

#### **3. Example: Parameter Estimation**
Imagine a simple 1D system where you need to estimate the variance $R$ of the measurement noise.
1.  Guess a value for $R$.
2.  Run the Kalman Filter with this $R$ value. This will generate a sequence of scalars $\nu_t$ and $F_t$.
3.  Calculate the log-likelihood: $\log L(R) = c - \frac{1}{2} \sum_{t=1}^T \left( \log F_t + \frac{\nu_t^2}{F_t} \right)$ (where $c$ is a constant).
4.  Use an optimization algorithm (e.g., Newton-Raphson) to find the value of $R$ that *maximizes* $\log L(R)$. This is the **Maximum Likelihood Estimate (MLE)**.

#### **4. Key Points & Summary**

| Key Point | Description |
| :--- | :--- |
| **Objective** | To estimate unknown parameters $\mathbf{\theta}$ of a State-Space Model from observed data $\mathbf{Y}_T$. |
| **Core Idea** | Find the parameter values that make the observed data **most probable**. |
| **Primary Tool** | The **Kalman Filter** is used to compute the prediction errors ($\boldsymbol{\nu}_t$) and their covariances ($\mathbf{F}_t$). |
| **Mathematical Form** | The log-likelihood is $\log L(\mathbf{\theta}) = -\frac{1}{2} \sum_{t=1}^T \left( \log |\mathbf{F}_t| + \boldsymbol{\nu}_t^\top \mathbf{F}_t^{-1} \boldsymbol{\nu}_t \right) + constant$. |
| **Process** | An optimization algorithm iteratively proposes $\mathbf{\theta}$, for which the Kalman Filter computes the log-likelihood, until the maximum is found. |
| **Assumption** | The system and measurement noises are Gaussian. This is fundamental for the density function form. |