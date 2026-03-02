**P, NP, NP‑Complete, NP‑Hard – Quick Revision (MSc CS, DU, 2025)**  

*Introduction*  
The classes P, NP, NP‑Complete and NP‑Hard form the core of computational complexity theory. They classify decision problems by the amount of resources required and highlight the boundaries of efficient computation. This summary follows the Delhi University MSc (CS) Advanced Algorithms syllabus (2025).

*Key Concepts*  
- **P (Polynomial Time)**: Problems solvable by a deterministic Turing machine in \(O(n^k)\) time for some constant \(k\). *Examples*: sorting, shortest‑path, matrix multiplication.  
- **NP (Non‑deterministic Polynomial Time)**: Problems for which a given certificate can be verified in polynomial time. *Examples*: SAT, Hamiltonian Path, Vertex‑Cover.  
- **Polynomial‑Time Reduction**: Problem \(A\) reduces to \(B\) (\(A \le_p B\)) if a polynomial‑time computable function transforms every instance of \(A\) into an instance of \(B\) preserving the answer.  
- **NP‑Complete**: A language \(L\) is NP‑Complete if (i) \(L\in\) NP, and (ii) every problem in NP reduces to \(L\) in polynomial time. The first NP‑Complete problem is SAT (Cook‑Levin theorem).  
- **NP‑Hard**: Problems at least as hard as the hardest problems in NP; they need not belong to NP. If an NP‑Hard problem were solvable in polynomial time, then P = NP. *Examples*: Halting Problem, Travelling Salesman (optimization version), Integer Programming.  
- **Relationships**:  
  - \(P \subseteq NP\) (unknown whether strict).  
  - NP‑Complete ⊂ NP.  
  - NP‑Hard ⊇ NP‑Complete (includes problems outside NP).  
  - If any NP‑Complete problem is in P, then P = NP.  
- **Proving NP‑Completeness**: (1) Show the problem is in NP, (2) reduce a known NP‑Complete problem (e.g., 3‑SAT, Vertex‑Cover) to it in polynomial time.  
- **Classic NP‑Complete Problems**: SAT, Clique, Vertex‑Cover, Independent Set, Subset‑Sum, Partition, Hamiltonian Cycle.  
- **Classic NP‑Hard Problems**: Travelling Salesman (decision version), Knapsack (optimization), Graph Coloring, Set Cover.  
- **Practical Impact**: Most real‑world optimization problems are NP‑Hard; we often use approximation algorithms, heuristics, or exponential‑time exact methods for small instances.

*Conclusion*  
Understanding P, NP, NP‑Complete and NP‑Hard is essential for distinguishing tractable from intractable problems and for making informed algorithmic choices. Master the definitions, reductions, and classic examples to ace the exam.