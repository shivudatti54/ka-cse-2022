# 2.1 - 2.3: Introduction to Computer Networks

=====================================================

## 2.1: Data Communications

---

Data communications refer to the process of exchanging data between devices over a communication channel. This process involves encoding, transmission, and decoding of data to ensure reliable and efficient communication.

### Key Concepts:

- **Data Encoding:** Data encoding involves converting raw data into a format that can be transmitted over a communication channel. This can be achieved through various methods such as binary encoding, ASCII encoding, or using protocols like HTTP.
- **Data Transmission:** Data transmission involves sending the encoded data over the communication channel. This can be achieved through various methods such as wireline transmission, wireless transmission, or satellite transmission.
- **Data Decoding:** Data decoding involves converting the received data back into its original form. This can be achieved through various methods such as binary decoding, ASCII decoding, or using protocols like FTP.

### Examples:

- When you send an email, the data is first encoded into a format that can be transmitted over the internet. The email client then transmits the encoded data over the internet to the recipient's email server. The recipient's email server then decodes the data and displays it in the recipient's email client.

## 2.2: Network Topology

---

Network topology refers to the physical and logical arrangement of devices in a computer network. This arrangement determines how data is transmitted between devices and can impact the performance of the network.

### Types of Network Topology:

- **Bus Topology:** In a bus topology, all devices are connected to a single cable, which serves as the main communication pathway.
- **Star Topology:** In a star topology, all devices are connected to a central device, which serves as the main communication hub.
- **Ring Topology:** In a ring topology, devices are connected in a circular configuration, and data travels in one direction around the ring.
- **Mesh Topology:** In a mesh topology, each device is connected directly to every other device, providing multiple paths for data transmission.

## 2.3: Network Models

---

Network models refer to the theoretical frameworks used to describe and analyze computer networks. These models help network designers and engineers understand the behavior and performance of various network topologies and protocols.

### OSI Model:

The OSI model is a 7-layered model that describes the functions of a computer network. The 7 layers are:

1.  **Physical Layer (Layer 1):** Defines the physical means of data transmission.
2.  **Data Link Layer (Layer 2):** Ensures error-free transfer of data frames between devices.
3.  **Network Layer (Layer 3):** Routes data between devices on different networks.
4.  **Transport Layer (Layer 4):** Provides reliable data transfer between devices.
5.  **Session Layer (Layer 5):** Establishes, manages, and terminates connections between applications.
6.  **Presentation Layer (Layer 6):** Converts data into a format that can be understood by the receiving device.
7.  **Application Layer (Layer 7):** Provides services to end-user applications.

### TCP/IP Model:

The TCP/IP model is a 4-layered model that describes the functions of a computer network. The 4 layers are:

1.  **Network Access Layer (Layer 1):** Defines the physical and logical means of data transmission.
2.  **Internet Layer (Layer 2):** Routes data between devices on different networks.
3.  **Transport Layer (Layer 3):** Provides reliable data transfer between devices.
4.  **Application Layer (Layer 4):** Provides services to end-user applications.

## Applications

Computer networks have a wide range of applications, including:

- **Internet:** The global network of interconnected computers that use standardized communication protocols to exchange data.
- **Local Area Network (LAN):** A network that connects devices in a limited geographical area, such as a home, office building, or campus.
- **Wide Area Network (WAN):** A network that connects devices over a larger geographical area, such as a city or country.
- **Wireless Network:** A network that connects devices wirelessly, using radio waves or infrared signals.

## Case Studies

- **The Internet:** The internet is a global network of interconnected computers that use standardized communication protocols to exchange data. It was developed in the 1960s as a project of the United States Department of Defense, and it has since become a vital part of modern communication.
- **Facebook:** Facebook is a social media platform that connects millions of users worldwide. It uses a combination of cloud computing, data analytics, and social networking protocols to provide a personalized experience for its users.
- **Amazon Web Services (AWS):** AWS is a cloud computing platform that provides a range of services, including computing power, storage, and database management. It uses a combination of data analytics, machine learning, and network protocols to ensure high availability and scalability.

## Modern Developments

- **Cloud Computing:** Cloud computing involves storing and processing data in a remote location, rather than on local devices. This technology has revolutionized the way businesses and individuals store and access data.
- **Internet of Things (IoT):** The IoT refers to the network of physical devices, vehicles, and other items that are embedded with sensors, software, and connectivity, allowing them to collect and exchange data.
- **Artificial Intelligence (AI):** AI refers to the development of computer systems that can perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making.

## Further Reading

- **"Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall:** This textbook provides a comprehensive introduction to computer networks, including data communications, network topology, and network models.
- **"Computer Networks: A Systems Approach" by James Kurose and Keith Ross:** This textbook provides a detailed analysis of computer networks, including data communications, network topology, and network models.
- **"TCP/IP Illustrated" by W. Richard Stevens:** This book provides a detailed analysis of the TCP/IP protocol suite, including its history, architecture, and implementation.

## Diagrams

- ** OSI Model Diagram:**
  ```
  +---------------+
  |  Physical    |
  |  Layer (Layer 1) |
  +---------------+
         |
         |
         v
  +---------------+
  |  Data Link    |
  |  Layer (Layer 2) |
  +---------------+
         |
         |
         v
  +---------------+
  |  Network Layer  |
  |  (Layer 3)      |
  +---------------+
         |
         |
         v
  +---------------+
  |  Transport    |
  |  Layer (Layer 4) |
  +---------------+
         |
         |
         v
  +---------------+
  |  Session Layer  |
  |  (Layer 5)      |
  +---------------+
         |
         |
         v
  +---------------+
  |  Presentation  |
  |  Layer (Layer 6) |
  +---------------+
         |
         |
         v
  +---------------+
  |  Application  |
  |  Layer (Layer 7) |
  +---------------+
  ```
- **TCP/IP Model Diagram:**
  ```
  +---------------+
  |  Network Access  |
  |  Layer (Layer 1) |
  +---------------+
         |
         |
         v
  +---------------+
  |  Internet Layer  |
  |  (Layer 2)      |
  +---------------+
         |
         |
         v
  +---------------+
  |  Transport Layer  |
  |  (Layer 3)      |
  +---------------+
         |
         |
         v
  +---------------+
  |  Application    |
  |  Layer (Layer 4) |
  +---------------+
  ```
