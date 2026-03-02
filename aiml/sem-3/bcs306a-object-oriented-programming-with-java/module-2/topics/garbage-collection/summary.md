# Garbage Collection in Java - Summary

## Key Definitions and Concepts

- **Garbage Collection**: Automatic memory management process in Java that identifies and reclaims memory occupied by unreachable objects.
- **GC Roots**: Starting points for garbage collection—stack variables, static fields, and JNI references.
- **Reachability**: An object is reachable if it can be accessed through a chain of references from GC roots.
- **Generational GC**: Approach that divides heap into Young Generation (new objects) and Old Generation (long-lived objects).

## Important Formulas and Theorems

- Heap size tuning: `-Xms<size>` (initial) and `-Xmx<size>` (maximum)
- Young generation size: `-Xmn<size>` or `-XX:NewRatio=<ratio>`
- GC algorithm selection: `-XX:+Use<GCType>GC` (e.g., `-XX:+UseG1GC`)

## Key Points

- Objects become eligible for GC when all references to them are nullified or go out of scope.
- Java uses generational garbage collection to optimize collection frequency—most objects die young.
- Four main GC algorithms: Serial (single-threaded), Parallel (throughput), CMS (low-pause), G1 (default modern collector).
- System.gc() is only a suggestion to JVM, not a command—JVM may ignore it.
- The finalize() method is deprecated since Java 9 due to performance issues.
- Memory leaks can still occur in Java through unintended object retention in collections or static references.
- ZGC provides ultra-low latency for large heap applications.
- OutOfMemoryError occurs when heap is exhausted—either due to memory leak or insufficient heap size.

## Common Mistakes to Avoid

1. Assuming System.gc() will immediately free memory—it may be ignored by JVM.
2. Using finalize() for resource cleanup—it's unreliable and deprecated.
3. Believing GC eliminates all memory problems—memory leaks still occur.
4. Setting references to null unnecessarily—objects become eligible naturally when out of scope.

## Revision Tips

1. Practice identifying which objects are eligible for garbage collection in code snippets.
2. Remember the names and characteristics of different garbage collectors.
3. Understand the difference between Minor GC (Young Gen) and Major/Full GC (Old Gen).
4. Review common memory leak scenarios in collections and static references.
5. Know the basic JVM tuning flags for heap size and GC selection.
