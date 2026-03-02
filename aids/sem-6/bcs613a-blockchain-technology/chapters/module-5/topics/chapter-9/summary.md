# **Chapter 9 Revision Notes**

## **Hyperledger Fabric Overview**

- Hyperledger Fabric is a modular, scalable, and highly-performant distributed ledger technology.
- It uses a client-server architecture and supports private and public blockchains.
- Fabric uses a consensus protocol called the "raft" algorithm.

## **Hyperledger Fabric Concepts**

- **Orderer:** The orderer is responsible for managing the ordering and validation of transactions.
- **Peer:** Peers are nodes that store and validate transactions.
- **Channel:** A channel is a dedicated network for a specific set of transactions.
- **Contract:** A contract is a self-executing smart contract that automates business logic.

## **Hyperledger Fabric Architecture**

- **Architecture Overview:**
  ```
  +---------------+
  |  Application  |
  +---------------+
           |
           |
           v
  +---------------+
  |  Chaincode    |
  +---------------+
           |
           |
           v
  +---------------+
  |  Smart Contract |
  +---------------+
           |
           |
           v
  +---------------+
  |  Peer         |
  +---------------+
           |
           |
           v
  +---------------+
  |  Orderer      |
  +---------------+
           |
           |
           v
  +---------------+
  |  Ledger       |
  +---------------+
  ```

## **Important Formulas and Definitions**

- **TPS (Transactions Per Second):** Measures the number of transactions processed per second.
- **Throughput:** The rate at which transactions are processed.
- **Latency:** The time it takes for a transaction to be processed.

## **Key Theorems**

- **Byzantine Generals' Theorem:** States that in a distributed system, there exists a set of generals who can agree on a decision even if some of them are faulty.
- **Raft Algorithm:** A consensus protocol that allows nodes to agree on a leader and make decisions.

## **Revision Tips**

- Understand the Hyperledger Fabric architecture and its components.
- Learn about the different types of blockchains supported by Fabric (private, public).
- Study the concepts of orderer, peer, channel, and contract.
- Practice deploying and managing smart contracts on Fabric.
