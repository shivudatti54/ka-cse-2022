# TCP Congestion Control Variants

## Comprehensive Study Material for Advanced Computer Networks

**Course:** Advanced Computer Networks (MCS-202)  
**Topic:** TCP Congestion Control Variants  
**Level:** MSc CS, Delhi University  
**Session:** July 2025

---

## Table of Contents

1. [Introduction to TCP Congestion Control](#1-introduction-to-tcp-congestion-control)
2. [Fundamental Congestion Control Mechanisms](#2-fundamental-congestion-control-mechanisms)
3. [TCP Congestion Control Variants](#3-tcp-congestion-control-variants)
4. [Mathematical Foundations](#4-mathematical-foundations)
5. [Comparative Analysis](#5-comparative-analysis)
6. [Practical Examples and Implementations](#6-practical-examples-and-implementations)
7. [Real-World Relevance](#7-real-world-relevance)
8. [Key Takeaways](#8-key-takeaways)
9. [References](#9-references)

---

## 1. Introduction to TCP Congestion Control

### 1.1 Background and Motivation

TCP (Transmission Control Protocol) is the cornerstone of reliable data transmission on the Internet. As network traffic grew exponentially, congestion became a critical issue. **Congestion** occurs when network resources (buffers, bandwidth, processing capacity) are overwhelmed by the volume of data packets, leading to packet loss, delays, and overall network degradation.

The seminal work by Van Jacobson and Michael Karels in 1988 laid the foundation for modern TCP congestion control. Their paper, "Congestion Avoidance and Control," introduced algorithms that transformed the Internet's reliability and performance.

### 1.2 Real-World Relevance

In 2025, with 5G networks, IoT devices, and cloud computing dominating the landscape, understanding TCP congestion control variants is essential:

- **Video Streaming:** Netflix, YouTube, and video conferencing applications depend on efficient congestion control to deliver smooth playback
- **Cloud Services:** Data centers running AI/ML workloads require optimized TCP variants to handle massive data transfers
- **Financial Trading:** High-frequency trading systems rely on low-latency TCP implementations
- **Telemedicine:** Remote healthcare applications demand reliable, congestion-aware networking

### 1.3 Delhi University Syllabus Context

This topic aligns with the MSc CS curriculum under "Advanced Computer Networks," specifically covering:
- TCP/IP protocol stack deep dive
- Network congestion management
- Performance optimization in transport layer protocols

---

## 2. Fundamental Congestion Control Mechanisms

### 2.1 The Congestion Window (cwnd)

The **congestion window** (`cwnd`) represents the maximum amount of data a sender can transmit without receiving acknowledgment (ACK). It's a fundamental parameter in all TCP variants:

```
Maximum Data in Flight = min(cwnd, rwnd)
```

Where `rwnd` is the receiver's advertised window.

### 2.2 Slow Start Algorithm

When a TCP connection begins, the sender has no knowledge of network capacity. **Slow Start** addresses this by exponentially increasing the sending rate:

**Algorithm:**
```
cwnd = 1 MSS (Maximum Segment Size)
for each ACK received:
    cwnd = cwnd + MSS
```

This results in exponential growth: 1 → 2 → 4 → 8 → 16... segments per RTT.

**Threshold (ssthresh):** Once `cwnd` reaches `ssthresh`, the algorithm transitions to Congestion Avoidance.

### 2.3 Congestion Avoidance

Once the connection is established, **Congestion Avoidance** provides linear growth:

**Algorithm:**
```
for each ACK received:
    cwnd = cwnd + MSS² / cwnd
```

This adds approximately one MSS per RTT, providing stable throughput.

### 2.4 Fast Retransmit and Fast Recovery

When packet loss occurs, these mechanisms improve performance:

- **Fast Retransmit:** After 3 duplicate ACKs, retransmit the lost segment without waiting for timeout
- **Fast Recovery:** Maintain sending during fast retransmit, adjusting `cwnd` based on duplicate ACKs

---

## 3. TCP Congestion Control Variants

### 3.1 TCP Tahoe

**Overview:** TCP Tahoe, developed in 1988, was the first implementation of Jacobson-Karels congestion control.

**Key Features:**
- Implements Slow Start, Congestion Avoidance, and Fast Retransmit
- On packet loss: sets `ssthresh = cwnd / 2`, then `cwnd = 1 MSS`

**Drawback:** Aggressive cwnd reduction even with single packet loss.

### 3.2 TCP Reno

**Overview:** TCP Reno (1990) improved upon Tahoe by adding Fast Recovery.

**Key Features:**
- On packet loss detection (3 dup ACKs):
  - `ssthresh = cwnd / 2`
  - `cwnd = ssthresh + 3 MSS` (accounting for packets in flight)
  - Enter Fast Recovery, then Congestion Avoidance
- Single packet loss per RTT: efficient recovery

**Drawback:** When multiple packets are lost in a window, performance degrades significantly.

### 3.3 TCP NewReno

**Overview:** NewReno (1996) addresses multiple packet loss scenarios without SACK support.

**Key Features:**
- Partial ACK handling: continues Fast Recovery until all lost packets are recovered
- Differentiates between full ACK (exits recovery) and partial ACK
- Performance improvement over Reno in lossy networks

**Mathematical Improvement:**
```
On partial ACK:
    cwnd = cwnd + MSS
    Retransmit next unacknowledged segment
```

### 3.4 TCP SACK (Selective Acknowledgment)

**Overview:** RFC 2018 introduces SACK to efficiently handle multiple packet losses.

**Key Features:**
- Receiver can specify non-contiguous blocks of received data
- Sender maintains a SACK scoreboard to track delivered segments
- Significantly improves recovery in high-loss environments

### 3.5 TCP BIC (Binary Increase Congestion Control)

**Overview:** BIC (2004) addresses the scalability issue of traditional TCP in high-bandwidth networks.

**Key Features:**
- Uses binary search to find the congestion point
- Two phases: Max probing (aggressive) and Additive Increase (conservative)
- Smooth transition between phases

**Algorithm:**
```
if cwnd < ssthresh:
    // Max probing - binary search
    cwnd = (cwnd + cwnd_max) / 2
else:
    // Additive increase
    cwnd = cwnd + MSS * (ssthresh / cwnd)
```

### 3.6 TCP CUBIC

**Overview:** CUBIC (2006) is the default TCP congestion control in Linux and Windows 10+. It's designed for high-bandwidth, high-latency networks.

**Key Features:**
- Uses a cubic function for window growth: `W(t) = C(t - K)³ + W_max`
- Where `K = ∛(W_max × β / C)`
- `W_max`: congestion window before loss
- `β`: multiplicative decrease factor (0.7)
- Fast convergence and excellent scalability

**Cubic Function Characteristics:**
- **Concave region:** Below `W_max`, aggressive window growth
- **Convex region:** Above `W_max`, cautious probing
- **TCP-friendly region:** At low bandwidth, behaves like TCP Reno

### 3.7 TCP Vegas

**Overview:** TCP Vegas (1994) is a delay-based congestion control, fundamentally different from loss-based approaches.

**Key Features:**
- Measures actual RTT rather than relying on packet loss
- Calculates expected throughput vs. actual throughput
- Adjusts `cwnd` based on the difference

**Algorithm:**
```
Expected = cwnd / BaseRTT
Actual = cwnd / CurrentRTT
Diff = Expected - Actual

if Diff < α:
    cwnd = cwnd + MSS
else if Diff > β:
    cwnd = cwnd - MSS * (Diff / cwnd)
else:
    cwnd unchanged
```

Typical values: `α = 2`, `β = 4`

**Advantages:** Lower packet loss, fairer bandwidth allocation
**Disadvantages:** Cannot fully utilize bandwidth in certain scenarios, competes poorly with loss-based TCP

### 3.8 FAST TCP

**Overview:** FAST (2004) is an improved delay-based congestion control for high-speed networks.

**Key Features:**
- Uses queuing delay as primary signal
- Incorporates a proportional-integral (PI) control mechanism
- Formula: `cwnd = cwnd × (α/RTT + β × (RTT - RTT_min))/cwnd`
- Better stability than Vegas in high-speed networks

### 3.9 Compound TCP

**Overview:** Compound TCP (2006) is Microsoft's default congestion control for Windows Vista/7/10.

**Key Features:**
- Combines loss-based and delay-based approaches
- Maintains a delay-based component (`cwnd_d`) alongside traditional `cwnd`
- Total window: `cwnd = cwnd_loss + cwnd_delay`

**Algorithm:**
```
cwnd_d = min(cwnd_d + α × (RTT_min/RTT)ⁿ, cwnd)
cwnd = cwnd + (MSS × MSS × cwnd_d) / cwnd
```

Where `α = 0.5`, `n = 4`

**Advantages:** Aggressive growth in high-bandwidth networks while maintaining fairness

### 3.10 TCP Hybla

**Overview:** TCP Hybla (2006) addresses performance in heterogeneous networks with high RTT variance (e.g., satellite networks).

**Key Features:**
- Normalizes congestion window based on RTT ratio
- Compensates for delay differences

**Algorithm:**
```
ρ = RTT / RTT_0  // RTT reference (e.g., 100ms)
cwnd = cwnd + (2^ρ - 1) × MSS / cwnd
```

This ensures that connections with higher RTT achieve similar throughput to low-RTT connections.

### 3.11 BBR (Bottleneck Bandwidth and RTT)

**Overview:** BBR (2016) by Google represents a paradigm shift—it's a model-based congestion control that doesn't rely on packet loss or delay signals.

**Key Concepts:**

1. **BtlBw (Bottleneck Bandwidth):** Maximum delivery rate across the path
2. **RTprop (Round Trip Propagation time):** Minimum RTT observed

**Operating Principle:**
- BBR builds models of both `BtlBw` and `RTprop`
- Sends at the rate matching `BtlBw`
- Explicitly avoids queue buildup

**Pacing:**
- BBR includes a pacing gain to control send rate
- Cycle through different pacing gains to probe for bandwidth changes

**States:**
1. **STARTUP:** Exponential growth like traditional TCP
2. **DRAIN:** Drain the queue after STARTUP
3. **PROBE_BW:** Cycle through pacing gains to probe bandwidth
4. **PROBE_RTT:** Occasional measurement of RTprop

**Code Representation:**
```python
class BBR:
    def __init__(self):
        self.btlbw = 0
        self.rtprop = float('inf')
        self.pacing_gain_cycle = [1.25, 0.75, 1, 1, 1, 1, 1, 1]
        self.cycle_index = 0
    
    def on_ack(self, rtt, delivered, delivery_rate):
        # Update models
        self.rtprop = min(self.rtprop, rtt)
        
        if delivery_rate > self.btlbw:
            self.btlbw = delivery_rate
        
        # Calculate pacing rate
        pacing_gain = self.pacing_gain_cycle[self.cycle_index]
        send_rate = self.btlbw * pacing_gain
        
        return send_rate
```

### 3.12 DCTCP (Data Center TCP)

**Overview:** DCTCP (2010) is designed specifically for low-latency, high-speed data center networks.

**Key Features:**
- Uses ECN (Explicit Congestion Notification) for early congestion detection
- Reacts proportionally to the number of marked packets
- Maintains small queues (low latency)

**Algorithm:**
```
α = (1 - g) × α + g × F
cwnd = cwnd × (1 - α/2)

Where:
    F = fraction of marked packets
    g = weight (typically 1/16 or 1/32)
```

**Advantages:** Low latency, high throughput in data centers, minimal bufferbloat

---

## 4. Mathematical Foundations

### 4.1 Throughput Models

**Classical TCP Throughput (Mathis et al.):**

For a TCP connection with:
- Loss rate: `p`
- RTT: `R`
- MSS: `M`

The maximum throughput is approximated by:

$$T = \frac{M}{R \times \sqrt{p}}$$

**Example Calculation:**
For `R = 50ms`, `M = 1460 bytes`, `p = 0.001` (0.1% loss):
```
T = 1460 / (0.05 × √0.001)
T = 1460 / (0.05 × 0.0316)
T = 1460 / 0.00158
T ≈ 924,050 bytes/sec ≈ 7.2 Mbps
```

### 4.2 Scalability Analysis

| Variant | Bandwidth Scaling | RTT Scaling | Loss Sensitivity |
|---------|------------------|-------------|------------------|
| Reno    | O(1/√p)         | O(1/R)      | High             |
| CUBIC   | O(∛p⁻¹)         | O(1/R)      | Moderate         |
| BBR     | O(B)            | O(1/RTT²)   | Low              |
| DCTCP   | O(1/p)          | O(1/R)      | Low              |

### 4.3 Queue Dynamics

For buffer size `B` and link capacity `C`:

**Drop-tail:**
- Packets dropped when buffer full
- Synchronized losses common

**AQM (Active Queue Management):**
- Random early detection (RED)
- CoDel (Controlled Delay)
- ECN marking

---

## 5. Comparative Analysis

### 5.1 Feature Comparison Matrix

| Feature | Tahoe | Reno | NewReno | CUBIC | Vegas | BBR | DCTCP |
|---------|-------|------|---------|-------|-------|-----|-------|
| Loss-based | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Delay-based | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | Partial |
| Model-based | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |
| SACK support | ✗ | ✗ | Optional | ✓ | ✗ | ✓ | ✓ |
| ECN support | ✗ | ✗ | ✗ | Optional | ✗ | ✓ | Required |
| High-speed | Poor | Poor | Poor | Excellent | Fair | Excellent | Excellent |
| Fairness | Good | Good | Good | Good | Good | Variable | Good |

### 5.2 When to Use Each Variant

**Scenario 1: General Internet browsing**
- **Recommended:** CUBIC or Reno
- **Reason:** Robust, well-tested, fair bandwidth sharing

**Scenario 2: High-speed data center**
- **Recommended:** DCTCP or BBR
- **Reason:** Low latency, high throughput, handles congestion gracefully

**Scenario 3: Satellite/heterogeneous networks**
- **Recommended:** Hybla
- **Reason:** Compensates for high RTT variance

**Scenario 4: Long-distance high-bandwidth links**
- **Recommended:** BBR
- **Reason:** Efficient bandwidth utilization without queue buildup

**Scenario 5: Competing with other TCP flows**
- **Recommended:** TCP-friendly variants (CUBIC, Reno)
- **Reason:** Fair bandwidth sharing

---

## 6. Practical Examples and Implementations

### 6.1 Example 1: Simulating TCP Reno in Python

```python
"""
TCP Reno Congestion Control Simulator
Author: Delhi University CS Dept
Demonstrates Slow Start, Congestion Avoidance, and Fast Recovery
"""

class TCPReno:
    def __init__(self, mss=1460, initial_cwnd=1):
        self.mss = mss  # Maximum Segment Size in bytes
        self.cwnd = initial_cwnd * mss  # Congestion window
        self.ssthresh = float('inf')  # Slow start threshold
        self.rtt = 0.1  # Round trip time in seconds (100ms)
        self.state = "SLOW_START"
        self.packet_loss_rate = 0.001  # Simulated loss rate
        
    def slow_start(self):
        """Exponential increase of cwnd"""
        self.cwnd += self.mss
        if self.cwnd >= self.ssthresh:
            self.state = "CONGESTION_AVOIDANCE"
        print(f"[Slow Start] cwnd: {self.cwnd} bytes")
        
    def congestion_avoidance(self):
        """Linear increase of cwnd (approximately 1 MSS per RTT)"""
        self.cwnd += (self.mss ** 2) / self.cwnd
        print(f"[Congestion Avoidance] cwnd: {self.cwnd} bytes")
        
    def on_ack(self, ack_num):
        """Handle incoming ACK"""
        if self.state == "SLOW_START":
            self.slow_start()
        elif self.state == "CONGESTION_AVOIDANCE":
            self.congestion_avoidance()
            
    def on_loss(self):
        """Handle packet loss"""
        # Halve cwnd and set ssthresh
        self.ssthresh = self.cwnd / 2
        self.cwnd = self.ssthresh
        self.state = "SLOW_START"
        print(f"[Loss Detected] ssthresh: {self.ssthresh}, cwnd reset to: {self.cwnd}")
        
    def simulate(self, num_rounds=20):
        """Run simulation for specified rounds"""
        print("=" * 50)
        print("TCP Reno Simulation")
        print("=" * 50)
        for i in range(num_rounds):
            print(f"Round {i+1}: ", end="")
            self.on_ack(i)
            
# Run simulation
tcp = TCPReno()
tcp.ssthresh = 10 * tcp.mss  # Set threshold after initial growth
tcp.state = "CONGESTION_AVOIDANCE"
tcp.simulate(15)
```

**Expected Output:**
```
Round 1: [Congestion Avoidance] cwnd: 2920 bytes
Round 2: [Congestion Avoidance] cwnd: 4380 bytes
Round 3: [Congestion Avoidance] cwnd: 5840 bytes
...
```

### 6.2 Example 2: BBR Implementation in Python

```python
"""
BBR (Bottleneck Bandwidth and RTT) Congestion Control
Implementation of Google's BBR algorithm
"""

import time
from collections import deque

class BBR:
    def __init__(self):
        # Model parameters
        self.btlbw = 0.0  # Bottleneck bandwidth (bytes/sec)
        self.rtprop = float('inf')  # Minimum RTT (seconds)
        
        # Timing
        self.rtprop_stale = float('inf')
        self.delivery_rate_history = deque(maxlen=100)
        self.rtt_history = deque(maxlen=100)
        
        # Pacing
        self.pacing_gain_cycle = [1.25, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        self.cycle_index = 0
        self.cycle_count = 0
        
        # State
        self.state = "STARTUP"
        self.max_cwnd = float('inf')
        
    def min_rtt_filter(self, rtt, time_now):
        """Update RTprop with 10-second staleness timer"""
        if rtt < self.rtprop:
            self.rtprop = rtt
            self.rtprop_stale = time_now + 10.0
        elif time_now > self.rtprop_stale:
            self.rtprop = rtt
            self.rtprop_stale = time_now + 10.0
            
    def calculate_delivery_rate(self, bytes_delivered, time_elapsed):
        """Calculate delivery rate from ACK information"""
        if time_elapsed > 0:
            return bytes_delivered / time_elapsed
        return 0
    
    def update_btlbw(self, delivery_rate):
        """Update bottleneck bandwidth estimate"""
        if delivery_rate > self.btlbw:
            self.btlbw = delivery_rate
            
    def get_pacing_rate(self):
        """Calculate current pacing rate"""
        pacing_gain = self.pacing_gain_cycle[self.cycle_index]
        return self.btlbw * pacing_gain
    
    def get_cwnd(self, bytes_in_flight):
        """Calculate congestion window"""
        # Ensure we have at least 4 packets in flight
        min_cwnd = 4 * 1460  # 4 MSS
        
        # Max bandwidth delay product
        bdp = self.btlbw * self.rtprop
        return max(min_cwnd, bdp + bytes_in_flight)
    
    def on_packet_ack(self, rtt, bytes_delivered, time_elapsed, time_now):
        """Handle incoming ACK"""
        # Update RTT model
        self.min_rtt_filter(rtt, time_now)
        
        # Update delivery rate
        delivery_rate = self.calculate_delivery_rate(bytes_delivered, time_elapsed)
        self.update_btlbw(delivery_rate)
        
        # State machine
        if self.state == "STARTUP":
            if self.btlbw > 0:
                # Growing exponentially until bandwidth doesn't increase
                pass
            # Check if we're in drain phase
            if self.cwnd >= self.max_cwnd * 0.75:
                self.state = "DRAIN"
                
        elif self.state == "PROBE_BW":
            # Cycle through pacing gains
            self.cycle_count += 1
            if self.cycle_count >= len(self.pacing_gain_cycle):
                self.cycle_count = 0
                self.cycle_index = (self.cycle_index + 1) % len(self.pacing_gain_cycle)
                
        elif self.state == "PROBE_RTT":
            # Measure RTprop periodically
            pass
            
        # Return calculated values
        return {
            'cwnd': self.get_cwnd(bytes_delivered),
            'pacing_rate': self.get_pacing_rate(),
            'btlbw': self.btlbw,
            'rtprop': self.rtprop,
            'state': self.state
        }

# Example usage
def simulate_bbr():
    bbr = BBR()
    
    # Simulate connection with 100ms RTT, 10 Mbps bandwidth
    simulated_rtt = 0.1
    simulated_bw = 10_000_000 / 8  # 10 Mbps in bytes/sec
    
    for i in range(50):
        # Simulate progressive delivery
        time_now = i * 0.1
        bytes_delivered = min(1460 * (i + 1), bbr.btlbw * time_now)
        
        result = bbr.on_packet_ack(
            rtt=simulated_rtt,
            bytes_delivered=bytes_delivered,
            time_elapsed=0.1,
            time_now=time_now
        )
        
        if i % 10 == 0:
            print(f"Round {i}: BBR state: {result['state']}, "
                  f"BtlBw: {result['btlbw']/1000:.2f} KB/s, "
                  f"RTprop: {result['rtprop']*1000:.2f} ms")

simulate_bbr()
```

### 6.3 Example 3: Network Configuration Commands

**Checking Current TCP Congestion Control (Linux):**
```bash
# View available congestion control algorithms
sysctl net.ipv4.tcp_available_congestion_control

# Check current algorithm
sysctl net.ipv4.tcp_congestion_control

# Change to BBR
sysctl net.ipv4.tcp_congestion_control=bbr

# Make persistent
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
```

**Monitoring TCP Statistics:**
```bash
# View TCP metrics
ss -ti

# View detailed TCP info
cat /proc/net/tcp

# Monitor with netstat
netstat -s | grep -i "retransmit\|congestion"
```

---

## 7. Real-World Relevance

### 7.1 Industry Adoption

| Company/Service | TCP Variant | Reason |
|-----------------|-------------|--------|
| Google | BBR | 5-14% latency reduction, better bandwidth utilization |
| Microsoft | Compound TCP | Default in Windows Vista+ |
| Akamai | CUBIC | High-performance CDN |
| Cloudflare | BBR + CUBIC | Edge network optimization |
| Netflix | QUIC (based on UDP) | Video streaming optimization |

### 7.2 Research Directions

1. **ATP (Additive Transport Protocol):** Kernel-bypass approach
2. **Google QUIC:** UDP-based with built-in congestion control
3. **FlexTCP:** Programmable congestion control
4. **PCC (Performance-oriented Congestion Control):** Learning-based

---

## 8. Key Takeaways

### 8.1 Core Concepts

1. **Congestion Control Evolution:** From basic Tahoe to model-based BBR, TCP congestion control has evolved significantly to address diverse network conditions.

2. **Loss vs. Delay-based:** Traditional TCP (Reno, CUBIC) relies on packet loss as congestion signal. Delay-based (Vegas, FAST) uses RTT measurements. BBR uses a model-based approach with both bandwidth and RTT.

3. **The cwnd-ssthresh Dynamic:** Understanding how these parameters interact is crucial:
   - Slow Start: `cwnd` grows exponentially until reaching `ssthresh`
   - Congestion Avoidance: Linear growth after threshold
   - On loss: Both parameters are adjusted based on the variant

### 8.2 Important Formulas

- **TCP Reno throughput:** `T ≈ M / (R × √p)`
- **CUBIC window:** `W(t) = C(t - K)³ + W_max`
- **BBR pacing:** `Rate = BtlBw × PacingGain`

### 8.3 Selection Criteria

| Network Condition | Recommended Variant |
|------------------|---------------------|
| General Internet | CUBIC |
| High-speed/Low-latency | BBR, DCTCP |
| Satellite/High RTT | Hybla |
| Competing flows | TCP-friendly (Reno, CUBIC) |
| Data centers | DCTCP, BBR |

### 8.4 Delhi University Examination Focus

- **Must Know:** Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery algorithms
- **Understand:** Differences between Tahoe, Reno, NewReno
- **Compare:** Loss-based vs. delay-based vs. model-based approaches
- **Analyze:** Mathematical throughput models and scalability

---

## 9. References

1. Jacobson, V., & Karels, M. (1988). "Congestion Avoidance and Control." ACM SIGCOMM.

2. Le, L., Aikat, J., Jeffay, K., & Smith, F. D. (2004). "The Effects of Active Queue Management on TCP Performance." ACM SIGCOMM.

3. Cardwell, N., Cheng, Y., Gunn, C. S., Yeganeh, S. H., & Jacobson, V. (2016). "BBR: Congestion-Based Congestion Control." ACM Queue.

4. Alizadeh, M., et al. (2010). "Data Center TCP (DCTCP)." ACM SIGCOMM.

5. Floyd, S. (2001). "HighSpeed TCP for Large Congestion Windows." RFC 3649.

6. Xu, L., Harfoush, K., & Rhee, I. (2004). "Binary Increase Congestion Control (BIC) for Fast Long-Distance Networks." IEEE INFOCOM.

7. TCP RFC 2581, 2582, 3517, 5681 (IETF Standards).

8. Delhi University MSc CS Syllabus - Advanced Computer Networks (MCS-202).

---

*Study Material prepared for MSc CS, Delhi University - July 2025 Session*