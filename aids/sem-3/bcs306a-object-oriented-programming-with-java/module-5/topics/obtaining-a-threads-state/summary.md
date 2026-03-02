# Obtaining a Thread's State - Summary

## Key Definitions and Concepts

- **Thread State**: The current condition or phase of a thread's execution lifecycle in Java
- **Thread.State**: An enumeration containing six constants representing all possible thread states
- **getState()**: A method in the Thread class that returns the current state as a Thread.State enum value

## Important Methods and Constants

| Method/Constant              | Description                             |
| ---------------------------- | --------------------------------------- |
| `Thread.getState()`          | Returns current thread state            |
| `Thread.State.NEW`           | Thread created but not started          |
| `Thread.State.RUNNABLE`      | Thread executing in JVM or ready to run |
| `Thread.State.BLOCKED`       | Waiting for monitor lock                |
| `Thread.State.WAITING`       | Waiting indefinitely for another thread |
| `Thread.State.TIMED_WAITING` | Waiting for specified time period       |
| `Thread.State.TERMINATED`    | Thread has completed execution          |

## Key Points

- A Java thread can exist in exactly one of six states at any given time
- NEW state occurs before `start()` is called; TERMINATED occurs after `run()` completes
- RUNNABLE means the thread is eligible to run, not necessarily currently executing
- BLOCKED specifically refers to waiting for a synchronized lock
- WAITING results from `wait()`, `join()`, or `LockSupport.park()` without timeout
- TIMED_WAITING results from `sleep()`, `wait(timeout)`, `join(timeout)`, or similar methods
- The `getState()` method is useful for debugging and monitoring thread behavior

## Common Mistakes to Avoid

- Confusing RUNNABLE with actively executing (a thread in RUNNABLE state may not be running)
- Attempting to restart a terminated thread (throws IllegalThreadStateException)
- Mixing up BLOCKED (waiting for lock) with WAITING (waiting for signal)
- Forgetting that sleep() causes TIMED_WAITING, not BLOCKED state

## Revision Tips

1. Draw the thread state diagram showing all six states and transition conditions
2. Practice writing code to observe different thread states using getState()
3. Remember: synchronized blocks cause BLOCKED, wait() causes WAITING, sleep() causes TIMED_WAITING
4. Use switch statements with Thread.State enum for state-based logic
5. Review how thread states relate to thread synchronization and deadlock scenarios
