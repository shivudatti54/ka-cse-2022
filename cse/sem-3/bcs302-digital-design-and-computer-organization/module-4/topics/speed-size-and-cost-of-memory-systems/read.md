# Speed, Size and Cost of Memory Systems

## Introduction

The fundamental challenge in computer memory design arises from the inherent contradictions among three critical performance parameters: **speed** (access latency), **capacity** (storage size), and **cost** (economic expenditure per bit). A processor executes instructions at nanosecond timescales, requiring data and instructions to be delivered with minimal delay. Simultaneously, modern software demands gigabytes to terabytes of storage for operating systems, applications, and datasets. Economically, memory costs must remain within reasonable bounds for consumer and enterprise computing.

The **triple trade-off** states that no single memory technology can simultaneously achieve optimal speed, capacity, and cost. This principle, rooted in physical and economic constraints, necessitates a sophisticated design approach: the **memory hierarchy**. This chapter analyzes the theoretical foundations, quantitative relationships, and engineering solutions that enable modern computer systems to approximate the ideal of fast, large, and inexpensive memory.

## Theoretical Foundation: The Speed-Size-Cost Trade-off

The interdependency among speed, size, and cost stems from both physical limitations and economic factors:

### Physical Constraints

1. **Access Time vs. Capacity**: Faster memory technologies (e.g., SRAM) require more complex circuitry per storage cell, limiting the number of cells that can be fabricated on a given silicon area.

2. **Power Consumption**: Higher speed operation requires greater power dissipation, constraining the feasible size of fast memories.

3. **Volatility vs. Density**: Non-volatile storage technologies (magnetic, flash) sacrifice access speed for data retention without power.

### Economic Constraints

The cost per bit ($C$) of memory follows an approximately inverse relationship with access time ($T_a$) and density:

$$C \propto \frac{1}{T_a \times D}$$

Where $D$ represents the storage density (bits per unit area).

### Quantitative Comparison of Memory Technologies

| Parameter            | SRAM (Cache)  | DRAM (Main Memory) | NAND Flash    | Magnetic Disk    |
| -------------------- | ------------- | ------------------ | ------------- | ---------------- |
| **Cell Complexity**  | 6 transistors | 1T + 1C            | 1 transistor  | 1 bit (magnetic) |
| **Access Time**      | 0.5–2 ns      | 50–100 ns          | 25–100 μs     | 5–15 ms          |
| **Refresh Required** | No            | Yes (64 ms)        | No            | No               |
| **Typical Capacity** | 64 KB – 32 MB | 4–64 GB            | 256 GB – 4 TB | 1–20 TB          |
| **Cost per GB**      | $5000–10000   | $3–8               | $0.03–0.10    | $0.02–0.05       |
| **Power per GB**     | High          | Medium             | Low           | Medium           |

## SRAM: Static Random Access Memory

### Circuit Structure and Operation

SRAM stores each bit using a **flip-flop** circuit comprising **six transistors** (4 transistors forming two cross-coupled inverters + 2 access transistors). This bistable circuit has two stable states representing logical '0' and '1'.

**Why SRAM is Faster Than DRAM:**

The absence of capacitive charging/discharging is the primary speed advantage:

1. **No Charge Transfer**: Unlike DRAM, SRAM does not charge or discharge a capacitor to store data. The voltage levels transition through the inverter chain without waiting for capacitor settle time ($RC$ delay).

2. **Direct Amplification**: The cross-coupled inverters provide immediate signal restoration, achieving full voltage swing in minimal time.

3. **No Refresh Overhead**: DRAM requires periodic refresh cycles (typically every 64 ms), consuming 15–30% of memory bandwidth. SRAM operates continuously at full bandwidth.

The access time of SRAM can be estimated from transistor-level RC modeling:

$$T_{access} \approx k \cdot (R_{on} \cdot C_{parasitic})$$

Where $k$ is a process-dependent constant, $R_{on}$ is the transistor on-resistance, and $C_{parasitic}$ encompasses junction and routing capacitance.

### Applications

SRAM is exclusively deployed in **on-chip and off-chip cache memories** (L1, L2, L3) where access latency critically impacts processor performance.

## DRAM: Dynamic Random Access Memory

### Circuit Structure and Operation

DRAM stores each bit as charge on a **capacitor** (typically 20–30 femtofarads), controlled by a single access transistor. This minimal cell structure enables 4–6× greater density than SRAM.

**The Refresh Requirement:**

The capacitor exhibits leakage current ($I_{leak}$), causing stored charge to dissipate according to:

$$V(t) = V_0 \cdot e^{-t/RC}$$

Where $RC$ is the time constant (typically 10–100 ms). To maintain data integrity, the capacitor voltage must be periodically refreshed:

$$t_{refresh} < \frac{V_{threshold} \cdot C}{I_{leak}}$$

Modern DRAM requires refresh intervals of 64 ms at typical operating temperatures.

### Performance Implications

The access time for DRAM comprises:

1. **Row activation** (RAS): 15–20 ns
2. **Column access** (CAS): 10–15 ns
3. **Precharge**: 10–15 ns
4. **Total cycle time**: 50–100 ns

## The Memory Hierarchy: Quantitative Analysis

The memory hierarchy exploits **locality of reference** to approximate ideal memory characteristics. Each level ($L_i$) possesses:

- **Access time** ($T_i$): Latency to retrieve data
- **Capacity** ($S_i$): Storage capacity in bytes
- **Cost per bit** ($C_i$): Economic cost normalized to bits

The hierarchy typically follows:

```
CPU Core → L1 Cache (SRAM) → L2 Cache (SRAM) → L3 Cache (SRAM)
 → Main Memory (DRAM) → SSD (NAND) → HDD (Magnetic)
```

### Quantitative Hierarchy Parameters

| Level       | Technology | $T_i$ (latency) | Typical $S_i$ | $C_i$ ($/GB) |
| ----------- | ---------- | --------------- | ------------- | ------------ |
| Register    | Flip-flop  | 0.25–0.5 ns     | 256 B         | $10^6$       |
| L1 Cache    | SRAM       | 1–2 ns          | 32–64 KB      | $5000$       |
| L2 Cache    | SRAM       | 3–10 ns         | 256 KB–1 MB   | $2500$       |
| L3 Cache    | SRAM       | 10–20 ns        | 2–32 MB       | $1000$       |
| Main Memory | DRAM       | 50–100 ns       | 4–64 GB       | $5$          |
| SSD         | NAND Flash | 25–100 μs       | 256 GB–4 TB   | $0.08$       |
| HDD         | Magnetic   | 5–15 ms         | 1–20 TB       | $0.03$       |

## Principle of Locality: Theoretical Basis

The memory hierarchy succeeds due to **locality of reference**, a well-documented property of application programs:

### Temporal Locality

Recently accessed memory locations exhibit high probability of re-accession within a short time interval. Formally:

$$P(X_{t+1} = X_t | X_t \text{ accessed}) > P(X_{t+1} = X_t)$$

This property arises from:

- Loop variables iterated repeatedly
- Function call stacks
- Frequently accessed data structures

### Spatial Locality

Memory accesses exhibit spatial correlation:

$$P(|X_{t+1} - X_t| < \delta | X_t \text{ accessed}) \gg P(|X_{t+1} - X_t| < \delta)$$

Causes include:

- Sequential instruction execution
- Array/structure element access
- Sequential file I/O

**Empirical Evidence**: Studies show temporal locality exhibits decay constant $\tau \approx 10^3$ instructions, while spatial locality shows correlation distance $d \approx 10$ bytes for sequential access patterns.

## Cache Memory: Performance Modeling

### Hit Rate and Miss Rate

For a cache level with hit rate $h$ and miss rate $(1-h)$:

- **Hit**: Data retrieved from cache in $T_{cache}$ time
- **Miss**: Data fetched from next hierarchy level in $T_{next}$ time

### Average Memory Access Time (AMAT)

The **Average Memory Access Time** for a two-level hierarchy is derived as:

$$AMAT = T_{cache} + (1 - h) \times T_{miss}$$

Where $T_{miss}$ represents the penalty incurred on a cache miss (time to fetch from next level).

**Proof of AMAT Derivation:**

Let total memory accesses = $N$. Hits = $hN$, Misses = $(1-h)N$.

Total access time = $hN \cdot T_{cache} + (1-h)N \cdot T_{next}$

Dividing by $N$:

$$AMAT = h \cdot T_{cache} + (1-h) \cdot T_{next}$$

Since $T_{cache} \ll T_{next}$, we approximate $T_{cache} \approx 0$ for the miss penalty component:

$$AMAT = T_{cache} + (1-h) \cdot (T_{next} - T_{cache})$$

Defining miss penalty $MP = T_{next} - T_{cache}$:

$$\boxed{AMAT = T_{cache} + (1-h) \times MP}$$

### Multi-Level AMAT

For a three-level hierarchy:

$$AMAT = T_{L1} + (1-h_{L1}) \times [T_{L2} + (1-h_{L2}) \times MP_{L2}]$$

**Numerical Example:**

Given:

- L1 Cache: $T_{L1}$ = 1 ns, $h_{L1}$ = 95%
- L2 Cache: $T_{L2}$ = 10 ns, $h_{L2}$ = 90%
- Main Memory: $T_{MM}$ = 80 ns

Miss penalties:

- $MP_{L1} = T_{L2} + (1-h_{L2}) \times T_{MM} = 10 + 0.1 \times 80 = 18$ ns
- $AMAT = 1 + 0.05 \times 18 = 1.9$ ns

**Interpretation**: The effective access time (1.9 ns) approaches L1 cache speed while utilizing the full main memory capacity.

## Cost-Performance Optimization

### Effective Cost Per Bit

For a two-level system with cache ($S_1$, $C_1$) and main memory ($S_2$, $C_2$):

$$C_{effective} = \frac{C_1 S_1 + C_2 S_2}{S_1 + S_2}$$

**Derivation**: Since $S_2 \gg S_1$ in practical systems ($S_2 / S_1 \approx 10^4$):

$$C_{effective} \approx C_2 \left(1 + \frac{S_1}{S_2}\left(\frac{C_1}{C_2} - 1\right)\right)$$

For $C_1 / C_2 = 1000$ and $S_1 / S_2 = 10^{-4}$:

$$C_{effective} \approx C_2 (1 + 0.1 - 0.0001) \approx 1.1 C_2$$

This demonstrates that the hierarchy achieves cache-level performance at near-main-memory cost.

### Design Optimization Problem

The optimal cache size $S_{opt}$ balances cost and performance:

$$\text{Minimize: } Cost(S) = C_1 S + C_2 S_{total}$$
$$\text{Subject to: } Performance(S) = AMAT(S) \leq AMAT_{target}$$

This constrained optimization yields diminishing returns beyond certain cache sizes due to the exponential decay of locality benefits.

## Key Theoretical Takeaways

1. **Trade-off Fundamental**: The relationship $C \cdot T_a \cdot D = \text{constant}$ represents the fundamental physical-economic constraint; any improvement in one parameter necessitates degradation in others.

2. **SRAM vs. DRAM**: The 6-transistor SRAM cell provides explicit state storage (no refresh) but at 4–6× area penalty; DRAM's 1T+1C cell achieves density at the cost of refresh overhead and longer access latency.

3. **Hierarchy Effectiveness**: The theoretical hit rate threshold for hierarchy benefit is $h > 1 - (T_{cache} / T_{next})$; for $T_{cache} = 1$ ns and $T_{next} = 100$ ns, any hit rate exceeding 1% justifies cache implementation.

4. **Locality Exploitation**: Temporal locality mandates small, fast caches; spatial locality justifies block transfer (cache lines typically 64 bytes).

5. **AMAT as Design Metric**: Average Memory Access Time provides the fundamental metric for hierarchy optimization, directly correlating with processor CPI (cycles per instruction).

## Assessment Items

### Hard Level Questions

**Question 1**: A processor has L1 cache with 1 ns access time and 95% hit rate, and L2 cache with 10 ns access time and 90% L1 miss rate. Main memory access requires 100 ns. Calculate the AMAT and determine the effective speedup compared to direct main memory access.

**Question 2**: Given a memory system with cache cost of $5000/GB and main memory cost of $5/GB, where the cache is 1 MB and main memory is 8 GB, calculate the average cost per bit of the hierarchical system. Compare this to the cost if only main memory were used.

**Question 3**: Prove that for a two-level memory hierarchy with access times $T_1$ and $T_2$ ($T_1 < T_2$) and hit rate $h$, the AMAT is always less than or equal to $T_2$, with equality only when $h = 0$.

**Question 4**: A DRAM chip requires refresh every 64 ms. If each row must be refreshed within 64 ms and there are 8192 rows, calculate the minimum refresh interval per row. If one refresh cycle takes 100 ns, what fraction of memory bandwidth is consumed by refresh operations at a memory cycle time of 10 ns?
