# Linear Binary Search (Binary Search) – Quick Revision  
**Subject:** Design and Analysis of Algorithms  
**Course:** BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)  
**Module:** Searching & Sorting (Unit‑III)

---

### Introduction
Binary Search is a **divide‑and‑conquer** algorithm that efficiently locates a target value in a **sorted array**. It repeatedly halves the search interval, achieving logarithmic time complexity—ideal for large datasets. The algorithm is a core topic in the Delhi University syllabus under *Searching Techniques*.

---

### Key Concepts

- **Precondition:** The input array must be **sorted** (ascending or descending).  
- **Core Idea:** Compare the target with the middle element; if equal, search succeeds; otherwise, discard the half that cannot contain the target and repeat on the remaining half.

- **Algorithm Steps (Iterative)**  
  1. Initialize `low = 0`, `high = n‑1`.  
  2. While `low ≤ high`:  
     - Compute `mid = low + (high - low) // 2` (prevents integer overflow).  
     - If `arr[mid] == target` → return `mid`.  
     - If `arr[mid] < target` → `low = mid + 1`.  
     - Else → `high = mid - 1`.  
  3. If loop ends → target not found (return `-1`).

- **Recursive Version**  
  - Base case: `low > high` → return `-1`.  
  - Recursive step: compute `mid`, then call the function on the appropriate half.  
  - **Space Complexity:** O(log n) due to call stack (vs. O(1) for iterative).

- **Time Complexity**  
  - Best case: O(1) (target at mid).  
  - Worst/Average case: **O(log n)** – the search interval is halved each iteration.

- **Space Complexity**  
  - Iterative: O(1)  
  - Recursive: O(log n)

- **Variations (often asked in exams)**  
  - **Lower Bound:** First occurrence of a given value.  
  - **Upper Bound:** Last occurrence.  
  - **Binary Search on Rotated Arrays** (optional extension).  

- **Common Pitfalls**  
  - Using `(low + high) // 2` can overflow in languages with fixed‑size integers → use `low + (high - low) // 2`.  
  - Forgetting the `=` in the while condition (`low <= high`) leads to missing elements.  

---

### Why It Matters (Exam Perspective)
- **Algorithmic Thinking:** Demonstrates divide‑and‑conquer and logarithmic speed‑up.  
- **Complexity Analysis:** Frequently tested – remember to derive the recurrence T(n) = T(n/2) + O(1).  
- **Implementation:** Be ready to write both iterative and recursive versions, and to spot when binary search is applicable (sorted data).

---

### Conclusion
Binary Search is the textbook example of an O(log n) algorithm, essential for efficient searching in sorted collections. Master its iterative logic, recurrence for time‑complexity, and beware of off‑by‑one errors—these are the points examiners love to test.  

*Revise the code snippets and complexity tables; they are enough to ace the binary‑search portion of the Delhi University DAA paper.*