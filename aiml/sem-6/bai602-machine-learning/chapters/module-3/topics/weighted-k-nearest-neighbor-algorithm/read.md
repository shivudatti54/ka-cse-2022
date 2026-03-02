Of course. Here is a comprehensive educational content piece on the Weighted K-Nearest-Neighbor Algorithm for  Engineering students.

# Weighted K-Nearest-Neighbor (WKNN) Algorithm

## 1. Introduction

The K-Nearest-Neighbor (KNN) algorithm is one of the simplest and most intuitive supervised machine learning algorithms, used for both classification and regression tasks. Its core principle is that similar things exist in close proximity. A fundamental assumption in standard KNN is that all neighbors contribute equally to the classification or prediction of a new data point. However, this is not always optimal. The **Weighted K-Nearest-Neighbor (WKNN)** algorithm enhances the standard KNN by addressing this very limitation, assigning a higher influence or "weight" to neighbors that are closer to the query point.

## 2. Core Concepts

### The Limitation of Standard KNN
In standard KNN, for a given query point, we find its `K` nearest neighbors in the training dataset based on a distance metric (like Euclidean, Manhattan, etc.). For classification, we then perform a majority vote among these `K` neighbors. Each neighbor, regardless of whether it is extremely close or barely within the `K`-neighborhood, gets exactly one vote. This can lead to misclassification if, for instance, several distant neighbors (belonging to one class) outvote a few very close neighbors (belonging to the correct class).

### How WKNN Addresses This
The Weighted KNN algorithm introduces a simple but powerful idea: **not all neighbors are created equal**. A closer neighbor is more similar to the query point and should have a greater say in the final decision than a farther one.

This is implemented by assigning a **weight** to each of the `K` neighbors. The weight is inversely proportional to the distance from the query point. The closer the neighbor, the higher its weight.

### The Weighting Function
The most common weighting function uses the inverse of the distance. For a neighbor at distance `d_i` from the query point, its weight `w_i` is typically calculated as:

**`w_i = 1 / d_i`**

To avoid issues when `d_i = 0` (which would make the weight infinite), it's common practice to add a very small constant or use a modified formula. Another robust alternative is to use the squared inverse distance:

**`w_i = 1 / (d_i^2 + ε)`** (where `ε` is a small value to prevent division by zero)

### The Mathematical Formulation for Classification
For a classification task:
1.  Calculate the distance between the query point and all training samples.
2.  Select the `K` nearest neighbors.
3.  Assign a weight to each of these `K` neighbors using the weighting function (`w_i = 1 / d_i`).
4.  Instead of a simple majority vote, calculate the total weight for each class among the `K` neighbors.
    *   `Total_Weight_Class_j = Σ w_i` for all neighbors `i` belonging to class `j`.
5.  Predict the class label with the **highest total weight**.

### For Regression Tasks
For regression (predicting a continuous value), the process is similar:
1.  Find the `K` nearest neighbors and assign weights.
2.  The predicted value is the **weighted average** of the target values of the `K` neighbors.
    *   `Predicted_Value = (Σ (w_i * y_i)) / (Σ w_i)` where `y_i` is the target value of the `i-th` neighbor.

## 3. Example

Let's consider a simple 2D classification problem to distinguish between Class **A** and Class **B**. We have a query point `Q` and set `K=5`. We find its 5 nearest neighbors.

| Neighbor | Distance from `Q` (`d_i`) | Class | Weight (`w_i = 1/d_i`) |
| :--- | :--- | :--- | :--- |
| **1** | 1.0 | **A** | `1/1.0 = 1.00` |
| **2** | 1.2 | **A** | `1/1.2 ≈ 0.83` |
| **3** | 2.1 | **B** | `1/2.1 ≈ 0.48` |
| **4** | 2.3 | **B** | `1/2.3 ≈ 0.43` |
| **5** | 2.5 | **B** | `1/2.5 = 0.40` |

**Standard KNN (Majority Vote):**
*   Class A votes: 2
*   Class B votes: 3
*   **Prediction: Class B**

**Weighted KNN:**
*   Total Weight for Class A: `1.00 + 0.83 = 1.83`
*   Total Weight for Class B: `0.48 + 0.43 + 0.40 = 1.31`
*   **Prediction: Class A**

Notice how the two very close neighbors from Class A had a much higher combined weight than the three farther neighbors from Class B. WKNN provides a more nuanced and often more accurate prediction in such scenarios.

## 4. Key Points & Summary

*   **Purpose:** WKNN is an enhancement of the KNN algorithm that assigns higher influence to nearer neighbors.
*   **Core Mechanism:** It uses a weighting function, typically the inverse of the distance (`w_i = 1 / d_i`), to assign a vote strength to each neighbor.
*   **Advantage over KNN:** It reduces the impact of noisy or irrelevant distant neighbors, often leading to higher accuracy, especially when the data distribution is uneven.
*   **Calculation:**
    *   For **Classification**: The class with the highest sum of weights is chosen.
    *   For **Regression**: The prediction is the weighted average of the neighbors' target values.
*   **Considerations:**
    *   Like KNN, WKNN is a **lazy learner** (no explicit training phase; all computation is deferred until prediction).
    *   It is **computationally expensive** for large datasets because it requires calculating distances to all training points for each query.
    *   Performance is highly dependent on the choice of `K` and the **distance metric** (Euclidean, Manhattan, etc.).
    *   **Feature scaling** is crucial since the distance metric is sensitive to the scale of the features.