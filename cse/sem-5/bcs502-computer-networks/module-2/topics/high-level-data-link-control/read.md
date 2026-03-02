# High-Level Data Link Control (HDLC)

## Introduction

High-Level Data Link Control (HDLC) is a bit-oriented protocol used for synchronous serial communication across point-to-point and multipoint links. Developed by ISO (International Organization for Standardization), HDLC serves as a foundation for many Data Link Layer protocols used in computer networking. It provides reliable transmission of data frames with error control and flow control mechanisms, making it essential for understanding modern communication protocols.

HDLC operates at the Data Link Layer (Layer 2) of the OSI model and is widely used in telecommunications, WAN (Wide Area Network) connections, and data transmission between computers. It forms the basis for several important protocols including Point-to-Point Protocol (PPP) and Link Access Procedure, Balanced (LAPB). Understanding HDLC is crucial for CSE students as it demonstrates fundamental concepts of data framing, error detection, and flow control that are applicable throughout computer networking.

## Key Concepts

### HDLC Protocol Architecture

HDLC uses a synchronous transmission mechanism where data is transmitted as a stream of bits organized into frames. The protocol supports three types of station configurations:

1. **Primary Station**: Controls the operation of the link, issues commands, and manages data flow
2. **Secondary Station**: Operates under the control of the primary station, responds to commands
3. **Combined Station**: Can function as both primary and secondary, initiating and responding to frames

### HDLC Frame Structure

An HDLC frame consists of six main fields:

| Field       | Size       | Description                              |
| ----------- | ---------- | ---------------------------------------- |
| Flag        | 8 bits     | Start and end delimiter (01111110)       |
| Address     | 8 bits     | Identifies the secondary station         |
| Control     | 8/16 bits  | Frame type and control information       |
| Information | Variable   | User data (0 or more bits)               |
| FCS         | 16/32 bits | Frame Check Sequence for error detection |

### Frame Types

HDLC defines three types of frames:

1. **Information Frames (I-frames)**: Carry user data and include send and receive sequence numbers
2. **Supervisory Frames (S-frames)**: Used for flow control and error recovery (RR, RNR, REJ, SREJ)
3. **Unnumbered Frames (U-frames)**: Used for link management and control functions (SNRM, SABM, DISC, UA, DM, FRMR)

### HDLC Operational Modes

HDLC operates in two primary modes:

- **Asynchronous Balanced Mode (ABM)**: Uses combined stations, no primary/secondary hierarchy
- **Asynchronous Response Mode (ARM)**: Primary controls, secondary can initiate transmission
- **Normal Response Mode (NRM)**: Secondary can transmit only when polled by primary

### Error Control and Flow Control

HDLC implements sophisticated error and flow control mechanisms:

- **Error Detection**: Uses CRC (Cyclic Redundancy Check) with 16-bit or 32-bit FCS
- **Error Recovery**: Uses Go-Back-N and Selective Reject ARQ techniques
- **Flow Control**: Uses receive ready (RR) and receive not ready (RNR) commands
- **Sliding Window Protocol**: Supports up to 7 outstanding frames (extended to 127)

### Bit Stuffing

HDLC uses bit stuffing to ensure the flag sequence (01111110) does not appear within the frame. The transmitter inserts a '0' after five consecutive '1's, and the receiver removes any '0' that follows five consecutive '1's.

## Examples

### Example 1: Frame Construction

Construct an HDLC frame to send the data byte 0x41 ('A') to address 0x03 using I-frame format with N(S)=3 and N(R)=5.

**Solution:**

1. **Flag**: 01111110 (0x7E)
2. **Address**: 00000011 (0x03)
3. **Control**: For I-frame with N(S)=3 (00000011) and N(R)=5 (00000101):

- Format: N(S) - P/F - N(R)
- Bits: 00000 1 11 (P=0) 00000101
- Control byte: 0x25 (binary: 00100101)

4. **Information**: 01000001 (0x41)
5. **FCS**: Calculate CRC-16 (for demonstration, assume 0x1A2B)
6. **Closing Flag**: 01111110 (0x7E)

Complete frame: 7E 03 25 41 1A 2B 7E

### Example 2: Bit Stuffing

Apply bit stuffing to the data sequence: 011011111011111101

**Solution:**

Step-by-step stuffing:

- Original: 011011111011111101
- After first '11111': Insert '0' → 011011111**0**01111101
- After second '11111': Insert '0' → 0110111110011111**0**1
- Final stuffed sequence: 01101111100111110101

The receiver will remove the inserted '0' bits to recover original data.

### Example 3: Error Detection Using CRC

Given data bits: 1101011011 and divisor: 1011, calculate the CRC using CRC-4 (CRC-ANSI).

**Solution:**

1. Append zeros equal to divisor length - 1 = 3 zeros
2. Data with zeros: 1101011011**000**
3. Perform binary division:

- 1011 goes into 1101 → quotient bit 1
- Continue division through all bits

4. Remainder (CRC): 100 (3 bits)
5. Transmitted data: 1101011011**100**

At receiver, same division performed; remainder should be zero for no errors.

## Exam Tips

1. **Remember the frame format**: Flag (8 bits) → Address (8 bits) → Control (8/16 bits) → Information (variable) → FCS (16/32 bits) → Flag (8 bits)

2. **Know the three frame types**: I-frames (information transfer), S-frames (supervisory), and U-frames (unnumbered/management)

3. **Bit stuffing rule**: Insert '0' after five consecutive '1's in data; this prevents false flag detection

4. **Control field formats**: Remember that I-frames contain both N(S) and N(R), S-frames contain only N(R), and U-frames have no sequence numbers

5. **Extended addressing**: HDLC supports extended address field where the least significant bit indicates more address bytes (0 = more follows, 1 = last address byte)

6. **Difference between modes**: NRM (Normal Response Mode) requires polling, ABM (Asynchronous Balanced Mode) allows any station to initiate transmission

7. **Error detection**: CRC-16 uses polynomial x^16 + x^12 + x^5 + 1 (CCITT), CRC-32 uses 0x04C11DB7

8. **Flow control commands**: RR (Receive Ready) acknowledges frames and indicates ready for more; RNR (Receive Not Ready) indicates temporary inability to receive

9. **Window size**: Standard HDLC uses 7-bit sequence numbers (window size 7), extended format uses 127

10. **Common commands/responses**: SABM (Set Asynchronous Balanced Mode), DISC (Disconnect), UA (Unnumbered Acknowledgment), DM (Disconnected Mode)
