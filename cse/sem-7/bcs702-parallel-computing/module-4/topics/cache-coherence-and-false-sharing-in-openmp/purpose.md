# Learning Objectives

After studying this topic, you should be able to:

1. Explain the hierarchical structure of computer memory and how cache lines function as the unit of data transfer between memory levels.

2. Describe the cache coherence problem in shared memory multiprocessors and explain why it is necessary for correct program execution.

3. Explain the four states of the MESI cache coherence protocol (Modified, Exclusive, Shared, Invalid) and describe how invalidations maintain coherence.

4. Define false sharing and distinguish it from true data sharing, explaining why false sharing causes performance degradation despite being functionally correct.

5. Identify scenarios in OpenMP programs where false sharing is likely to occur, particularly with array elements accessed by different threads.

6. Apply practical techniques to avoid false sharing, including padding, alignment, and thread-local accumulation with reduction.

7. Analyze OpenMP code to determine whether it is susceptible to false sharing and propose appropriate optimizations.

8. Evaluate the performance trade-offs between different false sharing mitigation strategies in the context of specific parallel algorithms.