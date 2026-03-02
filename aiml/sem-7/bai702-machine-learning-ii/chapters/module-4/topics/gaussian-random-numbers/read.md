python
import numpy as np

# Generate 1000 standard normal random numbers (mean=0, std=1)
standard_normal_data = np.random.randn(1000)

# Generate 1000 Gaussian numbers with mean=5 and standard deviation=2
custom_gaussian_data = np.random.normal(loc=5, scale=2, size=1000)