# Free Space Management

## Purpose

Track which disk blocks are free and available for allocation.

## Methods

### 1. Bit Vector (Bitmap)

Each block represented by 1 bit: 0=free, 1=allocated.

```
Block: 0 1 2 3 4 5 6 7 8 9
Bitmap: 1 1 1 0 0 1 1 0 0 0
 ↑allocated ↑free
```

**Advantages**:

- Simple and efficient
- Easy to find first free block
- Easy to find n contiguous blocks

**Disadvantages**:

- Bitmap can be large for big disks
- Must keep in memory for efficiency

**Size**: disk_size / (8 × block_size) bytes

### 2. Linked List

Free blocks linked together.

```
Free list head → Block 3 → Block 4 → Block 7 → ...
```

**Advantages**:

- No space waste (use free blocks themselves)

**Disadvantages**:

- Cannot easily get contiguous blocks
- Traversal required for allocation

### 3. Grouping

First free block stores addresses of n free blocks. Last of these points to another such block.

```
Block[0]: [1, 4, 7, 9, 12, ptr to Block[15]]
Block[15]: [16, 18, 20, 22, 25, ptr to Block[30]]
```

### 4. Counting

Store (start_block, count) pairs for runs of free blocks.

```
(3, 2) → blocks 3, 4 are free
(7, 3) → blocks 7, 8, 9 are free
```

**Advantage**: Efficient when blocks allocated/freed in clusters.

## Comparison

| Method      | Find Free | Contiguous | Space          |
| ----------- | --------- | ---------- | -------------- |
| Bitmap      | O(n) scan | Easy       | Fixed overhead |
| Linked List | O(1)      | Difficult  | No overhead    |
| Grouping    | O(1)      | Medium     | Minimal        |
| Counting    | O(1)      | Easy       | Minimal        |

## Practical Considerations

1. **Bitmap** used by: ext2/3/4, NTFS
2. **Counting** good for SSDs (allocate extents)
3. Keep free-space structure in memory for speed
4. Write to disk periodically (journaling)
