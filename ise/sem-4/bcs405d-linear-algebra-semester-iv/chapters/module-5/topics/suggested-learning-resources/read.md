python
from scipy.optimize import linprog

# Coefficients of the Objective Function (to MINIMIZE).

# To maximize, we minimize the negative.

c = [-3, -5] # Represents: Minimize -Z = -3x1 -5x2

# Coefficients of the Inequality Constraints (LHS)

A_ub = [[1, 0],   [0, 2],   [3, 2]]
b_ub = [4, 12, 18] # RHS

# Bounds for variables (x1 >=0, x2>=0 is default)

res = linprog(c, A_ub=A_ub, b_ub=b_ub, method='highs')

print(res)

# The output will give you the optimal x1, x2, and the max Z (=-fun)
