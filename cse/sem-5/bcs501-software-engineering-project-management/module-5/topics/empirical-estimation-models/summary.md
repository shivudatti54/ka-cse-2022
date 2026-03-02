# Empirical Estimation Models - Summary

## Key Definitions and Concepts

- **Empirical Estimation Models:** Mathematical approaches derived from historical project data to predict software effort, cost, and schedule.
- **COCOMO:** Constructive Cost Model developed by Barry Boehm, the most widely used empirical estimation model.
- **Person-Month (PM):** Unit of effort measurement representing one person working for one month.
- **KLOC:** Thousands of Lines of Code, a measure of software size.
- **Function Points (FP):** Size metric measuring functionality from user's perspective, independent of programming language.
- **Cost Drivers:** Factors that multiplicatively affect effort estimation (reliability, complexity, personnel capability).
- **Scale Factors:** Factors in COCOMO II that affect the exponent in effort calculation.

## Important Formulas and Theorems

**Basic COCOMO:**

- Effort = a × (KLOC)^b
- Development Time = c × (Effort)^d

**Intermediate COCOMO:**

- Effort = [a × (KLOC)^b] × EAF
- Where EAF = Product of all cost drivers

**Putnam Model:**

- Effort = L³ / (t³ × p²)

**Function Points:**

- AFP = UAF × VAF
- VAF = 0.65 + 0.01 × Σ(Complexity Adjustment Factors)

## Key Points

- COCOMO has three project modes: Organic (simple), Semi-detached (medium), Embedded (complex).
- Basic COCOMO uses only size; Intermediate adds 15 cost drivers; Detailed applies drivers at phase level.
- COCOMO II addresses modern development with three models: Application Composition, Early Design, and Post-Architecture.
- Function Points are language-independent and measure user-perceived functionality.
- Putnam Model shows inverse cubic relationship between development time and effort.
- Empirical models improve accuracy through calibration with organization-specific historical data.
- Hybrid approaches combining multiple techniques often yield better results.

## Common Mistakes to Avoid

- Using organic mode coefficients for embedded projects (leads to severe underestimation).
- Forgetting to multiply by EAF in intermediate COCOMO (only calculating base effort).
- Confusing unadjusted function points with adjusted function points.
- Applying the same productivity parameter across different organizations or project types.
- Ignoring cost drivers that significantly impact effort estimates in intermediate and detailed models.

## Revision Tips

1. Memorize COCOMO coefficients for all three modes - this is frequently tested in exams.
2. Practice numerical problems on Basic and Intermediate COCOMO calculations.
3. Remember the five components of Function Point analysis for practical applications.
4. Understand the relationship: as development time decreases, effort and cost increase significantly.
5. Focus on understanding when to apply each estimation model rather than just memorizing formulas.
