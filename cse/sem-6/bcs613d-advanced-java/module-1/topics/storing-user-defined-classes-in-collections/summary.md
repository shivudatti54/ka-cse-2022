# Storing User-Defined Classes in Collections

## Overview

When storing custom objects in collections, especially hash-based collections like HashSet and HashMap, proper implementation of equals(), hashCode(), and compareTo() methods is essential. These methods ensure correct behavior for containment checks, duplicate detection, and sorting operations.

## Key Points

- **equals() Method**: Defines object equality based on field values, not reference
- **hashCode() Method**: Must return same value for equal objects, used by hash-based collections
- **compareTo() Method**: Defines natural ordering for Comparable interface
- **HashCode Contract**: If equals() returns true, hashCode() must return same value
- **Objects.hash()**: Utility method to generate hashCode from multiple fields
- **Objects.equals()**: Null-safe equality checking utility method
- **Consistent Implementation**: Override both equals() and hashCode() together

## Important Concepts

- HashSet and HashMap rely on hashCode() and equals()
- TreeSet and TreeMap rely on compareTo() or Comparator
- Mutable objects as keys can cause lost entries
- compareTo() should be consistent with equals()
- Integer.compare() for comparing int values in compareTo()

## Notes

- Always override equals() and hashCode() together for hash-based collections
- For TreeSet/TreeMap, implement Comparable or provide Comparator
- Remember: equal objects must have same hashCode, but same hashCode doesn't mean equal
