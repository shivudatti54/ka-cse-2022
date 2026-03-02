# Combinational and Sequential Circuits

## Comprehensive Study Material for Computer System Architecture

---

## 1. Introduction

Digital electronics forms the backbone of modern computing systems, and understanding the distinction between combinational and sequential circuits is fundamental to computer architecture. While **combinational circuits** produce outputs based solely on current inputs, **sequential circuits** incorporate memory elements that allow outputs to depend on both current inputs and past inputs (history).

In the real world, these circuits are everywhere:

- **Combinational circuits** are used in calculators, ALU (Arithmetic Logic Units), and data path units
- **Sequential circuits** form the basis of memory elements, counters, shift registers, and control units in processors
- Modern microprocessors contain millions of these fundamental building blocks working in harmony

This study material covers the complete spectrum of combinational and sequential circuits as prescribed in the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus, with emphasis on practical applications, timing analysis, and state machine design.

---

## 2. Fundamentals: Combinational vs Sequential Circuits

### 2.1 Combinational Circuits

**Definition**: Combinational circuits are digital logic circuits whose output depends only on the present input values. They have no memory element.

**Characteristics**:
- Output = f(Input₁, Input₂, ..., Inputₙ)
- No feedback paths
- No memory capability
- Faster operation (no waiting for state changes)
- Examples: Adders, Subtractors, Multiplexers, Decoders

```
        ┌──────────────┐
Input → │  Combinational │ → Output
        │     Logic      │
        └──────────────┘
```

### 2.2 Sequential Circuits

**Definition**: Sequential circuits are digital logic circuits whose output depends on both current inputs and previous outputs (stored state).

**Characteristics**:
- Output = f(Input, Present State)
- Next State = g(Input, Present State)
- Contains feedback paths
- Has memory capability
- Requires clock signal (usually)
- Examples: Flip-flops, Registers, Counters, State Machines

```
        ┌──────────────┐
Input → │  Sequential  │ → Output
        │     Logic    │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   Memory     │
        │   Element    │
        └──────────────┘
```

---

## 3. Combinational Circuits: Detailed Analysis

### 3.1 Arithmetic Circuits

#### 3.1.1 Half Adder

A half adder adds two 1-bit numbers and produces sum and carry outputs.

**Truth Table**:

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 |    0    |     0     |
| 0 | 1 |    1    |     0     |
| 1 | 0 |    1    |     0     |
| 1 | 1 |    0    |     1     |

**Boolean Expressions**:
- Sum (S) = A ⊕ B (XOR)
- Carry (C) = A · B (AND)

**Circuit Diagram**:
```
    A ──┬───[XOR]──→ S
        │   
    B ──┴───[AND]──→ C
```

#### 3.1.2 Full Adder

A full adder adds three 1-bit numbers (two significant bits and one carry-in).

**Truth Table**:

| A | B | Cin | Sum (S) | Cout |
|---|----|-----|---------|------|
| 0 | 0 |  0  |    0    |  0   |
| 0 | 0 |  1  |    1    |  0   |
| 0 | 1 |  0  |    1    |  0   |
| 0 | 1 |  1  |    0    |  1   |
| 1 | 0 |  0  |    1    |  0   |
| 1 | 0 |  1  |    0    |  1   |
| 1 | 1 |  0  |    0    |  1   |
| 1 | 1 |  1  |    1    |  1   |

**Boolean Expressions**:
- Sum (S) = A ⊕ B ⊕ Cin
- Carry Out (Cout) = (A · B) + (Cin · (A ⊕ B))

**Implementation using two half adders**:
```
        A ──┬─────────────┐
            │  Half Adder │
        B ──┴───[XOR]──┬──→ S
                       │
                    [XOR]──→ Sum
                       │
        Cin ──────────┘
        
        First HA Carry ──┬──[OR]──→ Cout
        Second HA Carry ─┘
```

#### 3.1.3 4-bit Parallel Adder (Ripple Carry)

Using four full adders connected in cascade to add two 4-bit numbers:

```
        A3 A2 A1 A0
        │  │  │  │
       FA FA FA FA
        │  │  │  │
        B3 B2 B1 B0
        │  │  │  │
       C3 C2 C1 C0 → Carry
        │  │  │  │
       S3 S2 S1 S0 → Sum
```

**VHDL Code for Full Adder**:

```vhdl
-- Full Adder Entity
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Full_Adder is
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           Cin : in STD_LOGIC;
           Sum : out STD_LOGIC;
           Cout : out STD_LOGIC);
end Full_Adder;

architecture Behavioral of Full_Adder is
begin
    Sum <= A XOR B XOR Cin;
    Cout <= (A AND B) OR (Cin AND (A XOR B));
end Behavioral;
```

### 3.2 Multiplexers (MUX)

A multiplexer selects one of many input lines and forwards it to a single output line based on select lines.

**4:1 Multiplexer**:

| S1 | S0 | Output (Y) |
|----|----|-------------|
| 0  | 0 |    I0       |
| 0  | 1 |    I1       |
| 1  0 |    I2       |
| 1  | 1 |    I3       |

**Boolean Expression**:
Y = I0·S1'·S0' + I1·S1'·S0 + I2·S1·S0' + I3·S1·S0

**Circuit Symbol**:
```
    I0 ─┐
    I1 ─┤
    I2 ─┤   ┌────┐
    I3 ─┤───│ MUX│──→ Y
    S0 ─┤   │    │
    S1 ─┘   └────┘
```

**Applications**:
- Data selection
- Function generation (implementing Boolean functions)
- Parallel-to-serial conversion
- Waveform generation

### 3.3 Demultiplexers (DEMUX)

A demultiplexer routes one input to one of several outputs based on select lines.

**1:4 Demultiplexer**:

| S1 | S0 | Output |
|----|----|--------|
| 0  | 0 |  Y=I→D0|
| 0  1 |  Y=I→D1|
| 1  | 0 |  Y=I→D2|
| 1  | 1 |  Y=I→D3|

### 3.4 Encoders and Decoders

#### 3.4.1 Decoder (2:4 Decoder)

Converts binary information from n input lines to a maximum of 2ⁿ unique output lines.

**Truth Table**:

| Enable | A1 | A0 | D3 | D2 | D1 | D0 |
|--------|----|----|----|----|----|-----|
|   1    | 0  | 0  | 0  | 0  | 0  |  1  |
|   1    | 0  | 1  | 0  | 0  | 1  |  0  |
|   1    | 1  | 0  | 0  | 1  | 0  |  0  |
|   1    | 1  | 1  | 1  | 0  | 0  |  0  |
|   0    | X  | X  | 0  | 0  | 0  |  0  |

#### 3.4.2 Encoder (4:2 Encoder)

Converts one of 2ⁿ input lines into n output lines.

**Priority Encoder**: If multiple inputs are high, highest priority input is encoded.

### 3.5 Magnitude Comparator

Compares two binary numbers and determines their relationship (A > B, A = B, A < B).

**For 1-bit comparator**:
- A > B: A·B'
- A < B: A'·B
- A = B: (A⊕B)' = A·B + A'·B'

---

## 4. Sequential Circuits: Detailed Analysis

### 4.1 Latches

Latches are level-triggered memory elements. They change output whenever the enable signal is active.

#### 4.1.1 SR Latch (Set-Reset)

**Circuit using NOR gates**:

```
    S ──┬──[NOR]──[NOR]──┬── Q
        │         ▲      │
        │         │      │
    R ──┴─────────┘      │
                        Q'
```

**Truth Table**:

| S | R | Q (next) | Q' (next) | State |
|---|---|----------|-----------|-------|
| 0 | 0 |    Q     |    Q'     | Hold  |
| 0 | 1 |    0     |    1      | Reset |
| 1 | 0 |    1     |    0      | Set   |
| 1 | 1 |    0     |    0      | Invalid |

**Issue**: When S=R=1, both outputs become 0, violating the complementary property.

#### 4.1.2 D Latch (Data Latch)

Eliminates the invalid state of SR latch by using a single data input.

**Truth Table**:

| D | Enable | Q (next) |
|---|--------|----------|
| 0 |   1    |    0     |
| 1 |   1    |    1     |
| X |   0    |    Q     |

**Characteristic Equation**: Q(next) = D · Enable + Q · Enable'

### 4.2 Flip-Flops

Flip-flops are edge-triggered memory elements. Output changes only at the rising or falling edge of the clock signal.

#### 4.2.1 D Flip-Flop

**Truth Table**:

| D | Clock (↑) | Q (next) |
|---|-----------|----------|
| 0 |   Rising |    0     |
| 1 |   Rising |    1     |

**Characteristic Equation**: Q(next) = D

**Timing Diagram**:
```
Clock:     ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
           │   │   │   │   │   │   │   │   │   │   │
           │   │   │   │   │   │   │   │   │   │   │
         ──┘   └───┘   └───┘   └───┘   └───┘   └───
              ↑       ↑       ↑
              
D:        ────────────┬───────────┬──────────────
                      │           │
                      │           │
Q:              ┌─────┘     ┌─────┘
                │           │
                │           │
              ──┴───────────┴──────────────────
```

#### 4.2.2 JK Flip-Flop

**Truth Table**:

| J | K | Clock (↑) | Q (next) |
|---|---|-----------|----------|
| 0 | 0 |  Rising   |    Q     (Hold) |
| 0 | 1 |  Rising   |    0     (Reset) |
| 1 | 0 |  Rising   |    1     (Set)  |
| 1 | 1 |  Rising   |    Q'    (Toggle) |

**Characteristic Equation**: Q(next) = J·Q' + K'·Q

#### 4.2.3 T Flip-Flop

**Truth Table**:

| T | Clock (↑) | Q (next) |
|---|-----------|----------|
| 0 |  Rising   |    Q     (Hold) |
| 1 |  Rising   |    Q'    (Toggle) |

**Characteristic Equation**: Q(next) = T ⊕ Q

### 4.3 Flip-Flop Timing Parameters

Understanding timing parameters is crucial for proper circuit operation:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Setup Time | t_su | Minimum time input must be stable before clock edge |
| Hold Time | t_h | Minimum time input must be stable after clock edge |
| Propagation Delay | t_p | Time for output to change after input/clock edge |
| Clock-to-Q Delay | t_co | Time for Q to change after clock edge |
| Maximum Clock Frequency | f_max | 1 / (t_su + t_co + t_p) |

**Timing Diagram showing setup and hold violations**:
```
Valid Setup Time:
Clock:    ┌───┐         ┌───┐
          │   │         │   │
        ──┘   └─────────┘   └─
              ↑            ↑
D:         ┌──┴──┐      ┌──┴──┐
          ─┘     └──────┘     └─
             t_su  ↑
             
Hold Time Violation (D changes too soon after clock):
Clock:    ┌───┐         
          │   │         
        ──┘   └─────────
              ↑         
D:         ──┴──┐  ← Changes within hold time!
              ↑│
```

### 4.4 Registers

A register is a group of flip-flops used to store binary information.

#### 4.4.1 4-bit Parallel Load Register

```vhdl
-- 4-bit Register with Parallel Load
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Register_4bit is
    Port ( Data_in : in STD_LOGIC_VECTOR(3 downto 0);
           Load : in STD_LOGIC;
           Clock : in STD_LOGIC;
           Data_out : out STD_LOGIC_VECTOR(3 downto 0));
end Register_4bit;

architecture Behavioral of Register_4bit is
begin
    process(Clock)
    begin
        if (Clock'event and Clock = '1') then
            if (Load = '1') then
                Data_out <= Data_in;
            end if;
        end if;
    end process;
end Behavioral;
```

#### 4.4.2 Shift Register

**Types**:
- SISO (Serial In Serial Out)
- SIPO (Serial In Parallel Out)
- PISO (Parallel In Serial Out)
- PIPO (Parallel In Parallel Out)

### 4.5 Counters

Counters are sequential circuits that cycle through a predetermined sequence of states.

#### 4.5.1 3-bit Asynchronous (Ripple) Counter

```
Clock → FF0 → FF1 → FF2 → Output
         ↓      ↓
        Q0     Q1      Q2
```

**Timing Diagram**:
```
Clock:  ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
        │ │   │ │   │ │   │ │   │ │   │ │   │ │   │ │
      ──┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘

Q0:     ──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──
        │ │  │ │  │ │  │ │  │ │  │ │  │ │  │ │

Q1:     ─────┐   ┌──┐   ┌──┐   ┌──┐   ┌──┐   ┌──
            │   │  │   │  │   │  │   │  │   │

Q2:     ─────────┐       ┌──┐       ┌──┐       ┌─
                │       │  │       │  │       │

Decimal: 0  1  2  3  4  5  6  7  0  1  2  3  4  5  6
```

**Problem**: Ripple counters have propagation delay accumulation (ripple effect).

#### 4.5.2 3-bit Synchronous Counter

All flip-flops receive clock simultaneously, eliminating ripple delay.

**Design using JK flip-flops**:
- FF0: J=K=1 (toggles every clock)
- FF1: J=K=Q0 (toggles when Q0=1)
- FF2: J=K=Q0·Q1 (toggles when Q0=Q1=1)

```vhdl
-- 3-bit Synchronous Counter
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Sync_Counter_3bit is
    Port ( Clock : in STD_LOGIC;
           Reset : in STD_LOGIC;
           Q : out STD_LOGIC_VECTOR(2 downto 0));
end Sync_Counter_3bit;

architecture Behavioral of Sync_Counter_3bit is
    signal Q_temp : STD_LOGIC_VECTOR(2 downto 0) := "000";
begin
    process(Clock, Reset)
    begin
        if (Reset = '1') then
            Q_temp <= "000";
        elsif (Clock'event and Clock = '1') then
            Q_temp(0) <= NOT Q_temp(0);
            Q_temp(1) <= Q_temp(1) XOR Q_temp(0);
            Q_temp(2) <= Q_temp(2) XOR (Q_temp(0) AND Q_temp(1));
        end if;
    end process;
    Q <= Q_temp;
end Behavioral;
```

---

## 5. Finite State Machines (FSM)

### 5.1 Mealy Machine vs Moore Machine

#### 5.1.1 Mealy Machine

**Definition**: Output depends on both current state and current input.

**Model**:
```
    Input →  [Next State  ] → [Output]
             [   Logic    ]   [ Logic ]
                   ↑
                   │
             [State Memory]
                   │
              Clock/Reset
```

**Characteristics**:
- Output: Z = f(X, Q)
- Next State: Q+ = g(X, Q)
- Fewer states potentially required
- Output may change asynchronously with input

#### 5.1.2 Moore Machine

**Definition**: Output depends only on current state.

**Model**:
```
    Input →  [Next State  ] → [Output]
             [   Logic    ]   [ Logic ]
                   ↑             ↑
                   │             │
             [State Memory]──────┘
                   │
              Clock/Reset
```

**Characteristics**:
- Output: Z = f(Q)
- Next State: Q+ = g(X, Q)
- More states potentially required
- Output changes synchronously with state

### 5.2 Example: Sequence Detector (Mealy Machine)

**Problem**: Design a Mealy machine to detect the sequence "101" with overlapping.

**State Diagram (Mealy)**:
```
    S0(00) ──0──→ S0
      │          1↓        0↓         1↓
      │          ↓         ↓          ↓
    1│         S1         S2         S3
      │         ↓          ↓         ↓
      │0        ↓1         ↓0        ↓1
      ↓        S0         S1         S0(output)
```

**State Table**:

| Present State | Input | Next State | Output |
|---------------|-------|------------|--------|
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S2 | 0 |
| S1 | 1 | S1 | 0 |
| S2 | 0 | S0 | 0 |
| S2 | 1 | S3 | 1 |

**Excitation Table (using D flip-flops)**:

| Present State | Input | Next State | D (Next Q) |
|---------------|-------|------------|------------|
| 00 | 0 | 00 | 0 |
| 00 | 1 | 01 | 1 |
| 01 | 0 | 10 | 0 |
| 01 | 1 | 01 | 1 |
| 10 | 0 | 00 | 0 |
| 10 | 1 | 00 | 0 |

### 5.3 Example: Traffic Light Controller (Moore Machine)

**Problem**: Design a 3-state traffic light controller for a busy highway and a farm road intersection.

**States**:
- S0: Green for Highway, Red for Farm (Duration: 60s)
- S1: Yellow for Highway, Red for Farm (Duration: 10s)
- S2: Red for Highway, Green for Farm (Duration: 30s)

**State Table**:

| Present State | Highway Light | Farm Light |
|---------------|---------------|-------------|
| S0 | Green | Red |
| S1 | Yellow | Red |
| S2 | Red | Green |

---

## 6. Synchronous vs Asynchronous Sequential Circuits

### 6.1 Asynchronous Sequential Circuits

- No global clock signal
- Output changes as soon as input changes
- Also called "fundamental mode" circuits
- Faster than synchronous (no clock delay)
- More susceptible to hazards and races
- Used in: Fast interrupt circuits, simple control logic

**Race Condition Example**:
```
Two paths to change state:
Path 1: A → B → Final (delay: 10ns)
Path 2: A → C → Final (delay: 15ns)

Result: Circuit may enter wrong intermediate state
```

### 6.2 Synchronous Sequential Circuits

- Uses a global clock signal
- All state changes occur at clock edges
- Easier to design and debug
- Less susceptible to hazards
- Used in: Counters, registers, processors, memory

**Comparison Table**:

| Aspect | Synchronous | Asynchronous |
|--------|-------------|--------------|
| Clock | Required | Not required |
| Speed | Limited by clock | Faster |
| Design | Easier | Complex |
| Hazards | Minimal | Significant |
| Power | Higher (clock switching) | Lower |
| Testability | Easier | Difficult |

---

## 7. Propagation Delay and Performance

### 7.1 Understanding Propagation Delay

Propagation delay (t_p) is the time taken for a change in input to produce a change in output.

**Types**:
- **t_pHL**: High-to-Low propagation delay
- **t_pLH**: Low-to-High propagation delay

**Formula for Maximum Operating Frequency**:

For a synchronous counter:
```
f_max = 1 / (t_co + t_su + t_p(comb))
```

Where:
- t_co = Clock-to-Q delay
- t_su = Setup time
- t_p(comb) = Propagation delay of combinational logic

### 7.2 Critical Path Analysis

The **critical path** is the longest path through a circuit that determines maximum speed.

**Example - 4-bit adder**:
```
Ripple Carry: Path = FA0 → FA1 → FA2 → FA3
t_critical = 4 × t_p(FA) = 4 × 20ns = 80ns
f_max ≈ 12.5 MHz

Carry Look-Ahead: t_critical = t_p(CLA) ≈ 25ns  
f_max ≈ 40 MHz
```

---

## 8. Assessment Section

### 8.1 Application-Based Questions

**Question 1**: Design a 4:1 multiplexer using only 2:1 multiplexers. Show the circuit diagram and verify the truth table.

**Question 2**: A digital system requires counting from 0 to 99. Design the circuit using two decade counters. What is the maximum clock frequency if each flip-flop has t_co = 10ns and t_su = 5ns?

**Question 3**: Convert the following Mealy machine to an equivalent Moore machine:
- Mealy: Output Z=1 when input X=1 and current state is S1

**Question 4**: Analyze the timing diagram and identify setup/hold time violations:
```
Clock:    ┌───┐   ┌───┐   ┌───┐
          │   │   │   │   │
        ──┘   └───┘   └───┘   ↑
        D: ───────┘└────┘└──────────
```

**Question 5**: Design a synchronous mod-6 counter using JK flip-flops. Write the state table, excitation table, and derive the equations.

### 8.2 Analytical Questions

**Question 1**: Compare the advantages and disadvantages of ripple carry adders versus carry look-ahead adders. Under what circumstances would you choose each?

**Question 2**: Explain the concept of "race condition" in asynchronous sequential circuits. How can it be avoided?

**Question 3**: Derive the characteristic equation for a JK flip-flop and show how it can be converted to D, T, and SR flip-flops.

**Question 4**: Why do synchronous sequential circuits use edge-triggered flip-flops rather than level-triggered latches for storage elements?

### 8.3 Multiple Choice Questions

1. **Which of the following is NOT a combinational circuit?**
   - (a) Multiplexer
   - (b) Decoder
   - (c) Flip-flop
   - (d) Comparator

2. **The output of a Mealy machine depends on:**
   - (a) Present state only
   - (b) Present input only
   - (c) Present state and present input
   - (d) Clock signal only

3. **In a 4-bit ripple counter, the maximum propagation delay is:**
   - (a) 4 × t_ff
   - (b) 2 × t_ff
   - (c) t_ff
   - (d) 16 × t_ff

4. **A JK flip-flop with J=K=1 operates as:**
   - (a) D flip-flop
   - (b) T flip-flop
   - (c) SR flip-flop
   - (d) Toggle flip-flop

5. **The main advantage of synchronous circuits over asynchronous is:**
   - (a) Higher speed
   - (b) Less power consumption
   - (c) Freedom from race conditions
   - (d) Simpler design

---

## 9. Key Takeaways

### 9.1 Combinational Circuits
- Output depends only on current inputs
- No memory elements
- Examples: Adders, Subtractors, MUX, DEMUX, Encoders, Decoders, Comparators
- Fundamental building blocks of ALU

### 9.2 Sequential Circuits
- Output depends on current inputs AND stored state
- Contains memory elements (latches/flip-flops)
- Requires clock signal for synchronization
- Types: Synchronous (clocked) and Asynchronous (fundamental mode)

### 9.3 Flip-Flops
- **D Flip-Flop**: Data storage, Q(next) = D
- **JK Flip-Flop**: Universal flip-flop, toggle capability
- **T Flip-Flop**: Simple toggle, Q(next) = T ⊕ Q
- **SR Flip-Flop**: Set-Reset functionality

### 9.4 State Machines
- **Mealy**: Output depends on state + input, fewer states
- **Moore**: Output depends on state only, more states
- Design involves: State diagram → State table → Excitation table → Circuit

### 9.5 Timing Analysis
- Setup time (t_su): Input stable before clock
- Hold time (t_h): Input stable after clock
- Propagation delay (t_p): Signal transition time
- Critical path determines maximum clock frequency

### 9.6 Practical Considerations
- Synchronous circuits preferred for complex systems
- Asynchronous useful for simple, fast control
- Propagation delay affects circuit performance
- Race conditions must be avoided in design

---

## References (Delhi University Syllabus Alignment)

This content covers the following units from the BSc (Hons) Computer Science NEP 2024 UGCF syllabus:

- Unit I: Fundamentals of Digital Circuits
- Unit II: Combinational Logic Design
- Unit III: Sequential Logic Design
- Unit IV: Finite State Machines
- Unit V: Timing and Synchronization

**Suggested Reading**:
1. Morris Mano, "Digital Design" - Pearson Publications
2. Thomas Floyd, "Digital Fundamentals" - Pearson Publications
3. Delhi University Practical Manual for Computer System Architecture

---

*End of Study Material*