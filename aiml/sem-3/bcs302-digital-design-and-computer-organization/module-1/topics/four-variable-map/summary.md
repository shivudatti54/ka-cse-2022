# Four Variable Map
### Summary: Four-Variable Karnaugh Map

The four-variable Karnaugh Map is a 4×4 grid tool used for minimizing Boolean functions with four input variables (A, B, C, D). Each of the 16 cells represents one minterm (m₀-m₁₅), arranged using Gray code ordering where adjacent cells differ by exactly one variable—this adjacency property is proven mathematically and enables variable elimination during grouping.

Key structural features include wrap-around adjacency (top-bottom and left-right), enabling groups to span across boundaries. The grouping rules mandate rectangular shapes of powers of 2 (1, 2, 4, 8, 16 cells), with larger groups eliminating more variables: a group of 2ⁿ cells eliminates exactly n variables, a theorem that follows from the constant-variable distinction principle.

The minimization procedure involves plotting the function, forming the largest possible prime implicants, identifying essential prime implicants (those covering unique minterms), and selecting the minimum set to cover all minterms. Worked examples demonstrated SOP minimization (yielding C' + D' for the given function), POS minimization, and don't-care condition handling—showing the flexibility of the K-map approach.

The K-map method remains foundational in digital design education, bridging theoretical Boolean algebra with practical circuit optimization and serving as a conceptual precursor to advanced algorithmic minimization techniques.