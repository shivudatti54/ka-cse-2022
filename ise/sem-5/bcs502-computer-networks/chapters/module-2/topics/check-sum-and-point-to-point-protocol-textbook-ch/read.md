# **Check Sum and Point to Point Protocol**

### Introduction

---

In a data communication system, errors can occur during data transmission due to various reasons such as signal degradation, noise, or interference. To detect and correct these errors, various error detection and correction techniques are used. Two popular techniques used in the data link layer are Check Sum and Point to Point Protocol.

### Check Sum

---

**Definition:** Check Sum is a mechanism used to detect errors in data transmission by calculating a digital signature of the data packet. This digital signature is then compared with the received Check Sum to determine if any errors occurred during transmission.

**How it works:**

1. The sender calculates the Check Sum of the data packet by summing up all the bits of the packet.
2. The sender sends the Check Sum along with the data packet.
3. The receiver calculates the Check Sum of the received data packet.
4. If the calculated Check Sum matches the received Check Sum, the data packet is considered error-free.

**Example:**

Suppose we have a data packet with the following bits: 11010110. The Check Sum of this packet is 6 (1+1+0+1+0+1+1+0). The sender sends this packet along with the Check Sum (6).

| Bit Position | Data Bit | Check Sum |
| ------------ | -------- | --------- |
| 1            | 1        | 1         |
| 2            | 1        | 1+1=2     |
| 3            | 0        | 2+0=2     |
| 4            | 1        | 2+1=3     |
| 5            | 0        | 3+0=3     |
| 6            | 1        | 3+1=4     |
| 7            | 0        | 4+0=4     |
| 8            | 1        | 4+1=5     |

If the receiver receives the packet with the following bits: 11010110 (no error) and the Check Sum is 5, then the receiver will detect an error because the calculated Check Sum does not match the received Check Sum.

### Point to Point Protocol

---

**Definition:** Point to Point Protocol (PTP) is a protocol used in a data communication system to detect and correct errors in data transmission. PTP uses a combination of Check Sum and error correction techniques to ensure that the data packet is delivered error-free.

**How it works:**

1. The sender calculates the Check Sum of the data packet and sends it along with the data packet.
2. The receiver calculates the Check Sum of the received data packet.
3. If the calculated Check Sum matches the received Check Sum, the receiver proceeds to the next step.
4. The receiver uses an error correction technique (such as cyclic redundancy check (CRC)) to detect any errors in the data packet.
5. If any errors are detected, the receiver sends an acknowledgement (ACK) to the sender indicating the error.
6. The sender retransmits the data packet with the corrected Check Sum.

**Example:**

Suppose we have a data packet with the following bits: 11010110. The Check Sum of this packet is 6 (1+1+0+1+0+1+1+0). The sender sends this packet along with the Check Sum (6) to the receiver.

| Bit Position | Data Bit | Check Sum |
| ------------ | -------- | --------- |
| 1            | 1        | 1         |
| 2            | 1        | 1+1=2     |
| 3            | 0        | 2+0=2     |
| 4            | 1        | 2+1=3     |
| 5            | 0        | 3+0=3     |
| 6            | 1        | 3+1=4     |
| 7            | 0        | 4+0=4     |
| 8            | 1        | 4+1=5     |

The receiver receives the packet with the following bits: 11010110 (no error) and the Check Sum is 5. The receiver detects no error and proceeds to the next step.

| Bit Position | Data Bit | Calculated Check Sum |
| ------------ | -------- | -------------------- |
| 1            | 1        | 1+1=2                |
| 2            | 1        | 2+0=2                |
| 3            | 0        | 2+1=3                |
| 4            | 1        | 3+0=3                |
| 5            | 0        | 3+1=4                |
| 6            | 1        | 4+0=4                |
| 7            | 0        | 4+1=5                |
| 8            | 1        | 5+1=6                |

The receiver uses an error correction technique (such as CRC) to detect any errors in the data packet. Suppose an error occurs during transmission, resulting in the following bits: 11110110.

| Bit Position | Data Bit | Calculated Check Sum |
| ------------ | -------- | -------------------- |
| 1            | 1        | 1+1=2                |
| 2            | 1        | 2+0=2                |
| 3            | 1        | 2+1=3                |
| 4            | 1        | 3+0=3                |
| 5            | 0        | 3+1=4                |
| 6            | 1        | 4+0=4                |
| 7            | 0        | 4+1=5                |
| 8            | 1        | 5+1=6                |

The receiver detects an error because the calculated Check Sum (6) does not match the received Check Sum (5). The receiver sends an acknowledgement (ACK) to the sender indicating the error.

The sender retransmits the data packet with the corrected Check Sum.

| Bit Position | Data Bit | Calculated Check Sum |
| ------------ | -------- | -------------------- |
| 1            | 1        | 1+1=2                |
| 2            | 1        | 2+0=2                |
| 3            | 0        | 2+1=3                |
| 4            | 1        | 3+0=3                |
| 5            | 0        | 3+1=4                |
| 6            | 1        | 4+0=4                |
| 7            | 0        | 4+1=5                |
| 8            | 1        | 5+1=6                |

The receiver receives the corrected packet and calculates the Check Sum (6). The receiver detects no error and sends an acknowledgement (ACK) to the sender.

### Key Concepts

---

- Check Sum: a mechanism used to detect errors in data transmission by calculating a digital signature of the data packet.
- Point to Point Protocol (PTP): a protocol used in a data communication system to detect and correct errors in data transmission.
- Error detection and correction techniques: techniques used to detect and correct errors in data transmission.
- Cyclic redundancy check (CRC): an error correction technique used to detect any errors in the data packet.

### Conclusion

---

In conclusion, Check Sum and Point to Point Protocol are two important error detection and correction techniques used in data communication systems. Check Sum is used to detect errors in data transmission by calculating a digital signature of the data packet, while Point to Point Protocol is used to detect and correct errors in data transmission using a combination of Check Sum and error correction techniques.
