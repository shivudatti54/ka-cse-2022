# Computer System Architecture

## Overview

Computer system architecture defines the conceptual design and operational structure of a computer system. The two fundamental architectures are Von Neumann (stored program with shared memory for instructions and data) and Harvard (separate memory for instructions and data).

## Key Points

- **Von Neumann Architecture**: Stored program concept, sequential execution, single bus for data and instructions, creates bottleneck
- **Harvard Architecture**: Separate memory for instructions and data, dual bus system, enables simultaneous access
- **CPU Components**: ALU (arithmetic/logical operations), Control Unit (instruction fetch/decode/control), Registers (temporary storage)
- **Memory Hierarchy**: CPU Registers → L1/L2/L3 Cache → RAM → SSD/HDD → Tertiary Storage
- **Bus Types**: Data Bus (carries data, bidirectional), Address Bus (carries addresses, unidirectional), Control Bus (carries control signals)
- **SMP (Symmetric Multiprocessing)**: All processors equal, share memory, run same OS instance
- **NUMA (Non-Uniform Memory Access)**: Processors have local memory (faster) and can access remote memory (slower)

## Important Concepts

- Principle of Locality: Temporal (recently accessed data likely accessed again) and Spatial (nearby data likely accessed)
- Modern processors use Modified Harvard Architecture (separate caches, unified main memory)
- Multicore processors have multiple CPU cores on single chip with shared cache levels
- Cache operations: Cache Hit (data found, fast) vs Cache Miss (data not found, slow)

## Notes

- Understand Von Neumann bottleneck and why Harvard architecture addresses it
- Know RISC vs CISC differences (simple vs complex instructions)
- Be able to draw CPU fetch-decode-execute cycle and memory hierarchy diagrams
