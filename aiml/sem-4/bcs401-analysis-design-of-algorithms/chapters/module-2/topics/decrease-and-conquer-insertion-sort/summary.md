# **DECREASE-AND-CONQUER: Insertion Sort**

## **Overview**

Insertion Sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## **Key Points**

- **Time Complexity**: O(n^2) in the worst case and O(n) in the best case
- **Space Complexity**: O(1)
- **Stability**: Yes
- **Description**:
  - Divide the input into a sorted and an unsorted region
  - Iterate through the unsorted region, comparing each element with the sorted region
  - Insert each element into its correct position in the sorted region
- **Key Formulas/Definitions/Theorems**:
  - **Insertion Sort Formula**: `T(n) = T(n-1) + O(n)`
  - **Definition**: An n-element array is said to be sorted if `arr[i] <= arr[j]` for all `i <= j`
  - **Theorem**: The best-case time complexity of Insertion Sort is O(n) when the input array is already sorted

## **How it Works**

- Initialize the sorted region with the first element of the input array
- Iterate through the unsorted region, comparing each element with the sorted region
- If an element is smaller than the current element in the sorted region, shift the element to the left
- Insert the element into its correct position in the sorted region
- Repeat until the entire input array is sorted

## **Advantages**

- Simple to implement
- Efficient for small datasets
- In-place sorting (no extra memory needed)

## **Disadvantages**

- Not efficient for large datasets (O(n^2) time complexity)
- Not suitable for data with duplicate elements (can lead to inefficient insertion)
