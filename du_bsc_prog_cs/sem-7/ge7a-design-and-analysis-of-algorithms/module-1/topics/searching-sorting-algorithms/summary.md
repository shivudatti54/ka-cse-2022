**Searching & Sorting Algorithms – Quick Revision**  
*(Reference: Delhi University BSc (Physical Science) CS – NEP 2024 Syllabus)*  

---

### Introduction  
Searching and sorting are fundamental algorithmic tasks. The syllabus requires knowledge of classic methods, their time‑space complexities, and the trade‑offs that dictate which algorithm to use in practice.

---

### Searching Algorithms  

- **Linear Search** – scan each element sequentially.  
  - *Time*: O(n) (worst/average).  
  - *Space*: O(1).  
  - Works on unsorted data.

- **Binary Search** – repeatedly halve a **sorted** interval.  
  - *Time*: O(log n).  
  - *Space*: O(1) (iterative) or O(log n) (recursive).  
  - Requires random‑access (array) and sorted input.

- **Hash Table (optional)** – average O(1) search via a hash function, but outside the core syllabus for exams.

---

### Sorting Algorithms  

#### 1. Comparison‑based O(n²) Sorts  
| Algorithm | Stable? | In‑place? | Best / Avg / Worst | Remarks |
|-----------|---------|-----------|--------------------|---------|
| **Bubble Sort** | Yes | Yes | O(n) / O(n²) / O(n²) | Simple; stops early if no swaps. |
| **Insertion Sort** | Yes | Yes | O(n) / O(n²) / O(n²) | Efficient for small or nearly sorted data. |
| **Selection Sort** | No | Yes | O(n²) / O(n²) / O(n²) | Minimizes swaps; not stable. |

#### 2. Comparison‑based O(n log n) Sorts  
| Algorithm | Stable? | In‑place? | Best / Avg / Worst | Remarks |
|-----------|---------|-----------|--------------------|---------|
| **Merge Sort** | Yes | No (needs O(n) aux) | O(n log n) / O(n log n) / O(n log n) | Ideal for linked lists; divides & conquers. |
| **Quick Sort** | No | Yes | O(n log n) / O(n log n) / O(n²) | Partition‑based; performance hinges on pivot choice. |
| **Heap Sort** | No | Yes | O(n log n) / O(n log n) / O(n log n) | Uses binary‑heap; guaranteed O(n log n) worst case. |

#### 3. Linear‑time (Non‑comparison) Sorts  
- **Counting Sort** – works for bounded integer keys.  
  - *Time*: O(n + k); *Space*: O(k).  
  - Stable when implemented carefully.  

- **Radix Sort** – sorts digit‑by‑digit using a stable sub‑sort (e.g., Counting Sort).  
  - *Time*: O(nk) where k = number of digits.  
  - Stable; often faster than comparison sorts for large n with small digit count.

---

### Complexity & Trade‑offs  

- **Stability** matters when preserving order of equal keys (e.g., database records).  
- **In‑place** algorithms use O(1) extra memory; useful when memory is limited.  
- **Best‑case** performance: O(n) for bubble/insertion if data already sorted.  
- **Worst‑case** matters for safety‑critical or large‑scale inputs; heap/merge guarantee O(n log n).  

---

### Conclusion  
For the Delhi University exam, focus on the algorithmic steps, big‑O notation, and when each method is preferable. Remember:  
- Use **linear search** for tiny or unsorted lists.  
- Use **binary search** on sorted arrays.  
- Choose **O(n²) sorts** for small or nearly sorted data; **O(n log n) sorts** for general large data; **linear sorts** when keys are integers within a known range.  

Mastering these concepts ensures you can pick the right tool for any searching or sorting problem.