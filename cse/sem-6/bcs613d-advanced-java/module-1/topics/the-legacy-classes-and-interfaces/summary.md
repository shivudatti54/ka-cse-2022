# Legacy Classes and Interfaces

## Overview

Legacy classes (Vector, Stack, Hashtable, Properties, Dictionary) and the Enumeration interface existed before the Java Collections Framework was introduced in Java 1.2. While still supported for backward compatibility, these classes are largely superseded by modern collection classes but remain important for maintaining older code.

## Key Points

- **Vector**: Synchronized version of ArrayList, thread-safe but slower due to synchronization overhead
- **Stack**: Extends Vector to provide LIFO stack operations (push, pop, peek)
- **Hashtable**: Synchronized Map implementation that doesn't allow null keys or values
- **Properties**: Extends Hashtable for managing configuration properties with string key-value pairs
- **Enumeration Interface**: Predecessor to Iterator for traversing collections
- **Dictionary**: Abstract class that was parent of Hashtable, now obsolete
- **Migration Path**: Convert Vector to ArrayList, Hashtable to HashMap, Stack to ArrayDeque for better performance

## Important Concepts

- All legacy classes are synchronized (thread-safe)
- Modern alternatives are faster but not thread-safe by default
- Enumeration has hasMoreElements() and nextElement() methods
- Iterator replaced Enumeration with additional remove() capability
- Properties class still commonly used for configuration files

## Notes

- In exams, remember Vector and Hashtable are synchronized while ArrayList and HashMap are not
- Know that Hashtable doesn't allow null keys/values while HashMap does
- Legacy classes still valid for simple thread-safety requirements
