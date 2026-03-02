# Recurrence Master Theorem – Quick Revision  

**Introduction**  
The Master Theorem gives a **closed‑form asymptotic** solution for recurrences of the form  

\[
T(n)=a\,T\!\left(\frac{n}{b}\right)+f(n)\qquad(a\ge 1,\;b>1,\;f(n)>0)
\]

which arise when an algorithm **divides** a problem into *a* sub‑problems each of size *n/b* and **conquers** them recursively, then **combines** the results in *f(n)* time. It is a core topic of the **Ge4A Data Structures** unit in the Delhi University B.Sc. (Physical Science – CS) NEP 2024 syllabus (Unit‑III: Analysis of Algorithms).

**Key Points**  

- **Applicability** – Works for recurrences where the sub‑problem size is exact (no floors/ceilings) and *f(n)* is asymptotically positive.  
- **Notation** – *a* = number of sub‑problems, *b* = size reduction factor, *f(n)* = cost of the combine step.  
- **Critical exponent** – Compute \(\log_b a\); this exponent determines the dominant term of the solution.  
- **Three cases**  
  1. **\(f(n)=O\!\big(n^{\log_b a-\varepsilon}\big)\)** (polynomially smaller) ⇒ \(T(n)=\Theta\big(n^{\log_b a}\big)\).  
  2. **\(f(n)=\Theta\big(n^{\log_b a}\big)\)** (same order) ⇒ \(T(n)=\Theta\big(n^{\log_b a}\log n\big)\).  
  3. **\(f(n)=\Omega\!\big(n^{\log_b a+\varepsilon}\big)\)** (polynomially larger) **and** the **regularity condition** \(a\,f(n/b)\le c\,f(n)\) for some \(c<1\) ⇒ \(T(n)=\Theta\big(f(n)\big)\).  
- **Proof intuition** – Summing work at each level of the recursion tree yields a geometric series; the dominant term depends on the ratio between *f(n)* and \(n^{\log_b a}\).  
- **Common examples**  
  - MergeSort: \(T(n)=2T(n/2)+\Theta(n)\) → \(a=2,\;b=2,\;\log_2 2=1\) → **Θ(n log n)** (case 2).  
  - Binary Search: \(T(n)=T(n/2)+\Theta(1)\) → \(a=1,\;b=2,\;\log_2 1=0\) → **Θ(log n)** (case 1).  
  - Strassen: \(T(n)=7T(n/2)+\Theta(n^2)\) → \(\log_2 7\approx2.81\) → **Θ(n^{2.81})** (case 1).  
- **Limitations** – Does **not** cover:  
  - Non‑polynomial *f(n)* (e.g., \(n^{\log n}\)).  
  - Cases where the exponent difference is not polynomial (use the **Extended Master Theorem** for \(f(n)=\Theta(n^{\log_b a}\log^k n)\)).  
  - Recurrences with floors/ceilings or variable splitting (generalised by the **Akra‑Bazzi method**).  
- **Relation to other methods** – Complements the **substitution method** (guess‑and‑verify) and **recursion‑tree** approach; Akra‑Bazzi extends the theorem to more general forms.

**Conclusion**  
The Master Theorem is a **fast, systematic** tool for analysing divide‑and‑conquer recurrences, enabling quick identification of the asymptotic running time of many classic algorithms. Master its three cases, the regularity condition, and its limits to ace exam questions on algorithm analysis (Delhi University NEP 2024).