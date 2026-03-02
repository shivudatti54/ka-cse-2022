# Latin Square Design - Summary

## Key Definitions

- **Latin Square**: An n × n array containing n symbols (treatments) where each symbol appears exactly once in each row and exactly once in each column.

- **Blocking Factors**: Two nuisance factors (represented by rows and columns) that are controlled in the experiment to reduce variability in treatment comparisons.

- **Treatment Factor**: The primary factor of interest whose effects are being compared (represented by the symbols in the Latin Square).

- **Replicate**: In Latin Square Design, each treatment appears exactly once in each row and column, so the entire square constitutes a single replicate.

## Important Formulas

**Statistical Model**: Y_{ijk} = μ + α_i + β_j + τ_k + ε_{ijk}

**Degrees of Freedom**:
- Total: n² - 1
- Treatments: n - 1
- Rows: n - 1
- Columns: n - 1
- Error: (n - 1)(n - 2)

**Sum of Squares**:
- SST = Σy² - (Σy)²/n²
- SSTr = n × Σ(Ȳ_{i..} - Ȳ_{...})² (Treatments)
- SSR = n × Σ(Ȳ_{.j.} - Ȳ_{...})² (Rows)
- SSC = n × Σ(Ȳ_{..k} - Ȳ_{...})² (Columns)
- SSE = SST - SSTr - SSR - SSC

## Key Points

1. Latin Square Design controls for two sources of nuisance variability simultaneously, making it more efficient than Randomized Block Design when two blocking factors exist.

2. The design requires all three factors (two blocks + one treatment) to have the same number of levels—this is a strict requirement.

3. The error degrees of freedom decreases as n increases: for n=3, df=2; for n=4, df=6; for n=5, df=12.

4. Randomization involves selecting a random Latin Square and then randomly assigning treatments to the symbols.

5. The additive model assumes no interaction between treatments and blocking factors—this is a critical assumption.

6. Latin Square Design is particularly useful in computer science for comparing algorithms across different hardware configurations and datasets.

7. The main advantage is increased precision in treatment estimates due to controlling two blocking factors; the main limitation is the requirement for equal levels.

## Common Mistakes

1. **Forgetting the constraint**: Students often ignore that the design is only applicable when the number of treatment levels equals the number of levels for both blocking factors.

2. **Confusing with factorial design**: Latin Square is not a factorial design—it has one treatment factor studied at multiple levels, not multiple factors at multiple levels.

3. **Ignoring assumptions**: Many students forget to check the additivity assumption—no interaction between treatments and blocking factors—which is critical for valid inference.

4. **Incorrect error degrees of freedom**: A common error is using n-1 instead of (n-1)(n-2) for error degrees of freedom when setting up the ANOVA table.