# **The Well Ordering Principle – Mathematical Induction**

## **Introduction**

The Well Ordering Principle is a fundamental concept in discrete mathematics that deals with the ordering of natural numbers. It states that every non-empty set of natural numbers has a least element. In this study material, we will explore the Well Ordering Principle and its application through Mathematical Induction.

## **Definition**

The Well Ordering Principle (WOP) is a statement in predicate logic that states:

- ∃x ∈ N (P(x))
- ∀x ∈ N (∀y ∈ N (y < x → P(y) ∨ P(x)))

Translation: There exists a natural number x such that P(x) is true. For all natural numbers y, if y is less than x, then either P(y) is true or P(x) is true.

## **Explanation**

The WOP is a powerful tool for establishing the validity of statements about natural numbers. It allows us to prove that a particular statement is true for all natural numbers by showing that it is true for some natural number and that it remains true for all smaller natural numbers.

## **Mathematical Induction**

Mathematical Induction is a method of proof that uses the Well Ordering Principle to establish the validity of a statement about natural numbers. The process involves two main steps:

1.  **Base Case**: We show that the statement is true for the smallest natural number (usually 1).
2.  **Inductive Step**: We assume that the statement is true for some arbitrary natural number k and show that it is true for k+1.

## **Key Concepts**

- **Well-Ordering Principle (WOP)**: Every non-empty set of natural numbers has a least element.
- **Mathematical Induction**: A method of proof that uses the WOP to establish the validity of a statement about natural numbers.
- **Base Case**: The smallest natural number for which we want to prove the statement is true.
- **Inductive Step**: The step where we assume the statement is true for some natural number k and show it is true for k+1.

## **Examples**

### Example 1: Proving the statement "n^2 is even for all natural numbers n"

- **Base Case**: n = 1: 1^2 = 1, which is odd. However, we cannot use this as our base case because the statement is false. Let's try n = 2: 2^2 = 4, which is even.
- **Base Case**: n = 2: 2^2 = 4, which is even.
- **Inductive Step**: Assume the statement is true for some arbitrary natural number k: k^2 is even. We want to show that (k+1)^2 is even.
  - (k+1)^2 = k^2 + 2k + 1
  - Since k^2 is even, 2k is even, and 1 is odd. Therefore, (k+1)^2 is even.

### Example 2: Proving the statement "n is even if and only if n/2 is an integer for all natural numbers n"

- **Base Case**: n = 1: 1 is odd, and 1/2 is not an integer. However, we cannot use this as our base case because the statement is false. Let's try n = 2: 2 is even, and 2/2 = 1, which is an integer.
- **Base Case**: n = 2: 2 is even, and 2/2 = 1, which is an integer.
- **Inductive Step**: Assume the statement is true for some arbitrary natural number k: k is even if and only if k/2 is an integer. We want to show that (k+1) is even if and only if (k+1)/2 is an integer.
  - Assume k is even: k = 2m for some natural number m.
  - Then (k+1) = 2m + 1, which is odd.
  - Assume k is odd: k = 2m+1 for some natural number m.
  - Then (k+1) = 2m+2, which is even.
  - Therefore, (k+1) is even if and only if (k+1)/2 is an integer.

## **Conclusion**

The Well Ordering Principle is a fundamental concept in discrete mathematics that deals with the ordering of natural numbers. It states that every non-empty set of natural numbers has a least element. Mathematical Induction is a method of proof that uses the Well Ordering Principle to establish the validity of a statement about natural numbers. By applying the Well Ordering Principle and Mathematical Induction, we can prove a wide range of statements about natural numbers.
