# Synchronization Hardware - Summary

## Key Definitions and Concepts

- SYNCHRONIZATION HARDWARE: Special processor instructions that perform atomic operations without interruption, forming the foundation for OS synchronization constructs

- ATOMIC OPERATION: An operation that executes completely without any other process observing or interfering with its intermediate states

- TEST-AND-SET: Instruction that atomically reads a boolean value and sets it to true, returning the old value for lock acquisition testing

- COMPARE-AND-SWAP (CAS): Atomic instruction that conditionally updates a memory location only if its current value matches an expected value, returning the actual value for retry logic

- FETCH-AND-ADD: Atomic instruction that increments a memory location and returns its previous value, useful for counters and ticket locks

- LOAD-LINKED/STORE-CONDITIONAL: Paired instructions where SC succeeds only if no modification occurred since the corresponding LL, enabling flexible lock-free operations

- MEMORY BARRIER: Hardware instruction enforcing ordering of memory operations across processors in weakly ordered architectures

## Important Formulas and Theorems

- TestAndSet(lock): old = *lock; *lock = true; return old;

- CompareAndSwap(ptr, expected, new): actual = *ptr; if(actual == expected) *ptr = new; return actual;

- FetchAndAdd(ptr, inc): old = *ptr; *ptr = old + inc; return old;

## Key Points

- Hardware synchronization primitives provide the atomic foundation upon which all software synchronization constructs depend

- Test-and-Set enables simple spin lock implementation but may cause starvation and busy-waits CPU cycles

- Compare-and-Swap supports lock-free algorithms by enabling retry-on-failure patterns for complex updates

- Fetch-and-Add implements ticket locks providing fair, FIFO ordering compared to basic spin locks

- Load-Linked/Store-Conditional offers more flexibility than CAS for complex atomic sequences with intermediate computation

- Modern lock-free data structures (queues, stacks, hash tables) rely primarily on CAS for atomic updates

- Busy-waiting spin locks are suitable only when critical sections are extremely short; OS should suspend long-waiting processes

## Common Mistakes to Avoid

- Assuming operations are atomic without hardware support—this leads to race conditions in read-modify-write sequences

- Confusing Test-and-Set (returns old value) with Swap (exchanges values)—these have different synchronization semantics

- Forgetting that CAS requires retry loops—a single CAS attempt may fail due to concurrent modification

- Ignoring memory ordering implications—using atomic primitives without barriers on weakly ordered architectures causes subtle bugs

- Believing spin locks are always efficient—context switching overhead makes sleeping locks preferable for long waits

## Revision Tips

- Trace execution through multiple processes for each primitive to understand the interleaving behavior

- Implement simple synchronization problems using different primitives to compare their usage patterns

- Memorize the return values and side effects of each primitive—exams test specific behaviors

- Connect hardware primitives to OS-level constructs like mutexes and semaphores to see the complete picture

- Practice drawing timeline diagrams showing process interactions with shared locks