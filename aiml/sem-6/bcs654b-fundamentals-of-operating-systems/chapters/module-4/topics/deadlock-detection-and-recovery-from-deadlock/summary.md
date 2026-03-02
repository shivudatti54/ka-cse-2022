# **Deadlock Detection and Recovery from Deadlock**

## **Definitions and Theorems**

- **Deadlock**: A situation where a thread is unable to proceed because it is waiting for a resource held by another thread that is also waiting for a resource held by the first thread.
- **Banker's Algorithm**: A deadlock detection and recovery algorithm that uses a set of rules to determine whether a deadlock is possible or has occurred.
- **Resource Allocation Graph (RAG)**: A graph used to represent the allocation of resources and the dependencies between them.

## **Deadlock Detection Methods**

- **Livelock Detection**: A technique that detects deadlocks by checking for livelocks (threads that are not making progress).
- **Wait-for Graph**: A graph used to represent the waiting relationships between threads and resources.
- **Banker's Algorithm**: Uses a set of rules to determine whether a deadlock is possible or has occurred.

## **Deadlock Recovery Methods**

- **Abort and Restart**: Repeatedly aborting and restarting threads until a solution is found.
- **Context Switching**: Swapping the context of two threads to resolve the deadlock.
- **Resource Preemption**: Preempting resources from one thread to another to resolve the deadlock.

## ** deadlock Detection Formula**

- _Deadlock condition_: If there exists a set of threads T and resources R such that for every thread t in T and every resource r in R, t is waiting for r and r is held by some other thread in T.

## **Key Points**

- Deadlock detection and recovery are crucial in operating systems to prevent system crashes.
- The Banker's Algorithm is a widely used deadlock detection and recovery algorithm.
- Resource preemption and context switching are two common deadlock recovery methods.
- Deadlock detection can be performed using livelock detection and wait-for graphs.
