# PMF, PDF, and CDF - Summary

## Key Definitions and Concepts

- **Random Variable**: A function mapping outcomes to real numbers; classified as discrete (countable values) or continuous (uncountable values in an interval)

- **Probability Mass Function (PMF)**: For discrete X, p_X(x) = P(X = x), giving probability of specific outcomes

- **Probability Density Function (PDF)**: For continuous X, f_X(x) describes likelihood density; P(X = a) = 0 for any specific value

- **Cumulative Distribution Function (CDF)**: F_X(x) = P(X ≤ x), universally applicable to both discrete and continuous variables

## Important Formulas and Theorems

- **PMF Properties**: p_X(x) ≥ 0 and Σ p_X(x) = 1

- **PDF Properties**: f_X(x) ≥ 0 and ∫ f_X(x) dx = 1

- **CDF Properties**: Non-decreasing, 0 ≤ F_X(x) ≤ 1, lim_{x→-∞}F_X(x)=0, lim_{x→∞}F_X(x)=1

- **CDF from PMF**: F_X(x) = Σ_{t≤x} p_X(t)

- **CDF from PDF**: F_X(x) = ∫_{-∞}^x f_X(t) dt

- **PDF from CDF**: f_X(x) = d/dx F_X(x)

- **Interval Probability from CDF**: P(a < X ≤ b) = F_X(b) - F_X(a)

## Key Points

1. Always identify variable type (discrete/continuous) before selecting PMF or PDF

2. For continuous distributions, probability of exact value is zero; only interval probabilities matter

3. CDF unifies discrete and continuous cases—know how to derive it from PMF/PDF

4. Verify normalization: PMF sums to 1, PDF integrates to 1

5. Common discrete distributions: Bernoulli, Binomial, Poisson

6. Common continuous distributions: Uniform, Exponential, Normal

7. F'(x) = f(x) is the fundamental relationship connecting PDF and CDF

## Common Mistakes to Avoid

1. Using P(X = x) for continuous variables—this is always zero!

2. Forgetting to integrate PDF over the entire support (common error in exams)

3. Confusing when to use summation (discrete) vs. integration (continuous)

4. Not verifying that probabilities sum/integrate to 1 before solving

5. Applying discrete formulas to continuous variables or vice versa

## Revision Tips

1. Practice converting between PMF, PDF, and CDF in both directions

2. Memorize the three properties for each function type—they're frequently tested

3. Solve at least 5 problems involving probability calculations from each type

4. Focus on exponential and uniform distributions—they commonly appear in exam questions

5. Remember: CDF is always the starting point for probability calculations in continuous cases