# **RMSprop and Adam**

## **Overview**

- RMSprop and Adam are two popular optimization algorithms used in deep learning.
- They are variants of the Adagrad algorithm and are designed to address its main limitations.

## **Key Points**

- **RMSprop (Root Mean Square Propagation)**
  - Formula: `β = β * (1 - γ) + γ * (n * x^2)`
  - β: learning rate
  - γ: decay rate
  - n: number of iterations
  - x: gradient
- **Adam (Adaptive Moment Estimation)**
  - Formula: `m = β * m + (1 - β) * x`
  - m: first moment estimate
  - β: first moment decay rate
- **Key differences**
  - RMSprop adapts the learning rate for each parameter, while Adam adapts the learning rate for the entire model.
  - Adam uses two moment estimates (m and v) to control the adaptive learning rate.

## **Theorems and Definitions**

- **Adagrad Convergence Theorem**: Adagrad converges to the optimal solution as the number of iterations increases.
- **RMSprop convergence**: RMSprop converges to the optimal solution as the number of iterations increases.
- **moment estimation**: A sequence of averages of squared values of the gradient.

## **Advantages**

- **RMSprop**: adapts learning rate to each parameter, reduces the risk of exploding gradients.
- **Adam**: adapts learning rate to entire model, makes it more computationally efficient.

## **Disadvantages**

- **RMSprop**: can suffer from slow convergence.
- **Adam**: can suffer from non-convergence if the initial values of m and v are not properly initialized.
