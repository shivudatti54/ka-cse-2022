# Digital Logic Gates - Compendium

## Essential Definitions

- **Logic Gate**: Electronic circuit implementing Boolean operations; accepts binary inputs, produces binary output
- **Truth Table**: Tabular enumeration of all input permutations with corresponding output states
- **Propagation Delay (t<sub>p</sub>)**: Interval between input transition and resulting output transition
- **Fan-out**: Maximum load-driving capability of a gate output
- **Fan-in**: Number of inputs accommodated by a gate
- **Noise Margin**: Maximum noise voltage tolerable without logical state misinterpretation

## Gate Summary

| Gate | Symbol | Expression | Output = 1 When    |
| ---- | ------ | ---------- | ------------------ |
| AND  | &      | Y = A·B    | All inputs = 1     |
| OR   | ≥1     | Y = A + B  | Any input = 1      |
| NOT  | 1      | Y = A̅      | Input = 0          |
| NAND | &̅      | Y = (AB)̅   | Not all inputs = 1 |
| NOR  | ≥1̅     | Y = (A+B)̅  | All inputs = 0     |
| XOR  | =1     | Y = A ⊕ B  | Inputs differ      |
| XNOR | =1̅     | Y = A ⊙ B  | Inputs identical   |

## Critical Theorems

- **NAND Universality**: Any Boolean function realizable using NAND gates alone
- **NOR Universality**: Any Boolean function realizable using NOR gates alone
- **De Morgan's Theorems**:
- (A + B)̅ = A̅ · B̅
- (A · B)̅ = A̅ + B̅

## Key Formulas

- **Critical Path Delay**: Σ t<sub>p</sub> (gate delays along longest path)
- **Dynamic Power**: P<sub>dynamic</sub> = C<sub>L</sub>V²<sub>DD</sub>f
- **Fan-out Calculation**: min(I<sub>OL</sub>/I<sub>IL</sub>, I<sub>OH</sub>/I<sub>IH</sub>)
