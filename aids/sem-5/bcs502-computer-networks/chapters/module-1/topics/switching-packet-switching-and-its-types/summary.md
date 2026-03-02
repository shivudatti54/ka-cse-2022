# **Switching: Packet Switching and its types**

## **Overview**

Packet switching is a method of transmitting data in a network by breaking it into small packets and transmitting each packet independently.

## **Key Points**

### **Definition**

- Packet switching: a method of transmitting data in a network by breaking it into small packets and transmitting each packet independently.
- A packet consists of a header and a payload.

### **Types of Switching**

- **Store-and-Forward Switching**:
  - A packet is stored in a buffer at the intermediate node before it is forwarded to its destination.
  - **Theorems**:
    - Store-and-forward switching is more reliable than cut-through switching.
    - Store-and-forward switching is more efficient than virtual circuit switching.
- **Cut-Through Switching**:
  - A packet is forwarded immediately after it is received, without being stored in a buffer.
  - **Theorems**:
    - Cut-through switching is faster than store-and-forward switching.
    - Cut-through switching is less reliable than store-and-forward switching.
- **Virtual Circuit Switching**:
  - A dedicated path is established between the sender and receiver before data is sent.
  - **Theorems**:
    - Virtual circuit switching is more reliable than cut-through switching.
    - Virtual circuit switching is less efficient than store-and-forward switching.

### **Packet Switching Formulas**

- **Packet Transmission Time**:
  - T = d / (r \* 8), where T is the transmission time, d is the distance between nodes, r is the speed of the link, and 8 is the number of bits in a byte.
- **Packet Loss Probability**:
  - P = (1 - e^(-λ \* t)) \* (1 - (λ \* t)), where P is the packet loss probability, λ is the packet arrival rate, and t is the transmission time.

### **Key Terms**

- **Buffer**: a temporary storage area for packets.
- **Header**: the part of a packet that contains control information.
- **Payload**: the part of a packet that contains the actual data.
