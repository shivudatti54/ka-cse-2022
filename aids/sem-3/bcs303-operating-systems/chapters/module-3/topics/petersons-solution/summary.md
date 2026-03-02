# **Peterson’s Solution**

## **Overview**

Peterson's solution is a synchronization algorithm used to solve the readers-writers problem in a shared memory system.

## **Key Points**

- **Problem Statement:** Two processes, a reader and a writer, share a common resource (a buffer) that can be read but not written by multiple processes simultaneously.
- **Peterson's Solution:**
  - Two processes await and notify using a semaphore.
  - Reader decrements the semaphore value and waits for it to become available.
  - Writer increments the semaphore value and notifies the reader when it becomes available.
- **Synchronization Conditions:**
  - Reader-Writer Algorithm (RWA): Reader and Writer processes must satisfy two conditions:
    - (1) A writer must not be holding the buffer when any reader arrives.
    - (2) A reader must not be holding the buffer when a writer arrives.
- **Algorithm:**
  - Reader: `while (s == 0) { wait(s); read(buffer); s++; notify(w); }`
  - Writer: `while (s == 1) { wait(r); write(buffer); r++; notify(s); }`

## **Important Formulas and Definitions**

- **Semaphor:** A variable that controls the access to a shared resource.
- **Semaphore Value:** The number of available resources.

**Theorem:**
Peterson's Solution is a correct solution to the readers-writers problem because it ensures that the shared buffer is accessed in a way that satisfies the two conditions of the RWA.

## **Revision Notes**

- Understand the readers-writers problem and the need for synchronization.
- Learn Peterson's solution and its key components.
- Practice implementing the algorithm and analyzing its correctness.

This summary provides a concise overview of Peterson's solution to the readers-writers problem. It highlights the key points, important formulas and definitions, and theorem that prove the correctness of the algorithm. It is ideal for quick revision before exams.
