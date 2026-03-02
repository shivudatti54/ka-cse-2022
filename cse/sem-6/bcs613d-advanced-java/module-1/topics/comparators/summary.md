# Comparators in Java - Summary

## Key Definitions

- **Comparator<T>**: A functional interface in java.util that defines a custom ordering for objects of type T, independent of the objects themselves.
- **compare(T o1, T o2)**: The primary method of Comparator that returns negative, zero, or positive based on the ordering of o1 relative to o2.
- **Comparable**: An interface that defines the natural ordering of a class (implemented by the class itself).
- **Functional Interface**: An interface with a single abstract method that can be implemented using lambda expressions.

## Important Formulas

- **Return value convention**: compare(o1, o2) returns:
  - Negative integer → o1 comes before o2
  - Zero → o1 equals o2
  - Positive integer → o1 comes after o2

- **Integer comparison**: Use Integer.compare(a, b) instead of a - b to avoid overflow

- **Comparator chaining**: result = primary.thenComparing(secondary).thenComparing(tertiary)

## Key Points

1. Comparator provides external control over sorting without modifying the source class
2. Comparator is defined in java.util package, while Comparable is in java.lang
3. Multiple Comparator implementations can provide different sort orders for the same class
4. Comparator is a functional interface (single abstract method: compare)
5. TreeSet and TreeMap require either Comparable or Comparator for element ordering
6. Java 8 added powerful default methods: reversed(), thenComparing()
7. Static factory methods: comparing(), nullsFirst(), nullsLast(), naturalOrder(), reverseOrder()
8. Collections.sort() and Arrays.sort() are stable sorts (maintain relative order of equal elements)
9. Comparator nullsFirst()/nullsLast() handle null values gracefully
10. Comparator can be used with parallelSort() for multi-threaded sorting of large arrays

## Common Mistakes

1. **Confusing return value sign**: Remember negative means first argument comes first, not that it's "less than" in the mathematical sense
2. **Using subtraction for comparison**: a - b can cause integer overflow; use Integer.compare() instead
3. **Forgetting to provide Comparator for TreeSet/TreeMap**: Results in ClassCastException if elements don't implement Comparable
4. **NullPointerException**: Forgetting to handle null values when sorting collections that may contain nulls
5. **Modifying original class unnecessarily**: Using Comparable when a separate Comparator would be more appropriate