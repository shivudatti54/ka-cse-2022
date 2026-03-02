# **BRUTE FORCE APPROACHES: Selection Sort and Bubble Sort**

### Introduction

- Brute force approaches are simple, yet inefficient algorithms that solve problems by trying all possible solutions.
- Selection Sort and Bubble Sort are two commonly used brute force algorithms.

### Selection Sort

---

- **Definition:** Selection Sort is a sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first unsorted element.
- **Time Complexity:** O(n^2)
- **Formula:** `arr[i] = min(arr[0..i-1])`
- **Example:** `arr[0] = min(arr[1..n-1])`
- **Step 1:** Find the minimum element in the unsorted part of the array.
- **Step 2:** Swap the minimum element with the first unsorted element.

### Bubble Sort

---

- **Definition:** Bubble Sort is a sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
- **Time Complexity:** O(n^2)
- **Formula:** `if (arr[i] > arr[i+1]) { swap(arr[i], arr[i+1]) }`
- **Example:** If `arr[0] > arr[1]`, swap them.
- **Step 1:** Compare adjacent elements.
- **Step 2:** Swap adjacent elements if they are in the wrong order.

### Important Theorems

- **Big O Notation:** The time complexity of an algorithm is expressed as a function of the size of the input, typically denoted as n.
- **Worst-Case Scenario:** The worst-case scenario occurs when the input is sorted in reverse order.

### Key Points

- Brute force approaches are simple to implement but inefficient.
- Selection Sort and Bubble Sort have a time complexity of O(n^2).
- Both algorithms are not suitable for large datasets.
- The choice of algorithm depends on the specific problem and requirements.
