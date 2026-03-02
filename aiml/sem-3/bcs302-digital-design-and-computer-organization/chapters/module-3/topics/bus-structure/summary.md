# Bus Structure - Summary

## Key Definitions and Concepts

- **Bus:** A set of conducting wires that transmits data, addresses, and control signals between computer components
- **Data Bus:** Bidirectional bus carrying actual data; width determines data transfer capacity per cycle
- **Address Bus:** Unidirectional bus carrying memory addresses from CPU to memory/I/O devices
- **Control Bus:** Carries timing and coordination signals (MEMR, MEMW, IOR, IOW)
- **Bus Arbitration:** Process of determining which device gains bus control when multiple devices request access
- **Bus Bandwidth:** Maximum data transfer rate, calculated as (Bus Width in bytes) × (Clock Frequency)

## Important Formulas and Theorems

- Maximum memory locations addressable = 2^(number of address lines)
- Bus Bandwidth (bytes/s) = Bus Width (bytes) × Clock Frequency (Hz)
- Bus Cycle Time = 1 / Clock Frequency

## Key Points

- The CPU connects to memory and I/O through three distinct bus types: data, address, and control
- Data bus width directly impacts system performance—wider buses enable faster data transfer
- Address bus width determines maximum directly addressable memory capacity
- Bus arbitration prevents multiple devices from simultaneously driving the bus
- Single bus systems are simple but create performance bottlenecks
- Multi-bus and hierarchical bus structures improve performance through parallel communication paths
- Wait states are inserted when slower devices cannot keep pace with CPU speed
- Modern computers use hierarchical bus designs balancing speed, cost, and flexibility

## Common Mistakes to Avoid

- Confusing data bus (bidirectional) with address bus (unidirectional from CPU)
- Forgetting that address bus width determines memory capacity, not data bus width
- Assuming wider buses always mean faster systems—considering bus speed and device capabilities is equally important
- Overlooking that actual bus performance is always lower than theoretical maximum due to protocol overhead

## Revision Tips

- Draw a diagram showing CPU, memory, and I/O connected via address, data, and control buses
- Practice calculating bandwidth and addressable memory for different bus configurations
- Memorize the direction of data flow for each bus type
- Review how bus design affects the basic performance equation (Execution Time = Instructions × Cycles/Instruction × Cycle Time)