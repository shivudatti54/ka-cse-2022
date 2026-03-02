# Granularity of Data Items and Multiple Granularity Locking

## Table of Contents

- [Granularity of Data Items and Multiple Granularity Locking](#granularity-of-data-items-and-multiple-granularity-locking)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Data Item Granularity](#data-item-granularity)
  - [Trade-offs in Granularity Selection](#trade-offs-in-granularity-selection)
  - [Multiple Granularity Locking (MGL) Protocol](#multiple-granularity-locking-mgl-protocol)
  - [Lock Escalation](#lock-escalation)
- [Examples](#examples)
  - [Example 1: Simple MGL Lock Acquisition](#example-1-simple-mgl-lock-acquisition)
  - [Example 2: Transaction Modifying Multiple Records](#example-2-transaction-modifying-multiple-records)
  - [Example 3: SIX Lock Usage](#example-3-six-lock-usage)
  - [Example 4: Compatibility Analysis](#example-4-compatibility-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Concurrency control in database management systems is essential for ensuring correct and consistent transaction execution when multiple users access the database simultaneously. One of the fundamental approaches to concurrency control is locking-based protocols. The **granularity of data items** refers to the size or level of detail at which locks are acquired in a database system. Choosing the appropriate lock granularity significantly impacts system performance, concurrency, and the overhead associated with lock management.

Multiple Granularity Locking (MGL) is an advanced locking protocol that addresses the limitations of fixed-granularity locking by allowing locks to be acquired at multiple levels of the database hierarchy simultaneously. This approach provides a flexible mechanism that balances the trade-off between concurrency and locking overhead. Understanding these concepts is crucial for database administrators and developers designing systems that require high throughput while maintaining data consistency.

In the context of the university's Database Management System curriculum, this topic forms a critical component of Module 5, dealing with advanced transaction processing concepts. The ability to design and analyze locking protocols at various granularities is essential for developing robust database applications and understanding how commercial database systems implement concurrency control mechanisms.

## Key Concepts

### Data Item Granularity

Granularity refers to the size of the data item that can be locked in a database system. The database hierarchy provides multiple levels at which locks can be applied:

1. **Database Level**: The entire database is locked as a single unit. This provides maximum simplicity but minimum concurrency. Only one transaction can access the database at a time.

2. **File Level**: An entire file (or relation/table) is locked. This offers better concurrency than database-level locking but still restricts access to multiple tables simultaneously.

3. **Page Level**: A page (typically 4KB-16KB) is the locked unit. This is common in many database systems like DB2 and Oracle. It provides moderate concurrency with reasonable overhead.

4. **Record Level**: Individual database tuples/rows are locked. This provides maximum concurrency but incurs significant lock management overhead.

5. **Field/Attribute Level**: Individual fields within a record can be locked. This offers the highest granularity but is rarely implemented due to excessive overhead.

### Trade-offs in Granularity Selection

**Fine Granularity (Record/Field level)**:

- **Advantages**: Maximum concurrency - multiple transactions can access different records simultaneously
- **Disadvantages**: Higher lock management overhead, more memory for lock tables, increased chance of deadlocks

**Coarse Granularity (Database/File level)**:

- **Advantages**: Low lock management overhead, fewer locks needed, reduced deadlock probability
- **Disadvantages**: Low concurrency - blocks access to unrelated data

### Multiple Granularity Locking (MGL) Protocol

Multiple Granularity Locking solves the problem of choosing the optimal granularity by allowing locks at multiple levels simultaneously. The protocol uses a hierarchical structure where locks on parent nodes indicate the intent to lock child nodes.

#### Lock Types in MGL

1. **Shared (S) Lock**: Allows reading but not modifying the data item. Compatible with other S locks on the same item.

2. **Exclusive (X) Lock**: Allows both reading and modifying the data item. Not compatible with any other lock type.

3. **Intention Shared (IS) Lock**: Indicates that the transaction intends to place S locks on child nodes. Must be held before acquiring S locks at lower levels.

4. **Intention Exclusive (IX) Lock**: Indicates that the transaction intends to place X locks on child nodes. Must be held before acquiring X locks at lower levels.

5. **Shared Intention Exclusive (SIX) Lock**: A combination lock indicating S lock on the current node with IX on child nodes. Used when reading entire granularity while also updating some child items.

#### Compatibility Matrix

The lock compatibility matrix determines which lock types can be held simultaneously:

|     | IS  | IX  | S   | SIX | X   |
| --- | --- | --- | --- | --- | --- |
| IS  | Yes | Yes | Yes | Yes | No  |
| IX  | Yes | Yes | No  | No  | No  |
| S   | Yes | No  | Yes | No  | No  |
| SIX | Yes | No  | No  | No  | No  |
| X   | No  | No  | No  | No  | No  |

#### MGL Locking Rules

1. The transaction must acquire appropriate locks starting from the root of the hierarchy.

2. To acquire an S lock on a node, the transaction must hold either IS or IX lock on its parent.

3. To acquire an X lock on a node, the transaction must hold either IX or SIX lock on its parent.

4. Locks are released in reverse order (bottom-up) at transaction commit or abort.

5. A node cannot be locked in S or IS mode if any descendant node is currently locked.

6. A node cannot be locked in X or IX mode if any descendant node is currently locked.

### Lock Escalation

Lock escalation is a mechanism that automatically promotes locks from fine granularity to coarser granularity when the number of locks held by a transaction exceeds a predefined threshold. This helps control lock management overhead while maintaining reasonable concurrency.

## Examples

### Example 1: Simple MGL Lock Acquisition

Consider a database hierarchy: Database → File1 → Page1 → Record1

**Scenario**: Transaction T1 wants to read Record1.

**Step-by-step solution**:

1. Acquire IS lock on Database (root level)
2. Acquire IS lock on File1 (intermediate level)
3. Acquire IS lock on Page1 (intermediate level)
4. Acquire S lock on Record1 (target level)

Lock hierarchy: IS(Database) → IS(File1) → IS(Page1) → S(Record1)

This ensures the system knows the transaction's intent at all levels before accessing the finest granularity.

### Example 2: Transaction Modifying Multiple Records

Consider: Database → File1 → Page1 → Records {R1, R2, R3}

**Scenario**: Transaction T2 wants to update R1 and R2 on Page1.

**Step-by-step solution**:

1. Acquire IX lock on Database
2. Acquire IX lock on File1
3. Acquire IX lock on Page1
4. Acquire X lock on R1
5. Acquire X lock on R2

Lock hierarchy: IX(Database) → IX(File1) → IX(Page1) → X(R1), X(R2)

Note: R3 remains unlocked and can be accessed by other transactions.

### Example 3: SIX Lock Usage

Consider: Database → File1 (contains Employee table)

**Scenario**: Transaction T3 needs to read the entire Employee table (S lock) and update one specific employee record (X lock on that record).

**Step-by-step solution**:

1. Acquire SIX lock on Database (S on Database + IX on descendants)
2. Acquire S lock on File1 (already covered by SIX at parent)
3. Acquire X lock on the specific Employee record

Lock hierarchy: SIX(Database) → S(File1) → X(SpecificRecord)

This is more efficient than holding S lock on File1 plus IX lock, as SIX combines both in a single lock type.

### Example 4: Compatibility Analysis

**Given**: Transaction T1 holds IX lock on Page1

**Question**: Can Transaction T2 acquire S lock on Record1 (child of Page1)?

**Analysis**:

- T1 holds: IX on Page1
- T2 wants: S on Record1

From compatibility matrix:

- IX (row) vs S (column): "No" - Not compatible

**Result**: T2 must wait until T1 releases IX lock on Page1.

**Question**: What if T1 held IS lock instead?

- IS (row) vs S (column): "Yes" - Compatible

**Result**: T2 can acquire S lock on Record1 immediately.

## Exam Tips

1. **Remember the lock compatibility matrix**: This is frequently tested in university exams. The compatibility between IS/IX/S/SIX/X locks is crucial for solving problems.

2. **Lock hierarchy order**: Always acquire locks from root to leaf (top-down) and release from leaf to root (bottom-up) in MGL protocols.

3. **Intent locks are hierarchical**: IS and IX locks indicate intention to acquire finer granularity locks. They must be acquired before S or X locks at lower levels.

4. **SIX lock efficiency**: Remember that SIX = S + IX combined. It provides read access to entire granularity while allowing updates to specific child items.

5. **Deadlock possibility**: Fine-grained locking increases deadlock probability because more locks are held simultaneously. Coarse-grained locking reduces deadlock probability but also reduces concurrency.

6. **Lock escalation thresholds**: When a transaction holds many fine-grained locks, the system may escalate to a coarse-grained lock to reduce overhead.

7. **Multiple granularity benefits**: The main advantage is balancing concurrency (fine) with overhead (coarse) by allowing dynamic choice.

8. **Problem-solving approach**: For exam questions, first identify the database hierarchy, then determine what each transaction needs to do, and finally apply the locking rules step-by-step.

9. **Remember the rules**: Before acquiring S lock at level i, must hold IS or S at level i-1. Before acquiring X lock at level i, must hold IX, SIX, or X at level i-1.

10. **Common misconception**: Students often forget that intent locks (IS, IX) must be acquired at all intermediate levels, not just the parent of the target node.
