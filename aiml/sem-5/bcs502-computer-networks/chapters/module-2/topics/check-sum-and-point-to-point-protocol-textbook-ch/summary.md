# **Check Sum and Point to Point Protocol**

### Introduction

- The Check Sum is a simple error detection technique used in data transmission.
- It is a numerical value calculated from the data being sent, used to detect errors during transmission.

### Key Points

- **Definition:** Check Sum = Σd_i
- **Types:**
  - Parity Check Sum
  - Cyclic Redundancy Check (CRC)
- **Parity Check Sum:**
  - Used for even and odd number data
  - Formula: Check Sum = (Σd_i) mod 2
- **CRC:**
  - Used for any data type
  - Formula: Check Sum = g(x) = (Σg_i \* d_i) mod n

### Point to Point Protocol

- A protocol used in local area networks (LANs) to transmit data between two devices.
- Uses the Check Sum to detect errors in the data.

### Important Formulas

- Check Sum formula: Σd_i
- Parity Check Sum formula: (Σd_i) mod 2
- CRC formula: g(x) = (Σg_i \* d_i) mod n

### Theorems

- **Hamming Code Theorem:** A (n, k, t) code can detect up to t-1 errors.
- **Sphere Packing Theorem:** The minimum distance of a code is maximized when the code is sphere packed.

### Key Definitions

- **Hamming Code:** A linear error-correcting code that uses parity bits to detect and correct errors.
- **Sphere Packing:** A technique used to maximize the minimum distance of a code.
