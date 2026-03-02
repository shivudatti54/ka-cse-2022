# **Controlled Access**

## **Introduction**

Controlled Access (CA) is a method of managing access to a shared medium in a computer network to prevent interference and collisions. It is an essential feature of Data Link Layer protocols, particularly in wireless networks. CA ensures that only authorized devices can transmit data on the network, thereby reducing errors and improving overall network performance.

## **Types of Controlled Access Methods**

There are several types of CA methods, including:

- **Token Ring**: Each device in the network receives a token (a signal indicating its turn to transmit) and must relinquish the token before transmitting.
-     **Token Passing**: Similar to Token Ring, but devices pass the token to adjacent devices instead of keeping it.
- **Sliding Window**: A fixed-size window of time is allocated for each device to transmit data.
- **Pom-pom protocol**: A protocol where devices use a token to gain access to the transmit medium.

### **Token Ring**

- **How it works**: Each device in the network has a buffer to store incoming data. When a device wants to transmit data, it requests the token from the network manager. The network manager checks if the device is allowed to transmit and grants the token if it is. The device then sends its data and waits for permission to transmit again.
- **Advantages**: Reduces collisions and interference, ensures fair access to the network.
- **Disadvantages**: Creates a bottleneck at the network manager, can be slow.

### **Token Passing**

- **How it works**: Similar to Token Ring, but devices pass the token to adjacent devices instead of keeping it.
- **Advantages**: Reduces collisions and interference, faster than Token Ring.
- **Disadvantages**: More complex than Token Ring, can be prone to token loss.

### **Sliding Window**

- **How it works**: A fixed-size window of time is allocated for each device to transmit data. Devices can transmit data as long as the window is not full.
- **Advantages**: Reduces collisions and interference, fast and efficient.
- **Disadvantages**: Can lead to congestion if the window is too small.

### **Pom-pom protocol**

- **How it works**: Devices use a token to gain access to the transmit medium. When a device wants to transmit data, it sends a "pom-pom" signal to the network.
- **Advantages**: Reduces collisions and interference, ensures fair access to the network.
- **Disadvantages**: Can be prone to token loss, complex to implement.

## **Comparison of CA Methods**

| CA Method        | Advantages                                                  | Disadvantages                                     |
| ---------------- | ----------------------------------------------------------- | ------------------------------------------------- |
| Token Ring       | Reduces collisions and interference, ensures fair access    | Creates bottleneck at network manager, slow       |
| Token Passing    | Reduces collisions and interference, faster than Token Ring | More complex than Token Ring, prone to token loss |
| Sliding Window   | Reduces collisions and interference, fast and efficient     | Can lead to congestion if window is too small     |
| Pom-pom protocol | Reduces collisions and interference, ensures fair access    | Prone to token loss, complex to implement         |

## **Conclusion**

Controlled Access is an essential feature of Data Link Layer protocols, particularly in wireless networks. There are several types of CA methods, each with its advantages and disadvantages. Understanding the different CA methods is crucial for designing and implementing efficient and reliable computer networks.
