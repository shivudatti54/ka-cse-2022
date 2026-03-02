# **Statistical Machine Learning for Data Science**

## **Module: Discriminant Analysis**

### Covariance Matrix and Fisher's Linear Discriminant

In discriminant analysis, the goal is to find a linear combination of features that can be used to distinguish between two or more classes. To achieve this, we need to calculate the covariance matrix and the Fisher's linear discriminant.

## **What is a Covariance Matrix?**

The covariance matrix is a square matrix that summarizes the covariance between each pair of features in a dataset. It is a measure of how much each feature varies from the mean of that feature.

## **What is a Fisher's Linear Discriminant?**

The Fisher's linear discriminant is a linear combination of features that maximizes the separation between the means of the different classes. It is a scalar value that represents the direction of the line that maximizes the separation between the classes.

## **Calculating the Sample Mean for Each Class**

To calculate the sample mean for each class, we need to first calculate the mean of each feature for each class. The sample mean is the average value of a feature in a dataset.

## **Example: Calculating the Sample Mean**

Suppose we have a dataset with two features, X1 and X2, and two classes, Class A and Class B. The dataset is shown below:

| X1  | X2  | Class |
| --- | --- | ----- |
| 10  | 20  | A     |
| 15  | 25  | A     |
| 12  | 22  | B     |
| 18  | 30  | B     |

To calculate the sample mean for each class, we need to calculate the mean of each feature for each class.

- For Class A:

* Mean of X1: (10 + 15 + 12) / 3 = 13.67
* Mean of X2: (20 + 25 + 22) / 3 = 23.33

- For Class B:

* Mean of X1: (18 + 12) / 2 = 15
* Mean of X2: (30 + 25) / 2 = 27.5

## **Key Concepts**

- **Sample mean**: The average value of a feature in a dataset.
- **Covariance matrix**: A square matrix that summarizes the covariance between each pair of features in a dataset.
- **Fisher's linear discriminant**: A linear combination of features that maximizes the separation between the means of the different classes.

## **Code Example**

Here is an example of how to calculate the sample mean for each class in Python:

```python
import numpy as np

# Define the dataset
X = np.array([[10, 20], [15, 25], [12, 22], [18, 30]])
y = np.array([0, 0, 1, 1])

# Calculate the sample mean for each class
mean_A = np.mean(X[y == 0, :], axis=0)
mean_B = np.mean(X[y == 1, :], axis=0)

print("Mean of Class A: ", mean_A)
print("Mean of Class B: ", mean_B)
```

This code calculates the sample mean for each class by taking the mean of each feature for each class.

### Interpreting the Results

---

The results of the sample mean calculation can be used to understand the characteristics of each class. For example, we can see that Class A has a mean X1 of 13.67 and a mean X2 of 23.33, while Class B has a mean X1 of 15 and a mean X2 of 27.5.

## **Conclusion**

In this study material, we learned how to calculate the sample mean for each class in discriminant analysis. We saw how to calculate the covariance matrix and the Fisher's linear discriminant, and how to use these results to understand the characteristics of each class.
