# Observations On Estimation - Summary

## Key Definitions

- **Software Estimation**: The process of predicting the effort, cost, time, and resources required to complete software development activities.
- **Accuracy**: How close an estimate is to the actual value; the correctness of the estimate.
- **Precision**: The level of detail or specificity in an estimate, often expressed as a single number.
- **Cone of Uncertainty**: A model showing how estimation uncertainty decreases as projects progress through their lifecycle.
- **Planning Fallacy**: A cognitive bias causing underestimation of time, cost, and risk for future tasks.
- **Reestimation**: The process of updating estimates as more information becomes available during project execution.

## Important Formulas

- **COCOMO Basic Model**: Effort = a × (KLOC)^b × ∏EFi
  - Where KLOC is thousands of lines of code, a and b are coefficients, and EFi are adjustment factors

- **Function Point Analysis**: FP = UFC × VAF
  - Where UFC is unadjusted function point count and VAF is value adjustment factor

- **Estimate Range**: Early estimates typically have ±50% to ±100% uncertainty, narrowing to ±10% to ±20% in later project phases

## Key Points

1. Software estimation is fundamentally difficult due to the unique, creative nature of software development where each project creates something new.

2. Estimates should be expressed as ranges rather than single point values to accurately represent inherent uncertainty.

3. The planning fallacy and optimism bias consistently cause software estimates to be optimistic, often by significant margins.

4. Decomposition techniques improve estimation by breaking complex projects into smaller, more manageable components.

5. Empirical estimation models require calibration to organizational context using historical project data to be effective.

6. The Cone of Uncertainty demonstrates that estimation uncertainty decreases as projects progress and more information becomes known.

7. There is a direct relationship between estimation accuracy and software quality outcomes; unrealistic estimates lead to quality compromises.

8. Estimation is not a one-time activity but requires continuous reestimation throughout the project lifecycle.

9. Human factors including psychological biases and organizational culture significantly impact estimation accuracy.

10. Productivity varies substantially across teams and individuals, requiring estimation techniques to account for team-specific capabilities.

## Common Mistakes

1. **Presenting estimates with false precision**: Providing estimates like "127.3 days" when uncertainty is ±50% creates false confidence.

2. **Ignoring requirements volatility**: Failing to account for requirements changes leads to significant estimation errors.

3. **Using generic models without calibration**: Applying COCOMO or similar models without organizational customization reduces accuracy.

4. **Not updating estimates**: Treating initial estimates as fixed values rather than planning parameters that require refinement.

5. **Underestimating integration effort**: Decomposition techniques often miss the effort required to integrate components.