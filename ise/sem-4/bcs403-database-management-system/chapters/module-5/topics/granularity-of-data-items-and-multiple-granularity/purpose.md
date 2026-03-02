### Learning Purpose: Granularity of Data Items & Multiple Granularity Locking

1.  **Why is this topic important?**
    This topic is crucial because it tackles the fundamental trade-off in database concurrency control: performance versus data integrity. Choosing the right "size" (granularity) of a data item to lock is vital. Locking entire tables is safe but cripples concurrency; locking individual rows is efficient but can lead to overhead and complexity. Multiple Granularity Locking (MGL) provides a sophisticated protocol to manage this, allowing transactions to lock data at different levels (database, table, page, row) simultaneously while ensuring serializability and preventing conflicts.

2.  **What will students learn?**
    Students will learn to define data granularity and identify the advantages and disadvantages of coarse-grained versus fine-grained locking. They will understand the principles of the MGL protocol, including the use of intention locks (IS, IX) to signal locking at a lower level. They will be able to explain how MGL enhances concurrency by allowing operations that do not conflict to proceed in parallel while strictly isolating conflicting operations.

3.  **How does it connect to other concepts?**
    This concept is a direct and advanced application of concurrency control theory, building directly on foundational knowledge of locks, serializability, and deadlock. It connects the theoretical concepts of schedules and conflicts to their practical implementation in real-world Database Management Systems (DBMS), which almost universally employ a form of MGL. It is also a key enabler for transaction processing and high-availability systems.

4.  **Real-world applications**
    MGL is not just theoretical; it is implemented in nearly every major DBMS (e.g., Oracle, SQL Server, PostgreSQL). It is the mechanism that allows an online store's database to process thousands of transactions per second—like reading product inventory (table-level lock) while multiple customers simultaneously place orders and update stock levels (row-level locks)—without compromising data consistency or bringing the system to a halt.