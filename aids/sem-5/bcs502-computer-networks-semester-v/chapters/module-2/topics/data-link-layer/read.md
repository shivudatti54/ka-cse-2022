# Data Link Control Services

=====================================

## Introduction

---

The Data Link Layer is the second layer of the OSI model, and it is responsible for providing error-free transfer of data frames between two devices on the same network. The Data Link Layer is divided into two sublayers: the Media Access Control (MAC) sublayer and the Logical Link Control (LLC) sublayer. In this chapter, we will focus on the Data Link Control (DLC) services provided by the LLC sublayer.

## DLC Services

---

The DLC services are responsible for providing a reliable and efficient data transfer between two devices on the same network. The DLC services include:

### Framing

---

Framing is the process of dividing the data into smaller frames and adding a header and a trailer to each frame. The header contains the source and destination addresses, and the trailer contains the error-checking information.

```
  +---------------+
  |  Header      |
  +---------------+
  |  Data        |
  +---------------+
  |  Trailer     |
  +---------------+
```

### Flow Control

---

Flow control is the process of regulating the amount of data that can be sent by a device at a given time. This is necessary to prevent network congestion and to ensure that the receiving device can handle the data.

There are two types of flow control:

- **Stop-and-Wait**: In this method, the sender sends a frame and waits for an acknowledgement from the receiver before sending the next frame.
- **Sliding Window**: In this method, the sender sends multiple frames and the receiver sends an acknowledgement for each frame. The sender can send more frames as long as the receiver has acknowledged the previous frames.

### Error Control

---

Error control is the process of detecting and correcting errors that occur during data transfer. There are two types of error control:

- **Error Detection**: This involves adding a checksum to the data frame. The receiver calculates the checksum and compares it with the checksum sent by the sender. If the two checksums do not match, the receiver sends an error message to the sender.
- **Error Correction**: This involves using error-correcting codes such as Hamming codes or Reed-Solomon codes. These codes can detect and correct errors that occur during data transfer.

### Connectionless and Connection-Oriented

---

There are two types of DLC services:

- **Connectionless**: In this method, the sender sends data frames without establishing a connection with the receiver. The receiver does not send an acknowledgement for each frame.
- **Connection-Oriented**: In this method, the sender establishes a connection with the receiver before sending data frames. The receiver sends an acknowledgement for each frame.

## Data Link Layer Protocols

---

There are several data link layer protocols that provide DLC services. Some of the most common protocols include:

- **HDLC (High-Level Data Link Control)**: This is a bit-oriented protocol that provides error-free transfer of data frames.
- **PPP (Point-to-Point Protocol)**: This is a byte-oriented protocol that provides error-free transfer of data frames over point-to-point links.
- **SLIP (Serial Line Internet Protocol)**: This is a byte-oriented protocol that provides error-free transfer of data frames over serial lines.

## Conclusion

---

In conclusion, the DLC services are an essential part of the data link layer. They provide error-free transfer of data frames between two devices on the same network. The DLC services include framing, flow control, error control, and connectionless and connection-oriented services.

## Exam Tips

---

- Make sure you understand the different DLC services and how they work.
- Be able to explain the difference between connectionless and connection-oriented services.
- Be able to describe the different data link layer protocols and their characteristics.
