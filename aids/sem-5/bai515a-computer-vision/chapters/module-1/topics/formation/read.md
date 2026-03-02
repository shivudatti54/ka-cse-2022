# Linear Programming Problem Formulation

## 1. Introduction to Linear Programming (LP)

Linear Programming (LP) is one of the most fundamental and widely used techniques in Operations Research and Optimization. It is a mathematical method for determining the best possible outcome (such as maximum profit or lowest cost) in a given mathematical model whose requirements are represented by **linear relationships**.

The core idea is to **optimize** (maximize or minimize) a linear function, called the **objective function**, subject to a set of linear **constraints**. These constraints are typically inequalities that define the limitations or requirements of the problem.

## 2. Key Components of an LP Problem

Every Linear Programming problem consists of three essential components:

1.  **Decision Variables**: These are the unknown quantities that we seek to determine. They represent the decisions to be made. They are usually denoted by symbols like $x_1, x_2, x_3, ..., x_n$ or $x, y, z$.
2.  **Objective Function**: This is a linear function of the decision variables that we want to either maximize (e.g., profit, revenue, efficiency) or minimize (e.g., cost, time, waste). It is expressed as:
    $Z = c_1x_1 + c_2x_2 + ... + c_nx_n$
    where $Z$ is the objective value, $c_i$ are coefficients (e.g., profit per unit), and $x_i$ are the decision variables.
3.  **Constraints**: These are the restrictions or limitations on the decision variables. They define the feasible region—the set of all possible solutions that satisfy the problem's conditions. Constraints are expressed as linear inequalities or equations:
    $a_{i1}x_1 + a_{i2}x_2 + ... + a_{in}x_n \leq b_i$ (or $\geq$ or $=$)
    where $a_{ij}$ are technological coefficients and $b_i$ are the right-hand side constants representing available resources or requirements.

Additionally, all LP problems assume **Non-negativity Constraints**. This means that decision variables cannot take negative values in most real-world contexts (e.g., you cannot produce a negative number of units).
$x_1, x_2, ..., x_n \geq 0$

## 3. Assumptions of Linear Programming

For a problem to be accurately modeled as an LP, it must satisfy the following key assumptions:

- **Proportionality**: The contribution of each decision variable to the objective function and constraints is directly proportional to its value. There are no economies or diseconomies of scale.
- **Additivity**: The total value of the objective function and the total resource usage are the sum of the individual contributions of each variable. There is no interaction between variables.
- **Divisibility**: Decision variables are allowed to take on any continuous, fractional value. This implies that solutions are not restricted to integers.
- **Certainty**: All parameters (coefficients $c_i$, $a_{ij}$, and $b_i$) are known constants with certainty. There is no probability or uncertainty involved.

## 4. Step-by-Step Guide to Formulating an LP Model

Formulating a real-world problem into an LP model is an art that requires practice. Follow these steps:

1.  **Understand the Problem**: Read the problem statement thoroughly. Identify what needs to be decided and what the goal is.
2.  **Identify Decision Variables**: Clearly define the symbols for your decision variables. Be specific about their units (e.g., $x_1$ = number of Product A manufactured per day).
3.  **Formulate the Objective Function**: Determine whether to maximize or minimize. Write an expression that calculates the total profit, cost, etc., based on the decision variables.
4.  **Formulate the Constraints**: Identify all the restrictions (limited resources, minimum requirements, contractual obligations, etc.). Translate each restriction into a linear inequality or equation using the decision variables.
5.  **Write Non-negativity Constraints**: Explicitly state that all decision variables are non-negative.

## 5. Example Formulations

### Example 1: The Product Mix Problem (Maximization)

**Problem Statement:** A company manufactures two products, X and Y. Each unit of Product X yields a profit of \$5, and each unit of Product Y yields \$8. Production requires time on two machines, M1 and M2.

- Product X requires 2 hours on M1 and 1 hour on M2.
- Product Y requires 1 hour on M1 and 3 hours on M2.
  The available machine time per day is 100 hours for M1 and 90 hours for M2. How many units of each product should be made daily to maximize profit?

**Formulation:**

1.  **Decision Variables:**
    Let $x$ = number of units of Product X to produce per day.
    Let $y$ = number of units of Product Y to produce per day.
2.  **Objective Function (Maximize Profit):**
    Maximize $Z = 5x + 8y$
3.  **Constraints:**
    - Machine M1 time constraint: $2x + 1y \leq 100$
    - Machine M2 time constraint: $1x + 3y \leq 90$
4.  **Non-negativity Constraints:**
    $x \geq 0, y \geq 0$

The complete LP model is:
Maximize $Z = 5x + 8y$
Subject to:
$2x + y \leq 100$
$x + 3y \leq 90$
$x, y \geq 0$

### Example 2: The Diet Problem (Minimization)

**Problem Statement:** A farmer wants to mix two types of feed, F1 and F2, for his livestock at minimum cost. Each pound of F1 costs \$0.50 and contains 3 units of nutrient A and 2 units of nutrient B. Each pound of F2 costs \$0.75 and contains 1 unit of nutrient A and 4 units of nutrient B. The daily diet requires at least 12 units of nutrient A and 16 units of nutrient B.

**Formulation:**

1.  **Decision Variables:**
    Let $x_1$ = pounds of Feed F1 to use daily.
    Let $x_2$ = pounds of Feed F2 to use daily.
2.  **Objective Function (Minimize Cost):**
    Minimize $Z = 0.5x_1 + 0.75x_2$
3.  **Constraints:**
    - Nutrient A requirement: $3x_1 + 1x_2 \geq 12$ (At least 12 units)
    - Nutrient B requirement: $2x_1 + 4x_2 \geq 16$ (At least 16 units)
4.  **Non-negativity Constraints:**
    $x_1 \geq 0, x_2 \geq 0$

The complete LP model is:
Minimize $Z = 0.5x_1 + 0.75x_2$
Subject to:
$3x_1 + x_2 \geq 12$
$2x_1 + 4x_2 \geq 16$
$x_1, x_2 \geq 0$

## 6. Common Pitfalls and How to Avoid Them

| Pitfall                           | Description                                                            | How to Avoid                                                                                    |
| :-------------------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **Incorrect Variable Definition** | Defining variables vaguely or with incorrect units.                    | Be precise. "Let $x$ be the number of..."                                                       |
| **Ignoring Non-negativity**       | Forgetting to state $x_i \geq 0$.                                      | Always make it the last step of your formulation.                                               |
| **Misinterpreting Constraints**   | Using $\leq$ when $\geq$ is needed, or vice versa.                     | Carefully read if it's a maximum limit ("cannot exceed") or a minimum requirement ("at least"). |
| **Overlooking Constraints**       | Missing a hidden constraint, like a balance or ratio constraint.       | List all resources, requirements, and logical conditions mentioned in the problem.              |
| **Linear Assumption Violation**   | Modeling a situation that isn't linear (e.g., fixed costs, discounts). | Verify that proportionality, additivity, and divisibility assumptions hold.                     |

## 7. Exam Tips

1.  **Read Carefully:** Underline key phrases like "maximize profit," "at least," "cannot exceed," and "available."
2.  **Define Variables First:** Always start by clearly defining your decision variables. This is the foundation.
3.  **Double-Check Units:** Ensure all terms in your objective function and constraints have consistent units (e.g., dollars, hours, pounds).
4.  **Verify Inequality Direction:** Before writing a constraint, ask: "Is this a $\leq$ (limit) or a $\geq$ (requirement) constraint?"
5.  **Practice, Practice, Practice:** Formulation is a skill. Work through as many different types of problems as possible (product mix, diet, blending, transportation, assignment).
6.  **Write the Final Model:** After formulating, neatly present the complete model: **Max/Min** [Objective Function] **subject to** [List of Constraints] and **Non-negativity Constraints**.
