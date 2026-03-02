# **Features, The Basics of NumPy Arrays, Sorted Arrays, Structured Data: Quick Revision Notes**

## **Features**

- Features are independent variables in a dataset that can be used to predict the dependent variable.
- Examples: age, occupation, income, etc.
- Important in data analysis, machine learning, and data visualization.

## **The Basics of NumPy Arrays**

- NumPy arrays are multi-dimensional collections of elements.
- Each element is of a fixed data type (e.g., int, float, complex).
- Arrays can be created using the `numpy.array()` function.

## **Sorted Arrays**

- A sorted array is a NumPy array whose elements are in ascending or descending order.
- Can be created using the `numpy.sort()` function.
- Example: `numpy.sort([3, 1, 2, 4])` returns `[1, 2, 3, 4]`.

## **Structured Data: NumPy’s Structured Arrays**

- Structured arrays are NumPy arrays with a fixed data type and a specific structure.
- Can contain multiple columns of data.
- Example: `numpy.dtype([('name', object), ('age', int)])`
- Created using the `numpy.dtype()` function.

## **Important Formulas, Definitions, and Theorems**

- **Mean**: The average value of an array, calculated as the sum of all elements divided by the number of elements.
  - Formula: `mean = sum / N`
- **Median**: The middle value of an array when sorted in ascending order.
  - Formula: `median = (sum of elements at 0 and length - 1) / 2`
- **Standard Deviation**: A measure of the spread or dispersion of an array from its mean value.
  - Formula: `stddev = sqrt(sum ((x_i - mean)^2) / N)`
- **Correlation Coefficient**: A measure of the linear relationship between two arrays.
  - Formula: `corr = sum ((x_i - mean_x) \* (y_i - mean_y)) / sqrt(sum ((x_i - mean_x)^2) \* sum ((y_i - mean_y)^2))`

Note: This summary is a quick revision guide and is not intended to be a comprehensive study guide.
