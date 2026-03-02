# **Fundamental Principles of Counting: The Rules of Sum and Product, Permutations, Combinations – The Binomial Theorem, Combinations with Repetition**

## **Introduction**

The study of counting and combinatorics is a fundamental aspect of discrete mathematical structures. This topic explores the basic principles of counting using the rules of sum and product, permutations, combinations, the binomial theorem, and combinations with repetition.

## **The Rules of Sum and Product**

The rules of sum and product are two fundamental principles used to count the number of ways to perform tasks.

- **The Rule of Sum**: The rule of sum states that if there are m ways to perform the first task and n ways to perform the second task, then there are (m + n) ways to perform both tasks. This can be represented mathematically as:
  - | A ∪ B | = | A | + | B | - | A ∩ B |

  where |A ∪ B| is the number of ways to perform both tasks, |A| and |B| are the number of ways to perform the first and second tasks, and |A ∩ B| is the number of ways to perform both tasks simultaneously.

- **The Rule of Product**: The rule of product states that if there are m ways to perform the first task and n ways to perform the second task, then there are m × n ways to perform both tasks. This can be represented mathematically as:
  - | A × B | = | A | × | B |

  where |A × B| is the number of ways to perform both tasks, |A| and |B| are the number of ways to perform the first and second tasks.

## **Permutations**

Permutations refer to the number of ways to arrange objects in a specific order.

### Definition

A permutation is a rearrangement of objects in a specific order. The number of permutations of n objects is represented mathematically as n!.

- **Example**: Find the number of permutations of 3 objects.
  - 3! = 3 × 2 × 1 = 6

  There are 6 ways to arrange 3 objects in a specific order.

## **Combinations**

Combinations refer to the number of ways to choose objects without considering the order.

### Definition

A combination is a selection of objects without considering the order. The number of combinations of n objects taken r at a time is represented mathematically as C(n, r).

- **Example**: Find the number of combinations of 5 objects taken 3 at a time.
  - C(5, 3) = 5! / (3! × (5-3)!)
  - = 5! / (3! × 2!)
  - = (5 × 4 × 3 × 2 × 1) / ((3 × 2 × 1) × (2 × 1))
  - = 10

  There are 10 ways to choose 3 objects from 5 objects without considering the order.

## **The Binomial Theorem**

The binomial theorem is a mathematical formula for expanding expressions of the form (x + y).

### Definition

The binomial theorem states that:

    *   (x + y)^n = ∑[n! / (k!(n-k)!)] × x^(n-k) × y^k

    where n is the exponent, k is the term number, and ∑ represents the sum of the terms.

- **Example**: Expand the expression (x + y)^3.
  - (x + y)^3 = ∑[3! / (k!(3-k)!)] × x^(3-k) × y^k
  - = (3! / (0!(3-0)!)) × x^(3-0) × y^0 + (3! / (1!(3-1)!)) × x^(3-1) × y^1 + (3! / (2!(3-2)!)) × x^(3-2) × y^2
  - = x^3 + 3x^2y + 3xy^2 + y^3

  The expansion of (x + y)^3 is x^3 + 3x^2y + 3xy^2 + y^3.

## **Combinations with Repetition**

Combinations with repetition refer to the number of ways to choose objects with repetition allowed.

### Definition

A combination with repetition is a selection of objects with repetition allowed. The number of combinations with repetition of n objects taken r at a time is represented mathematically as C(n+r-1, r).

- **Example**: Find the number of combinations with repetition of 5 objects taken 3 at a time.
  - C(5+3-1, 3) = C(7, 3)
  - = 7! / (3! × (7-3)!)
  - = (7 × 6 × 5 × 4 × 3 × 2 × 1) / ((3 × 2 × 1) × (4 × 3 × 2 × 1))
  - = 35

  There are 35 ways to choose 3 objects from 5 objects with repetition allowed.
