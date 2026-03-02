# Data Flow and Behavioural Model

=====================================

## Introduction

---

- Data flow models describe the flow of data through a system using diagrams.
- Behavioural models describe the expected behaviour of a system using equations.

## Data Flow Models

---

- **Data Flow Diagrams (DFDs):**
  - Used to model the flow of data through a system.
  - Consist of:
    - Pools: data stores
    - Processes: operations performed on data
    - Data Flows: data transferred between pools and processes
  - Types:
    - Level 0: input/output diagrams
    - Level 1: data flow diagrams
- **Flow-Matrix (or Flow-Chart):**
  - Used to model the flow of data through a system.
  - Consist of:
    - Rectangles: represent processes
    - Arrows: represent data flows
    - Labels: represent data names
  - Advantages:
    - Easy to understand
    - Can be used for both hardware and software design

## Behavioural Models

---

- **Equation-based models:**
  - Used to model the expected behaviour of a system using mathematical equations.
  - Consist of:
    - State equations: describe the state of the system
    - Transition equations: describe the transitions between states
- **State Machine Model:**
  - Used to model the expected behaviour of a system using finite state machines.
  - Consist of:
    - States: represent the current state of the system
    - Transitions: represent the transitions between states
    - Inputs: trigger transitions

## Important Formulas, Definitions, and Theorems

---

- **Karnaugh map:**
  - Used to simplify Boolean expressions
- **State equation:**
  - `q(n+1) = f(q(n), u(n))`
  - describes the state of the system at time `n+1` based on the previous state `q(n)` and input `u(n)`
- **Laplace transform:**
  - Used to solve differential equations
  - `F(s) = ∫[0∞) y(t)e^(-st)dt`
  - represents the Laplace transform of a signal `y(t)`

## Key Points

---

- Data flow models describe the flow of data through a system using diagrams.
- Behavioural models describe the expected behaviour of a system using equations.
- Key models include Data Flow Diagrams, Flow-Matrix, Equation-based models, and State Machine Model.
- Important formulas include Karnaugh map, State equation, and Laplace transform.
