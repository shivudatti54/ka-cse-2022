# Transmission Modes and Network Devices
## Computer Networks — BSc (Hons) Computer Science (NEP 2024 UGCF)
### Delhi University

---

## 1. Introduction

In today's interconnected world, understanding how data moves between computers and devices forms the foundation of modern communication systems. Whether you're streaming a video, sending an email, or conducting a video conference, the principles of **transmission modes** and **network devices** determine how efficiently and effectively data travels across networks.

This study material covers two critical components of computer networking:

1. **Transmission Modes** — Define the direction of data flow between communicating devices
2. **Network Devices** — Hardware components that enable connectivity, data forwarding, and network management

These topics align with the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science and are essential for both theoretical examinations and practical networking implementations.

---

## 2. Transmission Modes

Transmission modes (also called communication modes) define the direction and flow of data between two communicating devices on a network. The choice of transmission mode affects network efficiency, cost, and the type of hardware required.

### 2.1 Classification of Transmission Modes

```
┌─────────────────────────────────────────────────────────────┐
│                    TRANSMISSION MODES                        │
├─────────────────┬─────────────────┬─────────────────────────┤
│    SIMPLEX      │  HALF-DUPLEX    │     FULL-DUPLEX         │
│                 │                 │                         │
│  One-way only   │  Two-way        │  Simultaneous           │
│  (Unidirectional)│  alternating   │  bidirectional          │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### 2.2 Simplex Mode

In **simplex mode**, data flows in **only one direction** — from the sender to the receiver. The communication is unidirectional; one device can only transmit, and the other can only receive.

**Characteristics:**
- Unidirectional communication
- Full bandwidth utilized in one direction
- Simple hardware requirements
- No possibility of feedback in the same channel

**Real-World Examples:**

| Application | Description |
|-------------|-------------|
| **Keyboard to Computer** | Data flows from keyboard to computer only; the computer doesn't send data back through the keyboard |
| **Television Broadcasting** | TV towers transmit signals to viewers; viewers cannot send data back through the same channel |
| **Radio Broadcasting** | Stations broadcast to receivers; no return path needed |
| **Mouse to Computer** | Mouse sends position/click data to computer |

**Technical Implementation:**

```python
# Simplex Communication - Sender Only
class SimplexSender:
    def __init__(self, data):
        self.data = data
    
    def transmit(self):
        # Simplex: Only sends, never receives
        print(f"Simplex Mode: Transmitting data → {self.data}")
        return self.data

# Simplex Communication - Receiver Only
class SimplexReceiver:
    def receive(self, data):
        # Simplex: Only receives, never transmits
        print(f"Simplex Mode: Receiving data ← {data}")

# Demonstration
sender = SimplexSender("Hello World")
receiver = SimplexReceiver()
transmitted_data = sender.transmit()
receiver.receive(transmitted_data)
```

### 2.3 Half-Duplex Mode

In **half-duplex mode**, data can flow in **both directions, but not simultaneously**. Devices can both send and receive, but they must take turns. When one device transmits, the other must wait.

**Characteristics:**
- Bidirectional but alternating
- Requires switching mechanism
- Shared channel capacity
- Potential delay due to turn-taking

**Real-World Examples:**

| Application | Description |
|-------------|-------------|
| **Walkie-Talkie** | Both parties can talk and listen, but not simultaneously; must say "over" to indicate turn change |
| **CB Radio** | Similar to walkie-talkie communication |
| **Traditional Ethernet (Half-Duplex)** | Old 10BASE-T networks used shared media |
| **Network Switch Management** | Console port communication |

**Technical Implementation:**

```python
import time

class HalfDuplexDevice:
    def __init__(self, name):
        self.name = name
        self.channel_busy = False
    
    def send(self, message, other):
        """Send data but must wait if channel is busy"""
        if self.channel_busy:
            print(f"{self.name}: Cannot send - waiting for channel")
            return
        
        self.channel_busy = True
        print(f"{self.name}: Transmitting → {message}")
        time.sleep(1)  # Transmission time
        other.receive(message)
        self.channel_busy = False
        print(f"{self.name}: Transmission complete, channel free")
    
    def receive(self, message):
        print(f"{self.name}: Receiving ← {message}")

# Demonstration of half-duplex (alternating communication)
device_a = HalfDuplexDevice("Device A")
device_b = HalfDuplexDevice("Device B")

# Turn 1: A sends to B
device_a.send("Hello B", device_b)
print()
# Turn 2: B sends to A (cannot happen simultaneously)
device_b.send("Hello A", device_a)
```

### 2.4 Full-Duplex Mode

In **full-duplex mode**, data can flow in **both directions simultaneously**. Both devices can transmit and receive at the same time, requiring separate channels or sophisticated signal separation techniques.

**Characteristics:**
- True bidirectional simultaneous communication
- Higher complexity and cost
- Maximum utilization of bandwidth
- Requires separate transmission paths or frequency division

**Real-World Examples:**

| Application | Description |
|-------------|-------------|
| **Telephone Conversation** | Both parties can speak and listen simultaneously |
| **Modern Ethernet (100BASE-TX, 1000BASE-T)** | Simultaneous send/receive using separate wire pairs |
| **Fiber Optic Communications** | Dedicated lanes for each direction |
| **Video Conferencing** | Simultaneous audio/video in both directions |
| **Wi-Fi (802.11)** | Modern standards support full-duplex |

**Technical Implementation:**

```python
import threading
import time

class FullDuplexChannel:
    def __init__(self):
        self.buffer_a_to_b = []
        self.buffer_b_to_a = []
        self.running = True
    
    def send_a_to_b(self, message):
        """Simultaneous send capability"""
        self.buffer_a_to_b.append(message)
    
    def send_b_to_a(self, message):
        """Simultaneous send capability"""
        self.buffer_b_to_a.append(message)
    
    def receive_a(self):
        return self.buffer_b_to_a.pop(0) if self.buffer_b_to_a else None
    
    def receive_b(self):
        return self.buffer_a_to_b.pop(0) if self.buffer_a_to_b else None

# Demonstration of full-duplex communication
channel = FullDuplexChannel()

def device_a_communication():
    for i in range(3):
        channel.send_a_to_b(f"Message A→B #{i+1}")
        msg = channel.receive_a()
        if msg:
            print(f"Device A received: {msg}")
        time.sleep(0.5)

def device_b_communication():
    for i in range(3):
        msg = channel.receive_b()
        if msg:
            print(f"Device B received: {msg}")
        channel.send_b_to_a(f"Message B→A #{i+1}")
        time.sleep(0.5)

# Run both threads simultaneously
thread_a = threading.Thread(target=device_a_communication)
thread_b = threading.Thread(target=device_b_communication)

print("Starting Full-Duplex Communication:")
thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
print("Communication complete!")
```

### 2.5 Comparison of Transmission Modes

| Feature | Simplex | Half-Duplex | Full-Duplex |
|---------|---------|-------------|-------------|
| **Direction** | One-way | Alternating two-way | Simultaneous two-way |
| **Bandwidth Efficiency** | 50% (one direction) | ~75% | 100% |
| **Cost** | Lowest | Moderate | Highest |
| **Complexity** | Simple | Moderate | Complex |
| **Examples** | Keyboard, TV | Walkie-Talkie, old Ethernet | Telephone, modern Wi-Fi |
| **Delay** | None | High (wait time) | None |

---

## 3. Network Devices

Network devices (also called networking hardware or network equipment) are physical devices that allow computers and other devices to communicate with each other. Each device operates at specific layers of the OSI model and serves distinct purposes.

### 3.1 Network Interface Card (NIC)

The **Network Interface Card (NIC)** is the fundamental hardware component that enables a computer to connect to a network. Every device on a network has a unique MAC (Media Access Control) address assigned to its NIC.

**Characteristics:**
- Operates at Data Link Layer (Layer 2)
- Provides unique MAC address (48-bit)
- Types: Ethernet NIC, Wireless NIC, Fiber NIC
- Speed ratings: 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps

**Real-World Example:**
```python
# Simulating NIC Address Representation
class NIC:
    def __init__(self, mac_address, connection_type="Ethernet"):
        self.mac_address = mac_address  # Format: XX:XX:XX:XX:XX:XX
        self.connection_type = connection_type
        self.status = "disconnected"
    
    def connect(self):
        self.status = "connected"
        print(f"NIC {self.mac_address} ({self.connection_type}): Connected")
    
    def disconnect(self):
        self.status = "disconnected"
        print(f"NIC {self.mac_address}: Disconnected")
    
    def send_frame(self, data, destination_mac):
        if self.status == "connected":
            print(f"Sending frame from {self.mac_address} to {destination_mac}")
            return f"Frame: {data}"
        else:
            print("Error: NIC not connected")
    
    def receive_frame(self, frame):
        print(f"NIC {self.mac_address} received: {frame}")

# Demonstration
nic1 = NIC("00:1A:2B:3C:4D:5E", "Gigabit Ethernet")
nic2 = NIC("AA:BB:CC:DD:EE:FF", "Gigabit Ethernet")

nic1.connect()
frame = nic1.send_frame("Hello Network", "AA:BB:CC:DD:EE:FF")
nic2.receive_frame(frame)
```

### 3.2 Repeater

A **repeater** is a network device that amplifies or regenerates weak or corrupted signals to extend the network's reach. It operates at the Physical Layer (Layer 1).

**Purpose:**
- Extends the maximum cable length
- Amplifies degraded signals
- Connects two network segments
- Does not filter or direct traffic

**Real-World Example:**
- Using a repeater to extend Ethernet cable beyond the 100-meter limit
- Wireless repeaters to extend Wi-Fi coverage in large buildings

```
[Computer]----100m----[Repeater]----100m----[Switch]
               (signal                    (regenerated
                weakening)                 signal)
```

### 3.3 Hub

A **hub** is a basic networking device that connects multiple computers in a network. It operates at the Physical Layer (Layer 1) and simply broadcasts incoming data to all connected ports.

**Characteristics:**
- Operates at Physical Layer
- No intelligence in packet forwarding
- Creates a single collision domain
- All devices share bandwidth
- Also known as "multiport repeater"

**Disadvantages:**
- Inefficient (unnecessary transmissions)
- Security concerns (all devices see all data)
- Collision domain issues
- Limited scalability

```
       ┌──────┐
       │ HUB  │
  ┌────┤      ├────┐
  │    │      │    │
[PC1] [PC2]  [PC3] [PC4]

Data from PC1 → Broadcasts to PC2, PC3, PC4
```

### 3.4 Bridge

A **bridge** connects two network segments and intelligently forwards traffic based on MAC addresses. It operates at the Data Link Layer (Layer 2).

**Characteristics:**
- Filters traffic based on MAC addresses
- Creates separate collision domains
- Learns device locations dynamically
- Reduces unnecessary traffic

**Working Principle:**
- When a frame arrives, the bridge checks the destination MAC address
- If destination is on the same segment, it's filtered
- If destination is on different segment, it's forwarded

### 3.5 Switch

A **switch** is an intelligent device that connects devices within a network and uses MAC addresses to forward data only to the intended destination. It operates at the Data Link Layer (Layer 2).

**Characteristics:**
- Operates at Data Link Layer
- Creates separate collision domains (microsegmentation)
- Learns MAC addresses dynamically (MAC address table)
- Full-duplex communication
- Much more efficient than hubs

**MAC Address Table (Switching Table):**

| Port | MAC Address | Device |
|------|-------------|--------|
| 1 | 00:1A:2B:3C:4D:5E | PC1 |
| 2 | AA:BB:CC:DD:EE:FF | PC2 |
| 3 | 11:22:33:44:55:66 | PC3 |
| 4 | 00:AA:BB:CC:DD:EE | Server |

**Technical Implementation:**

```python
class NetworkSwitch:
    def __init__(self, num_ports=4):
        self.num_ports = num_ports
        self.mac_table = {}  # MAC address to port mapping
        self.ports = {i: None for i in range(1, num_ports + 1)}
    
    def learn_mac(self, mac_address, port):
        """Learn which MAC address is on which port"""
        self.mac_table[mac_address] = port
        print(f"Learned: MAC {mac_address} is on Port {port}")
    
    def forward_frame(self, source_mac, destination_mac, incoming_port):
        """Forward frame based on MAC table"""
        # Learn source MAC address
        self.learn_mac(source_mac, incoming_port)
        
        # Check if destination MAC is known
        if destination_mac in self.mac_table:
            dest_port = self.mac_table[destination_mac]
            if dest_port != incoming_port:
                print(f"Forwarding frame from Port {incoming_port} to Port {dest_port}")
            else:
                print(f"Filtering: Destination on same port as source")
        else:
            # Flood if unknown (broadcast)
            print(f"Flooding: Unknown destination, broadcasting to all ports except {incoming_port}")
    
    def display_table(self):
        print("\n--- MAC Address Table ---")
        for mac, port in self.mac_table.items():
            print(f"Port {port}: {mac}")

# Demonstration
switch = NetworkSwitch(num_ports=4)

# Simulate network traffic
print("Frame 1: PC1 (00:1A:2B:3C:4D:5E) to PC2 (AA:BB:CC:DD:EE:FF)")
switch.forward_frame("00:1A:2B:3C:4D:5E", "AA:BB:CC:DD:EE:FF", 1)

print("\nFrame 2: PC2 (AA:BB:CC:DD:EE:FF) to PC1 (00:1A:2B:3C:4D:5E)")
switch.forward_frame("AA:BB:CC:DD:EE:FF", "00:1A:2B:3C:4D:5E", 2)

switch.display_table()
```

### 3.6 Router

A **router** connects different networks and directs traffic between them based on IP addresses. It operates at the Network Layer (Layer 3).

**Characteristics:**
- Operates at Network Layer
- Connects different networks (LAN to LAN, LAN to WAN)
- Uses IP addresses for routing decisions
- Creates broadcast domains
- Implements routing protocols

**Real-World Example:**
- Home router connecting LAN to Internet (WAN)
- Enterprise routers connecting different office networks

**Routing Table Example:**

| Destination Network | Next Hop | Interface |
|---------------------|----------|-----------|
| 192.168.1.0/24 | Direct | eth0 |
| 10.0.0.0/8 | 192.168.1.1 | eth1 |
| 0.0.0.0/0 | ISP_Gateway | eth0 |

### 3.7 Gateway

A **gateway** connects networks that use different protocols or architectures. It operates at all layers of the OSI model and performs protocol conversion.

**Characteristics:**
- Connects dissimilar networks
- Performs protocol translation
- Often combines router and other device functions
- Used for LAN to WAN connections
- Essential for internet connectivity

**Examples:**
- Email gateway (converts different email formats)
- VoIP gateway (converts voice to IP packets)
- Home gateway (router + modem combination)

### 3.8 Modem

A **modem** (Modulator-Demodulator) converts digital data from computers to analog signals for transmission over telephone or cable lines, and vice versa.

**Types:**
- **Dial-up Modem**: Converts to audio signals for telephone lines
- **Cable Modem**: Uses cable television infrastructure
- **DSL Modem**: Uses telephone lines for digital data
- **Optical Network Terminal (ONT)**: Fiber optic modems

**Purpose:**
- Internet connectivity
- Signal conversion (digital ↔ analog/wave)
- Bridge between local network and ISP

### 3.9 Access Point (AP)

An **Access Point** allows wireless devices to connect to a wired network using Wi-Fi.

**Characteristics:**
- Operates at Data Link Layer
- Converts wired Ethernet to wireless signals
- Supports multiple simultaneous connections
- Implements wireless security (WPA, WPA2, WPA3)
- Can function as standalone or as part of WLAN controller

### 3.10 Firewall

A **firewall** is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.

**Characteristics:**
- Operates at Network Layer and above
- Filters traffic based on rules
- Protects against unauthorized access
- Types: Hardware, Software, Cloud-based

---

## 4. OSI Model Layer Summary for Network Devices

| OSI Layer | Devices |
|-----------|---------|
| **Layer 1: Physical** | Hub, Repeater, Cable, NIC |
| **Layer 2: Data Link** | Switch, Bridge, NIC |
| **Layer 3: Network** | Router |
| **Layer 4: Transport** | Gateway (with translation) |
| **Layer 7: Application** | Gateway, Firewall |

---

## 5. Assessment Questions

### 5.1 Multiple Choice Questions

**Level 1: Basic (Easy)**

1. In which transmission mode can data flow in both directions simultaneously?
   - a) Simplex
   - b) Half-Duplex
   - c) Full-Duplex
   - d) Multi-Duplex

2. Which device operates at the Physical Layer (Layer 1) of the OSI model?
   - a) Switch
   - b) Router
   - c) Hub
   - d) Bridge

3. What is the unique address assigned to a Network Interface Card?
   - a) IP Address
   - b) MAC Address
   - c) Port Number
   - d) Subnet Mask

**Level 2: Intermediate**

4. A switch creates separate _____ domains, while a router creates separate _____ domains.
   - a) Broadcast, Collision
   - b) Collision, Broadcast
   - c) Network, Subnet
   - d) Domain, Segment

5. Which device would you use to connect a home network to the Internet?
   - a) Hub
   - b) Switch
   - c) Gateway/Router
   - d) Repeater

6. In half-duplex communication, if device A is transmitting, device B:
   - a) Can also transmit simultaneously
   - b) Must wait until A finishes
   - c) Can receive only
   - d) Cannot send or receive

**Level 3: Advanced (Challenging)**

7. A bridge learns MAC addresses dynamically. When it receives a frame with an unknown destination MAC, it:
   - a) Drops the frame
   - b) Forwards to all ports except the source
   - c) Forwards to the specific port in its table
   - d) Sends an ARP request

8. Which of the following is NOT a function of a router?
   - a) Path determination
   - b) Packet forwarding
   - c) Collision detection
   - d) Connecting different networks

9. In a network with 4 computers connected via a hub, if computer A sends data to computer B, which computers will receive the data?
   - a) Only Computer B
   - b) Only Computers B, C, and D
   - c) All computers
   - d) Only Computers A and B

10. A repeater is used to:
    - a) Filter traffic based on MAC addresses
    - b) Connect two different network protocols
    - c) Amplify weak signals and extend network distance
    - d) Provide wireless connectivity

### 5.2 Short Answer Questions

1. Differentiate between a hub and a switch with respect to collision domains and bandwidth utilization.

2. Explain why full-duplex communication requires more complex hardware than half-duplex.

3. Describe the function of a MAC address table in a network switch.

4. Why is a router considered more intelligent than a hub or switch?

5. Give two practical examples each for simplex, half-duplex, and full-duplex transmission modes.

### 5.3 Long Answer Questions

1. **Explain the three types of transmission modes in computer networks with suitable examples. Also, discuss the advantages and disadvantages of each mode.**

2. **Describe the functions of the following network devices: Repeater, Hub, Bridge, Switch, Router, and Gateway. Also mention the OSI layer at which each device operates.**

3. **With the help of a diagram, explain how a switch forwards frames based on MAC addresses. Include the concept of MAC address learning and flooding.**

4. **Compare and contrast a hub, a switch, and a router in terms of:
   - OSI Layer of operation
   - Collision domains created
   - Broadcast domains
   - Intelligent decision-making
   - Typical use cases**

---

## 6. Flashcards

### Set 1: Transmission Modes

| Term | Definition |
|------|------------|
| **Simplex Mode** | Communication in one direction only; one device transmits, the other only receives |
| **Half-Duplex Mode** | Communication in both directions but not simultaneously; devices take turns |
| **Full-Duplex Mode** | Simultaneous bidirectional communication; both devices can send and receive at once |
| **Bandwidth Utilization** | The percentage of available bandwidth actively used for data transmission |

### Set 2: Network Devices

| Term | Definition |
|------|------------|
| **NIC (Network Interface Card)** | Hardware component that enables a device to connect to a network; has a unique MAC address |
| **Repeater** | Layer 1 device that amplifies/regenerates network signals to extend cable length |
| **Hub** | Layer 1 device that broadcasts incoming data to all connected ports; creates single collision domain |
| **Bridge** | Layer 2 device that connects two network segments and filters traffic based on MAC addresses |
| **Switch** | Layer 2 device that connects devices within a network; forwards data only to destination port using MAC table |
| **Router** | Layer 3 device that connects different networks and directs traffic based on IP addresses |
| **Gateway** | Device that connects networks using different protocols; performs protocol translation |
| **Modem** | Device that converts digital data to analog signals for transmission over analog lines |
| **Access Point** | Device that allows wireless devices to connect to a wired network |
| **Firewall** | Security device that monitors and controls network traffic based on security rules |

### Set 3: Key Concepts

| Term | Definition |
|------|------------|
| **MAC Address** | 48-bit unique hardware address assigned to NIC; expressed as six pairs of hexadecimal digits |
| **Collision Domain** | Network segment where collisions can occur; hubs create one collision domain per network |
| **Broadcast Domain** | Network segment where broadcast messages reach all devices; routers separate broadcast domains |
| **MAC Address Table** | Switch's internal table mapping MAC addresses to specific ports |
| **Flooding** | Switch forwards frame to all ports except source when destination is unknown |

---

## 7. Key Takeaways

### Transmission Modes
- **Simplex** is unidirectional—ideal for input devices like keyboards where only data entry occurs
- **Half-Duplex** allows two-way communication but not simultaneously—used in walkie-talkies and traditional Ethernet
- **Full-Duplex** enables simultaneous bidirectional communication—standard in modern networks, telephones, and video conferencing
- The choice of transmission mode impacts network design, hardware requirements, and cost

### Network Devices Summary
1. **NIC**: The fundamental building block connecting devices to networks
2. **Repeater**: Extends network distance by amplifying signals
3. **Hub**: Basic connectivity device (largely obsolete due to inefficiency)
4. **Bridge**: Intelligent segment connector using MAC addresses
5. **Switch**: Modern standard for LAN connectivity—creates separate collision domains
6. **Router**: Connects different networks and directs traffic based on IP addresses
7. **Gateway**: Protocol converter for dissimilar network architectures
8. **Modem**: Converts between digital and analog for remote connectivity

### Critical Relationships
- **Switches** have replaced **hubs** in modern networks due to efficiency
- **Routers** operate at Layer 3, creating separate **broadcast domains**
- **Switches** operate at Layer 2, creating separate **collision domains**
- Full-duplex communication eliminates collisions entirely

### Exam Tips
- Remember the OSI layer for each device—this is frequently tested
- Know the difference between collision and broadcast domains
- Be able to draw and explain switch MAC address table learning
- Understand why full-duplex is preferred over half-duplex in modern networking
- Know real-world examples for each transmission mode

---

*This study material covers the complete syllabus requirements for "Transmission Modes and Network Devices" as per Delhi University NEP 2024 UGCF BSc (Hons) Computer Science curriculum.*