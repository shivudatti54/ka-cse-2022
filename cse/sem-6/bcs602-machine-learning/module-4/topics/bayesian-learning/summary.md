# Bayesian Learning

## Overview

Bayesian learning treats model parameters as random variables with probability distributions rather than fixed values. It combines prior beliefs with observed data to produce posterior distributions, enabling principled uncertainty quantification and incorporation of domain knowledge into machine learning models.

## Key Points

- **Paradigm Shift**: Parameters are distributions not point estimates; P(θ|Data) instead of θ\*
- **Bayes Rule for Learning**: P(θ|D) = P(D|θ)\*P(θ)/P(D); posterior = likelihood × prior / evidence
- **Prior Distribution P(θ)**: Encodes initial beliefs about parameters before seeing data; can be informative (strong beliefs) or non-informative (weak beliefs)
- **Posterior Distribution P(θ|D)**: Updated beliefs after observing data; combines prior and likelihood
- **MAP Estimation**: θ_MAP = argmax P(θ|D) = argmax P(D|θ)\*P(θ); single best parameter value
- **Prediction**: Average over posterior: P(y|x,D) = ∫P(y|x,θ)\*P(θ|D)dθ; accounts for parameter uncertainty

## Important Concepts

- Maximum Likelihood (ML): θ_ML = argmax P(D|θ); ignores prior, can overfit
- MAP vs ML: MAP includes prior, ML is special case with uniform prior
- Conjugate priors: prior and posterior have same form (e.g., Beta-Binomial); simplifies computation
- Bayesian vs Frequentist: Bayesian treats parameters as random, Frequentist as fixed unknowns

## Notes

- Understand posterior = likelihood × prior / evidence interpretation
- MAP estimation formula: θ_MAP = argmax[P(D|θ)*P(θ)]
- Know difference: ML (no prior), MAP (includes prior), Full Bayesian (distribution)
- Conjugate prior pairs: Beta-Binomial, Gamma-Poisson, Gaussian-Gaussian
