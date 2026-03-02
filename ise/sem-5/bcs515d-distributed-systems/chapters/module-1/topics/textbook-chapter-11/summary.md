# **Distributed Systems Revision Notes - Chapter 1.1**

### Key Concepts

- **Definition of Distributed Systems**:
  - A collection of interconnected computers that appear as a single system to users.
  - Computers may be geographically dispersed and communicate through communication networks.

### Terminology

- **Distributed System Model**:
  - Two models:
    1. **Homogeneous Model**: All computers in the system are identical.
    2. **Heterogeneous Model**: Computers in the system are of different types.

### Key Features

- **Autonomy**: Each computer in the system operates independently.
- **Interconnectedness**: Computers in the system are connected through communication networks.
- **Distribution**: Resources are scattered across multiple computers.

### Types of Distributed Systems

- **Homogeneous Distributed System**: Used for applications requiring identical processing power and memory.
- **Heterogeneous Distributed System**: Used for applications requiring different processing powers and memories.

### Important Formulas/Definitions/Theorems

- **Ring Structure**:
  - A linear communication topology where each computer is connected to its two neighbors.
  - Used in applications requiring uniform communication delays.
- **Bus Structure**:
  - A linear communication topology where all computers are connected to a single communication line.
  - Used in applications requiring faster communication speeds.
- **Star Structure**:
  - A communication topology where all computers are connected to a central node.
  - Used in applications requiring high-speed communication and fault-tolerance.
- **Fault Tolerance**:
  - The ability of a distributed system to continue operating even when one or more computers fail.

### Important Definitions

- **Load Sharing**:
  - The distribution of workload across multiple computers in a distributed system.
- **Resource Sharing**:
  - The sharing of resources such as memory, processing power, and files across multiple computers in a distributed system.

### Important Theorems

- **Piggybacking Theorem**:
  - States that if two computers can communicate with each other in a single step, then they can communicate with each other in a single step even if they go through a third computer.
