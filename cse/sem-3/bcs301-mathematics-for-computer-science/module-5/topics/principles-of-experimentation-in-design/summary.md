# Principles Of Experimentation In Design - Summary

## Key Definitions

- **Experimental Design**: A systematic plan for conducting experiments to collect data that will be analyzed to draw valid conclusions.

- **Randomization**: The random assignment of experimental units to treatments, controlling for both known and unknown confounding variables.

- **Replication**: Repeating measurements under the same treatment conditions to estimate experimental error and increase precision.

- **Blocking**: Grouping experimental units based on a characteristic that affects the response but is not of interest, to remove its variation from experimental error.

- **Experimental Unit**: The smallest entity to which a treatment is independently applied.

- **Treatment**: The specific condition or intervention being studied in an experiment.

- **Response Variable**: The outcome being measured in an experiment.

- **Factor**: An independent variable with two or more levels being investigated.

- **Confounding Variable**: A variable that varies systematically with the treatment and can affect the apparent results.

- **Interaction**: When the effect of one factor depends on the level of another factor.

## Important Formulas

- **Total Variation Decomposition (ANOVA foundation)**:
  Total SS = Treatment SS + Block SS + Error SS

- **Degrees of Freedom**:
  - For k treatments with r replications: df(treatment) = k - 1, df(error) = k(r - 1)

- **Replication Impact on Precision**:
  Standard error decreases by factor of √r with r replications

## Key Points

1. Randomization is the only principle that controls for unknown confounders and is essential for valid statistical inference.

2. The three fundamental principles of experimental design are Randomization, Replication, and Blocking (RRB).

3. Proper identification of the experimental unit is crucial—it determines the appropriate statistical analysis and degrees of freedom.

4. Blocking removes variation attributable to a known source from the error term, increasing power to detect treatment effects.

5. Replication provides estimates of experimental error and enables calculation of confidence intervals for treatment effects.

6. Factorial designs allow simultaneous study of multiple factors and detection of interactions between factors.

7. The choice of experimental design affects what conclusions can be drawn and the efficiency of resource utilization.

8. In computer science, these principles apply to algorithm comparison, A/B testing, hyperparameter optimization, and performance benchmarking.

## Common Mistakes

1. **Confusing replication with repeated measurements**: Using the same experimental unit repeatedly does not constitute true replication and violates independence assumptions.

2. **Over-blocking**: Including too many blocking factors reduces degrees of freedom for error and may not provide benefit if blocks have no real effect.

3. **Ignoring randomization**: Non-random assignment of treatments can lead to systematic bias that invalidates statistical conclusions.

4. **Insufficient replication**: Too few replications result in low statistical power and wide confidence intervals, potentially missing real effects.

5. **Incorrect experimental unit**: Failing to properly identify the unit of analysis can lead to pseudoreplication and inflated Type I error rates.