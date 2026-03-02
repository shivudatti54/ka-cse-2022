# RMSprop and Adam

### Overview

- RMSprop (Root Mean Squared Propagation) and Adam (Adaptive Moment Estimation) are popular optimization algorithms used for training deep neural networks.
- They address the vanishing and exploding gradient problems in traditional stochastic gradient descent (SGD) algorithms.

## RMSprop

### Key Points

- **Definition:** RMSprop is an optimization algorithm that adjusts the learning rate based on the magnitude of the gradient.
- **Formula:** `v_t = gamma * v_{t-1} + (1 - gamma) * gradient^2_t`
  - `v_t`: the exponentially weighted average of squared gradients.
  - `gamma`: a hyperparameter controlling the forgetting rate.
- **Update Rule:** `w_t = w_{t-1} - learning_rate * gradient_t / sqrt(v_t + epsilon)`
  - `w_t`: the updated model weights.
  - `epsilon`: a small value added to the denominator to prevent division by zero.

## Adam

### Key Points

- **Definition:** Adam is an optimization algorithm that adapts the learning rate for each parameter based on the magnitude of the gradient and the first and second moments of the gradient.
- **Formulas:**
  - `m_t = beta1 * m_{t-1} + (1 - beta1) * gradient_t`
    - `m_t`: the exponentially weighted average of the first moment of the gradient.
  - `v_t = beta2 * v_{t-1} + (1 - beta2) * gradient^2_t`
    - `v_t`: the exponentially weighted average of the second moment of the gradient.
  - `beta1` and `beta2`: hyperparameters controlling the forgetting rates.
  - `m_hat_t = m_t / (1 - beta1^t)`
  - `v_hat_t = v_t / (1 - beta2^t)`
  - `beta1^t` and `beta2^t`: exponentials of the beta parameters.
- **Update Rule:**
  - `w_t = w_{t-1} - learning_rate * m_hat_t / sqrt(v_hat_t + epsilon)`
  - `m_t` and `v_t`: the updated first and second moments of the gradient.

### Important Theorems

- RMSprop and Adam are both first-order optimization methods, meaning they only rely on the gradient of the loss function to update the model parameters.
- Both algorithms have been shown to be more effective than traditional SGD algorithms in training deep neural networks.

### Quick Revision Tips

- Remember that RMSprop and Adam are both optimization algorithms that address the vanishing and exploding gradient problems.
- Key formulas include `v_t` and `m_t` in RMSprop, and `m_t` and `v_t` in Adam.
- Important hyperparameters include `gamma`, `beta1`, and `beta2` in both algorithms.
