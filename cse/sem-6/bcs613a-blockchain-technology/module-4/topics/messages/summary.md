# Messages

Summary

- Messages are data packets sent from one entity to another on the Ethereum blockchain.
- Messages have a structure consisting of sender, recipient, value, data, and gas fields.
- There are two primary types of messages: transaction messages and call messages.
- Message call transactions involve sending a message to a smart contract, which executes the code associated with the recipient contract.

### Important Formulas, Definitions, and Theorems

- Message structure: {sender, recipient, value, data, gas}
- Transaction message: a message that sends Ether (ETH) from one account to another.
- Call message: a message that invokes a function on a smart contract.

### Key Points

- Messages are a fundamental concept in Ethereum that enables communication between smart contracts and other entities.
- Gas is a critical component of messages, as it determines the execution costs of the message.
- Message call transactions are executed by the EVM, which executes the code associated with the recipient contract.
- The `eth_sendTransaction` method is used to send messages to smart contracts.

### Revision Tips

1. Review the structure of a message and the different types of messages.
2. Practice explaining the concept of gas and its role in message execution.
3. Study examples of sending messages to smart contracts using the `eth_sendTransaction` method.
4. Focus on understanding how message call transactions work and how they are executed by the EVM.
