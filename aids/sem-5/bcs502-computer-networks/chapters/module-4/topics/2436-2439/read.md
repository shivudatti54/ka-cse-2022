# **24.3.6-24.3.9: Transport Layer Protocols**

## **Introduction**

The Transport Layer is the fourth layer of the OSI model and is responsible for providing reliable data transfer between devices on a network. This layer provides error-free transfer of data between devices, ensuring that data is delivered in the correct order and without duplication or loss.

## **24.3.6: Connection-Oriented Transport**

### Definition

Connection-Oriented Transport is a transport-layer protocol that establishes a connection between two devices before data transfer begins. This connection is maintained throughout the data transfer process.

### Characteristics

- Establishes a connection before data transfer begins
- Provides reliable data transfer
- Ensures error-free transfer of data
- Maintains a connection throughout the data transfer process

### Example

Imagine two devices, Device A and Device B, that want to exchange data. To establish a connection, Device A sends a connection request to Device B, which responds with a connection acknowledgment. Once the connection is established, data can be transferred between the devices. The connection is maintained until all data has been transferred.

### Key Concepts

- Connection establishment
- Connection maintenance
- Reliable data transfer

## **24.3.7: Connectionless Transport**

### Definition

Connectionless Transport is a transport-layer protocol that does not establish a connection before data transfer begins. Instead, devices communicate with each other to determine the best path for data transfer.

### Characteristics

- Does not establish a connection before data transfer begins
- Provides best-effort delivery of data
- May result in data loss or duplication
- Does not maintain a connection throughout the data transfer process

### Example

Imagine two devices, Device A and Device B, that want to exchange data. Device A sends data to Device B, which responds with an acknowledgment. If the data is lost or duplicated, Device B simply discards the incorrect data.

### Key Concepts

- Connectionless communication
- Best-effort delivery
- Risk of data loss or duplication

## **24.3.8: Congestion Control**

### Definition

Congestion Control is a mechanism used to prevent network congestion by regulating the amount of data transmitted by devices.

### Characteristics

- Regulates the amount of data transmitted by devices
- Prevents network congestion
- Ensures fair sharing of network resources

### Example

Imagine a network with a limited bandwidth. If one device transmits data at a high rate, it can cause congestion and slow down other devices. The congestion control mechanism prevents this by regulating the amount of data transmitted by each device.

### Key Concepts

- Network congestion
- Fair sharing of network resources
- Data transmission regulation

## **24.3.9: Flow Control**

### Definition

Flow Control is a mechanism used to regulate the amount of data that can be transmitted by a device at any given time.

### Characteristics

- Regulates the amount of data transmitted by a device
- Ensures efficient use of network resources
- Prevents data loss or duplication

### Example

Imagine a network with a limited bandwidth. If a device transmits data at a high rate, it can cause a bottleneck. The flow control mechanism prevents this by regulating the amount of data transmitted by the device.

### Key Concepts

- Network resource utilization
- Efficient data transmission
- Data regulation

By understanding the Transport Layer protocols, including Connection-Oriented Transport, Connectionless Transport, Congestion Control, and Flow Control, you can better appreciate the complexities of network communication and the mechanisms that ensure reliable data transfer.
