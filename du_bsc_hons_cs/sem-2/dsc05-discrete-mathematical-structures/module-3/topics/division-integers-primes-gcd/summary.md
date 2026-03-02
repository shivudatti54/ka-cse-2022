# Division in Integers, Primes, and GCD - Summary

## Key Definitions and Concepts

- **Division Algorithm**: For integers a and b (b > 0), there exist unique integers q and r such that a = bq + r, where 0 ≤ r < b. Here, a is the dividend, b is the divisor, q is the quotient, and r is the remainder.

- **Prime Number**: A natural number greater than 1 that has no positive divisors other than 1 and itself. Examples: 2, 3, 5, 7, 11, ...

- **Composite Number**: A natural number greater than 1 that is not prime (has divisors other than 1 and itself).

- **Greatest Common Divisor (GCD)**: The largest positive integer that divides both given integers a and b without leaving a remainder. Denoted as gcd(a, b).

- **Coprime (Relatively Prime)**: Two integers are coprime if gcd(a, b) = 1.

## Important Formulas and Theorems

- **Division Algorithm**: a = bq + r, where 0 ≤ r < b

- **Euclidean Algorithm**: gcd(a, b) = gcd(b, a mod b), repeated until b = 0

- **Bézout's Identity**: If d = gcd(a, b), then there exist integers x and y such that ax + by = d

- **Fundamental Theorem of Arithmetic**: Every integer n > 1 can be uniquely expressed as a product of primes (up to order)

## Key Points

1. The Division Algorithm guarantees unique quotient and remainder for any integer division.

2. There are infinitely many prime numbers (Euclid's theorem).

3. The number 1 is neither prime nor composite.

4. The Euclidean algorithm is highly efficient, running in O(log min(a, b)) time.

5. The Extended Euclidean Algorithm computes both gcd(a, b) and the Bézout coefficients x, y.

6. If gcd(a, b) = d, then gcd(a/d, b/d) = 1 (the numbers become coprime after division by d).

7. Prime factorization is unique up to the ordering of factors.

8. GCD has the property: gcd(a, b) = gcd(b, a) = gcd(a, b - qa) for any integer q.

## Common Mistakes to Avoid

- **Forgetting the condition 0 ≤ r < b** when stating the Division Algorithm—this is crucial for uniqueness.

- **Treating 1 as a prime number**—it is not prime by definition (not greater than 1).

- **Not checking base cases** in the Euclidean algorithm—ensure proper handling when b = 0.

- **Incorrect sign handling**—gcd is always non-negative, and gcd(a, 0) = |a|.

## Revision Tips

1. Practice the Euclidean algorithm with at least 5 different pairs of numbers until it becomes automatic.

2. Memorize the proof of Euclid's theorem—it frequently appears in exams.

3. Work backwards from the second-to-last equation when solving Extended Euclidean Algorithm problems.

4. Remember that gcd(0, 0) is undefined, but gcd(a, 0) = |a| for any non-zero a.

5. Review the relationship between GCD and LCM: gcd(a, b) × lcm(a, b) = |a × b|.