# Atomic Commit Protocols in Distributed Transactions

## Introduction to Distributed Transactions

A **distributed transaction** is a type of transaction that spans multiple networked resources, often across different physical locations or database systems. Unlike a local transaction that operates on a single database, a distributed transaction must coordinate its operations across several participants to ensure data consistency. The fundamental challenge is guaranteeing the **ACID properties** (Atomicity, Consistency, Isolation, Durability) in a distributed environment where failures are common.

**Atomicity** is particularly crucial. It means that a transaction must either commit (all its operations are permanently applied) or abort (all its operations are rolled back as if they never happened). There should be no middle ground where only some operations are applied. In a distributed system, achieving this is complex because the different participants (e.g., databases, services) might fail independently or become disconnected from the network.

An **Atomic Commit Protocol** is a distributed algorithm that ensures this all-or-nothing outcome for a transaction across multiple participants. It is the mechanism that allows the participants to collectively decide the final outcome of the transaction.

## The Need for Atomic Commit Protocols

Consider a simple example: a banking transaction that transfers $100 from an account in `Database A` to an account in `Database B`.

1.  Debit $100 from Account X in Database A.
2.  Credit $100 to Account Y in Database B.

If the system crashes after Step 1 but before Step 2, $100 vanishes. If it commits Step 1 and then a network partition isolates Database B, making Step 2 impossible, the transaction is left in an inconsistent state. An atomic commit protocol is designed to prevent these scenarios by ensuring both operations are applied or neither is applied, even in the face of failures.

## The Two-Phase Commit Protocol (2PC)

The Two-Phase Commit Protocol is the most fundamental and widely discussed atomic commit protocol. It involves a central coordinator and multiple participants (cohorts). The protocol proceeds in two distinct phases.

### Roles

*   **Coordinator:** The transaction manager. It is the component that initiates and drives the protocol. Often, this is the node where the transaction originated.
*   **Participant (Cohort):** A resource manager that executes part of the transaction and holds the relevant data (e.g., a local database server).

### Phase 1: Voting Phase

1.  The coordinator sends a `VOTE-REQUEST` message to all participants.
2.  Upon receiving this message, each participant performs the following:
    *   It writes all the transaction's log records (including undo and redo information) to its persistent storage. This is a **prepare** operation.
    *   It then votes. If the participant successfully prepared the transaction and is ready to commit, it sends a `VOTE-COMMIT` message to the coordinator. If anything went wrong (e.g., a constraint violation, local failure), it sends a `VOTE-ABORT` message.

This phase ensures that every participant is in a state where it is *capable* of committing if instructed to do so.

### Phase 2: Decision Phase

The coordinator collects the votes.

*   **Case 1: All participants voted `VOTE-COMMIT`.**
    *   The coordinator makes the irrevocable decision to commit.
    *   It writes a `commit` record to its own log, making the decision durable.
    *   It then sends a `GLOBAL-COMMIT` message to all participants.
    *   Each participant, upon receiving `GLOBAL-COMMIT`, commits the transaction locally and sends an `ACK` message back to the coordinator.
    *   The coordinator, after receiving all `ACKs`, can forget about the transaction.

*   **Case 2: Any participant voted `VOTE-ABORT` (or a participant times out).**
    *   The coordinator makes the irrevocable decision to abort.
    *   It writes an `abort` record to its log.
    *   It then sends a `GLOBAL-ABORT` message to all participants.
    *   Each participant, upon receiving `GLOBAL-ABORT`, aborts the transaction locally (using the undo log) and sends an `ACK`.
    *   The coordinator, after receiving all `ACKs`, can forget about the transaction.

### ASCII Diagram of 2PC (Successful Commit)

```
Coordinator Participant A  Participant B
     |            |            |
     |--VOTE-REQ->|            |
     |            |--prepare-->|
     |            |<-VOTE-COMMIT
     |------------VOTE-REQ---->|
     |            |            |--prepare-->
     |            |            |<-VOTE-COMMIT
(All votes commit)
     |--write commit log------>|
     |            |            |
     |--GLOBAL-COMMIT--------->|
     |            |--commit--->|
     |            |<-ACK-------|
     |<-ACK----------------------|
     |(Forget Tx) |            |
```

### Blocking Problem and Timeouts

The major drawback of 2PC is that it is a **blocking protocol**. If the coordinator fails after sending `VOTE-REQUEST` but before sending the final decision, participants are left in an uncertain state. They have prepared the transaction and are ready to commit, but they cannot proceed until they hear back from the coordinator. They are **blocked** and must wait for the coordinator to recover. This locks resources indefinitely, which is highly undesirable.

Participants use timeouts to detect coordinator failure. However, upon timing out, a participant cannot unilaterally decide to abort or commit because it doesn't know the decision or the state of other participants. Resolving this requires a complex and slow recovery procedure, often involving newly elected coordinators querying other participants.

## The Three-Phase Commit Protocol (3PC)

The Three-Phase Commit Protocol was designed to eliminate the blocking problem of 2PC. It introduces an extra phase to ensure the system can make progress even if the coordinator fails.

### The Three Phases

1.  **Phase 1: CanCommit?** Similar to 2PC's voting phase. The coordinator sends a `canCommit?` request. Participants respond with "Yes" if they are prepared to commit, otherwise "No".
2.  **Phase 2: PreCommit** (The new phase).
    *   If the coordinator receives all "Yes" responses, it sends a `preCommit` message to all participants. This message means, "We have unanimously agreed to commit; prepare to receive the final commit command."
    *   Upon receiving `preCommit`, a participant knows that *every other participant* has also voted to commit. It is now guaranteed that a commit decision will be made eventually.
3.  **Phase 3: DoCommit**
    *   The coordinator sends a `doCommit` message.
    *   Participants commit the transaction and send back an `ACK`.

### Non-Blocking Property

The key is the `preCommit` state. If a participant times out waiting for the `doCommit` message after receiving `preCommit`, it knows that all other participants are also in the `preCommit` state. Therefore, it can safely proceed to commit the transaction on its own, following a predefined election process to become the new coordinator. This makes 3PC **non-blocking**.

### Drawbacks of 3PC

While non-blocking, 3PC has significant drawbacks that limit its practical use:
*   **Increased Latency:** The extra message round-trip increases the time to complete a transaction.
*   **Complexity:** The protocol is more complex to implement and recover from.
*   **Network Assumption:** It assumes a *synchronous* network model where message delays are bounded, which is often not a realistic assumption in large-scale distributed systems. 2PC is more resilient in asynchronous networks.

Due to these reasons, 2PC, despite its blocking nature, is more widely used in practice, often with optimizations and well-defined recovery procedures.

## Comparison of 2PC and 3PC

| Feature | Two-Phase Commit (2PC) | Three-Phase Commit (3PC) |
| :--- | :--- | :--- |
| **Phases** | 2 (Vote, Decision) | 3 (CanCommit?, PreCommit, DoCommit) |
| **Blocking?** | **Yes.** Participants block if coordinator fails after prepare. | **No.** System can make progress after a coordinator failure. |
| **Message Cost** | 2n messages (n requests + n responses for phase 1, n commands + n acks for phase 2) | 3n messages (additional n preCommit messages) |
| **Latency** | Lower (2 rounds) | Higher (3 rounds) |
| **Complexity** | Simpler | More complex |
| **Network Model** | Works in asynchronous networks | Requires a synchronous network model |
| **Practical Use** | **Very common** (e.g., XA standard, distributed databases) | Rare, mostly of theoretical interest |

## Exam Tips

*   **Always emphasize the "all-or-nothing" property.** This is the core goal of atomic commit protocols.
*   **Clearly describe the roles of the coordinator and participants** in 2PC. Be able to walk through both the success and failure scenarios.
*   **Understand and be able to explain the blocking problem.** This is the critical weakness of 2PC. Describe what happens when the coordinator fails and why participants get stuck.
*   **Know why 3PC was proposed and how it solves blocking** (via the `preCommit` state). Also, be prepared to discuss its drawbacks.
*   **For diagram questions,** practice drawing the message flow for 2PC for both commit and abort cases. Label the phases.
*   **Remember the practical reality:** While 3PC is theoretically superior in terms of non-blocking, 2PC is the industry workhorse due to its simplicity and lower latency. Systems mitigate the blocking problem through efficient coordinator recovery mechanisms.