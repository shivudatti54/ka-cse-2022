# Learning Objectives

After studying this topic, you should be able to:

1. Explain the fork-join parallel execution model used by OpenMP and describe how threads are created and synchronized.

2. Identify and apply the `#pragma omp parallel` directive to create parallel regions and execute code concurrently across multiple threads.

3. Use work-sharing constructs such as `#pragma omp for` and `#pragma omp parallel for` to distribute loop iterations among threads.

4. Analyze the behavior of `omp_get_thread_num()` and `omp_get_num_threads()` functions for thread identification and team size determination.

5. Implement basic thread synchronization using implicit and explicit barriers in parallel regions.

6. Distinguish between different OpenMP clauses (such as `num_threads`, `if`, `private`, `shared`) and apply them appropriately in parallel programs.

7. Design and implement simple parallel algorithms using OpenMP directives to solve computational problems efficiently.

8. Evaluate the correctness of OpenMP programs by understanding how sequential code can be transformed into parallel code using compiler directives.
