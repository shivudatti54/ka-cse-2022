# Concurrency Control Based on Timestamp Ordering

## Introduction

Concurrency control in database management systems ensures that multiple transactions can execute simultaneously without violating data consistency. Among the various techniques developed for this purpose, Timestamp-Based Ordering (TSO) stands out as a prominent method that uses time values to determine the order of transaction execution. Unlike lock-based approaches that prevent conflicts by restricting access to data items, timestamp ordering allows transactions to proceed based on their unique timestamp identifiers, making it an optimistic concurrency control technique.

The timestamp ordering approach was introduced by Reuter and Bernstein in the early 1980s as an alternative to traditional locking mechanisms. This method is particularly effective in environments where conflicts between transactions are relatively rare, as it avoids the overhead of lock management and deadlock detection. In the the syllabus for BCS403 Database Management System, this topic forms a crucial part of Module 5, which deals with transaction processing and concurrency control. Understanding timestamp ordering is essential for students to grasp how modern database systems manage concurrent access while maintaining the ACID properties of transactions.

## Key Concepts

### Timestamps

A timestamp is a unique identifier assigned to each transaction when it begins execution. In its simplest form, a timestamp can be a monotonically increasing counter or the current system time. Each transaction T_i receives two important timestamps:

1. **Start Timestamp (TS(T_i))**: The time at which the transaction begins its execution
2. **Finish Timestamp**: The time at which the transaction completes

The start timestamp determines the priority of the transaction—older timestamps (smaller values) have higher priority and are considered to have arrived earlier in the system. This temporal ordering forms the foundation of the timestamp-based concurrency control protocol.

### Timestamp Ordering Protocol

The Timestamp Ordering (TO) protocol ensures that any conflicting operations are executed in timestamp order. For every data item Q, the system maintains two timestamp values:

1. **Read_Timestamp(Q)**: The largest timestamp of any transaction that has successfully read Q
2. **Write_Timestamp(Q)**: The largest timestamp of any transaction that has successfully written Q

When a transaction T_i attempts to read or write a data item Q, the protocol checks the following conditions:

**Read Operation:**

- If TS(T_i) < Write_Timestamp(Q), the transaction is reading a value that was overwritten by a younger transaction. This violates the timestamp order, so the read operation is rejected, and T_i is rolled back.
- If TS(T_i) ≥ Write_Timestamp(Q), the read operation proceeds, and Read_Timestamp(Q) is updated to max(Read_Timestamp(Q), TS(T_i)).

**Write Operation:**

- If TS(T_i) < Read_Timestamp(Q), the transaction is attempting to write a value that has been read by a younger transaction. This violates the order, so the write is rejected and T_i is rolled back.
- If TS(Timestamp) < Write_Timestamp(Q), the transaction is attempting to overwrite a value written by a younger transaction. Again, T_i is rolled back.
- Otherwise, the write operation proceeds, and Write_Timestamp(Q) is updated to TS(T_i).

### Thomas' Write Rule

An important optimization to the basic timestamp ordering protocol is Thomas' Write Rule, which allows certain write operations that would normally be rejected to be ignored instead. When a transaction T_i attempts to write a data item Q:

- If TS(T_i) < Read_Timestamp(Q), the write is rejected (as before)
- If TS(T_i) < Write_Timestamp(Q), instead of rejecting the write, the system can simply ignore it (treat it as a no-op) because a newer transaction has already written to Q
- Otherwise, the write proceeds normally

This optimization increases the number of writes that can be successfully completed, improving system throughput while still maintaining correctness.

### Strict Timestamp Ordering

The basic timestamp ordering protocol does not guarantee that transactions are serialized in a strict order (where one transaction commits before another reads or writes a value written by the first). To achieve strict serialization, the Strict Timestamp Ordering protocol adds the following constraint:

- A transaction T_i can only read a data item Q if TS(T_i) > Write_Timestamp(Q)—note the strict greater-than operator
- Similarly, a transaction can only write Q if TS(T_i) > Read_Timestamp(Q) and TS(T_i) > Write_Timestamp(Q)

This ensures that no transaction reads or writes data that has been written by an uncommitted transaction, preventing cascading rollbacks.

## Examples

### Example 1: Basic Timestamp Ordering with Read and Write Operations

Consider two transactions T1 and T2 with timestamps TS(T1) = 10 and TS(T2) = 20. Let the initial value of data item X be 100. Analyze the following execution:

```
T1: Read(X)
T2: Write(X, 200)
T1: Write(X, 150)
```

**Step-by-step execution using TO protocol:**

1. T1 attempts Read(X):

- Write_Timestamp(X) = 0 (initial)
- TS(T1) = 10 ≥ Write_Timestamp(X) = 0, so read succeeds
- Read_Timestamp(X) = max(0, 10) = 10
- Value read: 100

2. T2 attempts Write(X, 200):

- Read_Timestamp(X) = 10
- TS(T2) = 20 ≥ Read_Timestamp(X) = 10, so condition passes
- Write_Timestamp(X) = 0
- TS(T2) = 20 ≥ Write_Timestamp(X) = 0, so write succeeds
- Write_Timestamp(X) = 20

3. T1 attempts Write(X, 150):

- Read_Timestamp(X) = 10
- TS(T1) = 10 is not greater than Read_Timestamp(X) = 10, so condition fails
- T1 is rolled back

Result: T1 is aborted because it attempted to write after reading a value that was subsequently overwritten by T2 (which has a younger timestamp).

### Example 2: Demonstrating Thomas' Write Rule

Consider three transactions with timestamps: T1 (TS=10), T2 (TS=20), T3 (TS=30). Let data item Y have Write_Timestamp(Y) = 15 initially.

Execute: T3 attempts Write(Y, 500)

**Basic TO Protocol:**

- Read_Timestamp(Y) = 15 (assuming some transaction read Y)
- TS(T3) = 30 ≥ Read_Timestamp(Y) = 15 ✓
- TS(T3) = 30 ≥ Write_Timestamp(Y) = 15 ✓
- Write succeeds, Write_Timestamp(Y) = 30

**Now if T1 (TS=10) attempts to Write(Y, 100) after T3:**

- Read_Timestamp(Y) = 15
- TS(T1) = 10 < Read_Timestamp(Y) = 15 → REJECT and rollback

**Using Thomas' Write Rule:**

If instead T1 had Write_Timestamp(Y) = 25 and Read_Timestamp(Y) = 20:

- T1 attempts Write(Y, 100):
- Read_Timestamp(Y) = 20
- TS(T1) = 10 < 20 → REJECT (cannot write)

Alternative scenario: If Read_Timestamp(Y) = 5 and Write_Timestamp(Y) = 25:

- TS(T1) = 10 < Read_Timestamp(Y) = 5? No, 10 ≥ 5 ✓
- TS(T1) = 10 < Write_Timestamp(Y) = 25? YES
- With Thomas' Write Rule: Instead of rejecting, the write is ignored (no-op)
- T1 continues execution rather than being rolled back

This demonstrates how Thomas' Write Rule can prevent unnecessary rollbacks.

### Example 3: Schedule Validation in Timestamp Ordering

Consider the schedule:

```
R1(X), R2(X), W1(X), R3(Y), W2(Y), W3(Y)
```

Where T1 has TS=100, T2 has TS=200, T3 has TS=300. Initial Write_Timestamp(X)=0, Write_Timestamp(Y)=0.

**Analysis:**

1. R1(X): TS(T1)=100 ≥ Write_Timestamp(X)=0 ✓, Read_Timestamp(X)=100
2. R2(X): TS(T2)=200 ≥ Write_Timestamp(X)=0 ✓, Read_Timestamp(X)=max(100,200)=200
3. W1(X): TS(T1)=100 < Read_Timestamp(X)=200 ✗ → T1 is rolled back

Since T1 is rolled back, any subsequent operations of T1 are not executed. The schedule is not conflict-serializable under timestamp ordering.

## Exam Tips

1. **Remember the basic rule**: In timestamp ordering, an operation is rejected if it would violate the timestamp order—specifically, if a transaction with an older timestamp tries to read/write after a transaction with a younger timestamp has already performed the conflicting operation.

2. **Know the two timestamps maintained**: Always remember that for each data item Q, the system maintains Read_Timestamp(Q) and Write_Timestamp(Q), representing the largest timestamps of transactions that have successfully read or written the item.

3. **Thomas' Write Rule optimization**: Understand that this rule allows certain writes to be treated as no-ops instead of causing rollbacks, improving throughput. Remember the condition: if TS(T_i) < Write_Timestamp(Q) but other conditions are satisfied, ignore the write.

4. **Distinguish between basic TO and Strict TO**: In strict timestamp ordering, the conditions use strict inequalities (>) to prevent cascading rollbacks, ensuring that transactions only read/write data from committed transactions.

5. **Deadlock freedom**: Remember that timestamp ordering protocols do not create deadlocks because each transaction has a predetermined order based on its timestamp—there can be no circular wait conditions.

6. **Starvation possibility**: Although deadlocks are avoided, starvation can occur if a transaction is repeatedly rolled back due to conflicts with newer transactions.

7. **Compare with locking**: In exams, be prepared to contrast timestamp ordering with lock-based protocols—timestamp ordering is optimistic (allows execution, checks for conflicts) while locking is pessimistic (prevents conflicts by restricting access).

8. **Cascading rollbacks**: The basic timestamp ordering protocol can lead to cascading rollbacks, whereas strict timestamp ordering prevents this by using stricter conditions.
