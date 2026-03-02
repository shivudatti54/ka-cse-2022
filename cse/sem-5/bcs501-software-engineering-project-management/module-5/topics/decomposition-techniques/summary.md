# Decomposition Techniques - Summary

## Key Definitions

- **Decomposition**: The process of breaking down a complex project or task into smaller, more manageable components to facilitate accurate estimation and control.

- **Work Breakdown Structure (WBS)**: A hierarchical decomposition of the total project scope into work packages that define the work to be accomplished to achieve project objectives.

- **Top-Down Decomposition**: An estimation approach that starts with project-level estimates and progressively elaborates into detailed component estimates.

- **Bottom-Up Decomposition**: An estimation approach that identifies all individual tasks at the finest detail, then aggregates estimates to project level.

- **Three-Point Estimation**: An estimation technique using optimistic, most likely, and pessimistic scenarios to derive expected values and uncertainty measures.

- **PERT (Program Evaluation and Review Technique)**: A statistical method using the formula: Expected = (O + 4M + P) / 6 for task estimation.

- **Estimation by Analogy**: Using historical data from similar completed projects to estimate current project parameters.

## Important Formulas

- **PERT Three-Point Estimate**: E = (O + 4M + P) / 6
- **Standard Deviation**: σ = (P - O) / 6
- **Variance**: σ² = [(P - O) / 6]²
- **Combined Standard Deviation** (independent tasks): σ_total = √(σ₁² + σ₂² + ... + σₙ²)
- **95% Confidence Interval**: E ± 2σ

## Key Points

1. Decomposition techniques address the inherent difficulty of estimating large, complex software projects by breaking them into smaller, more estimable components.

2. The Work Breakdown Structure (WBS) serves as the foundational framework for project decomposition, organizing all work hierarchically from project level to individual tasks.

3. Top-down decomposition aligns with strategic objectives but may suffer from optimism bias; bottom-up decomposition captures ground realities but requires detailed task knowledge.

4. Three-point estimation provides not just a point estimate but also communicates uncertainty through standard deviation and confidence intervals.

5. The PERT formula weights the most likely estimate four times more heavily than optimistic and pessimistic extremes, reflecting realistic estimation behavior.

6. Estimation by analogy leverages historical project data but requires careful selection of comparable projects and adjustment for differences.

7. Effective decomposition typically requires combining multiple techniques rather than relying on a single approach.

8. Decomposition must include all project scope (100% rule) while excluding work outside scope to maintain estimation accuracy.

9. Aggregation of decomposed estimates must account for dependencies, integration effort, and project management overhead.

10. The quality of decomposition directly impacts software quality management by enabling realistic planning, resource allocation, and risk mitigation.

## Common Mistakes

1. **Incomplete decomposition**: Failing to include all project work in WBS, leading to underestimated effort and schedule overruns.

2. **Over-decomposition**: Creating excessively detailed WBS structures that add management overhead without improving estimation accuracy.

3. **Ignoring dependencies**: Aggregating task estimates without accounting for sequential or parallel relationships between tasks.

4. **Single-point estimate overreliance**: Using only most likely estimates without considering uncertainty ranges, resulting in overconfident commitments.

5. **Poor historical data**: Applying estimation by analogy without adequate documented historical projects or proper adjustment for differences.

6. **Scope creep during decomposition**: Including work that falls outside project scope, inflating estimates beyond actual requirements.

7. **Neglecting non-development activities**: Focusing only on development tasks while omitting estimation for testing, deployment, documentation, and project management.