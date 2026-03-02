# AND Search and AND-OR Graphs

## Overview

AND search extends traditional OR search to handle problem decomposition where solving a problem requires solving all of its subproblems. AND-OR graphs represent both choices (OR nodes) and mandatory decompositions (AND nodes), with the AO\* algorithm finding optimal solution graphs rather than simple paths.

## Key Points

- **OR Nodes**: Represent choices where only one successor needs to be solved, similar to standard search paths
- **AND Nodes**: Represent problem decompositions where all successors must be solved to solve the parent problem
- **Solution Graph**: A tree containing the start node where OR nodes include one successor and AND nodes include all successors
- **AO\* Algorithm**: Extends A\* to AND-OR graphs by iteratively expanding nodes and propagating cost estimates backward
- **Cost Computation**: AND node cost equals sum of all successor costs; OR node cost equals minimum of successor costs
- **SOLVED Marking**: An AND node is SOLVED when all children are SOLVED; an OR node is SOLVED when any child is SOLVED

## Important Concepts

- Problem reduction transforms complex problems into simpler subproblems that must all be solved
- Solution graphs represent complete solutions, not just single paths from start to goal
- Tower of Hanoi is a classic example of AND decomposition with recursive subproblems
- AO\* maintains admissibility and optimality when using admissible heuristics

## Notes

- Draw AND-node successors clearly with connecting arcs to distinguish from OR choices
- Remember the cost formulas: SUM for AND nodes, MIN for OR nodes
- Trace AO\* step-by-step showing expansion, cost revision, and SOLVED propagation
- AND search applies to theorem proving, planning, and any domain requiring complete subproblem solutions
