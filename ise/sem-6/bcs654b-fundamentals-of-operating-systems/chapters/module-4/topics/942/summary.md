# 9.4.2 Deadlock Prevention and Detection

==============================================

### Key Concepts

- **Definition:** A situation in a system where two or more processes are unable to proceed because each is waiting for the other to release a resource.
- **Types of Deadlocks:** Chicken and Lizard deadlocks

### Theorems and Formulas

- **Hunger and Thirst Theorem:** If two processes P1 and P2 are in a deadlock, then for every resource R1, there is a resource R2 such that P1 needs R1 but not R2, and P2 needs R2 but not R1.
- **Banker's Theorem:** If two processes P1 and P2 are in a deadlock, then for every resource R1, the number of units of R1 needed by P1 is less than or equal to the number of units available, and the number of units available is less than or equal to the number of units needed by P2.

### Methods for Handling Deadlocks

- **Prevention:**
  - **Resource Ordering:** Ordering resources to reduce the likelihood of deadlock
  - **Resource Priority:** Prioritizing resources to prevent deadlock
  - **Mutual Exclusion:** Implementing mutual exclusion to prevent two processes from accessing the same resource simultaneously
- \*\*Detection and Recovery:
  - **Deadlock Detection:** Using algorithms to detect deadlocks
  - **Deadlock Recovery:** Implementing algorithms to recover from deadlocks, such as rolling back processes or aborting processes
