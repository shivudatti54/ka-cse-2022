# Sequences & Summations – Quick Revision  
**B.Sc. (H) Computer Science – Delhi University (NEP 2024 UGCF)**  
*Unit 2 of Discrete Mathematical Structures*

---

### Introduction  
A **sequence** is an ordered list of numbers defined explicitly or by a recurrence relation, while a **summation** (or series) adds the terms of a sequence. This unit, prescribed in the Delhi University B.Sc. (H) CS syllabus (NEP 2024 UGCF), introduces definitions, common types, and evaluation techniques—essential for algorithmic analysis and combinatorial reasoning.

---

### Key Concepts (Bullet Points)

- **Sequence definition**: a function \(a: \mathbb{N} \to \mathbb{R}\) (or \(\mathbb{Z}\)); term \(a_n\).  
- **Arithmetic Progression (AP)**: \(a_n = a_1 + (n-1)d\).  
- **Geometric Progression (GP)**: \(a_n = a_1 r^{\,n-1}\).  
- **Fibonacci sequence**: \(F_n = F_{n-1} + F_{n-2}\) with \(F_0 = 0, F_1 = 1\).  
- **Recurrence relation**: expresses \(a_n\) in terms of previous terms; solving gives a closed‑form formula.  
- **Summation notation**: \(\displaystyle\sum_{i=m}^{n} a_i\); \(m\) = lower bound, \(n\) = upper bound.  
- **Arithmetic series sum**: \(\displaystyle\sum_{i=1}^{n} \bigl(a + (i-1)d\bigr) = \frac{n}{2}\bigl[2a + (n-1)d\bigr]\).  
- **Geometric series (finite)**: \(\displaystyle\sum_{i=0}^{n-1} ar^{i} = a\frac{1-r^{\,n}}{1-r}\) \((r\neq1)\).  
- **Geometric series (infinite)**: if \(|r|<1\), \(\displaystyle\sum_{i=0}^{\infty} ar^{i} = \frac{a}{1-r}\).  
- **Special sums**:  
  - \(\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}\)  
  - \(\displaystyle\sum_{i=1}^{n} i^{2} = \frac{n(n+1)(2n+1)}{6}\)  
  - \(\displaystyle\sum_{i=1}^{n} i^{3} = \left[\frac{n(n+1)}{2}\right]^{2}\)  
- **Linearity & constant‑multiple**: \(\displaystyle\sum (a_i + b_i) = \sum a_i + \sum b_i\); \(\displaystyle\sum c a_i = c\sum a_i\).  
- **Change of index**: \(\displaystyle\sum_{i=m}^{n} a_i = \sum_{j=m-k}^{\,n-k} a_{j+k}\).  
- **Telescoping series**: \(\displaystyle\sum_{i=1}^{n} (b_i - b_{i-1}) = b_n - b_0\).  
- **Bounding techniques**: integral test, comparison test, monotone bounds; e.g., \(\displaystyle\sum_{i=1}^{n} f(i) \le \int_{1}^{n} f(x)\,dx + f(1)\).  
- **Floor/ceiling in sums**: \(\displaystyle\sum_{i=1}^{\lfloor n/2\rfloor} f(i)\) can be split or approximated using \(\lfloor\cdot\rfloor\) / \(\lceil\cdot\rceil\).  
- **Generating functions**: \(A(x)=\sum_{n\ge0} a_n x^n\); coefficients yield closed‑form solutions for many recurrences.  
- **Applications**: loop‑count analysis → \(O(n)\), \(O(n^2)\); counting combinations; solving recurrence relations in algorithms.

---

### Conclusion  
Mastering sequences and summations enables you to model discrete processes, evaluate series efficiently, and determine the time/space complexity of algorithms—core skills tested in the Delhi University examination and in later computer‑science topics.