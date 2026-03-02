# **Information and Network Security Study Material**

## **Topic: 21102024 1 Annexure-II 2 What is a Hash Function? The Birthday Problem**

### What is a Hash Function?

#### Definition

A hash function is a one-way mathematical function that takes an input, known as a message, and produces a fixed-size output, known as a hash value or digest. The hash function is designed to be deterministic, meaning that the same input will always produce the same output.

#### Characteristics

- **Deterministic**: The same input always produces the same output.
- **Non-invertible**: It is computationally infeasible to determine the original input from the output.
- **Fixed-size output**: The output is always of a fixed size, regardless of the size of the input.
- **Collision-resistant**: It is computationally infeasible to find two different inputs that produce the same output.

#### Example

Suppose we have a hash function `h(x)` that takes a string `x` as input and produces a hash value `h(x)`. If we input the string "hello", the hash function might produce the output "123456". If we input the string "world", the hash function might produce the output "789012". The hash function is deterministic, meaning that "hello" will always produce "123456", and "world" will always produce "789012".

### The Birthday Problem

#### Definition

The Birthday Problem is a probability problem that asks how many people must be in a room before there is a greater than 50% chance that at least two people share the same birthday.

#### Explanation

The Birthday Problem is often used to illustrate the concept of a hash table, where each person's birthday is mapped to a unique hash value. The problem is solved by calculating the probability that at least two people share the same birthday. The solution involves using a mathematical formula to calculate the probability.

#### Formula

Let `n` be the number of people in the room. The probability that at least two people share the same birthday is given by:

```
1 - (1 - (365/n))^(n-1)
```

#### Example

Suppose we have 23 people in the room. The probability that at least two people share the same birthday is:

```
1 - (1 - (365/23))^(23-1)
```

Using a calculator, we find that the probability is approximately 0.507. This means that there is a greater than 50% chance that at least two people share the same birthday.

### Key Concepts

- **Hash function**: A one-way mathematical function that takes an input and produces a fixed-size output.
- **Deterministic**: The same input always produces the same output.
- **Non-invertible**: It is computationally infeasible to determine the original input from the output.
- **Fixed-size output**: The output is always of a fixed size, regardless of the size of the input.
- **Collision-resistant**: It is computationally infeasible to find two different inputs that produce the same output.
- **Birthday Problem**: A probability problem that asks how many people must be in a room before there is a greater than 50% chance that at least two people share the same birthday.

### Conclusion

Hash functions and the Birthday Problem are essential concepts in information and network security. Hash functions are used to map input data to a fixed-size output, while the Birthday Problem is used to illustrate the concept of a hash table. Understanding these concepts is crucial for designing secure systems and protecting against unauthorized access.

### Study Questions

1. What is a hash function, and what are its characteristics?
2. What is the Birthday Problem, and how is it used to illustrate the concept of a hash table?
3. What is the probability that at least two people share the same birthday in a room of 23 people?

### Answers

1. A hash function is a one-way mathematical function that takes an input and produces a fixed-size output. The characteristics of a hash function include being deterministic, non-invertible, having a fixed-size output, and being collision-resistant.
2. The Birthday Problem is a probability problem that asks how many people must be in a room before there is a greater than 50% chance that at least two people share the same birthday. It is used to illustrate the concept of a hash table.
3. The probability that at least two people share the same birthday in a room of 23 people is approximately 0.507.
