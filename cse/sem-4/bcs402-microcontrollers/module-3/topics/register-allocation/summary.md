# Register Allocation - Summary

## Key Definitions

- **Register Allocation**: The compiler optimization that maps program variables to a limited number of hardware registers
- **Live Variable**: A variable whose current value will be used in some future computation before being redefined
- **Interference**: Two variables interfere if they are live at the same program point and cannot share a register
- **Interference Graph**: An undirected graph where vertices represent variables and edges represent interference between variables
- **Register Spilling**: The process of storing a variable's value to memory when insufficient registers are available
- **Caller-Saved Registers**: Registers that may be modified by a called function; caller must save them if needed
- **Callee-Saved Registers**: Registers that must be preserved across function calls by the callee

## Important Formulas

- **Live Variable Equations**:
  - LiveIn[p] = Use[p] ∪ (LiveOut[p] - Def[p])
  - LiveOut[p] = ∪ LiveIn[succ(p)]

- **Spill Cost**: SpillCost(v) = LoadCost(v) × Loads(v) + StoreCost(v) × Stores(v)

- **k-Colorability**: A graph is k-colorable if vertices can be assigned k colors such that no adjacent vertices share a color

## Key Points

- Register allocation addresses the fundamental mismatch between numerous program variables and limited hardware registers
- Live variable analysis computes which variables must retain their values at each program point
- The interference graph captures register conflicts and is central to allocation algorithms
- Graph coloring (Chaitin's algorithm) and linear scan are the two primary allocation approaches
- Caller-saved registers are efficient for short-lived values; callee-saved registers reduce save/restore overhead for values needed across calls
- Spilling incurs memory access costs; compilers use spill cost analysis to choose optimal spilling candidates
- Pointer aliasing restricts optimization by forcing the compiler to assume potential memory conflicts
- Higher optimization levels enable more aggressive register utilization

## Common Mistakes

- Confusing register allocation (which variables get registers) with register assignment (which physical register)
- Assuming the `register` keyword forces register allocation; compilers typically ignore this hint
- Forgetting that live variable analysis must consider all possible execution paths, including branches
- Underestimating the impact of aliasing on register allocation—compilers must conservatively assume aliasing
- Ignoring calling conventions when predicting register usage in function call scenarios