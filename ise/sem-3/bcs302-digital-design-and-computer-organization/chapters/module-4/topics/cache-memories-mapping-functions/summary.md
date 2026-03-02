# Cache Memories – Mapping Functions

### Definitions and Notations

- **Cache**: A small, fast memory that stores frequently accessed data or instructions.
- **Tag**: An identifier for a cache line, used to distinguish between different data or instructions.
- **Set**: A group of cache lines that share the same tag.
- **Mapping Function**: A method for mapping memory addresses to cache lines.
- **Index**: An index into the set of cache lines that corresponds to a memory address.
- **Valid Bit**: A bit that indicates whether a cache line is valid or not.
- **Dirty Bit**: A bit that indicates whether a cache line needs to be written back to main memory.

### Mapping Functions

- **Direct Mapping**: Each memory address maps directly to a specific cache line.
  - Formula: `Index = Address mod N` (where N is the number of cache lines per set)
  - Advantages: Simple, fast mapping.
  - Disadvantages: May lead to cache line collisions.

### Important Formulas and Theorems

- **Direct Mapping Formula**: `Index = Address mod N`
- **Set Associativity**: The number of cache lines per set.
- **Cache Line Size**: The size of each cache line in bits.
- **Cache Hit**: When a requested cache line is found in the cache.
- **Cache Miss**: When a requested cache line is not found in the cache.
- **Cache Replacement Policy**: A method for replacing a cache line when it becomes invalid.

### Revisions

- Review the different types of mapping functions (e.g., direct mapping, indirect mapping, fully associative mapping).
- Understand the advantages and disadvantages of each mapping function.
- Practice calculating indices and valid/dirty bits for different mapping functions.
- Review the formulas and theorems related to cache memories and mapping functions.
