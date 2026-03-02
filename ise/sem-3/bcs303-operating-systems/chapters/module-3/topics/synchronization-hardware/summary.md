# **Synchronization Hardware Revision Notes**

### Definitions and Theorems

- **Synchronization**: The process of synchronizing multiple sources of data to ensure they are identical and consistent.
- **Synchronization hardware**: Components used to synchronize data between multiple sources.
- **Bus protocol**: A method of communication between devices on a computer bus.
- **Arbitration protocol**: A method of resolving conflicts between devices on a computer bus.

### Key Concepts

- **Bus topology**: A network topology in which devices are connected through a common bus.
- **Master-slave**: A bus topology in which one device (master) controls the other devices (slaves).
- **Token ring**: A bus topology in which each device has a token that must be passed to the next device before data can be transmitted.
- **Causal delay model**: A model used to analyze the delay between the occurrence of an event and the detection of the event.
- **Critical section**: A code segment that accesses shared resources.

### Important Formulas

- **Bus protocol delay**: T = (d / V) \* (2n - 1)
  - Where T = delay, d = distance between devices, V = maximum speed of the bus, and n = number of devices
- **Arbitration delay**: T = (d / V) \* (2n - 1)
  - Where T = delay, d = distance between devices, V = maximum speed of the bus, and n = number of devices

### Important Concepts and Terms

- **Bus reservation**: A method of reserving a time slot on the bus for a device.
- **Bus contention**: A situation in which multiple devices try to access the bus simultaneously.
- **Bus error**: An error that occurs when a device on the bus detects an error.

### Quick Revision Tips

- Review bus topology and arbitration protocols to understand how devices communicate on a computer bus.
- Focus on key formulas and theorems related to bus protocol and arbitration delay.
- Practice analyzing the causal delay model and identifying critical sections of code.

Remember to practice and review regularly to reinforce your understanding of synchronization hardware.
