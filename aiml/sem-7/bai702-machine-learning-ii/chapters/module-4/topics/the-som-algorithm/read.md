# Machine Learning II - Module 4: The Self-Organizing Map (SOM) Algorithm

## Introduction

The Self-Organizing Map (SOM), also known as a Kohonen Map after its inventor Teuvo Kohonen, is a prominent unsupervised learning algorithm used for dimensionality reduction and data visualization. Unlike many neural networks that use error-correction learning (like backpropagation), the SOM employs competitive learning to produce a low-dimensional (typically 2D) **discretized representation** of the input space. This "map" preserves the topological properties of the input data, making it an invaluable tool for exploring high-dimensional data and discovering clusters or patterns within it.

## Core Concepts

### 1. The Structure of a SOM

A SOM consists of two fully connected layers:
*   **Input Layer:** This layer has `D` neurons, where `D` is the dimensionality of your input feature vector (e.g., for a data point `x = [x1, x2, x3]`, `D=3`).
*   **Output/Competitive Layer (Map):** This is typically a 2D grid of neurons (e.g., a 5x5, 10x10 grid). Each neuron in this grid has a **weight vector** of the same dimension `D` as the input data. This weight vector represents the neuron's position in the input space. Initially, these weights are assigned small random values.

### 2. The SOM Algorithm: A Step-by-Step Process

The algorithm iteratively processes data points to organize the map. Here's how it works:

**Step 1: Initialization**
Initialize the weight vectors for each neuron in the output map randomly (or via PCA). Choose an initial learning rate `α(0)` (e.g., 0.1) and an initial neighborhood radius `σ(0)` (e.g., half the grid diameter).

**Step 2: Sampling**
Randomly draw a training input vector `x` from your dataset.

**Step 3: Finding the Best Matching Unit (BMU)**
Calculate the distance (usually Euclidean distance) between the input vector `x` and the weight vector `w_j` of every neuron in the output map.
$$ \text{BMU} = \arg\min_j(||x - w_j||) $$
The neuron with the smallest distance is the "winner," called the Best Matching Unit (BMU).

**Step 4: Updating the Weights**
The key idea is that the BMU and its **neighboring neurons** on the 2D grid have their weight vectors adjusted to become more like the input vector `x`. The magnitude of this adjustment decreases with both *time* and *distance* from the BMU.

The weight update rule for a neuron `j` at iteration `t` is:
$$ w_j(t+1) = w_j(t) + \alpha(t) \cdot h_{j, \text{BMU}}(t) \cdot (x(t) - w_j(t)) $$
where:
*   `α(t)` is the learning rate at time `t`, which decays over time (e.g., `α(t) = α₀ * exp(-t / λ)`).
*   `h_{j, BMU}(t)` is the **neighborhood function**. It defines how strongly a neuron `j` is influenced by the current BMU. A common choice is a Gaussian function:
    $$ h_{j, \text{BMU}}(t) = \exp\left(-\frac{||r_j - r_{\text{BMU}}||^2}{2\sigma(t)^2}\right) $$
    where `r_j` and `r_BMU` are the positions of neuron `j` and the BMU on the 2D grid, and `σ(t)` is the neighborhood radius that also decays over time.

**Step 5: Repeat**
Repeat Steps 2-4 for a large number of iterations (e.g., thousands of times), gradually reducing the learning rate `α` and the neighborhood radius `σ` until they approach zero.

### Example: Visualizing Colors

Imagine you want to map RGB colors (3D space: Red, Green, Blue) onto a 2D grid.
*   Each input vector `x` is an RGB triplet like `[0.9, 0.2, 0.2]` (reddish).
*   Each neuron on the 2D map has a weight vector `[w_r, w_g, w_b]`, which also represents a color.
*   Initially, the neuron weights are random, so the map looks like noise.
*   As training progresses, the algorithm organizes the map. Similar colors (points close in 3D space) become mapped to neurons that are close to each other on the 2D grid.
*   The final result is a smooth color gradient across the 2D map, where one region might contain all shades of blue, another greens, etc., effectively creating a structured palette from the random initial state.

## Key Points & Summary

*   **Unsupervised Learning:** SOM is an unsupervised algorithm used for clustering and visualization without needing labeled data.
*   **Dimensionality Reduction:** It projects high-dimensional data onto a low-dimensional (usually 2D) grid, making complex data interpretable.
*   **Topological Preservation:** Its most crucial property is that it preserves the **topological structure** of the input data. Points that are neighbors in the input space remain neighbors on the output map.
*   **Competitive Learning:** Neurons compete to be the BMU for a given input. Only the winner and its neighbors learn.
*   **Training Dynamics:** The learning rate and neighborhood radius must decay over time to ensure the map stabilizes and forms an organized representation. This decay is crucial for convergence.
*   **Applications:** SOMs are widely used in exploratory data analysis, feature extraction, pattern recognition, and tasks like document organization or gene expression analysis.

In essence, the SOM algorithm is like a self-organizing elastic net that stretches to fit the data while maintaining its inherent structure, providing a powerful "window" into high-dimensional datasets.