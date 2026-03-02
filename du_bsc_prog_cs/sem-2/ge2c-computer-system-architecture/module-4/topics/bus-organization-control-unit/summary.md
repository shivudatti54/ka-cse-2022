# Bus Organization & Control Unit  
**Subject:** Ge2C – Computer System Architecture  
**Programme:** BSc (Physical Sciences) CS – Delhi University (NEP 2024)

---

## Introduction
The **bus** is the communication backbone that interconnects the CPU, memory, and I/O devices. The **Control Unit** manages all bus‑related activities – directing data flow, generating timing signals, and resolving contention among multiple bus masters. Understanding bus organization and its control mechanisms is essential for designing efficient computer systems and for exam success.

---

## Key Concepts

- **Bus Types**
  - **Address Bus** – carries memory/I/O addresses (unidirectional).
  - **Data Bus** – transfers data words (bidirectional, width determines throughput).
  - **Control Bus** – carries timing and control signals (e.g., RD, WR, MEMR, MEMW, IOR, IOW, INT, BUSY).

- **Bus Organization**
  - **System Bus** = Address + Data + Control bus (connects CPU, main memory, and primary I/O).
  - **I/O Bus** – dedicated to peripheral devices (e.g., ISA, PCI, USB).
  - **Memory Bus** – high‑speed link between CPU and main memory.

- **Control Unit Functions**
  - **Signal Generation** – produces RD/WR, MEM/I/O, and interrupt acknowledge pulses.
  - **Bus Arbitration** – decides which device gains control when multiple masters request the bus.
  - **Timing Control** – synchronizes bus cycles (synchronous vs. asynchronous) and defines setup/hold times.
  - **Data Path Management** – multiplexes address/data lines, enables tri‑state buffers, and routes data to/from registers.

- **Arbitration Methods**
  - **Centralized** – a dedicated arbiter (e.g., daisy‑chain, priority encoder) resolves requests.
  - **Distributed** – each device follows a protocol (e.g., token‑passing, round‑robin).
  - **Priority Schemes** – fixed priority, rotating priority, or hierarchical priority.

- **Bus Cycles**
  - **Read Cycle** – address placed → RD asserted → memory/I/O drives data → CPU latches data.
  - **Write Cycle** – address + data placed → WR asserted → memory/I/O captures data.
  - **Interrupt Cycle** – INT request → CPU acknowledges → service routine vector fetched.
  - **DMA Cycle** – bus master (DMA controller) takes control for block transfers without CPU intervention.

- **Bus Performance**
  - **Bandwidth** = (bus width) × (clock frequency) / cycles per transfer.
  - **Latency** – waiting time for arbitration or response.
  - **Trade‑offs** – wider bus increases bandwidth but raises cost and complexity; higher clock speeds need stricter timing and shielding.

- **Relevant Standards (as per DU syllabus)**
  - **PCI/PCI‑Express** – modern system and expansion bus.
  - **USB** – serial peripheral interconnect.
  - **SCSI** – high‑speed disk/ tape bus.
  - **ISA** – legacy PC expansion bus (for basic I/O).

---

## Conclusion
The bus organization and its control unit dictate how efficiently the CPU, memory, and peripherals communicate. Mastery of bus types, control signals, arbitration, timing, and performance metrics equips students to analyze and design modern computer architectures—an essential competency for the Ge2C exam and future system‑design roles.