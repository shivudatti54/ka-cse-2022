# **Challenges in Neural Network Optimization**

**Key Concepts:**

- **Optimization Problem**: Finding the optimal weights and biases for a neural network to achieve the best possible performance on a given task.
- **Cost Function**: A mathematical function that measures the difference between the network's predictions and the actual output.
- **Gradient Descent**: An optimization algorithm used to minimize the cost function.

**Formulas and Definitions:**

- **Cost Function**: $J(w) = \frac{1}{2} \sum_{i=1}^{n} (y_i - \hat{y_i})^2$
- **Gradient Descent Update Rule**: $w \leftarrow w - \alpha \nabla J(w)$
- **Stochastic Gradient Descent**: $w \leftarrow w - \alpha \nabla J(w_k)$, where $w_k$ is the weight at iteration $k$

**Theorems:**

- **Convergence Theorem**: If the cost function is convex and the gradient descent update rule is used, then the algorithm will converge to the global minimum.
- **Optimality Criterion**: The minimum cost function value is reached when the gradient of the cost function with respect to the weights is zero.

**Common Challenges:**

- **Overfitting**: When the network is too complex and performs well on the training data but poorly on new, unseen data.
- **Underfitting**: When the network is too simple and fails to capture the underlying patterns in the data.
- **Vanishing Gradients**: When the gradients of the cost function with respect to the weights become very small, making it difficult for the algorithm to converge.
- **Exploding Gradients**: When the gradients of the cost function with respect to the weights become very large, causing the weights to update too quickly and potentially leading to instability.

**Important Hyperparameters:**

- **Learning Rate**: The step size of the gradient descent update rule.
- **Batch Size**: The number of samples used to compute the gradient of the cost function.
- **Number of Iterations**: The number of times the gradient descent update rule is applied.
