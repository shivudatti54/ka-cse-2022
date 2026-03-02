# Bitcoin Network and Wallets

## Introduction to the Bitcoin Network

The Bitcoin network is a decentralized, peer-to-peer (P2P) network that enables the transfer of value without the need for a central authority. It is the foundational infrastructure that supports the Bitcoin cryptocurrency, allowing participants (nodes) to communicate, validate transactions, and maintain a shared, immutable ledger—the blockchain.

### Key Characteristics of the Bitcoin Network

*   **Decentralization:** Unlike traditional client-server models, there is no central server. All nodes are equal participants, communicating directly with each other.
*   **Peer-to-Peer (P2P) Architecture:** Nodes form a mesh network, connecting to multiple other peers. This structure enhances resilience, as the network remains operational even if some nodes fail or disconnect.
*   **Permissionless:** Anyone can join the network by running a node software client (e.g., Bitcoin Core). No central authority grants permission.
*   **Open Source:** The network protocols and software are open source, allowing for transparency, auditability, and community-driven development.

### Network Nodes and Their Roles

Not all nodes in the Bitcoin network are identical. They can be categorized based on the functions they perform:

| Node Type | Key Functions | Resource Requirements | Description |
| :--- | :--- | :--- | :--- |
| **Full Node** | - Validates all transactions and blocks<br>- Relays transactions and blocks<br>- Stores a full copy of the blockchain | High (Storage, Bandwidth, CPU) | The backbone of the network. Enforces all consensus rules independently. It downloads every block and transaction and checks them against Bitcoin's core rules (e.g., no double-spending, valid signatures, correct block structure). |
| **Pruned Full Node** | - Validates all transactions and blocks<br>- Relays transactions and blocks | Medium (CPU, Bandwidth) but Low Storage | Performs all the functions of a full node but does not store the entire blockchain history. After validating blocks, it deletes old data, keeping only the headers and a small portion of the most recent blockchain data (e.g., the last ~5 GB). Still provides full security. |
| **Archival Full Node** | - Validates all transactions and blocks<br>- Relays transactions and blocks<br>- Serves historical data to other nodes | Very High (Storage, Bandwidth, CPU) | A full node that retains the entire blockchain history from the genesis block. These nodes are crucial for new nodes bootstrapping and for data analysis. |
| **Mining Node** | - Validates transactions and blocks<br>- Creates new blocks by solving Proof-of-Work<br>- Relays blocks | Extremely High (Specialized Hardware - ASICs) | A specialized full node that participates in the mining process. It bundles valid transactions into a candidate block and expends computational power to find a valid nonce that meets the network's difficulty target. |
| **SPV (Simplified Payment Verification) Client / Lightweight Node** | - Verifies transactions relevant to it<br>- Does not validate all rules | Low (Storage, Bandwidth) | Does not download the entire blockchain. Instead, it downloads only the block headers (~80 bytes each). To verify a transaction, it relies on connecting to full nodes and using Merkle proofs to cryptographically confirm the transaction was included in a valid block. Offers less security than a full node. Typical for mobile wallets. |

```
+----------------+     +----------------+     +----------------+
|   SPV/Light    |     |   Full Node    |     |  Mining Node   |
|    Wallet      |---->|  (Validator)   |<----|  (Miner)       |
+----------------+     +----------------+     +----------------+
         |                     |                       |
         | (Requests Merkle    | (Relays Valid Tx/Blk) | (Broadcasts
         |  Proofs for Tx)     |                       |  new Block)
         v                     v                       v
+-----------------------------------------------------------------+
|                  Bitcoin P2P Network Mesh                       |
+-----------------------------------------------------------------+
         ^                     ^                       ^
+----------------+     +----------------+     +----------------+
|   Merchant     |     |   Exchange     |     |   Another      |
|   Service      |---->|    Node        |<----|   Full Node    |
+----------------+     +----------------+     +----------------+
```

### How the Network Propagates Data

1.  **Transaction Propagation:** When a user creates a transaction, their wallet (node) broadcasts it to its connected peers.
2.  **Validation and Relay:** Each receiving peer validates the transaction against its memory pool (mempool) and consensus rules. If valid, it relays the transaction to its other peers. Invalid transactions are rejected and not propagated.
3.  **Block Propagation:** When a miner solves a block, it broadcasts the new block to its peers.
4.  **Block Validation:** Full nodes receiving the block validate every transaction within it and the block header (especially the Proof-of-Work). If valid, they add it to their local copy of the blockchain and relay it. This process ensures only valid blocks are accepted by the network.

This gossip protocol ensures data eventually reaches every node in the network, creating a robust and fault-tolerant system.

---

## Understanding Bitcoin Wallets

A Bitcoin wallet is a software application or hardware device that stores the cryptographic keys needed to interact with the Bitcoin blockchain. **Crucially, a wallet does not "store" bitcoin.** Bitcoin exist as immutable records on the distributed ledger. The wallet stores the keys that prove ownership of those records and allow them to be spent.

### Private Keys, Public Keys, and Addresses

*   **Private Key:** A secret 256-bit number (often represented in Wallet Import Format - WIF). This is the ultimate source of control over your bitcoin. **Anyone with the private key has complete control over the associated funds. It must be kept secret at all times.**
*   **Public Key:** A number derived from the private key using Elliptic Curve Cryptography (ECDSA, as covered in Module-2). It can be shared publicly and is used to generate addresses and verify digital signatures.
*   **Bitcoin Address:** An encoded version of the public key, often starting with '1', '3', or 'bc1'. It acts as the public destination to which others can send bitcoin. It is generated by applying a series of hash functions (SHA-256 and RIPEMD-160) and adding a checksum for error detection.

**Simplified Generation Path:**
`Private Key --(ECDSA)--> Public Key --(SHA-256 + RIPEMD-160 + checksum + encoding)--> Bitcoin Address`

### Types of Wallets

Wallets can be categorized based on how they manage keys and their connection to the internet.

**1. Based on Key Custody:**
*   **Custodial Wallet:** A third party (e.g., Coinbase, Binance) holds your private keys on your behalf. You trust them to manage security and conduct transactions. This is similar to a traditional bank.
*   **Non-Custodial Wallet:** You, the user, are in sole possession and control of your private keys. The wallet software helps you manage them, but the responsibility for securing them falls entirely on you. "Not your keys, not your coins."

**2. Based on Connection to the Internet (Hot vs. Cold):**
*   **Hot Wallet:** A wallet connected to the internet. This includes web wallets, exchange wallets, and desktop/mobile wallets. They are convenient for frequent transactions but are more vulnerable to online threats like hacking.
*   **Cold Wallet:** A wallet that remains offline. This provides a much higher level of security as the private keys are never exposed to an online environment.
    *   **Hardware Wallet:** A dedicated physical device (e.g., Ledger, Trezor) that stores keys offline. It signs transactions internally and only broadcasts the signed transaction to the network via a connected online device.
    *   **Paper Wallet:** A physical document that has a printed private key and public address. It's secure from digital theft but vulnerable to physical damage and loss.

**3. Based on Key Derivation (HD Wallets):**
Most modern wallets are Hierarchical Deterministic (HD) wallets.
*   **Non-HD Wallets:** A random private key is generated for each address. Managing backups for many keys is cumbersome.
*   **HD Wallets:** A single master **seed phrase** (typically 12 or 24 words) is generated. From this seed, a tree of millions of unique key pairs can be deterministically derived.
    *   **Benefit:** You only need to back up the seed phrase once to recover all past and future keys generated by the wallet.
    *   The seed phrase is the master key to all your funds. Its security is paramount.

### Comparison of Wallet Types

| Wallet Type | Example | Custody | Internet Connection | Security Level | Ease of Use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Exchange Wallet | Coinbase, Binance | Custodial | Hot | Low (You trust the exchange) | Very Easy |
| Mobile Wallet | BlueWallet, BRD | Non-Custodial | Hot | Medium | Easy |
| Desktop Wallet | Bitcoin Core, Electrum | Non-Custodial | Hot | Medium | Medium |
| Hardware Wallet | Ledger Nano, Trezor | Non-Custodial | Cold | High | Medium |
| Paper Wallet | BitAddress.org | Non-Custodial | Cold | High (if created securely) | Hard |

### The Transaction Lifecycle from a Wallet's Perspective

1.  **Creation:** A user initiates a send request in their wallet software, specifying the recipient's address and amount.
2.  **Signing:** The wallet constructs an unsigned transaction. Using the private key corresponding to the bitcoin being spent, the wallet creates a digital signature for the transaction, proving ownership.
3.  **Broadcasting:** The signed transaction is broadcast to the Bitcoin P2P network.
4.  **Propagation & Mempool:** The transaction is validated and propagated by nodes, landing in their mempools (pools of unconfirmed transactions).
5.  **Mining:** A mining node includes the transaction in a candidate block and performs Proof-of-Work.
6.  **Confirmation:** Once the block is mined and added to the blockchain, the transaction receives its first confirmation. Subsequent blocks build on top of it, increasing the number of confirmations and making the transaction more immutable.

---

## Exam Tips

*   **Focus on Key Differences:** Be able to clearly distinguish between full nodes and SPV nodes, and between hot and cold storage. Understand the security trade-offs involved.
*   **Understand the Sequence:** Know the step-by-step process of how a transaction is created, signed, broadcast, and confirmed. This is a common topic for longer questions.
*   **"Not Your Keys, Not Your Coins":** This mantra is central to Bitcoin. Be prepared to explain what it means in the context of custodial vs. non-custodial wallets.
*   **Remember the Mnemonic:** The seed phrase for an HD wallet is the root of all derived keys. Its importance for backup and recovery is critical.
*   **Visualize the Network:** Sketching a simple diagram of the P2P network with different node types can help structure your answer in an exam.