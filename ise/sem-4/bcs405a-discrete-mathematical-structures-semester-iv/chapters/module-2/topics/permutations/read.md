# Permutations and Combinations

## Permutations (Order Matters)

### Basic Permutation

Arrange r items from n items:

```
P(n,r) = n!/(n-r)!
```

**Example:** 3 people in 5 chairs = P(5,3) = 5!/2! = 60

### Permutations with Repetition

n items where item i repeats n_i times:

```
n! / (n₁! × n₂! × ... × nₖ!)
```

**Example:** Arrange "MISSISSIPPI"
= 11! / (4! × 4! × 2!) = 34,650

### Circular Permutation

Arrange n items in circle:

```
(n-1)!
```

**Example:** 6 people at round table = 5! = 120

## Combinations (Order Doesn't Matter)

### Basic Combination

Choose r items from n:

```
C(n,r) = n! / (r! × (n-r)!)
```

**Example:** Choose 3 from 5 = C(5,3) = 10

### Properties

1. C(n,r) = C(n, n-r)
2. C(n,0) = C(n,n) = 1
3. C(n,r) + C(n,r+1) = C(n+1,r+1) (Pascal's Identity)

## Stars and Bars

Distribute n identical items into r distinct bins:

```
C(n+r-1, r-1)
```

**Example:** 10 candies to 3 kids = C(12,2) = 66 ways
