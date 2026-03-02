# Learning Objectives

After studying this topic, you should be able to:

1. Understand the concept of OpenMP tasks and explain how they differ from parallel regions and parallel for directives in handling irregular workloads.

2. Explain the task execution model in OpenMP, including how the runtime schedules tasks across threads and the role of work-stealing.

3. Apply the `#pragma omp task` directive to create explicit parallel work units within parallel regions for non-loop-based parallelism.

4. Implement task synchronization using `taskwait` directive to ensure completion of child tasks before proceeding.

5. Analyze and resolve task dependencies using the `depend` clause (in, out, inout) to establish ordering between related tasks.

6. Design parallel solutions using tasking for irregular problems such as tree traversals, graph algorithms, and recursive divide-and-conquer strategies.

7. Compare task-based parallelism with loop-based parallelism and select the appropriate approach based on problem structure and computational patterns.
