# **Non-Convex Optimization: Convergence to Critical Points**

## **Introduction**

Non-convex optimization is a branch of optimization that deals with finding the optimal solution to a mathematical problem when the objective function is not convex. In contrast to convex optimization, where the objective function is a convex function, in non-convex optimization, the objective function is a non-convex function. Non-convex optimization is widely used in many fields such as machine learning, computer vision, and engineering.

## **Definition of Convex and Non-Convex Functions**

- **Convex Function**: A function f(x) is said to be convex if for any two points x1 and x2 in the domain of f, and any λ in [0,1], the following inequality holds:

  f(λx1 + (1-λ)x2) ≤ λf(x1) + (1-λ)f(x2)

- **Non-Convex Function**: A function f(x) is said to be non-convex if the above inequality does not hold for all x1 and x2 in the domain of f, and all λ in [0,1].

## **Convergence to Critical Points**

In non-convex optimization, finding the critical points of the objective function is crucial. A critical point is a point where the gradient of the objective function is zero or undefined. Convergence to a critical point is the goal of many non-convex optimization algorithms.

## **Types of Convergence**

- **Local Convergence**: A method converges to a critical point within a certain neighborhood.
- **Global Convergence**: A method converges to a critical point regardless of the starting point.

## **Key Concepts**

- **Stationary Point**: A point where the gradient of the objective function is zero or undefined.
- **Critical Point**: A point where the gradient of the objective function is zero or undefined.
- **Saddle Point**: A point where the gradient of the objective function is undefined.
- **Local Minimum**: A point where the gradient of the objective function is zero, and the objective function is decreasing in all directions.
- **Global Minimum**: A point where the gradient of the objective function is zero, and the objective function is decreasing in all directions, regardless of the starting point.

## **Examples**

- **Binary Classification**: A binary classification problem is a non-convex optimization problem where the objective function is the cross-entropy loss function.

  f(x) = -[y*ln(p) + (1-y)*ln(1-p)]

  where x = [p, q] is the probability of positive class and y is the true label.

- **Generative Adversarial Networks (GANs)**: A GAN is a non-convex optimization problem where the objective function is the binary cross-entropy loss function.

  f(x) = -[log(1 - D(x)) + log(D(x))]

  where x is the input, D(x) is the output of the discriminator network, and y is the true label.

## **Non-Convex Optimization Algorithms**

- **Gradient Descent**: A first-order optimization algorithm that uses the gradient of the objective function to update the parameters.
- **Stochastic Gradient Descent**: A first-order optimization algorithm that uses the gradient of the objective function evaluated at a random point in the gradient descent direction.
- **Momentum**: A technique that adds a fraction of the previous gradient to the current gradient to help escape local minima.

## **Conclusion**

Non-convex optimization is a powerful technique for solving optimization problems where the objective function is not convex. Convergence to critical points is a crucial aspect of non-convex optimization, and there are many algorithms that can be used to achieve convergence. By understanding the key concepts and techniques of non-convex optimization, you can develop algorithms that can solve complex optimization problems.
