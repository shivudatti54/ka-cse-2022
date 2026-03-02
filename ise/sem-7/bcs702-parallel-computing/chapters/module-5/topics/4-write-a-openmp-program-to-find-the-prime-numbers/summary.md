# **Summary: 4. Write a OpenMP program to find the prime numbers from 1 to n employing parallel for directive**

**Key Points:**

- **Prime Numbers**: A prime number is a positive integer that is divisible only by itself and 1.
- **Sieve of Eratosthenes**: An algorithm to find all prime numbers up to a given number n.
- **OpenMP Program**: To find prime numbers from 1 to n using parallel for directive.

**Important Formulas and Definitions:**

- **Sieve of Eratosthenes**: `n = √(max(n))`, where `max(n)` is the maximum number to check for primality.
- **Prime Number Test**: `if (i % j == 0) then not prime; else prime;` where `i` is the number to check and `j` is the divisor.

**Theorems:**

- **Fermat's Little Theorem**: If `p` is a prime number, then `a^p ≡ a (mod p)` for any integer `a`.
- **Euler's Totient Function**: `φ(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)`, where `p1, p2, ..., pk` are distinct prime factors of `n`.

**OpenMP Program:**

```c
#include <stdio.h>
#include <omp.h>

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    #pragma omp parallel for
    for (int i = 2; i <= n; i++) {
        int isPrime = 1;
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                isPrime = 0;
                break;
            }
        }
        if (isPrime == 1) {
            printf("%d ", i);
        }
    }

    return 0;
}
```

**Revision Notes:**

- Use OpenMP to parallelize the loop to find prime numbers.
- Use the Sieve of Eratosthenes algorithm to find prime numbers up to `n`.
- Use a for loop with parallel for directive to iterate over numbers from 2 to `n`.
- Check if each number is prime by testing divisibility up to its square root.
- Print prime numbers if they are found.
