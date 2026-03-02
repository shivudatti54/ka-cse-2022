# Selection Bias - Summary

## Key Definitions and Concepts

- **Selection Bias**: A systematic error occurring when the sample selected for analysis is not representative of the target population, leading to results that differ systematically from the true population parameters.

- **Sampling Bias**: Non-random selection of samples, including convenience sampling, voluntary response bias, and undercoverage of population segments.

- **Survivorship Bias**: Analyzing only successful cases while ignoring failures, creating a distorted view of true success factors.

- **Attrition Bias**: Systematic dropout of participants during studies, particularly when dropouts are correlated with outcomes.

## Important Formulas and Concepts

- Selection bias exists when P(Y | X, S=1) ≠ P(Y | X), where S indicates selection into the sample.

- Weighted estimate formula: Σ(wi × xi) / Σ(wi), where weights compensate for unequal selection probabilities.

- Probability sampling methods: Simple Random Sampling, Stratified Sampling, Cluster Sampling.

## Key Points

1. Selection bias is systematic and does NOT decrease with larger sample sizes, unlike random sampling error.

2. The fundamental problem is that the selection mechanism is correlated with the outcome variable.

3. Types include sampling bias, survivorship bias, recall bias, attrition bias, confirmation bias, and publication bias.

4. Detection requires comparing sample characteristics to known population parameters.

5. Mitigation involves probability sampling, weighting adjustments, and propensity score methods.

6. Selection bias affects external validity (generalizability) more than internal validity.

7. In machine learning, biased training data leads to models that perform unequally across different groups.

## Common Mistakes to Avoid

- Confusing selection bias with random sampling error - remember that random error decreases with n, bias does not.

- Assuming larger samples automatically solve bias problems - they only reduce random variation.

- Ignoring selection bias when using convenience samples or observational data.

- Forgetting that selection bias can occur at any stage of research - from subject recruitment to analysis.

## Revision Tips

1. Create a table listing each type of bias with a one-line definition and one real-world example.

2. Practice identifying bias in exam-style scenarios by asking: "How was this sample selected? Is it correlated with the outcome?"

3. Remember the key distinction: random error = imprecise but unbiased; selection bias = precise but wrong.

4. For exam questions, always suggest at least one mitigation strategy when identifying bias.