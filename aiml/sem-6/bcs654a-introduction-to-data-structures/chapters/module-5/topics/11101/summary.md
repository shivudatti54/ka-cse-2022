**11.10.1 Quick Revision Notes**

**Key Concepts:**

- **Sorting Algorithms**: Used to arrange elements in a specific order.
- **Stability**: A sorting algorithm is stable if it maintains the relative order of equal elements.
- **Time Complexity**: Measures the efficiency of an algorithm.
  - Best-case: O(1)
  - Average-case: O(n log n)
  - Worst-case: O(n^2)

**Sorting Algorithms:**

- **Bubble Sort**:
  - Works by repeatedly swapping adjacent elements if they are in the wrong order.
  - Time complexity: O(n^2)
  - Example: `arr = [5, 2, 8, 3, 1];`
  - `for (int i = 0; i < arr.length - 1; i++) {`
  - `    for (int j = 0; j < arr.length - i - 1; j++) {`
  - `        if (arr[j] > arr[j + 1]) {`
  - `            // Swap elements`
  - `        }`
  - `    }`
  - `}`

- **Selection Sort**:
  - Works by repeatedly finding the minimum element from the unsorted part of the array.
  - Time complexity: O(n^2)
  - Example: `arr = [5, 2, 8, 3, 1];`
  - `for (int i = 0; i < arr.length - 1; i++) {`
  - `    min_idx = i;`
  - `    for (int j = i + 1; j < arr.length; j++) {`
  - `        if (arr[j] < arr[min_idx]) {`
  - `            min_idx = j;`
  - `        }`
  - `    }`
  - `    // Swap elements`
  - `}`

- **Insertion Sort**:
  - Works by inserting each element into its proper position in the sorted part of the array.
  - Time complexity: O(n^2)
  - Example: `arr = [5, 2, 8, 3, 1];`
  - `for (int i = 1; i < arr.length; i++) {`
  - `    key = arr[i];`
  - `    j = i - 1;`
  - `    while (j >= 0 && key < arr[j]) {`
  - `        arr[j + 1] = arr[j];`
  - `        j--;`
  - `    }`
  - `    arr[j + 1] = key;`
  - `}`

**Important Formulas:**

- **Big O Notation**: O(1) = constant time complexity
- **Average-case Time Complexity**: O(n log n) for comparison-based sorting algorithms
- **Worst-case Time Complexity**: O(n^2) for comparison-based sorting algorithms

**Important Definitions:**

- **Stable Sorting Algorithm**: Maintains the relative order of equal elements
- **Unstable Sorting Algorithm**: May not maintain the relative order of equal elements

**Important Theorems:**

- **Comparison-based Sorting Algorithm**: Requires at least n log n comparisons to sort n elements
- **Optimal Time Complexity**: O(n log n) is the optimal time complexity for comparison-based sorting algorithms
