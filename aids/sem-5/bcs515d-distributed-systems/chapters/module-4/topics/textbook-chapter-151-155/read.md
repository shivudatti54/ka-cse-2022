# **Distributed Systems: Coordination and Agreement**

## **Chapter 15.1: Introduction**

- Distributed systems are a collection of independent computers that work together as a single system to achieve a common goal.
- Each computer in the system is called a node or a process.
- The nodes communicate with each other using a network to share resources and coordinate their actions.
- Distributed systems are used in various applications such as banking, stock trading, and social media.

## **Characteristics of Distributed Systems**

- **Decentralization**: No single node controls the entire system.
- **Autonomy**: Each node operates independently.
- **Distribution**: Nodes are geographically dispersed.
- **Concurrency**: Multiple nodes can execute tasks simultaneously.
- **Fault tolerance**: The system can continue to function even if some nodes fail.

## **Coordination and Agreement**

- Coordination refers to the process of synchronizing the actions of multiple nodes in a distributed system.
- Agreement refers to the process of ensuring that all nodes agree on a particular value or state.
- Coordination and agreement are essential for achieving the common goal of a distributed system.

## **Distributed Mutual Exclusion**

- Distributed mutual exclusion is a problem in distributed systems where two or more nodes want to access a shared resource simultaneously.
- The problem requires that only one node can access the resource at a time.
- Distributed mutual exclusion can be solved using various algorithms such as:
  - **Token Ring algorithm**: Each node has a token that can be passed to the next node.
  - **Token Bucket algorithm**: Each node has a bucket that can be depleted when the token is passed.
  - **Piggyback algorithm**: A node passes the token to the next node and then sends a message to the current node.

## **Distributed Generalized Lock Algorithm**

- The Distributed Generalized Lock Algorithm (DGLA) is a distributed mutual exclusion algorithm that allows multiple readers to access a shared resource simultaneously.
- The algorithm uses a token ring data structure to grant access to the resource.
- The DGLA ensures that only one writer can access the resource at a time and multiple readers can access the resource simultaneously.

## **Distributed Generalized Wait-Free Algorithm**

- The Distributed Generalized Wait-Free Algorithm (DGWA) is a distributed mutual exclusion algorithm that allows multiple readers to access a shared resource simultaneously without any wait.
- The algorithm uses a token ring data structure to grant access to the resource.
- The DGWA ensures that only one writer can access the resource at a time and multiple readers can access the resource simultaneously without any wait.

## **Real-World Applications**

- **Database systems**: Distributed mutual exclusion is used in database systems to allow multiple users to access shared data simultaneously.
- **Web servers**: Distributed mutual exclusion is used in web servers to allow multiple users to access shared resources simultaneously.
- **Social media platforms**: Distributed mutual exclusion is used in social media platforms to allow multiple users to access shared resources simultaneously.
