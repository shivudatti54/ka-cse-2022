# Module 4: Currency (ETH and ETC)

## 1. Introduction

In the realm of blockchain, a "currency" or "cryptocurrency" is more than just digital money. It is a fundamental utility token that powers and secures its native network. This module focuses on the two primary cryptocurrencies associated with the Ethereum platform: **Ether (ETH)** on the Ethereum Mainnet and **Ether Classic (ETC)** on the Ethereum Classic chain. Their existence is a direct result of a pivotal philosophical schism in the blockchain community, making their study crucial for understanding both technical and governance aspects of decentralized systems.

## 2. Core Concepts

### Ether (ETH) - The Fuel of Ethereum Mainnet

Ether (ETH) is the native cryptocurrency of the Ethereum blockchain. Its roles are multifaceted:

*   **Fuel for Operations (Gas):** Every computation, transaction, or smart contract execution on the Ethereum network requires computational resources. To prevent spam and allocate resources fairly, these operations cost "gas." ETH is used to pay for this gas. The more complex the operation (e.g., deploying a smart contract vs. a simple transfer), the more gas is required, and consequently, the more ETH must be paid.
    *   **Example:** If Alice wants to send 1 ETH to Bob, she might pay a gas fee of 0.001 ETH. If she wants to interact with a complex DeFi smart contract, the gas fee could be 0.01 ETH.

*   **Store of Value and Medium of Exchange:** Beyond its utility function, ETH is a digital asset held for investment and used as a currency for goods and services within the crypto ecosystem.

*   **Network Security (Proof-of-Stake):** Since "The Merge" in September 2022, Ethereum transitioned from Proof-of-Work (PoW) to Proof-of-Stake (PoS). In PoS, validators are required to "stake" a minimum of 32 ETH to participate in validating transactions and creating new blocks. This staked ETH acts as a security deposit; validators who act maliciously have their stake "slashed" (partially destroyed). This mechanism secures the network and incentivizes honest participation.

### The DAO Hack and The Fork: The Birth of ETC

To understand Ether Classic (ETC), one must understand "The DAO" event in 2016.

*   **The DAO:** A Decentralized Autonomous Organization (DAO) was a complex smart contract designed to operate as a venture capital fund. It raised over $150 million worth of ETH.
*   **The Exploit:** A hacker exploited a vulnerability in The DAO's code and drained approximately 3.6 million ETH (a third of the total raised) into a child contract.
*   **The Dilemma:** The community faced a critical decision:
    1.  **Do nothing:** Accept the hack as the immutable, albeit unfortunate, outcome of deploying faulty code—a core principle of "code is law."
    2.  **Intervene:** Execute a "hard fork" to rewrite the blockchain's history, moving the stolen funds to a new contract so investors could recover them.

### Ether Classic (ETC) - The Original Chain Persists

The Ethereum community voted to execute the hard fork, creating the new history we now know as the **Ethereum Mainnet (ETH)**. However, a significant minority rejected this intervention, believing it violated the principle of immutability. They continued mining the original, unaltered blockchain, which was renamed **Ethereum Classic**.

*   **Ether Classic (ETC)** is the native currency of this original, unforked chain.
*   **Philosophy:** The ETC network upholds the principle that "code is law" and that blockchain transactions should be immutable and censorship-resistant, regardless of outcomes.
*   **Technical Difference:** A key technical distinction is that Ethereum Classic has **remained on Proof-of-Work (PoW)**, using miners (not stakers) to secure its network. This makes its consensus mechanism identical to Bitcoin's.

### ETH vs. ETC: A Comparative Summary

| Feature | **Ether (ETH)** | **Ether Classic (ETC)** |
| :--- | :--- | :--- |
| **Blockchain** | Ethereum Mainnet (Post-Fork) | Ethereum Classic (Original Chain) |
| **Core Philosophy** | Pragmatism; community governance can intervene in extreme cases. | Idealism; "Code is Law" – absolute immutability. |
| **Consensus Mechanism** | **Proof-of-Stake (PoS)** since 2022. | **Proof-of-Work (PoW)**. |
| **Primary Function** | Gas for a vast ecosystem of dApps, DeFi, and NFTs. | Digital cash and commodity for a smaller ecosystem; upholds original Ethereum vision. |
| **Market & Ecosystem** | The second-largest cryptocurrency by market cap; massive developer activity. | Significantly smaller market cap and ecosystem. |

## 3. Key Points & Summary

*   **ETH** is the currency of the forked Ethereum Mainnet, used primarily for **paying gas fees** and **staking** to secure the network under its **Proof-of-Stake** consensus.
*   **ETC** is the currency of the original, unforked Ethereum Classic chain, maintained by a community that prioritizes **immutability ("code is law")** and continues to use **Proof-of-Work**.
*   The split between ETH and ETC was not a technical failure but a **philosophical disagreement** on governance and immutability, triggered by The DAO hack in 2016.
*   The key technical difference today is the **consensus algorithm**: PoS for ETH and PoW for ETC.
*   For an engineer, this case study is vital for understanding the real-world implications of blockchain governance, hard forks, and the trade-offs between immutability and pragmatism.