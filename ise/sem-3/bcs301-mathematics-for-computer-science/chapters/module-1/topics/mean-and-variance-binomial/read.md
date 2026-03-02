python
import numpy as np

n = 10
p = 0.8
num_simulations = 100000 # Simulate 100,000 batches of 10 packets

# Generate random binomial data

simulated_data = np.random.binomial(n, p, num_simulations)

# Calculate the observed mean and variance

observed_mean = np.mean(simulated_data)
observed_variance = np.var(simulated_data)

print(f"Theoretical Mean: {n*p}, Observed Mean: {observed_mean}")
print(f"Theoretical Variance: {n*p\*(1-p)}, Observed Variance: {observed_variance}")
