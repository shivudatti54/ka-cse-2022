# Basic Operational Concepts
### Module Summary: Basic Operational Concepts

**Core Concepts:**
- The CPU executes instructions through a repetitive **fetch-decode-execute** cycle
- Each phase involves specific **micro-operations** that transfer data between registers, ALU, and memory
- **Register Transfer Notation (RTL)** provides formal specification: `MAR ← PC`, `MBR ← M[MAR]`, `IR ← MBR`

**Key Registers:**
- **PC (Program Counter)**: Holds address of next instruction; modified by branch/jump instructions
- **IR (Instruction Register)**: Holds current instruction being decoded
- **MAR/MBR**: Interface registers for CPU-memory communication

**Performance Analysis:**
- **CPI (Clock Cycles Per Instruction)**: Average cycles = Σ(frequency × CPI) for each instruction type
- **Execution Time** = Instruction Count × CPI × Clock Period
- Different instruction types have different CPI values based on complexity

**Advanced Topics:**
- **Control Unit**: Generates timing signals; implemented via hardwired FSM or microprogramming
- **Interrupt Handling**: Modifies basic cycle to save state and transfer to ISR
- **Pipelining**: Overlaps instruction phases to improve throughput toward CPI = 1