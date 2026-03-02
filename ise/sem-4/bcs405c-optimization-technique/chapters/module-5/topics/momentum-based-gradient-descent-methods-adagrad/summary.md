# **Momentum-based Gradient Descent Methods: Adagrad**

## **Key Points**

- **Definition:** Adagrad is a stochastic optimization algorithm that uses momentum to adapt the learning rate for each parameter.
- **Formula:** `m_t = γm_{t-1} + (1-γ)x_t^2`, `v_t = γv_{t-1} + x_t`, `λ_t = -λ_t - α \* v_t`
- **Variables:**
  - `x_t`: current parameter update
  - `m_t`: past updates (momentum)
  - `v_t`: past updates to momentum
  - `λ_t`: previous parameter update
  - `γ`: decay rate for momentum
  - `α`: learning rate
- **How it Works:**
  - Combines momentum and Adagrad updates to adapt the learning rate
  - Uses past updates to momentum to adapt the learning rate
  - Helps to escape the local minimum problem
- **Important Concepts:**
  - **Adagrad Update:** `λ_t = λ_{t-1} - α \* x_t^2`
  - **Momentum Update:** `m_t = γm_{t-1} + (1-γ)x_t^2`
  - **Exponential Moving Average (EMA):** used in Adagrad to calculate momentum

## **Mathematical Background**

- **Adagrad Update:**
  - `λ_t = λ_{t-1} - α \* x_t^2`
- **Momentum Update:**
  - `m_t = γm_{t-1} + (1-γ)x_t^2`
- **Adagrad Formula:**
  - `m_t = γm_{t-1} + (1-γ)x_t^2`, `v_t = γv_{t-1} + x_t`, `λ_t = -λ_t - α \* v_t`

## **Theorems and Definitions**

- **Adagrad Convergence Theorem:** `E[\sum_{t=1}^T (λ_t - λ^*)^2] ≤ (1-\frac{1}{2\gamma}) (E[\sum_{t=1}^T x_t^2])`
- **Adagrad Unboundedness Theorem:** `D^2 \sum_{t=1}^T (λ_t - λ^*)^2 ≤ \frac{1}{2\gamma} \sum_{t=1}^T (x_t^2)^2`
