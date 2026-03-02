# Sequential Searching

### Definition

- Sequential searching is a simple searching algorithm where the search key is compared one by one with each element in the sequence (array or list) until a match is found.

### Key Points

- **Time Complexity:**
  - Best-case: O(1) (when the search key is the first element)
  - Average-case: O(n) (when the search key is somewhere in the sequence)
  - Worst-case: O(n) (when the search key is not in the sequence)
- **Approach:**
  1.  Start at the first element of the sequence.
  2.  Compare the search key with the current element.
  3.  If they match, return the current element as the result.
  4.  If not, move to the next element and repeat step 2.
- **Important Formulas:**

- Linear search formula: `T(n) = n`
- Worst-case scenario: `T(n) = n`

### Important Definitions

- **Linear Search:** A searching algorithm that searches for an element in a sequence by comparing each element one by one.
- **Sequence:** An ordered list of elements.

### Important Theorems

- **Linear Search Theorem:** If we have a sequence of `n` elements and we search for an element in linear search, the time complexity is `O(n)`.
- **Optimality Theorem:** Linear search is the optimal searching algorithm for sequences of size `n`.

### Important Concepts

- **Array Search:** A searching algorithm that searches for an element in an array by comparing each element one by one.
- **List Search:** A searching algorithm that searches for an element in a list by comparing each element one by one.

### Notes

- Sequential searching is not an efficient algorithm for large datasets due to its high time complexity.
- It is often used for small datasets or when the search key is expected to be the first occurrence.
