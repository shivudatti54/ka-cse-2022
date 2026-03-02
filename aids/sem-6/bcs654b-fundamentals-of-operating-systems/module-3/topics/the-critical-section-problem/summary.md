# The Critical Section Problem

## Overview

The critical section problem addresses race conditions when multiple processes access shared resources concurrently. Solutions must satisfy mutual exclusion, progress, and bounded waiting using software (Peterson's, Bakery) or hardware (Test-and-Set, Compare-and-Swap) approaches.

## Key Points

- **Race Condition**: Shared variable counter with concurrent access leads to inconsistent data (could be 4, 5, or 6 instead of expected value)
- **Critical Section**: Code segment accessing shared resource, structured as entry section → critical section → exit section → remainder section
- **Mutual Exclusion**: Only one process in critical section at a time
- **Progress**: If no process in CS and some wish to enter, only those not in remainder section participate in decision
- **Bounded Waiting**: Bound exists on times other processes enter CS after a request and before grant
- **Peterson's Solution**: Uses turn and flag[2] variables, works for 2 processes only
- **Bakery Algorithm**: Ticket number system for n processes, lowest number enters CS, tie broken by process ID
- **Test-and-Set**: Atomic hardware operation returning old value while setting new, fast but busy waiting
- **Compare-and-Swap**: Atomic operation comparing expected value, foundation of lock-free programming

## Important Concepts

- Software solutions (Peterson's, Bakery) are software-only but complex with high overhead
- Hardware solutions (Test-and-Set, CAS) fast and simple but cause busy waiting
- Process structure: do { entry; CRITICAL SECTION; exit; remainder } while(true)
- Test-and-Set usage: while (TestAndSet(&lock)); for entry, lock=false for exit

## Notes

- Practice Peterson's solution with turn and flag variables for 2 processes
- Understand Bakery algorithm ticket number system for n processes
- Know trade-offs: Peterson's (simple, 2 processes only), Bakery (n processes, complex), Test-and-Set (fast, busy waiting)
- Remember all three requirements: mutual exclusion, progress, bounded waiting
