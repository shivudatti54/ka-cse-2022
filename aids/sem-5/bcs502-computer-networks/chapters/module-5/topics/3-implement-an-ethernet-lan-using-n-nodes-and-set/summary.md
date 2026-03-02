# **Implementing an Ethernet LAN using n nodes**

## **Key Points**

- **Ethernet LAN**: A local area network that uses Ethernet as the underlying technology.
- **n nodes**: The number of devices connected to the LAN.
- **Traffic nodes**: Devices that send and receive data on the LAN.
- **Congestion window**: The amount of data that can be sent without causing network congestion.

## **Key Formulas and Definitions**

- **Bandwidth**: The rate at which data can be transmitted over the LAN, measured in bits per second (bps).
- **Throughput**: The amount of data that can be transmitted over the LAN per unit time, measured in bits per second (bps).
- **Packet switching**: The method of transmitting data in small packets over the LAN.
- **Congestion control algorithm**: A protocol used to regulate the amount of data sent over the LAN to avoid congestion.

## **Important Theorems and Concepts**

- **Maxwell's Averaged Stationary Source**: A key concept in understanding congestion window.
- **TELOS (Time-Estimated Load of the Source)**: A formula used to calculate the congestion window.

## **Revision Notes**

- **Step 1**: Set up the Ethernet LAN with n nodes and traffic nodes.
- **Step 2**: Simulate the data transmission between nodes using packet switching.
- **Step 3**: Calculate the congestion window using TELOS and Maxwell's Averaged Stationary Source.
- **Step 4**: Plot the congestion window for different source/destination pairs.

## **Important Formulas**

- **TELOS**: T = (S/N) \* (1 - (R \* t) / (B \* (1 - S/N)))
- **Maxwell's Averaged Stationary Source**: S(t) = (S0 / (1 + (R \* t) / (B \* (1 - S0/N))))
