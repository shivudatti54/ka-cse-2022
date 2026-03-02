# Summary: Iterator Pattern in Java Collections

## Core Concepts

### Iterator Interface
The `Iterator<E>` interface provides a unified mechanism to traverse collection elements without exposing internal structure. It maintains cursor position and supports element removal during iteration.

### Interface Methods
- **`hasNext()`**: Returns boolean indicating whether more elements exist
- **`next()`**: Returns next element and advances cursor; throws `NoSuchElementException` if exhausted
- **`remove()`**: Removes last element returned by `next()`; optional operation

### Iterable Interface
`Iterable<T>` is the root interface requiring `iterator()` method. All Collection implementations implement `Iterable`, enabling the enhanced for-loop syntax.

## Iterator vs. Alternative Approaches

| Approach | Modification During Iteration | Use Case |
|----------|-------------------------------|----------|
| Traditional for-loop | Direct removal possible | Index-based operations |
| Enhanced for-loop | Not supported | Read-only traversal |
| Iterator | Supported via `remove()` | Safe modification |
| ListIterator | Add, set, remove supported | Complex List manipulation |

## Fail-Fast Behavior

Java iterators implement **fail-fast** semantics:
- Throw `ConcurrentModificationException` on detecting concurrent modification
- Not guaranteed, but designed to fail immediately
- Works by comparing `modCount` (actual modifications) with `expectedModCount` (iterator creation count)

**Important**: Fail-fast behavior is not a reliability guarantee but a best-effort detection mechanism.

## ListIterator Extensions

For `List` implementations, `ListIterator` provides:
- Bidirectional navigation (`hasPrevious()`, `previous()`)
- Element modification (`set(E e)`)
- Element insertion (`add(E e)`)
- Index tracking (`nextIndex()`, `previousIndex()`)

## Legacy Comparison

`Enumeration` (JDK 1.0) vs. `Iterator` (JDK 1.2):
- Iterator supports element removal
- Iterator has shorter, more readable method names
- Iterator is the modern standard

## Design Pattern Significance

The Iterator pattern exemplifies:
- **Encapsulation**: Hides internal collection structure
- **Polymorphism**: Uniform traversal interface
- **Single Responsibility**: Separates traversal from storage
- **Dependency Inversion**: Depends on abstract `Iterable`, not concrete collections

## Key Takeaways for Exams

1. Always use `iterator.remove()` for safe removal during iteration
2. Check `hasNext()` before calling `next()` to avoid exceptions
3. Enhanced for-loop uses iterators internally
4. Fail-fast iterators throw `ConcurrentModificationException`
5. `ListIterator` is specific to `List` implementations
6. `Iterator` is unidirectional; `ListIterator` is bidirectional