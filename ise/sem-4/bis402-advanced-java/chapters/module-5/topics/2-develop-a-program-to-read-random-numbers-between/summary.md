**Revision Notes: Developing a Program to Read Random Numbers between a Given Range that are Multiples of 2 and 5**

### Introduction

- The problem requires developing a program that reads random numbers between a given range that are multiples of both 2 and 5.
- The numbers should be integers between the range [lower_bound, upper_bound] (inclusive).

### Mathematical Background

- Multiples of 2 and 5 can be found by applying the least common multiple (LCM) of 2 and 5, which is 10.
- To find all multiples of 10 within a range, we use the formula:
  - Lower bound = (lower_bound / 10) \* 10 (if lower_bound is a multiple of 10)
  - Upper bound = (upper_bound / 10) \* 10 (if upper_bound is a multiple of 10)

### Java Program Requirements

- Use Java's built-in `Random` class to generate random numbers.
- Use a loop to iterate through the range and check if each number is a multiple of 10.
- Store the multiples in an array or list for output.

### Important Formulas and Definitions

- Least Common Multiple (LCM): The smallest positive integer that is a multiple of both numbers.
- Multiples of a number: Integers that can be divided by that number without a remainder.
- Random numbers: Numbers generated using a pseudorandom number generator algorithm.

### Key Points for Revision

- Use the LCM of 2 and 5 (10) to find the multiples of 2 and 5.
- Apply the formula to adjust the range bounds if necessary.
- Iterate through the range and check for multiples of 10.
- Store the multiples in an array or list for output.
- Use Java's `Random` class to generate random numbers.
