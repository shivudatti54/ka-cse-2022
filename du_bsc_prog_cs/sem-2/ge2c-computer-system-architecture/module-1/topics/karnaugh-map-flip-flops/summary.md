# Karnaugh Maps and Flip-Flops - Summary

## Key Definitions and Concepts
- **Karnaugh Map (K-map)**: A graphical method for simplifying Boolean algebra expressions using grouped adjacent cells representing minterms
- **Implicant**: A product term that implies the function; a prime implicant cannot be combined with another term
- **Flip-Flop**: A bistable sequential logic element that stores one bit of information, edge-triggered
- **Characteristic Table**: Defines flip-flop output (Q⁺) in terms of inputs and current state (Q)
- **Excitation Table**: Specifies input conditions required to cause specific state transitions (Q → Q⁺)

## Important Formulas and Theorems
- **K-map sizes**: n variables → 2ⁿ cells
- **SR Flip-Flop**: Q⁺ = S + R'Q (with constraint SR = 0)
- **D Flip-Flop**: Q⁺ = D
- **JK Flip-Flop**: Q⁺ = JQ' + K'Q
- **T Flip-Flop**: Q⁺ = T ⊕ Q = TQ' + T'Q

## Key Points
- K-maps exploit geometric adjacency to identify terms differing by only one variable, which can be combined and simplified
- Groups must be powers of 2 (1,2,4,8,16) and should be as large as possible for maximum simplification
- Edge wrapping allows cells at opposite boundaries to be considered adjacent
- D flip-flop is simplest (Q⁺ = D) and most widely used in registers and data storage
- JK flip-flop is most versatile, with toggle capability when J=K=1
- T flip-flop is ideal for frequency division and binary counters
- Flip-flops are edge-triggered (state changes only at clock transitions), unlike level-sensitive latches

## Common Mistakes to Avoid
- Forgetting that K-map cells wrap around edges; corner cells are adjacent to each other
- Creating groups with odd numbers of cells (must be powers of 2)
- Confusing characteristic tables with excitation tables—one describes behavior, the other defines required inputs
- Overlooking the invalid state (S=R=1) in SR flip-flops
- Drawing incorrect clock triggering edges—flip-flops change state only on rising or falling edges, not throughout the clock pulse

## Revision Tips
- Practice drawing all K-map sizes (2,3,4 variable) until automatic
- Memorize all four flip-flop characteristic equations—they form the basis for sequential circuit analysis
- Work through at least 3-4 K-map minimization problems covering both SOP and POS forms
- Create a comparison table of flip-flop types, their inputs, behaviors, and common applications
- Practice deriving excitation tables from characteristic tables and vice versa