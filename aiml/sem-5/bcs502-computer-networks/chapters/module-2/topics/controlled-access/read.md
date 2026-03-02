# **Controlled Access**

## **Introduction**

Controlled Access is a method of managing multiple users who share a common communication medium, such as a wireless network or a bus. It ensures that only authorized users can access the network, preventing unauthorized users from transmitting data or causing interference.

## **Types of Controlled Access**

- **Single-Access Method**: Only one user can access the network at a time.
- **Multi-Access Method**: Multiple users can access the network simultaneously.

## **Techniques for Controlled Access**

### 1. Frequency Division Multiple Access (FDMA)

- **Definition**: FDMA divides the available bandwidth into multiple frequency channels.
-     Each user is assigned a specific frequency channel to use.
- **Advantages**:
  - Simple implementation
  - Low cost
- **Disadvantages**:
  - Limited number of users can share the available bandwidth
  - Interference between channels

### 2. Time Division Multiple Access (TDMA)

- **Definition**: TDMA divides the available bandwidth into multiple time slots.
- Each user is assigned a specific time slot to transmit data.
- **Advantages**:
  - Efficient use of bandwidth
  - No interference between users
- **Disadvantages**:
  - Complex implementation
  - Requires precise timing

### 3. Code Division Multiple Access (CDMA)

- **Definition**: CDMA divides the available bandwidth into multiple code channels.
- Each user is assigned a specific code to transmit data.
- **Advantages**:
  - High security
  - Multi-user capability
- **Disadvantages**:
  - Complex implementation
  - High power consumption

### 4. Carrier Sense Multiple Access (CSMA)

- **Definition**: CSMA uses a carrier sense mechanism to detect idle periods in the network.
- Users transmit data only when the channel is idle.
- **Advantages**:
  - Simple implementation
  - Low cost
- **Disadvantages**:
  - Interference between users
  - Delay in transmission

### 5. Random Access Method (RAM)

- **Definition**: RAM allows users to access the network without any prior reservation or coordination.
- Users transmit data randomly and are granted access based on the network's capacity.
- **Advantages**:
  - Simple implementation
  - Fast access
- **Disadvantages**:
  - Interference between users
  - Congestion in the network

### 6. Time Slot Multiplexing (TSM)

- **Definition**: TSM divides the available bandwidth into multiple time slots.
- Each user is assigned a specific time slot to transmit data.
- **Advantages**:
  - Efficient use of bandwidth
  - No interference between users
- **Disadvantages**:
  - Complex implementation
  - Requires precise timing

### 7. Inter-Frame Space (IFS) protocol

- **Definition**: IFS protocol allocates time slots for each user to transmit data.
- Users are granted access to the network based on the allocated time slots.
- **Advantages**:
  - Efficient use of bandwidth
  - No interference between users
- **Disadvantages**:
  - Complex implementation
  - Requires precise timing

### 8. Polling protocol

- **Definition**: Polling protocol sends a request for data to each user.
- Users respond with their data, and the request is repeated for each user.
- **Advantages**:
  - Simple implementation
  - Low cost
- **Disadvantages**:
  - Interference between users
  - Delay in transmission

### 9. Demand Priority protocol

- **Definition**: Demand Priority protocol prioritizes users based on their demand for bandwidth.
- Users with higher priority are granted access to the network first.
- **Advantages**:
  - Efficient use of bandwidth
  - No interference between users
- **Disadvantages**:
  - Complex implementation
  - Requires precise priority assignment

### 10. Token Ring protocol

- **Definition**: Token Ring protocol uses a token to grant access to the network.
- Tokens are passed around the ring, and users are granted access based on the presence of a token.
- **Advantages**:
  - Efficient use of bandwidth
  - No interference between users
- **Disadvantages**:
  - Complex implementation
  - Requires precise token management

## **Comparison of Controlled Access Techniques**

| Technique       | Advantages                                                | Disadvantages                                                |
| --------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| FDMA            | Simple implementation, Low cost                           | Limited number of users, Interference between channels       |
| TDMA            | Efficient use of bandwidth, No interference between users | Complex implementation, Requires precise timing              |
| CDMA            | High security, Multi-user capability                      | Complex implementation, High power consumption               |
| CSMA            | Simple implementation, Low cost                           | Interference between users, Delay in transmission            |
| RAM             | Simple implementation, Fast access                        | Interference between users, Congestion in the network        |
| TSM             | Efficient use of bandwidth, No interference between users | Complex implementation, Requires precise timing              |
| IFS             | Efficient use of bandwidth, No interference between users | Complex implementation, Requires precise timing              |
| Polling         | Simple implementation, Low cost                           | Interference between users, Delay in transmission            |
| Demand Priority | Efficient use of bandwidth, No interference between users | Complex implementation, Requires precise priority assignment |
| Token Ring      | Efficient use of bandwidth, No interference between users | Complex implementation, Requires precise token management    |

## **Conclusion**

Controlled Access is an essential technique for managing multiple users in a common communication medium. Different techniques, such as FDMA, TDMA, CDMA, CSMA, RAM, TSM, IFS, Polling, Demand Priority, and Token Ring, offer various advantages and disadvantages. The choice of technique depends on the specific requirements of the network, including the number of users, available bandwidth, and security requirements.
