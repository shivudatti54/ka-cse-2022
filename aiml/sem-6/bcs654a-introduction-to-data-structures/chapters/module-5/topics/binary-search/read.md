# Introduction to Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed the possible locations to just one.

## How Binary Search Works

Here's a step-by-step explanation of how binary search works:

1. **Start with a sorted list**: Binary search requires the list to be sorted. If the list is not sorted, the results will be incorrect.
2. **Find the middle element**: Find the middle element of the list.
3. **Compare the target element with the middle element**: Compare the target element with the middle element.
4. **If the target element is equal to the middle element, return the index**: If the target element is equal to the middle element, return the index of the middle element.
5. **If the target element is less than the middle element, repeat the process with the left half**: If the target element is less than the middle element, repeat the process with the left half of the list.
6. **If the target element is greater than the middle element, repeat the process with the right half**: If the target element is greater than the middle element, repeat the process with the right half of the list.
7. **Repeat the process until the target element is found or the list is exhausted**: Repeat the process until the target element is found or the list is exhausted.

## Example of Binary Search

Suppose we have a sorted list of integers: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`. We want to find the index of the element `5` using binary search.

1. **Start with the entire list**: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
2. **Find the middle element**: `5`
3. **Compare the target element with the middle element**: `5` is equal to `5`, so we return the index `4`.

## Time Complexity of Binary Search

The time complexity of binary search is `O(log n)`, where `n` is the number of elements in the list. This is because with each iteration, the size of the list is reduced by half.

## Space Complexity of Binary Search

The space complexity of binary search is `O(1)`, because we only need to store the index of the middle element and the target element.

## Comparison with Linear Search

Binary search is more efficient than linear search for large lists, because it has a lower time complexity. However, for small lists, linear search may be faster because it has a lower overhead.

| Search Algorithm | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Binary Search    | `O(log n)`      | `O(1)`           |
| Linear Search    | `O(n)`          | `O(1)`           |

## Exam Tips

- Make sure to understand the concept of binary search and how it works.
- Practice implementing binary search in code.
- Be able to explain the time and space complexity of binary search.
- Be able to compare binary search with linear search.
