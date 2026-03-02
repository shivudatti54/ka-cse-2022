# Locally Weighted Regression (LWR)

**Definition:**
Locally Weighted Regression (LWR) is a non-parametric regression technique that uses the concept of nearest neighbors to estimate the local regression function.

**Key Points:**

- **Local Regression**: LWR approximates the regression function at each data point using a weighted average of values from a small, local neighborhood.
- **Nearest-Neighbor Search**: LWR uses a nearest-neighbor search algorithm to identify the most relevant data points for each data point.
- **Weighting Scheme**: The weights assigned to each nearest neighbor are typically based on their proximity to the data point.
- **Freedom of Parameters**: LWR allows for the specification of various parameters, such as the number of neighbors to consider, the weighting scheme, and the bandwidth.

**Formulas and Theorems:**

- **LWR Equations**:
  - $y_{i,\theta} = \frac{\sum_{j=1}^{m} w_{j,i} x_{i,j}}{\sum_{j=1}^{m} w_{j,i}}$
  - $w_{j,i} = \frac{1}{\sum_{k=1}^{n} \frac{1}{\|x_{i,j} - x_{i,k}\|}}$
- **Theorem**: LWR is a linear combination of local kernel estimates, which converges to the true regression function as the number of neighbors increases.

**Important Concepts:**

- **Kernel Functions**: Used to compute the distance between data points, such as the Gaussian kernel: $k(x,y) = \exp(-\frac{\|x-y\|^2}{2\sigma^2})$.
- **Bandwidth Selection**: Techniques for selecting the optimal bandwidth, such as the Silverman's rule: $\sigma = \frac{1.06s_n(1-h)^{1/5}}{n^{1/5}}$, where $s_n$ is the sample standard deviation and $h$ is the smoothing factor.

**Revision Tips:**

- Understand the differences between LWR and other regression techniques, such as linear regression and decision trees.
- Be able to explain the concept of local regression and how LWR approximates it.
- Familiarize yourself with the various weighting schemes and bandwidth selection techniques used in LWR.
