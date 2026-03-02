python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a seed for reproducibility
np.random.seed(42)

# Define population parameters
lambda_param = 0.5
pop_mean = 1 / lambda_param  # μ = 2
pop_std = 1 / lambda_param   # σ = 2

# Generate the population data (exponential distribution)
population = np.random.exponential(scale=pop_mean, size=100000)

# Set sample parameters
num_samples = 10000  # Number of samples to draw
sample_size = 40     # Size of each sample (n)

# Initialize an array to store the sample means
sample_means = np.zeros(num_samples)

# Draw samples and compute their means
for i in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=True)
    sample_means[i] = np.mean(sample)

# Calculate the mean and standard deviation of the sample means
mean_of_means = np.mean(sample_means)
std_of_means = np.std(sample_means)

# Calculate the theoretical Standard Error
theoretical_se = pop_std / np.sqrt(sample_size) # ~ 2 / sqrt(40) ≈ 0.316

# Plot the results
plt.figure(figsize=(10, 6))

# Plot histogram of the sample means
sns.histplot(sample_means, kde=True, stat='density', color='skyblue', label='Distribution of Sample Means')

# Plot a normal PDF for comparison
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
from scipy.stats import norm
p = norm.pdf(x, mean_of_means, std_of_means)
plt.plot(x, p, 'k', linewidth=2, label='Normal Fit')

# Add labels and title
plt.title(f'Demonstration of the Central Limit Theorem\n'
          f'Population: Exponential(λ={lambda_param}), Sample Size n = {sample_size}')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.axvline(mean_of_means, color='red', linestyle='--', label=f'Mean of Means = {mean_of_means:.2f}')
plt.legend()
plt.grid(True)
plt.show()

# Print key statistics
print(f"Population Mean (μ): {pop_mean}")
print(f"Mean of Sample Means: {mean_of_means:.4f}")
print(f"\nPopulation Std (σ): {pop_std}")
print(f"Standard Error (Theoretical): {theoretical_se:.4f}")
print(f"Standard Deviation of Sample Means (Calculated): {std_of_means:.4f}")