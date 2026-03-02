# Constraint Satisfaction Problems (CSP)

## Introduction

Constraint Satisfaction Problems (CSP) represent one of the most important paradigms in Artificial Intelligence for solving combinatorial problems. A CSP consists of a set of variables, each with a domain of possible values, and a set of constraints that specify allowable combinations of values. The goal is to find a complete assignment of values to all variables that satisfies all constraints.

CSPs appear extensively in real-world applications including scheduling (timetabling, airline crew scheduling), resource allocation, puzzle solving (Sudoku, crossword puzzles), scene interpretation, natural language processing, and planning. What makes CSPs particularly significant in AI is that many practical problems can be naturally formulated as CSPs, making it possible to apply general-purpose algorithms rather than developing custom solutions for each problem.

The study of CSPs is crucial for DU students because it introduces fundamental search and inference techniques that form the backbone of many AI systems. Unlike standard search problems where the goal is to find a path, CSPs require finding a state that satisfies all constraints simultaneously. This requires sophisticated techniques like backtracking, constraint propagation, and heuristic guidance, all of which are essential skills for any AI practitioner.

## Key Concepts

### Formal Definition of CSP

A Constraint Satisfaction Problem is defined as a triple (X, D, C) where:

- **X = {X₁, X₂, ..., Xₙ}** is a set of n variables
- **D = {D₁, D₂, ..., Dₙ}** is a set of domains, where Dᵢ is the set of possible values for variable Xᵢ
- **C = {C₁, C₂, ..., Cₘ}** is a set of constraints

Each constraint Cᵢ involves some subset of variables and specifies the allowable combinations of values. A **solution** is an assignment {X₁=v₁, X₂=v₂, ..., Xₙ=vₙ} where each vᵢ ∈ Dᵢ and all constraints are satisfied.

### Types of Constraints

**Unary Constraints** involve only a single variable. For example, "X ≠ 4" or "X > 0" are unary constraints that restrict the domain of a single variable.

**Binary Constraints** involve exactly two variables. For example, "X ≠ Y" or "X < Y" specify relationships between two variables. Binary CSPs, where all constraints are binary, are particularly important because any general CSP can be reduced to an equivalent binary CSP.

**Higher-Order Constraints** involve three or more variables. For example, "X + Y + Z = 10" or "All different(X, Y, Z, W)" (the Alldiff constraint, commonly used in puzzles like Sudoku).

**Global Constraints** are constraints that are defined over an arbitrary number of variables. The Alldiff constraint and the Sum constraint are examples of global constraints that frequently appear in practical CSPs.

### Constraint Graph Representation

The **constraint graph** is a crucial structure for understanding CSPs. Each variable becomes a node, and each binary constraint becomes an edge connecting the two variables involved. This graph structure is essential for understanding algorithms like arc consistency (AC-3) and for visualizing the problem's complexity.

The constraint graph's topology provides insights into problem difficulty. Problems with highly connected constraint graphs are typically harder to solve because any assignment affects many other variables through the constraint network.

### Backtracking Search

Backtracking is the fundamental algorithm for solving CSPs. It systematically explores the space of possible assignments:

1. Choose an unassigned variable
2. Order its domain values (try each value)
3. Check if the current partial assignment violates any constraints
4. If valid, recurse to assign the next variable
5. If contradiction reached, backtrack (undo assignment, try next value)

The basic backtracking algorithm has exponential worst-case complexity, but various enhancements can dramatically improve its performance.

### Constraint Propagation

Constraint propagation algorithms are inference techniques that prune the search space by eliminating values that cannot be part of any solution. The key idea is **local consistency** - making the problem locally consistent before or during search.

**Forward Checking** is a simple form of constraint propagation. After assigning a value to a variable, it removes incompatible values from the domains of unassigned neighboring variables. If any domain becomes empty, backtracking occurs immediately.

**Arc Consistency (AC-3)** is a more sophisticated algorithm. A constraint between variables X and Y is arc-consistent if for every value in X's domain, there exists some value in Y's domain that satisfies the constraint, and vice versa. AC-3 repeatedly enforces arc consistency until no more values can be removed. This algorithm has O(ed³) complexity where e is the number of arcs and d is the maximum domain size.

### Heuristics for Improved Search

Three critical heuristics significantly improve backtracking efficiency:

**Minimum Remaining Values (MRV) Heuristic**: Choose the variable with the fewest legal values remaining. This variable is most likely to cause failure early, saving computation time. Also called "most constrained variable" heuristic.

**Least Constraining Value Heuristic**: When choosing a value for a variable, prefer the value that rules out the fewest choices for neighboring variables. This leaves more flexibility for future assignments.

**Degree Heuristic**: Choose the variable that is involved in the largest number of constraints with other unassigned variables. This acts as a tie-breaker for MRV and helps reduce branching factor.

### Algorithm Recap: AC-3 (Arc Consistency-3)

```
function AC-3(csp):
    queue = all arcs (Xi, Xj) in csp
    while queue not empty:
        (Xi, Xj) = queue.pop()
        if Revise(csp, Xi, Xj):
            if DXi is empty:
                return false  // no solution possible
            for each Xk in Xi.neighbors - Xj:
                queue.push((Xk, Xi))
    return true

function Revise(csp, Xi, Xj):
    revised = false
    for each value x in DXi:
        if no value y in DXj satisfies constraint(Xi=x, Xj=y):
            remove x from DXi
            revised = true
    return revised
```

### Problem Variations

**Complete Solution**: Find one assignment satisfying all constraints.

**Flexible CSP**: Handle over-constrained problems where no complete solution exists. Techniques include constraint relaxation (removing less important constraints) or finding solutions that violate minimal constraints.

**Optimization CSP**: Among all solutions, find one that optimizes some objective function.

## Examples

### Example 1: Map Coloring Problem

**Problem**: Color the four countries (Australia, New Zealand, Japan, India) with three colors (Red, Green, Blue) such that no neighboring countries share the same color.

**Variables**: {Australia, NZ, Japan, India}
**Domains**: {Red, Green, Blue} for all variables
**Constraints**: Australia ≠ NZ, Australia ≠ Japan, India ≠ Japan

**Solution using Backtracking with MRV**:

1. All variables have 3 values. Choose Australia (degree = 2, highest connectivity).
2. Assign Australia = Red
3. Forward check: Remove Red from NZ and Japan domains.
   - NZ: {Green, Blue}
   - Japan: {Green, Blue}
   - India: {Red, Green, Blue}
4. Choose Japan (MRV: 2 values). Assign Japan = Green.
5. Forward check: Remove Green from India.
   - India: {Red, Blue}
6. Choose NZ (MRV: 2 values). Assign NZ = Green.
7. Constraint check: NZ and Australia already satisfy (Red ≠ Green). OK.
8. Choose India. Domain = {Red, Blue}. Both work.
9. **Solution found**: Australia=Red, Japan=Green, NZ=Green, India=Blue.

### Example 2: Sudoku (N-Queens Extension)

**Problem**: Standard 9×9 Sudoku has 81 variables (cells), each domain {1-9}. Constraints include:
- Row constraints: All different in each row
- Column constraints: All different in each column  
- 3×3 box constraints: All different in each subgrid

**Applying AC-3 for preprocessing**:

Consider row constraint between cells (1,1) and (1,2): For each value in cell (1,1), there must exist a different value in cell (1,2). AC-3 propagates constraints across the entire grid, significantly reducing domains before search begins. In practice, AC-3 alone can solve many Sudoku puzzles by reducing all domains to single values.

**Backtracking with MRV**: After AC-3, if multiple cells remain, select the cell with smallest domain (typically 2-3 values after propagation). This dramatically reduces search space.

### Example 3: Cryptarithmetic Puzzle (SEND + MORE = MONEY)

**Variables**: {S, E, N, D, M, O, R, Y}
**Domain**: {0, 9} for each variable (but leading letters S, M ≠ 0)

**Constraints**:
- AllDiff(S, E, N, D, M, O, R, Y)
- S*1000 + E*100 + N*10 + D + M*1000 + O*100 + R*10 + E = M*10000 + O*1000 + N*100 + E*10 + Y

**Applying MRV and AC-3**:
- M is most constrained (only 1-9), S also (1-9)
- Constraints propagate: column addition constraints create dependencies
- After arc consistency, domains shrink significantly
- Backtracking finds solution: S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2
- Verify: 9567 + 1085 = 10652

## Exam Tips

1. **Know the formal definition**: Be able to define CSP as a triple (X, D, C) and explain each component clearly in exams.

2. **Understand constraint types**: Differentiate between unary, binary, and higher-order constraints with examples. Know that binary CSPs can represent any CSP.

3. **Algorithm complexity**: Remember that basic backtracking is O(d^n) where d is domain size and n is variables. AC-3 is O(ed³).

4. **Heuristic purposes**: Know why MRV (choose variable with fewest values) reduces backtracking by failing early. Know why LCV (least constraining value) preserves flexibility.

5. **Forward checking vs AC-3**: Forward checking removes values from neighbors after each assignment. AC-3 ensures arc consistency more thoroughly before search begins.

6. **Constraint propagation benefits**: These techniques reduce search space dramatically and detect failure early without exhaustive search.

7. **Graph representation**: Draw constraint graphs for simple problems like map coloring. Understand how graph topology affects difficulty.

8. **Application areas**: Be ready to give examples of real-world CSP applications (scheduling, resource allocation, puzzles).

9. **Satisfiability**: Remember that CSPs are decision problems - determining if a solution exists. Optimization variants exist but are computationally harder.

10. **Alldiff constraint**: This global constraint is particularly important. Understand that enforcing arc consistency on Alldiff requires checking matching conditions.