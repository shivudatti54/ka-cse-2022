**Signals & Transmission Media – Quick Revision (Delhi University, BSc CS – NEP 2024)**  

*Introduction*  
This unit introduces the fundamental concepts of **signals** (analog & digital) and the **media** used to carry them between devices in a computer network. Understanding these concepts is essential for analysing data transmission, network performance, and the design of reliable communication systems.

---

### 1. Signals
- **Analog**: Continuous values (e.g., voice, video).  
- **Digital**: Discrete binary (0/1) pulses.  
- **Signal Properties**: Amplitude, frequency, phase, wavelength, and bandwidth.  
- **Encoding Techniques**: NRZ‑L, NRZ‑I, Manchester, Differential Manchester, AMI – convert data into signal form.  

### 2. Transmission Modes
- **Simplex**: One‑direction only (e.g., TV broadcast).  
- **Half‑Duplex**: Two‑way, one at a time (e.g., walkie‑talkie).  
- **Full‑Duplex**: Simultaneous two‑way (e.g., telephone).  
- **Serial vs. Parallel**: Serial transmits bit‑by‑bit; parallel transmits multiple bits simultaneously (short distances).  

### 3. Transmission Media
#### Guided (Wired)
- **Twisted‑Pair (UTP/STP)**: Cat5e/6/6a; used in LANs; susceptible to EMI.  
- **Coaxial Cable**: Higher bandwidth & shielding; used for cable TV and early Ethernet.  
- **Fiber‑Optic**: Light‑based; immune to EMI, very high bandwidth, long distances (single‑mode & multimode).  

#### Unguided (Wireless)
- **Radio Waves**: Low‑to‑mid frequency; used in Wi‑Fi, Bluetooth, cellular.  
- **Microwave**: Line‑of‑sight; high capacity point‑to‑point links.  
- **Infrared**: Short‑range, line‑of‑sight (e.g., remote controls).  

### 4. Key Performance Parameters
- **Bandwidth‑Delay Product**: Determines throughput for long‑latency links.  
- **Throughput (bps) vs. Bandwidth (Hz)**: Practical data transfer rate vs. capacity of the medium.  
- **Latency (Propagation + Transmission + Processing)**: End‑to‑end delay.  
- **Jitter**: Variation in packet arrival times; critical for real‑time traffic.  

### 5. Transmission Impairments
- **Attenuation**: Signal strength loss over distance.  
- **Distortion**: Shape change due to varying propagation speeds.  
- **Noise**: Thermal, intermodulation, crosstalk, impulse – degrades signal quality.  
- **Signal‑to‑Noise Ratio (SNR)**: Higher SNR → better error performance.  

### 6. Multiplexing & Switching (Brief)
- **Frequency‑Division (FDM)**, **Time‑Division (TDM)**, **Code‑Division (CDM)**: Share medium among multiple signals.  
- **Circuit‑Switched** (dedicated path) vs. **Packet‑Switched** (store‑and‑forward).  

---

*Conclusion*  
Mastering signals and the various guided/unguided transmission media, along with their performance metrics and impairments, equips a network engineer to choose the appropriate medium for a given application, design robust LAN/WAN topologies, and troubleshoot connectivity issues effectively.  

*(Based on Delhi University BSc (CS) NEP 2024 Syllabus – Unit: Signals Transmission Media)*