# Textbook: Ch

## COMPUTER NETWORKS

### Module: Introduction: Data Communications, Networks, Network Types, Networks Models: Protocol

### Topic: Textbook: Ch

In this chapter, we will delve into the world of computer networks, focusing on the protocol model that governs our digital communication. The protocol model is the framework that enables devices on a network to communicate effectively, ensuring that data is transmitted accurately and efficiently.

### Historical Context

The development of the protocol model can be traced back to the 1960s, when the United States Department of Defense's Advanced Research Projects Agency (ARPA) funded a project to create a network of computers that could communicate with each other. This project, known as ARPANET, was the first operational packet switching network, and it laid the foundation for the modern internet.

In the 1970s and 1980s, the Internet Protocol (IP) was developed, which enabled different networks to communicate with each other. The IP model, also known as the TCP/IP model, became the de facto standard for the internet.

### The OSI Model

The Open Systems Interconnection (OSI) model is a 7-layered protocol model that was developed in the 1980s. The OSI model is an international standard that provides a framework for understanding how data is transmitted over a network. The 7 layers of the OSI model are:

1. **Physical Layer (Layer 1)**: Defines the physical means of transmitting data between devices, including cable specifications and wireless transmission protocols.
2. **Data Link Layer (Layer 2)**: Provides error-free transfer of data frames between two devices on the same network, using protocols such as Ethernet and Wi-Fi.
3. **Network Layer (Layer 3)**: Routes data between devices on different networks, using protocols such as IP and ICMP.
4. **Transport Layer (Layer 4)**: Provides reliable data transfer between devices, using protocols such as TCP and UDP.
5. **Session Layer (Layer 5)**: Establishes, manages, and terminates connections between applications running on different devices.
6. **Presentation Layer (Layer 6)**: Converts data into a format that can be understood by the receiving device, using protocols such as MIME and SSL.
7. **Application Layer (Layer 7)**: Provides services to end-user applications, such as email, file transfer, and web browsing.

### The TCP/IP Model

The TCP/IP model is a 4-layered protocol model that is used by the internet. The 4 layers of the TCP/IP model are:

1. **Network Access Layer (Layer 1)**: Provides access to the network, using protocols such as IP and ICMP.
2. **Internet Layer (Layer 2)**: Routes data between devices on different networks, using protocols such as IP and IGMP.
3. **Transport Layer (Layer 3)**: Provides reliable data transfer between devices, using protocols such as TCP and UDP.
4. **Application Layer (Layer 4)**: Provides services to end-user applications, such as email, file transfer, and web browsing.

### Comparison of OSI and TCP/IP Models

While both models provide a framework for understanding how data is transmitted over a network, there are some key differences between the two models.

| Layer | OSI Model          | TCP/IP Model         |
| ----- | ------------------ | -------------------- |
| 1     | Physical Layer     | Network Access Layer |
| 2     | Data Link Layer    | Network Access Layer |
| 3     | Network Layer      | Internet Layer       |
| 4     | Transport Layer    | Transport Layer      |
| 5     | Session Layer      | Not included         |
| 6     | Presentation Layer | Not included         |
| 7     | Application Layer  | Application Layer    |

### Case Study: Email Transmission

When you send an email, it follows a journey through the network, involving multiple layers of the protocol model.

1. **Application Layer**: Your email client (e.g. Gmail) breaks the email into small packets and adds a header that contains the sender's and recipient's email addresses.
2. **Transport Layer**: The email packets are transmitted to a mail server using TCP or UDP protocol.
3. **Internet Layer**: The mail server routes the email packets to the recipient's network using IP protocol.
4. **Network Access Layer**: The email packets are transmitted to the recipient's email server using protocols such as SMTP or IMAP.
5. **Application Layer**: The email packets are reassembled and presented to the recipient's email client.

### Applications and Examples

The protocol model has numerous applications in various fields, including:

- **Email**: Email transmission relies on the TCP/IP model to ensure reliable and efficient data transfer.
- **File Transfer**: File transfer protocols such as FTP and SFTP use the TCP/IP model to transfer files between devices.
- **Web Browsing**: Web browsers use the TCP/IP model to retrieve web pages from servers.
- **Video Conferencing**: Video conferencing protocols such as Skype and Zoom use the TCP/IP model to establish and manage connections between devices.

### Further Reading

- "Computer Networks" by Andrew S. Tanenbaum and David J. Wetherall
- "TCP/IP Illustrated, Volume 1: The Protocols" by Keith B. Kerr
- "The OSI Model" by Cisco Systems
- "TCP/IP Model" by IBM

In conclusion, the protocol model is a fundamental concept in computer networking that provides a framework for understanding how data is transmitted over a network. The OSI model and TCP/IP model are two popular protocol models that are used in different contexts. Understanding the protocol model is essential for designing and implementing efficient and reliable computer networks.
