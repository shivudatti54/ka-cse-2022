# **Backpropagation and Automatic Differentiation, Gradients in a Deep Network**

## **Key Points**

- **Backpropagation**: an optimization algorithm used for training deep neural networks
- **Automatic Differentiation**: a method to compute the gradients of a function with respect to its inputs without explicit differentiation
- **Gradients in a Deep Network**:
  - Compute the gradient of the loss function with respect to each weight using backpropagation
  - Use chain rule to propagate the gradients through the network
- **Gradient of Quadratic Cost**:
  - Define the quadratic cost function: `J(w) = 0.5 * ||w - w_true||^2`
  - Compute the gradient of J(w) with respect to w: `∂J/∂w = w - w_true`
- **Descending the Gradient of Cost**:
  - Update the weights using gradient descent: `w_new = w_old - learning_rate * ∂J/∂w`
- **The Gradient Descent Algorithm**:
  - Initialize weights and learning rate
  - Compute the gradient of the cost function with respect to each weight
  - Update the weights using gradient descent
  - Repeat until convergence or max iterations

## **Important Formulas and Definitions**

- **Backpropagation formula**: `∂J/∂w = σ(w) * (y - σ(w))`
- **Chain rule**: `∂/∂w ∫[f(x) * ∂/∂x] dx = ∫[∂/∂w f(x) * ∂/∂x] dx`
- **Quadratic cost function**: `J(w) = 0.5 * ||w - w_true||^2`

## **Theorems**

- **Gradient Descent Convergence Theorem**: under certain conditions, gradient descent converges to the optimal solution

## **Revision Tips**

- Review the backpropagation algorithm and its application in deep neural networks
- Practice computing gradients using automatic differentiation
- Understand the gradient descent algorithm and its convergence properties
