# **Statistical Machine Learning for Data Science: Chapter 3 & 4 Study Material**

## **Chapter 3: Multi-Arm Bandit Algorithms**

### Introduction

Multi-arm bandit algorithms are a type of reinforcement learning algorithm that can be used for decision-making in situations where there are multiple actions to choose from, and the goal is to optimize a reward function.

### Key Concepts

- **Bandit problem**: A bandit problem is a situation where an agent has to decide which action to take from a set of available actions, with the goal of maximizing a reward function.
- **Exploration-exploitation trade-off**: The exploration-exploitation trade-off is the tension between exploring different actions to gather more information and exploiting the knowledge gained to maximize the reward function.
- **Epsilon-greedy algorithm**: The epsilon-greedy algorithm is a popular algorithm for solving bandit problems, which chooses the action with the highest expected reward with probability (1 - epsilon) and chooses a random action with probability epsilon.

### Algorithms

- **Epsilon-greedy algorithm**: The epsilon-greedy algorithm works as follows:
  - Choose a random action with probability epsilon.
  - Choose the action with the highest expected reward with probability (1 - epsilon).
- **Upper confidence bound (UCB) algorithm**: The UCB algorithm works as follows:
  - Calculate the average reward for each action.
  - Add a bonus term to the average reward to account for the uncertainty in the reward.
  - Choose the action with the highest predicted reward.

### Example

Suppose we have a multi-arm bandit algorithm with three actions: A, B, and C. We want to maximize the reward function, which is:

    *   Action A: 10 + 2\*epsilon
    *   Action B: 5 + 3\*epsilon
    *   Action C: 8 + 4\*epsilon

where epsilon is a small positive value.

Using the epsilon-greedy algorithm, we would choose action A with probability (1 - epsilon) and a random action with probability epsilon. The UCB algorithm would choose action A with the highest predicted reward.

### Code

```python
import numpy as np

def epsilon_greedy(actions, rewards, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(actions)
    else:
        return np.argmax(rewards)

def ucb(actions, rewards, confidence_interval):
    avg_rewards = np.array(rewards) / len(actions)
    bonus_terms = confidence_interval * np.sqrt(np.log(len(actions)) / len(actions))
    predicted_rewards = avg_rewards + bonus_terms
    return np.argmax(predicted_rewards)

# Example usage:
actions = ['A', 'B', 'C']
rewards = [10 + 2*np.random.rand(), 5 + 3*np.random.rand(), 8 + 4*np.random.rand()]
epsilon = 0.1
confidence_interval = 1.0

print(epsilon_greedy(actions, rewards, epsilon))
print(ucb(actions, rewards, confidence_interval))
```

## **Chapter 4: Power and Sample Size Calculations**

### Introduction

Power and sample size calculations are used to determine the required sample size for a statistical analysis to detect a statistically significant effect.

### Key Concepts

- **Power**: Power is the probability that the analysis will detect a statistically significant effect if there is one.
- **Sample size**: Sample size is the number of participants or observations required to detect a statistically significant effect.

### Power Calculations

Power calculations involve estimating the effect size and the desired power level.

- **Effect size**: Effect size is a measure of the magnitude of the expected effect.
- **Desired power level**: Desired power level is the probability of detecting a statistically significant effect.

The formula for power calculation is:

    P = 1 - β

where P is the power and β is the probability of Type II error.

### Sample Size Calculations

Sample size calculations involve estimating the effect size and the desired power level.

- **Effect size**: Effect size is a measure of the magnitude of the expected effect.
- **Desired power level**: Desired power level is the probability of detecting a statistically significant effect.

The formula for sample size calculation is:

    n = (Z^2 * σ^2) / E^2

where n is the sample size, Z is the Z-score corresponding to the desired power level, σ is the standard deviation, and E is the effect size.

### Example

Suppose we want to detect a difference in the mean of two groups with a power level of 0.8 and an effect size of 0.5. We assume that the standard deviation is 1.0.

Using the power calculation formula, we get:

    P = 1 - β = 0.8
    β = 1 - P = 0.2

Using the sample size calculation formula, we get:

    n = (Z^2 * σ^2) / E^2
    n = (1.28^2 * 1.0^2) / 0.5^2
    n = 32.64

We round up to the nearest whole number to ensure that we have enough power.

### Code

```python
import numpy as np

def power(effect_size, alpha):
    beta = 1 - alpha
    power = 1 - beta
    return power

def sample_size(effect_size, power, alpha):
    z_score = np.sqrt((1 - power) / alpha)
    sample_size = (z_score**2 * 1.0**2) / effect_size**2
    return int(sample_size)

# Example usage:
effect_size = 0.5
power = 0.8
alpha = 0.05

print(power(effect_size, alpha))
print(sample_size(effect_size, power, alpha))
```

## **Interpreting Regression Results**

### Introduction

Interpreting regression results involves understanding the relationship between the independent variables and the dependent variable.

### Key Concepts

- **Coefficient**: Coefficient is a measure of the change in the dependent variable for a unit change in the independent variable.
- **Coefficient of determination**: Coefficient of determination is a measure of the proportion of variance in the dependent variable that is explained by the independent variables.

### Interpreting Coefficients

- **Positive coefficient**: Positive coefficient indicates that as the independent variable increases, the dependent variable also increases.
- **Negative coefficient**: Negative coefficient indicates that as the independent variable increases, the dependent variable decreases.
- **Zero coefficient**: Zero coefficient indicates that there is no linear relationship between the independent variable and the dependent variable.

### Interpreting Coefficient of Determination

- **High coefficient of determination**: High coefficient of determination indicates that the independent variables explain a large proportion of the variance in the dependent variable.
- **Low coefficient of determination**: Low coefficient of determination indicates that the independent variables explain a small proportion of the variance in the dependent variable.

### Example

Suppose we have a linear regression model with two independent variables: X1 and X2, and one dependent variable: Y.

| Coefficient | Interpretation                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------- |
| 0.5         | For every unit increase in X1, Y increases by 0.5 units.                                                             |
| -0.2        | For every unit increase in X2, Y decreases by 0.2 units.                                                             |
| 0.8         | The coefficient of determination is 0.8, indicating that the independent variables explain 80% of the variance in Y. |

### Code

```python
import numpy as np
import pandas as pd

def interpret_coefficients(coefficients, independent_variables, dependent_variable):
    interpretation = ""
    for coefficient, independent_variable in zip(coefficients, independent_variables):
        if coefficient > 0:
            interpretation += f"For every unit increase in {independent_variable}, {dependent_variable} increases by {coefficient} units. "
        elif coefficient < 0:
            interpretation += f"For every unit increase in {independent_variable}, {dependent_variable} decreases by {abs(coefficient)} units. "
        else:
            interpretation += f"There is no linear relationship between {independent_variable} and {dependent_variable}. "
    return interpretation

def interpret_coefficient_of_determination(coefficient_of_determination, variance):
    interpretation = ""
    if coefficient_of_determination > 0.7:
        interpretation += "The independent variables explain a large proportion of the variance in the dependent variable. "
    elif coefficient_of_determination < 0.3:
        interpretation += "The independent variables explain a small proportion of the variance in the dependent variable. "
    else:
        interpretation += "The independent variables explain a moderate proportion of the variance in the dependent variable. "
    return interpretation

# Example usage:
coefficients = [0.5, -0.2]
independent_variables = ["X1", "X2"]
dependent_variable = "Y"

print(interpret_coefficients(coefficients, independent_variables, dependent_variable))

coefficient_of_determination = 0.8
variance = 100

print(interpret_coefficient_of_determination(coefficient_of_determination, variance))
```
