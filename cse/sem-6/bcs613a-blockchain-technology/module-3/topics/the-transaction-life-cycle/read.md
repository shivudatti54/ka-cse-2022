# Module 3: Blockchain Transaction Life Cycle

## Introduction

In traditional centralized systems like banks, a transaction is a simple update to a central ledger. Blockchain, however, is a decentralized peer-to-peer network, which makes the process of recording a transaction fundamentally different and more complex. Understanding the life cycle of a transaction—from its initiation to its permanent addition to the blockchain—is crucial for grasping how trust and consensus are achieved in a trustless environment. This note breaks down this process step-by-step.

---

## The Transaction Life Cycle: A Step-by-Step Breakdown

The journey of a transaction can be summarized in seven key stages.

### 1. Transaction Creation & Signing

It all starts when a user (say, Alice) wants to send some cryptocurrency (e.g., 1 Bitcoin) to another user (Bob).

- **Action:** Alice's wallet software creates a **transaction message**. This message contains:
- **Inputs:** References to the previous transactions where Alice received the Bitcoins she now wants to spend (proving she has the funds).
- **Outputs:** Bob's public address and the amount (1 BTC). It can also include a change output back to Alice's own address if the input was for more than 1 BTC.
- **Other Metadata:** Network fees, version number, etc.
- **Cryptographic Signing:** To authorize this transaction, Alice must prove she owns the inputs. Her wallet software uses her **private key** to digitally sign the transaction. This signature is added to the transaction data, creating a signed, valid transaction object. This proves that she is the rightful owner authorizing the transfer.

**Example:** It's like writing a cheque (creating the transaction), filling in the amount and payee (outputs), citing your bank account number as the source of funds (inputs), and then signing it at the bottom (cryptographic signature).

### 2. Broadcasting to the Network

Once signed, Alice's wallet broadcasts this transaction to all **nodes** (computers participating in the network) it is connected to. Each node that receives it will validate it and then forward it to its peers. This flooding mechanism ensures the transaction propagates across the entire network within seconds.

### 3. Initial Validation by Nodes

Every node that receives the transaction performs a set of checks to validate it before relaying it further. This is a critical first line of defense against invalid transactions. Key checks include:

- **Digital Signature Verification:** Does the signature match the public address of the inputs?
- **Double-Spending Check:** Are the inputs listed in the transaction actually unspent? The node checks its copy of the blockchain to ensure the funds haven't already been spent in a previous transaction.
- **Syntax Check:** Is the transaction structured correctly?
  If it fails any check, it is immediately rejected and not propagated.

### 4. Inclusion in the Mempool

Once a transaction passes the initial validation, it is placed in a waiting area called the **mempool** (memory pool). The mempool is a node's collection of all valid, unconfirmed transactions waiting to be included in a block. Transactions here are "pending." Nodes may have slightly different mempools based on which transactions they have received.

### 5. Block Creation by a Miner/Validator

A special node called a **miner** (in Proof-of-Work) or **validator** (in Proof-of-Stake) takes on the role of grouping transactions from the mempool into a candidate **block**. They select transactions, often prioritizing those with higher transaction fees (as these fees are their reward). They then perform the computationally expensive work of finding a valid hash for this new block (solving the "cryptographic puzzle" in PoW).

### 6. Block Propagation & Consensus

Once the miner finds a valid hash, they broadcast the new block to the network. Other nodes receive this block and perform a new set of validations:

- **Verify the Proof-of-Work** (i.e., does the block's hash meet the difficulty target?).
- **Validate all transactions** inside the block again.
- Check that the block links correctly to the previous block.

If the block is valid, nodes add it to their local copy of the blockchain. This is where **consensus** is achieved: the network agrees that this block is the next legitimate one in the chain. The transactions inside it are now considered **confirmed**.

### 7. Subsequent Confirmations

The first confirmation happens when the block is added. As subsequent blocks are mined and added on top of it, the transaction gains more **confirmations**. Each new block makes it exponentially harder to reverse the transaction, as it would require re-mining not just that block but all blocks after it. For high-value transfers, it's common to wait for multiple confirmations (e.g., 3-6) to ensure settlement.

---

## Key Points & Summary

| Stage                 | Key Actor        | Action                                                               | Outcome                                                           |
| :-------------------- | :--------------- | :------------------------------------------------------------------- | :---------------------------------------------------------------- |
| **1. Creation**       | User/Wallet      | A transaction message is created and cryptographically signed.       | A valid, signed transaction object.                               |
| **2. Broadcast**      | Wallet/Node      | The transaction is sent to peer nodes in the network.                | The transaction propagates across the P2P network.                |
| **3. Validation**     | Network Nodes    | Nodes check the transaction's validity (signature, no double-spend). | Invalid transactions are rejected; valid ones are relayed.        |
| **4. Mempool**        | Network Nodes    | Valid transactions wait in a temporary holding area.                 | Transactions are in a pending state.                              |
| **5. Block Creation** | Miner/Validator  | Transactions are grouped into a candidate block and mined/validated. | A new, valid block is created.                                    |
| **6. Consensus**      | Network Nodes    | The new block is validated and accepted by the network.              | The block is added to the blockchain; transactions are confirmed. |
| **7. Confirmations**  | Network (Miners) | New blocks are added on top of the block containing the transaction. | The transaction becomes more secure and immutable.                |

**In essence, the transaction life cycle is a process of moving from a user-initiated intent to a network-verified and consensus-backed fact, achieving decentralization and trust through cryptographic proof and distributed agreement.**
