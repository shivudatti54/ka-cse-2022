# Counting Principles

## Sum Rule (Addition Principle)

If task A can be done in m ways and task B in n ways, and they cannot be done simultaneously:

- Total ways = m + n

**Example:** Choose a book from 5 fiction OR 3 non-fiction = 5 + 3 = 8 ways

## Product Rule (Multiplication Principle)

If task A can be done in m ways and task B in n ways, and both must be done:

- Total ways = m × n

**Example:** 3 shirts and 4 pants = 3 × 4 = 12 outfits

## Inclusion-Exclusion Principle

For two sets A and B:

```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

For three sets:

```
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |B ∩ C| - |A ∩ C| + |A ∩ B ∩ C|
```

## Pigeonhole Principle

If n items are placed in m containers where n > m, at least one container has more than one item.

**Generalized:** If n items in m containers, at least one container has ⌈n/m⌉ items.

**Examples:**

1. 13 people → at least 2 share birthday month
2. 5 cards from deck → at least 2 same suit

## Division Rule

If outcome can be achieved in n ways, but each distinct outcome counted k times:

- Distinct outcomes = n/k

**Example:** Arrange 3 people in circle = 3!/3 = 2 ways (divide by rotations)
