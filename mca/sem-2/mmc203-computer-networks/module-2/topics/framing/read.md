# Data Link Layer Framing


## Table of Contents

- [Data Link Layer Framing](#data-link-layer-framing)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Frame Structure and Components](#frame-structure-and-components)
  - [Character-Oriented Framing (Byte Stuffing)](#character-oriented-framing-byte-stuffing)
  - [Bit-Oriented Framing (Bit Stuffing)](#bit-oriented-framing-bit-stuffing)
  - [Physical Layer Coding Violations](#physical-layer-coding-violations)
  - [Frame Synchronization](#frame-synchronization)
  - [Common Framing Protocols](#common-framing-protocols)
- [Examples](#examples)
  - [Example 1: Bit Stuffing Operation](#example-1-bit-stuffing-operation)
  - [Example 2: Byte Stuffing Operation](#example-2-byte-stuffing-operation)
  - [Example 3: Ethernet Frame Analysis](#example-3-ethernet-frame-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Framing is a fundamental concept in data communication that refers to the process of dividing a stream of bits from the physical layer into manageable data units called frames. The data link layer, which is the second layer of the OSI model, is responsible for this critical function. Framing provides a way for the receiving end to identify the beginning and end of each data unit, ensuring reliable data transfer between adjacent nodes connected by a communication link.

In computer networks, the physical layer merely transmits raw bits without any structure or meaning. Without framing, a receiver would have no way of determining where one message ends and another begins. The data link layer solves this problem by encapsulating network layer packets into frames, adding control information such as frame delimiters, addresses, and error detection codes. This makes framing essential for efficient and error-free communication in local area networks (LANs), wide area networks (WANs), and modern high-speed communication systems.

The importance of framing extends beyond simple data delimitation. It also facilitates flow control, error handling, and physical medium access management. Different framing techniques have been developed to address various challenges including bit-oriented vs. character-oriented protocols, synchronization issues, and transparency requirements. Understanding these techniques is crucial for network engineers and developers working with communication protocols.

## Key Concepts

### Frame Structure and Components

A typical data frame consists of several essential components that enable proper transmission and reception. The frame header contains control information including source and destination addresses (MAC addresses in Ethernet), frame type identifiers, and sequence numbers for tracking. The payload or data field carries the network layer packet (such as an IP datagram). The frame trailer includes error detection mechanisms like the Frame Check Sequence (FCS), which uses cyclic redundancy check (CRC) to detect transmission errors.

The minimum and maximum frame sizes are often defined by the underlying protocol. For example, Ethernet defines a minimum frame size of 64 bytes and maximum of 1518 bytes. Frames smaller than the minimum are considered "runt frames" and are typically discarded, while frames exceeding the maximum are called "jumbo frames" and may require special handling or may be considered errors.

### Character-Oriented Framing (Byte Stuffing)

Character-oriented framing, also known as byte-stuffing, was widely used in early protocols like BISYNC (Binary Synchronous Communication) and PPP (Point-to-Point Protocol) in asynchronous links. This approach treats each character as a unit, using special sentinel characters to mark frame boundaries. The flag byte (usually 0x7E) marks both the beginning and end of a frame.

The transparency problem arises when the flag byte appears within the data payload. To solve this, byte stuffing inserts a special escape character (0x7D) before any flag or escape character in the data. Upon reception, the receiver removes these escape characters to restore original data. For example, 0x7E becomes 0x7D 0x5E, and 0x7D becomes 0x7D 0x5D in the transmitted stream.

### Bit-Oriented Framing (Bit Stuffing)

Bit-oriented protocols like HDLC (High-Level Data Link Control) treat frames as a continuous stream of bits rather than bytes. The flag sequence 01111110 (0x7E) marks frame boundaries. Bit stuffing addresses the transparency problem by inserting a single zero after any sequence of five consecutive 1s in the data. The receiver automatically removes any zero that follows five consecutive 1s, restoring the original data.

This method provides better efficiency than byte stuffing as it does not require byte alignment and offers more efficient use of bandwidth. Bit stuffing is used in protocols like HDLC, PPP (in synchronous links), and various other data link layer implementations. The overhead is minimal since stuffing only occurs after five consecutive 1s, which is statistically infrequent in random data.

### Physical Layer Coding Violations

Some protocols use specific coding violations at the physical layer to indicate frame boundaries. This approach is used in Ethernet 10BASE5 and 10BASE2 implementations where the invalid signal transitions (coding violations) in the physical layer encoding serve as frame delimiters. Similarly, some token ring implementations use special symbols that do not correspond to valid data bits.

This method eliminates the need for stuff/destuffing operations since the delimiters cannot occur naturally in the data stream. However, it requires tight integration between the data link and physical layers, making it protocol-specific and less flexible than software-based stuffing approaches.

### Frame Synchronization

Frame synchronization is the process by which the receiver identifies the correct boundaries of incoming frames. This involves detecting the flag sequences and properly handling the stuffed data within frames. Proper synchronization requires distinguishing between flags that are legitimately part of the data versus those marking boundaries, which is achieved through the stuffing/destuffing mechanism.

Loss of synchronization can occur due to transmission errors, timing issues, or equipment failures. When synchronization is lost, the receiver may experience frame slippage or complete communication failure until proper alignment is restored. Most protocols include recovery mechanisms such as looking for the next valid flag sequence to resynchronize.

### Common Framing Protocols

**HDLC (High-Level Data Link Control):** A bit-oriented protocol that serves as the basis for many modern data link protocols. HDLC supports both point-to-point and point-to-multipoint configurations and includes features for flow control, error recovery, and link management.

**PPP (Point-to-Point Protocol):** Widely used for establishing direct connections between two nodes, such as between a computer and an ISP. PPP includes framing capabilities as part of its protocol stack, supporting both character-oriented (async) and bit-oriented (synchronous) operation.

**Ethernet (IEEE 802.3):** Uses a specific frame format with preamble, start frame delimiter, source/destination MAC addresses, length/type field, data, and FCS. Ethernet frames do not use bit/byte stuffing but rely on the physical layer's coding for synchronization.

## Examples

### Example 1: Bit Stuffing Operation

**Problem:** Apply bit stuffing to the following data sequence: 011011111011111101

**Solution:**

Starting with the original data: 011011111011111101

We scan for five consecutive 1s and insert a 0 after each occurrence:

1. Position 4-8: We have 11111 (bits 4-8), so we insert a 0 after position 8

- Data becomes: 011011111**0**01111101

2. Now scanning again: We have 11111 starting at position 10, so we insert another 0

- Data becomes: 0110111110011111**0**01

3. The final stuffed data: 01101111100111110101

**Verification:** Count the bits - original 18 bits became 20 bits after stuffing two zeros.

### Example 2: Byte Stuffing Operation

**Problem:** For a character-oriented protocol using flag 0x7E and escape 0x7D, show the transmitted data for the payload: "A\x7EB\x7D" (where \x denotes hexadecimal)

**Solution:**

Original payload bytes: 0x41 0x7E 0x42 0x7D

We need to stuff any 0x7E or 0x7D occurring in the data:

- 0x41 (letter 'A') - no stuffing needed, remains 0x41
- 0x7E (flag) - becomes 0x7D 0x5E
- 0x42 (letter 'B') - no stuffing needed, remains 0x42
- 0x7D (escape) - becomes 0x7D 0x5D

Transmitted payload: 0x41 0x7D 0x5E 0x42 0x7D 0x5D

With flag bytes added at beginning and end:
Transmitted frame: 0x7E 0x41 0x7D 0x5E 0x42 0x7D 0x5D 0x7E

### Example 3: Ethernet Frame Analysis

**Problem:** Given an Ethernet frame with the following hex dump: AA AA AA AA AA AA 00 0C 29 4A 5B 3E 08 00 45 00 00 34..., identify the source and destination MAC addresses.

**Solution:**

Ethernet frame structure (first 14 bytes are header):

- Bytes 1-6: Destination MAC Address
- Bytes 7-12: Source MAC Address
- Bytes 13-14: EtherType/Length

Extracting addresses from the hex dump:

- Destination MAC: AA AA AA AA AA AA
- Source MAC: 00 0C 29 4A 5B 3E

The EtherType field (08 00) indicates IPv4. The source MAC address 00:0C:29:4A:5B:3E belongs to a VMware virtual network interface, indicating this frame originated from a virtual machine.

## Exam Tips

1. **Distinguish between bit stuffing and byte stuffing:** Remember that bit stuffing works at the bit level (after five 1s insert a 0) while byte stuffing uses escape characters at the byte level. Bit stuffing is more bandwidth-efficient.

2. **Know the flag sequences:** For bit-oriented protocols, the flag is 01111110 (0x7E). For character-oriented protocols, the flag is typically 0x7E (same value, different interpretation).

3. **Transparency is the key concept:** The main purpose of stuffing is to ensure that flag sequences appearing in the data do not get mistaken for frame boundaries. Always explain this when describing stuffing mechanisms.

4. **Ethernet does not use stuffing:** Unlike HDLC and PPP, standard Ethernet frames do not employ bit or byte stuffing. Frame synchronization relies on physical layer preamble and Start Frame Delimiter (SFD).

5. **Frame check sequence (FCS) purpose:** The CRC in the trailer provides error detection. If errors are detected, the frame is typically discarded, and higher layers handle retransmission (in reliable protocols).

6. **Minimum frame size requirement:** Ethernet requires a minimum frame size of 64 bytes to ensure that collisions can be detected by all stations. This includes header (14 bytes), data (46 bytes minimum), and FCS (4 bytes).

7. **Understand when destuffing occurs:** The receiver performs destuffing BEFORE computing the CRC/FCS. This ensures that the original data is correctly reconstructed but also means corrupted stuffed bits can propagate.

8. **PPP framing modes:** PPP supports both HDLC-like bit stuffing for synchronous links and character stuffing for asynchronous links (like dial-up modems). Know the appropriate applications for each.
