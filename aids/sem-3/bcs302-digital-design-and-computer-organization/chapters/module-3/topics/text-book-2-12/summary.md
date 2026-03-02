# **Text Book 2: 1.2 - Digital Design and Computer Organization**

### Key Points

- **Bus Structure**
  - Types of buses: AHB (Advanced Hardware Bus), AXI (Advanced eXtensible Interface)
  - Bus width: 32-bit, 64-bit, etc.
  - Address decoding: Decoding logic for address bus
- **Bus Timing**
  - Clock speed: Measured in cycles per second (Hz)
  - Clock period: Time taken by the clock signal to complete one cycle
  - Setup time: Time between clock edge and data valid
  - Hold time: Time between data valid and clock edge
- **Bus protocols**
  - Master-slave protocol: Master controls data transfer
  - Arbitration protocol: Ranges (e.g. AXI, AHB)
- **Bus width and Speed**
  - Bus width: 32-bit, 64-bit, 128-bit, etc.
  - Bus speed: 1 Mhz, 100 Mhz, 1 Gz, etc.

### Important Formulas and Definitions

- **Bus width**: Number of bits transferred between nodes
- **Clock speed**: Number of cycles per second
- **Clock period**: Time taken by clock signal to complete one cycle
- **Setup time**: Time between clock edge and data valid
- **Hold time**: Time between data valid and clock edge
- **Arbitration protocol**: Used to resolve conflicts between masters

### Theorems and Concepts

- **Axiom**: Master always wins arbitration
- **Bus contention**: When multiple masters try to access same bus
