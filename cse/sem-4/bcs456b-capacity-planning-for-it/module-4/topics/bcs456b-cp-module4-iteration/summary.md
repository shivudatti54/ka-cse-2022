# Iteration and Calibration - Summary

## Key Definitions and Concepts

- **Iteration in Capacity Planning**: A cyclical process of prediction, implementation, measurement, and refinement that continuously improves capacity planning accuracy.

- **Model Calibration**: The process of adjusting model parameters to ensure theoretical predictions match actual system performance.

- **Model Verification**: Checking that a capacity planning model is mathematically correct and behaves according to theoretical expectations.

- **Model Validation**: Confirming that model predictions accurately represent real-world system behavior using independent data sets.

- **Workload Characterization**: The process of identifying transaction types, measuring resource demands, and understanding arrival patterns.

- **Sensitivity Analysis**: Technique to understand how changes in input parameters affect model outputs.

## Important Formulas and Theorems

- **Utilization Calculation**: Utilization = Arrival Rate × Service Time (or Throughput × Service Demand)
- **Queueing Relationship**: As utilization approaches 100%, response time increases exponentially
- **Seasonal Index**: Seasonal Index = Peak Period Utilization / Base Period Utilization
- **Growth Projection**: Future Capacity = Current Capacity × (1 + Growth Rate)^n

## Key Points

- Capacity planning is an ongoing iterative process, not a one-time activity.

- Model calibration requires both technical understanding of the system and analysis of actual performance data.

- Verification ensures mathematical correctness; validation ensures practical accuracy.

- Typical utilization thresholds: 70-80% for sustained operations, action needed above 80%, immediate intervention above 90%.

- Workload characterization involves identifying different transaction types and their resource requirements.

- Sensitivity analysis helps identify which parameters most significantly impact predictions.

- Automated calibration using machine learning can handle complex, multi-dimensional models more efficiently than manual methods.

- Seasonal variations must be accounted for in capacity predictions for businesses with cyclical demand patterns.

## Common Mistakes to Avoid

- Confusing model verification with validation - these are distinct but complementary processes.

- Setting static thresholds without considering workload patterns or business requirements.

- Using outdated baseline data that no longer reflects current system behavior.

- Over-calibrating models to historical data without considering future changes in workload characteristics.

- Neglecting to validate predictions against actual performance after implementation.

## Revision Tips

- Focus on understanding the iteration cycle phases and their sequence.

- Practice calculating utilization and response times using queueing formulas.

- Remember the distinction between verification and validation - this is a common exam question.

- Review the three main calibration techniques and be able to explain each with examples.

- Understand how seasonal variations and growth trends affect capacity predictions.
