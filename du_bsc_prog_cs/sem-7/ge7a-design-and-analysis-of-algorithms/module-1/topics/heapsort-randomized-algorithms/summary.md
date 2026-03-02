## Heapsort & Randomized Algorithms (Ge7A – Design & Analysis of Algorithms, DU NEP 2024)

**Introduction**  
Heapsort is a deterministic, in‑place comparison sort that relies on the binary‑heap data structure. Randomized algorithms augment classic deterministic approaches with randomness to improve expected run‑time or to avoid pathologically bad inputs; the classic examples are randomized QuickSort and QuickSelect.

### Heapsort (Deterministic Sorting)
- **Binary heap**: complete binary tree stored as an array; *max‑heap* (parent ≥ children) is used for ascending order.
- **Heapify (sift‑down)**: recursively restores the heap property in O(log n) by moving a node down to its correct position.
- **Build‑heap**: Floyd’s bottom‑up heap construction runs in Θ(n) time.
- **Sorting phase**: repeatedly swap the root (largest element) with the last unsorted position, reduce the heap size, and heapify the new root – each extraction costs O(log n).
- **Overall complexity**: Θ(n log n) worst‑case (no best/worst‑case distinction).
- **Space**: O(1) auxiliary (in‑place).
- **Stability**: not stable; equal keys may change relative order.
- **Use in exams**: emphasize the heap invariants, the linear‑time heap build, and the O(n log n) guarantee.

### Randomized Algorithms (Performance via Randomness)
- **Why randomize?** To make worst‑case inputs unlikely, giving better *expected* run‑time while preserving correctness.
- **Randomized QuickSort**  
  - Choose pivot uniformly at random (or shuffle the array first).  
  - Expected number of comparisons = Θ(n log n); probability of O(n²) worst‑case is < 1/n for large n.
- **Randomized Selection (QuickSelect)**  
  - Find the k‑th smallest element using a random pivot.  
  - Expected time Θ(n); worst‑case Θ(n²) but exponentially unlikely.
- **Types of randomized algorithms**  
  - *Monte Carlo*: may return an incorrect answer with bounded error (e.g., randomized primality test).  
  - *Las Vegas*: always correct; only runtime is random (e.g., randomized QuickSort).
- **Analysis tools**: indicator random variables, linearity of expectation, probability bounds (Chernoff, Markov).
- **Other examples** (for quick revision): randomized skip lists, universal hashing, randomized approximation algorithms.

**Conclusion**  
Heapsort offers deterministic Θ(n log n) performance with O(1) space, while randomized algorithms (most notably QuickSort and QuickSelect) trade a negligible probability of worst‑case behaviour for an expected linear or linear‑logarithmic runtime. Both topics are core to the Ge7A DAA syllabus and frequently appear in Delhi University examinations.