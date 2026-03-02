# **Methods for Handling Deadlocks**

## **Introduction**

In operating systems, a deadlock is a situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource. Deadlocks can lead to system instability and crashes. To prevent or recover from deadlocks, various methods have been developed. In this study material, we will explore the methods for handling deadlocks.

## **Definitions**

- **Deadlock**: A situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource.
- **Resource**: A variable or data that can be allocated to a process.

## **Methods for Handling Deadlocks**

### 1. **Abort and Restart**

In this method, the system terminates one of the processes involved in the deadlock and restarts it. This method is simple but can lead to data loss and system crashes.

- **Pros**:
  - Simple to implement
  - Fast recovery time
- **Cons**:
  - Data loss
  - System crashes

### 2. **Rollback Recovery**

In this method, the system rolls back the changes made by the processes involved in the deadlock. This method requires a log of all transactions and can be time-consuming.

- **Pros**:
  - Data consistency
  - No data loss
- **Cons**:
  - Time-consuming
  - Log maintenance

### 3. **Priority Inheritance**

In this method, the process with the highest priority inherits the resources of the process with the lower priority. This method can lead to priority inversion.

- **Pros**:
  - Prevents priority inversion
  - Fast recovery time
- **Cons**:
  - Priority inversion
  - Resource starvation

### 4. **Resource Preemption**

In this method, the operating system forcibly takes the resources of a process involved in a deadlock and assigns them to another process. This method can lead to resource fragmentation.

- **Pros**:
  - Prevents resource fragmentation
  - Resource sharing
- **Cons**:
  - Resource fragmentation
  - Resource starvation

### 5. **Deadlock Detection and Prevention**

In this method, the system detects deadlocks at the beginning of the execution and prevents them from occurring. This method requires complex scheduling algorithms.

- **Pros**:
  - Prevents deadlocks
  - Fast recovery time
- **Cons**:
  - Complex scheduling algorithms
  - Resource starvation

### 6. ** banker's algorithm**

In this method, the system uses a banker's algorithm to allocate resources to processes. This method requires complex scheduling algorithms.

- **Pros**:
  - Prevents deadlocks
  - Fast recovery time
- **Cons**:
  - Complex scheduling algorithms
  - Resource starvation

## **Conclusion**

Deadlocks are a common problem in operating systems. The above methods can be used to prevent or recover from deadlocks. The choice of method depends on the specific requirements of the system.

## **Example**

Suppose we have three processes, P1, P2, and P3, and three resources, R1, R2, and R3. The process allocation table is as follows:

| Process | Resource 1 | Resource 2 | Resource 3 |
| ------- | ---------- | ---------- | ---------- |
| P1      | 1          | 0          | 1          |
| P2      | 1          | 1          | 0          |
| P3      | 0          | 1          | 1          |

The process scheduling table is as follows:

| Process | Priority |
| ------- | -------- |
| P1      | 2        |
| P2      | 3        |
| P3      | 1        |

In this scenario, P1 and P2 are waiting for resource R3, and P3 is waiting for resource R2. Therefore, we have a deadlock situation.

To resolve this deadlock, we can use the banker's algorithm. The algorithm allocates one more resource to P1 and P2, and then assigns resource R3 to P3.

| Process | Resource 1 | Resource 2 | Resource 3 |
| ------- | ---------- | ---------- | ---------- |
| P1      | 1          | 0          | 1          |
| P2      | 1          | 1          | 2          |
| P3      | 0          | 1          | 1          |

Now, P1 and P2 have enough resources to execute, and P3 has enough resources to execute. Therefore, we have resolved the deadlock situation.
