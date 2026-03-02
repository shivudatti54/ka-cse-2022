# Gas

## Introduction

In the Ethereum blockchain, gas is a fundamental concept that plays a crucial role in the execution of transactions and smart contracts. In this topic, we will delve into the concept of gas, its significance, and how it is used in the Ethereum ecosystem.

## What is Gas?

Gas is a unit of measurement that represents the amount of computational effort required to execute a transaction or a smart contract on the Ethereum blockchain. It is a way to quantify the amount of work that needs to be done to validate a transaction or execute a contract.

## Why is Gas Needed?

Gas is needed to prevent denial-of-service (DoS) attacks on the Ethereum network. Without gas, an attacker could create a contract that consumes an excessive amount of computational resources, effectively bringing the network to a halt. By requiring gas for every transaction and contract execution, the network can prevent such attacks and ensure that the system remains stable.

## How Does Gas Work?

When a user sends a transaction or deploys a smart contract, they need to specify the amount of gas they are willing to pay for its execution. The gas is then used to execute the transaction or contract, and any remaining gas is refunded to the user.

## Gas Price

The gas price is the amount of Ether (ETH) that a user is willing to pay for each unit of gas. The gas price is set by the user, and it determines the priority of the transaction or contract execution. A higher gas price means that the transaction or contract will be executed faster, while a lower gas price means it may take longer.

## Gas Limit

The gas limit is the maximum amount of gas that a user is willing to spend on a transaction or contract execution. If the gas limit is reached, the transaction or contract execution will fail, and any remaining gas will be refunded to the user.

## Gas in Smart Contracts

In smart contracts, gas is used to execute the contract's code. The contract's author specifies the gas limit and gas price for the contract's execution. If the contract's execution exceeds the gas limit, the contract will fail, and any remaining gas will be refunded to the user.

## Example

Suppose a user wants to send a transaction to a smart contract that requires 100 units of gas to execute. The user sets the gas price to 20 Gwei (a unit of Ether) and the gas limit to 1000 units. If the contract's execution requires only 50 units of gas, the user will be refunded 950 units of gas (1000 - 50).

## Exam Tips

1. Understand the concept of gas and its significance in the Ethereum blockchain.
2. Know how gas is used to prevent denial-of-service (DoS) attacks.
3. Be able to explain how gas works, including gas price and gas limit.
4. Understand how gas is used in smart contracts.
5. Be able to calculate gas costs for transactions and contract executions.
6. Know the units of measurement for gas, including Gwei.
