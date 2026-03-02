# **Check Sum and Point to Point Protocol**

### Introduction

In computer networking, error detection and correction are critical components of data transmission. Two popular techniques used for error detection are Check Sum and Point to Point Protocol. In this section, we will delve into the concepts of Check Sum and Point to Point Protocol, their advantages, and limitations.

### What is Check Sum?

**Definition:** A Check Sum is a value calculated from the data sent over a network. It is used to detect any corruption or alteration of the data during transmission.

**How it works:**

- The sender calculates the Check Sum of the data using a specific algorithm (e.g., CRC-8).
- The sender appends the Check Sum to the end of the data packet.
- The receiver calculates the Check Sum of the received data packet and compares it with the appended Check Sum.
- If the two Check Sums match, the data is considered valid; otherwise, it indicates error or corruption during transmission.

### Advantages of Check Sum:

- Simple to implement
- Fast computation
- Provides immediate indication of errors

### Limitations of Check Sum:

- Does not provide any correction mechanism
- Can be vulnerable to errors due to finite precision of the calculation

### What is Point to Point Protocol?

**Definition:** Point to Point Protocol is a technique used to transmit data between two end points. It ensures that data is transmitted accurately and efficiently.

**How it works:**

- The sender breaks the data into small packets and assigns a sequence number to each packet.
- The packets are transmitted to the receiver.
- The receiver reassembles the data packets in the correct order.
- The receiver applies error detection mechanisms (e.g., Check Sum) to ensure data integrity.

### Advantages of Point to Point Protocol:

- Ensures accurate data transmission
- Provides correction mechanisms for errors
- Suitable for low-bandwidth networks

### Limitations of Point to Point Protocol:

- Can be susceptible to packet loss or corruption
- Requires more computational resources

### Block Coding

Block Coding is a technique used in data transmission to detect and correct errors. It works by dividing data into blocks and appending a Check Sum to each block.

**Types of Block Coding:**

- **Cyclic Redundancy Check (CRC):** Uses a specific algorithm to calculate the Check Sum.
- **Hamming Code:** Uses a combination of bits to detect and correct errors.

### Cyclic Codes

Cyclic Codes are a type of Block Coding that uses a specific algorithm to calculate the Check Sum. They are widely used in data transmission due to their simplicity and efficiency.

**Types of Cyclic Codes:**

- **Single Error Correcting Code (SECC):** Can detect and correct single-bit errors.
- **Double Error Correcting Code (DECC):** Can detect and correct double-bit errors.

### Key Concepts

- **Data Link Layer:** Responsible for error detection and correction.
- **Block Coding:** Divides data into blocks and calculates a Check Sum.
- **Cyclic Codes:** A type of Block Coding used for error detection and correction.
- **Check Sum:** A value used to detect errors during data transmission.
- **Point to Point Protocol:** Ensures accurate data transmission between two end points.
