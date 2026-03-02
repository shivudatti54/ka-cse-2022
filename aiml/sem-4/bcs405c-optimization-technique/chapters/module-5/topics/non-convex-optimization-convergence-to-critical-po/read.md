# **Non-Convex Optimization: Convergence to Critical Points**

## **Introduction**

Non-convex optimization is a field of optimization that deals with finding the minimum or maximum of a function subject to constraints when the objective function is non-convex. In this study material, we will explore the concept of convergence to critical points in non-convex optimization.

## **What is a Critical Point?**

A critical point of a function is a point where the gradient of the function is zero or undefined. In other words, it is a point where the function is neither increasing nor decreasing. Critical points can be local maxima, local minima, or saddle points.

## **Key Concepts**

- **Convexity**: A function is convex if its graph lies above any line segment connecting two points on the graph. A function is non-convex if its graph lies below some line segments.
- **Convergence**: Convergence refers to the process of finding a sequence of iterates that converges to a critical point.
- **Critical Point**: A point where the gradient of the function is zero or undefined.
- **Local Minimum**: A minimum value of a function in a neighborhood around a point.
- **Local Maximum**: A maximum value of a function in a neighborhood around a point.

## **Convergence to Critical Points**

Convergence to critical points is a fundamental concept in non-convex optimization. The goal is to find a sequence of iterates that converges to a critical point, which is either a local minimum, local maximum, or saddle point.

## **Types of Convergence**

- **Strong Convergence**: A sequence of iterates converges strongly to a critical point if the sequence converges to the critical point in the norm.
- **Weak Convergence**: A sequence of iterates converges weakly to a critical point if the sequence converges to the critical point in the weak sense.

## **Examples**

### Example 1: Non-Convex Optimization Problem

Consider the following non-convex optimization problem:

minimize f(x) = -x^2 - 5x - 3

subject to:

x >= 0

x <= 1

In this problem, the objective function f(x) = -x^2 - 5x - 3 is non-convex, and the constraints x >= 0 and x <= 1 restrict the feasible region.

### Example 2: Convergence to Critical Points

Consider the following sequence of iterates:

x\_{k+1} = x_k - \alpha \nabla f(x_k)

where \alpha is a step size, and \nabla f(x_k) is the gradient of the objective function at x_k.

If the sequence converges to a critical point, then the gradient of the objective function at the critical point is zero.

## **Challenges in Non-Convex Optimization**

Non-convex optimization is challenging due to the following reasons:

- **Lack of Convexity**: Non-convex functions can have multiple local minima, local maxima, or saddle points, making it difficult to find the global optimum.
- **Non-Convex Constraints**: Non-convex constraints can restrict the feasible region, making it difficult to find the optimal solution.
- **Non-Convex Objective Function**: Non-convex objective functions can be difficult to optimize, especially when the function is non-quadratic.

## **Conclusion**

Non-convex optimization is a challenging field of optimization that deals with finding the minimum or maximum of a non-convex function subject to constraints. Convergence to critical points is a fundamental concept in non-convex optimization, and understanding the types of convergence, examples, and challenges in non-convex optimization is crucial for solving non-convex optimization problems.
