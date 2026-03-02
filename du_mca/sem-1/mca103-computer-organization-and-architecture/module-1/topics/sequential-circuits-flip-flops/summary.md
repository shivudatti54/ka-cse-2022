# Sequential Circuits & Flip-Flops - Summary

## Key Definitions and Concepts
- **Sequential Circuit**: Digital circuit with memory of past states
- **Flip-Flop**: Basic 1-bit memory element with clock control
- **Setup Time**: Minimum data stability period before clock edge
- **Hold Time**: Minimum data stability period after clock edge
- **Metastability**: Temporary unstable state violating timing constraints

## Important Formulas and Theorems
- D Flip-Flop: Q(t+1) = D
- JK Flip-Flop: Q(t+1) = JQ' + K'Q
- T Flip-Flop: Q(t+1) = T ⊕ Q
- Maximum Clock Frequency: f<sub>max</sub> = 1/(t<sub>cq</sub> + t<sub>comb</sub> + t<sub>su</sub>)
- Metastability MTBF = (e<sup>t<sub>r</sub>/τ</sup>)/(f<sub>clk</sub> f<sub>data</sub>)

## Key Points
- Synchronous circuits use global clock; asynchronous use local signals
- D flip-flops are preferred for data storage due to simplicity
- Master-Slave configuration prevents race conditions
- Counters require careful state encoding to avoid glitches
- Setup violations cause metastability; hold violations cause data corruption
- Dual-port RAMs use flip-flops for simultaneous read/write operations
- Clock gating reduces power consumption in sequential circuits

## Common Mistakes to Avoid
- Confusing latches with edge-triggered flip-flops
- Neglecting to account for propagation delays in timing diagrams
- Using asynchronous reset signals without proper synchronization
- Forgetting to initialize flip-flops in state machine designs

## Revision Tips
1. Practice converting between flip-flop types using characteristic equations
2. Draw timing diagrams for different clock edge scenarios
3. Memorize standard flip-flop excitation tables
4. Solve previous years' DU questions on counter design and timing analysis
5. Use Verilog/VHDL simulators to visualize sequential circuit behavior