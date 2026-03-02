# Introduction to Bitcoin

## What is Bitcoin?

Bitcoin is a decentralized digital currency, often referred to as a cryptocurrency, that enables peer-to-peer transactions without the need for a central authority or intermediary. It was introduced in a 2008 whitepaper by an individual or group using the pseudonym Satoshi Nakamoto. Bitcoin operates on a technology called blockchain, which is a public, distributed ledger that records all transactions across a network of computers.

Unlike traditional fiat currencies (like the US Dollar or Euro) issued by governments, Bitcoin is not controlled by any single entity. Its supply is mathematically capped at 21 million coins, making it a deflationary asset. Bitcoin combines concepts from cryptography, distributed systems, and economics to create a novel form of money.

## Key Concepts of Bitcoin

### 1. Decentralization
The Bitcoin network is maintained by a distributed network of nodes (computers) that collectively validate and record transactions. This eliminates the need for a central bank or clearinghouse, reducing the risk of censorship, single points of failure, and control by any single party.

### 2. Cryptography
Bitcoin uses cryptographic techniques to secure transactions and control the creation of new units. This includes:
- **Public-key cryptography** for creating addresses and authorizing transactions.
- **Hash functions** (SHA-256) for linking blocks in the chain and creating a tamper-evident record.
- **Digital signatures** to prove ownership of funds.

### 3. The Blockchain
The blockchain is the foundational technology of Bitcoin. It is a chronologically ordered, append-only ledger of all transactions that have ever occurred on the network.

```
Block 1 (Genesis) -> Block 2 -> Block 3 -> ... -> Block N
```
Each block contains a list of transactions, a timestamp, and a cryptographic hash of the previous block, creating an immutable chain. Altering a single block would require recalculating all subsequent blocks, which is computationally infeasible.

### 4. Mining and Consensus (Proof-of-Work)
New bitcoins are created and transactions are confirmed through a process called **mining**. Miners compete to solve a complex cryptographic puzzle (Proof-of-Work). The first miner to solve the puzzle gets to add the next block to the blockchain and is rewarded with newly minted bitcoins (the **block reward**) and transaction fees.

This process secures the network because altering the blockchain would require an attacker to control more than 50% of the total mining power (a **51% attack**), which is extremely costly and difficult.

### 5. Wallets
A Bitcoin wallet is a software application or hardware device that stores the cryptographic keys needed to interact with the Bitcoin network. It does not "store" bitcoins themselves; rather, it holds the private keys that prove ownership of the bitcoins recorded on the blockchain. Wallets generate addresses, which are hashed versions of public keys, to which funds can be sent.

## Bitcoin Transactions

### Transaction Lifecycle
1.  **Creation:** A user initiates a transaction by specifying a recipient's address and an amount to send using their wallet software.
2.  **Signing:** The wallet software signs the transaction with the user's private key, cryptographically proving they own the funds being spent.
3.  **Broadcasting:** The signed transaction is broadcast to the peer-to-peer Bitcoin network.
4.  **Validation:** Network nodes (miners and full nodes) verify the transaction's validity (checking signatures, ensuring no double-spending, etc.).
5.  **Mining:** Valid transactions are gathered by miners into a candidate block. Miners then perform Proof-of-Work to find a valid hash for this block.
6.  **Confirmation:** Once a miner finds a valid block, it is broadcast to the network. Other nodes verify the block and add it to their copy of the blockchain. The transaction is now considered to have one confirmation. With each subsequent block added, the number of confirmations increases, making the transaction more secure and irreversible.

### Transaction Structure
A transaction is fundamentally a set of inputs and outputs.

*   **Inputs:** References to previous transaction outputs (UTXOs - Unspent Transaction Outputs) that prove the sender has the funds. Inputs contain a signature (unlocking script).
*   **Outputs:** Instructions that assign ownership of bitcoins to new addresses. Outputs contain a condition (locking script) that must be met to spend them in the future.

A simple transaction transferring value from Alice to Bob can be visualized as:

```
Transaction #1234
├── Input(s)
│   └── Refers to Output #1 of Transaction #567 (Alice's source of funds)
├── Output(s)
│   ├── Output #1: 0.4 BTC to Bob's Address (Locking Script: <Bob's Public Key Hash>)
│   └── Output #2: 0.1 BTC back to Alice's Address (Change)
└── Witness Data: Alice's digital signature
```

### Types of Transactions
The most common transaction type since a upgrade called SegWit (Segregated Witness) is the **Pay-to-Witness-Public-Key-Hash (P2WPKH)**. Historically, **Pay-to-Public-Key-Hash (P2PKH)** was standard. Other types include multi-signature transactions (requiring multiple keys to authorize spending) and Pay-to-Script-Hash (P2SH).

## Bitcoin Block Structure

A block is a container data structure that aggregates transactions. The key components are:

1.  **Block Header:** An 80-byte segment containing the block's metadata.
    *   **Version:** The block version number.
    *   **Previous Block Hash:** A 256-bit hash pointing to the previous block, linking them together.
    *   **Merkle Root:** A hash of all the transactions in the block, providing a single fingerprint for the entire set.
    *   **Timestamp:** The current time as seconds since 1970-01-01T00:00 UTC.
    *   **Difficulty Target:** The Proof-of-Work difficulty target this block's hash must meet.
    *   **Nonce:** A 4-byte field that miners change to try and achieve a valid block hash.

2.  **Transaction Counter:** A number indicating how many transactions follow.
3.  **Transactions:** The list of all transactions included in this block.

The process of creating a Merkle Root from transactions is shown below:

```
                    Merkle Root (Hash)
                           |
                    +------+------+
                    |             |
            Hash(0+1)        Hash(2+3)
            /       \        /       \
       Hash(0)     Hash(1) Hash(2)   Hash(3)
          |          |       |         |
       Tx Hash 0  Tx Hash 1 Tx Hash 2 Tx Hash 3
```

## The Genesis Block

The **Genesis Block**, or Block 0, is the very first block in the Bitcoin blockchain. It was mined by Satoshi Nakamoto on January 3, 2009. It is hardcoded into the Bitcoin software. Unlike subsequent blocks, it does not reference a previous block. A famous note was embedded in its coinbase transaction: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks," highlighting Bitcoin's purpose as an alternative to the traditional financial system.

## The Bitcoin Network

The Bitcoin network is a peer-to-peer (P2P) network where all participants (nodes) are equal. There are two main types of nodes:

*   **Full Nodes:** These download and validate every block and transaction. They enforce the consensus rules of the network independently. Full nodes store the entire blockchain and are crucial for Bitcoin's security and decentralization.
*   **SPV (Simplified Payment Verification) Nodes/Light Clients:** These only download block headers, not the full transaction history. They rely on full nodes to verify transactions, making them less secure but more lightweight (e.g., mobile wallets).

Nodes discover each other using a DNS seed system and then communicate by relaying transactions and blocks using the **Gossip protocol**, where information is flooded throughout the network.

## Wallets

A wallet manages keys and addresses. They come in various forms with different trade-offs between security and convenience.

| Wallet Type | Description | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Hardware** | Physical device (e.g., Ledger, Trezor) | Excellent security (keys never leave device) | Cost, less convenient for frequent use |
| **Software (Desktop/Mobile)** | App on a computer or phone | Good balance of convenience and control | Device must be secure from malware |
| **Web/Custodial** | Hosted by an exchange (e.g., Coinbase) | Very easy to use, user doesn't manage keys | You trust a third party (counterparty risk) |
| **Paper** | Keys printed on paper | Cold storage, immune to online attacks | Physical vulnerability, hard to use for spending |

Wallets can also be categorized by their connection to the internet:
*   **Hot Wallet:** Connected to the internet (e.g., software, web wallets). Convenient but more vulnerable.
*   **Cold Wallet:** Offline storage (e.g., hardware, paper wallets). Highly secure for long-term storage ("cold storage").

## Smart Contracts Basics and Oracles

While often associated with platforms like Ethereum, Bitcoin has a limited but powerful smart contract capability through its **scripting language**. This language is used in locking scripts to set conditions for spending an output (e.g., "requires one signature," "requires 3 out of 5 signatures," "requires a secret key"). However, it is not Turing-complete by design, prioritizing security and predictability.

An **Oracle** is a trusted external data source that provides real-world information to a blockchain. While not native to Bitcoin's core protocol, oracles can be integrated to create more complex conditional transactions (e.g., a transaction that only executes if a certain sports team wins, based on data from an oracle). This is a more advanced concept typically explored in other blockchain ecosystems.

## Exam Tips

*   **Focus on Core Definitions:** Be able to clearly define Bitcoin, blockchain, mining, and decentralization in your own words.
*   **Understand the Flow:** Memorize the transaction lifecycle from creation to confirmation. Draw the diagram.
*   **Contrast and Compare:** Be prepared to explain the differences between traditional finance and Bitcoin (centralized vs. decentralized, immutable vs. mutable ledger).
*   **Know the Structures:** Understand the components of a transaction (inputs/outputs/UTXO) and a block header. The Merkle Root is a frequently tested concept for its role in efficient verification.
*   **Mining Mechanics:** Explain Proof-of-Work, its purpose (security and issuance), and the incentives for miners (block reward + fees).
*   **Wallet Wisdom:** Be able to discuss the different types of wallets and their security trade-offs. Remember: wallets hold keys, not coins.
*   **Genesis Block:** Remember its significance as the first block and the message embedded within it.