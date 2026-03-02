# Linear Search Fundamentals

## What is Linear Search?

Linear search (also called sequential search) is the simplest searching algorithm. It works by checking each element in a collection one by one, from the beginning to the end, until the target element is found or the entire collection has been searched.

## How It Works

1. Start from the **first element** of the array
2. **Compare** the current element with the target value
3. If they **match**, return the current index
4. If they **don't match**, move to the next element
5. **Repeat** steps 2-4 until:
   - The target is found (return index), OR
   - The end of array is reached (return -1, not found)

## When to Use Linear Search

**Use when:**

- Data is **unsorted** (binary search won't work)
- Collection is **small** (n < 100)
- Searching **only once** (no benefit from sorting)
- Data stored in **linked list** (random access not available)

**Avoid when:**

- Data is **sorted** (use binary search instead)
- Collection is **large** and searched frequently
- Performance is critical

## Time and Space Complexity

| Case    | Time Complexity | Explanation                            |
| ------- | --------------- | -------------------------------------- |
| Best    | O(1)            | Target found at first position         |
| Average | O(n/2) = O(n)   | Target found in middle on average      |
| Worst   | O(n)            | Target at last position or not present |

**Space Complexity:** O(1) - only uses a few variables regardless of input size

## Real-World Analogies

1. **Finding a book on an unsorted shelf** - You check each book left to right until you find the one you want

2. **Looking for a friend in a crowd** - You scan faces one by one until you spot your friend

3. **Finding a word in an unsorted word list** - Check each word from top to bottom

## Variations

### 1. Sentinel Linear Search

Places the target at the end of array to eliminate bounds checking in the loop.

### 2. Bidirectional Linear Search

Searches from both ends simultaneously, potentially halving the search time.

### 3. Linear Search with Transposition

Moves found elements one position forward, optimizing for frequently searched items.

## Summary

- Linear search is the **simplest** search algorithm
- Works on **any** collection (sorted or unsorted)
- **O(n)** time complexity - checks each element once
- **O(1)** space - no extra memory needed
- Best for **small or unsorted** data
- Foundation for understanding more complex algorithms
