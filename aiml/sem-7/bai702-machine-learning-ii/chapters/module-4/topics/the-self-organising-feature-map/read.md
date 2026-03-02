# Self-Organising Feature Map (SOM)

## Introduction

The Self-Organising Feature Map (SOM), often referred to as a Kohonen Map after its inventor Teuvo Kohonen, is a prominent type of artificial neural network used in **unsupervised machine learning**. Unlike supervised learning models that require labeled data, SOMs learn to classify, cluster, and visualize high-dimensional data based on its inherent patterns and relationships, projecting it onto a low-dimensional (typically 2D) grid of neurons. This makes it an exceptional tool for tasks like data visualization, dimensionality reduction, and exploratory data analysis.

## Core Concepts

### 1. The Architecture

An SOM consists of two fully connected layers:
*   **Input Layer:** Contains `n` neurons, each representing one feature (dimension) of the input data vector. For example, an input vector could be `[price, screen_size, weight]` for a dataset of laptops.
*   **Output Layer (Map/Grid):** A low-dimensional (usually 1D or 2D) grid of neurons. Each neuron in this grid has an `n`-dimensional **weight vector** (or **reference vector**). This weight vector has the same dimensionality as the input data. Initially, these weights are assigned small random values.

The grid topology (e.g., rectangular or hexagonal) defines the neighborhood relationships between neurons, which is crucial for the learning process.

### 2. The Learning Algorithm: "Winner-Takes-Most"

The training of an SOM is competitive and iterative. For each input data vector presented to the network, the following steps occur:

#### Step 1: Finding the Best Matching Unit (BMU)
The algorithm calculates the distance (e.g., using Euclidean distance) between the input vector and the weight vector of every neuron in the output grid. The neuron whose weight vector is **closest** to the input vector is declared the **Best Matching Unit (BMU)** or the "winning neuron."

`BMU = argmin(||X - W_j||)` for all neurons `j`.

#### Step 2: Identifying the Neighborhood
A topological neighborhood is defined around the BMU. Neurons within this neighborhood radius will be updated, along with the BMU itself. The size of this neighborhood **decreases over time** during training.

#### Step 3: Updating the Weights
The key step: The weight vectors of the BMU and its neighboring neurons are adjusted to become more like the input vector. The update rule is:

`W_j(t+1) = W_j(t) + Θ(j, t) * α(t) * [X(t) - W_j(t)]`

Where:
*   `W_j(t)` is the weight of neuron `j` at time `t`.
*   `α(t)` is the **learning rate**, which decreases monotonically over time (e.g., starts at 0.1 and decays to 0).
*   `Θ(j, t)` is the **neighborhood function**. It dictates how strongly a neighbor is updated based on its distance from the BMU. A common function is the Gaussian function. This function ensures that neurons closer to the BMU are updated more than those farther away.

This process is repeated for a large number of iterations or until convergence.

### 3. The Outcome: Topological Preservation

The most powerful property of an SOM is **topology preservation**. If two data points are similar (close) in the high-dimensional input space, their corresponding BMUs will be close to each other on the 2D output map. Conversely, dissimilar data points will be mapped far apart. This results in the SOM forming a semantically ordered, non-linear projection of the input data onto the grid, effectively creating a **"feature map."**

## Example: Customer Segmentation

Imagine a company with a dataset of customers, each described by high-dimensional features like `[age, annual_income, spending_score]`.

1.  An SOM can be trained on this data.
2.  After training, the 2D grid will self-organize.
3.  You will find that one region of the map contains neurons whose weight vectors represent "high income, high spending" customers.
4.  Another region might represent "young, moderate income, high spending" customers.
5.  A different region might cluster "older, low spending" customers.

The map provides a visual interface to see all the natural clusters (segments) in the data without any prior labels.

## Key Points & Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Type of Learning** | Unsupervised Learning |
| **Primary Goal** | Dimensionality reduction, clustering, and visualization of high-dimensional data. |
| **Key Mechanism** | Competitive, "winner-takes-most" learning with a neighborhood function. |
| **Core Strength** | **Topological Preservation:** Maintains the relational structure of the input data. |
| **Output** | A low-dimensional (2D) discretized representation of the input space, called a feature map. |
| **Applications** | Data mining, customer segmentation, speech recognition, missing data imputation, and exploratory data analysis. |

**In summary,** the Self-Organising Feature Map is a powerful neural network algorithm that learns the intrinsic topology of complex data without supervision. It compresses high-dimensional data while preserving its most important relational structures, producing an intuitive and visually interpretable 2D map of clustered features.