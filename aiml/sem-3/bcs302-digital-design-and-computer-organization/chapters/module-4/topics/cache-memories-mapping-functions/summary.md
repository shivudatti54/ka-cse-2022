### Cache Memories – Mapping Functions

#### Revision Notes

**Definitions and Formulas:**

- **Cache Mapping Function**: A function that maps the virtual address of a memory location to its corresponding physical address.
- **Cache Mapping Algorithm**: A set of rules that determine how to map virtual addresses to physical addresses.
- **Set-Associative Cache**: A cache that uses a set of tags to map virtual addresses to physical addresses.
- **Direct-Mapped Cache**: A cache that uses a single tag to map virtual addresses to physical addresses.
- **Formula for Set-Associative Cache**: `P = (V \* A) mod S`, where `P` is the physical address, `V` is the virtual address, `A` is the offset, and `S` is the set size.
- **Formula for Direct-Mapped Cache**: `P = (V mod T) \* A`, where `P` is the physical address, `V` is the virtual address, `A` is the offset, and `T` is the tag size.

**Theorems:**

- **Cache Mapping Theorem**: The cache mapping function is a one-to-one function, meaning that each virtual address maps to exactly one physical address.
- **Cache Replacement Theorem**: The cache can replace a least-recently-used (LRU) entry to make room for a new entry.

**Key Points:**

- Cache mapping functions determine how to map virtual addresses to physical addresses.
- Cache mapping algorithms determine how to implement the cache mapping function.
- Set-associative caches use a set of tags to map virtual addresses to physical addresses, while direct-mapped caches use a single tag.
- Cache replacement policies, such as LRU, determine which entry to replace when the cache is full.
- Cache mapping functions and algorithms are important in digital design and computer organization.
