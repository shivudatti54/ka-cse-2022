# Momentum-based Gradient Descent Methods: Adagrad

### Definition

- Adagrad (Adaptive Gradient) is a variant of gradient descent that adapts the learning rate for each parameter based on the magnitude of the gradient.
- It is a momentum-based gradient descent method that uses a history of past gradients to adjust the learning rate.

### Key Points

- **Adagrad Update Rule**:
  \[ \theta*t = \theta*{t-1} - \frac{\alpha_t}{\gamma_t} \Delta \theta_t \]
  where:

* $\theta_t$ is the updated parameter value
* $\alpha_t$ is the learning rate at time $t$
* $\gamma_t$ is the adaptive learning rate at time $t$
* $\Delta \theta_t$ is the gradient at time $t$

- **Adaptive Learning Rate**:
  \[ \gamma*t = \sqrt{\gamma*{t-1} + \frac{\alpha^2}{\epsilon}} \]
  where:

* $\epsilon$ is a small value to prevent division by zero

- **Momentum Term**:
  \[ v*t = \beta v*{t-1} + \alpha \Delta \theta_t \]
  where:

* $v_t$ is the momentum term at time $t$
* $\beta$ is the momentum coefficient

### Theorem

- The Adagrad update rule can be rewritten as:
  \[ \theta*t = \theta*{t-1} - \alpha \frac{\Delta \theta_t}{\gamma_t} \]
  This shows that the learning rate is adjusted based on the magnitude of the gradient.

### Key Formulas

- Adagrad Update Rule: $\theta_t = \theta_{t-1} - \frac{\alpha_t}{\gamma_t} \Delta \theta_t$
- Adaptive Learning Rate: $\gamma_t = \sqrt{\gamma_{t-1} + \frac{\alpha^2}{\epsilon}}$
- Momentum Term: $v_t = \beta v_{t-1} + \alpha \Delta \theta_t$

### Important Concepts

- Momentum-based gradient descent methods
- Adaptive learning rates
- Gradient descent optimization technique
