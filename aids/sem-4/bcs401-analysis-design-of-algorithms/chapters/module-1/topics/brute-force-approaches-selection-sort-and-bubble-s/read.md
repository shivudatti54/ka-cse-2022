# **BRUTE FORCE APPROACHES: Selection Sort and Bubble Sort**

## **Introduction**

Brute force approaches are inefficient algorithms that use simple, repetitive steps to solve a problem. They often rely on comparing elements to find the minimum or maximum value, which can lead to a time complexity of O(n^2) in the worst case. However, understanding these algorithms is crucial for grasping the basics of algorithmic problem-solving.

## **Selection Sort**

### Definition

Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element.

### How it Works

1.  Start from the first element of the array.
2.  Compare the current element with the remaining unsorted elements.
3.  Find the minimum element from the unsorted part of the array.
4.  Swap the current element with the minimum element.
5.  Move to the next element and repeat the process until the entire array is sorted.

### Example

Suppose we have an array of integers: `[64, 25, 12, 22, 11]`.

1.  Start with the first element: `64`.
2.  Compare `64` with the remaining elements: `25`, `12`, `22`, `11`.
3.  Find the minimum element: `11`.
4.  Swap `64` with `11`: `[11, 25, 12, 22, 64]`.
5.  Move to the next element: `25`.
6.  Compare `25` with the remaining elements: `12`, `22`, `64`.
7.  Find the minimum element: `12`.
8.  Swap `25` with `12`: `[11, 12, 25, 22, 64]`.
9.  Move to the next element: `22`.
10. Compare `22` with the remaining element: `64`.
11. Find the minimum element: `22`.
12. Swap `22` with `64`: `[11, 12, 22, 64, 25]`.
13. Move to the next element: `25`.
14. Compare `25` with the remaining unsorted element: `64`.
15. Find the minimum element: `64`.
16. Swap `25` with `64`: `[11, 12, 22, 64, 25]`.

The array is now sorted: `[11, 12, 22, 25, 64]`.

### Code

```python
def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the current element with the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
```

## **Bubble Sort**

### Definition

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.

### How it Works

1.  Start from the first element of the array.
2.  Compare the current element with the next element.
3.  If the current element is greater than the next element, swap them.
4.  Repeat the process until the end of the array is reached.
5.  Repeat the entire process until no more swaps are needed, indicating that the array is sorted.

### Example

Suppose we have an array of integers: `[64, 25, 12, 22, 11]`.

1.  Start with the first element: `64`.
2.  Compare `64` with the next element: `25`.
3.  Since `64` is greater than `25`, swap them: `[25, 64, 12, 22, 11]`.
4.  Move to the next element: `12`.
5.  Compare `12` with the next element: `22`.
6.  Since `12` is less than `22`, no swap is needed.
7.  Move to the next element: `22`.
8.  Compare `22` with the next element: `11`.
9.  Since `22` is greater than `11`, swap them: `[25, 64, 12, 11, 22]`.
10. Move to the next element: `64`.
11. Compare `64` with the next element: `12`.
12. Since `64` is greater than `12`, swap them: `[25, 64, 12, 11, 22]`.
13. Move to the next element: `11`.
14. Compare `11` with the next element: `22`.
15. Since `11` is less than `22`, no swap is needed.

The array is now sorted: `[11, 12, 22, 25, 64]`.

### Code

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements and swap them if they are in the wrong order
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If there were no swaps during the last iteration, the array is already sorted, and we can terminate
        if not swapped:
            break
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
print(bubble_sort(arr))  # [11, 12, 22, 25, 64]
```

## **Comparison of Selection Sort and Bubble Sort**

|                      | Selection Sort                   | Bubble Sort                      |
| -------------------- | -------------------------------- | -------------------------------- |
| **Time Complexity**  | O(n^2)                           | O(n^2)                           |
| **Space Complexity** | O(1)                             | O(1)                             |
| **Stability**        | Stable                           | Unstable                         |
| **Efficiency**       | Not efficient for large datasets | Not efficient for large datasets |

In conclusion, while selection sort and bubble sort are simple to understand and implement, they are not efficient for large datasets. They have a time complexity of O(n^2), which makes them impractical for real-world applications. However, they can serve as useful examples for illustrating basic sorting concepts and techniques.
