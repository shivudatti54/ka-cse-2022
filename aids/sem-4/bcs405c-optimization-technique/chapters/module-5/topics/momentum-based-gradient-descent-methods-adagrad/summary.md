# **Momentum-based Gradient Descent Methods: Adagrad**

## **Key Points**

- Adagrad is a momentum-based gradient descent method that adapts the learning rate for each parameter based on the gradient magnitude.
- It was introduced by John Hanin in 2002.
- Adagrad is an online optimization algorithm, meaning it updates the model parameters after each sample.
- The algorithm helps in avoiding the vanishing or exploding gradients.
- Adagrad uses the formula: $\theta_{t+1} = \theta_t - \alpha \frac{g_t}{g_t^2}$, where $\theta_{t+1}$ is the updated parameter, $\theta_t$ is the previous parameter, $\alpha$ is the learning rate, $g_t$ is the gradient at time $t$.

## **Definitions and Formulas**

- **Gradient**: The derivative of the loss function with respect to the model parameters.
- **Learning Rate**: The step size of each gradient update.
- **Momentum**: A hyperparameter that controls how much the algorithm uses the previous update to compute the next update.
- **Adagrad Update Formula**: $\theta_{t+1} = \theta_t - \alpha \frac{g_t}{g_t^2}$
- **Adagrad Reset Formula**: $\beta = \beta_{old} + \alpha \cdot g_t^2$, $\beta_{old} = 0$

## **Theorems**

- **Adagrad Convergence**: Adagrad converges to the optimal solution for convex loss functions.
- **Adagrad Stability**: Adagrad is stable for convex loss functions and has a bounded second moment.

## **Important Notes**

- Adagrad is sensitive to the choice of the initial value of the momentum.
- Adagrad can suffer from slow convergence in some cases.
- Adagrad is often used in combination with other optimization techniques, such as RMSProp and Adam.
