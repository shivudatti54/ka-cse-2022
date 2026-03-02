# Function Point Metrics - Summary

## Key Definitions and Concepts

- **Function Point (FP):** A standardized unit for measuring software size based on functionality delivered to users, independent of programming language.
- **Function Point Analysis (FPA):** The technique used to measure software size by quantifying the functional user requirements.
- **Function Components:** The five types of functions counted in FPA: External Inputs (EI), External Outputs (EO), External Inquiries (EQ), Internal Logical Files (ILF), and External Interface Files (EIF).
- **Unadjusted Function Points:** The initial FP count before applying complexity adjustment factors.
- **Value Adjustment Factor (VAF):** A multiplier (0.65 to 1.35) that adjusts FP count based on system characteristics.

## Important Formulas and Theorems

| Component | Low | Average | High |
|-----------|-----|---------|------|
| EI | 3 FP | 4 FP | 6 FP |
| EO | 4 FP | 5 FP | 7 FP |
| EQ | 3 FP | 4 FP | 6 FP |
| ILF | 7 FP | 10 FP | 15 FP |
| EIF | 5 FP | 7 FP | 10 FP |

**VAF = 0.65 + (0.01 × TDI)**

Where TDI = Sum of ratings (0-5) for all 14 General System Characteristics

**Adjusted FP = Unadjusted FP × VAF**

## Key Points

- Function Points measure "what" the software does, not "how" it is built.
- ILF vs EIF: Internal files are maintained by the application; external interface files are maintained by other systems.
- EQ vs EO: Inquiries retrieve data without modification; Outputs process and generate new data.
- VAF typically ranges from 0.8 to 1.2 in practice; extreme values are uncommon.
- Function Points enable cross-project comparisons and productivity benchmarking.
- FP can be converted to LOC for use in estimation models like COCOMO.
- FPA is particularly effective for business application software with significant data handling.

## Common Mistakes to Avoid

1. **Confusing ILF with EIF** — Remember: ILF data stays within your application; EIF data comes from external systems.

2. **Forgetting the VAF formula base value** — The formula is 0.65 + (0.01 × TDI), not just TDI × 0.01.

3. **Counting the same function multiple times** — Each unique user function is counted once, regardless of how many times it is used.

4. **Ignoring complexity ratings** — Not all functions have the same complexity; use the correct FP values for each complexity level.

5. **Overlooking the adjustment factor range** — VAF must always be between 0.65 and 1.35; verify your calculation.

## Revision Tips

1. **Practice with examples** — Work through at least 3-4 different scenarios to master the calculation process.

2. **Create a summary table** — Write the complexity values table from memory and verify against your notes.

3. **Understand the 14 GSCs** — Review each characteristic briefly to ensure you can apply them in estimation scenarios.

4. **Solve previous year questions** — DU exam papers often include FP calculation problems—practice these extensively.

5. **Connect to cost estimation** — Understand how FP relates to effort, duration, and cost estimation in real projects.