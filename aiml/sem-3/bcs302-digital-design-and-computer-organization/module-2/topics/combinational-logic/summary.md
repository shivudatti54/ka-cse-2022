# Summary: Combinational Logic

**1. Definition:** Combinational circuits produce outputs dependent solely on current inputs with no memory or feedback. Formally: Y(t) = F[X(t)] for all time t.

**2. Design Procedure:** Problem specification → Input/Output assignment → Truth table construction → Boolean function derivation → Minimization (K-maps/algebraic) → Gate implementation.

**3. Key Circuits:**
- **Half Adder:** S = A ⊕ B, C = A•B
- **Full Adder:** S = A ⊕ B ⊕ C_in, C_out = AB + BC_in + AC_in (implementable with two half adders + OR)
- **MUX:** Data selector; 2ⁿ-to-1 with n select lines
- **DEMUX:** Data distributor; 1-to-2ⁿ with n select lines
- **Decoder:** n-to-2ⁿ binary to unary conversion
- **Priority Encoder:** 2ⁿ-to-n with priority logic
- **Magnitude Comparator:** Determines A > B, A = B, A < B
- **Parity Circuit:** Single-bit error detection

**4. Minimization Techniques:** Karnaugh map grouping, algebraic simplification, Quine-McCluskey for automation.

**5. Universal Gates:** NAND and NOR gates can implement any Boolean function independently.

**6. Timing Considerations:** Propagation delay (t_p) determines circuit speed; critical path analysis identifies maximum operating frequency.

**7. Hazard Analysis:** Static hazards (1-hazard, 0-hazard) eliminated by adding redundant prime implicants using K-map optimization.

These concepts provide the foundation for constructing complex digital systems including ALUs, control units, and complete processor datapaths.