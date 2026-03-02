# Why Study CAP Theorem?

## Foundation for Distributed Design

The CAP theorem is the **most important concept** for understanding trade-offs in distributed systems. Every distributed database, cache, or storage system is designed with CAP trade-offs in mind.

## Exam Relevance

| Aspect         | Details                                         |
| -------------- | ----------------------------------------------- |
| Frequency      | Asked in almost every exam                      |
| Marks          | 8-15 marks typically                            |
| Question Types | Explain CAP, classify systems, design scenarios |

## Industry Importance

### Database Selection

- Choose between Cassandra (AP) vs MongoDB (CP)
- Understand DynamoDB's consistency options
- Select appropriate database for use case

### System Architecture

- Design services with correct trade-offs
- Handle partition scenarios properly
- Balance latency and consistency

### Interview Essential

- Most common distributed systems question
- Shows understanding of fundamental trade-offs
- Required knowledge for senior positions

## Real-World Relevance

### Every Major Tech Company

- Amazon: DynamoDB is AP
- Google: Spanner is CP
- Netflix: Uses both CP and AP systems
- Facebook: Different systems for different data

### Everyday Applications

- Why your feed shows old posts briefly
- Why payments are slower but accurate
- Why DNS sometimes shows stale IPs

## Connection to Other Topics

Understanding CAP leads to:

- **Consistency Models** - Different levels of consistency
- **Replication Strategies** - How to achieve desired properties
- **Consensus Algorithms** - Achieving CP guarantees
- **Distributed Transactions** - ACID in distributed systems

## Learning Outcomes

After studying this topic, you should be able to:

1. Define CAP theorem and its three properties
2. Explain why CA is impossible
3. Classify systems as CP or AP
4. Apply CAP to real-world scenarios
5. Understand PACELC extension
6. Make design decisions based on CAP trade-offs
