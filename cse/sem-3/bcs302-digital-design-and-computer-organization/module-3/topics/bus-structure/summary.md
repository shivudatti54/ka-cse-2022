### Topic Summary: Bus Structure

**Key Definitions:**
- **Bus:** A shared communication pathway comprising parallel wires connecting CPU, memory, and I/O devices
- **Bus Arbitration:** Process of resolving conflicts when multiple devices simultaneously request bus access
- **Bus Bandwidth:** Maximum data transfer rate, computed as (Bus Width × Clock Frequency)

**Core Concepts:**
1. Three bus types: Data (bidirectional), Address (unidirectional), Control (timing/signals)
2. Single bus offers simplicity but creates performance bottlenecks under high load
3. Hierarchical bus architecture separates high-speed CPU-memory traffic from lower-speed I/O
4. Synchronous buses use fixed clock cycles; asynchronous buses use request-acknowledge handshaking
5. Centralized arbitration employs a single arbiter; distributed arbitration spreads logic across devices

**Critical Formulas:**
- Addressable memory = 2ⁿ (where n = number of address lines)
- Bus Bandwidth = Bus Width (bits) × Clock Frequency (Hz)

**Practical Implications:**
- 64-bit bus at 800 MHz yields 6.4 GB/s theoretical bandwidth
- Wait states reduce effective bandwidth proportionally
- Modern systems use PCIe hierarchy (x16 for GPUs, x4 for NVMe) rather than legacy parallel buses