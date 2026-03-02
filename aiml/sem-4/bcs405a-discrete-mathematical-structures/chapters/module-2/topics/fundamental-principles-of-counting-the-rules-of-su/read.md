# **Fundamental Principles of Counting**

## **The Rules of Sum and Product**

### Definition

The Rules of Sum and Product are two fundamental principles used to count the number of ways to choose items from a set.

### Rules of Sum

- **Rule of Sum**: The number of ways to choose items from two sets is the sum of the number of ways to choose items from each set individually.
  - Let A and B be two sets with |A| = m and |B| = n elements respectively.
  - The number of ways to choose one item from A and one item from B is |A| × |B| = mn.

  - The number of ways to choose an item from A or B is |A| + |B|.

  - Example:
    - A set A contains 3 elements: {1, 2, 3} and a set B contains 2 elements: {a, b}.
    - Number of ways to choose one item from A and one item from B is 3 × 2 = 6.
    - Number of ways to choose an item from A or B is 3 + 2 = 5.

### Rules of Product

- **Rule of Product**: The number of ways to choose items from multiple sets is the product of the number of ways to choose items from each set.
  - Let A, B, and C be three sets with |A| = m, |B| = n, and |C| = p elements respectively.
  - The number of ways to choose one item from each of A, B, and C is |A| × |B| × |C| = mnp.

  - Example:
    - A set A contains 2 elements: {1, 2}, a set B contains 2 elements: {a, b}, and a set C contains 3 elements: {c, d, e}.
    - Number of ways to choose one item from each of A, B, and C is 2 × 2 × 3 = 12.

## **Permutations**

### Definition

A permutation is an arrangement of objects in a specific order.

### Rules of Permutation

- **Rule of Permutation**: The number of ways to arrange n distinct objects is n!.
  - n! = n × (n - 1) × ... × 2 × 1

  - Example:
    - 3 distinct objects: {a, b, c}
    - Number of ways to arrange the objects is 3! = 3 × 2 × 1 = 6.

## **Combinations**

### Definition

A combination is a selection of objects without considering the order.

### Rules of Combination

- **Rule of Combination**: The number of ways to choose k objects from n distinct objects is given by the combination formula.
  - nCk = n! / (k! × (n - k)!)

  - Example:
    - 5 distinct objects: {1, 2, 3, 4, 5} and we want to choose 3 objects.
    - Number of ways to choose 3 objects is 5C3 = 5! / (3! × 2!) = 10.

## **The Binomial Theorem**

### Definition

The Binomial Theorem is a formula to expand expressions of the form (x + y)^n.

### Rules of the Binomial Theorem

- **Binomial Theorem**: (x + y)^n = ∑[n! / (k! × (n - k)!)] × x^k × y^(n - k), where k ranges from 0 to n.
  - Example:
    - (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3.

## **Combinations with Repetition**

### Definition

Combinations with repetition allow for the selection of items where the same item can be selected more than once.

### Rules of Combinations with Repetition

- **Rule of Combinations with Repetition**: The number of ways to choose k items from n distinct items with repetition is given by the combination with repetition formula.
  - nCk = (n + k - 1)! / (k! × (n - 1)!)

  - Example:
    - 5 distinct objects: {1, 2, 3, 4, 5} and we want to choose 3 objects with repetition.
    - Number of ways to choose 3 objects is 5C3 = (5 + 3 - 1)! / (3! × (5 - 1)!) = 35.
