# Peterson's Solution

### Overview

Peterson's solution is a synchronization algorithm used to solve the readers-writers problem in operating systems.

### Key Points

- **Peterson's Algorithm:**
  - Two processes P1 and P2 share a common variable "shared" that needs to be accessed concurrently.
  - The processes use two flags: `turn` and `writable`.
- **Algorithm Steps:**
  1.  Initialize `turn` and `writable` to 0.
  2.  When P1 wants to read:
      - Set `turn` to 1.
      - If `turn` == 1, then P1 is the exclusive reader.
      - If `writable` == 1, then P1 can proceed to read.
  3.  When P1 wants to write:
      - Set `turn` to 1.
      - If `turn` == 1, then P1 is the exclusive writer.
      - If `writable` == 1, then P1 can proceed to write.
  4.  When P2 wants to read or write:
      - Set `turn` to 0.
      - If `turn` == 0, then either P1 or P2 is trying to read or write.
      - If `writable` == 1, then the process can proceed.

### Important Formulas and Definitions

- **Turn Flag:** Used to ensure exclusive access to the shared variable.
- **Writable Flag:** Used to determine if the shared variable can be written to.
- **Exclusive Reader/Writer:** A process that is the only one accessing the shared variable.

### Theorem

- If the Peterson's algorithm is used to solve the readers-writers problem, then:
  - If there are `n` readers, then the shared variable is accessed by at most `n` processes at any given time.
  - If there is one writer, then the shared variable is accessed by at most two processes (the writer and the reader) at any given time.

### Important Theorems

- Peterson's algorithm is a solution to the readers-writers problem.
- Peterson's algorithm ensures that the shared variable is accessed by at most `n` processes at any given time for `n` readers.
