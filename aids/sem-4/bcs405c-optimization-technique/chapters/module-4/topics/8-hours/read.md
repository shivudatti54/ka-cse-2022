# **Convex Optimization-2: (8 hours)**

## **Introduction**

The topic of (8 hours) is a fundamental concept in Convex Optimization. It is an optimization technique used to find the minimum or maximum of a convex function subject to a set of constraints. In this study material, we will cover the definition, explanation, and examples of the (8 hours) technique.

## **Definition**

The (8 hours) technique is a method used to solve linear programming problems. It is also known as the Simplex Method or the North-West Corner Rule. The technique is used to find the optimal solution to a linear programming problem by iteratively adding or subtracting variables from the basic feasible solution.

## **Explanation**

The (8 hours) technique is based on the following steps:

1.  **Initialization**: The basic feasible solution is initialized with all variables set to zero.
2.  **Iteration**: The variable with the largest reduced cost is selected and added to the basic solution.
3.  **Subtraction**: The variable with the smallest reduced cost is subtracted from the basic solution.
4.  **Repeat**: Steps 2 and 3 are repeated until the optimal solution is reached.

## **Key Concepts**

- **Reduced Cost**: The reduced cost of a variable is the difference between its current value and the minimum value that can be achieved by reducing the variable to zero.
- **Basic Feasible Solution**: A basic feasible solution is a solution that satisfies all the constraints of the linear programming problem and has all variables in their basic (constant) values.
- **Optimal Solution**: The optimal solution is the solution that minimizes or maximizes the objective function.

## **Example**

Suppose we have a linear programming problem of the following form:

Minimize Z = 2x + 3y

Subject to:

x + y ≤ 10
2x + 3y ≤ 20
x, y ≥ 0

To solve this problem using the (8 hours) technique, we would follow the steps as follows:

1.  Initialize the basic feasible solution with all variables set to zero.
2.  Select the variable with the largest reduced cost, which is x in this case.
3.  Add x to the basic solution and set its value to 10.
4.  Subtract y from the basic solution and set its value to 0.
5.  Repeat steps 2 and 3 until the optimal solution is reached.

## **Code**

Here is an example of how to implement the (8 hours) technique in Python:

```python
import numpy as np

def simplex_method(c, A, b):
    n = len(c)
    m = len(A)
    m_plus_1 = m + 1
    s = np.zeros(m_plus_1)
    x = np.zeros(n)
    x[0] = b[0] / c[0]
    s[0] = 1
    d = np.zeros(m_plus_1)
    d[0] = -c[0]
    for i in range(1, m_plus_1):
        for j in range(m):
            d[i] += s[j] * A[j][i]
        i_j = np.argmax(d)
        if d[i_j] == 0:
            break
        s[i] = 1
        d[i] = -c[i]
        x[i] = b[i] / c[i]
        for j in range(m_plus_1):
            if j != i:
                s[j] -= s[i] * A[j][i]
                d[j] += c[i] * A[j][i]
        if i == m:
            break
    return x

c = np.array([2, 3])
A = np.array([[1, 1], [2, 3]])
b = np.array([10, 20])

x = simplex_method(c, A, b)
print(x)
```

## **Conclusion**

The (8 hours) technique is a fundamental concept in Convex Optimization that is used to find the minimum or maximum of a convex function subject to a set of constraints. The technique is based on the Simplex Method or the North-West Corner Rule and is used to solve linear programming problems. The key concepts of the (8 hours) technique include reduced cost, basic feasible solution, and optimal solution. The example code demonstrates how to implement the (8 hours) technique in Python.
