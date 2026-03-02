# **Revision Notes: 24.3.6-24.3.9 - Introduction to Transport Layer**

### Introduction to Transport Layer

- **Definition:** The transport layer is the fourth layer of the OSI model, responsible for reliable data transfer between devices.
- **Functions:**
  - Segments data into smaller units (segments)
  - Assigns sequence numbers to ensure correct ordering
  - Provides error-checking and correction mechanisms
  - Offers flow control to prevent network congestion

### Transport-Layer Protocols: Introduction

- **Definition:** Transport-layer protocols regulate the transfer of data between devices on a network.
- **Key Protocols:**
  - TCP (Transmission Control Protocol)
  - UDP (User Datagram Protocol)

### Connection-Oriented vs. Connectionless

- **Connection-Oriented:** Establishes a connection between devices before data transfer (e.g., TCP)
- **Connectionless:** Does not establish a connection before data transfer (e.g., UDP)

### Synchronization and Flow Control

- **Synchronization:** Ensures correct ordering of data segments (sequence numbers)
- **Flow Control:** Regulates data transfer rate to prevent network congestion (windowing)

### Theorems and Formulas

- **Pareto's Law:** 80% of data is transferred within 20% of the total data
- **Jain's Theorem:** Used to calculate the available bandwidth
- **Bit Error Rate (BER):** Formula: P = q(1-q)^n
