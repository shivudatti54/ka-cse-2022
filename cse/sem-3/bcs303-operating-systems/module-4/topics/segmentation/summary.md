# Segmentation - Summary

## Key Definitions

- **Segmentation**: A memory management technique that divides a program's address space into variable-sized logical units called segments based on the program's logical structure.

- **Segment**: A logical unit of memory representing a meaningful collection of information such as code, data, stack, or heap.

- **Segment Table**: A data structure maintained by the OS that maps segment numbers to physical base addresses and contains limit/protection information.

- **Logical Address**: An address expressed as a (segment number, offset) pair that refers to a location within a specific segment.

- **Physical Address**: The actual memory address in RAM where data is stored.

- **Segmentation Fault**: An exception generated when a program accesses memory outside its allocated segments or violates segment protection.

- **Segment Table Entry (STE)**: Contains base address, limit (size), valid bit, and protection bits for a segment.

## Important Formulas

- **Physical Address Calculation**: `Physical Address = Segment Base + Offset`

- **Address Translation Validity Check**: `Valid if 0 ≤ Offset < Segment Limit`

- **Logical Address Structure**: `[Segment Number (s)] [Offset (d)]`

- **Maximum Segments**: If segment field has n bits, maximum segments = 2^n

## Key Points

1. Segmentation divides memory into variable-sized segments based on logical program structure, unlike fixed-size pages in paging.

2. Each segment has its own base address (starting physical location) and limit (size), enabling independent management of different program components.

3. The segment table maps logical segment numbers to physical addresses and stores protection information for each segment.

4. Address translation validates that the offset is within the segment limit before computing the physical address as base + offset.

5. Segmentation provides natural code sharing (read-only code segments can be mapped to same physical memory by multiple processes).

6. Segmentation eliminates internal fragmentation but may suffer from external fragmentation due to variable-sized segments.

7. Modern architectures (like x86) often combine segmentation with paging to get benefits of both: logical structure and efficient physical memory management.

8. Protection is enforced at segment level with read, write, and execute permissions stored in each segment table entry.

9. Context switching requires saving and restoring the entire segment table, adding overhead compared to simpler schemes.

10. Segmentation faults occur when programs access invalid memory addresses or violate segment access permissions.

## Common Mistakes

1. **Confusing segment base with physical address**: The base is the starting address of the segment in physical memory, not the final address.

2. **Forgetting limit checking**: Students often compute physical address without verifying that offset < limit, leading to incorrect results or missing security violations.

3. **Mixing up segmentation and paging**: Segmentation uses variable-sized segments while paging uses fixed-size pages; these are fundamentally different approaches.

4. **Ignoring protection bits**: The segment table stores access rights that must be checked before allowing memory operations.

5. **Incorrect segment number indexing**: The segment number directly indexes into the segment table; no division or scaling is needed (unlike page table lookup).