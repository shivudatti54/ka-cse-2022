# Learning Purpose: Loop-Carried Dependency

**1. Why this topic matters**
Loop-carried dependencies occur when an iteration of a loop depends on the result of a previous iteration, fundamentally limiting or preventing safe parallelization. Failing to recognize these dependencies before adding OpenMP parallel directives leads to incorrect results that may appear correct on some runs but fail unpredictably on others. Identifying loop-carried dependencies is a critical skill for determining which loops can be safely parallelized.

**2. What you will learn**
You will learn to define and identify the three types of loop-carried dependencies: flow (true), anti, and output dependencies. You will practice analyzing code to determine whether a loop can be parallelized with OpenMP, apply the reduction clause to handle specific dependency patterns (associative and commutative operations), and understand why synchronization constructs inside parallel loops often lead to poor performance.

**3. How it connects to other topics**
This topic directly applies the OpenMP parallel for directive and reduction clause from earlier topics in this module. It connects to scheduling (how iterations are assigned to threads affects dependency handling) and to the broader theme of identifying parallelism in sequential code that runs throughout the course, including CUDA kernel design in Module 5.

**4. Real-world relevance**
Loop-carried dependency analysis is performed routinely by compiler developers building auto-parallelizing compilers and by application developers parallelizing scientific simulation codes, signal processing algorithms, and numerical solvers. Correctly identifying and resolving these dependencies is often the key challenge when modernizing legacy codes for parallel hardware.
