# **Sequential Searching**

## **Introduction**

Sequential searching is a simple searching algorithm that looks for a specific element in a list or array by comparing each element one by one, starting from the first element. This algorithm is also known as linear searching.

## **How it Works**

Here's a step-by-step explanation of the sequential searching algorithm:

1.  Start at the first element of the list or array.
2.  Compare the current element with the target element.
3.  If they match, return the index of the current element.
4.  If the current element is greater than the target element, move to the next element.
5.  If the current element is less than the target element, move to the previous element.
6.  Repeat steps 2-5 until the target element is found or the end of the list or array is reached.

## **Example**

Suppose we have a list of numbers: `[3, 1, 4, 1, 5, 9, 2, 6]`. We want to find the index of the number `5` using sequential searching.

1.  Start at the first element (`3`).
2.  Compare `3` with `5`. They don't match.
3.  Move to the next element (`1`).
4.  Compare `1` with `5`. They don't match.
5.  Move to the next element (`4`).
6.  Compare `4` with `5`. They don't match.
7.  Move to the next element (`1`).
8.  Compare `1` with `5`. They match!
9.  Return the index of the current element, which is `4`.

## **Time Complexity**

The time complexity of sequential searching is O(n), where n is the number of elements in the list or array. This is because in the worst-case scenario, we have to compare each element with the target element.

## **Advantages and Disadvantages**

Advantages:

- Simple to implement.
- Efficient for small lists or arrays.
- Works for any type of data (numbers, strings, etc.).

Disadvantages:

- Inefficient for large lists or arrays.
- May take a long time to find the target element.

## **Best Practices**

- Use sequential searching for small lists or arrays.
- Consider using more efficient algorithms like binary searching for larger lists or arrays.
- Always check if the target element is present at the end of the list or array before starting the search.

## **Code Implementation**

Here's an example implementation of sequential searching in Python:

```python
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target element not found

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6]
target = 5
index = sequential_search(arr, target)

if index != -1:
    print(f"Target element {target} found at index {index}.")
else:
    print(f"Target element {target} not found in the array.")
```

This implementation takes an array and a target element as input, and returns the index of the target element if found. If the target element is not found, it returns -1.
