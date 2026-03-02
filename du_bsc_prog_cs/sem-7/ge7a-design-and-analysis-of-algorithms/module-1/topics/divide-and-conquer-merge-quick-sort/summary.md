**Divide‑and‑Conquer – Merge Sort & Quick Sort**  
*(Ge7A Design & Analysis of Algorithms – DU NEP 2024, Unit III – Sorting)*  

---

### Introduction  
Divide‑and‑Conquer (D&C) is a classic algorithm design paradigm that solves a problem by:  
1. **Dividing** it into sub‑problems that are smaller instances of the same problem,  
2. **Conquering** (solving) each sub‑problem recursively, and  
3. **Merging** the solutions to obtain the final result.  

Merge Sort and Quick Sort are the two canonical D&C sorting algorithms taught in the Delhi University B.Sc. (Physical Science) CS syllabus.

---

### Key Concepts  

- **Merge Sort**  
  - **Divide:** Split the array into two roughly equal halves.  
  - **Conquer:** Recursively sort each half.  
  - **Merge:** Combine the two sorted halves in O(n) time using a helper function.  
  - **Time Complexity:**  
    - *Worst‑case / Average / Best*: **Θ(n log n)**.  
  - **Space:** **Θ(n)** extra space for the temporary array (not in‑place).  
  - **Stability:** Stable – equal elements retain their relative order.  
  - **Use‑case:** Preferred when stable sorting and guaranteed O(n log n) performance are required (e.g., external sorting).

- **Quick Sort**  
  - **Divide (Partition):** Choose a **pivot**; rearrange the array so all elements ≤ pivot are on the left and > pivot on the right.  
  - **Conquer:** Recursively apply Quick Sort to the left and right sub‑arrays.  
  - **Merge:** No explicit merge step – the concatenated partitions already form a sorted array.  
  - **Time Complexity:**  
    - *Worst‑case*: **Θ(n²)** (when pivot is always smallest/largest).  
    - *Average / Best*: **Θ(n log n)** (random or median‑of‑three pivot).  
  - **Space:** **O(log n)** stack space for recursion (in‑place).  
  - **Stability:** Not stable.  
  - **Use‑case:** In‑place, fast in practice for arrays; often the default internal sorting routine.

- **Recurrence Relations**  
  - Merge Sort: `T(n) = 2 T(n/2) + Θ(n) ⇒ T(n)=Θ(n log n)` (by Master Theorem).  
  - Quick Sort (average): `T(n) = 2 T(n/2) + Θ(n) ⇒ T(n)=Θ(n log n)`.  

- **Pivot Selection Strategies**  
  - First / Last element – simple but vulnerable to worst‑case.  
  - Random index – reduces probability of worst‑case.  
  - Median‑of‑three – improves balance.

- **Practical Notes**  
  - Hybrid algorithms (e.g., IntroSort) combine Quick Sort’s speed with Merge Sort’s guarantees.  
  - For **linked lists**, Merge Sort is preferred (no random access).  
  - For **small sub‑arrays** (size ≤ 10–15), insertion sort is often faster due to lower overhead.

---

### Conclusion  
Both Merge Sort and Quick Sort embody the divide‑and‑conquer principle, offering Θ(n log n) average performance. Merge Sort provides stability and predictable run‑time but requires extra space; Quick Sort is in‑place and usually faster in practice but is not stable and can degrade to Θ(n²). Understanding their trade‑offs is essential for selecting the right sorting method in algorithm design and for exam success in Ge7A.