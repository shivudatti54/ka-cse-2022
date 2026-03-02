# **Computer Networks - Packet Dropping**

### Key Concepts

- **Packet Dropping**: The loss of packets during transmission due to network congestion, errors, or interference.
- **Packet Loss Rate**: The percentage of packets lost during transmission, calculated as:
  ```math
  Packet Loss Rate = (Number of packets lost / Total Number of packets transmitted) \* 100
  ```

````
* **Mean Square Error (MSE)**: A measure of packet loss, calculated as:
  ```math
MSE = (1/N) \* ∑(y_i - x_i)^2
````

where y_i is the actual packet received, x_i is the expected packet, and N is the number of packets.

### Important Formulas

- **Packet Loss Formula**:
  ```math
  Packet Loss = 1 - (Number of packets received / Total Number of packets transmitted)
  ```

```
* **Round-Trip Time (RTT)**: The time it takes for a packet to travel from the sender to the receiver and back.
* **Jitter**: The variation in packet arrival times, measured in milliseconds.

### Important Definitions

* **Network Congestion**: The situation where the number of packets transmitted exceeds the network's capacity.
* **Error Detection**: Techniques used to detect errors during packet transmission, such as checksums and cyclic redundancy checks (CRCs).

### Theorems

* **Cramer's Rule**: A theorem used to calculate packet loss rates.
* **Fano's Inequality**: A theorem used to bound the packet loss rate.

### Quick Revision Tips

* Understand the concept of packet dropping and its impact on network performance.
* Familiarize yourself with packet loss formulas and calculation methods.
* Review error detection and correction techniques to minimize packet loss.
* Practice calculating packet loss rates and MSE to improve your understanding of the subject.
```
