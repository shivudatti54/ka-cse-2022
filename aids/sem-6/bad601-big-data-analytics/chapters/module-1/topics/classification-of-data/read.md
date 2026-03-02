# Classification of Optimization Problems

## Introduction to Optimization Problem Classification

Optimization is the process of finding the best solution from all feasible solutions. To systematically approach optimization, we must first understand how to classify optimization problems. Proper classification helps us select appropriate solution methods and understand problem characteristics.

An optimization problem generally consists of:
- **Objective function**: The function to minimize or maximize
- **Decision variables**: Variables we can control
- **Constraints**: Restrictions on the decision variables

The general form is:
```
Minimize/Maximize: f(x)
Subject to: g_i(x) ≤ 0, i = 1, 2, ..., m
             h_j(x) = 0, j = 1, 2, ..., p
```

## Major Classification Categories

### 1. Based on Nature of Variables

#### Continuous Optimization
Variables can take any real value within specified ranges.

**Example**: Finding optimal dimensions for a container to minimize material usage:
```
Minimize: 2πr² + 2πrh
Subject to: πr²h ≥ 1000
            r > 0, h > 0
```

#### Discrete Optimization
Variables are restricted to discrete values (integers, binary choices).

**Example**: Knapsack problem - selecting items to maximize value without exceeding weight limit:
```
Maximize: Σ v_i*x_i
Subject to: Σ w_i*x_i ≤ W
            x_i ∈ {0, 1} for all i
```

#### Mixed Integer Optimization
Combination of continuous and discrete variables.

**Example**: Facility location problem with continuous production quantities and binary location decisions.

### 2. Based on Objective Function and Constraints

#### Linear Programming (LP)
Objective function and constraints are linear.

**Standard form**:
```
Minimize: c₁x₁ + c₂x₂ + ... + cₙxₙ
Subject to: a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ ≤ b₁
            a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ ≤ b₂
            ...
            x₁, x₂, ..., xₙ ≥ 0
```

#### Nonlinear Programming (NLP)
Objective function or constraints are nonlinear.

**Example**: 
```
Minimize: x₁² + x₂² + x₁x₂
Subject to: x₁ + x₂ ≥ 4
            x₁, x₂ ≥ 0
```

### 3. Based on Constraints

#### Constrained Optimization
Problems with explicit constraints on variables.

```
Minimize: f(x)
Subject to: g(x) ≤ 0
             h(x) = 0
```

#### Unconstrained Optimization
Problems without explicit constraints.

```
Minimize: f(x)
```

### 4. Based on Deterministic Nature

#### Deterministic Optimization
All parameters are known with certainty.

**Example**: Production planning with known demands and costs.

#### Stochastic Optimization
Some parameters are uncertain or probabilistic.

**Example**: Portfolio optimization with uncertain returns.

### 5. Based on Number of Objectives

#### Single-Objective Optimization
One objective function to optimize.

```
Minimize: f(x)
```

#### Multi-Objective Optimization
Multiple conflicting objectives to optimize simultaneously.

```
Minimize: [f₁(x), f₂(x), ..., fₖ(x)]
```

## Convex vs Non-Convex Optimization

### Convex Optimization
A convex optimization problem has:
- Convex objective function
- Convex feasible region (convex constraints)

**Mathematical definition**: A function f is convex if:
```
f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)
for all x, y in domain and λ ∈ [0, 1]
```

**Properties of convex problems**:
- Any local minimum is a global minimum
- Efficient algorithms available for solution
- Well-understood theoretical properties

**Example of convex function**: f(x) = x²

```
ASCII Diagram of Convex Function:

        /
       /
      /
_____/
```

### Non-Convex Optimization
Either the objective function or constraints are non-convex.

**Properties of non-convex problems**:
- Multiple local minima possible
- Harder to solve globally
- Often require specialized algorithms

**Example of non-convex function**: f(x) = sin(x)

```
ASCII Diagram of Non-Convex Function:

  /\    /\
 /  \  /  \
/    \/    \
```

**Comparison Table: Convex vs Non-Convex Problems**

| Characteristic | Convex Problems | Non-Convex Problems |
|----------------|-----------------|---------------------|
| Local optimum | Is global optimum | May not be global optimum |
| Solution difficulty | Generally easier | Generally harder |
| Algorithms | Gradient descent, LP, QP | Branch and bound, metaheuristics |
| Guarantees | Strong theoretical guarantees | Fewer guarantees |

## Global vs Local Optima

### Local Optimum
A point x* is a local minimum if:
```
f(x*) ≤ f(x) for all x in some neighborhood around x*
```

### Global Optimum
A point x** is a global minimum if:
```
f(x**) ≤ f(x) for all x in the feasible region
```

**Visual representation**:
```
ASCII Diagram of Local and Global Minima:

Global Minima      Local Minima
    ___               ___
   /   \             /   \
  /     \_         _/     \_
 /        \___ ___/         \
/                           \
```

**Characteristics of local and global optima**:

| Aspect | Local Optimum | Global Optimum |
|--------|---------------|----------------|
| Definition | Best in immediate neighborhood | Best in entire feasible region |
| Convex problems | Same as global | Same as local |
| Non-convex problems | Multiple may exist | Only one true optimum |
| Finding | Easier with gradient methods | Requires global search techniques |

## Problem Classification Flowchart

```
                            Start
                              |
                  +-----------v-----------+
                  | Optimization Problem |
                  +-----------+-----------+
                              |
          +-------------------+-------------------+
          |                                       |
  +-------v-------+                     +---------v---------+
  | Linear        |                     | Nonlinear         |
  | Objectives &  |                     | Objectives or     |
  | Constraints   |                     | Constraints       |
  +-------+-------+                     +---------+---------+
          |                                       |
  +-------v-------+                     +---------v---------+
  | Continuous    |                     | Check Convexity   |
  | Variables     |                     +---------+---------+
  +-------+-------+                               |
          |                           +-----------v-----------+
  +-------v-------+                   | Convex               | Non-convex
  | LP Methods    |                   | NLP                 | NLP
  | (Simplex, etc)|                   | (Gradient-based)    | (Global methods)
  +---------------+                   +---------------------+-----------------
```

## Examples of Different Problem Types

### Example 1: Linear Programming (Production Planning)
```
Maximize: 3x + 2y (profit)
Subject to: 2x + y ≤ 100 (labor hours)
            x + y ≤ 80 (machine hours)
            x, y ≥ 0
```

### Example 2: Nonlinear Programming (Engineering Design)
```
Minimize: πr²h (material cost)
Subject to: πr²h ≥ 1000 (volume requirement)
            h ≤ 2r (stability constraint)
            r, h > 0
```

### Example 3: Integer Programming (Scheduling)
```
Minimize: Σ c_ij x_ij
Subject to: Σ x_ij = 1 for all jobs i
            Σ x_ij = 1 for all machines j
            x_ij ∈ {0, 1}
```

## Importance of Proper Classification

1. **Algorithm selection**: Different problems require different solution methods
2. **Computational efficiency**: Some classifications lead to more efficient solutions
3. **Solution quality**: Understanding problem structure helps ensure optimal solutions
4. **Problem formulation**: Guides how we model real-world problems mathematically

## Exam Tips

1. **Identify problem type first**: Always begin by classifying the problem before attempting to solve it
2. **Look for linearity**: Check if objective and constraints are linear
3. **Check variable types**: Determine if variables are continuous, integer, or mixed
4. **Assess convexity**: For nonlinear problems, try to determine if the problem is convex
5. **Consider constraints**: Note whether the problem is constrained or unconstrained
6. **Multiple choice strategy**: Eliminate options based on problem classification characteristics
7. **Show your reasoning**: In written answers, explain how you classified the problem

**Common mistakes to avoid**:
- Assuming all optimization problems are convex
- Applying linear methods to nonlinear problems
- Ignoring integer constraints when they exist
- Confusing local and global optima in non-convex problems