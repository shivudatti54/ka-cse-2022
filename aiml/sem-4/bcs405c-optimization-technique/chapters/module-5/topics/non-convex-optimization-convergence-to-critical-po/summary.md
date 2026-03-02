# **Non-Convex Optimization: Convergence to Critical Points**

## **Definition**

- Non-convex optimization is a type of optimization problem where the objective function is not convex.
- Convergence to critical points is a fundamental concept in non-convex optimization.

## **Key Points**

- **Critical Points**: A critical point of a function is a point where the gradient is zero or undefined.
- **Local Minima**: A local minimum is a critical point where the function is not strictly smaller at any other point in the neighborhood.
- **Global Minima**: A global minimum is a critical point that is also the smallest value of the function over the entire domain.

## **Convergence Theorems**

- **Weierstrass Theorem**: Every continuous function on a compact set has a minimum value.
- **Karush-Kuhn-Tucker (KKT) Theorem**: A necessary condition for a point to be a local minimum (or maximum) of a convex function.

## **Non-Convex Optimization Formulations**

- **Subgradient Method**: An iterative method that uses a subgradient to update the solution.
- **Momentum Method**: An iterative method that uses a momentum term to escape local minima.

## **Important Formulas**

- **Subgradient**: A subgradient of a function at a point is a vector that is less than or equal to the gradient at that point.
- **Momentum Term**: A momentum term is added to the update rule to escape local minima.

## **Important Definitions**

- **Convex Set**: A set where the line segment between any two points is entirely contained within the set.
- **Non-Convex Set**: A set where the line segment between any two points is not entirely contained within the set.

## **Key Theorems**

- **Frank-Wolfe Theorem**: A necessary and sufficient condition for a point to be a local minimum (or maximum) of a convex function.
- **KKT Conditions**: A set of conditions that are necessary and sufficient for a point to be a local minimum (or maximum) of a convex function.
