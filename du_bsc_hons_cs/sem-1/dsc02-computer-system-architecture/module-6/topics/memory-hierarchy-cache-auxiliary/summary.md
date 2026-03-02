# Memory Hierarchy, Cache and Auxiliary Memory  

**Introduction**: The memory hierarchy is a fundamental concept in computer system architecture, designed to bridge the speed‑cost gap between the fast processor and slower, larger storage. According to the Delhi University B.Sc. (Hons) CS NEP‑2024 UGCF syllabus, this unit covers hierarchical organization, cache mechanisms, and auxiliary storage.  

**Key Concepts**  

- **Memory Hierarchy Levels** (fastest → slowest, cheapest → most expensive)  
  - **Registers** – on‑chip, sub‑nanosecond latency.  
  - **Cache (L1, L2, L3)** – SRAM, few nanoseconds, tens to hundreds of KB.  
  - **Main Memory (RAM)** – DRAM, tens to hundreds of nanoseconds, GB capacity.  
  - **Secondary/Auxiliary Storage** – HDD, SSD, magnetic tape, optical drives; millisecond latency, TB+ capacity.  

- **Locality of Reference**  
  - Temporal locality – recently accessed items likely re‑accessed.  
  - Spatial locality – nearby addresses accessed soon after.  

- **Cache Memory**  
  - **Mapping Techniques**:  
    - Direct mapped (one line per set)  
    - Fully associative (any location)  
    - Set‑associative (compromise between the two)  
  - **Cache Line/Block**: smallest unit transferred (e.g., 64 B).  
  - **Write Policies**: Write‑through (update memory immediately) vs. Write‑back (delay update).  
  - **Replacement Policies**: LRU, FIFO, Random.  
  - **Hit Ratio & Access Time**: Average memory access time (AMAT) = Hit time + Miss rate × Miss penalty.  
  - **Multilevel Caches**: Inclusive vs. exclusive hierarchies; shared vs. private caches.  

- **Auxiliary (Secondary) Storage**  
  - **Magnetic Disks**: Tracks, sectors, cylinders, seek time, rotational latency, transfer rate.  
  - **RAID**: Levels 0‑5 provide redundancy/performance; commonly used in servers.  
  - **Solid‑State Drives (SSD)**: NAND flash, no moving parts, lower latency, higher throughput than HDD.  
  - **Tape/Optical**: Sequential access, high capacity, used for archival.  

- **Interaction with CPU & OS**  
  - **Bus & Memory Controller**: Coordinate data movement between levels.  
  - **Virtual Memory & TLB**: Translate logical addresses, reduce miss penalty.  
  - **DMA (Direct Memory Access)**: Offload I/O transfers from CPU.  

- **Exam‑Focused Summary**  
  - Memory hierarchy balances speed, cost, and capacity.  
  - Cache design (mapping, write policy, replacement) directly influences hit ratio.  
  - Auxiliary memory provides non‑volatile, high‑capacity storage; performance measured in I/Ops and throughput.  
  - Understanding AMAT and locality helps predict system performance.  

**Conclusion**: Mastery of memory hierarchy, cache mechanisms, and auxiliary storage is essential for designing cost‑effective, high‑performance computer systems—a core objective of the Delhi University Computer System Architecture syllabus.