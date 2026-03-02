# Segmentation


## Table of Contents

- [Segmentation](#segmentation)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Segment Definition and Structure](#segment-definition-and-structure)
  - [Address Translation in Segmentation](#address-translation-in-segmentation)
  - [Segment Table and Descriptor Format](#segment-table-and-descriptor-format)
  - [Segmentation with Paging](#segmentation-with-paging)
  - [Segment Protection and Access Rights](#segment-protection-and-access-rights)
  - [Segment Sharing](#segment-sharing)
- [Examples](#examples)
  - [Example 1: Simple Segment Address Translation](#example-1-simple-segment-address-translation)
  - [Example 2: Segmentation Fault Detection](#example-2-segmentation-fault-detection)
  - [Example 3: Segment Sharing Between Processes](#example-3-segment-sharing-between-processes)
- [Exam Tips](#exam-tips)

## Introduction

Segmentation is a memory management technique that divides a program's address space into variable-sized logical units called segments. Unlike paging, which divides memory into fixed-sized blocks, segmentation reflects the natural division of a program into logically meaningful units such as code, data, stack, heap, and shared libraries. Each segment represents a logical entity with a specific purpose and size, making it easier for programmers to think about memory organization in terms of program structure rather than physical memory addresses.

The fundamental principle behind segmentation is that different parts of a program have different characteristics and access patterns. The code segment contains executable instructions and is typically read-only and shared across multiple processes. The data segment stores global and static variables, while the heap manages dynamically allocated memory. The stack handles function calls and local variables. By treating these as separate segments, the operating system can provide appropriate protection and manage each segment according to its specific requirements.

Segmentation was introduced to solve several problems associated with earlier memory management schemes. It provides a mechanism for logical memory organization that matches programmer intuition, enables protection by allowing different access rights for different segments, facilitates sharing of common code and data, and allows programs to grow or shrink segments dynamically. Modern operating systems combine segmentation with paging to leverage the benefits of both techniques, resulting in a powerful and flexible memory management system.

## Key Concepts

### Segment Definition and Structure

A segment is a contiguous portion of a program's logical address space with a specific purpose. Each segment is identified by a segment number and has a segment base (starting physical address) and a segment limit (length or size). The operating system maintains a segment table for each process, which stores the base and limit information for all segments belonging to that process. The segment table acts as a mapping between logical segment numbers and physical memory addresses.

When a program references a memory location, the CPU generates a logical address consisting of two parts: a segment selector (segment number) and an offset within that segment. The segment selector identifies which segment is being accessed, and the offset specifies the byte position within that segment. The memory management unit (MMU) uses the segment table to translate this logical address into a physical address by adding the offset to the segment's base address, after checking that the offset is within the segment's limit.

### Address Translation in Segmentation

The address translation process in segmentation involves several steps. First, the CPU extracts the segment number and offset from the logical address. The segment number indexes into the segment table to retrieve the corresponding segment descriptor containing the base address and limit. The MMU then checks whether the offset is less than the limit; if not, a segmentation fault occurs. If the offset is valid, the physical address is calculated by adding the base address to the offset. This physical address is then used to access the actual memory location.

For example, consider a system with 16-bit logical addresses where the segment number occupies 4 bits and the offset occupies 12 bits. This allows for 16 segments, each of which can be up to 4096 bytes (2^12) in size. When the CPU generates logical address 0x3A57 (binary: 0011 101001010111), the segment number is 3 (0x3) and the offset is 0xA57 (2655 decimal). The segment table entry for segment 3 might have base address 0x14000 and limit 0x1000 (4096). Since the offset 2655 is less than the limit 4096, the physical address becomes 0x14000 + 0x0A57 = 0x14A57.

### Segment Table and Descriptor Format

The segment table is an array of segment descriptors stored in memory, with a segment register (or base register in some architectures) pointing to its location. Each descriptor contains several important fields beyond just the base and limit. The base field holds the starting physical address of the segment in memory. The limit field specifies the size of the segment, defining the maximum valid offset. Access rights field indicates the type of access permitted (read, write, execute) for protection purposes.

Modern architectures like x86 support additional descriptor fields. The Present bit indicates whether the segment is currently loaded in memory or has been swapped to disk. The Access bit is set when the segment is accessed, useful for page replacement algorithms. The User/Supervisor bit distinguishes between user mode and kernel mode access. The Granularity bit determines whether the limit is interpreted in bytes or pages (4KB blocks). These fields enable sophisticated memory protection and virtual memory support.

### Segmentation with Paging

Pure segmentation faces challenges with external fragmentation because segments are variable-sized and can leave holes in physical memory when they are loaded, removed, or relocated. To address this limitation, modern systems combine segmentation with paging in a two-level scheme. The logical address is first divided into a segment number and offset, just like pure segmentation. The offset is then divided into a page number and page offset using paging.

This hybrid approach provides the logical benefits of segmentation (logical organization, protection, sharing) while gaining the physical memory management advantages of paging (no external fragmentation, simple memory allocation). The segment table entry points to a page table rather than directly to a physical segment base. This combination is used in x86 architectures where segmentation is mandatory (though often with flat memory models) and in some embedded systems requiring specific memory protection models.

### Segment Protection and Access Rights

Segmentation provides fine-grained protection by allowing different access rights for different segments. A code segment might be marked as read-only and executable, preventing modification of instructions and detecting certain types of bugs. Data segments can be marked as read-write, while segments containing sensitive information can be marked as read-only for certain processes. The hardware checks access rights during every memory reference, ensuring that any violation generates a protection fault.

Operating systems can implement ring-based protection using segmentation, where inner rings have more privileges than outer rings. The x86 architecture supports four privilege levels (rings 0-3), with ring 0 being the most privileged (kernel) and ring 3 being the least privileged (user applications). Segments with higher privilege levels can access segments with lower privilege levels, but not vice versa, preventing user programs from corrupting kernel data structures.

### Segment Sharing

Segments enable efficient sharing of code and data between processes. When multiple processes need to execute the same program, they can share the code segment rather than each having a private copy. The segment table entries for different processes can point to the same physical segment in memory. The operating system maintains reference counts for shared segments and only deallocates them when all processes have released them.

Shared memory segments provide a mechanism for inter-process communication. Processes can attach to a shared segment and communicate by reading and writing to the shared memory region. This is significantly faster than message passing through the kernel because it avoids copying data between address spaces. Operating systems typically provide system calls like shmat() and shmget() in Unix systems for creating and managing shared memory segments.

## Examples

### Example 1: Simple Segment Address Translation

Consider a system with the following segment table for a process:

| Segment Number | Base (hex) | Limit (bytes) |
|----------------|------------|---------------|
| 0 (Code)       | 0x00400000 | 8192          |
| 1 (Data)       | 0x00402000 | 16384         |
| 2 (Stack)      | 0x00406000 | 4096          |
| 3 (Heap)       | 0x00407000 | 8192          |

Given logical address (segment 2, offset 500), translate to physical address.

**Solution:**

Step 1: Identify the segment number and offset. Segment = 2, Offset = 500

Step 2: Look up segment 2 in the segment table. Base = 0x00406000, Limit = 4096

Step 3: Check if offset is valid: 500 < 4096. This is valid.

Step 4: Calculate physical address: Physical = Base + Offset = 0x00406000 + 500

Converting to decimal: 0x00406000 = 4210688, and 500 = 500
Physical address in decimal = 4210688 + 500 = 4211188

In hexadecimal: 0x00406000 + 0x000001F4 = 0x004061F4

Therefore, logical address (2, 500) maps to physical address 0x004061F4.

### Example 2: Segmentation Fault Detection

Using the same segment table from Example 1, determine if the following logical addresses cause a segmentation fault:

(a) Logical address: Segment 1, Offset 10000
(b) Logical address: Segment 0, Offset 8192

**Solution:**

(a) For segment 1 with offset 10000:
- Segment 1 limit = 16384 bytes
- Check: 10000 < 16384? YES, valid access.
- Physical address = 0x00402000 + 10000 = 0x00404E70

(b) For segment 0 with offset 8192:
- Segment 0 limit = 8192 bytes
- Check: 8192 < 8192? NO, this equals the limit, which is invalid.
- This generates a segmentation fault because valid offsets range from 0 to 8191.

The key principle is that offsets must be strictly less than the limit (0 ≤ offset < limit), not less than or equal to the limit.

### Example 3: Segment Sharing Between Processes

Process A and Process B both execute the same text editor program. The code segment is 16384 bytes and loaded at physical address 0x00010000. The segment tables are:

**Process A:**
| Segment | Base      | Limit |
|---------|-----------|-------|
| 0 (Code)| 0x00010000| 16384 |
| 1 (Data)| 0x00014000| 8192  |

**Process B:**
| Segment | Base      | Limit |
|---------|-----------|-------|
| 0 (Code)| 0x00010000| 16384 |
| 1 (Data)| 0x00018000| 8192  |

**Analysis:**

Both processes share the same code segment (segment 0 points to 0x00010000 for both), saving 16384 bytes of physical memory. However, they have different data segments. When Process A writes to offset 100 in its data segment, it accesses physical address 0x00014000 + 100 = 0x00014064. When Process B writes to offset 100 in its data segment, it accesses physical address 0x00018000 + 100 = 0x00018064. This demonstrates both sharing (code) and isolation (data) provided by segmentation.

## Exam Tips

1. Remember that segmentation uses variable-sized segments while paging uses fixed-sized pages. This is a crucial distinction frequently tested in exams.

2. The logical address in segmentation consists of two parts: segment number (or selector) and offset (or displacement). The segment number indexes into the segment table.

3. Physical address calculation: Physical Address = Segment Base + Offset. Always verify that Offset < Segment Limit before calculating.

4. Segmentation eliminates internal fragmentation (unlike paging) because segments are sized to fit the exact logical requirements, but it can suffer from external fragmentation.

5. The segment table is maintained by the operating system for each process and is stored in memory. A special register (like the segment table base register) points to it.

6. Protection in segmentation is implemented through access rights in each segment descriptor. Common access rights include read, write, and execute permissions.

7. Combined segmentation and paging provides both logical organization (segmentation) and efficient physical memory management (paging). This hybrid approach is used in x86 architectures.

8. Segment sharing allows multiple processes to share code or data segments by having their segment table entries point to the same physical memory location.

9. A segmentation fault occurs when a program tries to access memory with an invalid segment number or with an offset that exceeds the segment limit.

10. In exam questions, always check the validity of the offset against the limit before performing address translation to avoid calculation errors.