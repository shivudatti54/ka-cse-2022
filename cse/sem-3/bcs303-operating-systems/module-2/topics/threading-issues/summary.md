# Threading Issues - Summary

## Key Definitions

- **Thread Cancellation**: The termination of a thread before natural completion, either asynchronously (immediate) or deferred (at cancellation points).
- **Thread-Local Storage (TLS)**: A mechanism allowing each thread to maintain its own copy of global or static variables, providing data isolation within shared address spaces.
- **Cancellation Point**: A specific function call where a thread checks for pending cancellation requests, such as `pthread_testcancel()`, `pthread_join()`, or I/O operations.
- **Cleanup Handler**: A function registered via `pthread_cleanup_push()` that executes when a thread terminates, ensuring proper resource release.
- **Thread Pool**: A design pattern maintaining a pool of pre-created worker threads to reuse for multiple tasks, avoiding repeated thread creation overhead.

## Important Formulas

- **Thread Creation Overhead**: Total cost ≈ TCB allocation + Stack allocation + Scheduler registration + Context initialization
- **TLS Access Time**: O(1) lookup using thread-specific data structures maintained by the runtime system
- **Cancellation Check Frequency**: Balance between responsiveness and performance overhead

## Key Points

1. Deferred cancellation is safer than asynchronous cancellation because it allows cleanup handlers to execute and release resources properly.

2. Thread-Local Storage provides efficient per-thread data isolation without requiring explicit synchronization or parameter passing between functions.

3. Signals in multithreaded processes are delivered to a single thread; use `pthread_sigmask()` to control signal delivery to specific threads.

4. After `fork()`, only the calling thread survives in the child; held locks remain locked, potentially causing deadlock in the child process.

5. Thread pools significantly reduce overhead for applications with many short-lived tasks by reusing existing threads rather than creating new ones.

6. Cancellation points must be explicitly inserted in long-running operations or the system calls that support cancellation to enable deferred cancellation.

7. The `pthread_atfork()` mechanism allows registration of handlers during fork, but proper handling of all locks remains challenging in complex programs.

8. Stack size for each thread defaults to a system value (often 1-8 MB); excessive thread creation can exhaust virtual address space.

## Common Mistakes

1. **Ignoring cleanup handlers**: Failing to use `pthread_cleanup_push/pop()` leads to resource leaks when threads are cancelled.

2. **Holding locks across fork**: Parent process locks may remain held in child processes after fork, causing permanent deadlock.

3. **Incorrect TLS key deletion**: Deleting TLS keys without ensuring all threads have released their associations can cause undefined behavior.

4. **Assuming all functions are cancellation points**: Many standard library functions are not cancellation points; explicit `pthread_testcancel()` calls may be necessary.

5. **Creating threads for trivial tasks**: Spawning threads for very short operations introduces more overhead than sequential execution would require.