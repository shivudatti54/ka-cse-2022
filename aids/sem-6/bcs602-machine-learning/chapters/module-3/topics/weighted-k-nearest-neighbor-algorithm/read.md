Of course. Here is a comprehensive educational note on the Weighted K-Nearest-Neighbor Algorithm for  Engineering students.

# **Machine Learning - Module 3: Weighted K-Nearest-Neighbor (WKNN) Algorithm**

## **1. Introduction**

The K-Nearest-Neighbor (KNN) algorithm is one of the simplest and most intuitive classification and regression algorithms in machine learning. It operates on the principle that similar data points exist in close proximity within the feature space. However, a significant limitation of standard KNN is that it gives equal importance (or vote) to all `K` neighbors, regardless of their distance from the query point. The **Weighted K-Nearest-Neighbor (WKNN)** algorithm enhances the basic KNN by addressing this very issue. It assigns a weight to each neighbor's vote, giving more influence to the points that are closer to the data point being classified.

---

## **2. Core Concepts Explained**

### **The Limitation of Standard KNN**
Imagine a scenario where you are using `K=5` neighbors to classify a new data point `X`. Three neighbors are relatively far away and belong to **Class A**, while the other two are very close and belong to **Class B**. Standard KNN would classify `X` as **Class A** because it's a majority vote. This seems counter-intuitive because the closer, more similar neighbors are being overshadowed by more distant, less relevant points.

### **How WKNN Solves This Problem**
WKNN introduces the concept of **weighting**. The core idea is simple: **"The closer a neighbor is, the more influence its vote should have."**

This is achieved by assigning a weight to each of the `K` neighbors. The weight is a function of the distance between the neighbor and the query point. The most common weighting function is the **inverse of the distance** or the **inverse of the squared distance**.

### **The Weighting Function**
For a query point `X_q`, the weight `w_i` for the `i-th` neighbor `X_i` is calculated as:

**`w_i = 1 / (d(X_q, X_i)^p`**

Where:
*   `d(X_q, X_i)` is the distance (e.g., Euclidean, Manhattan) between the query point and the neighbor.
*   `p` is a power parameter. Commonly, `p=1` (inverse distance) or `p=2` (inverse squared distance) is used.

**Important:** If `d(X_q, X_i) = 0` (i.e., an exact match), the weight would become undefined (division by zero). To avoid this, the algorithm can simply assign the class of that exact matching point, or a very high weight is assigned.

### **The Classification Process in WKNN**
1.  **Compute Distances:** Calculate the distance from the query point `X_q` to every point in the training set.
2.  **Identify Neighbors:** Identify the `K` points in the training data closest to `X_q` (the neighbors).
3.  **Calculate Weights:** For each of the `K` neighbors, compute its weight `w_i` using the weighting function.
4.  **Tally Weighted Votes:**
    *   For a **classification** task, sum the weights for each class among the `K` neighbors.
    *   The class with the highest total weighted sum is the predicted class.
5.  **(For Regression):** For a **regression** task, the predicted value is the weighted average of the target values of the `K` neighbors.
    `prediction = (sum(w_i * y_i)) / (sum(w_i))`

---

## **3. Example**

Let's solidify this with a simple 2D classification example. We want to classify a new query point `X_q = (5.0, 5.0)`.

Our training data has four points with their classes:
*   `A = (4.0, 4.5), Class = Red`
*   `B = (5.5, 5.5), Class = Blue`
*   `C = (6.0, 5.0), Class = Blue`
*   `D = (3.5, 4.0), Class = Red`

Let's use `K=3` and Euclidean distance (`p=2` for inverse squared distance).

**Step 1 & 2: Compute Distances and Find 3 Nearest Neighbors**
*   `d(X_q, A) = sqrt((5-4)^2 + (5-4.5)^2) = sqrt(1 + 0.25) ≈ 1.12`
*   `d(X_q, B) = sqrt((5-5.5)^2 + (5-5.5)^2) = sqrt(0.25 + 0.25) ≈ 0.71` **(Closest)**
*   `d(X_q, C) = sqrt((5-6)^2 + (5-5)^2) = sqrt(1 + 0) = 1.00`
*   `d(X_q, D) = sqrt((5-3.5)^2 + (5-4)^2) = sqrt(2.25 + 1) ≈ 1.80`

The 3 nearest neighbors are **B, C, and A**.

**Step 3: Calculate Weights (using `1 / distance^2`)**
*   `w_B = 1 / (0.71)^2 ≈ 1 / 0.5 ≈ 2.00`
*   `w_C = 1 / (1.00)^2 = 1 / 1 = 1.00`
*   `w_A = 1 / (1.12)^2 ≈ 1 / 1.25 ≈ 0.80`

**Step 4: Tally Weighted Votes**
*   **Class Blue (B and C):** `w_B + w_C = 2.00 + 1.00 = 3.00`
*   **Class Red (A):** `w_A = 0.80`

The total weighted vote for **Blue (3.00)** is significantly higher than for Red (0.80). Therefore, WKNN confidently classifies `X_q` as **Class Blue**.

**Comparison with Standard KNN:** Standard KNN would see 2 Blues (B, C) and 1 Red (A) and also predict Blue. However, in this case, the weights strongly confirm the decision. If point A was slightly closer and point C was slightly farther, the weighted vote could change the outcome, demonstrating its superior nuance.

---

## **4. Key Points & Summary**

| **Aspect** | **Description** |
| :--- | :--- |
| **Core Idea** | An enhancement of KNN where neighbors' votes are weighted by their inverse distance to the query point. |
| **Advantage over KNN** | More robust and accurate. It gives more importance to closer, more similar neighbors, reducing the influence of noisy or irrelevant distant points. |
| **Key Formula** | `weight = 1 / (distance^p)`. `p=1` or `p=2` are most common. |
| **Use Case** | Primarily used for classification, but can be easily adapted for regression tasks by taking a weighted average. |
| **Considerations** | • Still requires choosing an optimal `K` value.<br>• Sensitive to the choice of distance metric.<br>• Computationally expensive for large datasets (like KNN).<br>• Requires meaningful distance calculations (feature scaling is crucial). |
| **Why it matters** | WKNN is a simple yet powerful refinement that often leads to more accurate and reliable predictions than its standard counterpart, making it a valuable tool in the machine learning toolbox. |