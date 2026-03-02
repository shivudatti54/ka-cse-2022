# Operating System: Definition, Structure & Operations  
*For BSc Physical Science (CS) – Delhi University, NEP 2024*

---

## 1. Introduction  
An Operating System (OS) is the core system software that manages hardware resources and provides an interface for user applications. In the Delhi University NEP 2024 syllabus, this unit (“OS – Definition, Structure, Operations”) introduces the fundamental role of the OS, its internal organization, and the mechanisms by which it controls computation.

---

## 2. Definition & Core Functions  
- **What is an OS?** – Layer of software between hardware and user programs.  
- **Primary functions**  
  - **Resource Management** – CPU, memory, I/O devices, storage.  
  - **Process Management** – Create, schedule, terminate processes; context switching.  
  - **Memory Management** – Allocation/de‑allocation, paging, segmentation, virtual memory.  
  - **File System** – Organization, naming, protection of files.  
  - **Device Handling** – Drivers, buffering, interrupt handling.  
  - **Security & Protection** – Access control, authentication, isolation.  

---

## 3. OS Types (by usage)  
- **Batch OS** – Jobs collected and processed in batches.  
- **Time‑Sharing OS** – Multi‑user interactive environment (e.g., UNIX).  
- **Real‑Time OS** – Strict timing constraints (e.g., embedded systems).  
- **Network OS** – Provides networking capabilities.  
- **Distributed OS** – Manages multiple interconnected machines as a single system.

---

## 4. OS Structure  

| Model | Description | Example |
|-------|-------------|---------|
| **Monolithic** | Entire kernel runs in a single address space; all services are compiled together. | Early UNIX, Linux (modular) |
| **Microkernel** | Minimal kernel; most services (file‑system, drivers) run in user space. | Minix, GNU Hurd |
| **Hybrid** | Combines monolithic speed with microkernel modularity. | Windows NT, macOS X |

- **Kernel** – Core of OS; executes privileged instructions, manages CPU调度, memory, interrupts.  
- **System Calls** – API for user programs to request OS services (e.g., `read`, `fork`, `exec`).  
- **User Space** – Libraries, shells, applications.  

---

## 5. OS Operations  

1. **Booting** – Power‑on self‑test (POST) → bootstrap loader → kernel initialization.  
2. **Shutdown** – Graceful termination of processes, flushing caches, powering off.  
3. **Process Scheduling** – Determines which ready process runs on CPU (FCFS, SJF, Round‑Robin, Multilevel Queue).  
4. **Interrupt Handling** – Hardware/Software interrupts trigger ISR (Interrupt Service Routines).  
5. **Device I/O** – Polling, DMA, buffering; drivers translate generic requests into device‑specific commands.  
6. **Virtual Memory** – Paging and page‑table management give each process a large, isolated address space.  
7. **Deadlock Handling** – Prevention, avoidance, detection, and recovery strategies.  

---

## 6. Key Terms for Quick Revision  

- **Kernel Mode vs. User Mode** – Privileged vs. restricted execution levels.  
- **Context Switch** – Saving/restoring CPU state when switching between processes.  
- **System Call Interface** – Bridge between user programs and OS services.  
- **Shell** – Command‑line interpreter that invokes system calls.  
- **File Descriptor** – OS‑provided handle for open files.  

---

## 7. Conclusion  
Understanding the **definition**, **structural models**, and **operational mechanisms** of an OS is essential for grasping how hardware is abstracted into usable services. This unit forms the foundation for later topics such as process synchronization, memory management, and distributed systems in the Delhi University BSc (Physical Science) curriculum.  

*Use this summary for rapid recall of OS concepts, focusing on definitions, structural variants, and the primary operations that keep a computer system running.*