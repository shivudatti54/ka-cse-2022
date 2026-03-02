# **1.1 - 1.3: Introduction to Computer Networks**

## **1.1: Data Communications**

### Definition

Data communications refer to the exchange of information between devices over a communication channel, such as a network. It involves the transmission, reception, and processing of data between devices.

### Key Concepts:

- **Data**: A set of digital characters used to represent information, such as text, images, and audio.
- **Communication channel**: A medium through which data is transmitted, such as a wire, wireless link, or fiber optic cable.
- **Transmission**: The process of sending data from a sender to a receiver.
- **Reception**: The process of receiving data from a sender.

### Example:

Imagine you are sending an email to a friend. The email is converted into a digital format and transmitted over the internet through a communication channel (e.g., a fiber optic cable). The email is received by your friend's email server, which then forwards it to their email client. The email client displays the email to your friend, who reads and responds.

### Key Technologies:

- **Modulation**: The process of varying a carrier wave to encode data onto it.
- **Demodulation**: The process of extracting the original data from the encoded carrier wave.
- **Error detection and correction**: Techniques used to detect and correct errors that occur during transmission.

### Code Example:

Here is an example of a simple data transmission using Python:

```python
import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
sock.connect(("www.example.com", 80))

# Send data
sock.send(b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n")

# Receive data
data = sock.recv(1024)

# Print the received data
print(data.decode())
```

This code sends a GET request to a web server and receives a response.

## **1.2: Networks Models**

### Definition

A network model is a representation of a computer network, including its components, architecture, and communication protocols.

### Key Models:

- **Physical Model**: A network model that focuses on the physical components of a network, such as cables, routers, and switches.
- **Data Link Model**: A network model that focuses on the communication between devices on a network, including protocols such as Ethernet and Wi-Fi.
- **Network Model**: A network model that focuses on the overall architecture of a network, including protocols such as TCP/IP.

### Example:

Imagine a network with two devices, a router and a laptop. The physical model would show the cables connecting the devices, the data link model would show the communication between the devices, and the network model would show the overall architecture of the network.

### Key Technologies:

- **Protocols**: Sets of rules and standards that govern data communication over a network.
- **Addressing**: The process of assigning a unique address to each device on a network.

### Code Example:

Here is an example of a simple network model using Python:

```python
import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a function to send data
def send_data(data):
    sock.connect(("www.example.com", 80))
    sock.send(data.encode())
    response = sock.recv(1024)
    sock.close()
    return response.decode()

# Define a function to receive data
def receive_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("www.example.com", 80))
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(1024)
    conn.close()
    return data.decode()

# Test the functions
print(send_data("GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"))
print(receive_data())
```

This code sends a GET request to a web server and receives a response.

## **1.3: Network Types**

### Definition

A network type refers to the type of network, such as a local area network (LAN), wide area network (WAN), or wireless network (WLAN).

### Key Types:

- **Local Area Network (LAN)**: A network that connects devices in a limited geographical area, such as a home or office building.
- **Wide Area Network (WAN)**: A network that connects devices over a large geographical area, such as a city or country.
- **Wireless Network (WLAN)**: A network that connects devices wirelessly, using radio waves or infrared signals.

### Example:

Imagine a network with several devices, including a router, switches, and laptops. The network type would be a LAN, as the devices are connected in a limited geographical area.

### Key Technologies:

- **Network topologies**: The arrangement of devices on a network, such as a bus, star, or mesh topology.
- **Network architectures**: The design and structure of a network, including protocols and devices.

### Code Example:

Here is an example of a simple LAN network model using Python:

```python
import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a function to send data
def send_data(data):
    sock.connect(("www.example.com", 80))
    sock.send(data.encode())
    response = sock.recv(1024)
    sock.close()
    return response.decode()

# Define a function to receive data
def receive_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("www.example.com", 80))
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(1024)
    conn.close()
    return data.decode()

# Test the functions
print(send_data("GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"))
print(receive_data())
```

This code sends a GET request to a web server and receives a response.
