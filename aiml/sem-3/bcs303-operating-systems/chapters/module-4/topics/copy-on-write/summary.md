# Copy-on-Write (CoW) Notes

### Definitions and Notations

- **Copy-on-Write (CoW)**: A technique used in operating systems to reduce the cost of creating multiple copies of a large file.
- **Formula**: `n(COW) = n(W) + O(log n)`
  - `n(COW)` = Number of copies required using CoW
  - `n(W)` = Number of copies required without CoW
  - `O(log n)` = Overhead of creating a copy

### Key Points

- **CoW**: Replaces writes to a file with a write to a copy of the file and a pointer update.
- **Advantages**:
  - Reduces the number of writes required
  - Can improve performance in systems with a large number of writes
- **Disadvantages**:
  - Increases the overhead of creating a copy
  - Can lead to increased memory usage
- **Theorem**: **Thomsen's Theorem**
  - If a system has `n` processes, each writing `w` words to a file, then `n(COW) = n(W) + O(log n)`
  - Proves that CoW is optimal for systems with a large number of writes

### Important Formulas and Equations

- **Time complexity**: `T(COW) = T(W) + O(log n)`
  - `T(COW)` = Time complexity using CoW
  - `T(W)` = Time complexity without CoW
  - `O(log n)` = Overhead of creating a copy
- **Space complexity**: `S(COW) = S(W) + O(n)`
  - `S(COW)` = Space complexity using CoW
  - `S(W)` = Space complexity without CoW
  - `O(n)` = Additional space required for the copy

### Important Concepts

- **File system structure**: CoW is typically used in file systems with a tree-like structure
- **Journaling**: CoW is often used in conjunction with journaling to improve reliability and performance

### Quick Revision Tips

- Understand the basics of CoW and its advantages and disadvantages
- Recall Thomsen's Theorem and its implications
- Be able to calculate the time and space complexity of CoW systems
- Familiarize yourself with file system structures and journaling techniques
