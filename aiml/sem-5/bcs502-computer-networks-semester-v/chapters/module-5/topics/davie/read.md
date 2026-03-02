# Module 5: Traffic Engineering with Differentiated Services (DiffServ)

## Topic: Davie's Edge Mechanism for DiffServ

### 1. Introduction

In the realm of Quality of Service (QoS) for IP networks, the Differentiated Services (DiffServ) architecture provides a scalable mechanism for classifying and managing network traffic. While DiffServ defines the overall framework, it relies on specific algorithms implemented at network nodes to enforce its policies. One such crucial algorithm, often referenced in the context of traffic conditioning at the edge of a network, is **Davie's Edge Mechanism** (or the **Three-Color Marker**). This mechanism is a refined approach to the standard Single Rate Three Color Marker (srTCM) defined in RFC 2697. It plays a vital role in ensuring traffic conforms to a specified profile before it enters the core network.

### 2. Core Concepts Explained

Davie's mechanism is designed to meter and mark IP packets based on a Committed Information Rate (CIR) and two associated burst sizes: a Committed Burst Size (CBS) and an Excess Burst Size (EBS).

The algorithm uses a token bucket system with two buckets to categorize incoming packets into three colors, analogous to a traffic light:

*   **Green:** For traffic that is within the committed rate.
*   **Yellow:** For traffic that exceeds the committed rate but is within the excess burst limit.
*   **Red:** For traffic that exceeds both the committed and excess burst limits.

Here’s a breakdown of the key components and the process:

*   **Committed Information Rate (CIR):** The guaranteed, long-term average data rate agreed upon in a Service Level Agreement (SLA). Tokens are added to the buckets at this rate.
*   **Committed Burst Size (CBS):** The maximum number of bytes (or tokens) available for the first, committed bucket. It allows for short-term bursts above the CIR without violating the contract.
*   **Excess Burst Size (EBS):** The maximum number of bytes (or tokens) available for the second, excess bucket. It allows for even larger, but less guaranteed, bursts of traffic.

The mechanism operates with **two token buckets**:

1.  **Bucket C (Committed):** Holds tokens up to the CBS. This bucket is filled first with tokens arriving at the CIR.
2.  **Bucket E (Excess):** Holds tokens up to the EBS. Tokens are only added to this bucket *after* Bucket C is full.

**The Packet Marking Logic:**
For each incoming packet of size `B` bytes:
1.  If Bucket C has at least `B` tokens, the packet is marked **Green** (in-profile). The tokens are subtracted from Bucket C.
2.  Else, if Bucket E has at least `B` tokens, the packet is marked **Yellow** (excess burst). The tokens are subtracted from Bucket E.
3.  Else, if both buckets lack sufficient tokens, the packet is marked **Red** (out-of-profile). No tokens are consumed.

**Example:**
Imagine an SLA with a CIR of 1 Mbps, a CBS of 2000 bytes, and an EBS of 4000 bytes.
*   A steady stream of small packets within 1 Mbps will be marked Green, drawing tokens only from Bucket C.
*   A sudden burst of a 1500-byte packet will be marked Green if Bucket C has enough tokens.
*   If a subsequent 2000-byte packet arrives and Bucket C is empty but Bucket E has tokens, it will be marked Yellow.
*   A large 5000-byte video frame arriving when both buckets are nearly empty might be marked Red, indicating it should be eligible for dropping if the network is congested.

### 3. Key Points and Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Purpose** | To police and mark traffic at the network edge based on a CIR and two burst sizes. |
| **Method** | A two-bucket token system (CBS and EBS) fed by tokens at the CIR. |
| **Output** | Marks packets as Green (conforming), Yellow (exceeding CIR but within EBS), or Red (violating). |
| **Key Advantage** | Provides more granular control than a single-bucket system by allowing two levels of burst tolerance. |
| **RFC Standard** | Based on and very similar to the Single Rate Three Color Marker (srTCM) in RFC 2697. |
| **Network Role** | Primarily used by an Internet Service Provider (ISP) at the customer edge to enforce the SLA. |

**Summary:** Davie's Edge Mechanism is a practical implementation of a traffic conditioner in the DiffServ model. By using a dual token bucket system, it effectively classifies packets into three service classes. This allows core network routers to make simple and fast forwarding decisions (e.g., low loss for Green, higher potential loss for Yellow, and drop for Red during congestion) based on these packet markings, enabling scalable end-to-end QoS without maintaining per-flow state in the network core.