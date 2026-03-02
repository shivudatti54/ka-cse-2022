# **Distributed Systems: Chapter 17.1-17.6**

## **Introduction to Distributed Systems**

Distributed systems are computer systems that consist of multiple interconnected nodes, which can be located in different geographical locations. These nodes can be connected through a network, such as the internet, and work together to achieve a common goal. Distributed systems are designed to provide a scalable, fault-tolerant, and flexible way to process and share data.

## **Historical Context**

The concept of distributed systems dates back to the 1960s, when the first network, ARPANET, was developed. ARPANET was a packet-switched network that connected multiple nodes, including computers, printers, and other devices. The network was used for communication and data transfer between these nodes.

In the 1970s and 1980s, distributed systems began to gain popularity with the development of the Internet and the World Wide Web. The Internet enabled the creation of a global network of interconnected computers, while the World Wide Web provided a platform for sharing and accessing information over the internet.

## **Types of Distributed Systems**

There are several types of distributed systems, including:

- **Client-Server Systems**: In a client-server system, a client (usually a user interface) requests services from a server, which is a program that provides services to clients.
- **Peer-to-Peer Systems**: In a peer-to-peer system, each node acts as both a client and a server, and can communicate directly with other nodes.
- **Cloud Computing Systems**: Cloud computing systems are distributed systems that provide on-demand access to computing resources, such as servers, storage, and applications.

## **Distributed Transactions**

A distributed transaction is a sequence of operations that are executed across multiple nodes in a distributed system. Distributed transactions are used to ensure that multiple nodes work together to achieve a common goal.

## **Flattened Distributed Transactions**

A flattened distributed transaction is a type of distributed transaction where the transaction is executed in a linear sequence, without the use of locks. This approach is simpler and faster than nested transactions, but it can lead to inconsistencies if one node fails before the transaction is committed.

## **Nested Distributed Transactions**

A nested distributed transaction is a type of distributed transaction where the transaction is executed in a hierarchical sequence, with inner transactions being executed before outer transactions. Nested transactions provide higher levels of isolation and consistency than flattened transactions.

## **Example of Flattened Distributed Transactions**

```markdown
+---------------+
| Node 1 |
+---------------+
|
| Transaction 1
v
+---------------+
| Node 2 |
+---------------+
|
| Transaction 2
v
+---------------+
| Node 3 |
+---------------+
```

In this example, Node 1 and Node 2 execute their transactions in sequence, without the use of locks. If Node 1 fails before the transaction is committed, the transaction will be rolled back, and Node 2 will not be affected.

## **Example of Nested Distributed Transactions**

```markdown
+---------------+
| Node 1 |
+---------------+
|
| Transaction 1 (inner)
v
+---------------+
| Node 2 |
+---------------+
|
| Transaction 2 (outer)
v
+---------------+
| Node 3 |
+---------------+
```

In this example, Node 1 executes its inner transaction before Node 2 executes its outer transaction. If Node 1 fails before the inner transaction is committed, the outer transaction will be rolled back, and Node 2 will not be affected.

## **Applications of Distributed Transactions**

Distributed transactions have many applications in distributed systems, including:

- **Financial transactions**: Distributed transactions are used in financial systems to transfer funds between accounts.
- **Supply chain management**: Distributed transactions are used in supply chain management to track inventory and manage orders.
- **Healthcare**: Distributed transactions are used in healthcare to manage patient records and share medical information.

## **Case Study: Distributed Transaction in Banking**

A bank wants to transfer funds from one account to another. The bank uses a distributed transaction to ensure that the transfer is executed in a linear sequence, without the use of locks. If the transfer is successful, the funds are transferred, and the transaction is committed. If the transfer fails, the transaction is rolled back, and the funds are not transferred.

## **Further Reading**

- **"Distributed Systems"** by Andrew S. Tanenbaum and Maarten van Steen
- **"Cloud Computing"** by David T. Campbell and Thomas Erl
- **"Distributed Transactions"** by Philip Bernstein, Nancy Goodman, and Eugenio Martinelli

In conclusion, distributed systems are computer systems that consist of multiple interconnected nodes, which can be located in different geographical locations. Distributed transactions are a type of distributed system that ensures multiple nodes work together to achieve a common goal. Flattened and nested distributed transactions are two types of distributed transactions, with flattened transactions being simpler and faster, but potentially leading to inconsistencies, and nested transactions providing higher levels of isolation and consistency. Distributed transactions have many applications in distributed systems, including financial transactions, supply chain management, and healthcare.
