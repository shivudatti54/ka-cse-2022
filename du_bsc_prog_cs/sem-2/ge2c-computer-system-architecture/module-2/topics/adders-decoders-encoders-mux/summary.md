# Adders, Decoders, Encoders & Multiplexers  
**Ge2C – Computer System Architecture** (Delhi University, NEP 2024)

---

### Introduction
Combinational logic forms the backbone of digital subsystems such as ALU, memory addressing, and data routing. This summary revisits the four fundamental building blocks—adders, decoders, encoders, and multiplexers—required for the Delhi University B.Sc. Physical Science (CS) exam (Unit 4: Combinational Logic Design).

---

### • Adders  
- **Half‑Adder** – 2‑bit sum (S) and carry (C) using XOR & AND.  
- **Full‑Adder** – Adds three bits (A, B, C_in); implements sum = A⊕B⊕C_in, carry = (A·B)+(C_in·(A⊕B)).  
- **Ripple‑Carry Adder (RCA)** – Cascaded full adders; simple but slow (propagation delay ∝ number of bits).  
- **Carry‑Look‑Ahead Adder (CLA)** – Generates carry directly using generate (G) and propagate (P) terms; reduces delay to O(log n).  

### • Decoders  
- **n‑to‑2ⁿ Decoder** – Converts n‑bit binary address into a one‑hot output line; each output corresponds to a minterm.  
- **Enable Input** – Used for cascading and implementing larger decoders.  
- **Applications** – Address decoding in memory, selecting one of many devices, generating combinational logic functions (via OR of selected outputs).  

### • Encoders  
- **Binary Encoder** – 2ⁿ‑to‑n code converter; outputs binary representation of the active input line.  
- **Priority Encoder** – Resolves multiple active inputs by assigning priority (most‑significant 1 wins); includes valid flag.  
- **Truth Table** – Essential for deriving minimal Boolean expressions; used in interrupt handling and keyboard scanning.  

### • Multiplexers (MUX)  
- **2ⁿ‑to‑1 MUX** – Selects one of 2ⁿ data inputs based on n‑select lines; output = selected input.  
- **Implementation of Logic Functions** – Any Boolean function of n variables can be realized by connecting the function’s minterms to the MUX inputs and using the variables as select lines (data‑selection method).  
- **Cascading** – Larger MUX can be built from smaller ones (tree structure).  
- **Demultiplexer (DMUX)** – Inverse of MUX; routes one input to one of 2ⁿ outputs based on select lines.  

---

### Conclusion
Mastering adders, decoders, encoders, and multiplexers equips you to design efficient combinational circuits for data processing, memory addressing, and signal routing—key competencies for the Ge2C paper under Delhi University’s NEP 2024 syllabus. Quick recall of truth tables, boolean equations, and typical IC packages (e.g., 74LS08, 74LS138, 74LS151) will streamline exam preparation.