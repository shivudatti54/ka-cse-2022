# Segmentation - Summary

## Key Definitions and Concepts

- **Segmentation**: A memory management technique that divides a program's logical address space into variable-sized segments based on logical divisions like code, data, stack, and heap.

- **Segment Table**: A data structure maintained by the operating system for each process, containing base address and limit (size) for each segment, along with access rights.

- **Logical Address**: Composed of a segment number (selector) and an offset within that segment. Used by programs to reference memory locations.

- **Physical Address**: The actual memory address in RAM, calculated by adding the segment base to the offset during address translation.

- **Segmentation Fault**: An error occurring when a program attempts to access memory with an invalid segment number or with an offset exceeding the segment limit.

## Important Formulas and Theorems

- **Address Translation Formula**: Physical Address = Segment Base + Offset

- **Validity Check**: A memory reference is valid if and only if (0 ≤ Offset < Segment Limit)

- **Maximum Segment Size**: Determined by the number of bits allocated for offset in the logical address. With n bits for offset, maximum segment size is 2^n bytes.

## Key Points

- Segmentation provides logical memory organization that matches programmer intuition about program structure.

- Each segment is variable-sized, eliminating internal fragmentation within segments.

- External fragmentation can occur because segments are variable-sized and can be placed anywhere in physical memory.

- Hardware support through segment registers and the Memory Management Unit (MMU) enables fast address translation.

- Protection is implemented through access rights stored in each segment descriptor entry.

- Multiple processes can share segments by pointing their segment table entries to the same physical memory location.

- Combined segmentation with paging provides the benefits of both: logical view from segmentation and efficient physical management from paging.

- Common segment types include code segment (read-only/executable), data segment (read-write), stack segment, and heap segment.

## Common Mistakes to Avoid

- Confusing segment limit with the maximum valid offset. Remember: valid offsets range from 0 to (limit - 1).

- Forgetting to check offset validity before calculating physical address, leading to incorrect answers in address translation problems.

- Confusing segmentation with paging: segmentation uses variable-sized blocks based on logic, while paging uses fixed-sized blocks for physical memory management.

- Misunderstanding that segmentation alone does not provide virtual memory capability; it requires paging for swapping segments in and out of memory.

## Revision Tips

- Practice solving address translation problems with different segment table configurations to master the calculation methodology.

- Create a comparison table between paging and segmentation to understand their differences and trade-offs clearly.

- Remember the key formula Physical Address = Base + Offset and always perform the validity check (Offset < Limit) first.

- Review how x86 architecture implements segmentation in real-world systems to connect theoretical concepts with practical applications.