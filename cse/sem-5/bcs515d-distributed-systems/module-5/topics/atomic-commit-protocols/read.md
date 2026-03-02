# Atomic Commit Protocols

## Introduction

Atomic Commit Protocols are fundamental mechanisms in distributed database systems that ensure the atomicity of distributed transactions. In a distributed environment where a transaction spans multiple database nodes, it becomes crucial to guarantee that either all the participating nodes commit the transaction or none of them do. Without proper atomic commit protocols, system failures or network partitions could lead to inconsistent states where some nodes commit and others abort, violating the fundamental ACID properties of transactions.

The importance of atomic commit protocols cannot be overstated in modern distributed systems. When a transaction involves multiple databases across different servers, we need a coordination mechanism that ensures all participants reach a unified decision - either commit or abort. This coordination becomes particularly challenging when dealing with network failures, node crashes, and asynchronous communication. The Two-Phase Commit (2PC) protocol and Three-Phase Commit (3PC) protocol are the most widely studied and implemented atomic commit protocols in distributed database systems.

In the context of 's Computer Science curriculum, understanding atomic commit protocols is essential for comprehending how modern distributed databases maintain consistency and reliability. These protocols form the backbone of transaction management in systems like distributed SQL databases, NoSQL databases, and distributed file systems. The study of these protocols also prepares students for advanced topics in distributed systems and helps them understand the trade-offs between consistency, availability, and partition tolerance.

## Key Concepts

### Two-Phase Commit (2PC) Protocol

The Two-Phase Commit protocol is the most commonly used atomic commit protocol in distributed systems. It involves two distinct phases: the voting phase and the decision phase.

**Phase 1: Voting Phase**

- The coordinator (transaction manager) sends a "prepare" message to all participating nodes (cohorts)
- Each participant executes the transaction up to the point of commitment
- Each participant locks the necessary resources and votes either "YES" (ready to commit) or "NO" (cannot commit)
- If any participant votes "NO", the coordinator initiates the abort procedure

**Phase 2: Decision Phase**

- After collecting all votes, the coordinator makes a global decision
- If all participants vote "YES", the coordinator sends "commit" messages to all participants
- If any participant votes "NO" or timeout occurs, the coordinator sends "abort" messages
- Each participant either commits or aborts based on the coordinator's decision and releases locks

**Advantages of 2PC:**

- Simple to implement and understand
- Guarantees atomicity in synchronous systems
- Low message overhead compared to more complex protocols

**Disadvantages of 2PC:**

- Blocking protocol - participants remain blocked waiting for coordinator's decision
- Coordinator failure can lead to indefinite blocking
- Does not handle network partitions effectively

### Three-Phase Commit (3PC) Protocol

The Three-Phase Commit protocol extends 2PC to eliminate the blocking problem by introducing an additional phase. It adds a "pre-commit" phase between voting and decision phases.

**Phase 1: Can Commit**

- Coordinator asks participants if they can commit
- Participants respond with "YES" or "NO"

**Phase 2: Pre-Commit**

- If all participants respond "YES", coordinator sends "pre-commit" message
- Participants acknowledge receipt and prepare to commit
- If coordinator receives "NO" or timeouts, it sends "abort"

**Phase 3: Do Commit**

- Coordinator sends "commit" message to all participants
- Participants complete the commit and release locks

**Advantages of 3PC:**

- Non-blocking under certain failure scenarios
- Better handling of coordinator failures
- More resilient to network delays

**Disadvantages of 3PC:**

- More complex to implement
- Higher message overhead
- Still not fully immune to all failure scenarios

### Coordinator and Participant Roles

In atomic commit protocols, distinct roles are assigned:

**Coordinator Responsibilities:**

- Initiates the transaction commit process
- Collects votes from all participants
- Makes global commit/abort decisions
- Communicates final decision to all participants
- Maintains transaction log for recovery

**Participant Responsibilities:**

- Execute transaction operations locally
- Vote on commit/abort during voting phase
- Execute commit or abort based on coordinator's decision
- Maintain local transaction log for recovery
- Release locks after transaction completion

### Failure Handling and Recovery

Atomic commit protocols must handle various failure scenarios:

**Participant Failure:**

- Before voting: Transaction aborted, no locks held
- After voting "YES" but before receiving decision: Must wait for coordinator, holding locks
- After commit/abort: Can recover using local log

**Coordinator Failure:**

- Before sending prepare: Can abort transaction
- After sending prepare: Participants wait indefinitely (blocking problem)
- After collecting votes: Need recovery mechanism to restore decision

**Network Partition:**

- Can lead to split-brain scenarios
- Protocols may enter inconsistent states
- Recovery mechanisms required after partition heals

## Examples

### Example 1: Two-Phase Commit Scenario - Successful Commit

Consider a distributed transaction T1 that transfers ₹5000 from Account A (stored in Database 1 in Bangalore) to Account B (stored in Database 2 in Mumbai). The transaction involves two operations: debit from A and credit to B.

**Step 1: Coordinator initiates 2PC**

- Transaction T1 starts at application server
- Coordinator sends "prepare" to both databases

**Step 2: Participants vote**

- Database 1 (Bangalore): Executes debit operation, locks Account A, checks constraints (sufficient balance), votes "YES"
- Database 2 (Mumbai): Executes credit operation, locks Account B, votes "YES"

**Step 3: Coordinator collects votes and decides**

- All votes are "YES"
- Coordinator sends "commit" to both databases

**Step 4: Participants commit**

- Database 1: Applies debit, releases lock on Account A, logs "COMMIT"
- Database 2: Applies credit, releases lock on Account B, logs "COMMIT"
- Transaction T1 completes successfully

### Example 2: Two-Phase Commit Scenario - Abort Case

Using the same transaction scenario, assume Account A has only ₹3000 (insufficient for ₹5000 transfer).

**Step 1: Coordinator initiates 2PC**

- Coordinator sends "prepare" to both databases

**Step 2: Participants vote**

- Database 1: Executes debit operation, detects constraint violation (insufficient balance), cannot proceed, votes "NO"
- Database 2: Could vote "YES" but waits for coordinator

**Step 3: Coordinator makes decision**

- Since Database 1 voted "NO", coordinator sends "abort" to both

**Step 4: Participants abort**

- Database 1: Discards changes, releases locks
- Database 2: Discards changes, releases locks
- Transaction T1 is rolled back completely

### Example 3: Three-Phase Commit Scenario

Consider the same transfer transaction with 3PC protocol:

**Phase 1: Can Commit**

- Coordinator asks: "Can you commit T1?"
- Database 1: Checks resources, votes "YES"
- Database 2: Checks resources, votes "YES"

**Phase 2: Pre-Commit**

- Coordinator sends "pre-commit" to both
- Both databases acknowledge "ACK"
- Both prepare for final commit, holding locks

**Phase 3: Do Commit**

- Coordinator sends "commit" to both
- Both databases apply changes and release locks
- Transaction completes

If coordinator fails in Phase 2, participants can communicate with each other to determine the correct action - since both received "pre-commit", both must eventually commit.

## Exam Tips

1. **Remember the key difference between 2PC and 3PC**: 2PC is blocking while 3PC is non-blocking under certain failure conditions. This is the most frequently asked distinction in exams.

2. **Draw the state diagrams**: For exam questions involving commit protocols, drawing the state transition diagrams for coordinator and participants can help organize your answer clearly.

3. **Know the exact message flow**: Be able to write the sequence of messages exchanged between coordinator and participants in both 2PC and 3PC protocols.

4. **Understand blocking vs non-blocking**: 2PC blocks when coordinator fails after participant votes "YES". 3PC eliminates this by adding the pre-commit phase.

5. **Remember the roles of participants**: They can vote "YES" or "NO", execute commit/abort, and must maintain transaction logs for recovery.

6. **Failure scenarios are important**: Be prepared to explain what happens when coordinator fails, when participants fail, and how recovery works in each case.

7. **ACID properties connection**: Understand how atomic commit protocols specifically ensure the atomicity property of transactions in distributed environments.

8. **Timeout handling**: Know how participants handle situations when they don't receive messages from the coordinator within expected timeframes.
