# **Revision Notes: 21.3.2 - IPv4 Datagram**

### Definitions and Theorems

- **Datagram**: A self-contained packet of data transmitted between devices on a network.
- **IP Datagram**: A packet of data that contains a source IP address, destination IP address, and data.
- **IPv4 Datagram**: A datagram that uses IPv4 protocol.

### Key Concepts

- **Header**: The part of the IP datagram that contains control information.
- **Fragmentation**: The process of dividing a large datagram into smaller, manageable pieces.
- **Reassembly**: The process of recombining fragmented datagrams.

### Formulas and Equations

- **MTU (Maximum Transmission Unit)**: The maximum size of a datagram that can be transmitted over a network interface.
- **Fragment Size**: The size of each fragment of a datagram.
- **Fragment Offset**: The offset of the fragment from the beginning of the original datagram.

### Key Points

- IPv4 datagrams are typically 20 bytes in size (header) plus data.
- Fragmentation occurs when a datagram is larger than the MTU.
- Reassembly occurs when a fragment is received and recombined with other fragments.
- The source IP address and destination IP address are used to route the datagram to its destination.
- Error-checking and correction are performed using checksum and error-checking algorithms.

### Important Formulas and Theorems

- **Checksum**: A calculation used to detect errors in data transmission.
- **CRC (Cyclic Redundancy Check)**: A calculation used to detect errors in data transmission.

### Quick Revision Tips

- Understand the structure of an IPv4 datagram.
- Know the process of fragmentation and reassembly.
- Be familiar with MTU and fragment size.
- Review checksum and CRC algorithms.
