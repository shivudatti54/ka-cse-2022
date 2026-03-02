# **Structure of Page Table**

### Introduction

In this chapter, we will explore the concept of page tables and their structure. Page tables are a crucial data structure in operating systems, used to manage virtual memory. In this section, we will discuss the different components of a page table and their relationships.

### 8.1 Page Table Structure

A page table is a data structure that maps virtual addresses to physical addresses. It is used to translate virtual memory addresses to physical memory addresses.

**Key Components of a Page Table:**

- **Page Table Entry (PTE):** A PTE is a single entry in the page table that maps a virtual page to a physical page.
- **Page Number (PN):** The page number is the virtual address of a page.
- **Frame Number (FN):** The frame number is the physical address of a page.
- **Valid Bit (V):** The valid bit indicates whether the page is valid or not.
- **Dirty Bit (D):** The dirty bit indicates whether the page has been modified.

**Example:**

Suppose we have a page table with the following entries:

| Page Table Entry (PTE) | Page Number (PN) | Frame Number (FN) | Valid Bit (V) | Dirty Bit (D) |
| ---------------------- | ---------------- | ----------------- | ------------- | ------------- |
| PTE1                   | 100              | 0x1000            | 1             | 0             |
| PTE2                   | 101              | 0x2000            | 1             | 0             |
| PTE3                   | 102              | 0x3000            | 0             | 1             |

In this example, PTE1 maps virtual page 100 to physical page 0x1000, PTE2 maps virtual page 101 to physical page 0x2000, and PTE3 maps virtual page 102 to physical page 0x3000. The valid bit for PTE1 and PTE2 is 1, indicating that the pages are valid. The dirty bit for PTE3 is 1, indicating that the page has been modified.

### 8.2 Page Table Types

There are two types of page tables:

- **Translation Lookaside Buffer (TLB):** A TLB is a small, fast page table that maps recent virtual addresses to physical addresses.
- **Main Page Table:** A main page table is a larger, slower page table that maps all virtual addresses to physical addresses.

**Key Differences:**

- **Size:** TLBs are smaller than main page tables.
- **Speed:** TLBs are faster than main page tables.
- ** Cacheability:** TLBs are usually cacheable, while main page tables are not.

### 8.3 Page Table Update

When a page is modified, the dirty bit in the page table entry is set. When the page is swapped out, the valid bit is cleared. When the page is swapped back in, the valid bit is set.

**Example:**

Suppose we have a page table with the following entries:

| Page Table Entry (PTE) | Page Number (PN) | Frame Number (FN) | Valid Bit (V) | Dirty Bit (D) |
| ---------------------- | ---------------- | ----------------- | ------------- | ------------- |
| PTE1                   | 100              | 0x1000            | 1             | 0             |
| PTE2                   | 101              | 0x2000            | 1             | 0             |

Suppose we modify page 100. The dirty bit for PTE1 is set to 1.

| Page Table Entry (PTE) | Page Number (PN) | Frame Number (FN) | Valid Bit (V) | Dirty Bit (D) |
| ---------------------- | ---------------- | ----------------- | ------------- | ------------- |
| PTE1                   | 100              | 0x1000            | 1             | 1             |
| PTE2                   | 101              | 0x2000            | 1             | 0             |

When page 100 is swapped out, the valid bit for PTE1 is cleared to 0.

| Page Table Entry (PTE) | Page Number (PN) | Frame Number (FN) | Valid Bit (V) | Dirty Bit (D) |
| ---------------------- | ---------------- | ----------------- | ------------- | ------------- |
| PTE1                   | 100              | 0x1000            | 0             | 1             |
| PTE2                   | 101              | 0x2000            | 1             | 0             |

When page 100 is swapped back in, the valid bit for PTE1 is set to 1.

| Page Table Entry (PTE) | Page Number (PN) | Frame Number (FN) | Valid Bit (V) | Dirty Bit (D) |
| ---------------------- | ---------------- | ----------------- | ------------- | ------------- |
| PTE1                   | 100              | 0x1000            | 1             | 1             |
| PTE2                   | 101              | 0x2000            | 1             | 0             |

### 8.4 Page Table Search

When a process needs to access a page, the page table is searched to find the corresponding physical page.

**Example:**

Suppose we have a page table with the following entries:

| Page Table Entry (PTE) | Page Number (PN) | Frame Number (FN) | Valid Bit (V) | Dirty Bit (D) |
| ---------------------- | ---------------- | ----------------- | ------------- | ------------- |
| PTE1                   | 100              | 0x1000            | 1             | 0             |
| PTE2                   | 101              | 0x2000            | 1             | 0             |
| PTE3                   | 102              | 0x3000            | 0             | 1             |

Suppose we want to access page 101. The page table is searched, and PTE2 is found. Since the valid bit for PTE2 is 1, page 101 is mapped to physical page 0x2000.

### 8.5 Deadlock Detection

Deadlock detection is used to detect whether a process is deadlocked at a particular point in time.

**Algorithm:**

1.  Create a set of all processes currently executing.
2.  For each process P in the set:
    - Check if P is waiting for any other process Q to release a resource R.
    - If P is waiting for Q to release R, then check if Q is waiting for P to release R.
    - If both P is waiting for Q to release R and Q is waiting for P to release R, then P and Q are deadlocked.

**Example:**

Suppose we have two processes P and Q, each waiting for the other to release a resource.

| Process | Resource | Waiting For |
| ------- | -------- | ----------- |
| P       | R1       | Q           |
| Q       | R2       | P           |

In this case, P and Q are deadlocked.

### 9.1 Deadlock Prevention

Deadlock prevention is used to prevent deadlocks from occurring in the first place.

**Algorithm:**

1.  Assign a unique resource ID to each resource.
2.  When a process P requests a resource R, check if P has a lock on R.
3.  If P has a lock on R, then check if P is waiting for any other resource.
4.  If P is waiting for any other resource, then P is deadlocked and the request is denied.

**Example:**

Suppose we have two processes P and Q, each requesting a resource R.

| Process | Resource | Resource ID |
| ------- | -------- | ----------- |
| P       | R1       | 1           |
| Q       | R2       | 2           |

If P has a lock on R1 and Q is waiting for P to release R1, then P and Q are deadlocked.

### 9.2 Deadlock Recovery

Deadlock recovery is used to recover from a deadlock situation.

**Algorithm:**

1.  Identify the deadlock situation.
2.  Choose a process P to roll back.
3.  Roll back P's actions until P releases any resources.
4.  Repeat the process for each process until all processes are released.

**Example:**

Suppose we have two processes P and Q, each trying to acquire a resource R.

| Process | Resource | Resource ID |
| ------- | -------- | ----------- |
| P       | R1       | 1           |
| Q       | R2       | 2           |

If P acquires R1 and Q tries to acquire R2, then P and Q are deadlocked. We can roll back P's actions until P releases R1, and then repeat the process for Q.

| Process | Resource | Resource ID |
| ------- | -------- | ----------- |
| P       | -        | -           |
| Q       | R2       | 2           |

We can then roll back P's actions until P releases R1, and repeat the process for Q.

### 9.3 Deadlock Avoidance

Deadlock avoidance is used to prevent deadlocks from occurring in the first place.

**Algorithm:**

1.  Use a bank account system to assign resources to processes.
2.  When a process P requests a resource R, check if P's bank account has enough credits to release R.
3.  If P's bank account has enough credits, then check if P is waiting for any other resource.
4.  If P is waiting for any other resource, then P is deadlocked and the request is denied.

**Example:**

Suppose we have two processes P and Q, each requesting a resource R.

| Process | Resource | Resource ID | Bank Account |
| ------- | -------- | ----------- | ------------ |
| P       | R1       | 1           | 5            |
| Q       | R2       | 2           | 3            |

If P acquires R1 and Q tries to acquire R2, then P and Q are deadlocked. We can check P's bank account and see that it has enough credits to release R1. We can then check Q's bank account and see that it does not have enough credits to release R2. Therefore, P is not deadlocked and Q's request is denied.

### 9.4.1 Bank Account System

The bank account system is a deadlock avoidance algorithm that assigns resources to processes using a bank account system.

**How it works:**

1.  Each process is assigned a bank account with a set of credits for each resource.
2.  When a process P requests a resource R, it checks if P's bank account has enough credits to release R.
3.  If P's bank account has enough credits, then P can acquire R.
4.  If P's bank account does not have enough credits, then P cannot acquire R.

**Example:**

Suppose we have two processes P and Q, each requesting a resource R.

| Process | Resource | Resource ID | Bank Account |
| ------- | -------- | ----------- | ------------ |
| P       | R1       | 1           | 5            |
| Q       | R2       | 2           | 3            |

If P acquires R1 and Q tries to acquire R2, then P's bank account is updated to (5 - 1) = 4 credits.

| Process | Resource | Resource ID | Bank Account |
| ------- | -------- | ----------- | ------------ |
| P       | R1       | 1           | 4            |
| Q       | R2       | 2           | 3            |

If Q tries to acquire R2, it will check P's bank account and see that it has enough credits to release R1. Q can then acquire R2.

| Process | Resource | Resource ID | Bank Account |
| ------- | -------- | ----------- | ------------ |
| P       | R1       | 1           | 4            |
| Q       | R1       | 1           | 2            |
| Q       | R2       | 2           | 3            |
