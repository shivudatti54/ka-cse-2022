**Pipelining Interrupts – Quick Revision (Ge2C – Delhi University, NEP 2024)**  

*Introduction*  
In a pipelined processor, an interrupt must be serviced while many instructions are simultaneously in various pipeline stages. Ensuring that the machine state is consistent and that the correct instruction is identified as the interrupt‑causing one adds complexity compared with a non‑pipelined CPU. This summary covers the essential concepts required for the Delhi University BSc (CS) exam.

---

- **What is an interrupt in a pipeline?**  
  - An asynchronous or synchronous event that forces the CPU to suspend the current instruction stream and transfer control to an Interrupt Service Routine (ISR).  
  - In a pipeline the interrupt may affect instructions that are already partially executed in IF, ID, EX, MEM, or WB stages.

- **Types of interrupts**  
  - **Synchronous** (e.g., overflow, divide‑by‑zero, page fault) – caused by the executing instruction.  
  - **Asynchronous** (e.g., I/O device request, timer) – independent of the instruction stream.

- **Key challenge – precise (exact) interrupts**  
  - The pipeline must guarantee that *all* instructions before the interrupting instruction have completed and *none* after it have altered the architectural state.  
  - This requirement is called **precise interrupt** and is essential for correct program recovery.

- **Pipeline flush**  
  - When an interrupt is detected, the pipeline registers (IF/ID, ID/EX, EX/MEM, MEM/WB) are cleared (flushed).  
  - The program counter (PC) of the interrupting instruction is saved so that execution can resume after the ISR.

- **Mechanisms to achieve precise interrupts**  
  - **History/Checkpoint Buffer** – records register‑file updates; on interrupt, the state is rolled back.  
  - **Reorder Buffer (ROB)** – holds results of speculative instructions; only commit results after the instruction is confirmed non‑interruptive.  
  - **Early detection** – evaluating condition codes in the ID stage reduces the number of flushed stages.

- **Interrupt latency**  
  - Defined as the number of cycles from interrupt request to the first instruction of the ISR.  
  - Latency grows with pipeline depth; deeper pipelines need more sophisticated hardware to keep latency low.

- **Prioritization & nested interrupts**  
  - The interrupt controller assigns a priority level; higher‑priority interrupts can preempt lower‑priority ones (nested interrupts).  
  - Nested handling requires saving the status register and PC for each level.

- **Performance impact**  
  - Flushing the pipeline introduces stall cycles (typically 1‑3 cycles per stage).  
  - Advanced techniques (ROB, checkpointing) mitigate the overhead but add hardware complexity.

- **Example (MIPS 5‑stage pipeline)**  
  - Overflow detected in EX stage → the EX/MEM register signals an interrupt.  
  - Pipeline flushes IF, ID, EX; saved PC points to the overflow instruction.  
  - Control transfers to the ISR; after service, execution resumes from the saved PC, preserving precise state.

- **Syllabus alignment (Delhi University – Ge2C)**  
  - This topic falls under **Unit III – Pipelining & Control Hazards**, which includes instruction pipelines, data/control hazards, and **interrupt handling in pipeline** as per the NEP 2024 curriculum.

---

*Conclusion*  
Effective pipelined interrupt handling balances correctness (precise state) with performance (low latency and minimal flush overhead). Mastery of concepts such as pipeline flush, precise interrupts, latency, and hardware support like history buffers is essential for exam success.