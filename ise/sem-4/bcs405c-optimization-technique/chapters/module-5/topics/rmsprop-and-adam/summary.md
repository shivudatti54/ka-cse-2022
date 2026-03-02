# RMSprop and Adam Optimization Techniques

### Introduction

These two optimization techniques are widely used in deep learning for training neural networks.

### RMSprop Optimization

- **Definition:** RMSprop is an adaptive learning rate optimizer that adjusts the learning rate for each parameter based on the magnitude of the gradient.
- **Formula:** `l('= (1 - omega) * g^2 + omega * l')`, where `omega` is the decay rate, `g` is the gradient, and `l` is the previous squared gradient.
- **Key points:**
  - Uses a moving average of squared gradients to normalize the learning rate.
  - Helps escape local minima by adjusting the learning rate.
  - Requires a hyperparameter `omega` to control the decay rate.

### Adam Optimization

- **Definition:** Adam is an adaptive learning rate optimizer that combines the benefits of RMSprop and momentum.
- **Formula:** `m = beta1 * m + (1 - beta1) * g`, `v = beta2 * v + (1 - beta2) * g^2`, and `l = l * (1 - beta1) + m`, where `beta1` and `beta2` are hyperparameters, `m` is the moving average of the gradient, `v` is the moving average of the squared gradient, and `l` is the momentum.
- **Key points:**
  - Uses two hyperparameters `beta1` and `beta2` to control the adaptation rate.
  - Combines the benefits of RMSprop and momentum to improve convergence.
  - Helps escape local minima by adjusting the learning rate.

### Comparison

|                          | RMSprop   | Adam             |
| ------------------------ | --------- | ---------------- |
| Learning rate adaptation | Yes       | Yes              |
| Momentum                 | No        | Yes              |
| Hyperparameters          | 1 (omega) | 2 (beta1, beta2) |

### Theorems

- **Adam's Convergence Theorem:** Adam converges at least as fast as RMSprop under certain conditions.
- **RMSprop's Stability Theorem:** RMSprop is stable if the learning rate is below a certain threshold.

### Important Formulas

- `l = (1 - omega) * g^2 + omega * l`
- `m = beta1 * m + (1 - beta1) * g`
- `v = beta2 * v + (1 - beta2) * g^2`
- `l = l * (1 - beta1) + m`

Note: This summary is a concise revision guide and is not intended to be a comprehensive treatment of the topic.
