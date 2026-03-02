Of course. Here is a comprehensive educational module on Spectral Properties for  engineering students.

# Module 1: Spectral Properties of Stationary Models

## 1. Introduction to Spectral Analysis

In the previous modules, we analyzed time series in the **time domain**. We looked at properties like the mean, variance, autocovariance `γ(h)`, and autocorrelation function `ρ(h)`, which describe how a signal correlates with itself over different time lags `h`.

**Spectral Analysis**, or analysis in the **frequency domain**, offers a complementary and powerful perspective. Instead of looking at correlations over time, it decomposes a stationary time series into its underlying constituent **frequencies** (or cycles). Think of a musical chord: your ear can identify the individual notes (frequencies) that make up the overall sound. Spectral analysis does this mathematically for a time series signal. It tells us which frequencies are strong (have high power) and which are weak (have low power) in the data-generating process.

## 2. Core Concepts Explained

### The Spectral Density Function

For a stationary time series `{X_t}`, the **Spectral Density Function** `f(ω)` is the key tool. It is the Fourier transform of the autocovariance function `γ(h)`.

**Definition:**
The spectral density is defined as:
$$
f(\omega) = \sum_{h=-\infty}^{\infty} \gamma(h) e^{-2\pi i \omega h}, \quad \text{for } -\frac{1}{2} \leq \omega \leq \frac{1}{2}
$$
where:
*   `ω` is the **frequency** (cycles per time unit). For example, if our time unit is "year", a frequency `ω = 0.1` corresponds to a cycle with a period of `1/0.1 = 10` years.
*   `γ(h)` is the autocovariance function at lag `h`.
*   `i` is the imaginary unit (`i² = -1`).

**Physical Interpretation:**
The value `f(ω)` represents the **power** or **variance** contributed by the frequency `ω` to the total variance of the process. A peak in the spectral density at a specific frequency `ω₀` indicates a strong cyclic component in the data with that frequency.

**Inverse Relationship:**
Just as the spectrum is derived from the autocovariance, the autocovariance can be recovered from the spectrum using the inverse Fourier transform:
$$
\gamma(h) = \int_{-1/2}^{1/2} f(\omega) e^{2\pi i \omega h}  d\omega
$$
This highlights the fundamental duality between the time domain (`γ(h)`) and the frequency domain (`f(ω)`). They are two different ways of conveying the same information about the process's structure.

### The Periodogram

In practice, we have a finite sample of data `(x₁, x₂, ..., xₙ)`, not the true theoretical autocovariance function. The **periodogram** `I(ω)` is the sample analogue of the spectral density. It is used to estimate `f(ω)` from observed data.

**Definition:**
The periodogram is defined as:
$$
I(\omega_j) = \frac{1}{n} \left| \sum_{t=1}^{n} x_t e^{-2\pi i \omega_j t} \right|^2
$$
where `ω_j = j/n` for `j = 0, 1, ..., [n/2]` are the **Fourier frequencies**.

While the periodogram is a natural estimator, it is not consistent—its variance does not decrease to zero as the sample size `n` increases. Therefore, we often **smooth** the periodogram (e.g., using a weighted moving average) to obtain a better, more interpretable estimate of the true spectral density.

### White Noise Spectrum

The spectrum of a **white noise process** `{W_t}` is fundamental. Recall that for white noise, `γ(0) = σ²` and `γ(h) = 0` for all `h ≠ 0`.

Plugging this into the spectral density formula:
$$
f(\omega) = \sum_{h=-\infty}^{\infty} \gamma(h) e^{-2\pi i \omega h} = \gamma(0)e^0 + 0 = \sigma^2
$$

**Result:** The spectral density of white noise is **constant** (`f(ω) = σ²`) for all frequencies `ω`. This means a white noise process has equal power across all frequencies, analogous to "white light" which contains all visible frequencies equally. Any deviation from this flat line in an estimated spectrum indicates autocorrelation and structure in the time series.

## 3. Example: An Annual Cycle

Imagine you are analyzing average monthly temperature data. You expect a strong **annual cycle** (`ω = 1/12 ≈ 0.0833` cycles per month).

*   **Time Domain:** The autocorrelation function `ρ(h)` would show significant positive correlation at lags `h=12, 24, 36,...` and negative correlation at `h=6, 18, 30,...`.
*   **Frequency Domain:** The estimated spectral density would show a very large, sharp **peak** precisely at the frequency `ω ≈ 0.0833`. The height of this peak shows how much variance in the temperature is explained by this annual cycle. All other frequencies would have much lower power.

## 4. Key Points & Summary

| Aspect | Time Domain Analysis | Frequency Domain (Spectral) Analysis |
| :--- | :--- | :--- |
| **What it studies** | Autocorrelation over lags `h` | Power over frequencies `ω` |
| **Main Tool** | Autocovariance Function `γ(h)` | Spectral Density Function `f(ω)` |
| **Perspective** | How values at different times relate | Which cycles are present and their strength |
| **Relationship** | `f(ω)` is the Fourier Transform of `γ(h)` | `γ(h)` is the Inverse FT of `f(ω)` |
| **Key Insight** | A peak in `f(ω)` at `ω₀` indicates a strong cyclic component with period `1/ω₀`. |
| **Baseline** | White noise has a flat spectrum (`f(ω) = constant`). |

**Summary:** Spectral analysis is an essential technique for engineers to identify hidden periodicities, cycles, and seasonal patterns in signals. It transforms the problem from the time domain to the frequency domain, providing a powerful alternative view of the data's structure that is often more intuitive for understanding oscillatory behavior.