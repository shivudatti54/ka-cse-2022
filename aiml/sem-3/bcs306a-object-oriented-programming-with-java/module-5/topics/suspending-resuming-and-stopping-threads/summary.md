# Suspending, Resuming, and Stopping Threads - Summary

## Key Definitions and Concepts

- **Thread**: A lightweight subprocess that allows a program to perform multiple operations concurrently.
- **Suspend/Resume**: Deprecated methods that paused and resumed thread execution (deprecated due to deadlock risks).
- **stop()**: Deprecated method that forcibly terminated threads, leaving objects in inconsistent states.
- **wait()**: Method that causes a thread to release its monitor lock and enter Waiting state.
- **notify()**: Method that wakes up a single thread waiting on an object's monitor.
- **interrupt()**: Recommended method to signal a thread to stop by setting its interrupt flag.

## Important Formulas and Theorems

- **Thread States**: New → Runnable → Blocked/Waiting/Timed Waiting → Terminated
- **Deprecated Methods**: suspend(), resume(), stop() - unsafe, deprecated since JDK 1.2
- **Modern Control Methods**: wait(), notify(), notifyAll() - require synchronized context
- **Interrupt Handling**: Thread.interrupted() (static, clears flag) vs isInterrupted() (instance, preserves flag)

## Key Points

1. The suspend(), resume(), and stop() methods were deprecated due to deadlock problems, resource leakage, and inconsistent object states.

2. The wait() method releases the monitor lock, while suspend() does not - this is the primary reason for the deadlock issue.

3. Modern thread control uses wait()/notify() for synchronization and interrupt() for termination.

4. The volatile keyword ensures visibility of flag variables across threads when using flag-based termination.

5. interrupt() does not forcibly stop a thread; it only sets an interrupt flag that the thread must check.

6. When interrupt() is called on a sleeping/waiting thread, it throws InterruptedException and clears the interrupt flag.

7. Thread.interrupted() is a static method that returns and clears the interrupt status, while isInterrupted() returns status without clearing.

8. Producer-consumer problems are best solved using wait() and notify() to coordinate between threads.

## Common Mistakes to Avoid

- Using deprecated suspend(), resume(), or stop() methods in production code
- Calling wait()/notify() without proper synchronization (synchronized block/method)
- Forgetting to use volatile keyword for shared flag variables
- Not handling InterruptedException properly in thread code
- Using stop() which can leave critical sections in inconsistent states

## Revision Tips

1. Practice writing producer-consumer programs using wait() and notify()
2. Remember the three main reasons for deprecation: deadlock, resource leakage, inconsistent state
3. Always use interrupt() with proper interrupt handling instead of stop()
4. Review the difference between isInterrupted() and Thread.interrupted()
5. Write sample programs demonstrating thread control with flags and interrupt()
