# Controlled Access

## Overview

Controlled Access is a protocol that allows multiple devices to share a common medium (e.g., wireless network) by allocating time slots for each device to transmit data.

### Key Points

- **Definition:** Controlled Access is a protocol that regulates access to a shared medium to prevent collisions and ensure reliable data transmission.
- **Types:**
  - Time Division Multiple Access (TDMA)
  - Frequency Division Multiple Access (FDMA)
  - Code Division Multiple Access (CDMA)
- **TDMA:**
  - Each device is assigned a time slot to transmit data
  - Other devices must wait for their assigned time slot to transmit
- **FDMA:**
  - Each device is assigned a specific frequency to transmit data
  - Other devices must not transmit on the same frequency
- **CDMA:**
  - Each device is assigned a unique code to transmit data
  - Other devices can transmit on any frequency, but must use a different code

### Formulas and Definitions

- **Bit Error Rate (BER):** The probability of a bit being transmitted incorrectly.
- **Signal-to-Noise Ratio (SNR):** The ratio of the desired signal power to the noise power.
- **Error Detection and Correction:**
  - **Hamming Code:** A linear error-correcting code that can detect and correct single-bit errors.
  - **Cyclic Redundancy Check (CRC):** A method of error detection that uses a polynomial to detect errors.

### Theorems

- **Shannon-Hartley Theorem:** A mathematical model that relates the capacity of a communication channel to its bandwidth and signal-to-noise ratio.
- **Cramer-Rao Lower Bound:** A lower bound on the variance of an unbiased estimator of a parameter, in this case, the bit error rate.

### Important Concepts

- **Access Control:** The process of regulating access to a shared medium to prevent collisions and ensure reliable data transmission.
- **Medium Access Control (MAC):** A layer of the OSI model that manages access to the physical medium.
