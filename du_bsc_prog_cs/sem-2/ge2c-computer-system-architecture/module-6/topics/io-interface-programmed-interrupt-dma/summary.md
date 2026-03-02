# I/O Interface, Programmed Interrupt & DMA
**Ge2C Computer System Architecture** | BSc Physical Science (CS) — Delhi University, NEP 2024

---

## Introduction

The I/O subsystem is critical for data transfer between the CPU and external devices. This summary covers three fundamental I/O handling techniques: **Programmed I/O**, **Interrupt-driven I/O**, and **Direct Memory Access (DMA)** — essential topics as per the Delhi University BSc CS syllabus under the Ge2C paper.

---

## Key Concepts

### 1. I/O Interface
- Acts as an intermediary between CPU and I/O devices
- Includes **I/O ports**, **device controllers**, and **control lines**
- Functions: Data transfer, status reporting, device selection, control signaling

### 2. Programmed I/O
- **CPU actively polls** device status registers continuously
- Data transfer controlled entirely by CPU
- **Disadvantages**: Wastes CPU cycles (busy-waiting), poor efficiency, blocks other operations
- Simple to implement; suitable for slow devices

### 3. Interrupt-Driven I/O
- Device **initiates** transfer by sending an interrupt signal
- CPU executes interrupt service routine (ISR) to handle data transfer
- **Advantages**: CPU not wasted in polling, efficient resource utilization, supports multiple devices
- **Process**: Interrupt request → CPU saves state → Execute ISR → Restore state → Continue
- Includes interrupt priority, vector tables, masking concepts

### 4. Direct Memory Access (DMA)
- **Bypasses CPU** — data transfers directly between I/O device and memory
- Uses a **DMA controller** (e.g., 8237 DMA chip)
- **Types**:
  - **Burst/Block Transfer Mode**: Entire block transferred in one go
  - **Cycle Stealing Mode**: DMA steals memory cycles
  - **Transparent Mode**: DMA transfers only when CPU not using bus
- **Advantages**: High-speed transfers, CPU freed for other tasks
- Used for disk, tape, network card I/O

---

## Comparison at a Glance

| Feature | Programmed I/O | Interrupt I/O | DMA |
|---------|---------------|---------------|-----|
| CPU Involvement | Continuous | On interrupt | Minimal |
| Speed | Slow | Moderate | Fast |
| Efficiency | Low | High | Highest |
| Complexity | Simple | Moderate | Complex |

---

## Conclusion

Understanding these I/O mechanisms is vital for designing efficient computer systems. **Programmed I/O** is simple but inefficient, **Interrupt-driven I/O** improves utilization, and **DMA** provides the highest performance for bulk data transfers. For the Delhi University NEP 2024 exam, remember to emphasize the trade-offs: CPU time vs. hardware complexity vs. transfer speed. DMA controllers and interrupt handling are frequently asked topics — ensure clarity on how each method handles the **data transfer cycle** between CPU, memory, and peripheral devices.