# Predicting Trends - Riding Your Waves - Summary

## Key Definitions and Concepts

- **Trend Prediction**: The process of forecasting future IT resource demands based on historical data analysis and pattern identification.

- **Time Series**: A sequence of data points collected at regular intervals, used to analyze demand patterns over time.

- **Capacity Planning Waves**: The cyclical nature of demand fluctuations in IT systems, including growth waves, stability waves, decline waves, and unexpected waves.

- **Moving Average**: A forecasting technique that calculates the average of a specific number of consecutive data points to smooth out short-term fluctuations.

- **Exponential Smoothing**: A forecasting technique that assigns exponentially decreasing weights to older observations, with the formula: F(t+1) = α × D(t) + (1-α) × F(t).

- **Linear Regression**: A statistical method that fits a straight line through data points to identify and predict long-term trends.

## Important Formulas and Theorems

- **Simple Moving Average**: SMA = (X₁ + X₂ + ... + Xₙ) / n

- **Exponential Smoothing**: Fₜ₊₁ = α × Dₜ + (1 - α) × Fₜ

- **Linear Regression Equation**: Y = a + bX, where b = (nΣXY - ΣXΣY) / (nΣX² - (ΣX)²)

## Key Points

- IT systems exhibit various demand patterns: seasonal (recurring at regular intervals), trend (long-term direction), cyclical (long-term oscillations), and random (unpredictable variations).

- Moving averages smooth short-term fluctuations to reveal longer-term trends; weighted moving averages give more importance to recent data.

- Exponential smoothing uses a smoothing constant α (between 0 and 1) to balance responsiveness to recent changes with forecast stability.

- Linear regression helps predict long-term capacity requirements by fitting a trend line through historical data points.

- "Riding your waves" means proactively preparing for different phases of demand cycles rather than reactively addressing issues.

- Short-term forecasts are generally more accurate than long-term forecasts due to reduced uncertainty.

- Qualitative forecasting methods are used when historical data is insufficient, while quantitative methods require historical data.

## Common Mistakes to Avoid

- Using an inappropriately large or small value for the smoothing constant α in exponential smoothing without considering the specific demand pattern characteristics.

- Applying linear regression when demand patterns are non-linear, leading to inaccurate forecasts.

- Ignoring seasonal variations when analyzing data that exhibits clear seasonal patterns.

- Forgetting that forecast accuracy decreases as the prediction horizon increases.

## Revision Tips

- Practice calculating moving averages and exponential smoothing with different values of n and α to understand their effects on forecasts.

- Memorize the exponential smoothing and linear regression formulas as they are frequently tested in university examinations.

- Review the concept of capacity planning waves and be able to explain how each type affects IT infrastructure planning.

- Solve at least 2-3 numerical problems from each forecasting technique to build confidence for exam questions.
