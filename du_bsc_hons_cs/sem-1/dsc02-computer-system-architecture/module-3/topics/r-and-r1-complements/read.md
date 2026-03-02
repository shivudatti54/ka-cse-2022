# R and R-1 Complements

## Introduction

In computer system architecture, binary numbers play a crucial role in representing data. Binary numbers are made up of only two digits: 0 and 1. When performing arithmetic operations on binary numbers, it is often necessary to find the complement of a number. There are two types of complements in binary arithmetic: R's complement and (R-1)'s complement. In this topic, we will explore the concept of R and R-1 complements, their importance, and how they are used in binary arithmetic.

The R's complement and (R-1)'s complement are used to represent the negative of a binary number. This is essential in computer arithmetic, as it allows us to perform subtraction and other operations involving negative numbers. Understanding R and R-1 complements is crucial for any student of computer science, as it lays the foundation for more advanced topics in computer system architecture.

## Key Concepts

### R's Complement

The R's complement of a binary number is obtained by flipping all the bits of the number and then adding 1 to the result. In other words, the R's complement of a binary number is obtained by changing all the 0s to 1s and all the 1s to 0s, and then adding 1 to the resulting number.

Mathematically, the R's complement of a binary number can be represented as:

R's complement = (NOT x) + 1

where x is the binary number.

### (R-1)'s Complement

The (R-1)'s complement of a binary number is obtained by flipping all the bits of the number. In other words, the (R-1)'s complement of a binary number is obtained by changing all the 0s to 1s and all the 1s to 0s.

Mathematically, the (R-1)'s complement of a binary number can be represented as:

(R-1)'s complement = NOT x

where x is the binary number.

## Examples

### Example 1: Finding the R's Complement of a Binary Number

Find the R's complement of the binary number 1010.

Solution:

Step 1: Flip all the bits of the number.

1010 -> 0101

Step 2: Add 1 to the result.

0101 + 1 = 0110

Therefore, the R's complement of 1010 is 0110.

### Example 2: Finding the (R-1)'s Complement of a Binary Number

Find the (R-1)'s complement of the binary number 1101.

Solution:

Step 1: Flip all the bits of the number.

1101 -> 0010

Therefore, the (R-1)'s complement of 1101 is 0010.

### Example 3: Using R's Complement for Subtraction

Subtract 1010 from 1111 using R's complement.

Solution:

Step 1: Find the R's complement of 1010.

1010 -> 0101 + 1 = 0110 (R's complement)

Step 2: Add the R's complement to 1111.

1111 + 0110 = 10101

Step 3: Remove the carry.

10101 -> 0101

Therefore, the result of subtracting 1010 from 1111 is 0101.

## Exam Tips

1. Understand the difference between R's complement and (R-1)'s complement.
2. Know how to find the R's complement and (R-1)'s complement of a binary number.
3. Practice using R's complement for subtraction.
4. Be able to identify when to use R's complement and when to use (R-1)'s complement.
5. Understand the importance of R's complement and (R-1)'s complement in computer arithmetic.
6. Be able to explain the mathematical representation of R's complement and (R-1)'s complement.
7. Practice solving problems involving R's complement and (R-1)'s complement.